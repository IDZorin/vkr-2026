"""token_provenance_v1.py

Build token-level provenance for a local A4V3 IR entry.

This complements the older lexical gap metrics. Instead of only saying
"source token is missing from the IR surface", it records where each source
token is accounted for:

- declaration layer: sort/entity/rel/fun/deontic declaration names/signatures
- formula layer: assertion names, callees, refs, binders, literals
- family signal layer: e.g. `cannot` covered by `DeonticDecl.prohibition`
- ignored glue: stopwords / Markdown list scaffolding

It also writes a per-entry waiver scaffold for the remaining uncovered content
tokens. Existing waiver comments are preserved when the scaffold is regenerated.

Outputs:
  <entry>/metrics_token_provenance_v1.json
  <entry>/metrics_token_provenance_v1.md
  <entry>/waiver_token_absorption_v1.json

CLI:
  python token_provenance_v1.py [entry_dir|run_root]
"""
from __future__ import annotations

import json
import pathlib
import re
import sys
from collections import defaultdict
from typing import Any
import yaml

SRC_DIR = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(SRC_DIR))

import a4v3_parser_v1 as parser  # noqa: E402
import extended_grounding_check_v1 as ext  # noqa: E402


_STOPWORDS = {
    "a", "an", "the", "of", "in", "on", "at", "for", "to", "from", "by",
    "and", "or", "but", "if", "with", "as", "is", "are", "was", "were",
    "be", "been", "being", "have", "has", "had", "this", "that", "these",
    "those", "it", "its", "they", "their", "them", "into", "which", "who",
    "whom", "whose", "there", "here", "also", "well", "as", "any", "each",
}

_GLUE_COMMENTS = {
    "accordance": (
        "Procedural glue: the local rule set is represented by explicit "
        "constraints rather than by a separate `accordance` carrier."
    ),
    "following": (
        "Discourse/list marker: the following listed rules are represented "
        "by the constraints themselves."
    ),
    "rules": (
        "Document-structure word: rule content is represented by top-level "
        "constraints, not by a separate `Rule` ontology object."
    ),
    "rule": (
        "Document-structure word: rule content is represented by top-level "
        "constraints, not by a separate `Rule` ontology object."
    ),
    "framework": (
        "Context qualifier: absorbed into the grounded local symbols that "
        "carry the framework-scoped assignment/universe semantics."
    ),
    "total": (
        "Modifier absorbed by count/comparison structure; no separate domain "
        "entity is needed unless the text defines a total as an object."
    ),
    "under": (
        "Scope preposition: absorbed into the guarded assignment/classification "
        "formulas rather than represented as a separate relation."
    ),
    "case": (
        "Discourse marker for an exception/branch; the branch condition is "
        "represented directly by the relevant implication/count formula."
    ),
    "contains": (
        "Verbal surface form absorbed by the membership/count formula; the IR "
        "uses `index_component` and `count(...) < 40` rather than a separate "
        "`contains` predicate."
    ),
    "classified": (
        "Process wording absorbed by classification constraints that assign "
        "a region from country-assignment conditions."
    ),
    "one": (
        "Cardinality wording from `one of the two`; absorbed by the region "
        "classification alternatives rather than modeled as a numeric literal."
    ),
    "two": (
        "Cardinality wording from `two regions`; represented by the two region "
        "entities used by the classification constraints."
    ),
}

_A4V3_TOP_LEVEL = (
    "sort ", "entity ", "rel ", "fun", "constraint ", "fact ", "axiom ",
    "prop ", "prohibition ", "obligation ", "permission ",
)

_URL_RE = re.compile(r"https?://[^\s\]\)<>'\"`]+")
_TRAILING_URL_PUNCT = ".,;:"


def _strip_markdown_scaffold(line: str) -> str:
    line = re.sub(r"^\s{0,3}#{1,6}\s*", "", line)
    line = re.sub(r"^\s*(?:[-*+]|\d+(?:\.\d+)*)[.)]?\s+", "", line)
    # Workspace source files often start with generated headers such as
    # "# Section 5.4 Source". They are file scaffolding, not methodology text.
    if re.fullmatch(r"(Section|Appendix)\s+\d+(?:\.\d+)*\s+Source", line.strip(), flags=re.IGNORECASE):
        return ""
    return line


def _source_tokens(source: str) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    seen: dict[str, dict[str, Any]] = {}
    for line_no, line in enumerate(str(source or "").splitlines(), start=1):
        clean = _strip_markdown_scaffold(line)
        token_re = r"\d{1,3}(?:,\d{3})+(?:\.\d+)?%?|[A-Za-z][A-Za-z0-9]*(?:-[A-Za-z0-9]+)*|\d+(?:\.\d+)?%?"
        for match in re.finditer(token_re, clean):
            surface = match.group(0)
            keys = _token_keys(surface)
            if not keys:
                continue
            canonical = sorted(keys)[0]
            item = seen.setdefault(
                canonical,
                {
                    "token": canonical,
                    "surface_forms": [],
                    "count": 0,
                    "source_locations": [],
                    "keys": sorted(keys),
                    "is_stopword": _is_stopword(surface),
                },
            )
            if surface not in item["surface_forms"]:
                item["surface_forms"].append(surface)
            item["count"] += 1
            item["source_locations"].append({"line": line_no, "column": match.start() + 1})
            item["keys"] = sorted(set(item["keys"]) | keys)
            item["is_stopword"] = bool(item["is_stopword"] or _is_stopword(surface))
    out.extend(seen.values())
    return sorted(out, key=lambda x: (x["source_locations"][0]["line"], x["source_locations"][0]["column"]))


def _clean_url(raw: str) -> str:
    return str(raw or "").strip().rstrip(_TRAILING_URL_PUNCT)


def _source_urls(inputs: list[tuple[str, str]]) -> list[dict[str, Any]]:
    """Extract exact URL artifacts from source-like text.

    URLs are not ordinary lexical tokens: stemming/case normalization can hide
    a lost link. Treat them as exact provenance artifacts.
    """
    seen: dict[str, dict[str, Any]] = {}
    for source_name, text in inputs:
        for line_no, line in enumerate(str(text or "").splitlines(), start=1):
            for match in _URL_RE.finditer(line):
                url = _clean_url(match.group(0))
                if not url:
                    continue
                item = seen.setdefault(
                    url,
                    {
                        "url": url,
                        "count": 0,
                        "source_locations": [],
                    },
                )
                item["count"] += 1
                item["source_locations"].append(
                    {
                        "source": source_name,
                        "line": line_no,
                        "column": match.start() + 1,
                    }
                )
    return sorted(
        seen.values(),
        key=lambda x: (
            x["source_locations"][0]["source"],
            x["source_locations"][0]["line"],
            x["source_locations"][0]["column"],
        ),
    )


def _url_provenance(source_urls: list[dict[str, Any]], ir_text: str) -> dict[str, Any]:
    records = []
    missing = []
    for item in source_urls:
        url = str(item.get("url") or "")
        covered = bool(url and url in ir_text)
        record = {
            "url": url,
            "count": item.get("count", 0),
            "status": "covered_exact" if covered else "missing_exact_url",
            "source_locations": item.get("source_locations", []),
            "provenance": [
                {
                    "source": "ir_surface",
                    "role": "exact_url_literal_or_comment",
                    "matched_text": url,
                }
            ] if covered else [],
        }
        records.append(record)
        if not covered:
            missing.append(record)
    return {
        "summary": {
            "source_url_count": len(records),
            "covered_url_count": len(records) - len(missing),
            "missing_url_count": len(missing),
            "url_coverage_rate": round((len(records) - len(missing)) / len(records), 3) if records else None,
        },
        "urls": records,
        "missing_urls": missing,
    }


def _is_stopword(token: str) -> bool:
    low = token.lower()
    return low in _STOPWORDS or (len(low) < 3 and not low.isdigit())


def _token_keys(value: Any) -> set[str]:
    text = str(value or "").strip()
    if not text:
        return set()
    keys: set[str] = set()
    if re.fullmatch(r"\d{1,3}(?:,\d{3})+(?:\.\d+)?%?", text):
        keys.add(text.replace(",", "").lower())
        return keys
    if re.fullmatch(r"\d+(?:\.\d+)?%?", text):
        keys.add(text.lower())
        if re.fullmatch(r"\d+\.\d+", text):
            keys.add("section" + text.replace(".", "_"))
        return keys
    for part in re.findall(r"[A-Za-z][A-Za-z0-9_]*|\d+(?:\.\d+)?%?", text):
        if re.fullmatch(r"\d+(?:\.\d+)?%?", part):
            keys.add(part.lower())
            continue
        keys.update(ext._normalize_name(part))
        for sub in re.split(r"[-_]", part):
            if sub:
                keys.update(ext._normalize_name(sub))
        for match in re.finditer(r"Section(\d+)_(\d+)", part, flags=re.IGNORECASE):
            keys.add(f"{match.group(1)}.{match.group(2)}")
            keys.add(f"section{match.group(1)}_{match.group(2)}")
    for key in list(keys):
        if key.endswith("y") and len(key) > 3:
            keys.add(key[:-1] + "i")
        if key.endswith("i") and len(key) > 3:
            keys.add(key[:-1] + "y")
        if key.endswith("s") and len(key) > 3 and not key.endswith(("is", "ss", "us")):
            keys.add(key[:-1])
        if key.endswith("es") and len(key) > 4:
            keys.add(key[:-2])
        if key.startswith("classif"):
            keys.add("classifi")
    irregular = {
        "indices": {"index"},
        "indic": {"index"},
        "usually": {"usual"},
        "usualli": {"usual"},
        # Porter-style stemming turns "capped" into "capp", while IR often
        # carries the source meaning as `cap_at` or a `<=` bound.
        "capp": {"cap"},
    }
    for key in list(keys):
        keys.update(irregular.get(key, set()))
    return {k for k in keys if k}


def _compact_evidence(record: dict[str, Any]) -> dict[str, Any]:
    return {k: v for k, v in record.items() if v not in (None, "", [], {})}


def _add_evidence(index: dict[str, list[dict[str, Any]]], text: Any, evidence: dict[str, Any]) -> None:
    for key in _token_keys(text):
        index[key].append(_compact_evidence(evidence | {"matched_text": str(text)}))


def _walk_expr(expr: Any, assertion_name: str, assertion_kind: str, index: dict[str, list[dict[str, Any]]], path: str = "expr") -> None:
    if isinstance(expr, dict):
        kind = str(expr.get("kind", "") or "")
        if kind == "call":
            _add_evidence(index, expr.get("callee"), {
                "source": "formula",
                "role": "callee",
                "assertion": assertion_name,
                "assertion_kind": assertion_kind,
                "expr_path": path,
            })
        elif kind == "ref":
            _add_evidence(index, expr.get("name"), {
                "source": "formula",
                "role": "ref",
                "assertion": assertion_name,
                "assertion_kind": assertion_kind,
                "expr_path": path,
            })
        elif kind == "count":
            binder = expr.get("binder")
            if isinstance(binder, dict):
                _add_evidence(index, binder.get("name"), {
                    "source": "formula",
                    "role": "count_binder",
                    "assertion": assertion_name,
                    "assertion_kind": assertion_kind,
                    "expr_path": path,
                })
                _add_evidence(index, binder.get("sort"), {
                    "source": "formula",
                    "role": "count_binder_sort",
                    "assertion": assertion_name,
                    "assertion_kind": assertion_kind,
                    "expr_path": path,
                })

        for key, value in expr.items():
            if key in {"kind", "callee", "name"}:
                continue
            _walk_expr(value, assertion_name, assertion_kind, index, f"{path}.{key}")
    elif isinstance(expr, list):
        for i, item in enumerate(expr):
            _walk_expr(item, assertion_name, assertion_kind, index, f"{path}[{i}]")
    elif isinstance(expr, (str, int, float)):
        _add_evidence(index, expr, {
            "source": "formula",
            "role": "literal",
            "assertion": assertion_name,
            "assertion_kind": assertion_kind,
            "expr_path": path,
        })


def _index_ir(ir_text: str, ast: dict[str, Any]) -> dict[str, list[dict[str, Any]]]:
    index: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for decl in ast.get("declarations", []):
        if not isinstance(decl, dict):
            continue
        family = f"{decl.get('family', '')}.{decl.get('kind', '')}"
        name = str(decl.get("name", "") or "")
        if name:
            _add_evidence(index, name, {
                "source": "declaration",
                "role": "declaration_name",
                "symbol": name,
                "family": family,
                "line": decl.get("line_no"),
            })
        for field in ("args", "result_sort", "agent_sort", "target_sort", "action", "scope", "parent", "sort"):
            value = decl.get(field)
            values = value if isinstance(value, list) else [value]
            for item in values:
                if item:
                    _add_evidence(index, item, {
                        "source": "declaration",
                        "role": field,
                        "symbol": name,
                        "family": family,
                        "line": decl.get("line_no"),
                    })
        for field in ("variants", "members", "enum_members"):
            value = decl.get(field)
            values = value if isinstance(value, list) else [value]
            for item in values:
                if item:
                    _add_evidence(index, item, {
                        "source": "declaration",
                        "role": field[:-1] if field.endswith("s") else field,
                        "symbol": name,
                        "family": family,
                        "line": decl.get("line_no"),
                    })
        for param in decl.get("params", []) or []:
            if not isinstance(param, dict):
                continue
            for field in ("name", "type"):
                _add_evidence(index, param.get(field), {
                    "source": "declaration",
                    "role": f"param_{field}",
                    "symbol": name,
                    "family": family,
                    "line": decl.get("line_no"),
                })

    for assertion in ast.get("assertions", []):
        if not isinstance(assertion, dict):
            continue
        assertion_name = str(assertion.get("name", "") or "assertion")
        assertion_kind = str(assertion.get("assert_kind", "") or assertion.get("kind", "") or "assertion")
        _add_evidence(index, assertion_name, {
            "source": "formula",
            "role": "assertion_name",
            "assertion": assertion_name,
            "assertion_kind": assertion_kind,
            "line": assertion.get("line_no"),
        })
        metadata = assertion.get("metadata") if isinstance(assertion.get("metadata"), dict) else {}
        realizes = assertion.get("realizes") or metadata.get("realizes")
        if realizes:
            _add_evidence(index, realizes, {
                "source": "formula_metadata",
                "role": "realizes",
                "assertion": assertion_name,
                "assertion_kind": assertion_kind,
                "line": assertion.get("line_no"),
            })
        _walk_expr(assertion.get("expr"), assertion_name, assertion_kind, index)

    # Surface fallback for deontic/action blocks that are currently parsed as
    # declarations, not assertions. Keep this generic: it reads A4V3 fields, not
    # methodology prose.
    for block in _surface_deontic_blocks(ir_text):
        name = block.get("name", "")
        family = block.get("family", "")
        for role in ("name", "action", "target", "scope", "agent"):
            value = block.get(role)
            if value:
                _add_evidence(index, value, {
                    "source": "deontic_surface",
                    "role": role,
                    "symbol": name,
                    "family": family,
                    "line": block.get("line"),
                })
    return dict(index)


def _iter_provenance_source_phrases(note: Any) -> list[str]:
    if not isinstance(note, dict):
        return []
    out: list[str] = []
    one = note.get("source_phrase")
    if isinstance(one, str) and one.strip():
        out.append(one.strip())
    many = note.get("source_phrases")
    if isinstance(many, list):
        for item in many:
            if isinstance(item, str) and item.strip():
                out.append(item.strip())
    return out


def _index_provenance_vocabulary_notes(
    entry_dir: pathlib.Path,
    ir_text: str,
    index: dict[str, list[dict[str, Any]]],
) -> None:
    """Add coverage evidence from provenance vocabulary source phrases.

    This is intentionally narrow: a vocabulary note covers source tokens only
    when the documented identifier actually appears in the current IR surface.
    Provenance lint separately checks that back-translations do not leak these
    identifiers as CamelCase English.
    """
    prov_path = entry_dir / "provenance.yaml"
    if not prov_path.exists():
        return
    try:
        data = yaml.safe_load(prov_path.read_text(encoding="utf-8")) or {}
    except Exception:
        return
    notes = data.get("vocabulary_notes") if isinstance(data, dict) else {}
    if not isinstance(notes, dict):
        return
    for identifier, note in notes.items():
        identifier_s = str(identifier or "").strip()
        if not identifier_s or identifier_s not in ir_text:
            continue
        for phrase in _iter_provenance_source_phrases(note):
            for source_token in _source_tokens(phrase):
                for key in source_token.get("keys", []):
                    index.setdefault(key, []).append(
                        {
                            "source": "provenance_vocabulary_notes",
                            "role": "source_phrase",
                            "symbol": identifier_s,
                            "matched_text": phrase,
                        }
                    )


def _surface_deontic_blocks(ir_text: str) -> list[dict[str, Any]]:
    lines = str(ir_text or "").splitlines()
    blocks: list[dict[str, Any]] = []
    idx = 0
    while idx < len(lines):
        stripped = lines[idx].strip()
        if not stripped.startswith(("prohibition ", "obligation ", "permission ")):
            idx += 1
            continue
        start = idx
        block_lines = [lines[idx]]
        idx += 1
        while idx < len(lines):
            candidate = lines[idx]
            candidate_stripped = candidate.strip()
            if candidate_stripped and not candidate[:1].isspace():
                if any(candidate_stripped.startswith(prefix) for prefix in _A4V3_TOP_LEVEL):
                    break
            block_lines.append(candidate)
            idx += 1
        text = "\n".join(block_lines)
        head = re.match(r"\s*(prohibition|obligation|permission)\s+([A-Za-z_][A-Za-z0-9_]*)", block_lines[0])
        kind = head.group(1) if head else "deontic"
        name = head.group(2) if head else ""
        record = {
            "family": f"DeonticDecl.{kind}",
            "name": name,
            "line": start + 1,
        }
        for key in ("action", "target", "scope", "agent"):
            match = re.search(rf"(?m)^\s*{re.escape(key)}\s*:\s*(.+?)\s*$", text)
            if match:
                record[key] = match.group(1).strip()
        blocks.append(record)
    return blocks


def _family_signal_evidence(source_token: dict[str, Any], ast: dict[str, Any]) -> list[dict[str, Any]]:
    surfaces = {str(s).lower() for s in source_token.get("surface_forms", [])}
    families = {f"{d.get('family', '')}.{d.get('kind', '')}" for d in ast.get("declarations", []) if isinstance(d, dict)}
    assertions = ast.get("assertions", []) if isinstance(ast.get("assertions"), list) else []
    assertion_kinds = {
        str(a.get("assert_kind", "") or a.get("kind", "")).lower()
        for a in assertions
        if isinstance(a, dict)
    }
    expr_text = json.dumps([a.get("expr") for a in assertions if isinstance(a, dict)], ensure_ascii=False).lower()
    out: list[dict[str, Any]] = []
    if surfaces & {"cannot", "can't", "mustn", "mustn't"} and "DeonticDecl.prohibition" in families:
        out.append({"source": "family_signal", "role": "modal_prohibition", "family": "DeonticDecl.prohibition"})
    if surfaces & {"must", "shall", "required", "need", "needs"} and "DeonticDecl.obligation" in families:
        out.append({"source": "family_signal", "role": "modal_obligation", "family": "DeonticDecl.obligation"})
    if surfaces & {"must", "shall", "required", "need", "needs"} and "constraint" in assertion_kinds:
        out.append({"source": "family_signal", "role": "hard_constraint_obligation", "assertion_kind": "constraint"})
    if surfaces & {"will"} and ("DeonticDecl.obligation" in families or "constraint" in assertion_kinds):
        out.append({"source": "family_signal", "role": "legal_future_or_procedural_future"})
    if surfaces & {"may", "permitted", "allowed"} and "DeonticDecl.permission" in families:
        out.append({"source": "family_signal", "role": "modal_permission", "family": "DeonticDecl.permission"})
    if surfaces & {"retain", "retains", "right"} and "DeonticDecl.permission" in families:
        out.append({"source": "family_signal", "role": "retained_right_permission", "family": "DeonticDecl.permission"})
    if surfaces & {"made", "make", "making"} and "DeonticDecl.obligation" in families:
        out.append({"source": "family_signal", "role": "passive_make_obligation", "family": "DeonticDecl.obligation"})
    if surfaces & {"not", "no", "non"} and '"op": "not"' in expr_text:
        out.append({"source": "family_signal", "role": "explicit_negation", "marker": "not"})
    if surfaces & {"each", "every", "any", "all"} and "forall" in expr_text:
        out.append({"source": "family_signal", "role": "universal_quantifier", "marker": "forall"})
    if surfaces & {"single", "individual"} and "forall" in expr_text:
        out.append({"source": "family_signal", "role": "per_item_universal_scope", "marker": "forall"})
    if surfaces & {"least"} and "gte" in expr_text:
        out.append({"source": "family_signal", "role": "at_least_comparison", "marker": ">="})
    return out


def _waiver_comment(token: str, surface_forms: list[str]) -> tuple[str, str]:
    candidates = {token.lower()}
    for form in surface_forms:
        candidates.add(str(form).lower())
        candidates.update(_token_keys(form))
    for candidate in candidates:
        if candidate in _GLUE_COMMENTS:
            return "absorbed_discourse_or_modifier", _GLUE_COMMENTS[candidate]
    return (
        "needs_human_review",
        "No direct token-level IR provenance was found. Add a human explanation if this word is intentionally absorbed rather than formalized.",
    )


def analyze_entry(entry_dir: pathlib.Path) -> dict[str, Any]:
    source_path = entry_dir / "source.md"
    normalized_path = entry_dir / "normalized.md"
    ir_path = entry_dir / "main_ir.a4v3"
    source_text = source_path.read_text(encoding="utf-8") if source_path.exists() else ""
    normalized_text = normalized_path.read_text(encoding="utf-8") if normalized_path.exists() else source_text
    ir_text = ir_path.read_text(encoding="utf-8") if ir_path.exists() else ""
    url_inputs = [("source.md", source_text)]
    if normalized_text and normalized_text != source_text:
        url_inputs.append(("normalized.md", normalized_text))
    url_status = _url_provenance(_source_urls(url_inputs), ir_text)

    try:
        ast = parser.parse(ir_text)
        parse_error = None
    except Exception as exc:  # pragma: no cover - defensive for broken workspaces
        ast = {"declarations": [], "assertions": [], "warnings": []}
        parse_error = str(exc)

    ir_index = _index_ir(ir_text, ast)
    _index_provenance_vocabulary_notes(entry_dir, ir_text, ir_index)
    records = []
    uncovered = []
    for src_token in _source_tokens(normalized_text or source_text):
        evidence = []
        for key in src_token.get("keys", []):
            evidence.extend(ir_index.get(key, []))
        evidence.extend(_family_signal_evidence(src_token, ast))

        # Deduplicate evidence while preserving useful detail.
        seen = set()
        unique_evidence = []
        for item in evidence:
            sig = json.dumps(item, ensure_ascii=False, sort_keys=True)
            if sig not in seen:
                seen.add(sig)
                unique_evidence.append(item)

        if src_token.get("is_stopword"):
            status = "ignored_stopword"
        elif unique_evidence:
            status = "covered"
        else:
            status = "uncovered_needs_waiver"

        record = {
            "token": src_token["token"],
            "surface_forms": src_token["surface_forms"],
            "count": src_token["count"],
            "status": status,
            "source_locations": src_token["source_locations"],
            "provenance": unique_evidence,
        }
        records.append(record)
        if status == "uncovered_needs_waiver":
            uncovered.append(record)

    content_records = [r for r in records if r["status"] != "ignored_stopword"]
    covered_content = [r for r in content_records if r["status"] == "covered"]
    result = {
        "entry_id": entry_dir.name,
        "schema": "metrics_token_provenance_v1",
        "parse_error": parse_error,
        "summary": {
            "source_token_count": len(records),
            "content_token_count": len(content_records),
            "covered_content_token_count": len(covered_content),
            "uncovered_content_token_count": len(uncovered),
            "ignored_stopword_count": len(records) - len(content_records),
            "content_coverage_rate": round(len(covered_content) / len(content_records), 3) if content_records else None,
        },
        "tokens": records,
        "uncovered_tokens": uncovered,
        "url_provenance": url_status,
    }
    return result


def _load_existing_waiver(path: pathlib.Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _waiver_payload(entry_dir: pathlib.Path, result: dict[str, Any]) -> dict[str, Any]:
    existing = _load_existing_waiver(entry_dir / "waiver_token_absorption_v1.json")
    existing_by_token = {
        str(item.get("token", "")): item
        for item in existing.get("items", [])
        if isinstance(item, dict)
    }
    items = []
    for record in result.get("uncovered_tokens", []):
        token = str(record.get("token", ""))
        category, generated_comment = _waiver_comment(token, list(record.get("surface_forms", []) or []))
        old = existing_by_token.get(token, {})
        preserve_old_comment = bool(old.get("reviewer")) or (
            old.get("comment")
            and old.get("suggested_category") != "needs_human_review"
        )
        items.append({
            "token": token,
            "surface_forms": record.get("surface_forms", []),
            "source_locations": record.get("source_locations", []),
            "status": "waiver_needed",
            "suggested_category": old.get("suggested_category") if preserve_old_comment else category,
            "comment": old.get("comment") if preserve_old_comment else generated_comment,
            "reviewer": old.get("reviewer") or "",
        })
    return {
        "entry_id": entry_dir.name,
        "schema": "waiver_token_absorption_v1",
        "generated_from": "metrics_token_provenance_v1.json",
        "items": items,
        "stale_tokens_from_previous_file": sorted(set(existing_by_token) - {item["token"] for item in items}),
    }


def _write_md(entry_dir: pathlib.Path, result: dict[str, Any]) -> pathlib.Path:
    lines = [
        f"# Token Provenance: {result['entry_id']}",
        "",
        "## Summary",
        "",
    ]
    for key, value in result.get("summary", {}).items():
        lines.append(f"- {key}: `{value}`")
    lines.extend(["", "## Uncovered Content Tokens", ""])
    uncovered = result.get("uncovered_tokens", [])
    if not uncovered:
        lines.append("- none")
    else:
        for item in uncovered:
            forms = ", ".join(item.get("surface_forms", []))
            lines.append(f"- `{item['token']}` ({forms})")
    url_summary = (result.get("url_provenance") or {}).get("summary") or {}
    lines.extend(["", "## Exact URL Provenance", ""])
    lines.append(
        f"- covered URLs: `{url_summary.get('covered_url_count')}/"
        f"{url_summary.get('source_url_count')}` "
        f"(`{url_summary.get('url_coverage_rate')}`)"
    )
    missing_urls = (result.get("url_provenance") or {}).get("missing_urls") or []
    if missing_urls:
        for item in missing_urls:
            lines.append(f"- missing exact URL: `{item.get('url')}`")
    else:
        lines.append("- missing exact URLs: none")
    lines.extend(["", "## Covered Content Tokens", ""])
    for item in result.get("tokens", []):
        if item.get("status") != "covered":
            continue
        prov = item.get("provenance", [])
        first = prov[0] if prov else {}
        where = first.get("assertion") or first.get("symbol") or first.get("role") or first.get("source")
        lines.append(f"- `{item['token']}` -> `{where}`")
    out = entry_dir / "metrics_token_provenance_v1.md"
    out.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return out


def _save(entry_dir: pathlib.Path, result: dict[str, Any]) -> pathlib.Path:
    out = entry_dir / "metrics_token_provenance_v1.json"
    out.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    _write_md(entry_dir, result)
    waiver = _waiver_payload(entry_dir, result)
    (entry_dir / "waiver_token_absorption_v1.json").write_text(
        json.dumps(waiver, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return out


def main() -> None:
    target = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path.cwd()
    if (target / "main_ir.a4v3").exists() or (target / "source.md").exists():
        result = analyze_entry(target)
        out = _save(target, result)
        summary = result.get("summary", {})
        print(f"Wrote {out}")
        print(
            "  content coverage: "
            f"{summary.get('covered_content_token_count')}/"
            f"{summary.get('content_token_count')} "
            f"({summary.get('content_coverage_rate')})"
        )
        print(f"  uncovered: {summary.get('uncovered_content_token_count')}")
        return

    n = 0
    uncovered_total = 0
    for ir_path in sorted(target.rglob("main_ir.a4v3")):
        entry_dir = ir_path.parent
        if entry_dir.name.startswith("_"):
            continue
        if not ir_path.read_text(encoding="utf-8").strip():
            continue
        result = analyze_entry(entry_dir)
        _save(entry_dir, result)
        n += 1
        uncovered_total += int(result.get("summary", {}).get("uncovered_content_token_count", 0) or 0)
    print(f"Processed {n} entries; uncovered content tokens: {uncovered_total}.")


if __name__ == "__main__":
    main()
