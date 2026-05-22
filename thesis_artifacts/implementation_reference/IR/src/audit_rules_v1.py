"""audit_rules_v1.py

Audit every rule in `IR/rules/*/diagnostic_rules.json`. For each rule
produce a row with:

  - name, module
  - what_it_counts, how_to_compute (concept)
  - threshold (auto-checkable? prose?)
  - repair_target (actionable for the agent?)
  - current_status (ok/warning/fail/inspect for the sample entry)
  - implementation_state (real/None/missing key)
  - similarity_group (lexical clustering by name)
  - overlap_candidates (other rules with similar name root)

Outputs:
  IR/outputs/runs/unified_methodology_v1/rules_audit_v1.json
  IR/outputs/runs/unified_methodology_v1/rules_audit_v1.md

The .md is the human-readable summary the user reviews to decide what to
keep / drop / implement.
"""
from __future__ import annotations
import json
import pathlib
import re
import sys
from collections import defaultdict, Counter

ROOT = pathlib.Path(r"<WORKSPACE_ROOT>")
RULES = ROOT / "IR/rules"
RUN = ROOT / "IR/outputs/runs/unified_methodology_v1"
SAMPLE_ENTRY = RUN / "01_local_blocks/sections/section_4_6"

sys.path.insert(0, str(ROOT / "IR/src"))
import run_diagnostic_suite_v1 as rds  # noqa: E402


_GENERIC_REPAIR_PHRASES = (
    "inspect relevant artifacts",
    "apply module-specific repair rules",
    "no universal repair",
)


def _is_actionable_repair(text: str) -> bool:
    if not text:
        return False
    t = text.lower().strip()
    if not t:
        return False
    return not any(phrase in t for phrase in _GENERIC_REPAIR_PHRASES)


def _is_machine_threshold(thr: dict) -> bool:
    return rds._has_machine_thresholds(thr or {})


def _name_root(name: str) -> str:
    """Cluster key — first 2 word-pieces of snake_case name."""
    parts = (name or "").split("_")
    if len(parts) >= 2:
        return "_".join(parts[:2])
    return name


def _classify_concept(rule: dict) -> str:
    """Coarse semantic category from name + description."""
    n = (rule.get("name", "") + " " +
         (rule.get("what_it_counts", "") or "") + " " +
         (rule.get("how_to_compute", "") or "")).lower()

    if "ungrounded" in n or "grounding" in n:
        return "grounding"
    if any(t in n for t in ("modality", "deontic", "obligation",
                              "permission", "prohibition", "shall", "may",
                              "cannot")):
        return "modality_deontic"
    if any(t in n for t in ("temporal", "before", "after", "eventually",
                              "always", "until")):
        return "temporal"
    if any(t in n for t in ("token", "lexical", "jaccard", "precision",
                              "recall", "coverage", "phrase")):
        return "lexical_token"
    if any(t in n for t in ("clause", "clause_coverage", "normalized_clause")):
        return "clause_alignment"
    if any(t in n for t in ("identifier", "compound_identifier",
                              "subterm", "crosslink", "decomposition")):
        return "identifier_lint"
    if any(t in n for t in ("render", "bertscore", "nli", "verbalize")):
        return "render_back"
    if any(t in n for t in ("probe_",)):
        return "targeted_probe"
    if any(t in n for t in ("multi_judge", "judge_", "critic")):
        return "judge_critic"
    if any(t in n for t in ("counterexample", "counter_example")):
        return "counterexample"
    if any(t in n for t in ("fact_recall", "fact_precision", "fact_f1",
                              "missing_fact", "render_only")):
        return "fact_extraction"
    if any(t in n for t in ("structure", "shape_error", "ast", "parse")):
        return "ir_structure"
    if any(t in n for t in ("merge", "overlay", "canonical", "cluster",
                              "alignment", "mapping")):
        return "merge_alignment"
    if any(t in n for t in ("variant", "stability", "consensus")):
        return "multi_variant"
    if any(t in n for t in ("call_count", "latency", "cost_estimate",
                              "wall_clock", "tokens_in", "tokens_out",
                              "timeout", "retry")):
        return "llm_meta"
    if any(t in n for t in ("silver", "gold")):
        return "silver_gold"
    if any(t in n for t in ("bridge_", "role_link")):
        return "bridge_resolution"
    if any(t in n for t in ("keep_", "preserve_", "make_edits_explicit",
                              "avoid_padding", "use_valid_ir_surface")):
        return "soft_principle"
    if any(t in n for t in ("count", "ratio", "_mass", "_rate")):
        return "ir_count_or_ratio"
    return "other"


# Rules from our new fidelity module — concepts already covered.
def _our_fidelity_concepts() -> set[str]:
    """Names of metrics we already have in source_to_ir_fidelity (and the
    backing modules: B5/B6/B8/A/B2/B3/family_coverage/lowering_audit)."""
    return {
        "fact_recall_to_source", "fact_precision_to_source",
        "missing_source_fact_count", "render_hallucinated_fact_count",
        "stronger_pair_count", "weaker_pair_count",
        "modality_quantifier_loss_in_render",
        "source_phrase_coverage_rate", "uncovered_source_phrases",
        "targeted_probe_preservation_rate",
        "multi_judge_unanimous", "multi_judge_mode_corresponds",
        "counterexample_source_ir_agreement_rate",
        "innf_family_diversity", "expected_family_present",
        "lowering_smell_count",
        "deontic_lowering_correct", "temporal_lowering_correct",
    }


def audit_rules() -> dict:
    samples = [SAMPLE_ENTRY]
    rows: list[dict] = []
    for rj in sorted(RULES.glob("*/diagnostic_rules.json")):
        data = json.loads(rj.read_text(encoding="utf-8"))
        module = data.get("module", rj.parent.name)
        for r in data.get("rules", []):
            if not isinstance(r, dict):
                continue
            name = r.get("name", "")
            thresholds = r.get("thresholds", {}) or {}
            value_paths = r.get("value_paths", []) or []
            repair = r.get("repair_target", "") or ""

            # current status — try resolve on sample
            value, found, level = None, False, "error_no_value"
            for vp in value_paths:
                v, ok = rds._extract_value(samples[0], vp, rule_name=name)
                if ok:
                    value = v
                    found = True
                    break
            if not found:
                level = "error_no_value"
            elif value is None:
                level = "value_is_none"
            else:
                level = rds._evaluate_thresholds(value, thresholds, "")

            rows.append({
                "module": module,
                "name": name,
                "what_it_counts": (r.get("what_it_counts") or "").strip()[:200],
                "how_to_compute": (r.get("how_to_compute") or "").strip()[:200],
                "threshold_machine_checkable": _is_machine_threshold(thresholds),
                "thresholds": thresholds,
                "repair_target": repair[:200],
                "actionable_repair": _is_actionable_repair(repair),
                "current_status_on_sample": level,
                "current_value_on_sample": value,
                "concept_category": _classify_concept(r),
                "name_root": _name_root(name),
                "duplicates_our_fidelity": name in _our_fidelity_concepts(),
            })

    # find lexical overlaps within legacy
    by_root: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        by_root[r["name_root"]].append(r)
    for r in rows:
        peers = by_root[r["name_root"]]
        r["overlap_candidates"] = [p["name"] for p in peers
                                     if p["name"] != r["name"]][:5]

    return {"rows": rows}


def write_summary(audit: dict) -> None:
    rows = audit["rows"]
    total = len(rows)
    by_cat: Counter = Counter(r["concept_category"] for r in rows)
    by_status: Counter = Counter(r["current_status_on_sample"] for r in rows)
    by_module: Counter = Counter(r["module"] for r in rows)
    impl = sum(1 for r in rows
               if r["current_status_on_sample"] not in
               ("error_no_value", "value_is_none"))
    actionable = sum(1 for r in rows if r["actionable_repair"])
    machine_thr = sum(1 for r in rows if r["threshold_machine_checkable"])
    duplicates = sum(1 for r in rows if r["duplicates_our_fidelity"])

    md: list[str] = []
    md.append(f"# Rules audit — {RUN.name}\n")
    md.append(f"- Total rules: **{total}**")
    md.append(f"- Implemented (computes a real value on sample entry): "
              f"**{impl}** ({100 * impl // total}%)")
    md.append(f"- Has actionable repair_target: **{actionable}** "
              f"({100 * actionable // total}%)")
    md.append(f"- Has machine-checkable threshold: **{machine_thr}** "
              f"({100 * machine_thr // total}%)")
    md.append(f"- Already covered by our fidelity rules: **{duplicates}**")
    md.append("")
    md.append("## By module")
    md.append("| module | rules |")
    md.append("|---|---:|")
    for m, n in by_module.most_common():
        md.append(f"| `{m}` | {n} |")
    md.append("")
    md.append("## By concept category")
    md.append("| category | rules |")
    md.append("|---|---:|")
    for c, n in by_cat.most_common():
        md.append(f"| `{c}` | {n} |")
    md.append("")
    md.append("## By current status (on sample entry section_4_6)")
    md.append("| status | rules |")
    md.append("|---|---:|")
    for s, n in by_status.most_common():
        md.append(f"| `{s}` | {n} |")
    md.append("")
    md.append("## Per-category breakdown")
    md.append("")

    by_cat_rows: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        by_cat_rows[r["concept_category"]].append(r)

    for cat in sorted(by_cat_rows, key=lambda c: -len(by_cat_rows[c])):
        items = by_cat_rows[cat]
        md.append(f"### `{cat}` — {len(items)} rules")
        md.append("")
        impl_in_cat = sum(1 for r in items
                          if r["current_status_on_sample"] not in
                          ("error_no_value", "value_is_none"))
        action_in_cat = sum(1 for r in items if r["actionable_repair"])
        md.append(f"- implemented: **{impl_in_cat}/{len(items)}**")
        md.append(f"- actionable repair: **{action_in_cat}/{len(items)}**")
        md.append("")
        md.append("| name | module | status | machine_thr | actionable | what_it_counts |")
        md.append("|---|---|---|---|---|---|")
        for r in sorted(items, key=lambda x: x["name"]):
            n = r["name"]
            mod = r["module"]
            st = r["current_status_on_sample"]
            mt = "✓" if r["threshold_machine_checkable"] else " "
            ac = "✓" if r["actionable_repair"] else " "
            wic = (r["what_it_counts"] or "").replace("|", "\\|")[:80]
            md.append(f"| `{n}` | `{mod}` | `{st}` | {mt} | {ac} | {wic} |")
        md.append("")

    out = RUN / "rules_audit_v1.md"
    out.write_text("\n".join(md), encoding="utf-8")
    json_out = RUN / "rules_audit_v1.json"
    json_out.write_text(json.dumps(audit, ensure_ascii=False, indent=2)
                         + "\n", encoding="utf-8")
    print(f"Wrote {out}")
    print(f"Wrote {json_out}")
    print()
    print("Quick stats:")
    print(f"  total: {total}")
    print(f"  implemented: {impl} ({100 * impl // total}%)")
    print(f"  actionable repair: {actionable} ({100 * actionable // total}%)")
    print(f"  machine threshold: {machine_thr} ({100 * machine_thr // total}%)")
    print(f"  duplicates our fidelity: {duplicates}")
    print()
    print(f"By category:")
    for c, n in by_cat.most_common():
        print(f"  {c}: {n}")


if __name__ == "__main__":
    audit = audit_rules()
    write_summary(audit)
