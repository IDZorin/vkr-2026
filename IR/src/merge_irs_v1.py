"""merge_irs_v1.py

Generic IR merge: combine N a4v3 IR strings into one canonical IR.

Works at any granularity — clause-level, span-level, document-level,
or multi-document. The merge function only knows about a4v3
declarations; it doesn't care what scope produced them.

Strategy (V0 — syntactic dedup):
  1. Parse each input IR via a4v3_parser_v1.
  2. Dedup declarations by (family, name).
     - First non-trivial occurrence wins.
     - Subsequent duplicates with same name+family are dropped silently.
     - SymbolDecl with same name but different signature → conflict
       reported in merge_meta, first kept.
  3. Sort declarations into canonical order: types → symbols → asserts
     → other.
  4. Emit by concatenating each chosen decl's `raw` text.

CLI:
    python merge_irs_v1.py --inputs a.a4v3 b.a4v3 c.a4v3 --out merged.a4v3
"""
from __future__ import annotations
import argparse
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import a4v3_parser_v1 as a4v3  # noqa: E402


_FAMILY_ORDER = (
    "TypeDecl", "SymbolDecl", "PathDecl", "ActionDecl",
    "AssertDecl", "DeonticDecl", "TemporalDecl", "ValidationDecl",
    "ProbabilisticDecl", "GameDecl", "GraphDecl", "TheoremDecl",
)
_FAMILY_PRIORITY = {f: i for i, f in enumerate(_FAMILY_ORDER)}


def _signature_key(d: dict) -> str | None:
    """Stable key for symbol-conflict detection (signature mismatch)."""
    if d.get("family") != "SymbolDecl":
        return None
    args = d.get("args") or []
    rs = d.get("result_sort") or ""
    sort = d.get("sort") or ""
    return f"{d.get('kind','')}({','.join(args)})->{rs}|{sort}"


def merge(inputs: list[str]) -> dict:
    """Take a list of a4v3 IR strings, return merge result.

    Returns dict:
      - "merged_text": str  — final IR
      - "n_inputs": int
      - "n_input_decls": int
      - "n_output_decls": int
      - "conflicts": [...]  — symbol conflicts (different signatures)
      - "duplicates": [...] — exact dedups (same family+name, identical)
      - "by_family": {family: count}
    """
    asts = []
    for i, txt in enumerate(inputs):
        try:
            ast = a4v3.parse(txt, strict=False)
        except Exception as e:
            ast = {"declarations": [], "warnings": [
                {"line_no": 0, "message": f"merge: parse error in input {i}: {e}"}
            ]}
        asts.append(ast)

    seen_keys: dict[tuple[str, str], dict] = {}
    conflicts: list[dict] = []
    duplicates: list[dict] = []

    for input_idx, ast in enumerate(asts):
        for d in ast.get("declarations", []):
            family = d.get("family", "")
            name = d.get("name", "")
            if not family or not name:
                continue
            key = (family, name)
            if key not in seen_keys:
                seen_keys[key] = {**d, "_input_idx": input_idx}
                continue
            # duplicate
            existing = seen_keys[key]
            sig_new = _signature_key(d)
            sig_old = _signature_key(existing)
            if sig_new is not None and sig_old is not None and sig_new != sig_old:
                conflicts.append({
                    "family": family, "name": name,
                    "kept_signature": sig_old, "kept_from_input": existing["_input_idx"],
                    "dropped_signature": sig_new, "dropped_from_input": input_idx,
                })
            else:
                duplicates.append({
                    "family": family, "name": name,
                    "kept_from_input": existing["_input_idx"],
                    "dropped_from_input": input_idx,
                })

    chosen = list(seen_keys.values())
    chosen.sort(key=lambda d: (
        _FAMILY_PRIORITY.get(d.get("family", ""), 99),
        d.get("name", ""),
    ))

    lines: list[str] = []
    for d in chosen:
        raw = (d.get("raw") or "").rstrip()
        if raw:
            lines.append(raw)

    merged_text = "\n".join(lines) + ("\n" if lines else "")

    by_family: dict[str, int] = {}
    for d in chosen:
        f = d.get("family", "?")
        by_family[f] = by_family.get(f, 0) + 1

    return {
        "merged_text": merged_text,
        "n_inputs": len(inputs),
        "n_input_decls": sum(len(a.get("declarations", [])) for a in asts),
        "n_output_decls": len(chosen),
        "conflicts": conflicts,
        "duplicates": duplicates,
        "by_family": by_family,
    }


def merge_files(input_paths: list[pathlib.Path],
                 out_path: pathlib.Path | None = None) -> dict:
    inputs = [p.read_text(encoding="utf-8") for p in input_paths]
    res = merge(inputs)
    if out_path is not None:
        out_path.write_text(res["merged_text"], encoding="utf-8")
        meta_path = out_path.with_suffix(".merge_meta.json")
        meta = {k: v for k, v in res.items() if k != "merged_text"}
        meta["input_paths"] = [str(p) for p in input_paths]
        meta_path.write_text(
            json.dumps(meta, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8")
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--inputs", nargs="+", required=True,
                    help="a4v3 IR files to merge")
    ap.add_argument("--out", required=True, help="output a4v3 path")
    args = ap.parse_args()
    res = merge_files([pathlib.Path(p) for p in args.inputs],
                       pathlib.Path(args.out))
    print(json.dumps({k: v for k, v in res.items() if k != "merged_text"},
                       ensure_ascii=False, indent=2, default=str))


if __name__ == "__main__":
    main()
