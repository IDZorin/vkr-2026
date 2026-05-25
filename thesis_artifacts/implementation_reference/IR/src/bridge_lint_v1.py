"""Deterministic lint for financial methodology bridge/main_bridge.a4v3.

The bridge layer is not a source-local IR entry, so the normal entry checks do
not catch bridge-specific mistakes such as a same_relation without argument
order or a declared BridgeSymbol with no bridge_declared_in location.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


ENTITY_RE = re.compile(
    r"^\s*entity\s+(?P<name>[A-Za-z_][A-Za-z0-9_]*)\s*:\s*"
    r"(?P<kind>BridgeEntry|BridgeIndex|BridgeSort|BridgeEntity|BridgeRelation|BridgeFamily|BridgeFrame|BridgeRole)\b"
)
CALL_RE = re.compile(r"\b(?P<name>[A-Za-z_][A-Za-z0-9_]*)\((?P<args>[^()]*)\)")
SAME_RELS = {"same_index", "same_sort", "same_entity", "same_relation"}
BRIDGE_SYMBOL_KINDS = {"BridgeIndex", "BridgeSort", "BridgeEntity", "BridgeRelation"}


def _strip_comment(line: str) -> str:
    return line.split("--", 1)[0]


def _split_args(raw: str) -> list[str]:
    return [arg.strip() for arg in raw.split(",") if arg.strip()]


def _severity(code: str) -> str:
    soft = {
        "bridge_symbol_without_location",
    }
    return "soft" if code in soft else "hard"


def _finding(code: str, message: str, *, line: int | None = None, data: dict[str, Any] | None = None) -> dict[str, Any]:
    out: dict[str, Any] = {
        "code": code,
        "severity": _severity(code),
        "message": message,
    }
    if line is not None:
        out["line"] = line
    if data:
        out["data"] = data
    return out


def analyze_bridge(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    entries: set[str] = set()
    families: set[str] = set()
    frames: set[str] = set()
    roles: set[str] = set()
    symbols: dict[str, str] = {}
    calls: list[tuple[int, str, list[str]]] = []

    for lineno, line in enumerate(text.splitlines(), start=1):
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
            calls.append((lineno, call.group("name"), _split_args(call.group("args"))))

    locations: set[str] = set()
    same_pairs: dict[str, set[tuple[str, str]]] = {name: set() for name in SAME_RELS}
    link_types: dict[tuple[str, str], str] = {}
    confidences: set[tuple[str, str]] = set()
    argument_orders: set[tuple[str, str]] = set()
    family_members: dict[str, set[str]] = {}
    family_anchors: set[str] = set()
    family_link_types: set[str] = set()
    family_confidences: set[str] = set()
    projected_relations: set[str] = set()
    projection_kinds: set[str] = set()
    projection_confidences: set[str] = set()
    projection_argument_roles: dict[str, set[str]] = {}
    projection_return_roles: dict[str, set[str]] = {}
    findings: list[dict[str, Any]] = []

    def require_symbol(arg: str, rel: str, lineno: int) -> None:
        if arg not in symbols:
            findings.append(
                _finding(
                    "undeclared_bridge_symbol_reference",
                    f"{rel} references undeclared bridge symbol {arg}",
                    line=lineno,
                    data={"symbol": arg, "relation": rel},
                )
            )

    def require_relation_symbol(arg: str, rel: str, lineno: int) -> None:
        require_symbol(arg, rel, lineno)
        if arg in symbols and symbols[arg] != "BridgeRelation":
            findings.append(
                _finding(
                    "bridge_argument_order_non_relation",
                    f"{rel} expects BridgeRelation symbols, got {arg}:{symbols[arg]}",
                    line=lineno,
                    data={"symbol": arg, "symbol_kind": symbols[arg], "relation": rel},
                )
            )

    def require_entry(arg: str, rel: str, lineno: int) -> None:
        if arg not in entries:
            findings.append(
                _finding(
                    "undeclared_bridge_entry_reference",
                    f"{rel} references undeclared bridge entry {arg}",
                    line=lineno,
                    data={"entry": arg, "relation": rel},
                )
            )

    def require_family(arg: str, rel: str, lineno: int) -> None:
        if arg not in families:
            findings.append(
                _finding(
                    "undeclared_bridge_family_reference",
                    f"{rel} references undeclared bridge family {arg}",
                    line=lineno,
                    data={"family": arg, "relation": rel},
                )
            )

    def require_frame(arg: str, rel: str, lineno: int) -> None:
        if arg not in frames:
            findings.append(
                _finding(
                    "undeclared_bridge_frame_reference",
                    f"{rel} references undeclared bridge frame {arg}",
                    line=lineno,
                    data={"frame": arg, "relation": rel},
                )
            )

    def require_role(arg: str, rel: str, lineno: int) -> None:
        if arg not in roles:
            findings.append(
                _finding(
                    "undeclared_bridge_role_reference",
                    f"{rel} references undeclared bridge role {arg}",
                    line=lineno,
                    data={"role": arg, "relation": rel},
                )
            )

    for lineno, name, args in calls:
        if name == "bridge_declared_in" and len(args) >= 2:
            require_symbol(args[0], name, lineno)
            require_entry(args[1], name, lineno)
            locations.add(args[0])
        elif name in SAME_RELS and len(args) >= 2:
            require_symbol(args[0], name, lineno)
            require_symbol(args[1], name, lineno)
            same_pairs[name].add((args[0], args[1]))
        elif name == "bridge_link_type" and len(args) >= 3:
            require_symbol(args[0], name, lineno)
            require_symbol(args[1], name, lineno)
            link_types[(args[0], args[1])] = args[2]
        elif name == "bridge_confidence" and len(args) >= 3:
            require_symbol(args[0], name, lineno)
            require_symbol(args[1], name, lineno)
            confidences.add((args[0], args[1]))
        elif name == "bridge_supported_by_entry" and len(args) >= 3:
            require_symbol(args[0], name, lineno)
            require_symbol(args[1], name, lineno)
            require_entry(args[2], name, lineno)
        elif name == "bridge_argument_order" and len(args) >= 2:
            require_relation_symbol(args[0], name, lineno)
            require_relation_symbol(args[1], name, lineno)
            argument_orders.add((args[0], args[1]))
        elif name == "bridge_family_member" and len(args) >= 2:
            require_family(args[0], name, lineno)
            require_symbol(args[1], name, lineno)
            family_members.setdefault(args[0], set()).add(args[1])
        elif name == "bridge_family_anchor" and len(args) >= 2:
            require_family(args[0], name, lineno)
            require_symbol(args[1], name, lineno)
            family_anchors.add(args[0])
        elif name == "bridge_family_link_type" and len(args) >= 2:
            require_family(args[0], name, lineno)
            family_link_types.add(args[0])
        elif name == "bridge_family_confidence" and len(args) >= 2:
            require_family(args[0], name, lineno)
            family_confidences.add(args[0])
        elif name == "bridge_relation_projects_to_frame" and len(args) >= 2:
            require_relation_symbol(args[0], name, lineno)
            require_frame(args[1], name, lineno)
            projected_relations.add(args[0])
        elif name == "bridge_projection_kind" and len(args) >= 2:
            require_relation_symbol(args[0], name, lineno)
            projection_kinds.add(args[0])
        elif name == "bridge_argument_role" and len(args) >= 3:
            require_relation_symbol(args[0], name, lineno)
            if not re.match(r"^\d+$", args[1]):
                findings.append(
                    _finding(
                        "bridge_argument_role_position_not_nat_literal",
                        f"{name} expects a Nat literal position, got {args[1]}",
                        line=lineno,
                        data={"symbol": args[0], "position": args[1]},
                    )
                )
            require_role(args[2], name, lineno)
            projection_argument_roles.setdefault(args[0], set()).add(args[2])
        elif name == "bridge_return_role" and len(args) >= 2:
            require_relation_symbol(args[0], name, lineno)
            require_role(args[1], name, lineno)
            projection_return_roles.setdefault(args[0], set()).add(args[1])
        elif name == "bridge_projection_confidence" and len(args) >= 2:
            require_relation_symbol(args[0], name, lineno)
            projection_confidences.add(args[0])

    for symbol, kind in sorted(symbols.items()):
        if kind in BRIDGE_SYMBOL_KINDS and symbol not in locations:
            findings.append(
                _finding(
                    "bridge_symbol_without_location",
                    f"{symbol}:{kind} has no bridge_declared_in location",
                    data={"symbol": symbol, "symbol_kind": kind},
                )
            )

    for rel_name, pairs in same_pairs.items():
        for pair in sorted(pairs):
            if pair not in link_types:
                findings.append(
                    _finding(
                        "same_pair_missing_link_type",
                        f"{rel_name}{pair} has no bridge_link_type",
                        data={"same_relation": rel_name, "pair": list(pair)},
                    )
                )
            if pair not in confidences:
                findings.append(
                    _finding(
                        "same_pair_missing_confidence",
                        f"{rel_name}{pair} has no bridge_confidence",
                        data={"same_relation": rel_name, "pair": list(pair)},
                    )
                )
            if rel_name == "same_relation" and pair not in argument_orders:
                findings.append(
                    _finding(
                        "same_relation_missing_argument_order",
                        f"same_relation{pair} has no bridge_argument_order",
                        data={"pair": list(pair)},
                    )
                )

    for pair, link_type in sorted(link_types.items()):
        if pair not in confidences:
            findings.append(
                _finding(
                    "bridge_link_type_missing_confidence",
                    f"bridge_link_type{pair}={link_type} has no bridge_confidence",
                    data={"pair": list(pair), "bridge_link_type": link_type},
                )
            )
        if link_type == "UnresolvedDrift":
            if any(pair in pairs for pairs in same_pairs.values()):
                findings.append(
                    _finding(
                        "unresolved_drift_marked_same",
                        f"{pair} is marked UnresolvedDrift and also same_*",
                        data={"pair": list(pair)},
                    )
                )

    for family in sorted(families):
        members = family_members.get(family, set())
        if len(members) < 2:
            findings.append(
                _finding(
                    "bridge_family_too_small",
                    f"{family} has fewer than two bridge_family_member links",
                    data={"family": family, "member_count": len(members)},
                )
            )
        if family not in family_anchors:
            findings.append(
                _finding(
                    "bridge_family_missing_anchor",
                    f"{family} has no bridge_family_anchor",
                    data={"family": family},
                )
            )
        if family not in family_link_types:
            findings.append(
                _finding(
                    "bridge_family_missing_link_type",
                    f"{family} has no bridge_family_link_type",
                    data={"family": family},
                )
            )
        if family not in family_confidences:
            findings.append(
                _finding(
                    "bridge_family_missing_confidence",
                    f"{family} has no bridge_family_confidence",
                    data={"family": family},
                )
            )

    projection_role_relations = set(projection_argument_roles) | set(projection_return_roles)
    for relation in sorted(projected_relations | projection_role_relations | projection_kinds | projection_confidences):
        if relation not in projected_relations:
            findings.append(
                _finding(
                    "bridge_projection_role_without_frame",
                    f"{relation} has projection metadata but no bridge_relation_projects_to_frame",
                    data={"symbol": relation},
                )
            )
        if relation in projected_relations and relation not in projection_kinds:
            findings.append(
                _finding(
                    "bridge_projection_missing_kind",
                    f"{relation} projects to a frame but has no bridge_projection_kind",
                    data={"symbol": relation},
                )
            )
        if relation in projected_relations and relation not in projection_confidences:
            findings.append(
                _finding(
                    "bridge_projection_missing_confidence",
                    f"{relation} projects to a frame but has no bridge_projection_confidence",
                    data={"symbol": relation},
                )
            )
        if relation in projected_relations and relation not in projection_role_relations:
            findings.append(
                _finding(
                    "bridge_projection_missing_roles",
                    f"{relation} projects to a frame but has no argument or return roles",
                    data={"symbol": relation},
                )
            )

    hard = [f for f in findings if f["severity"] == "hard"]
    soft = [f for f in findings if f["severity"] == "soft"]
    return {
        "schema": "bridge_lint_v1",
        "bridge_file": str(path),
        "declared_entries": len(entries),
        "declared_symbols": len(symbols),
        "declared_families": len(families),
        "declared_frames": len(frames),
        "declared_roles": len(roles),
        "projected_relations": len(projected_relations),
        "findings": findings,
        "hard_findings": len(hard),
        "soft_findings": len(soft),
        "status": "failed" if hard else "passed",
    }


def _write_reports(result: dict[str, Any], bridge_dir: Path) -> None:
    (bridge_dir / "bridge_lint_v1.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    lines = [
        "# Bridge Lint v1",
        "",
        f"- status: `{result['status']}`",
        f"- declared entries: `{result['declared_entries']}`",
        f"- declared symbols: `{result['declared_symbols']}`",
        f"- declared frames: `{result['declared_frames']}`",
        f"- declared roles: `{result['declared_roles']}`",
        f"- projected relations: `{result['projected_relations']}`",
        f"- hard findings: `{result['hard_findings']}`",
        f"- soft findings: `{result['soft_findings']}`",
        "",
    ]
    if result["findings"]:
        lines.append("## Findings")
        for finding in result["findings"]:
            loc = f" line {finding['line']}" if "line" in finding else ""
            lines.append(
                f"- `{finding['severity']}` `{finding['code']}`{loc}: {finding['message']}"
            )
    else:
        lines.append("No bridge-lint findings.")
    (bridge_dir / "bridge_lint_v1.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("target", help="bridge directory or main_bridge.a4v3 path")
    args = parser.parse_args()

    target = Path(args.target)
    bridge_file = target / "main_bridge.a4v3" if target.is_dir() else target
    result = analyze_bridge(bridge_file)
    _write_reports(result, bridge_file.parent)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if result["hard_findings"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
