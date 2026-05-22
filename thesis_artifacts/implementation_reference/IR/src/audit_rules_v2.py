"""audit_rules_v2.py

Re-audit rules with proper split:

  WORKING rules (have implementation) — classify by 3 axes:
    - Where (artifact / layer): text / normalized / ir / render /
      ir_vs_text / ir_vs_normalized / triangle / corpus
    - What (measurement type): count / ratio / boolean_check / similarity /
      existence / shape_validation / threshold_pass / lint_pattern
    - Why (role for the agent): actionable_fix / coverage_indicator /
      structural_compliance / layer_alignment

  UNIMPLEMENTED rules — separate list, per-rule decision pending.

Outputs:
  IR/outputs/runs/unified_methodology_v1/rules_audit_v2.json
  IR/outputs/runs/unified_methodology_v1/rules_audit_v2.md
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
SAMPLE = RUN / "01_local_blocks/sections/section_4_6"

sys.path.insert(0, str(ROOT / "IR/src"))
import run_diagnostic_suite_v1 as rds  # noqa: E402


_GENERIC_REPAIR = (
    "inspect relevant artifacts",
    "apply module-specific repair rules",
    "no universal repair",
)


def _is_actionable(text: str) -> bool:
    if not text:
        return False
    t = text.lower().strip()
    return bool(t) and not any(p in t for p in _GENERIC_REPAIR)


def _is_machine(thr: dict) -> bool:
    return rds._has_machine_thresholds(thr or {})


def _trivial_warning_threshold(thr: dict, name: str) -> bool:
    """warning `> 0` for non-error count → trivially fires on every entry."""
    if not isinstance(thr, dict):
        return False
    w = (thr.get("warning") or "").replace(" ", "")
    if w not in ("> 0", ">0"):
        return False
    error_tokens = ("miss", "error", "ungrounded", "loss", "drift", "fail",
                     "hallucin", "missing", "unresolved", "buried", "smell",
                     "violation", "incompat", "conflict", "duplicate",
                     "orphan", "uncovered", "broken")
    return not any(tok in name.lower() for tok in error_tokens)


# ── Classification axis 1: Where (artifact / layer) ──

def _classify_where(rule: dict) -> str:
    paths = rule.get("value_paths") or []
    paths_blob = " ".join(p for p in paths if isinstance(p, str)).lower()

    if "metrics_targeted_probes" in paths_blob:
        return "triangle"
    if "metrics_multi_judge" in paths_blob:
        return "triangle"
    if "metrics_counterexample_probing" in paths_blob:
        return "triangle"
    if "metrics_fact_extraction_compare" in paths_blob:
        return "triangle"
    if "metrics_modal_temporal" in paths_blob:
        return "triangle"
    if "metrics_source_phrase_coverage" in paths_blob:
        return "ir_vs_text"
    if "metrics_family_coverage" in paths_blob:
        return "ir_vs_text"
    if "lowering_audit" in paths_blob:
        return "ir"
    if "_llm_render_metrics_" in paths_blob:
        return "render"
    if "_llm_semantic_verdict_" in paths_blob:
        return "triangle"
    if "merge_alignment_metrics" in paths_blob:
        return "corpus"
    if "ir_structure_metrics" in paths_blob:
        return "corpus"
    if "declaration_lint_report" in paths_blob:
        return "corpus"
    if "micro_ontology_alignment" in paths_blob:
        return "corpus"
    if "main_ir_metrics" in paths_blob:
        if "source_vs_normalized" in paths_blob:
            return "text_vs_normalized"
        if "grounding" in paths_blob or "lexical_coverage" in paths_blob:
            return "ir_vs_text"
        if "semantic_preservation" in paths_blob or "render_back" in paths_blob:
            return "triangle"
        if any(s in paths_blob for s in ("validity", "definition_quality",
                                          "identifier_glue", "parameterization",
                                          "assertion_complexity", "compression",
                                          "extended")):
            return "ir"
        return "ir"
    # by name fallback
    n = rule.get("name", "").lower()
    if "render" in n:
        return "render"
    if "merge" in n or "overlay" in n or "ontology" in n:
        return "corpus"
    if "source_vs_normalized" in n or "normalized_vs_source" in n:
        return "text_vs_normalized"
    if "vs_text" in n or "vs_source" in n or "vs_normalized" in n:
        return "ir_vs_text"
    return "unclassified"


# ── Axis 2: What (measurement type) ──

def _classify_what(rule: dict) -> str:
    n = rule.get("name", "").lower()
    thr = rule.get("thresholds", {}) or {}
    if "_count" in n or n.endswith("count"):
        return "count"
    if "_ratio" in n or "_rate" in n:
        return "ratio"
    if any(t in n for t in ("present", "available", "absent", "exists",
                              "is_", "_failed", "_passed", "_pass",
                              "_below_threshold", "_above_threshold")):
        return "boolean_check"
    if any(t in n for t in ("jaccard", "similarity", "overlap", "distance",
                              "bertscore", "nli")):
        return "similarity"
    if any(t in n for t in ("shape_error", "ast_valid", "parse_failed",
                              "validation_failed", "rendering_ok")):
        return "shape_validation"
    if any(t in n for t in ("recall", "precision", "f1", "coverage")):
        return "ratio"
    if any(t in n for t in ("_mean", "_median", "_max", "_min", "_top",
                              "_score", "_mass", "_depth")):
        return "statistic"
    if any(t in n for t in ("candidates", "findings", "matches")):
        return "lint_pattern"
    if "verdict" in n:
        return "categorical"
    return "other"


# ── Axis 3: Why (role for agent) ──

def _classify_why(rule: dict, working: bool) -> str:
    if not working:
        return "n/a"  # unimplemented — no role
    n = rule.get("name", "").lower()
    repair = (rule.get("repair_target") or "").lower()
    if any(t in n for t in ("ast_valid", "parse_failed", "shape_error",
                              "validation_failed", "rendering_ok")):
        return "structural_compliance"
    if _is_actionable(repair):
        return "actionable_fix"
    if any(t in n for t in ("jaccard", "similarity", "overlap", "distance",
                              "bertscore", "nli", "alignment", "vs_text",
                              "vs_normalized", "vs_source", "_to_text",
                              "_to_normalized", "_to_source", "render_back",
                              "render_to", "source_to")):
        return "layer_alignment"
    return "coverage_indicator"


# ── Status of each rule on sample ──

def _status_on_sample(rule: dict) -> tuple[str, object | None, str | None]:
    """Return (status, value, source_file_basename).

    The third item — which actual file resolved the key — drives the
    `where` classification axis (we trust observed file, not the path
    text which often is a plain-language placeholder)."""
    paths = rule.get("value_paths") or []
    name = rule.get("name", "")
    for vp in paths:
        if not isinstance(vp, str):
            continue
        v, ok = rds._extract_value(SAMPLE, vp, rule_name=name)
        if ok:
            src_file = _which_file_holds_key(SAMPLE, vp, name)
            if v is None:
                return ("unimplemented_value_none", None, src_file)
            return ("working", v, src_file)
    return ("unimplemented_no_key", None, None)


def _which_file_holds_key(entry_dir: pathlib.Path, value_path: str,
                            rule_name: str) -> str | None:
    """Find which file in entry_dir actually contains the resolved key,
    so `where` axis can use observed file rather than path text."""
    # If path is `file::dotted` — file is explicit
    m = rds._PATH_RE.match(value_path) if hasattr(rds, "_PATH_RE") else None
    if m:
        return m.group(1)
    # Else search candidate files in order
    name_to_search = rule_name
    m = re.search(r"<search recursive\s+(?:metrics\s+)?(?:JSON|json)\s+for\s+key\s+`?([^`>]+)`?\s*>",
                   value_path, re.IGNORECASE)
    if m:
        name_to_search = m.group(1).strip()
    elif re.match(r"^[A-Za-z_][A-Za-z0-9_]*(?:\.[A-Za-z_][A-Za-z0-9_]*)+\s*$",
                   value_path):
        name_to_search = value_path.split(".")[-1]

    for p in rds._iter_legacy_metric_files(entry_dir):
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            continue
        if rds._recursive_find(data, name_to_search):
            return p.name
    # corpus-level
    run_root = rds._find_run_root(entry_dir)
    if run_root is not None:
        for fn in rds._CORPUS_METRIC_FILES:
            p = run_root / fn
            if not p.exists():
                continue
            try:
                data = json.loads(p.read_text(encoding="utf-8"))
            except Exception:
                continue
            if rds._recursive_find(data, name_to_search):
                return p.name
    return None


def _classify_where_from_file(src_file: str | None) -> str:
    if not src_file:
        return "unclassified"
    s = src_file.lower()
    if "metrics_targeted_probes" in s:
        return "triangle"
    if "metrics_multi_judge" in s:
        return "triangle"
    if "metrics_counterexample" in s:
        return "triangle"
    if "metrics_fact_extraction" in s:
        return "triangle"
    if "metrics_modal_temporal" in s:
        return "triangle"
    if "metrics_source_phrase_coverage" in s:
        return "ir_vs_text"
    if "metrics_family_coverage" in s:
        return "ir_vs_text"
    if "lowering_audit" in s:
        return "ir"
    if "_llm_render_metrics_" in s:
        return "render"
    if "_llm_semantic_verdict_" in s:
        return "triangle"
    if "merge_alignment" in s:
        return "corpus"
    if "ir_structure_metrics" in s:
        return "corpus"
    if "declaration_lint" in s:
        return "corpus"
    if "manual_section_workspace_artifact" in s:
        return "ir"
    if "main_ir_metrics" in s:
        return "ir_or_layer_metrics"  # need section-level subdivision
    return "unclassified"


def _classify_threshold_state(rule: dict) -> str:
    thr = rule.get("thresholds", {}) or {}
    if _trivial_warning_threshold(thr, rule.get("name", "")):
        return "trivial_warning"
    if not _is_machine(thr):
        return "inspect_only"
    return "auto_judge"


# ── Axis 4: Scope (granularity at which rule operates) ──
#
# In current architecture: one source.md span → one entry directory →
# one main_ir.a4v3 file. So a rule that needs only the local
# IR + source/normalized text is span-level. Rules that aggregate across
# entries (corpus metrics, merge alignment, cross-entry consistency) are
# corpus-level. Entry-level (multiple spans inside one entry) is reserved
# for future architecture where one entry contains several IR fragments.

def _classify_scope(where: str, name: str) -> str:
    if where == "corpus":
        return "corpus"
    n = name.lower()
    if any(t in n for t in ("cross_entry", "across_entries", "between_entries",
                              "merge_alignment", "corpus_", "_global",
                              "registry_consistency", "overlay_consistency")):
        return "corpus"
    if "gold_" in n or "silver_" in n:
        # gold/silver compare against another run — outside-span context
        return "corpus"
    return "span"


def main():
    rules: list[dict] = []
    for rj in sorted(RULES.glob("*/diagnostic_rules.json")):
        data = json.loads(rj.read_text(encoding="utf-8"))
        for r in data.get("rules", []):
            if not isinstance(r, dict):
                continue
            status, value, src_file = _status_on_sample(r)
            working = status == "working"
            thr_state = _classify_threshold_state(r)
            where = _classify_where_from_file(src_file)
            # subdivide the legacy metric file by section path
            if where == "ir_or_layer_metrics":
                vp_blob = " ".join(p for p in (r.get("value_paths") or [])
                                    if isinstance(p, str)).lower()
                # legacy `main_ir_metrics_v1.json` has many top-level
                # sections; map to layers
                if "source_vs_normalized" in vp_blob:
                    where = "text_vs_normalized"
                elif "render_back" in vp_blob or "semantic_preservation" in vp_blob:
                    where = "triangle"
                elif "grounding" in vp_blob or "lexical_coverage" in vp_blob:
                    where = "ir_vs_text"
                else:
                    where = "ir"
            rules.append({
                "module": data.get("module", rj.parent.name),
                "name": r.get("name", ""),
                "what_it_counts": (r.get("what_it_counts") or "").strip()[:200],
                "how_to_compute": (r.get("how_to_compute") or "").strip()[:200],
                "repair_target": (r.get("repair_target") or "").strip()[:200],
                "thresholds": r.get("thresholds", {}),
                "status_on_sample": status,
                "value_on_sample": value,
                "source_file_on_sample": src_file,
                "threshold_state": thr_state,
                "where": where,
                "what": _classify_what(r),
                "why": _classify_why(r, working),
                "scope": _classify_scope(where, r.get("name", "")),
                "actionable": _is_actionable(r.get("repair_target", "")),
            })

    working = [r for r in rules if r["status_on_sample"] == "working"]
    unimpl_none = [r for r in rules if r["status_on_sample"] == "unimplemented_value_none"]
    unimpl_nokey = [r for r in rules if r["status_on_sample"] == "unimplemented_no_key"]

    # Aggregations across working rules
    by_where: Counter = Counter(r["where"] for r in working)
    by_what: Counter = Counter(r["what"] for r in working)
    by_why: Counter = Counter(r["why"] for r in working)
    cross_3d: Counter = Counter((r["where"], r["what"], r["why"]) for r in working)
    by_thr: Counter = Counter(r["threshold_state"] for r in working)
    by_scope: Counter = Counter(r["scope"] for r in working)

    md: list[str] = []
    md.append(f"# Rules audit v2 — {RUN.name}\n")
    md.append(f"- Total: **{len(rules)}**")
    md.append(f"- Working (have implementation, real value): **{len(working)}**")
    md.append(f"- Unimplemented (value=None — concept stub in extended): **{len(unimpl_none)}**")
    md.append(f"- Unimplemented (no key in any metric file): **{len(unimpl_nokey)}**")
    md.append("")

    md.append("## Working rules — by Where")
    md.append("| where | rules |")
    md.append("|---|---:|")
    for k, v in by_where.most_common():
        md.append(f"| `{k}` | {v} |")
    md.append("")

    md.append("## Working rules — by What (measurement type)")
    md.append("| what | rules |")
    md.append("|---|---:|")
    for k, v in by_what.most_common():
        md.append(f"| `{k}` | {v} |")
    md.append("")

    md.append("## Working rules — by Why (role for agent)")
    md.append("| why | rules |")
    md.append("|---|---:|")
    for k, v in by_why.most_common():
        md.append(f"| `{k}` | {v} |")
    md.append("")

    md.append("## Working rules — by threshold state")
    md.append("| state | rules |")
    md.append("|---|---:|")
    for k, v in by_thr.most_common():
        md.append(f"| `{k}` | {v} |")
    md.append("")

    md.append("## Cross-table (where × what × why) — top 20")
    md.append("| where | what | why | rules |")
    md.append("|---|---|---|---:|")
    for (w, wt, wy), n in cross_3d.most_common(20):
        md.append(f"| `{w}` | `{wt}` | `{wy}` | {n} |")
    md.append("")

    # Per-axis cell drilldowns
    md.append("## Working rules — per where, per why")
    md.append("")
    by_where_rules: dict[str, list[dict]] = defaultdict(list)
    for r in working:
        by_where_rules[r["where"]].append(r)
    for where in sorted(by_where_rules, key=lambda x: -len(by_where_rules[x])):
        items = by_where_rules[where]
        md.append(f"### where = `{where}` — {len(items)} rules")
        md.append("")
        per_why: dict[str, list[dict]] = defaultdict(list)
        for r in items:
            per_why[r["why"]].append(r)
        for why in sorted(per_why, key=lambda x: -len(per_why[x])):
            wlist = per_why[why]
            md.append(f"#### why = `{why}` ({len(wlist)} rules)")
            md.append("")
            md.append("| name | module | what | thr | actionable | what_it_counts |")
            md.append("|---|---|---|---|---|---|")
            for r in sorted(wlist, key=lambda x: x["name"])[:50]:
                wic = (r["what_it_counts"] or "").replace("|", "\\|")[:80]
                ac = "✓" if r["actionable"] else " "
                md.append(f"| `{r['name']}` | `{r['module']}` | `{r['what']}` | "
                          f"`{r['threshold_state']}` | {ac} | {wic} |")
            if len(wlist) > 50:
                md.append(f"| _...+{len(wlist)-50} more_ |")
            md.append("")

    # Unimplemented section — separate list for per-rule decisions
    md.append("---")
    md.append("")
    md.append("## Unimplemented rules — decisions pending")
    md.append("")
    md.append(f"### value=None (concept declared in `extended` but stubbed) — "
              f"{len(unimpl_none)}")
    md.append("")
    md.append("| name | module | what_it_counts | how_to_compute |")
    md.append("|---|---|---|---|")
    for r in sorted(unimpl_none, key=lambda x: x["name"]):
        wic = (r["what_it_counts"] or "(no description)").replace("|", "\\|")[:80]
        htc = (r["how_to_compute"] or "(no description)").replace("|", "\\|")[:80]
        md.append(f"| `{r['name']}` | `{r['module']}` | {wic} | {htc} |")
    md.append("")
    md.append(f"### no key in any metric file (no implementation at all) — "
              f"{len(unimpl_nokey)}")
    md.append("")
    md.append("| name | module | what_it_counts | how_to_compute |")
    md.append("|---|---|---|---|")
    for r in sorted(unimpl_nokey, key=lambda x: x["name"]):
        wic = (r["what_it_counts"] or "(no description)").replace("|", "\\|")[:80]
        htc = (r["how_to_compute"] or "(no description)").replace("|", "\\|")[:80]
        md.append(f"| `{r['name']}` | `{r['module']}` | {wic} | {htc} |")

    out = RUN / "rules_audit_v2.md"
    out.write_text("\n".join(md), encoding="utf-8")
    json_out = RUN / "rules_audit_v2.json"
    json_out.write_text(json.dumps(
        {"rules": rules,
         "summary": {
             "total": len(rules),
             "working": len(working),
             "unimpl_value_none": len(unimpl_none),
             "unimpl_no_key": len(unimpl_nokey),
             "by_where": dict(by_where),
             "by_what": dict(by_what),
             "by_why": dict(by_why),
             "by_threshold_state": dict(by_thr),
             "by_scope": dict(by_scope),
         }}, ensure_ascii=False, indent=2, default=str) + "\n",
        encoding="utf-8")
    print(f"Wrote {out}")
    print(f"Wrote {json_out}")
    print()
    print(f"Total: {len(rules)}")
    print(f"  Working: {len(working)}")
    print(f"  Unimplemented (value=None): {len(unimpl_none)}")
    print(f"  Unimplemented (no key): {len(unimpl_nokey)}")
    print()
    print("Where:", dict(by_where))
    print()
    print("Why:", dict(by_why))
    print()
    print("Thresholds:", dict(by_thr))


if __name__ == "__main__":
    main()
