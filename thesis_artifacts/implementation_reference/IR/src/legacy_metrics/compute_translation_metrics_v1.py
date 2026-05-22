from __future__ import annotations

import argparse
import itertools
import json
import math
import os
import re
from collections import Counter
from datetime import datetime
from pathlib import Path
import statistics
from types import SimpleNamespace
from typing import Any

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent))

import run_advisor_drafter_experiment as ir_stage
import run_questioner_answerer_to_ir_experiment as qa_stage


ROOT_DIR = Path(__file__).resolve().parents[3] / "IR" / "index" / "legacy_metric_resources"

# a4v3 surface syntax tokens — sourced from canonical spec via a4v3_grammar.
# Previously hardcoded (28 tokens, missing temporal/deontic keywords like
# `prop`, `eventually`, `obligation`, etc., causing content_token metrics
# to false-positive on those keywords).
def _load_ir_syntax_tokens() -> frozenset[str]:
    import sys as _sys, pathlib as _pathlib
    _sys.path.insert(0, str(_pathlib.Path(__file__).parent.parent))
    from a4v3_grammar import all_keywords  # noqa: E402
    extras = frozenset({
        # additional carrier-type / built-in primitives that aren't in the
        # spec's family-keyword tables but appear in IR text as type names.
        "bool", "int", "nat", "rational", "string",
        # legacy AST shape keywords (canonical_ast_v1 form)
        "call", "ref",
    })
    return all_keywords() | extras


_IR_SYNTAX_TOKENS: frozenset[str] = _load_ir_syntax_tokens()

_STOPWORDS = {
    "a",
    "an",
    "the",
    "of",
    "in",
    "on",
    "at",
    "to",
    "for",
    "by",
    "or",
    "and",
    "if",
    "is",
    "are",
    "be",
    "as",
    "with",
    "that",
    "this",
    "it",
    "its",
    "into",
    "from",
    "which",
    "every",
    "each",
}

_RELATION_FUSION_CUES = {
    "responsible",
    "responsibility",
    "determination",
    "determine",
    "determined",
    "included",
    "including",
    "following",
    "preceding",
    "open",
    "opened",
    "stored",
    "used",
    "using",
    "cease",
    "ceased",
    "capture",
    "captures",
}

_CONDITIONAL_PACKING_CUES = {
    "if",
    "would",
    "had",
    "not",
    "before",
    "prior",
    "following",
    "immediately",
    "unless",
    "but",
    "occurred",
    "occurring",
}

_CONFIDENCE_TO_SCORE = {
    "low": 0.33,
    "medium": 0.66,
    "high": 1.0,
}

_SILVER_REFERENCE_MD = (
    Path(__file__).resolve().parents[3] / "IR" / "outputs" / "runs"
    / "silver_baseline" / "definitions_full6_multivariant_critic_v1_with_gold.md"
)
# Subset of top-level decls used by the structure-token check (legacy: 6 forms).
# Sourced from the canonical spec via family_block_keywords for TypeDecl,
# SymbolDecl (selected: entity, fun, rel) and AssertDecl (selected: constraint, fact).
def _load_structure_top_level() -> tuple[str, ...]:
    import sys as _sys, pathlib as _pathlib
    _sys.path.insert(0, str(_pathlib.Path(__file__).parent.parent))
    from a4v3_grammar import family_block_keywords  # noqa: E402
    # Match the legacy 6-form subset: type+selected symbol+selected assert.
    type_kws = set(family_block_keywords("TypeDecl"))    # sort, struct
    sym_kws = {"entity", "fun", "rel"}                    # subset of SymbolDecl
    asrt_kws = {"constraint", "fact"}                      # subset of AssertDecl
    out = ("sort",)  # legacy order: sort first; struct dropped from this view
    out += ("entity", "fun", "rel", "constraint", "fact")
    return out


_STRUCTURE_TOP_LEVEL: tuple[str, ...] = _load_structure_top_level()
_STRUCTURE_LOGIC = ("forall", "exists", "and", "or", "not", "implies", "iff")


def _save_json(path: Path, payload: Any) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def _manual_reference_payload(payload: dict[str, Any]) -> dict[str, Any]:
    candidate = payload.get("manual_reference", {}) or payload.get("reference_override", {}) or {}
    return candidate if isinstance(candidate, dict) else {}


def _manual_reference_clauses(reference: dict[str, Any]) -> list[str]:
    raw = reference.get("manual_normalized_clauses")
    if not isinstance(raw, list):
        raw = reference.get("normalized_clauses")
    if isinstance(raw, list):
        return [str(item).strip() for item in raw if str(item).strip()]
    text_value = str(
        reference.get("manual_normalized_text")
        or reference.get("normalized_text")
        or ""
    ).strip()
    if not text_value:
        return []
    return [line.strip() for line in text_value.splitlines() if line.strip()]


def _effective_reference_context(
    ctx: ir_stage.ExperimentContext,
    payload: dict[str, Any],
) -> tuple[Any, bool]:
    reference = _manual_reference_payload(payload)
    disable_silver_reference = bool(
        payload.get("disable_silver_reference", False)
        or reference.get("disable_silver_reference", False)
    )
    if not reference:
        return ctx, disable_silver_reference

    entry = dict(ctx.entry)
    source_excerpt = str(
        reference.get("mutated_text")
        or reference.get("source_excerpt")
        or entry.get("source_excerpt", "")
        or ""
    ).strip()
    normalized_clauses = _manual_reference_clauses(reference)
    source_term = str(
        reference.get("source_term")
        or reference.get("focus_term")
        or entry.get("source_term", "")
        or ""
    ).strip()

    if source_excerpt:
        entry["source_excerpt"] = source_excerpt
        entry["raw_source_excerpt"] = source_excerpt
    if normalized_clauses:
        entry["normalized_clauses"] = normalized_clauses
    if source_term:
        entry["source_term"] = source_term
    if reference.get("source_spans") is not None:
        entry["source_spans"] = reference.get("source_spans")

    return (
        SimpleNamespace(
            entry=entry,
            prelude_json=ctx.prelude_json,
        ),
        disable_silver_reference,
    )


def _word_tokens(text: str) -> list[str]:
    if not isinstance(text, str):
        return []
    return [token.lower() for token in re.findall(r"[A-Za-z][A-Za-z0-9_-]*", text)]


def _content_tokens(text: str, focus_term: str = "") -> list[str]:
    focus_words = {token.lower() for token in re.findall(r"[A-Za-z][A-Za-z-]{2,}", focus_term or "")}
    tokens: list[str] = []
    for raw in _word_tokens(text):
        pieces = ir_stage._split_identifier_tokens(raw) or [raw.lower()]
        for token in pieces:
            token = token.lower()
            if token in _STOPWORDS or token in focus_words or token in _IR_SYNTAX_TOKENS or len(token) < 4:
                continue
            tokens.append(token)
    return tokens


def _unique_preserve_order(tokens: list[str]) -> list[str]:
    seen: set[str] = set()
    unique: list[str] = []
    for token in tokens:
        if token in seen:
            continue
        seen.add(token)
        unique.append(token)
    return unique


def _content_token_set(text: str, focus_term: str = "") -> list[str]:
    return _unique_preserve_order(_content_tokens(text, focus_term))


def _content_token_counter(text: str, focus_term: str = "") -> Counter[str]:
    return Counter(_content_tokens(text, focus_term))


def _identifier_pieces(name: str, *, content_only: bool = False) -> list[str]:
    pieces = [piece.lower() for piece in (ir_stage._split_identifier_tokens(name) or [str(name).strip().lower()]) if piece]
    if not content_only:
        return pieces
    return [
        piece
        for piece in pieces
        if piece not in _STOPWORDS and piece not in _IR_SYNTAX_TOKENS and len(piece) >= 3
    ]


def _identifier_piece_lexicon(
    *,
    ctx: ir_stage.ExperimentContext,
    advisory: dict[str, Any],
    focus_term: str,
    include_advisory: bool,
) -> set[str]:
    parts: list[str] = []
    parts.extend(_word_tokens(str(ctx.entry.get("source_term", "") or "")))
    parts.extend(_word_tokens(str(ctx.entry.get("source_excerpt", "") or "")))
    parts.extend(_word_tokens(" ".join(str(item) for item in ctx.entry.get("normalized_clauses", []) if isinstance(item, str))))
    for item in ctx.prelude_json.get("sorts", []) or []:
        if isinstance(item, dict):
            parts.extend(_identifier_pieces(str(item.get("name", "") or ""), content_only=True))
    for item in ctx.prelude_json.get("entities", []) or []:
        if isinstance(item, dict):
            parts.extend(_identifier_pieces(str(item.get("name", "") or ""), content_only=True))
    for item in ctx.prelude_json.get("functions", []) or []:
        if isinstance(item, dict):
            parts.extend(_identifier_pieces(str(item.get("name", "") or ""), content_only=True))
    for item in ctx.prelude_json.get("relations", []) or []:
        if isinstance(item, dict):
            parts.extend(_identifier_pieces(str(item.get("name", "") or ""), content_only=True))
    if include_advisory:
        parts.extend(_word_tokens(json.dumps(advisory, ensure_ascii=False)))
    focus_words = {token.lower() for token in re.findall(r"[A-Za-z][A-Za-z-]{2,}", focus_term or "")}
    return {
        part
        for part in parts
        if part not in _STOPWORDS and part not in _IR_SYNTAX_TOKENS and len(part) >= 3 and part not in focus_words
    }


def _walk_expr_names(expr: Any, acc: list[str]) -> None:
    if not isinstance(expr, dict):
        return
    kind = str(expr.get("kind", "")).strip()
    if kind == "ref":
        name = str(expr.get("name", "") or "").strip()
        if name:
            acc.append(name)
    elif kind == "call":
        callee = str(expr.get("callee", "") or "").strip()
        if callee:
            acc.append(callee)
        for arg in expr.get("args", []) or []:
            _walk_expr_names(arg, acc)
    elif kind in {"eq", "implies", "iff"}:
        _walk_expr_names(expr.get("left"), acc)
        _walk_expr_names(expr.get("right"), acc)
    elif kind in {"not"}:
        _walk_expr_names(expr.get("arg"), acc)
    elif kind in {"and", "or"}:
        for arg in expr.get("args", []) or []:
            _walk_expr_names(arg, acc)
    elif kind in {"forall", "exists"}:
        for item in expr.get("vars", []) or []:
            if isinstance(item, dict):
                name = str(item.get("name", "") or "").strip()
                sort = str(item.get("sort", "") or "").strip()
                if name:
                    acc.append(name)
                if sort:
                    acc.append(sort)
        _walk_expr_names(expr.get("body"), acc)
    elif kind == "ite":
        _walk_expr_names(expr.get("cond"), acc)
        _walk_expr_names(expr.get("then"), acc)
        _walk_expr_names(expr.get("else"), acc)
    elif kind == "let":
        for item in expr.get("bindings", []) or []:
            if isinstance(item, dict):
                name = str(item.get("name", "") or "").strip()
                if name:
                    acc.append(name)
                _walk_expr_names(item.get("value"), acc)
        _walk_expr_names(expr.get("body"), acc)


def _collect_named_ir_identifiers(ir_ast: dict[str, Any]) -> list[str]:
    names: list[str] = []
    for item in ir_ast.get("declarations", []) or []:
        if not isinstance(item, dict):
            continue
        for key in ("name", "sort", "result_sort"):
            value = str(item.get(key, "") or "").strip()
            if value:
                names.append(value)
        for arg in item.get("args", []) or []:
            value = str(arg or "").strip()
            if value:
                names.append(value)
    for item in ir_ast.get("assertions", []) or []:
        if not isinstance(item, dict):
            continue
        name = str(item.get("name", "") or "").strip()
        if name:
            names.append(name)
        _walk_expr_names(item.get("expr"), names)
    unique: list[str] = []
    seen: set[str] = set()
    for name in names:
        norm = ir_stage._normalized_identifier(name)
        if not norm or norm in seen:
            continue
        seen.add(norm)
        unique.append(name)
    return unique


def _identifier_glue_metrics(
    *,
    ir_ast: dict[str, Any],
    ctx: ir_stage.ExperimentContext,
    advisory: dict[str, Any],
    focus_term: str,
) -> dict[str, Any]:
    identifiers = _collect_named_ir_identifiers(ir_ast)
    source_lexicon = _identifier_piece_lexicon(ctx=ctx, advisory=advisory, focus_term=focus_term, include_advisory=False)
    advisory_lexicon = _identifier_piece_lexicon(ctx=ctx, advisory=advisory, focus_term=focus_term, include_advisory=True)
    rows: list[dict[str, Any]] = []
    for name in identifiers:
        raw_pieces = _identifier_pieces(name, content_only=False)
        content_pieces = _identifier_pieces(name, content_only=True)
        grounded_source = sum(1 for piece in content_pieces if piece in source_lexicon)
        grounded_advisory = sum(1 for piece in content_pieces if piece in advisory_lexicon)
        rows.append(
            {
                "identifier": name,
                "raw_piece_count": len(raw_pieces),
                "content_piece_count": len(content_pieces),
                "raw_pieces": raw_pieces,
                "content_pieces": content_pieces,
                "glue_excess_raw": max(0, len(raw_pieces) - 3),
                "glue_excess_content": max(0, len(content_pieces) - 2),
                "source_grounded_content_piece_count": grounded_source,
                "advisory_grounded_content_piece_count": grounded_advisory,
                "source_grounded_content_piece_ratio": (
                    grounded_source / len(content_pieces) if content_pieces else 1.0
                ),
                "advisory_grounded_content_piece_ratio": (
                    grounded_advisory / len(content_pieces) if content_pieces else 1.0
                ),
            }
        )
    raw_piece_counts = [row["raw_piece_count"] for row in rows]
    content_piece_counts = [row["content_piece_count"] for row in rows]
    identifier_count = len(rows)
    compound_identifier_count_raw = sum(1 for row in rows if row["raw_piece_count"] >= 4)
    compound_identifier_count_content = sum(1 for row in rows if row["content_piece_count"] >= 3)
    identifier_glue_excess_mass_raw = int(sum(row["glue_excess_raw"] for row in rows))
    identifier_glue_excess_mass_content = int(sum(row["glue_excess_content"] for row in rows))
    low_source_grounded_glued_identifier_count = sum(
        1
        for row in rows
        if row["content_piece_count"] >= 3 and float(row["source_grounded_content_piece_ratio"]) < 0.67
    )
    top_examples = sorted(
        rows,
        key=lambda row: (
            -int(row["glue_excess_content"]),
            -int(row["glue_excess_raw"]),
            float(row["source_grounded_content_piece_ratio"]),
            -int(row["content_piece_count"]),
            str(row["identifier"]).lower(),
        ),
    )[:20]
    low_grounding_examples = [
        row
        for row in sorted(
            rows,
            key=lambda row: (
                float(row["source_grounded_content_piece_ratio"]),
                -int(row["content_piece_count"]),
                str(row["identifier"]).lower(),
            ),
        )
        if row["content_piece_count"] >= 2
    ][:20]
    relation_fused_examples = [
        row
        for row in rows
        if row["content_piece_count"] >= 4
        and any(piece in _RELATION_FUSION_CUES for piece in row["content_pieces"])
        and len([piece for piece in row["content_pieces"] if piece not in _RELATION_FUSION_CUES]) >= 2
    ]
    conditional_packing_examples = [
        row
        for row in rows
        if row["raw_piece_count"] >= 5
        and any(piece in _CONDITIONAL_PACKING_CUES for piece in row["raw_pieces"])
        and row["content_piece_count"] >= 3
    ]
    return {
        "identifier_count": identifier_count,
        "compound_identifier_count_raw": compound_identifier_count_raw,
        "compound_identifier_count_content": compound_identifier_count_content,
        "compound_identifier_rate_raw": (
            compound_identifier_count_raw / identifier_count if identifier_count else None
        ),
        "compound_identifier_rate_content": (
            compound_identifier_count_content / identifier_count if identifier_count else None
        ),
        "max_identifier_piece_count_raw": max(raw_piece_counts) if raw_piece_counts else 0,
        "max_identifier_piece_count_content": max(content_piece_counts) if content_piece_counts else 0,
        "mean_identifier_piece_count_raw": (statistics.mean(raw_piece_counts) if raw_piece_counts else 0.0),
        "mean_identifier_piece_count_content": (
            statistics.mean(content_piece_counts) if content_piece_counts else 0.0
        ),
        "identifier_glue_excess_mass_raw": identifier_glue_excess_mass_raw,
        "identifier_glue_excess_mass_content": identifier_glue_excess_mass_content,
        "identifier_glue_excess_rate_raw": (
            identifier_glue_excess_mass_raw / identifier_count if identifier_count else None
        ),
        "identifier_glue_excess_rate_content": (
            identifier_glue_excess_mass_content / identifier_count if identifier_count else None
        ),
        "source_grounded_content_piece_ratio_mean": (
            statistics.mean(float(row["source_grounded_content_piece_ratio"]) for row in rows) if rows else 1.0
        ),
        "advisory_grounded_content_piece_ratio_mean": (
            statistics.mean(float(row["advisory_grounded_content_piece_ratio"]) for row in rows) if rows else 1.0
        ),
        "low_source_grounded_glued_identifier_count": low_source_grounded_glued_identifier_count,
        "low_source_grounded_glued_identifier_rate": (
            low_source_grounded_glued_identifier_count / identifier_count if identifier_count else None
        ),
        "entity_relation_target_fusion_count": len(relation_fused_examples),
        "entity_relation_target_fusion_rate": (
            len(relation_fused_examples) / identifier_count if identifier_count else None
        ),
        "conditional_relation_name_packing_count": len(conditional_packing_examples),
        "conditional_relation_name_packing_rate": (
            len(conditional_packing_examples) / identifier_count if identifier_count else None
        ),
        "top_glued_identifiers": top_examples,
        "lowest_source_grounded_identifiers": low_grounding_examples,
        "entity_relation_target_fusion_examples": relation_fused_examples[:20],
        "conditional_relation_name_packing_examples": conditional_packing_examples[:20],
    }


def _counter_overlap(left: Counter[str], right: Counter[str]) -> int:
    keys = set(left) | set(right)
    return sum(min(left.get(key, 0), right.get(key, 0)) for key in keys)


def _overuse_examples(current: Counter[str], baseline: Counter[str], top_k: int = 20) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for token in sorted(set(current) | set(baseline)):
        current_count = int(current.get(token, 0))
        baseline_count = int(baseline.get(token, 0))
        delta = current_count - baseline_count
        if delta > 0:
            rows.append(
                {
                    "token": token,
                    "current_count": current_count,
                    "baseline_count": baseline_count,
                    "delta": delta,
                }
            )
    rows.sort(key=lambda item: (-item["delta"], -item["current_count"], item["token"]))
    return rows[:top_k]


def _repeat_metrics(current: Counter[str], baseline: Counter[str]) -> dict[str, Any]:
    overuse = {token: current[token] - baseline.get(token, 0) for token in current if current[token] > baseline.get(token, 0)}
    underuse = {token: baseline[token] - current.get(token, 0) for token in baseline if baseline[token] > current.get(token, 0)}
    overlap = _counter_overlap(current, baseline)
    current_total = sum(current.values())
    baseline_total = sum(baseline.values())
    return {
        "multiset_recall": (overlap / baseline_total) if baseline_total else 1.0,
        "multiset_precision": (overlap / current_total) if current_total else 1.0,
        "repeat_overuse_token_count": len(overuse),
        "repeat_overuse_mass": int(sum(overuse.values())),
        "repeat_underuse_token_count": len(underuse),
        "repeat_underuse_mass": int(sum(underuse.values())),
        "repeat_overuse_examples": _overuse_examples(current, baseline),
    }


def _assistant_turn_count(raw_messages: Any) -> int:
    if not isinstance(raw_messages, list):
        return 0
    count = 0
    for item in raw_messages:
        if isinstance(item, dict) and str(item.get("role", "")).strip() == "assistant":
            count += 1
    return count


def _normalize_whitespace(text: str) -> str:
    return re.sub(r"\s+", " ", str(text or "")).strip()


def _humanize_identifier(name: str) -> str:
    pieces = ir_stage._split_identifier_tokens(name) or [str(name).strip()]
    return " ".join(piece.lower() for piece in pieces if piece).strip()


def _oxford_join(items: list[str], conj: str = "and") -> str:
    values = [item for item in items if item]
    if not values:
        return ""
    if len(values) == 1:
        return values[0]
    if len(values) == 2:
        return f"{values[0]} {conj} {values[1]}"
    return f"{', '.join(values[:-1])}, {conj} {values[-1]}"


def _verbalize_term(expr: Any) -> str:
    if not isinstance(expr, dict):
        return str(expr)
    kind = str(expr.get("kind", "")).strip()
    if kind == "ref":
        return _humanize_identifier(str(expr.get("name", "") or "value"))
    if kind in {"literal", "lit"}:
        value = expr.get("value", "")
        return _humanize_identifier(str(value)) if isinstance(value, str) else str(value)
    if kind == "call":
        callee = _humanize_identifier(str(expr.get("callee", "") or "predicate"))
        args = [_verbalize_term(arg) for arg in expr.get("args", [])]
        if args:
            return f"{callee} for {_oxford_join(args)}"
        return callee
    if kind == "not":
        return f"not ({_verbalize_term(expr.get('arg'))})"
    if kind == "and":
        args = [_verbalize_term(arg) for arg in expr.get("args", []) if isinstance(arg, dict)]
        return "(" + _oxford_join(args, "and") + ")"
    if kind == "or":
        args = [_verbalize_term(arg) for arg in expr.get("args", []) if isinstance(arg, dict)]
        return "(" + _oxford_join(args, "or") + ")"
    if kind == "eq":
        return f"{_verbalize_term(expr.get('left'))} equals {_verbalize_term(expr.get('right'))}"
    comparison_phrases = {
        "neq": "does not equal",
        "gt": "is greater than",
        "lt": "is less than",
        "gte": "is greater than or equal to",
        "lte": "is less than or equal to",
    }
    if kind in comparison_phrases:
        return (
            f"{_verbalize_term(expr.get('left'))} "
            f"{comparison_phrases[kind]} "
            f"{_verbalize_term(expr.get('right'))}"
        )
    if kind == "implies":
        return f"if {_verbalize_term(expr.get('left'))}, then {_verbalize_term(expr.get('right'))}"
    if kind == "iff":
        return (
            f"{_verbalize_term(expr.get('left'))} if and only if "
            f"{_verbalize_term(expr.get('right'))}"
        )
    if kind == "count":
        binder = expr.get("binder")
        if isinstance(binder, dict):
            name = _humanize_identifier(str(binder.get("name", "") or "item"))
            sort = _humanize_identifier(str(binder.get("sort", "") or "thing"))
            return (
                f"the number of {name} of type {sort} such that "
                f"{_verbalize_term(expr.get('predicate'))}"
            )
        return f"the count of items such that {_verbalize_term(expr.get('predicate'))}"
    if kind == "forall":
        vars_ = [
            f"{_humanize_identifier(str(item.get('name', '') or 'x'))} of type {_humanize_identifier(str(item.get('sort', '') or 'thing'))}"
            for item in expr.get("vars", [])
            if isinstance(item, dict)
        ]
        return f"for every {_oxford_join(vars_)}, {_verbalize_term(expr.get('body'))}"
    if kind == "exists":
        vars_ = [
            f"{_humanize_identifier(str(item.get('name', '') or 'x'))} of type {_humanize_identifier(str(item.get('sort', '') or 'thing'))}"
            for item in expr.get("vars", [])
            if isinstance(item, dict)
        ]
        return f"there exists {_oxford_join(vars_)}, {_verbalize_term(expr.get('body'))}"
    if kind == "ite":
        return (
            f"if {_verbalize_term(expr.get('cond'))}, then {_verbalize_term(expr.get('then'))}, "
            f"else {_verbalize_term(expr.get('else'))}"
        )
    if kind == "let":
        bindings = []
        for item in expr.get("bindings", []):
            if isinstance(item, dict):
                bindings.append(
                    f"{_humanize_identifier(str(item.get('name', '') or 'tmp'))} equals {_verbalize_term(item.get('value'))}"
                )
        return f"let {_oxford_join(bindings)}, then {_verbalize_term(expr.get('body'))}"
    return _humanize_identifier(kind or "expression")


def _verbalize_declaration(item: dict[str, Any]) -> str:
    decl = str(item.get("decl", "")).strip()
    if decl == "sort":
        return f"{_humanize_identifier(str(item.get('name', '') or 'type'))} is a type."
    if decl == "entity":
        return f"{_humanize_identifier(str(item.get('name', '') or 'entity'))} is a distinguished entity."
    if decl == "symbol":
        symbol_kind = str(item.get("symbol_kind", "")).strip()
        name = _humanize_identifier(str(item.get("name", "") or "symbol"))
        args = [_humanize_identifier(str(arg)) for arg in item.get("args", []) if str(arg).strip()]
        result_sort = _humanize_identifier(str(item.get("result_sort", "") or "value"))
        if symbol_kind == "fun":
            if args:
                return f"{name} maps {_oxford_join(args)} to {result_sort}."
            return f"{name} denotes a {result_sort}."
        if symbol_kind == "rel":
            if args:
                return f"{name} holds between {_oxford_join(args)}."
            return f"{name} is a proposition."
    return ""


def _verbalize_assertion(item: dict[str, Any]) -> str:
    kind = _humanize_identifier(str(item.get("assert_kind", "") or "assertion"))
    name = _humanize_identifier(str(item.get("name", "") or "rule"))
    expr = _verbalize_term(item.get("expr"))
    return f"{kind} {name} states that {expr}."


_TOP_LEVEL_A4V3_PREFIXES = (
    "sort ",
    "entity ",
    "rel ",
    "fun",
    "constraint ",
    "fact ",
    "prop ",
    "prohibition ",
    "obligation ",
    "permission ",
)


def _surface_block_value(block: str, key: str) -> str:
    match = re.search(rf"(?m)^\s*{re.escape(key)}\s*:\s*(.+?)\s*$", block)
    return match.group(1).strip() if match else ""


def _verbalize_deontic_surface(ir_text: str) -> list[str]:
    lines = str(ir_text or "").splitlines()
    out: list[str] = []
    idx = 0
    while idx < len(lines):
        stripped = lines[idx].strip()
        if not stripped.startswith("prohibition "):
            idx += 1
            continue

        block_lines = [lines[idx]]
        idx += 1
        while idx < len(lines):
            candidate = lines[idx]
            candidate_stripped = candidate.strip()
            if candidate_stripped and not candidate[:1].isspace():
                if any(candidate_stripped.startswith(prefix) for prefix in _TOP_LEVEL_A4V3_PREFIXES):
                    break
            block_lines.append(candidate)
            idx += 1

        block = "\n".join(block_lines)
        name_match = re.match(r"\s*prohibition\s+([A-Za-z_][A-Za-z0-9_]*)", block_lines[0])
        name = _humanize_identifier(name_match.group(1) if name_match else "prohibition")
        agent_match = re.search(r"(?m)^\s*agent\s*:\s*([A-Za-z_][A-Za-z0-9_]*)", block)
        agent = _humanize_identifier(agent_match.group(1) if agent_match else "agent")
        action = _humanize_identifier(_surface_block_value(block, "action") or "act")
        target = _humanize_identifier(_surface_block_value(block, "target") or "")
        scope = _humanize_identifier(_surface_block_value(block, "scope") or "")

        tail_parts = []
        if target:
            tail_parts.append(f"toward {target}")
        if scope:
            tail_parts.append(f"within {scope}")
        tail = f" {' '.join(tail_parts)}" if tail_parts else ""
        out.append(f"prohibition {name} states that {agent} is prohibited from {action}{tail}.")
    return out


def _render_back_from_ir_ast(ir_ast: dict[str, Any], focus_term: str = "", ir_text: str = "") -> str:
    if not isinstance(ir_ast, dict):
        return ""
    declaration_texts = [
        _verbalize_declaration(item)
        for item in ir_ast.get("declarations", [])
        if isinstance(item, dict)
    ]
    assertion_texts = [
        _verbalize_assertion(item)
        for item in ir_ast.get("assertions", [])
        if isinstance(item, dict)
    ]
    focus_norm = ir_stage._normalized_identifier(focus_term)
    prioritized_declarations: list[str] = []
    other_declarations: list[str] = []
    for item, text in zip(ir_ast.get("declarations", []), declaration_texts):
        if not text:
            continue
        if isinstance(item, dict) and focus_norm and ir_stage._normalized_identifier(str(item.get("name", ""))) == focus_norm:
            prioritized_declarations.append(text)
        else:
            other_declarations.append(text)
    deontic_texts = _verbalize_deontic_surface(ir_text)
    parts = prioritized_declarations + assertion_texts + deontic_texts + other_declarations
    return _normalize_whitespace(" ".join(part for part in parts if part))


def _safe_bertscore(candidate: str, reference: str) -> dict[str, float | None]:
    if not candidate.strip() or not reference.strip():
        return {"precision": None, "recall": None, "f1": None}
    os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")
    from bert_score import score

    precision, recall, f1 = score(
        [candidate],
        [reference],
        model_type="distilbert-base-uncased",
        verbose=False,
    )
    return {
        "precision": float(precision[0]),
        "recall": float(recall[0]),
        "f1": float(f1[0]),
    }


_NLI_BUNDLE: tuple[Any, Any] | None = None


def _load_nli_bundle() -> tuple[Any, Any]:
    global _NLI_BUNDLE
    if _NLI_BUNDLE is not None:
        return _NLI_BUNDLE
    os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")
    from transformers import AutoModelForSequenceClassification, AutoTokenizer

    tokenizer = AutoTokenizer.from_pretrained("cross-encoder/nli-distilroberta-base", local_files_only=True)
    model = AutoModelForSequenceClassification.from_pretrained(
        "cross-encoder/nli-distilroberta-base",
        local_files_only=True,
    )
    model.eval()
    _NLI_BUNDLE = (tokenizer, model)
    return _NLI_BUNDLE


def _nli_scores(premise: str, hypothesis: str) -> dict[str, float | None]:
    if not premise.strip() or not hypothesis.strip():
        return {"entailment": None, "neutral": None, "contradiction": None}
    tokenizer, model = _load_nli_bundle()
    import torch

    encoded = tokenizer(
        premise,
        hypothesis,
        truncation=True,
        padding=True,
        return_tensors="pt",
        max_length=512,
    )
    with torch.no_grad():
        logits = model(**encoded).logits
        probs = torch.softmax(logits, dim=-1)[0].tolist()
    id2label = getattr(model.config, "id2label", {}) or {}
    scores = {"entailment": None, "neutral": None, "contradiction": None}
    for idx, prob in enumerate(probs):
        label = str(id2label.get(idx, f"label_{idx}")).strip().lower()
        if label in scores:
            scores[label] = float(prob)
    return scores


def _extract_silver_reference_ir(entry_id: str) -> dict[str, Any]:
    if not _SILVER_REFERENCE_MD.exists():
        return {"found": False, "path": str(_SILVER_REFERENCE_MD), "reference_ir": ""}
    text = _SILVER_REFERENCE_MD.read_text(encoding="utf-8")
    pattern = rf"##\s+{re.escape(entry_id)}\b.*?Gold:\s*```a4v3\s*(.*?)```"
    match = re.search(pattern, text, flags=re.DOTALL)
    if not match:
        return {"found": False, "path": str(_SILVER_REFERENCE_MD), "reference_ir": ""}
    return {
        "found": True,
        "path": str(_SILVER_REFERENCE_MD),
        "reference_ir": _normalize_whitespace(match.group(1)),
    }


def _parse_arity_from_decl(line: str) -> int | None:
    if ":" not in line:
        return None
    rhs = line.split(":", 1)[1].strip()
    if not rhs:
        return None
    if "->" in rhs:
        lhs = rhs.split("->", 1)[0].strip()
    else:
        lhs = rhs
    if not lhs:
        return 0
    return lhs.count(",") + 1


def _structure_feature_counts(ir_text: str) -> dict[str, Counter[str]]:
    lines = [line.strip() for line in str(ir_text or "").splitlines() if line.strip()]
    top = Counter()
    logic = Counter()
    arity = Counter()
    for line in lines:
        for token in _STRUCTURE_TOP_LEVEL:
            if line.startswith(f"{token} "):
                top[token] += 1
                if token in {"fun", "rel"}:
                    value = _parse_arity_from_decl(line)
                    if value is not None:
                        bucket = min(value, 4)
                        arity[f"{token}_arity_{bucket}"] += 1
                break
        lowered = line.lower()
        for token in _STRUCTURE_LOGIC:
            logic[token] += len(re.findall(rf"\b{re.escape(token)}\b", lowered))
        logic["eq"] += lowered.count("=")
    return {"top": top, "logic": logic, "arity": arity}


def _counter_cosine(left: Counter[str], right: Counter[str]) -> float | None:
    keys = set(left) | set(right)
    if not keys:
        return None
    dot = sum(left.get(key, 0) * right.get(key, 0) for key in keys)
    left_norm = math.sqrt(sum(value * value for value in left.values()))
    right_norm = math.sqrt(sum(value * value for value in right.values()))
    if left_norm == 0.0 or right_norm == 0.0:
        return None
    return dot / (left_norm * right_norm)


def _mean(values: list[float]) -> float | None:
    if not values:
        return None
    return float(sum(values) / len(values))


def _pstdev(values: list[float]) -> float | None:
    if not values:
        return None
    if len(values) == 1:
        return 0.0
    return float(statistics.pstdev(values))


def _shannon_entropy(counts: Counter[str]) -> float | None:
    total = sum(counts.values())
    if total <= 0:
        return None
    entropy = 0.0
    for count in counts.values():
        if count <= 0:
            continue
        p = count / total
        entropy -= p * math.log2(p)
    return float(entropy)


def _iter_expr_nodes(expr: Any) -> list[dict[str, Any]]:
    nodes: list[dict[str, Any]] = []
    if isinstance(expr, dict):
        nodes.append(expr)
        for value in expr.values():
            if isinstance(value, dict):
                nodes.extend(_iter_expr_nodes(value))
            elif isinstance(value, list):
                for item in value:
                    nodes.extend(_iter_expr_nodes(item))
    elif isinstance(expr, list):
        for item in expr:
            nodes.extend(_iter_expr_nodes(item))
    return nodes


def _quantifier_slot_count(ir_ast: dict[str, Any]) -> int:
    total = 0
    for assertion in ir_ast.get("assertions", []):
        if not isinstance(assertion, dict):
            continue
        for node in _iter_expr_nodes(assertion.get("expr")):
            kind = str(node.get("kind", "")).strip()
            if kind in {"forall", "exists"}:
                total += len([item for item in node.get("vars", []) if isinstance(item, dict)])
    return total


def _focus_symbol_signature(ir_ast: dict[str, Any], focus_term: str) -> str:
    focus_norm = ir_stage._normalized_identifier(focus_term)
    for item in ir_ast.get("declarations", []):
        if not isinstance(item, dict):
            continue
        if ir_stage._normalized_identifier(str(item.get("name", ""))) != focus_norm:
            continue
        if str(item.get("decl", "")).strip() != "symbol":
            return f"{item.get('decl', 'decl')}:{item.get('name', '')}"
        symbol_kind = str(item.get("symbol_kind", "")).strip() or "symbol"
        args = [str(arg).strip() for arg in item.get("args", []) if str(arg).strip()]
        result_sort = str(item.get("result_sort", "")).strip()
        if symbol_kind == "fun":
            return f"fun({','.join(args)})->{result_sort}"
        return f"{symbol_kind}({','.join(args)})"
    return "missing"


def _parameterization_metrics_for_ir_ast(ir_ast: dict[str, Any], focus_term: str) -> dict[str, Any]:
    declarations = [item for item in ir_ast.get("declarations", []) if isinstance(item, dict)]
    callable_symbols = [
        item
        for item in declarations
        if str(item.get("decl", "")).strip() == "symbol"
        and str(item.get("symbol_kind", "")).strip() in {"fun", "rel"}
    ]
    callable_with_args = [item for item in callable_symbols if len(item.get("args", []) or []) > 0]
    top_level_parameter_slot_count = sum(len(item.get("args", []) or []) for item in callable_symbols)
    quantifier_parameter_slot_count = _quantifier_slot_count(ir_ast)
    total_parameter_slot_mass = top_level_parameter_slot_count + quantifier_parameter_slot_count
    factorization_count = len(callable_with_args)
    focus_signature = _focus_symbol_signature(ir_ast, focus_term)
    focus_symbol_arity = None
    if focus_signature != "missing":
        for item in callable_symbols:
            if ir_stage._normalized_identifier(str(item.get("name", ""))) == ir_stage._normalized_identifier(focus_term):
                focus_symbol_arity = len(item.get("args", []) or [])
                break
    return {
        "callable_symbol_count": len(callable_symbols),
        "callable_symbol_with_args_count": factorization_count,
        "top_level_parameter_slot_count": top_level_parameter_slot_count,
        "quantifier_parameter_slot_count": quantifier_parameter_slot_count,
        "total_parameter_slot_mass": total_parameter_slot_mass,
        "factorization_count": factorization_count,
        "parameter_slots_per_factor": (
            top_level_parameter_slot_count / factorization_count if factorization_count else 0.0
        ),
        "factorization_index": (
            factorization_count / max(1, top_level_parameter_slot_count) if top_level_parameter_slot_count else 0.0
        ),
        "focus_symbol_signature": focus_signature,
        "focus_symbol_arity": focus_symbol_arity,
    }


def _empty_expr_complexity() -> dict[str, int]:
    return {
        "node_count": 0,
        "depth": 0,
        "ite_count": 0,
        "quantifier_count": 0,
        "connective_count": 0,
        "branching_point_count": 0,
        "max_fanout": 0,
        "call_count": 0,
    }


def _merge_expr_complexity(children: list[dict[str, int]]) -> dict[str, int]:
    if not children:
        return _empty_expr_complexity()
    return {
        "node_count": sum(child["node_count"] for child in children),
        "depth": max(child["depth"] for child in children),
        "ite_count": sum(child["ite_count"] for child in children),
        "quantifier_count": sum(child["quantifier_count"] for child in children),
        "connective_count": sum(child["connective_count"] for child in children),
        "branching_point_count": sum(child["branching_point_count"] for child in children),
        "max_fanout": max(child["max_fanout"] for child in children),
        "call_count": sum(child["call_count"] for child in children),
    }


def _expr_complexity(expr: Any) -> dict[str, int]:
    if not isinstance(expr, dict):
        return _empty_expr_complexity()
    kind = str(expr.get("kind", "")).strip()
    if not kind:
        return _empty_expr_complexity()
    if kind == "ref":
        return {
            "node_count": 1,
            "depth": 1,
            "ite_count": 0,
            "quantifier_count": 0,
            "connective_count": 0,
            "branching_point_count": 0,
            "max_fanout": 0,
            "call_count": 0,
        }
    if kind == "call":
        children = [_expr_complexity(arg) for arg in expr.get("args", []) or [] if isinstance(arg, dict)]
        merged = _merge_expr_complexity(children)
        return {
            "node_count": 1 + merged["node_count"],
            "depth": 1 + merged["depth"],
            "ite_count": merged["ite_count"],
            "quantifier_count": merged["quantifier_count"],
            "connective_count": merged["connective_count"],
            "branching_point_count": merged["branching_point_count"],
            "max_fanout": max(len(children), merged["max_fanout"]),
            "call_count": 1 + merged["call_count"],
        }
    if kind in {"eq", "implies", "iff", "add", "sub", "mul", "div"}:
        children = [_expr_complexity(expr.get("left")), _expr_complexity(expr.get("right"))]
        merged = _merge_expr_complexity(children)
        is_logic = kind in {"implies", "iff"}
        return {
            "node_count": 1 + merged["node_count"],
            "depth": 1 + merged["depth"],
            "ite_count": merged["ite_count"],
            "quantifier_count": merged["quantifier_count"],
            "connective_count": merged["connective_count"] + (1 if is_logic else 0),
            "branching_point_count": merged["branching_point_count"] + (1 if is_logic else 0),
            "max_fanout": max(2, merged["max_fanout"]),
            "call_count": merged["call_count"],
        }
    if kind == "not":
        child = _expr_complexity(expr.get("arg"))
        return {
            "node_count": 1 + child["node_count"],
            "depth": 1 + child["depth"],
            "ite_count": child["ite_count"],
            "quantifier_count": child["quantifier_count"],
            "connective_count": child["connective_count"] + 1,
            "branching_point_count": child["branching_point_count"],
            "max_fanout": child["max_fanout"],
            "call_count": child["call_count"],
        }
    if kind in {"and", "or"}:
        children = [_expr_complexity(arg) for arg in expr.get("args", []) or [] if isinstance(arg, dict)]
        merged = _merge_expr_complexity(children)
        arity = len(children)
        return {
            "node_count": 1 + merged["node_count"],
            "depth": 1 + merged["depth"],
            "ite_count": merged["ite_count"],
            "quantifier_count": merged["quantifier_count"],
            "connective_count": merged["connective_count"] + 1,
            "branching_point_count": merged["branching_point_count"] + max(0, arity - 1),
            "max_fanout": max(arity, merged["max_fanout"]),
            "call_count": merged["call_count"],
        }
    if kind in {"forall", "exists"}:
        body = _expr_complexity(expr.get("body"))
        var_count = len([item for item in expr.get("vars", []) or [] if isinstance(item, dict)])
        return {
            "node_count": 1 + body["node_count"],
            "depth": 1 + body["depth"],
            "ite_count": body["ite_count"],
            "quantifier_count": body["quantifier_count"] + 1,
            "connective_count": body["connective_count"],
            "branching_point_count": body["branching_point_count"] + max(0, var_count - 1),
            "max_fanout": max(var_count, body["max_fanout"]),
            "call_count": body["call_count"],
        }
    if kind == "ite":
        children = [
            _expr_complexity(expr.get("cond")),
            _expr_complexity(expr.get("then")),
            _expr_complexity(expr.get("else")),
        ]
        merged = _merge_expr_complexity(children)
        return {
            "node_count": 1 + merged["node_count"],
            "depth": 1 + merged["depth"],
            "ite_count": merged["ite_count"] + 1,
            "quantifier_count": merged["quantifier_count"],
            "connective_count": merged["connective_count"] + 1,
            "branching_point_count": merged["branching_point_count"] + 2,
            "max_fanout": max(3, merged["max_fanout"]),
            "call_count": merged["call_count"],
        }
    if kind == "let":
        binding_values = [
            _expr_complexity(item.get("value"))
            for item in expr.get("bindings", []) or []
            if isinstance(item, dict)
        ]
        body = _expr_complexity(expr.get("body"))
        merged = _merge_expr_complexity(binding_values + [body])
        return {
            "node_count": 1 + merged["node_count"],
            "depth": 1 + merged["depth"],
            "ite_count": merged["ite_count"],
            "quantifier_count": merged["quantifier_count"],
            "connective_count": merged["connective_count"],
            "branching_point_count": merged["branching_point_count"],
            "max_fanout": max(len(binding_values) + 1, merged["max_fanout"]),
            "call_count": merged["call_count"],
        }
    return {
        "node_count": 1,
        "depth": 1,
        "ite_count": 0,
        "quantifier_count": 0,
        "connective_count": 0,
        "branching_point_count": 0,
        "max_fanout": 0,
        "call_count": 0,
    }


def _assertion_complexity_metrics(
    assertions: list[dict[str, Any]],
    *,
    normalized_clause_count: int,
) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    for item in assertions:
        if not isinstance(item, dict):
            continue
        complexity = _expr_complexity(item.get("expr"))
        rows.append(
            {
                "name": str(item.get("name", "") or "").strip(),
                "assert_kind": str(item.get("assert_kind", "") or "").strip(),
                **complexity,
            }
        )
    node_counts = [int(row["node_count"]) for row in rows]
    depths = [int(row["depth"]) for row in rows]
    ite_counts = [int(row["ite_count"]) for row in rows]
    quantifier_counts = [int(row["quantifier_count"]) for row in rows]
    connective_counts = [int(row["connective_count"]) for row in rows]
    branching_counts = [int(row["branching_point_count"]) for row in rows]
    call_counts = [int(row["call_count"]) for row in rows]
    assertion_count = len(rows)
    total_node_count = sum(node_counts)
    max_node_count = max(node_counts) if node_counts else 0
    top_complex_assertions = sorted(
        rows,
        key=lambda row: (
            -int(row["node_count"]),
            -int(row["depth"]),
            -int(row["branching_point_count"]),
            str(row["name"]).lower(),
        ),
    )[:10]
    normalized_clause_count_safe = max(1, normalized_clause_count)
    max_depth = max(depths) if depths else 0
    max_branching = max(branching_counts) if branching_counts else 0
    total_ite = sum(ite_counts)
    return {
        "assertion_count": assertion_count,
        "mean_assertion_node_count": (statistics.mean(node_counts) if node_counts else 0.0),
        "max_assertion_node_count": max_node_count,
        "total_assertion_node_count": total_node_count,
        "mean_assertion_depth": (statistics.mean(depths) if depths else 0.0),
        "max_assertion_depth": max_depth,
        "total_ite_count": total_ite,
        "max_ite_count_per_assertion": max(ite_counts) if ite_counts else 0,
        "total_quantifier_count": sum(quantifier_counts),
        "total_connective_count": sum(connective_counts),
        "total_branching_point_count": sum(branching_counts),
        "max_branching_point_count_per_assertion": max_branching,
        "mean_call_count_per_assertion": (statistics.mean(call_counts) if call_counts else 0.0),
        "single_assertion_logic_share": (max_node_count / total_node_count if total_node_count else None),
        "overcompressed_single_assertion_flag": int(
            normalized_clause_count >= 3
            and assertion_count == 1
            and (max_node_count >= 12 or max_depth >= 5 or max_branching >= 4 or total_ite > 0)
        ),
        "top_complex_assertions": top_complex_assertions,
        "normalized_clause_count": normalized_clause_count,
        "node_count_per_normalized_clause": (total_node_count / normalized_clause_count_safe),
        "branching_point_count_per_normalized_clause": (
            sum(branching_counts) / normalized_clause_count_safe
        ),
    }


def _normalized_alignment_metrics(
    *,
    normalized_clause_count: int,
    assertions: list[dict[str, Any]],
    parameterization: dict[str, Any],
    assertion_complexity: dict[str, Any],
) -> dict[str, Any]:
    assertion_count = len(assertions)
    normalized_clause_count_safe = max(1, normalized_clause_count)
    clause_underdecomposition_mass = max(0, normalized_clause_count - assertion_count)
    clause_overdecomposition_mass = max(0, assertion_count - normalized_clause_count)
    return {
        "normalized_clause_count": normalized_clause_count,
        "logic_block_count": assertion_count,
        "clause_to_logic_block_ratio": (
            normalized_clause_count / assertion_count if assertion_count else float(normalized_clause_count)
        ),
        "logic_block_to_clause_ratio": (assertion_count / normalized_clause_count_safe),
        "clause_underdecomposition_mass": clause_underdecomposition_mass,
        "clause_overdecomposition_mass": clause_overdecomposition_mass,
        "focus_symbol_arity": parameterization.get("focus_symbol_arity"),
        "helper_factorization_count": parameterization.get("factorization_count"),
        "single_assertion_logic_share": assertion_complexity.get("single_assertion_logic_share"),
        "underdecomposed_logic_flag": int(
            normalized_clause_count >= 3
            and assertion_count <= 1
            and bool(assertion_complexity.get("overcompressed_single_assertion_flag"))
        ),
    }


def _structure_similarity(current_ir: str, other_ir: str) -> float | None:
    return _silver_structure_similarity(current_ir, other_ir).get("silver_structure_similarity")


def _token_jaccard(left_text: str, right_text: str) -> float | None:
    left = set(_content_tokens(left_text))
    right = set(_content_tokens(right_text))
    if not left and not right:
        return 1.0
    if not left or not right:
        return 0.0
    return len(left & right) / len(left | right)


def _variant_variability_metrics(
    *,
    variants: list[dict[str, Any]],
    focus_term: str,
    selected_rendered_ir: str,
) -> dict[str, Any]:
    usable: list[dict[str, Any]] = []
    for item in variants:
        if not isinstance(item, dict):
            continue
        result = item.get("result", {}) or {}
        if str(result.get("status", "")).strip() != "ok":
            continue
        ir_ast = result.get("ir_ast", {})
        rendered_ir = _normalize_whitespace(str(result.get("rendered_ir", "") or ""))
        if not isinstance(ir_ast, dict) or not rendered_ir:
            continue
        parameterization = _parameterization_metrics_for_ir_ast(ir_ast, focus_term)
        usable.append(
            {
                "reading_id": str(item.get("reading_id", "")).strip(),
                "rendered_ir": rendered_ir,
                "parameterization": parameterization,
                "focus_signature": parameterization["focus_symbol_signature"],
                "total_parameter_slot_mass": parameterization["total_parameter_slot_mass"],
                "factorization_count": parameterization["factorization_count"],
            }
        )
    if not usable:
        return {
            "usable_variant_count": 0,
            "unique_variant_signature_count": 0,
            "focus_signature_unique_count": 0,
            "focus_signature_mode_share": None,
            "pairwise_structure_similarity_mean": None,
            "pairwise_structure_distance_mean": None,
            "pairwise_token_jaccard_mean": None,
            "parameter_slot_mass_mean": None,
            "parameter_slot_mass_stddev": None,
            "factorization_count_mean": None,
            "factorization_count_stddev": None,
            "same_parameter_mass_different_structure_pair_count": 0,
            "selected_ir_is_mode": None,
        }
    focus_signatures = [item["focus_signature"] for item in usable]
    focus_counts = Counter(focus_signatures)
    parameter_masses = [float(item["total_parameter_slot_mass"]) for item in usable]
    factor_counts = [float(item["factorization_count"]) for item in usable]
    pairwise_structure: list[float] = []
    pairwise_token: list[float] = []
    same_mass_different_structure_pair_count = 0
    for left, right in itertools.combinations(usable, 2):
        structure = _structure_similarity(left["rendered_ir"], right["rendered_ir"])
        if structure is not None:
            pairwise_structure.append(float(structure))
            if left["total_parameter_slot_mass"] == right["total_parameter_slot_mass"] and structure < 0.999:
                same_mass_different_structure_pair_count += 1
        token_jaccard = _token_jaccard(left["rendered_ir"], right["rendered_ir"])
        if token_jaccard is not None:
            pairwise_token.append(float(token_jaccard))
    selected_count = sum(1 for item in usable if item["rendered_ir"] == _normalize_whitespace(selected_rendered_ir))
    return {
        "usable_variant_count": len(usable),
        "unique_variant_signature_count": len({item["rendered_ir"] for item in usable}),
        "focus_signature_unique_count": len(focus_counts),
        "focus_signatures": dict(focus_counts),
        "artifact_signature_entropy": _shannon_entropy(Counter(item["rendered_ir"] for item in usable)),
        "focus_signature_entropy": _shannon_entropy(focus_counts),
        "focus_signature_mode_share": (max(focus_counts.values()) / len(usable)) if usable else None,
        "pairwise_structure_similarity_mean": _mean(pairwise_structure),
        "pairwise_structure_distance_mean": (
            None if not pairwise_structure else float(1.0 - (_mean(pairwise_structure) or 0.0))
        ),
        "pairwise_token_jaccard_mean": _mean(pairwise_token),
        "parameter_slot_mass_mean": _mean(parameter_masses),
        "parameter_slot_mass_stddev": _pstdev(parameter_masses),
        "factorization_count_mean": _mean(factor_counts),
        "factorization_count_stddev": _pstdev(factor_counts),
        "same_parameter_mass_different_structure_pair_count": same_mass_different_structure_pair_count,
        "selected_ir_is_mode": bool(selected_count and selected_count == max(Counter(item["rendered_ir"] for item in usable).values())),
    }


def _silver_structure_similarity(current_ir: str, silver_ir: str) -> dict[str, Any]:
    current = _structure_feature_counts(current_ir)
    silver = _structure_feature_counts(silver_ir)
    top_score = _counter_cosine(current["top"], silver["top"])
    logic_score = _counter_cosine(current["logic"], silver["logic"])
    arity_score = _counter_cosine(current["arity"], silver["arity"])
    present = [score for score in (top_score, logic_score, arity_score) if score is not None]
    total = sum(present) / len(present) if present else None
    return {
        "top_level_cosine": top_score,
        "logic_cosine": logic_score,
        "arity_cosine": arity_score,
        "silver_structure_similarity": total,
    }


def _expr_fingerprint(expr: Any) -> str:
    if isinstance(expr, dict):
        kind = str(expr.get("kind", "")).strip()
        if kind == "ref":
            return f"ref:{expr.get('name', '')}"
        if kind == "call":
            args = ",".join(_expr_fingerprint(arg) for arg in expr.get("args", []))
            return f"call:{expr.get('callee', '')}({args})"
        if kind in {"eq", "implies", "add", "sub", "mul", "div"}:
            return f"{kind}({_expr_fingerprint(expr.get('left'))},{_expr_fingerprint(expr.get('right'))})"
        if kind == "not":
            return f"not({_expr_fingerprint(expr.get('arg'))})"
        if kind == "and" or kind == "or":
            args = ",".join(_expr_fingerprint(arg) for arg in expr.get("args", []))
            return f"{kind}({args})"
        if kind == "forall" or kind == "exists":
            vars_fp = ",".join(f"{item.get('name','')}:{item.get('sort','')}" for item in expr.get("vars", []))
            return f"{kind}[{vars_fp}]({_expr_fingerprint(expr.get('body'))})"
        if kind == "ite":
            return f"ite({_expr_fingerprint(expr.get('cond'))},{_expr_fingerprint(expr.get('then'))},{_expr_fingerprint(expr.get('else'))})"
        if kind == "let":
            bindings = ",".join(
                f"{item.get('name','')}={_expr_fingerprint(item.get('value'))}"
                for item in expr.get("bindings", [])
                if isinstance(item, dict)
            )
            return f"let[{bindings}]({_expr_fingerprint(expr.get('body'))})"
        if kind == "member":
            return f"member({_expr_fingerprint(expr.get('binder'))},{_expr_fingerprint(expr.get('predicate'))})"
        return json.dumps(expr, ensure_ascii=False, sort_keys=True)
    if isinstance(expr, list):
        return "[" + ",".join(_expr_fingerprint(item) for item in expr) + "]"
    return json.dumps(expr, ensure_ascii=False, sort_keys=True)


def _count_reflexive_equalities(expr: Any) -> int:
    if not isinstance(expr, dict):
        return 0
    kind = str(expr.get("kind", "")).strip()
    count = 0
    if kind == "eq":
        left = _expr_fingerprint(expr.get("left"))
        right = _expr_fingerprint(expr.get("right"))
        if left == right:
            count += 1
    for value in expr.values():
        if isinstance(value, dict):
            count += _count_reflexive_equalities(value)
        elif isinstance(value, list):
            for item in value:
                count += _count_reflexive_equalities(item)
    return count


def _structural_variant_signature(variant: dict[str, Any]) -> str:
    result = (variant.get("result", {}) or {})
    rendered_ir = _normalize_whitespace(str(result.get("rendered_ir", "") or ""))
    if rendered_ir:
        return rendered_ir
    ir_ast = result.get("ir_ast", {})
    return json.dumps(ir_ast, ensure_ascii=False, sort_keys=True)


def _status_count(audit_items: list[dict[str, Any]], *needles: str) -> int:
    needle_norms = [needle.lower() for needle in needles]
    count = 0
    for item in audit_items:
        if not isinstance(item, dict):
            continue
        required = str(item.get("required_ir_location", "")).lower()
        if any(needle in required for needle in needle_norms) and str(item.get("status", "")).strip() != "covered_formally":
            count += 1
    return count


def _audit_role_to_required_location(role: str) -> str:
    role_norm = role.lower()
    if "scope" in role_norm:
        return "DefinitionNode.scope / applies_to_component_set"
    if "counterfactual" in role_norm:
        return "DefinitionNode.core_condition.counterfactual"
    if "exclusion" in role_norm or "scheduled_vs_unscheduled" in role_norm:
        return "DefinitionNode.exclusions"
    if "clarification" in role_norm or "intent_new_components" in role_norm or "close_of_trading_reference" in role_norm:
        return "DefinitionNode.clarification_annotation / scope_note"
    if "determination" in role_norm or "responsibility" in role_norm:
        return "DefinitionNode.governance_final_decision"
    return ""


def _normalize_audit_items(audit_payload: dict[str, Any]) -> list[dict[str, Any]]:
    items = [item for item in audit_payload.get("items", []) if isinstance(item, dict)]
    if items:
        return items
    elements = [item for item in audit_payload.get("elements", []) if isinstance(item, dict)]
    normalized: list[dict[str, Any]] = []
    for item in elements:
        status_raw = str(item.get("status", "")).strip().upper()
        if status_raw == "PASS":
            status = "covered_formally"
        elif status_raw == "FAIL":
            status = "missing"
        else:
            status = "partial"
        normalized.append(
            {
                "fragment": str(item.get("required_fragment", "")).strip(),
                "required_ir_location": _audit_role_to_required_location(str(item.get("role", "")).strip()),
                "status": status,
                "where_found": str(item.get("ir_location", "")).strip(),
                "issue": str(item.get("notes", "")).strip(),
            }
        )
    return normalized


def _allowed_surface_tokens(
    *,
    ctx: ir_stage.ExperimentContext,
    advisory_contract: dict[str, Any],
    include_prelude: bool,
    include_advisory: bool,
) -> set[str]:
    allowed: set[str] = set(_IR_SYNTAX_TOKENS)
    sources = [
        str(ctx.entry.get("source_term", "") or ""),
        str(ctx.entry.get("source_excerpt", "") or ""),
        " ".join(str(item) for item in ctx.entry.get("normalized_clauses", []) if isinstance(item, str)),
    ]
    if include_prelude:
        prelude = ir_stage._compact_prelude(ctx.prelude_json)
        sources.append(json.dumps(prelude, ensure_ascii=False))
    if include_advisory:
        sources.append(json.dumps(advisory_contract or {}, ensure_ascii=False))
    for text in sources:
        allowed.update(_word_tokens(text))
    return allowed


def _surface_texts(result: dict[str, Any]) -> tuple[str, str]:
    formula_surface = str(result.get("rendered_ir", "") or "")
    prose_surface = json.dumps(
        {
            "rendering_notes": result.get("rendering_notes", []),
            "primitive_usage": result.get("primitive_usage", []),
            "strengths": result.get("strengths", []),
            "residual_risks": result.get("residual_risks", []),
        },
        ensure_ascii=False,
    )
    return formula_surface, prose_surface


def _effective_selected_result(ir_payload: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    drafter = (ir_payload.get("drafter", {}) or {})
    result = (drafter.get("result", {}) or {})
    ir_ast = result.get("ir_ast", {})
    rendered_ir = str(result.get("rendered_ir", "") or "").strip()
    if isinstance(ir_ast, dict) and ir_ast and rendered_ir:
        return drafter, result
    variants = [item for item in ir_payload.get("drafter_variants", []) if isinstance(item, dict)]
    critic = (ir_payload.get("critic", {}) or {})
    selected_id = str(critic.get("selected_reading_id", "") or "").strip()
    successful_variants: list[tuple[dict[str, Any], dict[str, Any]]] = []
    for variant in variants:
        variant_result = (variant.get("result", {}) or {})
        variant_ir_ast = variant_result.get("ir_ast", {})
        variant_rendered_ir = str(variant_result.get("rendered_ir", "") or "").strip()
        if not (isinstance(variant_ir_ast, dict) and variant_ir_ast and variant_rendered_ir):
            continue
        successful_variants.append((variant, variant_result))
        if bool(variant.get("is_critic_selected", False)):
            return variant, variant_result
        if selected_id and str(variant.get("reading_id", "")).strip() == selected_id:
            return variant, variant_result
    if len(successful_variants) == 1:
        return successful_variants[0]
    if successful_variants:
        for variant, variant_result in successful_variants:
            if bool(variant.get("is_advisor_selected", False)):
                return variant, variant_result
        return successful_variants[0]
    return drafter, result


def compute_metrics(payload: dict[str, Any], *, include_semantic_models: bool = True) -> dict[str, Any]:
    entry_id = str(payload.get("entry_id", "")).strip()
    ctx = ir_stage._load_entry_context(entry_id)
    ctx, disable_silver_reference = _effective_reference_context(ctx, payload)
    ir_payload = payload.get("ir_stage", {}) or {}
    if not ir_payload and any(key in payload for key in ("advisor", "drafter", "critic", "drafter_variants")):
        ir_payload = payload
    advisory = ((ir_payload.get("advisor", {}) or {}).get("contract", {}) or {})
    drafter, result = _effective_selected_result(ir_payload)
    ir_ast = result.get("ir_ast", {}) if isinstance(result.get("ir_ast", {}), dict) else {}
    critic = (ir_payload.get("critic", {}) or {})
    coverage = (payload.get("coverage", {}) or {})
    audit = (payload.get("coverage_audit", {}) or {})
    if isinstance(audit.get("coverage_audit"), dict):
        audit = audit["coverage_audit"]
    enforcement = (payload.get("coverage_enforcement", {}) or {})
    if not enforcement and coverage and audit:
        enforcement = qa_stage._coverage_enforcement(coverage, audit)
    audit_items = _normalize_audit_items(audit)

    canonical_payload = {
        "schema_version": result.get("schema_version", ""),
        "focus_term": result.get("focus_term", ""),
        "ir_ast": result.get("ir_ast", {}),
        "rendering_notes": result.get("rendering_notes", []),
        "primitive_usage": result.get("primitive_usage", []),
        "strengths": result.get("strengths", []),
        "residual_risks": result.get("residual_risks", []),
    }
    # Use the extended validator that monkey-patches lt/gt/lte/gte/count
    # support into the legacy V6 canonical validator. The bare legacy
    # validator only recognizes `eq` and would false-positive on every IR
    # using comparison operators or count-binders.
    try:
        import sys as _sys, pathlib as _pathlib
        _sys.path.insert(0, str(_pathlib.Path(__file__).parent.parent))
        import extended_canonical_validator_v1 as _ev  # noqa: E402
        canonical_errors = _ev.validate_extended(canonical_payload)
    except Exception:
        # Fall back to bare validator if extended fails to load.
        canonical_errors = ir_stage._validate_canonical_drafter_payload(canonical_payload)
    origin_errors = ir_stage._validate_symbol_origins(result, ctx, advisory)
    origin_joined = "\n".join(origin_errors)

    source_excerpt = str(ctx.entry.get("source_excerpt", "") or "")
    normalized_text = " ".join(str(item) for item in ctx.entry.get("normalized_clauses", []) if isinstance(item, str))
    if not normalized_text.strip():
        normalized_text = source_excerpt
    focus_term = str(result.get("focus_term", "") or advisory.get("focus_term", "") or "")

    source_excerpt_content_tokens = ir_stage._semantic_coverage_tokens(source_excerpt, focus_term)
    source_excerpt_content_counter = _content_token_counter(source_excerpt, focus_term)
    reference_content_tokens = ir_stage._semantic_coverage_tokens(normalized_text, focus_term)
    reference_content_counter = _content_token_counter(normalized_text, focus_term)
    formula_surface, prose_surface = _surface_texts(result)
    formula_token_counter = _content_token_counter(formula_surface, focus_term)
    prose_token_counter = _content_token_counter(prose_surface, focus_term)
    full_surface_token_counter = formula_token_counter + prose_token_counter
    formula_tokens = set(formula_token_counter)
    prose_tokens = set(prose_token_counter)
    full_tokens = formula_tokens | prose_tokens
    reference_token_set = set(reference_content_tokens)
    source_excerpt_token_set = set(source_excerpt_content_tokens)

    formula_overlap = reference_token_set & formula_tokens
    full_overlap = reference_token_set & full_tokens
    formula_recall = len(formula_overlap) / len(reference_token_set) if reference_token_set else 1.0
    full_recall = len(full_overlap) / len(reference_token_set) if reference_token_set else 1.0
    full_jaccard = len(full_overlap) / len(reference_token_set | full_tokens) if (reference_token_set or full_tokens) else 1.0
    formula_repeat_metrics = _repeat_metrics(formula_token_counter, reference_content_counter)
    full_repeat_metrics = _repeat_metrics(full_surface_token_counter, reference_content_counter)

    normalized_token_set = reference_token_set
    normalized_content_counter = reference_content_counter
    source_vs_normalized_overlap = source_excerpt_token_set & normalized_token_set
    source_vs_normalized_jaccard = (
        len(source_vs_normalized_overlap) / len(source_excerpt_token_set | normalized_token_set)
        if (source_excerpt_token_set or normalized_token_set)
        else 1.0
    )
    source_vs_normalized_repeat_metrics = _repeat_metrics(normalized_content_counter, source_excerpt_content_counter)
    if include_semantic_models:
        source_vs_normalized_bertscore = _safe_bertscore(normalized_text, source_excerpt)
        nli_normalized_to_source = _nli_scores(normalized_text, source_excerpt)
        nli_source_to_normalized = _nli_scores(source_excerpt, normalized_text)
        source_vs_normalized_contradiction_candidates = [
            score
            for score in (
                nli_normalized_to_source.get("contradiction"),
                nli_source_to_normalized.get("contradiction"),
            )
            if isinstance(score, float)
        ]
        source_vs_normalized_contradiction_score = (
            max(source_vs_normalized_contradiction_candidates)
            if source_vs_normalized_contradiction_candidates
            else None
        )
    else:
        source_vs_normalized_bertscore = {"precision": None, "recall": None, "f1": None}
        nli_normalized_to_source = {"entailment": None, "neutral": None, "contradiction": None}
        nli_source_to_normalized = {"entailment": None, "neutral": None, "contradiction": None}
        source_vs_normalized_contradiction_score = None

    formula_word_tokens = _word_tokens(formula_surface)
    prose_word_tokens = _word_tokens(prose_surface)
    allowed_text_only = _allowed_surface_tokens(
        ctx=ctx,
        advisory_contract=advisory,
        include_prelude=False,
        include_advisory=False,
    )
    allowed_text_prelude = _allowed_surface_tokens(
        ctx=ctx,
        advisory_contract=advisory,
        include_prelude=True,
        include_advisory=False,
    )
    allowed_text_prelude_advisory = _allowed_surface_tokens(
        ctx=ctx,
        advisory_contract=advisory,
        include_prelude=True,
        include_advisory=True,
    )

    new_formula_tokens_text_only = sorted({token for token in formula_word_tokens if token not in allowed_text_only})
    new_formula_tokens_text_prelude = sorted({token for token in formula_word_tokens if token not in allowed_text_prelude})
    new_formula_tokens_text_prelude_advisory = sorted(
        {token for token in formula_word_tokens if token not in allowed_text_prelude_advisory}
    )
    full_word_tokens = formula_word_tokens + prose_word_tokens
    new_full_tokens_text_only = sorted({token for token in full_word_tokens if token not in allowed_text_only})
    new_full_tokens_text_prelude = sorted({token for token in full_word_tokens if token not in allowed_text_prelude})
    new_full_tokens_text_prelude_advisory = sorted(
        {token for token in full_word_tokens if token not in allowed_text_prelude_advisory}
    )

    new_formula_content_tokens_text_only = sorted(
        token for token in new_formula_tokens_text_only if token not in _STOPWORDS and len(token) >= 4
    )
    new_formula_content_tokens_text_prelude = sorted(
        token for token in new_formula_tokens_text_prelude if token not in _STOPWORDS and len(token) >= 4
    )
    new_formula_content_tokens_text_prelude_advisory = sorted(
        token for token in new_formula_tokens_text_prelude_advisory if token not in _STOPWORDS and len(token) >= 4
    )
    new_full_content_tokens_text_only = sorted(
        token for token in new_full_tokens_text_only if token not in _STOPWORDS and len(token) >= 4
    )
    new_full_content_tokens_text_prelude = sorted(
        token for token in new_full_tokens_text_prelude if token not in _STOPWORDS and len(token) >= 4
    )
    new_full_content_tokens_text_prelude_advisory = sorted(
        token for token in new_full_tokens_text_prelude_advisory if token not in _STOPWORDS and len(token) >= 4
    )

    assertions = [item for item in ir_ast.get("assertions", []) if isinstance(item, dict)]
    declarations = [item for item in ir_ast.get("declarations", []) if isinstance(item, dict)]
    reflexive_equality_count = sum(_count_reflexive_equalities(item.get("expr")) for item in assertions)

    focus_term_norm = ir_stage._normalized_identifier(focus_term)
    top_decl_names = [str(item.get("name", "")).strip() for item in declarations]
    focus_term_in_top_level_decl = any(
        ir_stage._normalized_identifier(name) == focus_term_norm for name in top_decl_names if name
    )
    focus_term_in_formula_body = focus_term.lower() in formula_surface.lower() if focus_term else False
    focus_term_explicitly_modeled = focus_term_in_top_level_decl or focus_term_in_formula_body

    normalized_clause_count = len([item for item in ctx.entry.get("normalized_clauses", []) if isinstance(item, str)])
    formula_bearing_item_count = len(assertions)
    formula_to_clause_compression_ratio = (
        normalized_clause_count / formula_bearing_item_count if formula_bearing_item_count else float(normalized_clause_count)
    )

    if "covered_formally_count" in audit:
        covered_formally_count = int(audit.get("covered_formally_count", 0) or 0)
        covered_only_in_notes_count = int(audit.get("covered_only_in_notes_count", 0) or 0)
        missing_count = int(audit.get("missing_count", 0) or 0)
    elif isinstance(audit.get("summary"), dict):
        summary_counts = audit.get("summary", {}) or {}
        covered_formally_count = int(summary_counts.get("pass", 0) or 0)
        covered_only_in_notes_count = 0
        missing_count = int(summary_counts.get("fail", 0) or 0)
    else:
        covered_formally_count = sum(1 for item in audit_items if str(item.get("status", "")).strip() == "covered_formally")
        covered_only_in_notes_count = sum(
            1 for item in audit_items if str(item.get("status", "")).strip() == "covered_only_in_notes"
        )
        missing_count = sum(1 for item in audit_items if str(item.get("status", "")).strip() == "missing")
    audit_item_count = len(audit_items)
    coverage_fragment_formal_ratio = covered_formally_count / audit_item_count if audit_item_count else 1.0
    coverage_fragment_any_ratio = (
        (covered_formally_count + covered_only_in_notes_count) / audit_item_count if audit_item_count else 1.0
    )
    prose_leak_count = int(enforcement.get("violation_count", 0) or 0)

    checklist_findings = critic.get("checklist_findings", {}) or {}
    explicit_link_violation_count = 0
    if isinstance(checklist_findings.get("keep_links_explicit"), dict):
        verdict = str(checklist_findings["keep_links_explicit"].get("verdict", "")).strip().lower()
        explicit_link_violation_count = 0 if verdict == "pass" else 1

    semantic_preservation = {
        "explicit_link_violation_count": explicit_link_violation_count,
        "scope_visibility_violation_count": _status_count(audit_items, "definitionnode.scope", "applies_to_component_set"),
        "exception_visibility_violation_count": _status_count(audit_items, "definitionnode.exclusions"),
        "counterfactual_loss_count": _status_count(audit_items, "definitionnode.core_condition.counterfactual"),
        "clarification_loss_count": _status_count(audit_items, "definitionnode.clarification_annotation"),
        "responsibility_loss_count": _status_count(
            audit_items,
            "definitionnode.governance_final_decision",
            "responsibility",
        ),
    }

    variants = [item for item in ir_payload.get("drafter_variants", []) if isinstance(item, dict)]
    variant_signatures = {_structural_variant_signature(item) for item in variants} if variants else set()

    qa_attempts = sum(
        int((payload.get(section, {}) or {}).get("raw_attempt_count", 0) or 0)
        for section in ("questioner", "answerer", "coverage", "coverage_audit")
    )
    critic_attempts = int((critic.get("raw_attempt_count", 0) or 0))
    advisor_call_lb = 0
    advisor_payload = ir_payload.get("advisor", {}) or {}
    advisor_samples = [item for item in advisor_payload.get("samples", []) if isinstance(item, dict)]
    if advisor_samples:
        advisor_call_lb = sum(_assistant_turn_count(item.get("raw_messages", [])) for item in advisor_samples)
    else:
        advisor_call_lb = _assistant_turn_count(advisor_payload.get("raw_messages", []))
    selected_drafter_call_lb = _assistant_turn_count(drafter.get("raw_messages", []))
    observable_llm_call_lower_bound = qa_attempts + critic_attempts + advisor_call_lb + selected_drafter_call_lb

    confidence_label = str(critic.get("confidence", "")).strip().lower()

    render_back_text = _render_back_from_ir_ast(
        ir_ast,
        focus_term,
        str(result.get("rendered_ir", "") or ""),
    )
    if include_semantic_models:
        bert_normalized = _safe_bertscore(render_back_text, normalized_text)
        bert_source = _safe_bertscore(render_back_text, source_excerpt)
        nli_render_to_normalized = _nli_scores(render_back_text, normalized_text)
        nli_normalized_to_render = _nli_scores(normalized_text, render_back_text)
        nli_render_to_source = _nli_scores(render_back_text, source_excerpt)
        nli_source_to_render = _nli_scores(source_excerpt, render_back_text)
        contradiction_candidates = [
            score
            for score in (
                nli_render_to_normalized.get("contradiction"),
                nli_normalized_to_render.get("contradiction"),
                nli_render_to_source.get("contradiction"),
                nli_source_to_render.get("contradiction"),
            )
            if isinstance(score, float)
        ]
        render_contradiction_score = max(contradiction_candidates) if contradiction_candidates else None
    else:
        bert_normalized = {"precision": None, "recall": None, "f1": None}
        bert_source = {"precision": None, "recall": None, "f1": None}
        nli_render_to_normalized = {"entailment": None, "neutral": None, "contradiction": None}
        nli_normalized_to_render = {"entailment": None, "neutral": None, "contradiction": None}
        nli_render_to_source = {"entailment": None, "neutral": None, "contradiction": None}
        nli_source_to_render = {"entailment": None, "neutral": None, "contradiction": None}
        render_contradiction_score = None

    if disable_silver_reference:
        silver_reference = {"found": False, "path": None, "reference_ir": None}
        silver_structure = {
            "top_level_cosine": None,
            "logic_cosine": None,
            "arity_cosine": None,
            "silver_structure_similarity": None,
        }
    else:
        silver_reference = _extract_silver_reference_ir(entry_id)
        silver_structure = (
            _silver_structure_similarity(
                str(result.get("rendered_ir", "") or ""),
                silver_reference.get("reference_ir", ""),
            )
            if silver_reference.get("found")
            else {
                "top_level_cosine": None,
                "logic_cosine": None,
                "arity_cosine": None,
                "silver_structure_similarity": None,
            }
        )
    parameterization = _parameterization_metrics_for_ir_ast(ir_ast, focus_term)
    identifier_glue = _identifier_glue_metrics(
        ir_ast=ir_ast,
        ctx=ctx,
        advisory=advisory,
        focus_term=focus_term,
    )
    assertion_complexity = _assertion_complexity_metrics(
        assertions,
        normalized_clause_count=normalized_clause_count,
    )
    normalized_alignment = _normalized_alignment_metrics(
        normalized_clause_count=normalized_clause_count,
        assertions=assertions,
        parameterization=parameterization,
        assertion_complexity=assertion_complexity,
    )
    variant_variability = _variant_variability_metrics(
        variants=variants,
        focus_term=focus_term,
        selected_rendered_ir=str(result.get("rendered_ir", "") or ""),
    )
    reference_content_mass = int(sum(reference_content_counter.values()))
    source_excerpt_content_mass = int(sum(source_excerpt_content_counter.values()))
    normalized_clause_count_safe = max(1, normalized_clause_count)
    parameter_slot_mass = float(parameterization["total_parameter_slot_mass"])
    formula_repeat_overuse_mass = float(formula_repeat_metrics["repeat_overuse_mass"])
    full_surface_repeat_overuse_mass = float(full_repeat_metrics["repeat_overuse_mass"])
    pairwise_structure_similarity_mean = variant_variability.get("pairwise_structure_similarity_mean")

    def _per(value: float | None, denom: float) -> float | None:
        if value is None:
            return None
        if denom <= 0.0:
            return None
        return float(value / denom)

    metrics = {
        "generated_at": datetime.now().astimezone().isoformat(),
        "entry_id": entry_id,
        "artifact_path": "",
        "catalog_version": "translation_metrics_catalog_v1",
        "validity": {
            "ast_valid": int(not canonical_errors),
            "ast_error_count": len(canonical_errors),
            "rendering_ok": int(str(result.get("rendering_status", "")).strip() == "rendered_from_ast"),
            "combined_validation_ok": int(str(result.get("status", "")).strip() == "ok"),
            "invalid_submit_count": int(drafter.get("invalid_submit_count", 0) or 0),
            "repair_orchestrator_count": int(drafter.get("repair_orchestrator_count", 0) or 0),
            "semantic_coverage_retry_count": int(drafter.get("semantic_coverage_retry_count", 0) or 0),
            "status": str(result.get("status", "")).strip(),
            "ast_conformance": str(result.get("ast_conformance", "")).strip(),
            "rendering_status": str(result.get("rendering_status", "")).strip(),
        },
        "grounding": {
            "ungrounded_symbol_count": origin_joined.count("symbol `"),
            "ungrounded_sort_count": origin_joined.count("sort `"),
            "ungrounded_ref_count": origin_joined.count("ref `"),
            "ungrounded_callee_count": origin_joined.count(".callee:"),
            "prelude_redeclaration_count": origin_joined.count("redeclares Prelude"),
            "origin_error_count": len(origin_errors),
            "new_formula_token_count_vs_text_only": len(new_formula_tokens_text_only),
            "new_formula_content_token_count_vs_text_only": len(new_formula_content_tokens_text_only),
            "new_formula_token_count_vs_text_prelude_only": len(new_formula_tokens_text_prelude),
            "new_formula_content_token_count_vs_text_prelude_only": len(new_formula_content_tokens_text_prelude),
            "new_formula_token_count_vs_text_prelude_advisory": len(new_formula_tokens_text_prelude_advisory),
            "new_formula_content_token_count_vs_text_prelude_advisory": len(
                new_formula_content_tokens_text_prelude_advisory
            ),
            "new_full_surface_token_count_vs_text_only": len(new_full_tokens_text_only),
            "new_full_surface_content_token_count_vs_text_only": len(new_full_content_tokens_text_only),
            "new_full_surface_token_count_vs_text_prelude_only": len(new_full_tokens_text_prelude),
            "new_full_surface_content_token_count_vs_text_prelude_only": len(new_full_content_tokens_text_prelude),
            "new_full_surface_token_count_vs_text_prelude_advisory": len(new_full_tokens_text_prelude_advisory),
            "new_full_surface_content_token_count_vs_text_prelude_advisory": len(
                new_full_content_tokens_text_prelude_advisory
            ),
            "new_formula_content_tokens_vs_text_only": new_formula_content_tokens_text_only[:50],
            "new_formula_content_tokens_vs_text_prelude_only": new_formula_content_tokens_text_prelude[:50],
            "new_formula_content_tokens_vs_text_prelude_advisory": new_formula_content_tokens_text_prelude_advisory[:50],
            "new_full_surface_content_tokens_vs_text_only": new_full_content_tokens_text_only[:50],
            "new_full_surface_content_tokens_vs_text_prelude_only": new_full_content_tokens_text_prelude[:50],
            "new_full_surface_content_tokens_vs_text_prelude_advisory": new_full_content_tokens_text_prelude_advisory[
                :50
            ],
        },
        "coverage": {
            "normalized_clause_count": normalized_clause_count,
            "formula_bearing_item_count": formula_bearing_item_count,
            "formula_to_clause_compression_ratio": formula_to_clause_compression_ratio,
            "coverage_fragment_count": audit_item_count,
            "covered_formally_count": covered_formally_count,
            "covered_only_in_notes_count": covered_only_in_notes_count,
            "missing_fragment_count": missing_count,
            "coverage_fragment_formal_ratio": coverage_fragment_formal_ratio,
            "coverage_fragment_any_ratio": coverage_fragment_any_ratio,
            "prose_leak_count": prose_leak_count,
        },
        "lexical_coverage": {
            "reference_text_basis": "normalized_clauses_or_source_excerpt_fallback",
            "source_content_token_count": len(reference_token_set),
            "source_content_token_mass": reference_content_mass,
            "formula_content_token_count": len(formula_tokens),
            "formula_content_token_mass": int(sum(formula_token_counter.values())),
            "full_surface_content_token_count": len(full_tokens),
            "full_surface_content_token_mass": int(sum(full_surface_token_counter.values())),
            "formula_content_token_recall": formula_recall,
            "full_surface_content_token_recall": full_recall,
            "full_surface_content_token_jaccard": full_jaccard,
            "formula_content_token_multiset_recall": formula_repeat_metrics["multiset_recall"],
            "formula_content_token_multiset_precision": formula_repeat_metrics["multiset_precision"],
            "formula_repeat_overuse_token_count": formula_repeat_metrics["repeat_overuse_token_count"],
            "formula_repeat_overuse_mass": formula_repeat_metrics["repeat_overuse_mass"],
            "formula_repeat_underuse_token_count": formula_repeat_metrics["repeat_underuse_token_count"],
            "formula_repeat_underuse_mass": formula_repeat_metrics["repeat_underuse_mass"],
            "formula_repeat_overuse_examples": formula_repeat_metrics["repeat_overuse_examples"],
            "full_surface_content_token_multiset_recall": full_repeat_metrics["multiset_recall"],
            "full_surface_content_token_multiset_precision": full_repeat_metrics["multiset_precision"],
            "full_surface_repeat_overuse_token_count": full_repeat_metrics["repeat_overuse_token_count"],
            "full_surface_repeat_overuse_mass": full_repeat_metrics["repeat_overuse_mass"],
            "full_surface_repeat_underuse_token_count": full_repeat_metrics["repeat_underuse_token_count"],
            "full_surface_repeat_underuse_mass": full_repeat_metrics["repeat_underuse_mass"],
            "full_surface_repeat_overuse_examples": full_repeat_metrics["repeat_overuse_examples"],
            "source_to_formula_token_gap_count": len(reference_token_set - formula_tokens),
            "source_to_full_surface_token_gap_count": len(reference_token_set - full_tokens),
            "source_content_tokens_missing_from_formula": sorted(reference_token_set - formula_tokens)[:50],
            "source_content_tokens_missing_from_full_surface": sorted(reference_token_set - full_tokens)[:50],
        },
        "source_vs_normalized": {
            "source_excerpt_content_token_count": len(source_excerpt_token_set),
            "source_excerpt_content_token_mass": source_excerpt_content_mass,
            "normalized_content_token_count": len(normalized_token_set),
            "normalized_content_token_mass": reference_content_mass,
            "normalized_clause_count": normalized_clause_count,
            "normalized_content_token_recall_from_source": (
                len(source_vs_normalized_overlap) / len(source_excerpt_token_set) if source_excerpt_token_set else 1.0
            ),
            "normalized_content_token_precision_to_source": (
                len(source_vs_normalized_overlap) / len(normalized_token_set) if normalized_token_set else 1.0
            ),
            "normalized_content_token_jaccard": source_vs_normalized_jaccard,
            "normalized_content_token_multiset_recall_from_source": source_vs_normalized_repeat_metrics["multiset_recall"],
            "normalized_content_token_multiset_precision_to_source": source_vs_normalized_repeat_metrics["multiset_precision"],
            "source_to_normalized_token_gap_count": len(source_excerpt_token_set - normalized_token_set),
            "normalized_to_source_new_token_count": len(normalized_token_set - source_excerpt_token_set),
            "normalized_repeat_overuse_token_count": source_vs_normalized_repeat_metrics["repeat_overuse_token_count"],
            "normalized_repeat_overuse_mass": source_vs_normalized_repeat_metrics["repeat_overuse_mass"],
            "normalized_repeat_underuse_token_count": source_vs_normalized_repeat_metrics["repeat_underuse_token_count"],
            "normalized_repeat_underuse_mass": source_vs_normalized_repeat_metrics["repeat_underuse_mass"],
            "normalized_repeat_overuse_examples": source_vs_normalized_repeat_metrics["repeat_overuse_examples"],
            "normalized_length_ratio_vs_source_mass": (
                reference_content_mass / source_excerpt_content_mass if source_excerpt_content_mass else None
            ),
            "normalized_content_mass_per_clause": (reference_content_mass / normalized_clause_count_safe),
            "source_normalized_bertscore_precision": source_vs_normalized_bertscore.get("precision"),
            "source_normalized_bertscore_recall": source_vs_normalized_bertscore.get("recall"),
            "source_normalized_bertscore_f1": source_vs_normalized_bertscore.get("f1"),
            "normalized_implies_source_entailment": nli_normalized_to_source.get("entailment"),
            "source_implies_normalized_entailment": nli_source_to_normalized.get("entailment"),
            "source_vs_normalized_contradiction_score": source_vs_normalized_contradiction_score,
        },
        "semantic_preservation": semantic_preservation,
        "definition_quality": {
            "focus_term_explicitly_modeled": int(focus_term_explicitly_modeled),
            "focus_term_in_top_level_decl": int(focus_term_in_top_level_decl),
            "focus_term_in_formula_body": int(focus_term_in_formula_body),
            "declaration_only_downgrade_flag": int(bool(not assertions and normalized_clause_count > 0)),
            "definition_body_present": int(bool(assertions)),
            "vacuous_constraint_flag": int(reflexive_equality_count > 0),
            "reflexive_equality_count": reflexive_equality_count,
        },
        "compression": {
            "notes_token_count": len(prose_word_tokens),
            "notes_content_token_count": len(prose_tokens),
            "notes_to_formula_content_ratio": (len(prose_tokens) / max(1, len(formula_tokens))),
        },
        "identifier_glue": identifier_glue,
        "parameterization": parameterization,
        "assertion_complexity": assertion_complexity,
        "normalized_alignment": normalized_alignment,
        "normalized_relative": {
            "new_formula_content_token_rate_vs_reference_mass": (
                len(new_formula_content_tokens_text_prelude_advisory) / reference_content_mass
                if reference_content_mass
                else None
            ),
            "new_full_surface_content_token_rate_vs_reference_mass": (
                len(new_full_content_tokens_text_prelude_advisory) / reference_content_mass
                if reference_content_mass
                else None
            ),
            "formula_repeat_overuse_rate": (
                formula_repeat_metrics["repeat_overuse_mass"] / reference_content_mass
                if reference_content_mass
                else None
            ),
            "full_surface_repeat_overuse_rate": (
                full_repeat_metrics["repeat_overuse_mass"] / reference_content_mass
                if reference_content_mass
                else None
            ),
            "parameter_slot_mass_per_clause": (
                parameterization["total_parameter_slot_mass"] / normalized_clause_count_safe
            ),
            "parameter_slot_mass_per_reference_token": (
                parameterization["total_parameter_slot_mass"] / reference_content_mass if reference_content_mass else None
            ),
            "factorization_per_clause": (parameterization["factorization_count"] / normalized_clause_count_safe),
            "factorization_per_reference_token": (
                parameterization["factorization_count"] / reference_content_mass if reference_content_mass else None
            ),
            "notes_content_token_rate_vs_reference_mass": (
                len(prose_tokens) / reference_content_mass if reference_content_mass else None
            ),
        },
        "tradeoff": {
            "render_bertscore_f1_to_normalized_per_parameter_slot_mass": _per(
                bert_normalized.get("f1"),
                parameter_slot_mass,
            ),
            "render_bertscore_f1_to_source_per_parameter_slot_mass": _per(
                bert_source.get("f1"),
                parameter_slot_mass,
            ),
            "render_nli_ir_implies_text_per_parameter_slot_mass": _per(
                nli_render_to_normalized.get("entailment"),
                parameter_slot_mass,
            ),
            "render_nli_text_implies_ir_per_parameter_slot_mass": _per(
                nli_normalized_to_render.get("entailment"),
                parameter_slot_mass,
            ),
            "render_bertscore_f1_to_normalized_per_formula_repeat_overuse_mass": _per(
                bert_normalized.get("f1"),
                formula_repeat_overuse_mass,
            ),
            "render_nli_text_implies_ir_per_formula_repeat_overuse_mass": _per(
                nli_normalized_to_render.get("entailment"),
                formula_repeat_overuse_mass,
            ),
            "render_nli_ir_implies_text_per_formula_repeat_overuse_mass": _per(
                nli_render_to_normalized.get("entailment"),
                formula_repeat_overuse_mass,
            ),
            "render_bertscore_f1_to_normalized_per_full_surface_repeat_overuse_mass": _per(
                bert_normalized.get("f1"),
                full_surface_repeat_overuse_mass,
            ),
            "render_nli_text_implies_ir_per_full_surface_repeat_overuse_mass": _per(
                nli_normalized_to_render.get("entailment"),
                full_surface_repeat_overuse_mass,
            ),
            "pairwise_structure_similarity_mean_per_parameter_slot_mass": _per(
                float(pairwise_structure_similarity_mean) if isinstance(pairwise_structure_similarity_mean, (int, float)) else None,
                parameter_slot_mass,
            ),
            "focus_signature_mode_share_per_parameter_slot_mass": _per(
                float(variant_variability.get("focus_signature_mode_share"))
                if isinstance(variant_variability.get("focus_signature_mode_share"), (int, float))
                else None,
                parameter_slot_mass,
            ),
        },
        "variants": {
            "candidate_reading_count": len(advisory.get("candidate_readings", []) or []),
            "draft_variant_count": len(variants),
            "unique_ir_variant_count": len(variant_signatures) if variant_signatures else int(bool(formula_surface)),
            "critic_selected_reading_id": str(critic.get("selected_reading_id", "")).strip(),
            "critic_selected_reading_label": str(critic.get("selected_reading_label", "")).strip(),
            "critic_confidence_label": confidence_label,
            "critic_confidence_score": _CONFIDENCE_TO_SCORE.get(confidence_label),
            "critic_merge_recommended": bool(critic.get("merge_recommended", False)),
        },
        "variability": variant_variability,
        "efficiency": {
            "observable_llm_call_lower_bound": observable_llm_call_lower_bound,
            "qa_json_attempt_count": qa_attempts,
            "critic_json_attempt_count": critic_attempts,
            "advisor_assistant_turn_count_lower_bound": advisor_call_lb,
            "selected_drafter_assistant_turn_count_lower_bound": selected_drafter_call_lb,
            "wall_clock_seconds": None,
            "max_call_latency_s": None,
        },
        "render_back": {
            "render_back_mode": "deterministic_proxy",
            "render_back_metric_status": (
                "proxy_only_until_llm_verbalizer_runs"
                if include_semantic_models
                else "semantic_models_skipped_for_deterministic_candidate_scoring"
            ),
            "render_back_text": render_back_text,
            "render_bertscore_precision_to_normalized": bert_normalized.get("precision"),
            "render_bertscore_recall_to_normalized": bert_normalized.get("recall"),
            "render_bertscore_f1_to_normalized": bert_normalized.get("f1"),
            "render_bertscore_precision_to_source": bert_source.get("precision"),
            "render_bertscore_recall_to_source": bert_source.get("recall"),
            "render_bertscore_f1_to_source": bert_source.get("f1"),
            "render_nli_ir_implies_text": nli_render_to_normalized.get("entailment"),
            "render_nli_text_implies_ir": nli_normalized_to_render.get("entailment"),
            "render_nli_ir_implies_source": nli_render_to_source.get("entailment"),
            "render_nli_source_implies_ir": nli_source_to_render.get("entailment"),
            "render_nli_render_to_normalized": nli_render_to_normalized,
            "render_nli_normalized_to_render": nli_normalized_to_render,
            "render_nli_render_to_source": nli_render_to_source,
            "render_nli_source_to_render": nli_source_to_render,
            "render_contradiction_score": render_contradiction_score,
        },
        "silver_reference": {
            "disabled_for_manual_reference": disable_silver_reference,
            "silver_reference_found": bool(silver_reference.get("found")),
            "silver_reference_path": silver_reference.get("path"),
            "silver_reference_ir": silver_reference.get("reference_ir"),
            **silver_structure,
        },
    }
    return metrics


def _render_metrics_md(metrics: dict[str, Any]) -> str:
    lines = [
        f"# Translation Metrics v1 - {metrics.get('entry_id', '')}",
        "",
        f"- generated_at: `{metrics.get('generated_at', '')}`",
        f"- artifact_path: `{metrics.get('artifact_path', '')}`",
        f"- catalog_version: `{metrics.get('catalog_version', '')}`",
        "",
    ]
    for section in (
        "validity",
        "grounding",
        "coverage",
        "lexical_coverage",
        "source_vs_normalized",
        "semantic_preservation",
        "definition_quality",
        "compression",
        "identifier_glue",
        "parameterization",
        "assertion_complexity",
        "normalized_alignment",
        "normalized_relative",
        "tradeoff",
        "variants",
        "variability",
        "efficiency",
        "render_back",
        "silver_reference",
    ):
        lines.extend(
            [
                f"## {section}",
                "",
                "```json",
                json.dumps(metrics.get(section, {}), ensure_ascii=False, indent=2),
                "```",
                "",
            ]
        )
    return "\n".join(lines)


def _metrics_stem_for_artifact(artifact_json_path: Path) -> str:
    stem = artifact_json_path.stem
    for suffix in (
        "_questioner_answerer_to_ir_experiment",
        "_advisor_drafter_experiment",
        "_ontology_then_ir_experiment",
        "_external_ontology_to_ir_experiment",
        "_cqbycq_to_ir_experiment",
    ):
        stem = stem.replace(suffix, "")
    return stem


def write_metrics_artifacts(
    artifact_json_path: Path,
    payload: dict[str, Any] | None = None,
    *,
    include_semantic_models: bool = True,
) -> tuple[Path, Path, dict[str, Any]]:
    resolved_payload = payload or json.loads(artifact_json_path.read_text(encoding="utf-8"))
    metrics = compute_metrics(resolved_payload, include_semantic_models=include_semantic_models)
    metrics["artifact_path"] = str(artifact_json_path)
    stem = _metrics_stem_for_artifact(artifact_json_path)
    out_json = artifact_json_path.parent / f"{stem}_metrics_v1.json"
    out_md = artifact_json_path.parent / f"{stem}_metrics_v1.md"
    _save_json(out_json, metrics)
    out_md.write_text(_render_metrics_md(metrics), encoding="utf-8")
    return out_json, out_md, metrics


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Compute translation metrics v1 for an existing QA->IR artifact.")
    parser.add_argument("--artifact-json", type=Path, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    out_json, out_md, _ = write_metrics_artifacts(args.artifact_json)
    print(str(out_json))
    print(str(out_md))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
