"""Merge-readiness audit for the seed methodology corpus.

This check sits between bridge construction and actual merged-IR generation.
It is deliberately conservative: it cannot prove that the canonical ontology is
complete, but it can catch the gaps that make post-merge contradiction checks
misleading.

Main questions:
- Are repeated declarations bridged?
- Are rule-bearing local symbols connected to bridge/canonical families?
- Are there still same-name/different-signature drifts needing a decision?
- Does the index-family/variant propagation layer exist?
- Are local facts likely to remain isolated from canonical reasoning?
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

THIS_DIR = Path(__file__).resolve().parent
if str(THIS_DIR) not in sys.path:
    sys.path.insert(0, str(THIS_DIR))

from a4v3_parser_v1 import parse  # noqa: E402


ENTITY_RE = re.compile(
    r"^\s*entity\s+(?P<name>[A-Za-z_][A-Za-z0-9_]*)\s*:\s*"
    r"(?P<kind>BridgeEntry|BridgeIndex|BridgeSort|BridgeEntity|BridgeRelation|BridgeFamily)\b"
)
CALL_RE = re.compile(r"\b([A-Za-z_][A-Za-z0-9_]*)\s*\(")
CAMEL_RE = re.compile(r"\b[A-Z][A-Za-z0-9_]*\b")
WORD_RE = re.compile(r"[A-Za-z][a-z0-9]*|[A-Z]+(?=[A-Z][a-z]|\b)")

BUILTINS = {
    "Nat",
    "Real",
    "Bool",
    "String",
    "Day",
    "Document",
    "DocumentPart",
    "Url",
    "WebResource",
    "Organization",
    "FinancialInstrument",
    "InvestmentFund",
    "FinancialContract",
    "Currency",
    "MonetaryAmount",
    "Percentage",
    "Percent",
    "Period",
    "Event",
    "VagueTerm",
    "Date",
    "Time",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
}

CORE_TOKEN_SETS = {
    "index": {"index"},
    "index_component": {"index", "component"},
    "security": {"security"},
    "exchange": {"exchange"},
    "trading_day": {"trading", "day"},
    "selection_day": {"selection", "day"},
    "rebalance_day": {"rebalance", "day"},
    "calculation_day": {"calculation", "day"},
    "trading_price": {"trading", "price"},
    "closing_price": {"closing", "price"},
    "index_level": {"index", "level"},
    "index_universe": {"index", "universe"},
    "methodology": {"methodology"},
    "corporate_action": {"corporate", "action"},
    "solactive": {"solactive"},
    "website": {"website"},
    "rbics": {"rbics"},
}

LOW_SIGNAL_NAMES = {
    "TheIndex",
    "Solactive",
    "SolactiveWebsite",
    "ThisGuideline",
    "AnnouncementSection",
}

EXACT_CORE_NAMES = {
    "Index",
    "TheIndex",
    "Security",
    "IndexComponent",
    "ShareClass",
    "Exchange",
    "TradingDay",
    "SelectionDay",
    "RebalanceDay",
    "RegularRebalanceDay",
    "EligibleRebalanceDay",
    "CalculationDay",
    "TradingPrice",
    "ClosingPrice",
    "IndexLevel",
    "IndexUniverse",
    "GbsIndexUniverse",
    "IndexAdministrator",
    "Solactive",
    "SolactiveWebsite",
    "ThisGuideline",
    "EquityIndexMethodology",
    "SolactiveEquityIndexMethodology",
    "CorporateAction",
    "IndexCalculation",
}

TYPE_GAP_SORTS = {
    "Index",
    "Security",
    "IndexComponent",
    "ShareClass",
    "Exchange",
    "TradingDay",
    "SelectionDay",
    "RebalanceDay",
    "RegularRebalanceDay",
    "EligibleRebalanceDay",
    "CalculationDay",
    "TradingPrice",
    "ClosingPrice",
    "IndexLevel",
    "IndexUniverse",
    "GbsIndexUniverse",
    "IndexAdministrator",
    "SolactiveOrganization",
    "EquityIndexMethodology",
    "CorporateAction",
    "IndexCalculation",
}


def _split_args(raw: str) -> list[str]:
    return [arg.strip() for arg in raw.split(",") if arg.strip()]


def _entry_paths(run_root: Path) -> list[Path]:
    out: list[Path] = []
    for sub in ("sections", "definitions", "appendix"):
        base = run_root / sub
        if not base.exists():
            continue
        for p in sorted(base.glob("*/main_ir.a4v3")):
            if any(part.startswith("agent_run") for part in p.parts):
                continue
            out.append(p)
    return out


def _entry_id(path: Path, run_root: Path) -> str:
    return path.parent.relative_to(run_root).as_posix()


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


def _core_match(name: str) -> str | None:
    tokens = _identifier_tokens(name)
    if not tokens:
        return None
    for core_name, required in CORE_TOKEN_SETS.items():
        if required <= tokens:
            return core_name
    return None


def _used_identifiers_from_decl(decl: dict[str, Any]) -> set[str]:
    if decl.get("family") not in {"AssertDecl", "DeonticDecl"}:
        return set()
    raw = decl.get("raw") or ""
    out = set(CALL_RE.findall(raw))
    out.update(CAMEL_RE.findall(raw))
    out.discard(decl.get("name") or "")
    keywords = {
        "and",
        "or",
        "not",
        "implies",
        "forall",
        "exists",
        "fact",
        "constraint",
        "obligation",
        "permission",
        "prohibition",
        "action",
        "target",
        "scope",
        "agent",
    }
    return {x for x in out if x not in keywords}


def _parse_bridge(bridge_path: Path) -> dict[str, Any]:
    text = bridge_path.read_text(encoding="utf-8")
    symbols: dict[str, str] = {}
    families: set[str] = set()
    symbol_locations: dict[str, str] = {}
    family_members: dict[str, set[str]] = defaultdict(set)
    symbol_families: dict[str, set[str]] = defaultdict(set)
    family_link_types: dict[str, str] = {}
    family_confidences: dict[str, str] = {}

    for line in text.splitlines():
        clean = line.split("--", 1)[0]
        m = ENTITY_RE.match(clean)
        if m:
            name = m.group("name")
            kind = m.group("kind")
            if kind == "BridgeFamily":
                families.add(name)
            elif kind != "BridgeEntry":
                symbols[name] = kind
        for call in re.finditer(r"\b([A-Za-z_][A-Za-z0-9_]*)\s*\(([^()]*)\)", clean):
            rel = call.group(1)
            args = _split_args(call.group(2))
            if rel == "bridge_declared_in" and len(args) >= 2:
                symbol_locations[args[0]] = args[1]
            elif rel == "bridge_family_member" and len(args) >= 2:
                family_members[args[0]].add(args[1])
                symbol_families[args[1]].add(args[0])
            elif rel == "bridge_family_link_type" and len(args) >= 2:
                family_link_types[args[0]] = args[1]
            elif rel == "bridge_family_confidence" and len(args) >= 2:
                family_confidences[args[0]] = args[1]

    return {
        "text": text,
        "symbols": symbols,
        "families": families,
        "symbol_locations": symbol_locations,
        "family_members": {k: sorted(v) for k, v in family_members.items()},
        "symbol_families": {k: sorted(v) for k, v in symbol_families.items()},
        "family_link_types": family_link_types,
        "family_confidences": family_confidences,
    }


def _finding(
    code: str,
    severity: str,
    message: str,
    *,
    entry: str | None = None,
    data: dict[str, Any] | None = None,
) -> dict[str, Any]:
    out: dict[str, Any] = {
        "code": code,
        "severity": severity,
        "message": message,
    }
    if entry:
        out["entry"] = entry
    if data:
        out["data"] = data
    return out


def analyze(run_root: Path) -> dict[str, Any]:
    bridge_path = run_root / "bridge" / "main_bridge.a4v3"
    merge_dir = run_root / "merge"
    canonical_path = merge_dir / "canonical_ontology_v1.a4v3"
    decisions_path = merge_dir / "canonical_bridge_decisions_v1.yaml"
    bridge = _parse_bridge(bridge_path)

    candidate_path = run_root / "bridge" / "bridge_candidate_audit_v1.json"
    candidate_audit: dict[str, Any] = {}
    if candidate_path.exists():
        candidate_audit = json.loads(candidate_path.read_text(encoding="utf-8"))

    entries: dict[str, dict[str, Any]] = {}
    decls: list[dict[str, Any]] = []
    decl_name_counts: Counter[tuple[str, str]] = Counter()
    parse_warnings: list[dict[str, Any]] = []

    for path in _entry_paths(run_root):
        entry_id = _entry_id(path, run_root)
        label = _entry_label(entry_id)
        text = path.read_text(encoding="utf-8")
        ast = parse(text, strict=False)
        if ast.get("warnings"):
            parse_warnings.append({"entry": entry_id, "warnings": ast["warnings"]})
        used: set[str] = set()
        local_decls: list[dict[str, Any]] = []
        for decl in ast.get("declarations", []):
            used.update(_used_identifiers_from_decl(decl))
        for decl in ast.get("declarations", []):
            kind = _symbol_kind(decl)
            name = decl.get("name")
            if not kind or not name:
                continue
            signature = _decl_signature(decl)
            bridge_symbol = f"{label}_{name}"
            item = {
                "entry": entry_id,
                "entry_label": label,
                "kind": kind,
                "name": name,
                "signature": signature,
                "sort": decl.get("sort"),
                "parent": decl.get("parent"),
                "args": decl.get("args") or [],
                "result_sort": decl.get("result_sort"),
                "bridge_symbol": bridge_symbol,
                "bridge_families": bridge["symbol_families"].get(bridge_symbol, []),
                "used_in_assertion_or_deontic": name in used,
                "core_match": _core_match(name),
            }
            decls.append(item)
            local_decls.append(item)
            decl_name_counts[(kind, name)] += 1
        entries[entry_id] = {"path": str(path), "label": label, "used": sorted(used), "decls": local_decls}

    findings: list[dict[str, Any]] = []

    if parse_warnings:
        findings.append(
            _finding(
                "entry_parse_warnings",
                "hard",
                "Some canonical seed methodology entries have parser warnings.",
                data={"parse_warning_count": len(parse_warnings), "parse_warnings": parse_warnings[:20]},
            )
        )

    if not canonical_path.exists():
        findings.append(
            _finding(
                "canonical_ontology_missing",
                "hard",
                "canonical_ontology_v1.a4v3 is missing.",
                data={"path": str(canonical_path)},
            )
        )
    if not decisions_path.exists():
        findings.append(
            _finding(
                "canonical_bridge_decisions_missing",
                "hard",
                "canonical_bridge_decisions_v1.yaml is missing.",
                data={"path": str(decisions_path)},
            )
        )

    unbridged_repeated = candidate_audit.get("unbridged_repeated_exact_count", 0)
    external_identifiers = candidate_audit.get("assertion_external_identifier_count", 0)
    if unbridged_repeated:
        findings.append(
            _finding(
                "unbridged_repeated_exact_declarations",
                "hard",
                "Repeated exact declarations remain outside the bridge.",
                data={"count": unbridged_repeated},
            )
        )
    if external_identifiers:
        findings.append(
            _finding(
                "assertion_external_identifiers",
                "hard",
                "Assertion bodies contain undeclared CamelCase identifiers.",
                data={"count": external_identifiers},
            )
        )

    for item in decls:
        repeated = decl_name_counts[(item["kind"], item["name"])] > 1
        bridgeable = bool(item["bridge_families"] or item["bridge_symbol"] in bridge["symbols"])
        if repeated and not bridgeable:
            findings.append(
                _finding(
                    "repeated_rule_symbol_without_bridge",
                    "soft",
                    f"{item['kind']} {item['name']} repeats across entries but has no bridge/family coverage.",
                    entry=item["entry"],
                    data=item,
                )
            )
        if (
            item["used_in_assertion_or_deontic"]
            and item["core_match"]
            and (item["name"] in EXACT_CORE_NAMES or decl_name_counts[(item["kind"], item["name"])] > 1)
            and not bridgeable
            and item["name"] not in BUILTINS
        ):
            severity = "soft" if item["name"] in LOW_SIGNAL_NAMES else "advisory"
            findings.append(
                _finding(
                    "rule_relevant_core_symbol_without_family",
                    severity,
                    f"Rule-bearing core-like symbol {item['name']} is not in a bridge family.",
                    entry=item["entry"],
                    data=item,
                )
            )

    for item in decls:
        if item["kind"] != "entity" or not item["used_in_assertion_or_deontic"]:
            continue
        sort_name = item.get("sort")
        if not sort_name or sort_name in BUILTINS:
            continue
        if sort_name not in TYPE_GAP_SORTS:
            continue
        if item["name"].startswith("Https") or item["name"].endswith("Name"):
            continue
        sort_bridge_symbol = f"{item['entry_label']}_{sort_name}"
        entity_bridgeable = bool(item["bridge_families"] or item["bridge_symbol"] in bridge["symbols"])
        sort_bridgeable = bool(bridge["symbol_families"].get(sort_bridge_symbol) or sort_bridge_symbol in bridge["symbols"])
        if not entity_bridgeable and not sort_bridgeable:
            findings.append(
                _finding(
                    "possible_type_gap_local_entity",
                    "advisory",
                    f"Entity {item['name']} is used in rules, but neither it nor its sort {sort_name} has bridge/family coverage.",
                    entry=item["entry"],
                    data={**item, "sort_bridge_symbol": sort_bridge_symbol},
                )
            )

    same_diff_records = candidate_audit.get("same_name_different_signature", [])
    same_diff_uncovered = [r for r in same_diff_records if not r.get("covered_by_bridge")]
    if same_diff_uncovered:
        findings.append(
            _finding(
                "same_name_different_signature_review",
                "soft",
                "Same-name declarations with different signatures exist without bridge coverage.",
                data={
                    "count": len(same_diff_uncovered),
                    "total_same_name_different_signature_count": len(same_diff_records),
                    "examples": same_diff_uncovered[:20],
                },
            )
        )

    lexical_records = candidate_audit.get("lexical_candidates", [])
    source_phrase_records = candidate_audit.get("source_phrase_candidates", [])
    lexical_uncovered = [r for r in lexical_records if not r.get("covered_by_bridge_symbol_guess")]
    source_phrase_uncovered = [r for r in source_phrase_records if not r.get("bridge_text_mentions_phrase_like")]
    if lexical_uncovered or source_phrase_uncovered:
        findings.append(
            _finding(
                "semantic_candidate_review_remaining",
                "advisory",
                "Uncovered lexical/source-phrase candidates remain; these are review candidates, not automatic merge instructions.",
                data={
                    "lexical_uncovered_count": len(lexical_uncovered),
                    "source_phrase_uncovered_count": len(source_phrase_uncovered),
                    "total_lexical_candidate_count": len(lexical_records),
                    "total_source_phrase_candidate_count": len(source_phrase_records),
                    "lexical_examples": lexical_uncovered[:20],
                    "source_phrase_examples": source_phrase_uncovered[:20],
                },
            )
        )

    bridge_text = bridge["text"]
    canonical_text = canonical_path.read_text(encoding="utf-8") if canonical_path.exists() else ""
    variant_required = [
        "TheIndexLocalPlaceholderFamily",
        "SolactiveTransatlanticCleanEnergyEURIndexPR",
        "SolactiveTransatlanticCleanEnergyEURIndexNTR",
        "SolactiveTransatlanticCleanEnergyEURIndexTR",
        "SolactiveTransatlanticCleanEnergyEURIndex5PercentAR",
        "SolactiveTransatlanticCleanEnergyEURIndex50AR",
        "generic_index_rule_applies_to_variant",
    ]
    missing_variant_items = [x for x in variant_required if x not in bridge_text and x not in canonical_text]
    if missing_variant_items:
        findings.append(
            _finding(
                "generic_index_variant_propagation_incomplete",
                "soft",
                "Generic index placeholder propagation to published variants is incomplete.",
                data={"missing": missing_variant_items},
            )
        )

    severity_counts = Counter(f["severity"] for f in findings)
    hard = severity_counts.get("hard", 0)
    status = "blocked" if hard else "passed_with_review_items"
    if not findings:
        status = "passed"

    rule_bearing_decl_count = sum(1 for d in decls if d["used_in_assertion_or_deontic"])
    bridged_rule_bearing_count = sum(
        1
        for d in decls
        if d["used_in_assertion_or_deontic"] and (d["bridge_families"] or d["bridge_symbol"] in bridge["symbols"])
    )

    return {
        "schema": "merge_readiness_audit_v1",
        "run_root": str(run_root),
        "entry_count": len(entries),
        "declaration_count": len(decls),
        "rule_bearing_declaration_count": rule_bearing_decl_count,
        "bridged_rule_bearing_declaration_count": bridged_rule_bearing_count,
        "bridge_family_count": len(bridge["families"]),
        "bridge_symbol_count": len(bridge["symbols"]),
        "candidate_audit_snapshot": {
            "parse_warning_count": candidate_audit.get("parse_warning_count"),
            "unbridged_repeated_exact_count": candidate_audit.get("unbridged_repeated_exact_count"),
            "same_name_different_signature_count": candidate_audit.get("same_name_different_signature_count"),
            "same_name_different_signature_uncovered_count": len(same_diff_uncovered),
            "lexical_candidate_count": candidate_audit.get("lexical_candidate_count"),
            "lexical_uncovered_by_bridge_symbol_guess_count": len(lexical_uncovered),
            "source_phrase_candidate_count": candidate_audit.get("source_phrase_candidate_count"),
            "source_phrase_uncovered_count": len(source_phrase_uncovered),
            "assertion_external_identifier_count": candidate_audit.get("assertion_external_identifier_count"),
        },
        "findings": findings,
        "hard_findings": severity_counts.get("hard", 0),
        "soft_findings": severity_counts.get("soft", 0),
        "advisory_findings": severity_counts.get("advisory", 0),
        "status": status,
    }


def _write_markdown(report: dict[str, Any], out_path: Path) -> None:
    lines: list[str] = []
    lines.append("# Merge Readiness Audit v1")
    lines.append("")
    lines.append(f"Status: `{report['status']}`")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    for key in [
        "entry_count",
        "declaration_count",
        "rule_bearing_declaration_count",
        "bridged_rule_bearing_declaration_count",
        "bridge_family_count",
        "bridge_symbol_count",
        "hard_findings",
        "soft_findings",
        "advisory_findings",
    ]:
        lines.append(f"- `{key}`: {report.get(key)}")
    lines.append("")
    lines.append("## Candidate Audit Snapshot")
    lines.append("")
    for key, value in report.get("candidate_audit_snapshot", {}).items():
        lines.append(f"- `{key}`: {value}")
    lines.append("")
    lines.append("## Findings")
    lines.append("")
    findings = report.get("findings", [])
    if not findings:
        lines.append("No findings.")
    else:
        for idx, finding in enumerate(findings, start=1):
            entry = f" entry `{finding['entry']}`" if finding.get("entry") else ""
            lines.append(
                f"{idx}. `{finding['severity']}` `{finding['code']}`{entry}: {finding['message']}"
            )
            data = finding.get("data") or {}
            compact_keys = ["name", "kind", "signature", "bridge_symbol", "bridge_families", "count"]
            compact = {k: data[k] for k in compact_keys if k in data}
            if compact:
                lines.append(f"   Data: `{json.dumps(compact, ensure_ascii=False)}`")
    lines.append("")
    lines.append("## Interpretation")
    lines.append("")
    lines.append(
        "Hard findings block merge. Soft findings require an explicit merge decision. "
        "Advisory findings are review prompts, especially for type-gap risks where a "
        "post-merge contradiction may fail only because a membership edge is missing."
    )
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-root", default="case_studies/financial_methodology")
    ap.add_argument("--out-dir", default=None)
    args = ap.parse_args()

    run_root = Path(args.run_root)
    out_dir = Path(args.out_dir) if args.out_dir else run_root / "merge"
    out_dir.mkdir(parents=True, exist_ok=True)
    report = analyze(run_root)
    json_path = out_dir / "merge_readiness_audit_v1.json"
    md_path = out_dir / "merge_readiness_audit_v1.md"
    json_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    _write_markdown(report, md_path)
    print(json.dumps({k: report[k] for k in ["status", "hard_findings", "soft_findings", "advisory_findings"]}, indent=2))


if __name__ == "__main__":
    main()
