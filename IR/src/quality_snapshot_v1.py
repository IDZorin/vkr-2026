"""quality_snapshot_v1.py

Build a compact, waiver-aware quality snapshot for one local IR entry.

This does not replace diagnostic_suite_v1.json. The diagnostic suite is a raw
rule dump and intentionally noisy. This snapshot separates blocking hard checks
from legacy/advisory signals so manual financial methodology workspaces can be reviewed cleanly.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import sys
from datetime import datetime
from typing import Any

sys.path.insert(0, str(pathlib.Path(__file__).parent))
try:
    import extended_grounding_check_v1 as extended_grounding
except Exception:  # pragma: no cover - snapshot still works without extension.
    extended_grounding = None
try:
    import token_provenance_v1 as token_provenance
except Exception:  # pragma: no cover - phrase waiver fallback stays literal.
    token_provenance = None


def _load_json(path: pathlib.Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return {"_load_error": str(exc)}


def _get(data: dict[str, Any], *path: str, default: Any = None) -> Any:
    cur: Any = data
    for part in path:
        if not isinstance(cur, dict) or part not in cur:
            return default
        cur = cur[part]
    return cur


def _token_waiver_status(entry_dir: pathlib.Path, token_metrics: dict[str, Any]) -> dict[str, Any]:
    waiver = _load_json(entry_dir / "waiver_token_absorption_v1.json")
    uncovered = token_metrics.get("uncovered_tokens") or []
    uncovered_tokens = {item.get("token") for item in uncovered if item.get("token")}
    items = waiver.get("items") or []
    approved_tokens = {
        item.get("token")
        for item in items
        if item.get("token") and item.get("reviewer") == "human_approved"
    }
    missing = sorted(t for t in uncovered_tokens if t not in approved_tokens)
    extra = sorted(t for t in approved_tokens if t not in uncovered_tokens)
    direct = int(_get(token_metrics, "summary", "covered_content_token_count", default=0) or 0)
    total = int(_get(token_metrics, "summary", "content_token_count", default=0) or 0)
    accounted = min(total, direct + len(uncovered_tokens & approved_tokens))
    return {
        "waiver_file_present": bool(waiver),
        "uncovered_token_count": len(uncovered_tokens),
        "human_approved_waiver_count": len(uncovered_tokens & approved_tokens),
        "approved_uncovered_tokens": sorted(uncovered_tokens & approved_tokens),
        "unapproved_uncovered_tokens": missing,
        "approved_tokens_not_currently_uncovered": extra,
        "waiver_accounted_content_token_count": accounted,
        "waiver_accounted_content_coverage_rate": round(accounted / total, 3) if total else None,
        "all_uncovered_tokens_have_human_waiver": not missing,
    }


def _phrase_waiver_status(phrase_metrics: dict[str, Any], token_status: dict[str, Any]) -> dict[str, Any]:
    uncovered = phrase_metrics.get("uncovered") or []
    approved_tokens = set(token_status.get("approved_uncovered_tokens") or [])
    waived_phrases = []
    unwaived_phrases = []
    for item in uncovered:
        token_groups: list[set[str]] = []
        phrase = str(item.get("phrase") or "")
        if token_provenance is not None and phrase:
            for source_token in token_provenance._source_tokens(phrase):
                if source_token.get("is_stopword"):
                    continue
                keys = set(source_token.get("keys") or [])
                if source_token.get("token"):
                    keys.add(str(source_token["token"]))
                if keys:
                    token_groups.append(keys)
        if not token_groups:
            for token in item.get("tokens", []):
                if not token:
                    continue
                raw_token = str(token)
                keys = {raw_token}
                if token_provenance is not None:
                    keys.update(token_provenance._token_keys(raw_token))
                token_groups.append(keys)
        if token_groups and all(group & approved_tokens for group in token_groups):
            waived_phrases.append(item)
        else:
            unwaived_phrases.append(item)
    phrase_count = phrase_metrics.get("phrase_count")
    covered_count = phrase_metrics.get("covered_count") or 0
    effective_covered_count = covered_count + len(waived_phrases)
    return {
        "uncovered_phrase_count": len(uncovered),
        "waived_uncovered_phrase_count": len(waived_phrases),
        "unwaived_uncovered_phrase_count": len(unwaived_phrases),
        "waived_uncovered_phrases": [item.get("phrase") for item in waived_phrases],
        "unwaived_uncovered_phrases": [item.get("phrase") for item in unwaived_phrases],
        "effective_covered_count": effective_covered_count,
        "effective_coverage_rate": round(effective_covered_count / phrase_count, 3) if phrase_count else None,
        "all_uncovered_phrases_have_token_waiver": not unwaived_phrases,
    }


def _exact_url_status(token_metrics: dict[str, Any]) -> dict[str, Any]:
    url_provenance = token_metrics.get("url_provenance") or {}
    summary = url_provenance.get("summary") or {}
    missing_urls = [
        item.get("url")
        for item in (url_provenance.get("missing_urls") or [])
        if item.get("url")
    ]
    return {
        "source_url_count": summary.get("source_url_count", 0),
        "covered_url_count": summary.get("covered_url_count", 0),
        "missing_url_count": summary.get("missing_url_count", 0),
        "url_coverage_rate": summary.get("url_coverage_rate"),
        "missing_urls": missing_urls,
        "all_source_urls_preserved_exactly": not missing_urls,
    }


def _diagnostic_fail_status(entry_dir: pathlib.Path, token_status: dict[str, Any]) -> dict[str, Any]:
    diag = _load_json(entry_dir / "diagnostic_suite_v1.json")
    findings = diag.get("findings") or []
    raw_fails = [f for f in findings if f.get("level") == "fail" or f.get("severity") == "fail"]
    waived_legacy = []
    render_nli_advisory = []
    source_normalization_nli_advisory = []
    blocking = []
    lexical_rules = {
        "content_token_jaccard",
        "content_token_multiset_recall",
        "content_token_multiset_precision",
        "content_token_recall",
        "formula_content_token_recall",
        "full_surface_content_token_recall",
    }
    render_rules = {
        "render_nli_ir_implies_text",
        "render_nli_text_implies_ir",
        "render_nli_ir_implies_source",
        "render_nli_source_implies_ir",
        "render_contradiction_score",
    }
    source_normalization_nli_rules = {
        "source_implies_normalized_entailment",
        "normalized_implies_source_entailment",
    }
    waiver_ok = bool(token_status.get("all_uncovered_tokens_have_human_waiver"))
    source_text = _read_file(entry_dir / "source.md")
    normalized_text = _read_file(entry_dir / "normalized.md")
    source_equals_normalized = bool(source_text and source_text == normalized_text)
    for f in raw_fails:
        rule = f.get("rule")
        if waiver_ok and rule in lexical_rules:
            waived_legacy.append(f)
        elif rule in render_rules:
            render_nli_advisory.append(f)
        elif source_equals_normalized and rule in source_normalization_nli_rules:
            source_normalization_nli_advisory.append(f)
        else:
            blocking.append(f)
    return {
        "raw_gate": diag.get("gate"),
        "raw_fail_count": len(raw_fails),
        "raw_warning_count": diag.get("n_warning"),
        "waiver_adjusted_legacy_lexical_fail_count": len(waived_legacy),
        "render_nli_advisory_fail_count": len(render_nli_advisory),
        "source_normalization_nli_advisory_fail_count": len(source_normalization_nli_advisory),
        "blocking_fail_count": len(blocking),
        "blocking_fail_rules": [
            {
                "module": f.get("module"),
                "rule": f.get("rule"),
                "value": f.get("value"),
            }
            for f in blocking
        ],
    }


def _read_file(path: pathlib.Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="replace").strip()


CANONICAL_FILE_SPECS = [
    {"key": "source", "path": "source.md", "required": True},
    {"key": "normalized", "path": "normalized.md", "required": True},
    {"key": "main_ir", "path": "main_ir.a4v3", "required": True},
    {"key": "repair", "path": "repair.a4v3", "required": False},
    {"key": "provenance", "path": "provenance.yaml", "required": True},
    {"key": "translator_notes", "path": "translator_notes.md", "required": False},
    {"key": "token_waiver", "path": "waiver_token_absorption_v1.json", "required": False},
]

ARTIFACT_SPECS = [
    {
        "key": "main_metrics",
        "pattern": "main_ir_metrics_v1.json",
        "required": True,
        "inputs": ["source", "normalized", "main_ir"],
    },
    {
        "key": "family_coverage",
        "pattern": "metrics_family_coverage_v1.json",
        "required": True,
        "inputs": ["source", "normalized", "main_ir"],
    },
    {
        "key": "source_phrase_coverage",
        "pattern": "metrics_source_phrase_coverage_v1.json",
        "required": True,
        "inputs": ["source", "main_ir"],
    },
    {
        "key": "token_provenance",
        "pattern": "metrics_token_provenance_v1.json",
        "required": True,
        "inputs": ["source", "main_ir"],
    },
    {
        "key": "lowering_audit",
        "pattern": "lowering_audit_v1.json",
        "required": True,
        "inputs": ["main_ir"],
    },
    {
        "key": "semantic_lint",
        "pattern": "a4v3_semantic_lint_v1.json",
        "required": True,
        "inputs": ["source", "normalized", "main_ir", "repair", "translator_notes"],
    },
    {
        "key": "provenance_lint",
        "pattern": "provenance_lint_v1.json",
        "required": True,
        "inputs": ["provenance", "main_ir"],
    },
    {
        "key": "diagnostic_suite",
        "pattern": "diagnostic_suite_v1.json",
        "required": True,
        "inputs": ["source", "normalized", "main_ir", "repair", "token_waiver"],
    },
    {
        "key": "single_semantic_judge",
        "pattern": "*_llm_semantic_verdict_*.json",
        "required": False,
        "inputs": ["source", "normalized", "main_ir"],
    },
    {
        "key": "multi_judge",
        "pattern": "metrics_multi_judge_consensus_v1.json",
        "required": False,
        "inputs": ["source", "main_ir"],
    },
    {
        "key": "counterexample_probing",
        "pattern": "metrics_counterexample_probing_v1.json",
        "required": False,
        "inputs": ["source", "main_ir"],
    },
]


def _sha256_file(path: pathlib.Path) -> str | None:
    if not path.exists():
        return None
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def _file_fingerprint(path: pathlib.Path) -> dict[str, Any]:
    if not path.exists():
        return {"exists": False}
    stat = path.stat()
    return {
        "exists": True,
        "size": stat.st_size,
        "mtime": datetime.fromtimestamp(stat.st_mtime).isoformat(timespec="seconds"),
        "mtime_epoch": stat.st_mtime,
        "sha256": _sha256_file(path),
    }


def _entry_hash(files: dict[str, dict[str, Any]]) -> str:
    h = hashlib.sha256()
    for key in sorted(files):
        info = files[key]
        if not info.get("exists"):
            continue
        h.update(key.encode("utf-8"))
        h.update(b"\0")
        h.update(str(info.get("sha256") or "").encode("utf-8"))
        h.update(b"\n")
    return h.hexdigest()


def _artifact_consistency(entry_dir: pathlib.Path) -> dict[str, Any]:
    canonical: dict[str, dict[str, Any]] = {}
    required_canonical_missing = 0
    for spec in CANONICAL_FILE_SPECS:
        info = _file_fingerprint(entry_dir / str(spec["path"]))
        info["path"] = str(spec["path"])
        info["required"] = bool(spec["required"])
        if spec["required"] and not info.get("exists"):
            required_canonical_missing += 1
        canonical[str(spec["key"])] = info

    artifacts: list[dict[str, Any]] = []
    required_stale = 0
    required_missing = required_canonical_missing
    advisory_stale = 0
    advisory_missing = 0

    for spec in ARTIFACT_SPECS:
        key = str(spec["key"])
        required = bool(spec["required"])
        inputs = [str(item) for item in (spec.get("inputs") or [])]
        input_infos = [
            canonical[item]
            for item in inputs
            if item in canonical and canonical[item].get("exists")
        ]
        max_input_mtime = max((float(info.get("mtime_epoch") or 0.0) for info in input_infos), default=0.0)
        matches = sorted(entry_dir.glob(str(spec["pattern"])))
        if not matches:
            if required:
                required_missing += 1
            else:
                advisory_missing += 1
            artifacts.append({
                "key": key,
                "pattern": spec["pattern"],
                "required": required,
                "status": "missing",
                "inputs": inputs,
            })
            continue
        for path in matches:
            info = _file_fingerprint(path)
            stale = bool(max_input_mtime and float(info.get("mtime_epoch") or 0.0) + 1e-6 < max_input_mtime)
            status = "stale" if stale else "current"
            if stale and required:
                required_stale += 1
            elif stale:
                advisory_stale += 1
            artifacts.append({
                "key": key,
                "path": path.name,
                "required": required,
                "status": status,
                "inputs": inputs,
                "mtime": info.get("mtime"),
                "sha256": info.get("sha256"),
                "max_input_mtime": (
                    datetime.fromtimestamp(max_input_mtime).isoformat(timespec="seconds")
                    if max_input_mtime
                    else None
                ),
            })

    status = "ok"
    if required_missing:
        status = "missing_required_artifacts"
    elif required_stale:
        status = "stale_required_artifacts"
    elif advisory_missing or advisory_stale:
        status = "advisory_artifact_drift"

    return {
        "schema": "artifact_consistency_v1",
        "status": status,
        "canonical_entry_sha256": _entry_hash(canonical),
        "canonical_files": {
            key: {
                k: v
                for k, v in info.items()
                if k not in {"mtime_epoch"}
            }
            for key, info in canonical.items()
        },
        "required_stale_count": required_stale,
        "required_missing_count": required_missing,
        "required_canonical_missing_count": required_canonical_missing,
        "advisory_stale_count": advisory_stale,
        "advisory_missing_count": advisory_missing,
        "artifacts": artifacts,
    }


def build_snapshot(entry_dir: pathlib.Path) -> dict[str, Any]:
    metrics = _load_json(entry_dir / "main_ir_metrics_v1.json")
    family = _load_json(entry_dir / "metrics_family_coverage_v1.json")
    phrases = _load_json(entry_dir / "metrics_source_phrase_coverage_v1.json")
    tokens = _load_json(entry_dir / "metrics_token_provenance_v1.json")
    lowering = _load_json(entry_dir / "lowering_audit_v1.json")
    semantic_lint = _load_json(entry_dir / "a4v3_semantic_lint_v1.json")
    provenance_lint = _load_json(entry_dir / "provenance_lint_v1.json")
    token_status = _token_waiver_status(entry_dir, tokens)
    phrase_waiver_status = _phrase_waiver_status(phrases, token_status)
    exact_url_status = _exact_url_status(tokens)
    diagnostic_status = _diagnostic_fail_status(entry_dir, token_status)
    artifact_consistency = _artifact_consistency(entry_dir)

    validity = {
        "ast_valid": _get(metrics, "validity", "ast_valid"),
        "ast_error_count": _get(metrics, "validity", "ast_error_count"),
        "rendering_ok": _get(metrics, "validity", "rendering_ok"),
        "combined_validation_ok": _get(metrics, "validity", "combined_validation_ok"),
    }
    grounding_raw = {
        "ungrounded_symbol_count": _get(metrics, "grounding", "ungrounded_symbol_count"),
        "ungrounded_sort_count": _get(metrics, "grounding", "ungrounded_sort_count"),
        "ungrounded_ref_count": _get(metrics, "grounding", "ungrounded_ref_count"),
        "ungrounded_callee_count": _get(metrics, "grounding", "ungrounded_callee_count"),
        "origin_error_count": _get(metrics, "grounding", "origin_error_count"),
    }
    grounding_extended = {}
    if extended_grounding is not None:
        try:
            grounding_extended = extended_grounding.check_entry(entry_dir)
        except Exception as exc:
            grounding_extended = {"_load_error": str(exc)}
    grounding = {
        "raw": grounding_raw,
        "extended": grounding_extended,
        "effective_ungrounded_symbol_count": grounding_extended.get(
            "ungrounded_symbol_count_extended",
            grounding_raw.get("ungrounded_symbol_count"),
        ),
        "effective_ungrounded_sort_count": grounding_extended.get(
            "ungrounded_sort_count_extended",
            grounding_raw.get("ungrounded_sort_count"),
        ),
        "effective_ungrounded_callee_count": grounding_extended.get(
            "ungrounded_callee_count_extended",
            grounding_raw.get("ungrounded_callee_count"),
        ),
    }
    family_status = {
        "required_gap_count": family.get("n_required_gaps"),
        "advisory_gap_count": family.get("n_advisory_gaps"),
        "required_gaps": family.get("required_gaps") or [],
        "advisory_gaps": family.get("advisory_gaps") or [],
    }
    phrase_status = {
        "phrase_count": phrases.get("phrase_count"),
        "covered_count": phrases.get("covered_count"),
        "uncovered_count": phrases.get("uncovered_count"),
        "coverage_rate": phrases.get("coverage_rate"),
        "waiver_status": phrase_waiver_status,
    }
    lowering_status = {
        "smell_count": lowering.get("n_smells"),
        "smells": lowering.get("smells") or [],
    }
    semantic_lint_status = semantic_lint.get("summary") or {}
    provenance_lint_status = provenance_lint.get("summary") or {}

    blocking_conditions = []
    if validity.get("ast_valid") != 1 or validity.get("combined_validation_ok") != 1:
        blocking_conditions.append("invalid_ast_or_combined_validation")
    if any((grounding.get(k) or 0) != 0 for k in (
        "effective_ungrounded_symbol_count",
        "effective_ungrounded_sort_count",
        "effective_ungrounded_callee_count",
    )):
        blocking_conditions.append("ungrounded_or_origin_errors")
    if (family_status.get("required_gap_count") or 0) != 0:
        blocking_conditions.append("required_family_gaps")
    if not phrase_waiver_status.get("all_uncovered_phrases_have_token_waiver"):
        blocking_conditions.append("uncovered_source_phrases")
    if not token_status.get("all_uncovered_tokens_have_human_waiver"):
        blocking_conditions.append("unapproved_token_waivers")
    if not exact_url_status.get("all_source_urls_preserved_exactly"):
        blocking_conditions.append("missing_exact_source_urls")
    # Lowering audit is intentionally advisory. These smells are useful repair
    # suggestions (for example, "must" in a constraint name), but they are not
    # hard evidence that the IR is invalid or semantically wrong.
    if diagnostic_status.get("blocking_fail_count") != 0:
        blocking_conditions.append("blocking_diagnostic_fails")
    if artifact_consistency.get("required_missing_count"):
        blocking_conditions.append("missing_required_artifacts")
    if artifact_consistency.get("required_stale_count"):
        blocking_conditions.append("stale_required_artifacts")
    if (provenance_lint_status.get("strong_findings") or 0) != 0:
        blocking_conditions.append("strong_provenance_lint_findings")

    clean_gate = "accepted" if not blocking_conditions else "needs_review"
    return {
        "entry_id": entry_dir.name,
        "schema": "quality_snapshot_v1",
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "clean_gate": clean_gate,
        "blocking_conditions": blocking_conditions,
        "validity": validity,
        "grounding": grounding,
        "family_coverage": family_status,
        "source_phrase_coverage": phrase_status,
        "token_provenance": {
            "summary": tokens.get("summary") or {},
            "waiver_status": token_status,
            "exact_url_status": exact_url_status,
        },
        "lowering_audit": lowering_status,
        "a4v3_semantic_lint": semantic_lint_status,
        "provenance_lint": provenance_lint_status,
        "artifact_consistency": artifact_consistency,
        "diagnostic_suite_raw": diagnostic_status,
        "notes": [
            "clean_gate ignores legacy lexical failures when every uncovered token has a human-approved waiver.",
            "render NLI failures are kept as advisory because they evaluate deterministic render-back text, not A4V3 validity.",
            "raw diagnostic_suite_v1.json is preserved unchanged for auditability.",
        ],
    }


def write_snapshot(entry_dir: pathlib.Path) -> pathlib.Path:
    snapshot = build_snapshot(entry_dir)
    out_json = entry_dir / "quality_snapshot_v1.json"
    out_md = entry_dir / "quality_snapshot_v1.md"
    out_json.write_text(json.dumps(snapshot, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    token_summary = snapshot["token_provenance"]["summary"]
    waiver = snapshot["token_provenance"]["waiver_status"]
    exact_urls = snapshot["token_provenance"]["exact_url_status"]
    diag = snapshot["diagnostic_suite_raw"]
    semantic_lint = snapshot.get("a4v3_semantic_lint") or {}
    provenance_lint = snapshot.get("provenance_lint") or {}
    artifacts = snapshot.get("artifact_consistency") or {}
    lines = [
        f"# Quality Snapshot: {snapshot['entry_id']}",
        "",
        f"- clean_gate: `{snapshot['clean_gate']}`",
        f"- blocking_conditions: `{', '.join(snapshot['blocking_conditions']) if snapshot['blocking_conditions'] else 'none'}`",
        f"- ast_valid / combined_validation_ok: `{snapshot['validity']['ast_valid']}` / `{snapshot['validity']['combined_validation_ok']}`",
        f"- effective grounding counts: symbols `{snapshot['grounding']['effective_ungrounded_symbol_count']}`, sorts `{snapshot['grounding']['effective_ungrounded_sort_count']}`, callees `{snapshot['grounding']['effective_ungrounded_callee_count']}`",
        f"- raw legacy grounding counts: symbols `{snapshot['grounding']['raw']['ungrounded_symbol_count']}`, sorts `{snapshot['grounding']['raw']['ungrounded_sort_count']}`, refs `{snapshot['grounding']['raw']['ungrounded_ref_count']}`, callees `{snapshot['grounding']['raw']['ungrounded_callee_count']}`, origin `{snapshot['grounding']['raw']['origin_error_count']}`",
        f"- required/advisory family gaps: `{snapshot['family_coverage']['required_gap_count']}` / `{snapshot['family_coverage']['advisory_gap_count']}`",
        f"- source phrase coverage: `{snapshot['source_phrase_coverage']['covered_count']}/{snapshot['source_phrase_coverage']['phrase_count']}` (`{snapshot['source_phrase_coverage']['coverage_rate']}`)",
        f"- source phrase waiver-adjusted coverage: `{snapshot['source_phrase_coverage']['waiver_status']['effective_covered_count']}/{snapshot['source_phrase_coverage']['phrase_count']}` (`{snapshot['source_phrase_coverage']['waiver_status']['effective_coverage_rate']}`)",
        f"- token direct coverage: `{token_summary.get('covered_content_token_count')}/{token_summary.get('content_token_count')}` (`{token_summary.get('content_coverage_rate')}`)",
        f"- token waiver-accounted coverage: `{waiver['waiver_accounted_content_token_count']}/{token_summary.get('content_token_count')}` (`{waiver['waiver_accounted_content_coverage_rate']}`)",
        f"- human-approved token waivers: `{waiver['human_approved_waiver_count']}/{waiver['uncovered_token_count']}`",
        f"- exact URL preservation: `{exact_urls['covered_url_count']}/{exact_urls['source_url_count']}` (`{exact_urls['url_coverage_rate']}`)",
        f"- lowering smells: `{snapshot['lowering_audit']['smell_count']}`",
        f"- a4v3 semantic lint findings: `{semantic_lint.get('total_findings', 0)}` "
        f"(strong `{semantic_lint.get('strong_findings', 0)}`, soft `{semantic_lint.get('soft_findings', 0)}`, "
        f"style `{semantic_lint.get('style_findings', 0)}`, "
        f"advisory `{semantic_lint.get('advisory_findings', 0)}`)",
        f"- provenance lint findings: `{provenance_lint.get('total_findings', 0)}` "
        f"(strong `{provenance_lint.get('strong_findings', 0)}`, "
        f"soft `{provenance_lint.get('soft_findings', 0)}`, "
        f"advisory `{provenance_lint.get('advisory_findings', 0)}`)",
        f"- artifact consistency: `{artifacts.get('status')}` "
        f"(required stale `{artifacts.get('required_stale_count')}`, "
        f"required missing `{artifacts.get('required_missing_count')}`, "
        f"advisory stale `{artifacts.get('advisory_stale_count')}`)",
        f"- raw diagnostic gate/fails/warnings: `{diag['raw_gate']}` / `{diag['raw_fail_count']}` / `{diag['raw_warning_count']}`",
        f"- blocking diagnostic fails after clean categorization: `{diag['blocking_fail_count']}`",
        "",
        "## Nonblocking Raw Alarms",
        "",
        f"- waiver-adjusted legacy lexical fails: `{diag['waiver_adjusted_legacy_lexical_fail_count']}`",
        f"- render-NLI advisory fails: `{diag['render_nli_advisory_fail_count']}`",
        f"- source-normalization NLI advisory fails: `{diag['source_normalization_nli_advisory_fail_count']}`",
    ]
    out_md.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return out_json


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("entries", nargs="+", help="entry directories")
    args = ap.parse_args()
    for raw in args.entries:
        entry = pathlib.Path(raw)
        out = write_snapshot(entry)
        snap = json.loads(out.read_text(encoding="utf-8"))
        print(f"{entry}: clean_gate={snap['clean_gate']} -> {out}")


if __name__ == "__main__":
    main()
