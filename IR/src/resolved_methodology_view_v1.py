"""Build a resolved methodology view for the seed methodology corpus.

This script deliberately does *not* rewrite local `main_ir.a4v3` files into a
new merged IR. Local IR remains the source-faithful gold layer. The resolved
view is an inspection artifact that says:

- which local declarations resolve through bridge families or pair groups;
- which declarations remain local-only;
- which assertion/deontic blocks depend on which resolved concepts;
- which canonical ontology declarations are available to the merge step.

The intended consumer is the merge/reasoning stage, not the translator.
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
    r"(?P<kind>BridgeEntry|BridgeIndex|BridgeSort|BridgeEntity|BridgeRelation|BridgeFamily|BridgeFrame|BridgeRole)\b"
)
CALL_RE = re.compile(r"\b([A-Za-z_][A-Za-z0-9_]*)\s*\(([^()]*)\)")
IDENT_CALL_RE = re.compile(r"\b([A-Za-z_][A-Za-z0-9_]*)\s*\(")
CAMEL_RE = re.compile(r"\b[A-Z][A-Za-z0-9_]*\b")

SAME_RELS = {"same_index", "same_sort", "same_entity", "same_relation"}
ASSERTION_FAMILIES = {"AssertDecl", "DeonticDecl"}
BUILTIN_OR_KEYWORD_NAMES = {
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


def _strip_comment(line: str) -> str:
    return line.split("--", 1)[0]


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
        if kind == "record":
            fields = decl.get("fields") or []
            return "record " + ", ".join(f"{f.get('name')}:{f.get('type')}" for f in fields)
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


def _used_identifiers_from_decl(decl: dict[str, Any]) -> set[str]:
    if decl.get("family") not in ASSERTION_FAMILIES:
        return set()
    raw = decl.get("raw") or ""
    out = set(IDENT_CALL_RE.findall(raw))
    out.update(CAMEL_RE.findall(raw))
    out.discard(decl.get("name") or "")
    return {x for x in out if x not in BUILTIN_OR_KEYWORD_NAMES}


class UnionFind:
    def __init__(self) -> None:
        self.parent: dict[str, str] = {}

    def find(self, x: str) -> str:
        if x not in self.parent:
            self.parent[x] = x
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a: str, b: str) -> None:
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return
        keep, drop = sorted([ra, rb])
        self.parent[drop] = keep

    def groups(self) -> dict[str, list[str]]:
        grouped: dict[str, list[str]] = defaultdict(list)
        for x in list(self.parent):
            grouped[self.find(x)].append(x)
        return {root: sorted(items) for root, items in sorted(grouped.items()) if len(items) > 1}


def _parse_bridge(bridge_path: Path) -> dict[str, Any]:
    text = bridge_path.read_text(encoding="utf-8")
    entries: set[str] = set()
    families: set[str] = set()
    frames: set[str] = set()
    roles: set[str] = set()
    symbols: dict[str, str] = {}
    symbol_locations: dict[str, str] = {}
    family_members: dict[str, set[str]] = defaultdict(set)
    symbol_families: dict[str, set[str]] = defaultdict(set)
    family_anchors: dict[str, str] = {}
    family_link_types: dict[str, str] = {}
    family_confidences: dict[str, str] = {}
    same_pairs: list[dict[str, Any]] = []
    pair_link_types: dict[tuple[str, str], str] = {}
    pair_confidences: dict[tuple[str, str], str] = {}
    projections: dict[str, dict[str, Any]] = defaultdict(lambda: {"argument_roles": {}})
    uf = UnionFind()

    for line_no, line in enumerate(text.splitlines(), start=1):
        clean = _strip_comment(line)
        m = ENTITY_RE.match(clean)
        if m:
            name = m.group("name")
            kind = m.group("kind")
            if kind == "BridgeEntry":
                entries.add(name)
            elif kind == "BridgeFamily":
                families.add(name)
            elif kind == "BridgeFrame":
                frames.add(name)
            elif kind == "BridgeRole":
                roles.add(name)
            else:
                symbols[name] = kind
        for call in CALL_RE.finditer(clean):
            name = call.group(1)
            args = _split_args(call.group(2))
            if name == "bridge_declared_in" and len(args) >= 2:
                symbol_locations[args[0]] = args[1]
            elif name == "bridge_family_member" and len(args) >= 2:
                family_members[args[0]].add(args[1])
                symbol_families[args[1]].add(args[0])
            elif name == "bridge_family_anchor" and len(args) >= 2:
                family_anchors[args[0]] = args[1]
            elif name == "bridge_family_link_type" and len(args) >= 2:
                family_link_types[args[0]] = args[1]
            elif name == "bridge_family_confidence" and len(args) >= 2:
                family_confidences[args[0]] = args[1]
            elif name in SAME_RELS and len(args) >= 2:
                a, b = args[0], args[1]
                uf.union(a, b)
                same_pairs.append({"relation": name, "left": a, "right": b, "line": line_no})
            elif name == "bridge_link_type" and len(args) >= 3:
                pair_link_types[(args[0], args[1])] = args[2]
            elif name == "bridge_confidence" and len(args) >= 3:
                pair_confidences[(args[0], args[1])] = args[2]
            elif name == "bridge_relation_projects_to_frame" and len(args) >= 2:
                projections[args[0]]["frame"] = args[1]
            elif name == "bridge_projection_kind" and len(args) >= 2:
                projections[args[0]]["projection_kind"] = args[1]
            elif name == "bridge_argument_role" and len(args) >= 3:
                projections[args[0]]["argument_roles"][args[1]] = args[2]
            elif name == "bridge_return_role" and len(args) >= 2:
                projections[args[0]]["return_role"] = args[1]
            elif name == "bridge_projection_confidence" and len(args) >= 2:
                projections[args[0]]["projection_confidence"] = args[1]

    pair_groups = uf.groups()
    symbol_pair_group: dict[str, str] = {}
    for root, members in pair_groups.items():
        for member in members:
            symbol_pair_group[member] = root

    return {
        "entries": sorted(entries),
        "symbols": symbols,
        "frames": sorted(frames),
        "roles": sorted(roles),
        "symbol_locations": symbol_locations,
        "families": sorted(families),
        "family_members": {k: sorted(v) for k, v in family_members.items()},
        "symbol_families": {k: sorted(v) for k, v in symbol_families.items()},
        "family_anchors": family_anchors,
        "family_link_types": family_link_types,
        "family_confidences": family_confidences,
        "same_pairs": same_pairs,
        "pair_link_types": {"|".join(k): v for k, v in pair_link_types.items()},
        "pair_confidences": {"|".join(k): v for k, v in pair_confidences.items()},
        "pair_groups": pair_groups,
        "symbol_pair_group": symbol_pair_group,
        "projections": {k: v for k, v in sorted(projections.items())},
    }


def _resolve_bridge_symbol(bridge_symbol: str, bridge: dict[str, Any]) -> dict[str, Any]:
    families = bridge["symbol_families"].get(bridge_symbol, [])
    if families:
        return {
            "resolution_kind": "bridge_family",
            "resolved_concepts": [f"BridgeFamily:{f}" for f in families],
            "bridge_families": families,
            "family_link_types": {f: bridge["family_link_types"].get(f) for f in families},
            "family_confidences": {f: bridge["family_confidences"].get(f) for f in families},
        }
    pair_root = bridge["symbol_pair_group"].get(bridge_symbol)
    if pair_root:
        return {
            "resolution_kind": "bridge_pair_group",
            "resolved_concepts": [f"BridgePairGroup:{pair_root}"],
            "bridge_pair_group": pair_root,
            "bridge_pair_group_members": bridge["pair_groups"].get(pair_root, []),
        }
    if bridge_symbol in bridge["symbols"]:
        return {
            "resolution_kind": "declared_bridge_symbol",
            "resolved_concepts": [f"BridgeSymbol:{bridge_symbol}"],
        }
    return {
        "resolution_kind": "local_only",
        "resolved_concepts": [f"Local:{bridge_symbol}"],
    }


def _parse_canonical(canonical_path: Path) -> dict[str, Any]:
    text = canonical_path.read_text(encoding="utf-8")
    ast = parse(text, strict=False)
    declarations: list[dict[str, Any]] = []
    subtype_edges: list[dict[str, str]] = []
    for decl in ast.get("declarations", []):
        kind = _symbol_kind(decl)
        name = decl.get("name")
        if not kind or not name:
            continue
        item = {
            "kind": kind,
            "name": name,
            "signature": _decl_signature(decl),
            "line_no": decl.get("line_no"),
        }
        declarations.append(item)
        if decl.get("family") == "TypeDecl" and decl.get("kind") == "subtype":
            subtype_edges.append({"child": name, "parent": decl.get("parent")})
    return {
        "path": str(canonical_path),
        "warnings": ast.get("warnings", []),
        "declarations": declarations,
        "subtype_edges": subtype_edges,
        "counts_by_kind": dict(Counter(d["kind"] for d in declarations)),
    }


def analyze(run_root: Path) -> dict[str, Any]:
    bridge_path = run_root / "bridge" / "main_bridge.a4v3"
    canonical_path = run_root / "merge" / "canonical_ontology_v1.a4v3"
    bridge = _parse_bridge(bridge_path)
    canonical = _parse_canonical(canonical_path)

    entries: dict[str, Any] = {}
    local_declarations: list[dict[str, Any]] = []
    rule_dependencies: list[dict[str, Any]] = []
    parse_warnings: list[dict[str, Any]] = []

    for path in _entry_paths(run_root):
        entry_id = _entry_id(path, run_root)
        entry_label = _entry_label(entry_id)
        text = path.read_text(encoding="utf-8")
        ast = parse(text, strict=False)
        if ast.get("warnings"):
            parse_warnings.append({"entry": entry_id, "warnings": ast["warnings"]})

        local_by_name: dict[str, dict[str, Any]] = {}
        entry_decl_count = 0
        entry_rule_count = 0

        for decl in ast.get("declarations", []):
            kind = _symbol_kind(decl)
            name = decl.get("name")
            if not kind or not name:
                continue
            bridge_symbol = f"{entry_label}_{name}"
            resolved = _resolve_bridge_symbol(bridge_symbol, bridge)
            item = {
                "entry": entry_id,
                "entry_label": entry_label,
                "path": str(path),
                "kind": kind,
                "name": name,
                "signature": _decl_signature(decl),
                "bridge_symbol": bridge_symbol,
                "projection": bridge["projections"].get(bridge_symbol),
                **resolved,
            }
            local_declarations.append(item)
            local_by_name[name] = item
            entry_decl_count += 1

        for decl in ast.get("declarations", []):
            if decl.get("family") not in ASSERTION_FAMILIES:
                continue
            name = decl.get("name")
            if not name:
                continue
            used_identifiers = sorted(x for x in _used_identifiers_from_decl(decl) if x in local_by_name)
            dependencies = []
            for symbol in used_identifiers:
                local = local_by_name[symbol]
                dependencies.append(
                    {
                        "symbol": symbol,
                        "kind": local["kind"],
                        "signature": local["signature"],
                        "bridge_symbol": local["bridge_symbol"],
                        "resolution_kind": local["resolution_kind"],
                        "resolved_concepts": local["resolved_concepts"],
                        "projection": local.get("projection"),
                    }
                )
            rule_dependencies.append(
                {
                    "entry": entry_id,
                    "entry_label": entry_label,
                    "kind": decl.get("kind"),
                    "name": name,
                    "line_no": decl.get("line_no"),
                    "dependency_count": len(dependencies),
                    "dependencies": dependencies,
                }
            )
            entry_rule_count += 1

        entries[entry_id] = {
            "label": entry_label,
            "path": str(path),
            "declaration_count": entry_decl_count,
            "assertion_or_deontic_count": entry_rule_count,
        }

    resolution_counts = Counter(d["resolution_kind"] for d in local_declarations)
    resolved_decl_count = sum(
        count
        for kind, count in resolution_counts.items()
        if kind in {"bridge_family", "bridge_pair_group", "declared_bridge_symbol"}
    )
    family_usage = Counter()
    projection_usage = Counter()
    for decl in local_declarations:
        for family in decl.get("bridge_families", []):
            family_usage[family] += 1
        projection = decl.get("projection") or {}
        if projection.get("frame"):
            projection_usage[projection["frame"]] += 1

    local_only_core_like = [
        d
        for d in local_declarations
        if d["resolution_kind"] == "local_only"
        and d["name"] in {"Index", "TheIndex", "Security", "IndexComponent", "TradingDay", "RebalanceDay", "SelectionDay"}
    ]

    status = "generated"
    if parse_warnings or canonical.get("warnings"):
        status = "generated_with_parse_warnings"

    return {
        "schema": "resolved_methodology_view_v1",
        "status": status,
        "run_root": str(run_root),
        "source_of_truth_note": (
            "This is a derived inspection view. Source of truth remains local IR "
            "+ audit envelope + bridge + canonical ontology."
        ),
        "entry_count": len(entries),
        "local_declaration_count": len(local_declarations),
        "resolved_declaration_count": resolved_decl_count,
        "local_only_declaration_count": resolution_counts.get("local_only", 0),
        "assertion_or_deontic_count": len(rule_dependencies),
        "bridge_family_count": len(bridge["families"]),
        "bridge_symbol_count": len(bridge["symbols"]),
        "bridge_pair_group_count": len(bridge["pair_groups"]),
        "bridge_frame_count": len(bridge["frames"]),
        "bridge_role_count": len(bridge["roles"]),
        "bridge_projection_count": len(bridge["projections"]),
        "canonical_declaration_count": len(canonical["declarations"]),
        "canonical_subtype_edge_count": len(canonical["subtype_edges"]),
        "resolution_counts": dict(resolution_counts),
        "top_bridge_families_by_local_declarations": family_usage.most_common(20),
        "top_projection_frames_by_local_declarations": projection_usage.most_common(20),
        "parse_warnings": parse_warnings,
        "canonical": canonical,
        "bridge_summary": {
            "entries": bridge["entries"],
            "families": bridge["families"],
            "frames": bridge["frames"],
            "roles": bridge["roles"],
            "family_members": bridge["family_members"],
            "family_link_types": bridge["family_link_types"],
            "family_confidences": bridge["family_confidences"],
            "pair_groups": bridge["pair_groups"],
            "projections": bridge["projections"],
        },
        "entries": entries,
        "local_declarations": local_declarations,
        "rule_dependencies": rule_dependencies,
        "review_prompts": {
            "local_only_core_like": local_only_core_like[:50],
            "note": (
                "These are not automatic failures. They are prompts to check whether "
                "a local symbol intentionally stays local or needs a bridge/canonical link."
            ),
        },
    }


def _write_markdown(report: dict[str, Any], out_path: Path) -> None:
    lines: list[str] = []
    lines.append("# Resolved Methodology View v1")
    lines.append("")
    lines.append(f"Status: `{report['status']}`")
    lines.append("")
    lines.append("This is a derived inspection view, not a rewritten merged IR.")
    lines.append("The source of truth remains local `main_ir.a4v3` files plus provenance, bridge, and canonical ontology.")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    for key in [
        "entry_count",
        "local_declaration_count",
        "resolved_declaration_count",
        "local_only_declaration_count",
        "assertion_or_deontic_count",
        "bridge_family_count",
        "bridge_symbol_count",
        "bridge_pair_group_count",
        "bridge_frame_count",
        "bridge_role_count",
        "bridge_projection_count",
        "canonical_declaration_count",
        "canonical_subtype_edge_count",
    ]:
        lines.append(f"- `{key}`: {report.get(key)}")
    lines.append("")
    lines.append("## Resolution Counts")
    lines.append("")
    for kind, count in sorted(report.get("resolution_counts", {}).items()):
        lines.append(f"- `{kind}`: {count}")
    lines.append("")
    lines.append("## Top Bridge Families")
    lines.append("")
    top = report.get("top_bridge_families_by_local_declarations", [])
    if not top:
        lines.append("No bridge family usage detected.")
    else:
        for family, count in top:
            link_type = report["bridge_summary"]["family_link_types"].get(family)
            confidence = report["bridge_summary"]["family_confidences"].get(family)
            lines.append(f"- `{family}`: {count} local declarations; link_type `{link_type}`; confidence `{confidence}`")
    lines.append("")
    lines.append("## Projection Frames")
    lines.append("")
    projections = report.get("top_projection_frames_by_local_declarations", [])
    if not projections:
        lines.append("No bridge projection frames detected.")
    else:
        for frame, count in projections:
            lines.append(f"- `{frame}`: {count} local declarations project to this frame")
    lines.append("")
    lines.append("## Canonical Ontology Snapshot")
    lines.append("")
    for kind, count in sorted(report.get("canonical", {}).get("counts_by_kind", {}).items()):
        lines.append(f"- `{kind}`: {count}")
    lines.append("")
    lines.append("## Rule Dependency View")
    lines.append("")
    lines.append(
        "Each assertion/deontic block keeps its local text, but this report records "
        "which local declarations it touches and how those declarations resolve via bridge/canonical layers."
    )
    lines.append("")
    dependency_counter = Counter()
    for rule in report.get("rule_dependencies", []):
        for dep in rule.get("dependencies", []):
            for concept in dep.get("resolved_concepts", []):
                dependency_counter[concept] += 1
    for concept, count in dependency_counter.most_common(25):
        lines.append(f"- `{concept}`: used by {count} local rule dependencies")
    if not dependency_counter:
        lines.append("No local rule dependencies detected.")
    lines.append("")
    lines.append("## Review Prompts")
    lines.append("")
    prompts = report.get("review_prompts", {}).get("local_only_core_like", [])
    if not prompts:
        lines.append("No local-only core-like symbols in the capped prompt set.")
    else:
        lines.append("Local-only core-like symbols to review before claiming deep contradiction coverage:")
        for item in prompts[:30]:
            lines.append(
                f"- `{item['entry']}` `{item['kind']}` `{item['name']}` "
                f"with signature `{item['signature']}`"
            )
    lines.append("")
    lines.append("## Interpretation")
    lines.append("")
    lines.append(
        "Bridge/canonical resolution makes cross-fragment references inspectable, "
        "but it is still a view. Process/workflow rules and operational lowering "
        "remain separate layers."
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
    json_path = out_dir / "resolved_methodology_view_v1.json"
    md_path = out_dir / "resolved_methodology_view_v1.md"
    json_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    _write_markdown(report, md_path)

    print(
        json.dumps(
            {
                "status": report["status"],
                "entry_count": report["entry_count"],
                "local_declaration_count": report["local_declaration_count"],
                "resolved_declaration_count": report["resolved_declaration_count"],
                "local_only_declaration_count": report["local_only_declaration_count"],
                "bridge_projection_count": report["bridge_projection_count"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
