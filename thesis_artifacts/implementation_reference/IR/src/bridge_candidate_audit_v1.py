"""Bridge candidate audit for DZ.

This is intentionally heuristic. It does not decide bridge truth; it finds
places worth human review before merge:

- repeated local IR declarations across entries;
- same relation/function names with different signatures;
- repeated bridge-relevant source phrases;
- CamelCase identifiers used in assertion bodies without local declaration.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

THIS_DIR = Path(__file__).resolve().parent
if str(THIS_DIR) not in sys.path:
    sys.path.insert(0, str(THIS_DIR))

from a4v3_parser_v1 import parse  # noqa: E402


CAMEL_RE = re.compile(r"\b[A-Z][A-Za-z0-9_]*\b")
CALL_RE = re.compile(r"\b([A-Za-z_][A-Za-z0-9_]*)\s*\(")
WORD_RE = re.compile(r"[A-Za-z][a-z0-9]*|[A-Z]+(?=[A-Z][a-z]|\b)")

BUILTIN_IDENTIFIERS = {
    "Nat",
    "Real",
    "Bool",
    "String",
    "Day",
    "Document",
    "DocumentPart",
    "Url",
    "Organization",
    "FinancialInstrument",
    "Currency",
    "MonetaryAmount",
    "Percentage",
    "Period",
    "Event",
    "VagueTerm",
    "Date",
    "Time",
    "WeekdayOf",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
}

SOURCE_PHRASES = [
    "Average Daily Value Traded",
    "Benchmark Regulation",
    "Business Day",
    "Calculation Day",
    "Closing Price",
    "Close of Business",
    "Daily Value Traded",
    "Data Vendor",
    "Eligible Rebalance Day",
    "Exchange",
    "Fixing Day",
    "Free Float",
    "Free Float Market Capitalization",
    "GBS Index Universe",
    "Index Administrator",
    "Index Component",
    "Index Component Requirements",
    "Index Currency",
    "Index Universe",
    "Index Universe Requirements",
    "Live Date",
    "Oversight Committee",
    "Rebalance Day",
    "Regular Rebalance Day",
    "Selection Day",
    "Share Class",
    "Solactive",
    "Start Date",
    "Trading Day",
    "Trading Price",
    "WM / Refinitiv Rate",
    "WM Fixing",
]


def _entry_paths(dz_root: Path) -> list[Path]:
    out: list[Path] = []
    for sub in ("sections", "definitions", "appendix"):
        base = dz_root / sub
        if not base.exists():
            continue
        for p in sorted(base.glob("*/main_ir.a4v3")):
            if any(part.startswith("agent_run") for part in p.parts):
                continue
            out.append(p)
    return out


def _entry_id(path: Path, dz_root: Path) -> str:
    rel = path.parent.relative_to(dz_root).as_posix()
    return rel


def _entry_label(entry_id: str) -> str:
    name = entry_id.rsplit("/", 1)[-1]
    if entry_id.startswith("definitions/"):
        return name
    if entry_id.startswith("sections/section_"):
        suffix = name.removeprefix("section_")
        return "Section" + "_".join(part for part in suffix.split("_"))
    if entry_id.startswith("appendix/appendix_"):
        suffix = name.removeprefix("appendix_")
        return "Appendix" + "_".join(part for part in suffix.split("_"))
    return name


def _decl_signature(decl: dict[str, Any]) -> str:
    family = decl.get("family")
    kind = decl.get("kind")
    if family == "TypeDecl":
        if kind == "subtype":
            return f"extends {decl.get('parent')}"
        if kind == "enum":
            return "enum " + "|".join(decl.get("enum_members", []))
        return "opaque"
    if family == "SymbolDecl":
        if kind == "entity":
            return f": {decl.get('sort')}"
        if kind == "rel":
            return "(" + ", ".join(decl.get("args", [])) + ")"
        if kind == "fun":
            return "(" + ", ".join(decl.get("args", [])) + ") -> " + decl.get("result_sort", "")
    return kind or ""


def _symbol_kind(decl: dict[str, Any]) -> str | None:
    family = decl.get("family")
    kind = decl.get("kind")
    if family == "TypeDecl":
        return "sort"
    if family == "SymbolDecl" and kind in {"entity", "rel", "fun"}:
        return kind
    return None


def _identifier_tokens(name: str) -> set[str]:
    tokens = [t.lower() for t in WORD_RE.findall(name.replace("_", " "))]
    stop = {"the", "of", "for", "and", "in", "to", "as", "by", "on", "with"}
    return {t for t in tokens if t and t not in stop}


def _assertion_blocks(text: str) -> list[str]:
    lines = text.splitlines()
    blocks: list[str] = []
    current: list[str] = []
    in_assertion = False
    top_re = re.compile(r"^\s*(sort|entity|fun|rel|fact|constraint|obligation|permission|prohibition)\b")
    for line in lines:
        if top_re.match(line):
            if current and in_assertion:
                blocks.append("\n".join(current))
            in_assertion = bool(re.match(r"^\s*(fact|constraint)\b", line))
            current = [line] if in_assertion else []
        elif in_assertion:
            current.append(line)
    if current and in_assertion:
        blocks.append("\n".join(current))
    return blocks


def analyze(dz_root: Path) -> dict[str, Any]:
    bridge_text = (dz_root / "bridge" / "main_bridge.a4v3").read_text(encoding="utf-8")
    entries: dict[str, dict[str, Any]] = {}
    decl_groups: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    symbol_by_entry: dict[str, set[str]] = {}
    parse_warnings: list[dict[str, Any]] = []

    for path in _entry_paths(dz_root):
        entry_id = _entry_id(path, dz_root)
        label = _entry_label(entry_id)
        text = path.read_text(encoding="utf-8")
        ast = parse(text, strict=False)
        if ast.get("warnings"):
            parse_warnings.append({"entry": entry_id, "warnings": ast["warnings"]})
        local_symbols: set[str] = set()
        decls: list[dict[str, Any]] = []
        for decl in ast["declarations"]:
            kind = _symbol_kind(decl)
            name = decl.get("name")
            if not kind or not name:
                continue
            signature = _decl_signature(decl)
            item = {
                "entry": entry_id,
                "entry_label": label,
                "kind": kind,
                "name": name,
                "signature": signature,
                "bridge_symbol_guess": f"{label}_{name}",
            }
            decl_groups[(kind, name)].append(item)
            decls.append(item)
            local_symbols.add(name)
            if decl.get("family") == "TypeDecl" and decl.get("kind") == "enum":
                local_symbols.update(decl.get("enum_members", []))
        symbol_by_entry[entry_id] = local_symbols
        entries[entry_id] = {"path": str(path), "label": label, "text": text, "decls": decls}

    repeated_exact: list[dict[str, Any]] = []
    same_name_different_signature: list[dict[str, Any]] = []
    unbridged_repeated_exact: list[dict[str, Any]] = []

    for (kind, name), items in sorted(decl_groups.items()):
        entry_ids = sorted({i["entry"] for i in items})
        if len(entry_ids) < 2:
            continue
        signatures = sorted({i["signature"] for i in items})
        guesses = [i["bridge_symbol_guess"] for i in items]
        bridge_hits = [g for g in guesses if g in bridge_text]
        record = {
            "kind": kind,
            "name": name,
            "entries": entry_ids,
            "signatures": signatures,
            "bridge_symbol_guesses": guesses,
            "bridge_hits": bridge_hits,
            "covered_by_bridge": bool(bridge_hits or name in bridge_text),
        }
        repeated_exact.append(record)
        if len(signatures) > 1:
            same_name_different_signature.append(record)
        if not record["covered_by_bridge"] and kind in {"sort", "entity", "rel", "fun"}:
            unbridged_repeated_exact.append(record)

    lexical_candidates: list[dict[str, Any]] = []
    decl_items = [item for group in decl_groups.values() for item in group]
    for i, a in enumerate(decl_items):
        at = _identifier_tokens(a["name"])
        if len(at) < 2:
            continue
        for b in decl_items[i + 1 :]:
            if a["entry"] == b["entry"] or a["kind"] != b["kind"] or a["name"] == b["name"]:
                continue
            bt = _identifier_tokens(b["name"])
            if len(bt) < 2:
                continue
            inter = at & bt
            union = at | bt
            score = len(inter) / len(union)
            if score >= 0.75:
                guess_a = a["bridge_symbol_guess"]
                guess_b = b["bridge_symbol_guess"]
                covered = guess_a in bridge_text or guess_b in bridge_text
                lexical_candidates.append({
                    "kind": a["kind"],
                    "left": {"entry": a["entry"], "name": a["name"], "signature": a["signature"]},
                    "right": {"entry": b["entry"], "name": b["name"], "signature": b["signature"]},
                    "token_overlap": round(score, 3),
                    "shared_tokens": sorted(inter),
                    "covered_by_bridge_symbol_guess": covered,
                })

    source_phrase_candidates: list[dict[str, Any]] = []
    for phrase in SOURCE_PHRASES:
        hits = []
        phrase_re = re.compile(re.escape(phrase), re.IGNORECASE)
        for entry_id, entry in entries.items():
            source = Path(entry["path"]).with_name("source.md")
            if source.exists():
                text = source.read_text(encoding="utf-8")
                count = len(phrase_re.findall(text))
                if count:
                    hits.append({"entry": entry_id, "count": count})
        if len(hits) >= 2:
            bridge_covered = "".join(phrase.split()).lower() in bridge_text.replace("_", "").lower() or phrase.replace(" ", "") in bridge_text
            source_phrase_candidates.append({
                "phrase": phrase,
                "hits": hits,
                "bridge_text_mentions_phrase_like": bridge_covered,
            })

    assertion_external_identifiers: list[dict[str, Any]] = []
    for entry_id, entry in entries.items():
        local = symbol_by_entry[entry_id]
        for block in _assertion_blocks(entry["text"]):
            header = block.splitlines()[0].strip()
            identifiers = sorted(set(CAMEL_RE.findall(block)))
            suspicious = [
                ident for ident in identifiers
                if ident not in local
                and ident not in BUILTIN_IDENTIFIERS
                and not ident.startswith("Section")
            ]
            if suspicious:
                assertion_external_identifiers.append({
                    "entry": entry_id,
                    "assertion": header,
                    "identifiers": suspicious,
                })

    return {
        "schema": "bridge_candidate_audit_v1",
        "dz_root": str(dz_root),
        "entry_count": len(entries),
        "parse_warning_count": len(parse_warnings),
        "parse_warnings": parse_warnings,
        "repeated_exact_count": len(repeated_exact),
        "same_name_different_signature_count": len(same_name_different_signature),
        "unbridged_repeated_exact_count": len(unbridged_repeated_exact),
        "lexical_candidate_count": len(lexical_candidates),
        "source_phrase_candidate_count": len(source_phrase_candidates),
        "assertion_external_identifier_count": len(assertion_external_identifiers),
        "repeated_exact": repeated_exact,
        "same_name_different_signature": same_name_different_signature,
        "unbridged_repeated_exact": unbridged_repeated_exact,
        "lexical_candidates": lexical_candidates[:200],
        "source_phrase_candidates": source_phrase_candidates,
        "assertion_external_identifiers": assertion_external_identifiers[:200],
    }


def _write_reports(result: dict[str, Any], bridge_dir: Path) -> None:
    (bridge_dir / "bridge_candidate_audit_v1.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    lines = [
        "# Bridge Candidate Audit v1",
        "",
        f"- entries scanned: `{result['entry_count']}`",
        f"- parse warnings: `{result['parse_warning_count']}`",
        f"- repeated exact declarations: `{result['repeated_exact_count']}`",
        f"- same-name different-signature declarations: `{result['same_name_different_signature_count']}`",
        f"- unbridged repeated exact declarations: `{result['unbridged_repeated_exact_count']}`",
        f"- lexical candidates: `{result['lexical_candidate_count']}`",
        f"- repeated source phrase candidates: `{result['source_phrase_candidate_count']}`",
        f"- assertion external identifier blocks: `{result['assertion_external_identifier_count']}`",
        "",
    ]
    if result["same_name_different_signature"]:
        lines.append("## Same Name, Different Signature")
        for item in result["same_name_different_signature"][:40]:
            lines.append(
                f"- `{item['kind']} {item['name']}` in {', '.join(item['entries'])}; "
                f"signatures: {item['signatures']}; bridge hits: {item['bridge_hits'] or 'none'}"
            )
        lines.append("")
    if result["unbridged_repeated_exact"]:
        lines.append("## Unbridged Repeated Exact Declarations")
        for item in result["unbridged_repeated_exact"][:80]:
            lines.append(
                f"- `{item['kind']} {item['name']}` in {', '.join(item['entries'])}; "
                f"signatures: {item['signatures']}"
            )
        lines.append("")
    if result["source_phrase_candidates"]:
        lines.append("## Repeated Source Phrases")
        for item in result["source_phrase_candidates"]:
            hit_s = ", ".join(f"{h['entry']}({h['count']})" for h in item["hits"])
            lines.append(f"- `{item['phrase']}`: {hit_s}")
        lines.append("")
    if result["assertion_external_identifiers"]:
        lines.append("## Assertion Identifiers Without Local Declaration")
        for item in result["assertion_external_identifiers"][:60]:
            lines.append(
                f"- `{item['entry']}` `{item['assertion']}`: {', '.join(item['identifiers'])}"
            )
        lines.append("")
    (bridge_dir / "bridge_candidate_audit_v1.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("dz_root", help="IR/outputs/runs/dz")
    args = parser.parse_args()
    dz_root = Path(args.dz_root)
    result = analyze(dz_root)
    _write_reports(result, dz_root / "bridge")
    print(json.dumps({
        "schema": result["schema"],
        "entry_count": result["entry_count"],
        "parse_warning_count": result["parse_warning_count"],
        "repeated_exact_count": result["repeated_exact_count"],
        "same_name_different_signature_count": result["same_name_different_signature_count"],
        "unbridged_repeated_exact_count": result["unbridged_repeated_exact_count"],
        "lexical_candidate_count": result["lexical_candidate_count"],
        "source_phrase_candidate_count": result["source_phrase_candidate_count"],
        "assertion_external_identifier_count": result["assertion_external_identifier_count"],
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
