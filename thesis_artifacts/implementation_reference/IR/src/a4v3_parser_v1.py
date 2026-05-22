"""a4v3_parser_v1.py

Single canonical parser for a4v3 IR text. Knows the full 12-INNF-family
vocabulary per `thoughts/IR_schema/a4v3_full_48.md`:

  TypeDecl         sort (opaque/enum/subtype), struct (record)
  SymbolDecl       entity, val, fun, rel, event, var, property
  AssertDecl       fact, constraint, axiom, key, disjoint, init
  PathDecl         path
  ActionDecl       action ... guard / effect / frame / unchanged
  TemporalDecl     prop, fairness
  DeonticDecl      obligation, permission, prohibition
  ValidationDecl   target, closed, deactivated, sparql_constraint
  ProbabilisticDecl  dist / distribution, reward, utility, objective
  GameDecl         obs, indist
  GraphDecl        dataset, reify
  TheoremDecl      theorem, checked

Reuses the existing expression parser (`ExprParser`) from the legacy
`compute_manual_section_workspace_metrics_v1` module for body expressions.

Output AST (dict):

  {
    "version": "a4v3_parsed_v1",
    "declarations": [Decl, ...],
    "assertions":   [AssertDecl, ...],   # subset of declarations,
                                          # separated for ease of legacy use
    "raw_text": str,
    "warnings": [{"line_no": int, "message": str}],
  }

Each Decl is `{family, kind, name, line_no, raw, ...family-specific}`.

Adapters:
  to_legacy_ast(ast)        — emit the V6 `_parse_manual_ir_to_ast` shape
                              for backward-compat consumers.
  to_named_buckets(ast)     — flat lists by category for grounding-check etc.

CLI:
  python a4v3_parser_v1.py <a4v3_file>
"""
from __future__ import annotations
import json
import pathlib
import re
import sys
from dataclasses import dataclass
from typing import Any

# Reuse legacy ExprParser for body expression parsing.
sys.path.insert(0, str(pathlib.Path(__file__).parent / "legacy_metrics"))
from compute_manual_section_workspace_metrics_v1 import (  # noqa: E402
    ExprParser, IrParseError, _split_top_level,
)


PARSER_VERSION = "a4v3_parsed_v1"


class A4v3ParseError(RuntimeError):
    pass


# ─────────────────────────────────────────────────────────────────────────
# Top-level keyword sets — drive the block splitter
# ─────────────────────────────────────────────────────────────────────────

# Top-level a4v3 declaration keywords — sourced from canonical spec via
# `a4v3_grammar.block_keywords()` covering all 12 INNF families.
def _load_block_keywords() -> tuple[str, ...]:
    from a4v3_grammar import block_keywords  # noqa: E402
    # Plus body-less decl modifiers (Family #6) that appear at line start.
    extras = ("opaque", "abstract", "declare")
    return tuple(sorted(set(block_keywords()) | set(extras)))


_BLOCK_KEYWORDS: tuple[str, ...] = _load_block_keywords()

_BLOCK_KW_RE = re.compile(
    r"^(?P<kw>" + "|".join(_BLOCK_KEYWORDS) + r")(?:\s|\b|$)"
)

_NAME_RE = r"[A-Za-z_][A-Za-z0-9_]*"


# ─────────────────────────────────────────────────────────────────────────
# Comments + blank-line handling
# ─────────────────────────────────────────────────────────────────────────

def _strip_comments(text: str) -> str:
    out: list[str] = []
    for line in text.splitlines():
        # Comments: lines starting with `--`, `//`, or `#` are full-line
        # comments. Inline `--` and whitespace-prefixed `//` are also stripped
        # for end-of-line annotations. Do not split inside URLs like
        # `https://...`, where `//` is not preceded by whitespace.
        stripped = line.lstrip()
        if stripped.startswith("--") or stripped.startswith("//") or stripped.startswith("#"):
            out.append("")  # preserve line numbering
            continue
        if "--" in line:
            line = line.split("--", 1)[0].rstrip()
        slash_comment = re.search(r"(^|\s)//", line)
        if slash_comment:
            line = line[:slash_comment.start()].rstrip()
        out.append(line)
    return "\n".join(out)


# ─────────────────────────────────────────────────────────────────────────
# Block splitter — one logical declaration per block, multi-line aware
# ─────────────────────────────────────────────────────────────────────────

def _is_block_start(line: str) -> bool:
    """A line that begins (no indent) with a known top-level keyword."""
    if not line or line[0].isspace():
        return False
    # Keyed continuation fields may appear flush-left in hand-written IR.
    # They are not top-level declarations even when the key is also a block
    # keyword (notably `action:` inside DeonticDecl vs `action Name(...)`).
    if re.match(r"^(action|agent|target|scope|deadline|context|decision|determination|guard|effect|parameters|reference|source)\s*:", line.strip()):
        return False
    return bool(_BLOCK_KW_RE.match(line.strip()))


def _split_blocks(text: str) -> list[dict[str, Any]]:
    """Split a4v3 text into list of {start_line: int, lines: list[str], raw: str}.

    A block starts at a line whose first non-whitespace token is a known
    top-level keyword. The block continues until the next such line or EOF.
    Empty lines are kept inside blocks (they may appear between e.g.
    constraint clauses) but trailing blanks are trimmed.
    """
    raw_lines = text.splitlines()
    blocks: list[dict[str, Any]] = []
    current: list[tuple[int, str]] = []
    start_line = 0
    for i, line in enumerate(raw_lines, start=1):
        if _is_block_start(line):
            if current:
                # flush previous block
                blocks.append({
                    "start_line": start_line,
                    "lines": [ln for _, ln in current],
                    "raw": "\n".join(ln for _, ln in current).rstrip(),
                })
            current = [(i, line)]
            start_line = i
            continue
        # continuation: belongs to the most recent block (if any)
        if current:
            current.append((i, line))
        # else: floating line outside any block — silently discarded
    if current:
        blocks.append({
            "start_line": start_line,
            "lines": [ln for _, ln in current],
            "raw": "\n".join(ln for _, ln in current).rstrip(),
        })
    return blocks


# ─────────────────────────────────────────────────────────────────────────
# Per-family declaration parsers
# ─────────────────────────────────────────────────────────────────────────

def _flatten_block(block_lines: list[str]) -> str:
    """Join multi-line block into a single space-separated string for parsing.

    This collapses indented continuation lines (used for sort enum
    `| Member`, DeonticDecl `action: ...`, ActionDecl `effect: ...`) into a
    single line so per-family regex parsers can match.
    """
    pieces: list[str] = []
    for line in block_lines:
        line = line.rstrip()
        if not line.strip():
            continue
        pieces.append(line.strip())
    return " ".join(pieces)


# ── TypeDecl ──

_SORT_HEAD_RE = re.compile(rf"^sort\s+(?P<name>{_NAME_RE})\s*(?P<rest>.*)$")
_STRUCT_HEAD_RE = re.compile(rf"^struct\s+(?P<name>{_NAME_RE})\s*\{{(?P<body>[^}}]*)\}}\s*$")


def _parse_type_decl(block: dict) -> dict:
    flat = _flatten_block(block["lines"])
    if flat.startswith("struct "):
        m = _STRUCT_HEAD_RE.match(flat)
        if not m:
            raise A4v3ParseError(f"line {block['start_line']}: bad struct decl: {flat[:80]}")
        body = m.group("body").strip()
        fields: list[dict] = []
        for f in _split_top_level(body, sep=","):
            if ":" not in f:
                raise A4v3ParseError(f"struct field needs `name: type`: {f}")
            fname, ftype = [x.strip() for x in f.split(":", 1)]
            fields.append({"name": fname, "type": ftype})
        return {
            "family": "TypeDecl", "kind": "record", "name": m.group("name"),
            "fields": fields,
            "line_no": block["start_line"], "raw": block["raw"],
        }

    m = _SORT_HEAD_RE.match(flat)
    if not m:
        raise A4v3ParseError(f"line {block['start_line']}: bad sort decl: {flat[:80]}")
    name = m.group("name")
    rest = m.group("rest").strip()

    if rest.startswith("extends") or rest.startswith("<"):
        parent = rest[len("extends"):].strip() if rest.startswith("extends") else rest[1:].strip()
        return {
            "family": "TypeDecl", "kind": "subtype", "name": name, "parent": parent,
            "line_no": block["start_line"], "raw": block["raw"],
        }
    if rest.startswith("="):
        rhs = rest[1:].strip()
        # enum members may span lines (collapsed in flat) and start with `|`
        members = [p.strip() for p in rhs.split("|") if p.strip()]
        return {
            "family": "TypeDecl", "kind": "enum", "name": name,
            "enum_members": members,
            "line_no": block["start_line"], "raw": block["raw"],
        }
    return {
        "family": "TypeDecl", "kind": "opaque", "name": name,
        "line_no": block["start_line"], "raw": block["raw"],
    }


# ── SymbolDecl ──

_ENTITY_RE = re.compile(rf"^entity\s+(?P<name>{_NAME_RE})\s*:\s*(?P<sort>{_NAME_RE})\s*$")
_VAL_RE = re.compile(rf"^val\s+(?P<name>{_NAME_RE})\s*:\s*(?P<sort>{_NAME_RE})(?:\s*=\s*(?P<value>.+))?\s*$")
_FUN_RE = re.compile(
    rf"^fun(?:\[(?P<flags>[^\]]+)\])?\s+(?P<name>{_NAME_RE})\s*:\s*(?P<sig>.+)$"
)
_REL_RE = re.compile(rf"^rel\s+(?P<name>{_NAME_RE})\s*:\s*(?P<sig>.+)$")
_REL_EXT_RE = re.compile(rf"^rel\s+(?P<name>{_NAME_RE})\s+extends\s+(?P<parent>{_NAME_RE})\s*$")
_EVENT_RE = re.compile(
    rf"^event\s+(?P<name>{_NAME_RE})(?:\((?P<params>[^)]*)\))?\s*$"
)
_VAR_RE = re.compile(
    rf"^var\s+(?P<name>{_NAME_RE})\s*:\s*(?P<rest>.+)$"
)
_PROPERTY_RE = re.compile(
    rf"^property\s+(?P<name>{_NAME_RE})\s*:\s*(?P<chars>.+)$"
)


def _parse_symbol_decl(block: dict) -> dict:
    flat = _flatten_block(block["lines"])

    if m := _ENTITY_RE.match(flat):
        return {
            "family": "SymbolDecl", "kind": "entity",
            "name": m.group("name"), "sort": m.group("sort"),
            "line_no": block["start_line"], "raw": block["raw"],
        }
    if m := _VAL_RE.match(flat):
        return {
            "family": "SymbolDecl", "kind": "const",
            "name": m.group("name"), "sort": m.group("sort"),
            "value_text": (m.group("value") or "").strip() or None,
            "line_no": block["start_line"], "raw": block["raw"],
        }
    if m := _REL_EXT_RE.match(flat):
        return {
            "family": "SymbolDecl", "kind": "rel",
            "name": m.group("name"), "args": [],
            "parents": [m.group("parent")],
            "line_no": block["start_line"], "raw": block["raw"],
        }
    if m := _FUN_RE.match(flat):
        sig = m.group("sig").strip()
        if "->" in sig:
            lhs, ret = [p.strip() for p in sig.rsplit("->", 1)]
            args = [p.strip() for p in _split_top_level(lhs, sep=",")] if lhs else []
        else:
            args = []
            ret = sig.strip()
        return {
            "family": "SymbolDecl", "kind": "fun", "name": m.group("name"),
            "args": args, "result_sort": ret,
            "flags": (m.group("flags") or "").strip() or None,
            "line_no": block["start_line"], "raw": block["raw"],
        }
    if m := _REL_RE.match(flat):
        sig = m.group("sig").strip()
        args = [p.strip() for p in _split_top_level(sig, sep=",")] if sig else []
        return {
            "family": "SymbolDecl", "kind": "rel", "name": m.group("name"),
            "args": args,
            "line_no": block["start_line"], "raw": block["raw"],
        }
    if m := _EVENT_RE.match(flat):
        params_text = (m.group("params") or "").strip()
        params: list[dict] = []
        for p in _split_top_level(params_text, sep=","):
            if ":" in p:
                pname, ptype = [x.strip() for x in p.split(":", 1)]
                params.append({"name": pname, "type": ptype})
        return {
            "family": "SymbolDecl", "kind": "event", "name": m.group("name"),
            "params": params,
            "line_no": block["start_line"], "raw": block["raw"],
        }
    if m := _VAR_RE.match(flat):
        return {
            "family": "SymbolDecl", "kind": "var", "name": m.group("name"),
            "sig_text": m.group("rest").strip(),
            "line_no": block["start_line"], "raw": block["raw"],
        }
    if m := _PROPERTY_RE.match(flat):
        chars = [c.strip() for c in m.group("chars").split("|") if c.strip()]
        return {
            "family": "SymbolDecl", "kind": "property", "name": m.group("name"),
            "characteristics": chars,
            "line_no": block["start_line"], "raw": block["raw"],
        }

    # Body-less / opaque / abstract / declare
    for kw in ("opaque", "abstract", "declare"):
        if flat.startswith(kw + " "):
            after = flat[len(kw):].strip()
            m = re.match(rf"^(?P<name>{_NAME_RE})\s*:\s*(?P<sig>.+)$", after)
            if m:
                return {
                    "family": "SymbolDecl", "kind": "body_less",
                    "name": m.group("name"),
                    "sig_text": m.group("sig").strip(),
                    "openness": kw,
                    "line_no": block["start_line"], "raw": block["raw"],
                }

    raise A4v3ParseError(f"line {block['start_line']}: unparseable symbol decl: {flat[:100]}")


# ── AssertDecl ──

_ASSERT_METADATA_RE = re.compile(
    rf"^\[\s*realizes\s*:\s*(?P<realizes>{_NAME_RE})\s*\]\s*$"
)
_BODY_HEADER_RE = re.compile(
    rf"^(?P<kw>fact|constraint|axiom|init)\s+(?P<name>{_NAME_RE})"
    rf"(?:\s*(?P<metadata>\[[^\]]*\]))?\s*:\s*(?P<body>.*)$",
    re.DOTALL,
)
_KEY_RE = re.compile(
    rf"^key\s*\[\s*(?P<role>identity|validation)\s*\]\s+(?P<sort>{_NAME_RE})\s+by\s+(?P<prop>.+?)\s*$"
)
_DISJOINT_RE = re.compile(r"^disjoint\s+(?P<sorts>.+)$")
_INIT_BLOCK_RE = re.compile(r"^init\s*\{(?P<body>.*)\}\s*$", re.DOTALL)


def _parse_assert_metadata(text: str | None, line_no: int) -> dict[str, str]:
    text = (text or "").strip()
    if not text:
        return {}
    if m := _ASSERT_METADATA_RE.match(text):
        return {"realizes": m.group("realizes")}
    raise A4v3ParseError(
        f"line {line_no}: unsupported assertion metadata: {text[:80]}"
    )


def _parse_assert_decl(block: dict) -> dict:
    flat = _flatten_block(block["lines"])

    if m := _KEY_RE.match(flat):
        return {
            "family": "AssertDecl", "kind": "key", "role": m.group("role"),
            "name": f"{m.group('sort')}_key",
            "sort": m.group("sort"), "property_name": m.group("prop").strip(),
            "line_no": block["start_line"], "raw": block["raw"],
        }
    if m := _DISJOINT_RE.match(flat):
        sorts = [s.strip() for s in m.group("sorts").split(",") if s.strip()]
        return {
            "family": "AssertDecl", "kind": "disjoint",
            "name": "disjoint_" + "_".join(sorts),
            "sorts": sorts,
            "line_no": block["start_line"], "raw": block["raw"],
        }
    if m := _INIT_BLOCK_RE.match(flat):
        return {
            "family": "AssertDecl", "kind": "init",
            "name": "init",
            "body_text": m.group("body").strip(),
            "line_no": block["start_line"], "raw": block["raw"],
        }
    if m := _BODY_HEADER_RE.match(flat):
        kw = m.group("kw")
        name = m.group("name")
        metadata = _parse_assert_metadata(m.group("metadata"), block["start_line"])
        body_text = m.group("body").strip()
        expr: Any = None
        expr_error: str | None = None
        if body_text:
            try:
                expr = ExprParser(body_text).parse()
            except IrParseError as e:
                expr_error = str(e)
        decl = {
            "family": "AssertDecl", "kind": kw, "name": name,
            "metadata": metadata,
            "body_text": body_text, "expr": expr, "expr_error": expr_error,
            "line_no": block["start_line"], "raw": block["raw"],
        }
        if metadata.get("realizes"):
            decl["realizes"] = metadata["realizes"]
        return decl
    raise A4v3ParseError(f"line {block['start_line']}: unparseable AssertDecl: {flat[:100]}")


# ── PathDecl ──

_PATH_RE = re.compile(rf"^path\s+(?P<name>{_NAME_RE})\s*=\s*(?P<expr>.+)$")


def _parse_path_decl(block: dict) -> dict:
    flat = _flatten_block(block["lines"])
    m = _PATH_RE.match(flat)
    if not m:
        raise A4v3ParseError(f"line {block['start_line']}: bad path decl: {flat[:80]}")
    return {
        "family": "PathDecl", "kind": "path",
        "name": m.group("name"), "expr_text": m.group("expr").strip(),
        "line_no": block["start_line"], "raw": block["raw"],
    }


# ── ActionDecl ──

_ACTION_HEAD_RE = re.compile(
    rf"^action\s+(?P<name>{_NAME_RE})\s*\((?P<params>[^)]*)\)\s*"
)


def _parse_action_decl(block: dict) -> dict:
    flat = _flatten_block(block["lines"])
    m = _ACTION_HEAD_RE.match(flat)
    if not m:
        raise A4v3ParseError(f"line {block['start_line']}: bad action decl: {flat[:80]}")
    rest = flat[m.end():]
    params_text = (m.group("params") or "").strip()
    params: list[dict] = []
    for p in _split_top_level(params_text, sep=","):
        if ":" in p:
            pname, ptype = [x.strip() for x in p.split(":", 1)]
            params.append({"name": pname, "type": ptype})
    fields = _parse_keyed_continuation(rest, ("guard", "effect", "frame",
                                                "unchanged", "pre_state", "post_state"))
    return {
        "family": "ActionDecl", "kind": "action", "name": m.group("name"),
        "params": params, **fields,
        "line_no": block["start_line"], "raw": block["raw"],
    }


# ── TemporalDecl ──

_PROP_RE = re.compile(rf"^prop\s+(?P<name>{_NAME_RE})\s*:\s*(?P<body>.+)$", re.DOTALL)
_FAIRNESS_RE = re.compile(rf"^fairness\s+(?P<name>{_NAME_RE})\s*:\s*(?P<body>.+)$",
                          re.DOTALL)
def _build_temporal_op_re() -> re.Pattern:
    """Sourced from canonical a4v3 spec — TemporalDecl kinds excluding 'fairness'.
    `fairness` is its own block-keyword (handled separately). The remaining
    kinds (always, eventually, once, next, until, since) appear as body
    operators preceding `(...)`."""
    from a4v3_grammar import temporal_kinds  # noqa: E402
    body_ops = [k for k in temporal_kinds() if k != "fairness"]
    if not body_ops:
        body_ops = ["always", "eventually", "once", "next"]
    return re.compile(rf"^(?P<op>{'|'.join(body_ops)})\s*\(")


_TEMPORAL_OP_RE = _build_temporal_op_re()


def _parse_temporal_decl(block: dict) -> dict:
    flat = _flatten_block(block["lines"])
    if m := _PROP_RE.match(flat):
        body = m.group("body").strip()
        op = "unknown"
        if op_m := _TEMPORAL_OP_RE.match(body):
            op = op_m.group("op")
        return {
            "family": "TemporalDecl", "kind": op or "prop",
            "name": m.group("name"), "body_text": body,
            "line_no": block["start_line"], "raw": block["raw"],
        }
    if m := _FAIRNESS_RE.match(flat):
        return {
            "family": "TemporalDecl", "kind": "fairness",
            "name": m.group("name"),
            "body_text": m.group("body").strip(),
            "line_no": block["start_line"], "raw": block["raw"],
        }
    raise A4v3ParseError(f"line {block['start_line']}: bad TemporalDecl: {flat[:80]}")


# ── DeonticDecl ──

_DEONTIC_HEAD_RE = re.compile(
    rf"^(?P<kw>obligation|permission|prohibition)\s+(?P<name>{_NAME_RE})"
    r"(?:\s*\((?P<params>[^)]*)\))?\s*"
)


def _parse_deontic_decl(block: dict) -> dict:
    flat = _flatten_block(block["lines"])
    m = _DEONTIC_HEAD_RE.match(flat)
    if not m:
        raise A4v3ParseError(f"line {block['start_line']}: bad DeonticDecl: {flat[:80]}")
    rest = flat[m.end():]
    params_text = (m.group("params") or "").strip()
    params: list[dict] = []
    agent_sort = None
    target_sort = None
    for p in _split_top_level(params_text, sep=","):
        if ":" in p:
            pname, ptype = [x.strip() for x in p.split(":", 1)]
            params.append({"name": pname, "type": ptype})
            if pname == "agent":
                agent_sort = ptype
            elif pname == "target":
                target_sort = ptype
    fields = _parse_keyed_continuation(rest, (
        "action", "deadline", "scope", "exception", "priority", "modality",
        "guard", "effect", "parameters", "applies_to", "reference",
        "on_section", "recipient", "source", "notice_min",
    ))
    return {
        "family": "DeonticDecl", "kind": m.group("kw"), "name": m.group("name"),
        "agent_sort": agent_sort, "target_sort": target_sort, "params": params,
        **fields,
        "line_no": block["start_line"], "raw": block["raw"],
    }


# ── ValidationDecl ──

_VALIDATION_HEAD_RE = re.compile(
    rf"^(?P<kw>target|closed|deactivated|sparql_constraint)\s+(?P<name>{_NAME_RE})\s*:?\s*(?P<rest>.*)$"
)


def _parse_validation_decl(block: dict) -> dict:
    flat = _flatten_block(block["lines"])
    m = _VALIDATION_HEAD_RE.match(flat)
    if not m:
        raise A4v3ParseError(f"line {block['start_line']}: bad ValidationDecl: {flat[:80]}")
    return {
        "family": "ValidationDecl", "kind": m.group("kw"),
        "name": m.group("name"),
        "rest_text": m.group("rest").strip(),
        "line_no": block["start_line"], "raw": block["raw"],
    }


# ── ProbabilisticDecl ──

_PROB_HEAD_RE = re.compile(
    rf"^(?P<kw>dist|distribution|reward|utility|objective)\s+(?P<name>{_NAME_RE})\s*:?\s*(?P<rest>.*)$"
)


def _parse_probabilistic_decl(block: dict) -> dict:
    flat = _flatten_block(block["lines"])
    m = _PROB_HEAD_RE.match(flat)
    if not m:
        raise A4v3ParseError(f"line {block['start_line']}: bad ProbabilisticDecl: {flat[:80]}")
    kw = m.group("kw")
    if kw == "dist":
        kw = "distribution"
    return {
        "family": "ProbabilisticDecl", "kind": kw, "name": m.group("name"),
        "rest_text": m.group("rest").strip(),
        "line_no": block["start_line"], "raw": block["raw"],
    }


# ── GameDecl ──

def _parse_game_decl(block: dict) -> dict:
    flat = _flatten_block(block["lines"])
    if flat.startswith("obs"):
        return {
            "family": "GameDecl", "kind": "observation",
            "name": "obs", "rest_text": flat[3:].strip(),
            "line_no": block["start_line"], "raw": block["raw"],
        }
    if flat.startswith("indist"):
        return {
            "family": "GameDecl", "kind": "indist",
            "name": "indist", "rest_text": flat[6:].strip(),
            "line_no": block["start_line"], "raw": block["raw"],
        }
    raise A4v3ParseError(f"line {block['start_line']}: bad GameDecl: {flat[:80]}")


# ── GraphDecl ──

_DATASET_RE = re.compile(rf"^dataset\s+(?P<name>{_NAME_RE})\s*\{{(?P<body>[^}}]*)\}}\s*$")
_REIFY_RE = re.compile(rf"^reify\s+(?P<name>{_NAME_RE})\s*:\s*(?P<body>.+)$")


def _parse_graph_decl(block: dict) -> dict:
    flat = _flatten_block(block["lines"])
    if m := _DATASET_RE.match(flat):
        return {
            "family": "GraphDecl", "kind": "dataset", "name": m.group("name"),
            "body_text": m.group("body").strip(),
            "line_no": block["start_line"], "raw": block["raw"],
        }
    if m := _REIFY_RE.match(flat):
        return {
            "family": "GraphDecl", "kind": "reification", "name": m.group("name"),
            "body_text": m.group("body").strip(),
            "line_no": block["start_line"], "raw": block["raw"],
        }
    raise A4v3ParseError(f"line {block['start_line']}: bad GraphDecl: {flat[:80]}")


# ── TheoremDecl ──

_THEOREM_RE = re.compile(rf"^theorem\s+(?P<name>{_NAME_RE})\s*:\s*(?P<body>.+)$",
                         re.DOTALL)
_CHECKED_RE = re.compile(rf"^checked\s+(?P<name>{_NAME_RE})\s*$")


def _parse_theorem_decl(block: dict) -> dict:
    flat = _flatten_block(block["lines"])
    if m := _THEOREM_RE.match(flat):
        return {
            "family": "TheoremDecl", "kind": "theorem", "name": m.group("name"),
            "body_text": m.group("body").strip(), "status": "open",
            "line_no": block["start_line"], "raw": block["raw"],
        }
    if m := _CHECKED_RE.match(flat):
        return {
            "family": "TheoremDecl", "kind": "checked", "name": m.group("name"),
            "status": "checked",
            "line_no": block["start_line"], "raw": block["raw"],
        }
    raise A4v3ParseError(f"line {block['start_line']}: bad TheoremDecl: {flat[:80]}")


# ── helper: parse colon-keyed continuation tail ──

def _parse_keyed_continuation(tail: str, known_keys: tuple[str, ...]) -> dict:
    """Parse `key1: value1 key2: value2 ...` where keys are a known set.

    The value of each key is everything from after `key:` up to the next
    known `key:` token or EOL. Used for DeonticDecl/ActionDecl bodies.
    """
    if not tail.strip():
        return {}
    keys_re = re.compile(
        r"\b(?P<key>" + "|".join(re.escape(k) for k in known_keys) + r")\s*:"
    )
    matches = list(keys_re.finditer(tail))
    out: dict[str, str] = {}
    for i, m in enumerate(matches):
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(tail)
        out[m.group("key")] = tail[start:end].strip().rstrip(";").strip()
    return out


# ─────────────────────────────────────────────────────────────────────────
# Family dispatch
# ─────────────────────────────────────────────────────────────────────────

_KW_TO_HANDLER = {
    "sort": _parse_type_decl,
    "struct": _parse_type_decl,
    "entity": _parse_symbol_decl,
    "val": _parse_symbol_decl,
    "fun": _parse_symbol_decl,
    "rel": _parse_symbol_decl,
    "event": _parse_symbol_decl,
    "var": _parse_symbol_decl,
    "property": _parse_symbol_decl,
    "opaque": _parse_symbol_decl,
    "abstract": _parse_symbol_decl,
    "declare": _parse_symbol_decl,
    "fact": _parse_assert_decl,
    "constraint": _parse_assert_decl,
    "axiom": _parse_assert_decl,
    "key": _parse_assert_decl,
    "disjoint": _parse_assert_decl,
    "init": _parse_assert_decl,
    "path": _parse_path_decl,
    "action": _parse_action_decl,
    "prop": _parse_temporal_decl,
    "fairness": _parse_temporal_decl,
    "obligation": _parse_deontic_decl,
    "permission": _parse_deontic_decl,
    "prohibition": _parse_deontic_decl,
    "target": _parse_validation_decl,
    "closed": _parse_validation_decl,
    "deactivated": _parse_validation_decl,
    "sparql_constraint": _parse_validation_decl,
    "dist": _parse_probabilistic_decl,
    "distribution": _parse_probabilistic_decl,
    "reward": _parse_probabilistic_decl,
    "utility": _parse_probabilistic_decl,
    "objective": _parse_probabilistic_decl,
    "obs": _parse_game_decl,
    "indist": _parse_game_decl,
    "dataset": _parse_graph_decl,
    "reify": _parse_graph_decl,
    "theorem": _parse_theorem_decl,
    "checked": _parse_theorem_decl,
}


def _dispatch_block(block: dict) -> dict:
    kw_match = _BLOCK_KW_RE.match(block["lines"][0].strip())
    if not kw_match:
        raise A4v3ParseError(
            f"line {block['start_line']}: cannot identify family for: {block['raw'][:80]}"
        )
    kw = kw_match.group("kw")
    handler = _KW_TO_HANDLER.get(kw)
    if not handler:
        raise A4v3ParseError(
            f"line {block['start_line']}: unhandled keyword {kw!r}"
        )
    return handler(block)


# ─────────────────────────────────────────────────────────────────────────
# Public API
# ─────────────────────────────────────────────────────────────────────────

def parse(ir_text: str, *, strict: bool = False) -> dict:
    """Parse a4v3 text into rich AST. If strict=False, individual block
    failures are recorded as warnings rather than raising."""
    cleaned = _strip_comments(ir_text)
    blocks = _split_blocks(cleaned)
    declarations: list[dict] = []
    assertions: list[dict] = []
    warnings: list[dict] = []

    for block in blocks:
        try:
            decl = _dispatch_block(block)
        except A4v3ParseError as e:
            if strict:
                raise
            warnings.append({
                "line_no": block["start_line"],
                "message": str(e),
                "raw": block["raw"][:120],
            })
            continue
        declarations.append(decl)
        if decl.get("family") == "AssertDecl":
            assertions.append(decl)

    return {
        "version": PARSER_VERSION,
        "declarations": declarations,
        "assertions": assertions,
        "warnings": warnings,
        "raw_text": ir_text,
    }


# ─────────────────────────────────────────────────────────────────────────
# Adapters
# ─────────────────────────────────────────────────────────────────────────

def to_legacy_ast(ast: dict) -> dict:
    """Emit the V6 `_parse_manual_ir_to_ast` shape — a flat list of decls
    (sort/entity/symbol with fun|rel kind) plus assertions list with
    constraint kind only. Extended families are dropped (legacy generator
    won't see them, but at least it won't crash)."""
    declarations: list[dict] = []
    assertions: list[dict] = []
    for d in ast["declarations"]:
        f, k = d["family"], d["kind"]
        if f == "TypeDecl":
            if k == "enum":
                declarations.append({"decl": "sort", "name": d["name"],
                                     "enum_members": d["enum_members"]})
            elif k == "subtype":
                declarations.append({"decl": "sort", "name": d["name"],
                                     "parent": d["parent"]})
            elif k == "opaque":
                declarations.append({"decl": "sort", "name": d["name"]})
            # struct: skip (V6 didn't model)
        elif f == "SymbolDecl":
            if k == "entity":
                declarations.append({"decl": "entity", "name": d["name"],
                                     "sort": d["sort"]})
            elif k == "fun":
                declarations.append({"decl": "symbol", "symbol_kind": "fun",
                                     "name": d["name"], "args": d.get("args", []),
                                     "result_sort": d.get("result_sort", "")})
            elif k == "rel":
                declarations.append({"decl": "symbol", "symbol_kind": "rel",
                                     "name": d["name"], "args": d.get("args", [])})
            # other SymbolDecl kinds (val/event/var/property/body_less): skip
        elif f == "AssertDecl" and k == "constraint":
            assertions.append({"decl": "assert", "assert_kind": "constraint",
                               "name": d["name"], "expr": d.get("expr")})
        # All other families silently dropped for legacy compat.
    return {"version": "canonical_ast_v1",
            "declarations": declarations, "assertions": assertions}


def to_named_buckets(ast: dict) -> dict:
    """Flat lists of names by category — for grounding-check style consumers."""
    out: dict[str, list[str]] = {
        "sorts": [], "entities": [], "functions": [], "relations": [],
        "vals": [], "events": [], "vars": [], "properties": [],
        "deontic": [], "temporal": [], "actions": [], "theorems": [],
        "paths": [], "validations": [], "probabilistic": [], "games": [],
        "graphs": [],
    }
    for d in ast["declarations"]:
        f, k, n = d["family"], d["kind"], d["name"]
        if f == "TypeDecl":
            out["sorts"].append(n)
        elif f == "SymbolDecl":
            if k == "entity":
                out["entities"].append(n)
            elif k == "fun":
                out["functions"].append(n)
            elif k == "rel":
                out["relations"].append(n)
            elif k == "const":
                out["vals"].append(n)
            elif k == "event":
                out["events"].append(n)
            elif k == "var":
                out["vars"].append(n)
            elif k == "property":
                out["properties"].append(n)
            elif k == "body_less":
                out["functions"].append(n)
        elif f == "DeonticDecl":
            out["deontic"].append(n)
        elif f == "TemporalDecl":
            out["temporal"].append(n)
        elif f == "ActionDecl":
            out["actions"].append(n)
        elif f == "TheoremDecl":
            out["theorems"].append(n)
        elif f == "PathDecl":
            out["paths"].append(n)
        elif f == "ValidationDecl":
            out["validations"].append(n)
        elif f == "ProbabilisticDecl":
            out["probabilistic"].append(n)
        elif f == "GameDecl":
            out["games"].append(n)
        elif f == "GraphDecl":
            out["graphs"].append(n)
    return out


def main():
    if len(sys.argv) <= 1:
        print("usage: a4v3_parser_v1.py <a4v3_file> [--strict]")
        sys.exit(2)
    strict = "--strict" in sys.argv
    p = pathlib.Path(sys.argv[1])
    text = p.read_text(encoding="utf-8")
    ast = parse(text, strict=strict)
    print(f"declarations: {len(ast['declarations'])}")
    print(f"assertions:   {len(ast['assertions'])}")
    print(f"warnings:     {len(ast['warnings'])}")
    if ast["warnings"]:
        for w in ast["warnings"][:5]:
            print(f"  line {w['line_no']}: {w['message'][:80]}")
    by_family: dict[str, int] = {}
    for d in ast["declarations"]:
        key = f"{d['family']}.{d['kind']}"
        by_family[key] = by_family.get(key, 0) + 1
    print()
    print("By family.kind:")
    for k, v in sorted(by_family.items(), key=lambda x: -x[1]):
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
