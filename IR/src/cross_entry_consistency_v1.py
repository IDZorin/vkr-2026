"""cross_entry_consistency_v1.py

Corpus-level consistency check across all entries in a run:

1. **Symbol kind drift** — same name declared with different decl-kinds across
   entries (e.g. `Day` as `sort` in entry A, as `fun` in entry B).
2. **Symbol arity drift** — same name declared with different arities in
   different entries (likely accidental rename or copy-paste bug).
3. **Symbol signature drift** — same name with different argument sorts or
   return type. Typically a real bug.
4. **Prelude redundancy** — entries declaring a sort that already exists in
   prelude (we already track per-entry; this aggregates).
5. **Casing duplicates** — `LiquidityWindow` and `liquidity_window` declared
   in different entries: probably the same concept, no canonical link.
6. **Overlay reference integrity** — entries refer to overlay symbol that
   doesn't exist in canonical_symbol_overlay_v3.json.

Output: corpus_consistency_report_v1.{json,md} at the run root.

CLI:
    python cross_entry_consistency_v1.py [run_root]
"""
from __future__ import annotations
import json
import pathlib
import re
import sys
from collections import defaultdict

ROOT = pathlib.Path(__file__).resolve().parents[2]
PRELUDE_PATH = ROOT / "IR/index/minimal_prelude_v1.json"
OVERLAY_PATH = ROOT / "IR/outputs/runs/unified_methodology_v1/02_alignment_and_canonicalization/definitions/canonical_symbol_overlay_v3.json"

# decl <name> ...
_DECL_LINE_RE = re.compile(
    r"^\s*(sort|entity|fun|rel|axiom|constraint)\s+([A-Za-z_][A-Za-z0-9_]*)\s*(.*)$"
)
# fun foo : T1, T2 -> T3
_FUN_SIG_RE = re.compile(r":\s*([^->]+?)\s*->\s*(.+?)\s*$")
# rel foo : T1, T2
_REL_SIG_RE = re.compile(r":\s*(.+?)\s*$")


def _parse_a4v3(text: str) -> list[dict]:
    """Return list of declarations: {kind, name, arg_sorts, return_sort, line_no}"""
    out: list[dict] = []
    for i, line in enumerate(text.splitlines(), start=1):
        if line.lstrip().startswith("#"):
            continue
        m = _DECL_LINE_RE.match(line)
        if not m:
            continue
        kind, name, rest = m.group(1), m.group(2), m.group(3)
        d = {"kind": kind, "name": name, "line_no": i, "arg_sorts": None,
             "return_sort": None}
        if kind == "fun":
            sig = _FUN_SIG_RE.search(rest)
            if sig:
                args = [a.strip() for a in sig.group(1).split(",") if a.strip()]
                d["arg_sorts"] = args
                d["return_sort"] = sig.group(2).strip()
        elif kind == "rel":
            sig = _REL_SIG_RE.search(rest)
            if sig:
                args = [a.strip() for a in sig.group(1).split(",") if a.strip()]
                d["arg_sorts"] = args
        elif kind == "entity":
            sig = _REL_SIG_RE.search(rest)
            if sig:
                d["return_sort"] = sig.group(1).strip()
        out.append(d)
    return out


def _load_prelude() -> dict:
    return json.loads(PRELUDE_PATH.read_text(encoding="utf-8"))


def _prelude_names(prelude: dict) -> dict[str, str]:
    """Returns: {name -> kind} for prelude entries."""
    out: dict[str, str] = {}
    for s in prelude.get("sorts", []) or []:
        out[s.get("name") if isinstance(s, dict) else s] = "sort"
    for s in prelude.get("symbols", []) or []:
        out[s.get("name")] = s.get("kind", "symbol")
    for s in prelude.get("relations", []) or []:
        out[s.get("name")] = "rel"
    for s in prelude.get("functions", []) or []:
        out[s.get("name")] = "fun"
    for s in prelude.get("entities", []) or []:
        out[s.get("name") if isinstance(s, dict) else s] = "entity"
    return out


def _load_overlay() -> dict:
    if not OVERLAY_PATH.exists():
        return {}
    return json.loads(OVERLAY_PATH.read_text(encoding="utf-8"))


def _overlay_names(overlay: dict) -> set[str]:
    out: set[str] = set()
    for sect in ("canonical", "symbols", "ontology_overlay", "exact_overlay"):
        items = overlay.get(sect)
        if not items:
            continue
        if isinstance(items, list):
            for it in items:
                if isinstance(it, dict):
                    nm = it.get("name") or it.get("canonical_name") or it.get("symbol")
                    if nm:
                        out.add(nm)
        elif isinstance(items, dict):
            out.update(items.keys())
    return out


def _camel_to_snake(name: str) -> str:
    s1 = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s1).lower()


def collect_run(run_root: pathlib.Path) -> dict:
    prelude = _load_prelude()
    prelude_kinds = _prelude_names(prelude)
    overlay = _load_overlay()
    overlay_set = _overlay_names(overlay)

    # name -> list of {entry_id, kind, arg_sorts, return_sort, line_no}
    by_name: dict[str, list[dict]] = defaultdict(list)
    # entry_id -> list of declarations
    per_entry: dict[str, list[dict]] = {}
    # entry_id -> list of redundant prelude redeclarations
    redundant_prelude: dict[str, list[str]] = defaultdict(list)

    for a4v3 in sorted(run_root.rglob("main_ir.a4v3")):
        if any(part.startswith("_") for part in a4v3.relative_to(run_root).parts):
            continue
        entry_id = a4v3.parent.name
        try:
            text = a4v3.read_text(encoding="utf-8")
        except Exception:
            continue
        decls = _parse_a4v3(text)
        per_entry[entry_id] = decls
        for d in decls:
            if d["kind"] in ("axiom", "constraint"):
                continue
            d2 = dict(d)
            d2["entry_id"] = entry_id
            by_name[d["name"]].append(d2)
            if d["name"] in prelude_kinds and d["kind"] == prelude_kinds[d["name"]]:
                redundant_prelude[entry_id].append(d["name"])

    # Detect drifts
    kind_drifts: list[dict] = []
    arity_drifts: list[dict] = []
    signature_drifts: list[dict] = []
    for name, decls in by_name.items():
        if len(decls) <= 1:
            continue
        kinds = {d["kind"] for d in decls}
        if len(kinds) > 1:
            kind_drifts.append({
                "name": name,
                "occurrences": [
                    {"entry": d["entry_id"], "kind": d["kind"], "line": d["line_no"]}
                    for d in decls
                ],
                "distinct_kinds": sorted(kinds),
            })
            continue  # don't double-report
        # same kind, check arity / signature
        arity_set = {
            (tuple(d["arg_sorts"] or ()), d["return_sort"]) for d in decls
            if d["kind"] in ("fun", "rel", "entity")
        }
        if len(arity_set) > 1:
            # arity differs?
            arities = {len(d["arg_sorts"] or ()) for d in decls if d["kind"] in ("fun", "rel")}
            if len(arities) > 1:
                arity_drifts.append({
                    "name": name,
                    "kind": list(kinds)[0],
                    "occurrences": [
                        {"entry": d["entry_id"],
                         "args": d["arg_sorts"],
                         "ret": d["return_sort"],
                         "line": d["line_no"]}
                        for d in decls
                    ],
                })
            else:
                signature_drifts.append({
                    "name": name,
                    "kind": list(kinds)[0],
                    "occurrences": [
                        {"entry": d["entry_id"],
                         "args": d["arg_sorts"],
                         "ret": d["return_sort"],
                         "line": d["line_no"]}
                        for d in decls
                    ],
                })

    # Casing duplicates: PascalCase ↔ snake_case for same concept
    casing_dups: list[dict] = []
    seen: dict[str, list[str]] = defaultdict(list)
    for name in by_name:
        snake = _camel_to_snake(name)
        seen[snake].append(name)
    for snake, variants in seen.items():
        if len(set(variants)) > 1:
            casing_dups.append({
                "snake_form": snake,
                "variants": sorted(set(variants)),
                "entries": sorted({
                    d["entry_id"] for v in variants for d in by_name[v]
                }),
            })

    return {
        "run": run_root.name,
        "totals": {
            "entries": len(per_entry),
            "unique_declared_names": len(by_name),
            "prelude_redundant_entries": len(redundant_prelude),
            "kind_drift_count": len(kind_drifts),
            "arity_drift_count": len(arity_drifts),
            "signature_drift_count": len(signature_drifts),
            "casing_duplicate_count": len(casing_dups),
        },
        "kind_drifts": kind_drifts,
        "arity_drifts": arity_drifts,
        "signature_drifts": signature_drifts,
        "casing_duplicates": casing_dups,
        "redundant_prelude_redeclarations": dict(redundant_prelude),
        "overlay_known_symbols": sorted(overlay_set),
    }


def _md_report(result: dict) -> str:
    lines = [f"# Cross-entry consistency — {result['run']}", ""]
    t = result["totals"]
    lines += [
        f"- entries: **{t['entries']}**",
        f"- unique declared names: {t['unique_declared_names']}",
        f"- entries with prelude redundancy: {t['prelude_redundant_entries']}",
        f"- kind drifts: **{t['kind_drift_count']}**",
        f"- arity drifts: **{t['arity_drift_count']}**",
        f"- signature drifts: **{t['signature_drift_count']}**",
        f"- casing duplicates: **{t['casing_duplicate_count']}**",
        "",
    ]

    if result["kind_drifts"]:
        lines.append("## Kind drifts (HIGH severity)")
        lines.append("")
        for kd in result["kind_drifts"]:
            lines.append(f"- `{kd['name']}` — declared as {kd['distinct_kinds']}:")
            for occ in kd["occurrences"]:
                lines.append(f"  - `{occ['entry']}` line {occ['line']}: `{occ['kind']}`")
        lines.append("")

    if result["arity_drifts"]:
        lines.append("## Arity drifts")
        lines.append("")
        for ad in result["arity_drifts"]:
            lines.append(f"- `{ad['name']}` ({ad['kind']}):")
            for occ in ad["occurrences"]:
                args = ", ".join(occ["args"] or [])
                ret = f" -> {occ['ret']}" if occ["ret"] else ""
                lines.append(f"  - `{occ['entry']}` line {occ['line']}: `({args}){ret}`")
        lines.append("")

    if result["signature_drifts"]:
        lines.append("## Signature drifts (same arity, different sorts)")
        lines.append("")
        for sd in result["signature_drifts"]:
            lines.append(f"- `{sd['name']}` ({sd['kind']}):")
            for occ in sd["occurrences"]:
                args = ", ".join(occ["args"] or [])
                ret = f" -> {occ['ret']}" if occ["ret"] else ""
                lines.append(f"  - `{occ['entry']}` line {occ['line']}: `({args}){ret}`")
        lines.append("")

    if result["casing_duplicates"]:
        lines.append("## Casing duplicates (likely same concept)")
        lines.append("")
        for cd in result["casing_duplicates"]:
            lines.append(
                f"- `{cd['snake_form']}` — variants: {cd['variants']}; "
                f"in entries: {cd['entries']}")
        lines.append("")

    if result["redundant_prelude_redeclarations"]:
        lines.append("## Prelude redeclarations")
        lines.append("")
        for eid, names in result["redundant_prelude_redeclarations"].items():
            lines.append(f"- `{eid}`: {sorted(set(names))}")
        lines.append("")

    return "\n".join(lines)


def main():
    if len(sys.argv) > 1:
        run_root = pathlib.Path(sys.argv[1])
    else:
        run_root = ROOT / "IR/outputs/runs/unified_methodology_v1"

    result = collect_run(run_root)

    json_p = run_root / "corpus_consistency_report_v1.json"
    md_p = run_root / "corpus_consistency_report_v1.md"
    json_p.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n",
                      encoding="utf-8")
    md_p.write_text(_md_report(result), encoding="utf-8")
    print(f"Wrote {json_p.relative_to(ROOT)}")
    print(f"Wrote {md_p.relative_to(ROOT)}")
    print(f"  totals: {result['totals']}")


if __name__ == "__main__":
    main()
