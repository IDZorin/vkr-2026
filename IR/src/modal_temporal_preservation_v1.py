"""modal_temporal_preservation_v1.py

Det-only metrics: do modal verbs / temporal connectives / quantifiers / numeric
literals survive the source -> IR -> render trip?

Compares three texts:
- source.md           (raw)
- normalized.md       (after stage 1)
- render_back text    (from existing *_llm_render_metrics_*.json — already produced)

For each text:
- Count modals (shall/may/must/will/can/should/cannot/...)
- Count temporal markers (before/after/then/when/until/since/while/during/...)
- Count quantifiers (every/all/any/some/no/none/each)
- Count numeric literals (integers, decimals, percentages)

Drift = abs(source_count - render_count). Missing = source has more.
Added = render has more (LLM hallucinated).

Also extract from a4v3 IR text:
- count of `implies` (modal proxy)
- count of `forall` / `exists` (quantifier proxy)
- count of numeric literals in declarations & constraints

Saves: metrics_modal_temporal_preservation_v1.json per entry.

CLI:
    python modal_temporal_preservation_v1.py [entry_dir|run_root]
    With no args, walks the default run.
"""
from __future__ import annotations
import json
import pathlib
import re
import sys
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parents[2]

# Domain-agnostic English token sets (no methodology-specific terms).
MODALS = {
    "shall", "must", "may", "should", "will", "would", "can", "could",
    "might", "ought", "cannot",
}
NEGATED_MODALS = {"may not", "shall not", "must not", "cannot", "should not", "will not"}
TEMPORAL = {
    "before", "after", "then", "when", "while", "during", "until", "since",
    "prior", "subsequently", "thereafter", "previously", "afterwards",
}
QUANTIFIERS = {
    "every", "all", "any", "some", "no", "none", "each", "either", "neither",
}

# Match standalone numbers, decimals, percentages, currency-ish patterns.
NUMERIC_RE = re.compile(r"\b\d+(?:\.\d+)?%?\b")

WORD_RE = re.compile(r"\b[\w']+\b", re.UNICODE)


def _tokenize_lower(text: str) -> list[str]:
    return [m.group(0).lower() for m in WORD_RE.finditer(text or "")]


def _strip_md_headers(text: str) -> str:
    if not text:
        return ""
    return "\n".join(
        line for line in text.splitlines() if not line.lstrip().startswith("#")
    )


def _count_categories(text: str) -> dict[str, dict]:
    text = _strip_md_headers(text or "")
    tokens = _tokenize_lower(text)
    text_lower = text.lower()

    modal_counts: Counter = Counter()
    temporal_counts: Counter = Counter()
    quant_counts: Counter = Counter()
    for t in tokens:
        if t in MODALS:
            modal_counts[t] += 1
        if t in TEMPORAL:
            temporal_counts[t] += 1
        if t in QUANTIFIERS:
            quant_counts[t] += 1

    neg_modals: Counter = Counter()
    for phrase in NEGATED_MODALS:
        n = text_lower.count(phrase)
        if n:
            neg_modals[phrase] = n

    nums = NUMERIC_RE.findall(text)
    return {
        "modals": dict(modal_counts),
        "negated_modals": dict(neg_modals),
        "temporal": dict(temporal_counts),
        "quantifiers": dict(quant_counts),
        "numeric_literals": nums,
        "_token_count": len(tokens),
    }


def _diff(a: dict, b: dict) -> dict:
    """Return per-key (added, removed) diffs and totals."""
    keys = set(a) | set(b)
    added: dict[str, int] = {}
    removed: dict[str, int] = {}
    for k in keys:
        d = b.get(k, 0) - a.get(k, 0)
        if d > 0:
            added[k] = d
        elif d < 0:
            removed[k] = -d
    return {
        "added_count": sum(added.values()),
        "removed_count": sum(removed.values()),
        "added": added,
        "removed": removed,
    }


def _diff_lists(a: list, b: list) -> dict:
    ca, cb = Counter(a), Counter(b)
    added = (cb - ca)
    removed = (ca - cb)
    return {
        "added_count": sum(added.values()),
        "removed_count": sum(removed.values()),
        "added": dict(added),
        "removed": dict(removed),
    }


_IMPLIES_RE = re.compile(r"\bimplies\b")
_FORALL_RE = re.compile(r"\bforall\b")
_EXISTS_RE = re.compile(r"\bexists\b")
_IFF_RE = re.compile(r"\biff\b")
_NOT_RE = re.compile(r"\bnot\b")
_AND_RE = re.compile(r"\band\b")
_OR_RE = re.compile(r"\bor\b")
# IR numeric literals appear bare in formulas; capture them context-free.
# We strip declarations first to avoid arity numbers (none expected in a4v3).
_DECL_LINE_RE = re.compile(r"^\s*(?:sort|entity|fun|rel|axiom|constraint)\b", re.MULTILINE)


def _ir_logical_counts(a4v3_text: str) -> dict:
    """Count logical operators and numeric literals in raw a4v3 text.

    Comments stripped (lines starting with #), declarations preserved.
    """
    if not a4v3_text:
        return {}
    # strip line comments
    no_comments = "\n".join(
        line for line in a4v3_text.splitlines() if not line.strip().startswith("#")
    )
    return {
        "implies_count": len(_IMPLIES_RE.findall(no_comments)),
        "iff_count": len(_IFF_RE.findall(no_comments)),
        "forall_count": len(_FORALL_RE.findall(no_comments)),
        "exists_count": len(_EXISTS_RE.findall(no_comments)),
        "not_count": len(_NOT_RE.findall(no_comments)),
        "and_count": len(_AND_RE.findall(no_comments)),
        "or_count": len(_OR_RE.findall(no_comments)),
        "numeric_literals": NUMERIC_RE.findall(no_comments),
    }


def _read_render_text(entry_dir: pathlib.Path) -> str:
    for jf in sorted(entry_dir.glob("*_llm_render_metrics_*.json")):
        try:
            data = json.loads(jf.read_text(encoding="utf-8"))
        except Exception:
            continue
        return data.get("render_back_text", "") or ""
    return ""


def analyze_entry(entry_dir: pathlib.Path) -> dict:
    src_p = entry_dir / "source.md"
    nrm_p = entry_dir / "normalized.md"
    a4v3_p = entry_dir / "main_ir.a4v3"

    source = src_p.read_text(encoding="utf-8") if src_p.exists() else ""
    normalized = nrm_p.read_text(encoding="utf-8") if nrm_p.exists() else ""
    render = _read_render_text(entry_dir)
    a4v3 = a4v3_p.read_text(encoding="utf-8") if a4v3_p.exists() else ""

    src_cats = _count_categories(source)
    nrm_cats = _count_categories(normalized)
    rnd_cats = _count_categories(render)
    ir_cats = _ir_logical_counts(a4v3)

    # Drifts: source vs render (overall trip), source vs normalized (stage 1),
    # normalized vs render (stage 2 round-trip).
    def pair(a, b):
        return {
            "modals": _diff(a["modals"], b["modals"]),
            "negated_modals": _diff(a["negated_modals"], b["negated_modals"]),
            "temporal": _diff(a["temporal"], b["temporal"]),
            "quantifiers": _diff(a["quantifiers"], b["quantifiers"]),
            "numeric_literals": _diff_lists(a["numeric_literals"], b["numeric_literals"]),
        }

    drifts = {
        "source_to_render": pair(src_cats, rnd_cats),
        "source_to_normalized": pair(src_cats, nrm_cats),
        "normalized_to_render": pair(nrm_cats, rnd_cats),
    }

    # Aggregate alarm signals: source has X but render lost it.
    alarms: list[dict] = []
    s2r = drifts["source_to_render"]
    for cat in ("modals", "negated_modals", "temporal", "quantifiers", "numeric_literals"):
        if s2r[cat]["removed_count"] > 0:
            alarms.append({
                "kind": f"{cat}_lost_in_render",
                "removed": s2r[cat]["removed"],
                "count": s2r[cat]["removed_count"],
            })
        if s2r[cat]["added_count"] > 0:
            alarms.append({
                "kind": f"{cat}_added_in_render",
                "added": s2r[cat]["added"],
                "count": s2r[cat]["added_count"],
            })

    return {
        "entry_id": entry_dir.name,
        "has_source": bool(source.strip()),
        "has_normalized": bool(normalized.strip()),
        "has_render": bool(render.strip()),
        "has_ir": bool(a4v3.strip()),
        "source": src_cats,
        "normalized": nrm_cats,
        "render": rnd_cats,
        "ir_logical": ir_cats,
        "drifts": drifts,
        "alarms": alarms,
        "alarm_count": len(alarms),
    }


def _save(entry_dir: pathlib.Path, result: dict) -> pathlib.Path:
    out = entry_dir / "metrics_modal_temporal_preservation_v1.json"
    out.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return out


def main():
    if len(sys.argv) > 1:
        target = pathlib.Path(sys.argv[1])
    else:
        target = ROOT / "IR/outputs/runs/unified_methodology_v1"

    if (target / "main_ir.a4v3").exists() or (target / "source.md").exists():
        # single entry
        result = analyze_entry(target)
        out = _save(target, result)
        print(f"Wrote {out}")
        print(f"  alarms: {result['alarm_count']}")
        return

    # walk run root
    n = 0
    n_alarm = 0
    for d in sorted(target.rglob("main_ir.a4v3")):
        entry_dir = d.parent
        if entry_dir.name.startswith("_"):
            continue
        result = analyze_entry(entry_dir)
        _save(entry_dir, result)
        n += 1
        if result["alarm_count"] > 0:
            n_alarm += 1
    print(f"Processed {n} entries; {n_alarm} have at least one drift alarm.")


if __name__ == "__main__":
    main()
