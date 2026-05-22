"""prelude_loader_v1.py

Read-only view of canonical prelude (and optionally overlay) for LLM
prompt injection.

Purpose: format the names available to agents (L3, L5, normalize, repair)
so they know what to reuse rather than invent.

Sources read:
  IR/index/minimal_prelude_v1.json — canonical cross-methodology prelude
  <run>/02_alignment_and_canonicalization/.../canonical_symbol_overlay_*.json
    — overlay produced by THIS run's merge layer (if it has run yet)

NB: overlay files from previous runs are NOT auto-loaded by default.
Until our merge layer (Stage 3) runs and produces overlay for the
current run, overlay is empty. Caller can pass an explicit overlay_path
to attach a known good overlay.

NO hardcoded BASE_SORTS / math primitives. The project uses domain
carriers (Price, Rational, FxRate, ...) — see ontology_declaration_policy.

CLI:
    python prelude_loader_v1.py [--overlay PATH]
"""
from __future__ import annotations
import argparse
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
PRELUDE_PATH = ROOT / "IR/index/minimal_prelude_v1.json"


_PRELUDE_CACHE: dict | None = None


def get_prelude() -> dict:
    """Canonical prelude — Day, Month, Weekday, FinancialInstrument, etc."""
    global _PRELUDE_CACHE
    if _PRELUDE_CACHE is None:
        _PRELUDE_CACHE = json.loads(PRELUDE_PATH.read_text(encoding="utf-8"))
    return _PRELUDE_CACHE


def get_overlay(overlay_path: pathlib.Path | None = None) -> dict:
    """Read overlay if file exists. Returns empty dict if no path or missing."""
    if overlay_path is None or not overlay_path.exists():
        return {"exact_overlay": [], "ontology_overlay": []}
    return json.loads(overlay_path.read_text(encoding="utf-8"))


def prelude_sort_names() -> set[str]:
    return {s["name"] for s in get_prelude().get("sorts", []) if s.get("name")}


def prelude_entity_map() -> dict[str, str]:
    """name -> sort"""
    return {e["name"]: e.get("sort", "") for e in get_prelude().get("entities", [])
            if e.get("name")}


def overlay_sort_names(overlay_path: pathlib.Path | None = None) -> set[str]:
    overlay = get_overlay(overlay_path)
    out: set[str] = set()
    for it in overlay.get("exact_overlay", []) or []:
        if not isinstance(it, dict):
            continue
        label = it.get("canonical_label")
        kinds = {m.get("kind") for m in (it.get("mappings") or [])
                 if isinstance(m, dict)}
        if "sort" in kinds and label:
            out.add(label)
    for it in overlay.get("ontology_overlay", []) or []:
        if not isinstance(it, dict):
            continue
        label = it.get("canonical_label") or it.get("name")
        kinds = {m.get("kind") for m in (it.get("mappings") or [])
                 if isinstance(m, dict)}
        if "sort" in kinds and label:
            out.add(label)
    return out


def format_for_prompt(overlay_path: pathlib.Path | None = None) -> str:
    """Render available canonical names for LLM prompt injection.

    Lists prelude sorts + entities. Includes overlay only if `overlay_path`
    is provided AND the file exists (i.e. our merge layer has produced
    overlay for the current run).
    """
    lines: list[str] = []
    p_sorts = sorted(prelude_sort_names())
    if p_sorts:
        lines.append("AVAILABLE PRELUDE SORTS (canonical, do not redeclare):")
        lines.append("  " + ", ".join(p_sorts))
        lines.append("")
    p_ents = prelude_entity_map()
    if p_ents:
        lines.append("AVAILABLE PRELUDE ENTITIES (name : sort):")
        for n in sorted(p_ents):
            lines.append(f"  {n} : {p_ents[n]}")
        lines.append("")
    o_sorts = sorted(overlay_sort_names(overlay_path))
    if o_sorts:
        lines.append("AVAILABLE OVERLAY SORTS (this run's merge canonical, prefer over novel):")
        lines.append("  " + ", ".join(o_sorts))
        lines.append("")
    return "\n".join(lines).rstrip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--overlay", default=None,
                    help="optional path to canonical_symbol_overlay JSON "
                         "(typically populated by this run's merge layer)")
    args = ap.parse_args()
    overlay_path = pathlib.Path(args.overlay) if args.overlay else None
    print("=== Prelude (+ overlay if provided) for prompt injection ===\n")
    print(format_for_prompt(overlay_path))


if __name__ == "__main__":
    main()
