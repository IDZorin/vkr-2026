"""run_diagnostic_suite_v1.py

Unified diagnostic orchestrator: ensures every metric module has run on
each entry, then applies all diagnostic_rules.json across IR/rules/ to
collect one acceptance verdict per entry.

Two phases per entry:

  PHASE 1 — ensure metric files exist
    For each module declared in `module_metric_files` of the rules JSON,
    if the metric JSON file is missing, run the corresponding *_v1.py
    module on the entry. (Det modules always run; LLM modules are
    optional via --skip-llm.)

  PHASE 2 — apply rules
    For each rule:
      - read its `value_paths` (dotted path with `::file_name::` prefix)
      - extract the actual value
      - compare against `thresholds`
      - emit a finding (ok / warning / fail) with evidence

Output:
  per-entry: <entry>/diagnostic_suite_v1.json
  corpus:    <run>/diagnostic_suite_corpus_report_v1.{json,md}

CLI:
  python run_diagnostic_suite_v1.py [entry_dir|run_root] [--skip-llm] [--corpus]
"""
from __future__ import annotations
import argparse
import json
import pathlib
import re
import subprocess
import sys
from collections import Counter, defaultdict

ROOT = pathlib.Path(__file__).resolve().parents[2]
RULES_DIR = ROOT / "IR/rules"
SRC_DIR = ROOT / "IR/src"


def _classify_scope(rule_name: str, value_paths: list) -> str:
    """Per-finding scope axis: span / entry / corpus.

    span: rule operates on local IR + source/normalized of one entry,
          and threshold is meaningful at single-clause/single-span level.
    entry: rule's threshold makes sense on full entry (multi-clause), but
           on a single-span IR it systematically fails (e.g. metrics
           normalised by parameter_slot_mass scale poorly on short IRs).
    corpus: rule needs aggregates across entries (merge alignment, gold/silver
            comparisons, cross-entry consistency).
    """
    paths_blob = " ".join(p for p in value_paths if isinstance(p, str)).lower()
    if any(t in paths_blob for t in ("merge_alignment", "ir_structure_metrics",
                                       "declaration_lint", "micro_ontology",
                                       "inter_run_comparison")):
        return "corpus"
    n = rule_name.lower()
    if any(t in n for t in ("cross_entry", "across_entries", "between_entries",
                              "merge_alignment", "corpus_", "_global",
                              "registry_consistency", "overlay_consistency",
                              "gold_", "silver_")):
        return "corpus"
    # Per-mass / per-slot tradeoff metrics: numerator (e.g. bertscore≤1)
    # divided by denominator that grows with span complexity (parameter_slot_mass,
    # formula_repeat_overuse_mass). On a single-span IR these are systematically
    # below threshold not because IR is bad, but because denominator is large.
    # Mark them as entry-scope so span-level repair doesn't chase them.
    if "_per_parameter_slot_mass" in n or "_per_formula_repeat_overuse_mass" in n \
       or "_per_full_surface_repeat_overuse_mass" in n:
        return "entry"
    return "span"


# Modules that don't need LLM — always safe to run.
_DET_MODULES = {
    "metrics_modal_temporal_preservation_v1.json": "modal_temporal_preservation_v1.py",
    "metrics_source_phrase_coverage_v1.json": "source_phrase_coverage_v1.py",
    "metrics_token_provenance_v1.json": "token_provenance_v1.py",
    "metrics_family_coverage_v1.json": "family_coverage_v1.py",
    "lowering_audit_v1.json": "lowering_audit_v1.py",
    "a4v3_semantic_lint_v1.json": "a4v3_semantic_lint_v1.py",
    
}

# LLM modules — gated by --skip-llm.
_LLM_MODULES = {
    "metrics_targeted_probes_v1.json": "targeted_probes_v1.py",
    "metrics_fact_extraction_compare_v1.json": "fact_extraction_compare_v1.py",
    "metrics_multi_judge_consensus_v1.json": "multi_judge_consensus_v1.py",
    "metrics_counterexample_probing_v1.json": "counterexample_probing_v1.py",
}

PYTHON = sys.executable


def _value_path_metric_file(value_path: str) -> str | None:
    if not isinstance(value_path, str):
        return None
    m = _PATH_RE.match(value_path.strip())
    if not m:
        return None
    return m.group(1)


def _rule_is_llm_gated(rule_name: str, value_paths: list[str],
                       metric_statuses: dict[str, str] | None) -> bool:
    explicit_files = {
        file_name
        for vp in value_paths
        for file_name in [_value_path_metric_file(vp)]
        if file_name
    }
    if explicit_files & set(_LLM_MODULES):
        return True

    llm_like_rule_names = {
        "semantic_verdict",
        "relation_type",
        "llm_bertscore",
        "llm_contradiction",
        "llm_ir_to_text",
        "llm_text_to_ir",
    }
    if rule_name in llm_like_rule_names or rule_name.startswith("probe_") or rule_name.startswith("llm_"):
        return True

    if metric_statuses:
        llm_statuses = [metric_statuses.get(name, "") for name in _LLM_MODULES]
        if any(str(status).startswith("skipped") for status in llm_statuses):
            if any("llm" in str(vp).lower() or "probe" in str(vp).lower() for vp in value_paths):
                return True
    return False


def _metric_target_is_stale(entry_dir: pathlib.Path, target: pathlib.Path,
                            script_name: str) -> bool:
    """Re-run metric modules when inputs or the module script are newer.

    This keeps local manual workspaces honest: if source.md / normalized.md /
    main_ir.a4v3 changed after the metric JSON was written, suite
    should not silently reuse stale values.
    """
    if not target.exists():
        return True

    target_mtime = target.stat().st_mtime
    deps = [
        entry_dir / "source.md",
        entry_dir / "normalized.md",
        entry_dir / "main_ir.a4v3",
        SRC_DIR / script_name,
    ]
    if target.name == "main_ir_metrics_v1.json":
        deps.extend([
            SRC_DIR / "legacy_metrics/compute_translation_metrics_v1.py",
            SRC_DIR / "legacy_metrics/compute_manual_section_workspace_metrics_v1.py",
            SRC_DIR / "extended_legacy_metrics_v1.py",
            SRC_DIR / "a4v3_parser_v1.py",
            SRC_DIR / "extended_canonical_validator_v1.py",
        ])
    for dep in deps:
        if dep.exists() and dep.stat().st_mtime > target_mtime:
            return True

    if target.name == "main_ir_metrics_v1.json":
        try:
            payload = json.loads(target.read_text(encoding="utf-8"))
        except Exception:
            return True
        if "extended" not in payload:
            return True

    return False


# ─────────────────────────────────────────────────────────────────────────
# Phase 1 — ensure metrics
# ─────────────────────────────────────────────────────────────────────────

def ensure_metrics(entry_dir: pathlib.Path, skip_llm: bool = False,
                   verbose: bool = False) -> dict[str, str]:
    """Run any missing metric modules on the entry. Returns dict of
    file_name → status (`exists` | `ran` | `skipped` | `error: ...`)."""
    statuses: dict[str, str] = {}
    targets = dict(_DET_MODULES)
    if not skip_llm:
        targets.update(_LLM_MODULES)

    for fname, script in targets.items():
        target = entry_dir / fname
        if target.exists() and not _metric_target_is_stale(entry_dir, target, script):
            statuses[fname] = "exists"
            continue
        if skip_llm and fname in _LLM_MODULES:
            statuses[fname] = "skipped (llm gated)"
            continue
        cmd = [PYTHON, str(SRC_DIR / script), str(entry_dir)]
        if verbose:
            print(f"  running {script} on {entry_dir.name}")
        try:
            subprocess.run(cmd, check=True, timeout=300, capture_output=True)
            statuses[fname] = "ran" if target.exists() else "error: no output"
        except subprocess.CalledProcessError as e:
            statuses[fname] = f"error: exit {e.returncode}"
        except subprocess.TimeoutExpired:
            statuses[fname] = "error: timeout"
    return statuses


# ─────────────────────────────────────────────────────────────────────────
# Phase 2 — apply rules
# ─────────────────────────────────────────────────────────────────────────

def _load_rule_modules() -> list[dict]:
    """Load all diagnostic_rules.json across IR/rules/*/."""
    out: list[dict] = []
    for rj in sorted(RULES_DIR.glob("*/diagnostic_rules.json")):
        try:
            data = json.loads(rj.read_text(encoding="utf-8"))
            data["_path"] = str(rj.relative_to(ROOT))
            out.append(data)
        except Exception:
            continue
    return out


_PATH_RE = re.compile(r"^([^:]+\.json)::(.+)$")
# Legacy placeholder forms used in the V6 689-rule corpus:
#   "<search recursive metrics JSON for key `name`>"
#   "<same JSON key as metric name when present>"
#   "<related section in metrics JSON>"
_LEGACY_RECURSIVE_RE = re.compile(
    r"<search recursive\s+(?:metrics\s+)?(?:JSON|json)\s+for\s+key\s+`?([^`>]+)`?\s*>",
    re.IGNORECASE
)
_LEGACY_SAME_KEY_RE = re.compile(r"<same JSON key as metric name", re.IGNORECASE)
# Generic plain-text placeholders like
#   "<check output, lint report, checklist result, or generated diagnostic finding>"
#   "<related section in metrics JSON>"
# — fall back to recursive search by rule name.
_LEGACY_GENERIC_PLACEHOLDER_RE = re.compile(r"^<.+>$")


_LEGACY_METRIC_FILES = (
    "main_ir_metrics_v1.json",
    "manual_ir_workspace_metrics_current_v1.json",
)
# glob patterns: per-entry metric files include both the det metrics file
# and the LLM-stage outputs (render-back, semantic-verdict). All are fair
# game for legacy rule resolution.
_LEGACY_METRIC_FILE_PATTERNS = (
    "main_ir_metrics_v1.json",
    "manual_ir_workspace_metrics_current_v1.json",
    "*_llm_render_metrics_*.json",
    "*_llm_semantic_verdict_*.json",
    "*_manual_section_workspace_artifact_current_v1.json",
    "inter_run_comparison_v1.json",
    "metrics_targeted_probes_v1.json",
    "metrics_family_coverage_v1.json",
    "metrics_modal_temporal_preservation_v1.json",
    "metrics_source_phrase_coverage_v1.json",
    "lowering_audit_v1.json",
)


def _iter_legacy_metric_files(entry_dir: pathlib.Path):
    seen: set[pathlib.Path] = set()
    for pat in _LEGACY_METRIC_FILE_PATTERNS:
        for p in entry_dir.glob(pat):
            if p in seen or not p.is_file():
                continue
            seen.add(p)
            yield p


# Corpus-level metric files — looked up at run root when per-entry lookup
# returns nothing. Feed merge_canonicalization + ontology_planning rules.
_CORPUS_METRIC_FILES = (
    "merge_alignment_metrics_v1.json",
    "ir_structure_metrics_v1.json",
    "declaration_lint_report_v1.json",
    "micro_ontology_alignment_candidates_v1.json",
)


def _find_run_root(entry_dir: pathlib.Path) -> pathlib.Path | None:
    """Walk up from entry_dir until we find a dir that contains
    `01_local_blocks/`. That's the run root."""
    cur = entry_dir.resolve()
    for _ in range(8):
        if (cur / "01_local_blocks").is_dir():
            return cur
        if cur.parent == cur:
            return None
        cur = cur.parent
    return None


def _recursive_find(data, target_key: str, max_results: int = 8):
    """Walk arbitrary nested dict/list, collect every value under `target_key`."""
    found: list = []

    def _walk(node):
        if len(found) >= max_results:
            return
        if isinstance(node, dict):
            for k, v in node.items():
                if k == target_key:
                    found.append(v)
                    if len(found) >= max_results:
                        return
                _walk(v)
        elif isinstance(node, list):
            for x in node:
                _walk(x)

    _walk(data)
    return found


def _legacy_resolve_recursive(entry_dir: pathlib.Path, key: str):
    """Fallback for old V6 rules: rummage through legacy metrics JSONs and
    return the first value found under `key`. Also checks corpus-level
    files at the run root (merge_alignment, ir_structure, etc.) when
    per-entry files don't have the key."""
    # 1) per-entry files (det metrics + LLM render + LLM verdict + artifact)
    for p in _iter_legacy_metric_files(entry_dir):
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            continue
        hits = _recursive_find(data, key)
        if hits:
            for h in hits:
                if isinstance(h, (int, float, str, bool)):
                    return h, True
            return hits[0], True

    # 2) corpus-level files at run root
    run_root = _find_run_root(entry_dir)
    if run_root is not None:
        for fn in _CORPUS_METRIC_FILES:
            p = run_root / fn
            if not p.exists():
                continue
            try:
                data = json.loads(p.read_text(encoding="utf-8"))
            except Exception:
                continue
            hits = _recursive_find(data, key)
            if hits:
                for h in hits:
                    if isinstance(h, (int, float, str, bool)):
                        return h, True
                return hits[0], True
    return None, False


def _extract_value(entry_dir: pathlib.Path, value_path: str,
                   rule_name: str = ""):
    """Resolve a value-path reference to actual JSON value within entry_dir.

    Supports two formats:
      1. New machine paths:  `metrics_X.json::dotted.path`
      2. Legacy placeholders: `<search recursive metrics JSON for key `X`>`
                              `<same JSON key as metric name when present>`
    """
    # Form 1: explicit file::dotted.path
    m = _PATH_RE.match(value_path)
    if m:
        fname, dotted = m.group(1), m.group(2)
        p = entry_dir / fname
        if not p.exists():
            return None, False
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            return None, False
        cur = data
        for part in dotted.split("."):
            if isinstance(cur, dict) and part in cur:
                cur = cur[part]
            elif isinstance(cur, list) and part.isdigit():
                try:
                    cur = cur[int(part)]
                except IndexError:
                    return None, False
            else:
                return None, False
        return cur, True

    # Form 2: legacy "<search recursive ... key X>"
    m = _LEGACY_RECURSIVE_RE.search(value_path)
    if m:
        return _legacy_resolve_recursive(entry_dir, m.group(1).strip())

    # Form 3: "<same JSON key as metric name when present>" — use rule_name
    if _LEGACY_SAME_KEY_RE.search(value_path) and rule_name:
        return _legacy_resolve_recursive(entry_dir, rule_name)

    # Form 3b: Any generic angle-bracket placeholder — fall back to
    # recursive search by rule name.
    if _LEGACY_GENERIC_PLACEHOLDER_RE.match(value_path.strip()) and rule_name:
        return _legacy_resolve_recursive(entry_dir, rule_name)

    # Form 4: bare dotted path "section.subsection.key" — search legacy
    # per-entry files (incl. LLM render/verdict), then corpus-level files.
    if re.match(r"^[A-Za-z_][A-Za-z0-9_]*(?:\.[A-Za-z_][A-Za-z0-9_]*)+\s*$", value_path):
        candidates: list[pathlib.Path] = list(_iter_legacy_metric_files(entry_dir))
        run_root = _find_run_root(entry_dir)
        if run_root is not None:
            candidates.extend(run_root / fn for fn in _CORPUS_METRIC_FILES)
        for p in candidates:
            if not p.exists():
                continue
            try:
                data = json.loads(p.read_text(encoding="utf-8"))
            except Exception:
                continue
            cur = data
            ok = True
            for part in value_path.split("."):
                if isinstance(cur, dict) and part in cur:
                    cur = cur[part]
                else:
                    ok = False
                    break
            if ok:
                return cur, True
        # leaf-key recursive fallback
        leaf = value_path.split(".")[-1]
        return _legacy_resolve_recursive(entry_dir, leaf)

    return None, False


_TRIVIAL_THRESHOLD_RE = re.compile(r"^\s*[><=!]+\s*-?[\d.]+\s*$")


def _is_machine_threshold(expr) -> bool:
    """A threshold is machine-checkable iff it is a string that's purely a
    comparator + numeric (e.g. `>= 0.85`, `< 0.5`, `= 0`, `true`, `false`,
    `= corresponds`). Anything with extra natural-language explanation
    ("> 0 for hard-fail families", "= 0 unless explicitly expected") is
    not — that's an LLM-generated description, not a checkable rule."""
    if not isinstance(expr, str):
        return False
    s = expr.strip()
    if not s:
        return False
    if s.lower() in ("true", "false"):
        return True
    if _TRIVIAL_THRESHOLD_RE.match(s):
        return True
    # `= corresponds` or `!= corresponds` — string comparison
    if re.match(r"^\s*[!=]=?\s*[A-Za-z_][A-Za-z0-9_-]*\s*$", s):
        return True
    return False


def _has_machine_thresholds(thresholds: dict) -> bool:
    """A rule is auto-checkable iff at least one of {ok, warning, fail} is
    machine-checkable. If only `inspect` is set or all entries are prose,
    rule downgrades to manual review (`inspect`)."""
    for level in ("ok", "warning", "fail"):
        if level in thresholds and _is_machine_threshold(thresholds[level]):
            return True
    return False


def _evaluate_thresholds(value, thresholds: dict, kind: str) -> str:
    """Return one of {ok, warning, fail, inspect, error_no_value, error_no_threshold}.

    - error_no_value: value is None — the metric file doesn't have this key,
      i.e. no generator computes it. This is a bug in rule definitions or
      missing implementation, not a silent skip.
    - error_no_threshold: value is present but no machine-checkable threshold.
      LLM described the metric but not how to grade it. Bug in rule definition.
    - inspect: value is present, no fail/warning/ok matched, only `inspect`
      level present (legitimate manual-review metric).
    """
    if value is None:
        return "error_no_value"
    # If thresholds have no machine-checkable expression, mark as error
    # unless the rule explicitly only has `inspect` (intentional review).
    if not _has_machine_thresholds(thresholds):
        if "inspect" in thresholds:
            return "inspect"
        return "error_no_threshold"
    # numeric thresholds
    def _try_num(s: str) -> tuple[str, float] | None:
        m = re.match(r"\s*(>=|<=|>|<|=|!=)\s*(-?[\d.]+)\s*$", s)
        if not m:
            return None
        return m.group(1), float(m.group(2))

    def _check(op: str, v, thr) -> bool:
        try:
            v = float(v)
        except (TypeError, ValueError):
            return False
        if op == ">=": return v >= thr
        if op == "<=": return v <= thr
        if op == ">":  return v > thr
        if op == "<":  return v < thr
        if op == "=":  return v == thr
        if op == "!=": return v != thr
        return False

    # bool / string equality matchers
    def _str_match(v, expr: str) -> bool:
        expr = expr.strip()
        if expr in ("true", "True"): return v is True
        if expr in ("false", "False"): return v is False
        if expr.startswith("="):
            return str(v).strip() == expr[1:].strip()
        if expr.startswith("!="):
            return str(v).strip() != expr[2:].strip()
        return False

    # priority: fail > warning > ok > inspect
    for level in ("fail", "warning", "ok"):
        if level not in thresholds:
            continue
        expr = thresholds[level]
        if not isinstance(expr, str):
            continue
        # numeric form
        num = _try_num(expr)
        if num and _check(num[0], value, num[1]):
            return level
        # string / bool
        if _str_match(value, expr):
            return level
    if "inspect" in thresholds:
        return "inspect"
    # value present, threshold has machine expressions but none matched —
    # this is an `ok` if no fail/warn matched and ok-expression is silent,
    # otherwise the rule is mis-defined (no level matched the value).
    if "ok" in thresholds:
        return "ok"
    return "error_no_threshold"


def _format_evidence(ev) -> str:
    """Make a human-readable one-line summary of arbitrary evidence value."""
    if ev is None:
        return ""
    if isinstance(ev, (str, int, float, bool)):
        return str(ev)
    if isinstance(ev, list):
        if not ev:
            return "(empty)"
        # show up to 3 items
        items = []
        for x in ev[:3]:
            if isinstance(x, dict):
                # try common keys
                for k in ("symbol", "phrase", "fact", "name", "kind",
                         "matched_token_or_phrase", "drift", "evidence",
                         "description"):
                    if k in x and x[k]:
                        items.append(f"{x[k]!s}")
                        break
                else:
                    items.append(str(x)[:80])
            else:
                items.append(str(x)[:80])
        more = "" if len(ev) <= 3 else f" (+{len(ev)-3} more)"
        return "; ".join(items) + more
    if isinstance(ev, dict):
        # show first few key→value pairs
        bits = []
        for k, v in list(ev.items())[:5]:
            bits.append(f"{k}={v!s}"[:60])
        return "; ".join(bits)
    return str(ev)[:200]


def apply_rules(entry_dir: pathlib.Path, *, skip_llm: bool = False,
                metric_statuses: dict[str, str] | None = None) -> dict:
    rule_modules = _load_rule_modules()
    findings: list[dict] = []
    by_module: dict[str, dict] = defaultdict(lambda: {"ok": 0, "warning": 0,
                                                       "fail": 0, "inspect": 0,
                                                       "error_no_value": 0,
                                                       "error_no_threshold": 0,
                                                       "rules": 0})
    for mod in rule_modules:
        mod_name = mod.get("module", "(unknown)")
        for rule in mod.get("rules", []):
            if not isinstance(rule, dict):
                continue
            name = rule.get("name", "(unnamed)")
            kind = rule.get("kind", "")
            value_paths = rule.get("value_paths", []) or []
            evidence_paths = rule.get("evidence_paths", []) or []
            thresholds = rule.get("thresholds", {}) or {}
            scope = _classify_scope(name, value_paths)

            # use first value_path that resolves to a file we can read
            value, found = None, False
            value_source = None
            for vp in value_paths:
                value, found = _extract_value(entry_dir, vp, rule_name=name)
                if found:
                    value_source = vp
                    break
            # gather ALL evidence pieces, keyed by the path they came from
            evidence_blocks: list[dict] = []
            for ep in evidence_paths:
                ev, ok = _extract_value(entry_dir, ep, rule_name=name)
                if ok:
                    evidence_blocks.append({
                        "path": ep,
                        "raw": ev,
                        "summary": _format_evidence(ev),
                    })

            # Distinguish: key truly missing (no path resolved) vs key found
            # but value is None (e.g. silver baseline not run yet).
            if not found:
                if skip_llm and _rule_is_llm_gated(name, value_paths, metric_statuses):
                    level = "inspect"
                else:
                    level = "error_no_value"
            elif value is None:
                level = "inspect"  # computed but no auto signal — manual review
            else:
                level = _evaluate_thresholds(value, thresholds, kind)
                if level == "fail" and scope != "span":
                    level = "inspect"
            by_module[mod_name][level] += 1
            by_module[mod_name]["rules"] += 1
            if level in ("warning", "fail", "error_no_value", "error_no_threshold"):
                error_msg = None
                if level == "error_no_value":
                    error_msg = (f"value_paths reference key/path that no "
                                 f"generator emits. Tried: "
                                 f"{[vp[:100] for vp in value_paths]}")
                elif level == "error_no_threshold":
                    error_msg = (f"thresholds has no machine-checkable "
                                 f"expression: {thresholds}")
                findings.append({
                    "module": mod_name,
                    "rule": name,
                    "kind": kind,
                    "level": level,
                    "scope": scope,
                    "value": value,
                    "value_source": value_source,
                    "value_paths_tried": value_paths if level == "error_no_value" else None,
                    "thresholds": thresholds if level == "error_no_threshold" else None,
                    "thresholds_full": thresholds,
                    "error_message": error_msg,
                    "evidence_blocks": evidence_blocks,
                    "evidence_summary": "; ".join(b["summary"]
                                                   for b in evidence_blocks
                                                   if b["summary"])[:500],
                    "what_it_counts": rule.get("what_it_counts"),
                    "how_to_compute": rule.get("how_to_compute"),
                    "bad_value_means": rule.get("bad_value_means"),
                    "repair_target": rule.get("repair_target"),
                    "diagnostic_output_must_include": rule.get("diagnostic_output_must_include"),
                })

    # acceptance gate — only fail/warning influence; error_* are separate.
    n_fail = sum(1 for f in findings if f["level"] == "fail")
    n_warn = sum(1 for f in findings if f["level"] == "warning")
    n_err_no_value = sum(1 for f in findings if f["level"] == "error_no_value")
    n_err_no_thr = sum(1 for f in findings if f["level"] == "error_no_threshold")
    if n_fail > 0:
        gate = "needs_review"
    elif n_warn > 3:
        gate = "needs_review"
    else:
        gate = "accepted"

    return {
        "entry_id": entry_dir.name,
        "by_module": {k: dict(v) for k, v in by_module.items()},
        "findings": findings,
        "n_findings": len(findings),
        "n_fail": n_fail,
        "n_warning": n_warn,
        "n_error_no_value": n_err_no_value,
        "n_error_no_threshold": n_err_no_thr,
        "gate": gate,
    }


def write_per_entry_markdown(entry_dir: pathlib.Path, result: dict) -> pathlib.Path:
    """Write a human-readable per-entry diagnostic report with full evidence."""
    lines: list[str] = []
    lines.append(f"# Diagnostic report — {result['entry_id']}")
    lines.append("")
    lines.append(f"- **gate**: `{result['gate']}`")
    lines.append(f"- fail: {result['n_fail']}, warning: {result['n_warning']}")
    lines.append("")
    if not result["findings"]:
        lines.append("_No alarms — all rules pass or non-applicable._")
    for f in sorted(result["findings"],
                    key=lambda x: (x["level"] != "fail",
                                   x["level"] != "warning",
                                   x["module"], x["rule"])):
        lines.append(f"## [{f['level'].upper()}] `{f['module']}` / `{f['rule']}`")
        lines.append("")
        lines.append(f"- value: **{f['value']}**  (from `{f.get('value_source','?')}`)")
        if f.get("bad_value_means"):
            lines.append(f"- meaning: {f['bad_value_means']}")
        if f.get("repair_target"):
            lines.append(f"- repair: {f['repair_target']}")
        if f.get("evidence_blocks"):
            lines.append("- evidence:")
            for b in f["evidence_blocks"]:
                summ = b.get("summary") or ""
                lines.append(f"  - `{b['path']}` → {summ}")
        lines.append("")
    out_p = entry_dir / "diagnostic_suite_v1.md"
    out_p.write_text("\n".join(lines), encoding="utf-8")
    return out_p


def diagnose_entry(entry_dir: pathlib.Path, skip_llm: bool = False,
                   verbose: bool = False) -> dict:
    if verbose:
        print(f"=== {entry_dir.name} ===")
    statuses = ensure_metrics(entry_dir, skip_llm=skip_llm, verbose=verbose)
    rules_eval = apply_rules(entry_dir, skip_llm=skip_llm, metric_statuses=statuses)
    rules_eval["metric_module_statuses"] = statuses
    out_p = entry_dir / "diagnostic_suite_v1.json"
    out_p.write_text(json.dumps(rules_eval, indent=2, ensure_ascii=False, default=str)
                     + "\n", encoding="utf-8")
    write_per_entry_markdown(entry_dir, rules_eval)
    if verbose:
        print(f"  gate={rules_eval['gate']}  fail={rules_eval['n_fail']}  "
              f"warn={rules_eval['n_warning']}  findings={rules_eval['n_findings']}")
    return rules_eval


def diagnose_corpus(run_root: pathlib.Path, skip_llm: bool = False,
                    verbose: bool = False) -> dict:
    entries: list[dict] = []
    for d in sorted(run_root.rglob("main_ir.a4v3")):
        entry_dir = d.parent
        if entry_dir.name.startswith("_"):
            continue
        entries.append(diagnose_entry(entry_dir, skip_llm=skip_llm, verbose=verbose))

    gate_counts = Counter(e["gate"] for e in entries)
    rule_findings: Counter = Counter()
    for e in entries:
        for f in e["findings"]:
            rule_findings[f"{f['module']}::{f['rule']}"] += 1

    summary = {
        "run": run_root.name,
        "n_entries": len(entries),
        "gate_distribution": dict(gate_counts),
        "top_findings": rule_findings.most_common(20),
        "entries": entries,
    }
    out_json = run_root / "diagnostic_suite_corpus_report_v1.json"
    out_json.write_text(json.dumps(summary, indent=2, ensure_ascii=False, default=str)
                        + "\n", encoding="utf-8")

    md = [f"# Diagnostic suite — {run_root.name}", ""]
    md.append(f"- entries: {len(entries)}")
    md.append(f"- gate: {dict(gate_counts)}")
    md.append("")
    md.append("## Top findings (by rule)")
    md.append("| rule | count |")
    md.append("|---|---:|")
    for r, c in rule_findings.most_common(20):
        md.append(f"| `{r}` | {c} |")
    md.append("")
    md.append("## Per-entry summary")
    md.append("| entry | gate | fail | warning | findings |")
    md.append("|---|---|---:|---:|---:|")
    for e in sorted(entries, key=lambda x: (x["gate"] != "accepted",
                                            -x["n_fail"], -x["n_warning"],
                                            x["entry_id"])):
        md.append(f"| `{e['entry_id']}` | {e['gate']} | {e['n_fail']} | "
                  f"{e['n_warning']} | {e['n_findings']} |")
    out_md = run_root / "diagnostic_suite_corpus_report_v1.md"
    out_md.write_text("\n".join(md), encoding="utf-8")

    return summary


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("target", help="entry dir or run root")
    ap.add_argument("--skip-llm", action="store_true",
                    help="don't run B2/B3/B5/A — only det metrics")
    ap.add_argument("--verbose", "-v", action="store_true")
    args = ap.parse_args()

    target = pathlib.Path(args.target)
    if (target / "main_ir.a4v3").exists():
        result = diagnose_entry(target, skip_llm=args.skip_llm, verbose=True)
        print(json.dumps({"gate": result["gate"], "n_fail": result["n_fail"],
                          "n_warning": result["n_warning"],
                          "by_module": result["by_module"]},
                         indent=2, ensure_ascii=False))
    else:
        summary = diagnose_corpus(target, skip_llm=args.skip_llm, verbose=args.verbose)
        print(f"\nWrote {target / 'diagnostic_suite_corpus_report_v1.md'}")
        print(f"  gate distribution: {summary['gate_distribution']}")
        print(f"  top findings: {summary['top_findings'][:5]}")


if __name__ == "__main__":
    main()
