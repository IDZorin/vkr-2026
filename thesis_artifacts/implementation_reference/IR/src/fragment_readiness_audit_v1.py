"""fragment_readiness_audit_v1.py

Deterministic corpus-level readiness audit for local seed methodology fragments.

The audit reads existing per-entry reports, reparses each local
``main_ir.a4v3`` with the canonical parser, and emits a single corpus report.
It does not rewrite fragment files and does not rerun heavyweight LLM/embedding
checks.

CLI:
    python IR/src/fragment_readiness_audit_v1.py --run-root case_studies/financial_methodology
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

THIS_DIR = Path(__file__).resolve().parent
if str(THIS_DIR) not in sys.path:
    sys.path.insert(0, str(THIS_DIR))

from a4v3_parser_v1 import parse  # noqa: E402


ENTRY_GROUPS = (
    ("sections", "section"),
    ("definitions", "definition"),
    ("appendix", "appendix"),
)

MANDATORY_ARTIFACTS = (
    "source.md",
    "main_ir.a4v3",
    "provenance.yaml",
    "role_annotations.yaml",
    "entry_checks_v1.json",
)

OPTIONAL_REVIEW_ARTIFACTS = (
    "translator_notes.md",
    "waiver_token_absorption_v1.json",
)

REPORT_FILES = (
    "entry_checks_v1.json",
    "quality_snapshot_v1.json",
    "a4v3_semantic_lint_v1.json",
    "metrics_token_provenance_v1.json",
    "metrics_family_coverage_v1.json",
    "metrics_source_phrase_coverage_v1.json",
    "lowering_audit_v1.json",
    "provenance_lint_v1.json",
    "provenance_backtranslation_metrics_v1.json",
    "role_annotation_lint_v1.json",
    "diagnostic_suite_v1.json",
)

FRESHNESS_INPUTS = (
    "source.md",
    "main_ir.a4v3",
    "provenance.yaml",
    "role_annotations.yaml",
)

REPORT_FRESHNESS_INPUTS = {
    "entry_checks_v1.json": FRESHNESS_INPUTS,
    "quality_snapshot_v1.json": FRESHNESS_INPUTS,
    "a4v3_semantic_lint_v1.json": ("main_ir.a4v3", "translator_notes.md", "provenance.yaml"),
    "metrics_token_provenance_v1.json": ("source.md", "provenance.yaml", "waiver_token_absorption_v1.json"),
    "metrics_family_coverage_v1.json": ("source.md", "main_ir.a4v3"),
    "metrics_source_phrase_coverage_v1.json": ("source.md", "main_ir.a4v3", "provenance.yaml"),
    "lowering_audit_v1.json": ("main_ir.a4v3",),
    "provenance_lint_v1.json": ("main_ir.a4v3", "provenance.yaml"),
    "provenance_backtranslation_metrics_v1.json": ("source.md", "provenance.yaml"),
    "role_annotation_lint_v1.json": ("main_ir.a4v3", "role_annotations.yaml"),
    "diagnostic_suite_v1.json": ("source.md", "main_ir.a4v3", "provenance.yaml"),
}


def _read_json(path: Path) -> tuple[dict[str, Any] | None, str | None]:
    try:
        return json.loads(path.read_text(encoding="utf-8")), None
    except Exception as exc:  # noqa: BLE001 - report malformed artifacts.
        return None, str(exc)


def _finding(
    code: str,
    severity: str,
    message: str,
    *,
    entry_id: str | None = None,
    entry_kind: str | None = None,
    file: str | None = None,
    data: dict[str, Any] | None = None,
) -> dict[str, Any]:
    item: dict[str, Any] = {
        "code": code,
        "severity": severity,
        "message": message,
    }
    if entry_id:
        item["entry_id"] = entry_id
    if entry_kind:
        item["entry_kind"] = entry_kind
    if file:
        item["file"] = file
    if data:
        item["data"] = data
    return item


def _discover_entries(run_root: Path) -> list[dict[str, Any]]:
    entries: list[dict[str, Any]] = []
    for group_dir_name, entry_kind in ENTRY_GROUPS:
        group_dir = run_root / group_dir_name
        if not group_dir.exists():
            continue
        for entry_dir in sorted(group_dir.iterdir(), key=lambda p: p.name.lower()):
            if not entry_dir.is_dir():
                continue
            if entry_dir.name.startswith("agent_run"):
                continue
            entries.append(
                {
                    "entry_id": entry_dir.name,
                    "entry_kind": entry_kind,
                    "entry_dir": entry_dir,
                    "relative_dir": str(entry_dir.relative_to(run_root)),
                }
            )
    return entries


def _mtime(path: Path) -> float | None:
    if not path.exists():
        return None
    return path.stat().st_mtime


def _is_stale(report_path: Path, input_paths: list[Path]) -> bool:
    report_time = _mtime(report_path)
    if report_time is None:
        return False
    return any((_mtime(path) or 0) > report_time for path in input_paths if path.exists())


def _summary_counts(summary: dict[str, Any] | None) -> dict[str, int]:
    summary = summary or {}
    return {
        "total": int(summary.get("total_findings", summary.get("total", 0)) or 0),
        "strong": int(summary.get("strong_findings", summary.get("strong", 0)) or 0),
        "soft": int(summary.get("soft_findings", summary.get("soft", 0)) or 0),
        "advisory": int(summary.get("advisory_findings", summary.get("advisory", 0)) or 0),
    }


def _semantic_summary(data: dict[str, Any] | None) -> dict[str, int]:
    if not data:
        return {"total": 0, "strong": 0, "soft": 0, "style": 0, "advisory": 0}
    summary = data.get("summary") or {}
    by_severity = data.get("by_severity") or {}
    return {
        "total": int(summary.get("total", len(data.get("findings", []))) or 0),
        "strong": int(summary.get("strong", by_severity.get("strong", 0)) or 0),
        "soft": int(summary.get("soft", by_severity.get("soft", 0)) or 0),
        "style": int(summary.get("style", by_severity.get("style", 0)) or 0),
        "advisory": int(summary.get("advisory", by_severity.get("advisory", 0)) or 0),
    }


def _quality_snapshot(data: dict[str, Any] | None) -> dict[str, Any]:
    if not data:
        return {
            "clean_gate": "missing",
            "blocking_conditions": [],
            "missing_required_artifacts": None,
            "required_stale_artifacts": None,
        }
    artifact = data.get("artifact_consistency") or {}
    return {
        "clean_gate": data.get("clean_gate"),
        "blocking_conditions": data.get("blocking_conditions") or [],
        "missing_required_artifacts": artifact.get("missing_required_artifacts"),
        "required_stale_artifacts": artifact.get("required_stale_artifacts"),
    }


def _analyze_entry(entry: dict[str, Any]) -> dict[str, Any]:
    entry_dir: Path = entry["entry_dir"]
    entry_id = entry["entry_id"]
    entry_kind = entry["entry_kind"]
    findings: list[dict[str, Any]] = []

    artifacts = {name: entry_dir / name for name in MANDATORY_ARTIFACTS}
    for name, path in artifacts.items():
        if not path.exists():
            findings.append(
                _finding(
                    "mandatory_artifact_missing",
                    "hard",
                    f"Mandatory fragment artifact {name} is missing.",
                    entry_id=entry_id,
                    entry_kind=entry_kind,
                    file=name,
                    data={"path": str(path)},
                )
            )
        elif name == "main_ir.a4v3" and path.stat().st_size == 0:
            findings.append(
                _finding(
                    "main_ir_empty",
                    "hard",
                    "main_ir.a4v3 is empty.",
                    entry_id=entry_id,
                    entry_kind=entry_kind,
                    file=name,
                    data={"path": str(path)},
                )
            )

    for name in OPTIONAL_REVIEW_ARTIFACTS:
        path = entry_dir / name
        if not path.exists():
            findings.append(
                _finding(
                    "optional_review_artifact_missing",
                    "advisory",
                    f"Optional review artifact {name} is absent.",
                    entry_id=entry_id,
                    entry_kind=entry_kind,
                    file=name,
                )
            )

    parse_warning_count: int | None = None
    declaration_count: int | None = None
    assertion_count: int | None = None
    main_ir_path = entry_dir / "main_ir.a4v3"
    if main_ir_path.exists() and main_ir_path.stat().st_size > 0:
        try:
            ast = parse(main_ir_path.read_text(encoding="utf-8"), strict=False)
            warnings = ast.get("warnings") or []
            parse_warning_count = len(warnings)
            declaration_count = len(ast.get("declarations") or [])
            assertion_count = len(ast.get("assertions") or [])
            if warnings:
                findings.append(
                    _finding(
                        "main_ir_parse_warnings",
                        "hard",
                        "main_ir.a4v3 has parser warnings.",
                        entry_id=entry_id,
                        entry_kind=entry_kind,
                        file="main_ir.a4v3",
                        data={"warnings": warnings[:20]},
                    )
                )
        except Exception as exc:  # noqa: BLE001 - parse exceptions block readiness.
            findings.append(
                _finding(
                    "main_ir_parse_exception",
                    "hard",
                    "main_ir.a4v3 could not be parsed.",
                    entry_id=entry_id,
                    entry_kind=entry_kind,
                    file="main_ir.a4v3",
                    data={"error": str(exc)},
                )
            )

    reports: dict[str, dict[str, Any] | None] = {}
    report_errors: dict[str, str] = {}
    for report_name in REPORT_FILES:
        report_path = entry_dir / report_name
        if not report_path.exists():
            reports[report_name] = None
            continue
        data, error = _read_json(report_path)
        reports[report_name] = data
        if error:
            report_errors[report_name] = error
            findings.append(
                _finding(
                    "report_json_malformed",
                    "hard",
                    f"Generated report {report_name} is not valid JSON.",
                    entry_id=entry_id,
                    entry_kind=entry_kind,
                    file=report_name,
                    data={"error": error},
                )
            )

    for report_name in REPORT_FILES:
        report_path = entry_dir / report_name
        input_paths = [entry_dir / name for name in REPORT_FRESHNESS_INPUTS.get(report_name, FRESHNESS_INPUTS)]
        if report_path.exists() and _is_stale(report_path, input_paths):
            findings.append(
                _finding(
                    "generated_report_stale",
                    "advisory",
                    f"Generated report {report_name} is older than at least one local source artifact.",
                    entry_id=entry_id,
                    entry_kind=entry_kind,
                    file=report_name,
                )
            )

    entry_checks = reports.get("entry_checks_v1.json") or {}
    if entry_checks:
        if entry_checks.get("overall_status") != "ok":
            findings.append(
                _finding(
                    "entry_checks_not_ok",
                    "hard",
                    "entry_checks_v1 overall_status is not ok.",
                    entry_id=entry_id,
                    entry_kind=entry_kind,
                    file="entry_checks_v1.json",
                    data={
                        "overall_status": entry_checks.get("overall_status"),
                        "failed_step_count": entry_checks.get("failed_step_count"),
                    },
                )
            )
    elif "entry_checks_v1.json" not in report_errors:
        findings.append(
            _finding(
                "entry_checks_missing",
                "hard",
                "entry_checks_v1.json is missing.",
                entry_id=entry_id,
                entry_kind=entry_kind,
                file="entry_checks_v1.json",
            )
        )

    quality = _quality_snapshot(reports.get("quality_snapshot_v1.json"))
    if quality["clean_gate"] == "missing":
        findings.append(
            _finding(
                "quality_snapshot_missing",
                "soft",
                "quality_snapshot_v1.json is missing.",
                entry_id=entry_id,
                entry_kind=entry_kind,
                file="quality_snapshot_v1.json",
            )
        )
    elif quality["clean_gate"] != "accepted":
        severity = "hard" if quality["blocking_conditions"] else "soft"
        findings.append(
            _finding(
                "quality_snapshot_not_accepted",
                severity,
                f"quality_snapshot clean_gate is {quality['clean_gate']!r}.",
                entry_id=entry_id,
                entry_kind=entry_kind,
                file="quality_snapshot_v1.json",
                data=quality,
            )
        )

    provenance_lint = reports.get("provenance_lint_v1.json")
    provenance_counts = _summary_counts((provenance_lint or {}).get("summary") if provenance_lint else None)
    if provenance_lint is None:
        findings.append(
            _finding(
                "provenance_lint_missing",
                "hard",
                "provenance_lint_v1.json is missing.",
                entry_id=entry_id,
                entry_kind=entry_kind,
                file="provenance_lint_v1.json",
            )
        )
    else:
        if provenance_counts["strong"]:
            findings.append(
                _finding(
                    "provenance_lint_strong_findings",
                    "hard",
                    "provenance_lint has strong findings.",
                    entry_id=entry_id,
                    entry_kind=entry_kind,
                    file="provenance_lint_v1.json",
                    data=provenance_counts,
                )
            )
        if provenance_counts["soft"]:
            findings.append(
                _finding(
                    "provenance_lint_soft_findings",
                    "soft",
                    "provenance_lint has soft findings.",
                    entry_id=entry_id,
                    entry_kind=entry_kind,
                    file="provenance_lint_v1.json",
                    data=provenance_counts,
                )
            )

    role_lint = reports.get("role_annotation_lint_v1.json")
    role_counts = _summary_counts((role_lint or {}).get("summary") if role_lint else None)
    if role_lint is None:
        findings.append(
            _finding(
                "role_annotation_lint_missing",
                "hard",
                "role_annotation_lint_v1.json is missing.",
                entry_id=entry_id,
                entry_kind=entry_kind,
                file="role_annotation_lint_v1.json",
            )
        )
    else:
        if role_counts["strong"]:
            findings.append(
                _finding(
                    "role_annotation_lint_strong_findings",
                    "hard",
                    "role_annotation_lint has strong findings.",
                    entry_id=entry_id,
                    entry_kind=entry_kind,
                    file="role_annotation_lint_v1.json",
                    data=role_counts,
                )
            )
        if role_counts["soft"]:
            findings.append(
                _finding(
                    "role_annotation_lint_soft_findings",
                    "soft",
                    "role_annotation_lint has soft findings.",
                    entry_id=entry_id,
                    entry_kind=entry_kind,
                    file="role_annotation_lint_v1.json",
                    data=role_counts,
                )
            )

    semantic = _semantic_summary(reports.get("a4v3_semantic_lint_v1.json"))
    if reports.get("a4v3_semantic_lint_v1.json") is None:
        findings.append(
            _finding(
                "semantic_lint_missing",
                "hard",
                "a4v3_semantic_lint_v1.json is missing.",
                entry_id=entry_id,
                entry_kind=entry_kind,
                file="a4v3_semantic_lint_v1.json",
            )
        )
    else:
        if semantic["strong"]:
            findings.append(
                _finding(
                    "semantic_lint_strong_findings",
                    "hard",
                    "a4v3_semantic_lint has strong findings.",
                    entry_id=entry_id,
                    entry_kind=entry_kind,
                    file="a4v3_semantic_lint_v1.json",
                    data=semantic,
                )
            )
        if semantic["soft"]:
            findings.append(
                _finding(
                    "semantic_lint_soft_findings",
                    "soft",
                    "a4v3_semantic_lint has soft findings.",
                    entry_id=entry_id,
                    entry_kind=entry_kind,
                    file="a4v3_semantic_lint_v1.json",
                    data=semantic,
                )
            )

    token = reports.get("metrics_token_provenance_v1.json") or {}
    token_summary = token.get("summary") or {}
    token_uncovered = int(token_summary.get("uncovered_content_token_count", 0) or 0)
    token_coverage = token_summary.get("content_coverage_rate")
    if reports.get("metrics_token_provenance_v1.json") is None:
        findings.append(
            _finding(
                "token_provenance_missing",
                "hard",
                "metrics_token_provenance_v1.json is missing.",
                entry_id=entry_id,
                entry_kind=entry_kind,
                file="metrics_token_provenance_v1.json",
            )
        )
    elif token_uncovered:
        findings.append(
            _finding(
                "token_provenance_uncovered_tokens",
                "advisory",
                "Token provenance has uncovered content tokens; expected glue/waiver review surface.",
                entry_id=entry_id,
                entry_kind=entry_kind,
                file="metrics_token_provenance_v1.json",
                data={
                    "uncovered_content_token_count": token_uncovered,
                    "content_coverage_rate": token_coverage,
                    "sample": (token.get("uncovered_tokens") or [])[:12],
                },
            )
        )

    family = reports.get("metrics_family_coverage_v1.json") or {}
    required_gaps = int(family.get("n_required_gaps", family.get("required_gaps", 0)) or 0)
    advisory_gaps = int(family.get("n_advisory_gaps", family.get("advisory_gaps", 0)) or 0)
    if reports.get("metrics_family_coverage_v1.json") is None:
        findings.append(
            _finding(
                "family_coverage_missing",
                "hard",
                "metrics_family_coverage_v1.json is missing.",
                entry_id=entry_id,
                entry_kind=entry_kind,
                file="metrics_family_coverage_v1.json",
            )
        )
    else:
        if required_gaps:
            findings.append(
                _finding(
                    "family_coverage_required_gaps",
                    "soft",
                    "Family coverage has required gaps.",
                    entry_id=entry_id,
                    entry_kind=entry_kind,
                    file="metrics_family_coverage_v1.json",
                    data={"required_gaps": required_gaps},
                )
            )
        if advisory_gaps:
            findings.append(
                _finding(
                    "family_coverage_advisory_gaps",
                    "advisory",
                    "Family coverage has advisory gaps.",
                    entry_id=entry_id,
                    entry_kind=entry_kind,
                    file="metrics_family_coverage_v1.json",
                    data={"advisory_gaps": advisory_gaps},
                )
            )

    phrases = reports.get("metrics_source_phrase_coverage_v1.json") or {}
    phrase_uncovered = int(phrases.get("uncovered_count", 0) or 0)
    if reports.get("metrics_source_phrase_coverage_v1.json") is None:
        findings.append(
            _finding(
                "source_phrase_coverage_missing",
                "hard",
                "metrics_source_phrase_coverage_v1.json is missing.",
                entry_id=entry_id,
                entry_kind=entry_kind,
                file="metrics_source_phrase_coverage_v1.json",
            )
        )
    elif phrase_uncovered:
        findings.append(
            _finding(
                "source_phrase_coverage_uncovered",
                "soft",
                "Source phrase coverage has uncovered phrases.",
                entry_id=entry_id,
                entry_kind=entry_kind,
                file="metrics_source_phrase_coverage_v1.json",
                data={
                    "uncovered_count": phrase_uncovered,
                    "coverage_rate": phrases.get("coverage_rate"),
                    "sample": (phrases.get("uncovered") or [])[:8],
                },
            )
        )

    lowering = reports.get("lowering_audit_v1.json") or {}
    lowering_smells = int(lowering.get("n_smells", 0) or 0)
    if reports.get("lowering_audit_v1.json") is None:
        findings.append(
            _finding(
                "lowering_audit_missing",
                "soft",
                "lowering_audit_v1.json is missing.",
                entry_id=entry_id,
                entry_kind=entry_kind,
                file="lowering_audit_v1.json",
            )
        )
    elif lowering_smells:
        findings.append(
            _finding(
                "lowering_audit_smells",
                "soft",
                "lowering_audit reports lowering smells.",
                entry_id=entry_id,
                entry_kind=entry_kind,
                file="lowering_audit_v1.json",
                data={"smells": lowering_smells, "by_candidate_family": lowering.get("by_candidate_family") or {}},
            )
        )

    back = reports.get("provenance_backtranslation_metrics_v1.json") or {}
    back_summary = back.get("summary") or {}
    back_warnings = int(back_summary.get("claims_with_warnings", 0) or 0)
    if reports.get("provenance_backtranslation_metrics_v1.json") is None:
        findings.append(
            _finding(
                "provenance_backtranslation_missing",
                "soft",
                "provenance_backtranslation_metrics_v1.json is missing.",
                entry_id=entry_id,
                entry_kind=entry_kind,
                file="provenance_backtranslation_metrics_v1.json",
            )
        )
    else:
        if back.get("status") != "ok":
            findings.append(
                _finding(
                    "provenance_backtranslation_not_ok",
                    "soft",
                    "Back-translation metrics status is not ok.",
                    entry_id=entry_id,
                    entry_kind=entry_kind,
                    file="provenance_backtranslation_metrics_v1.json",
                    data={"status": back.get("status")},
                )
            )
        if back_warnings:
            findings.append(
                _finding(
                    "provenance_backtranslation_warnings",
                    "advisory",
                    "Back-translation metrics have claim warnings.",
                    entry_id=entry_id,
                    entry_kind=entry_kind,
                    file="provenance_backtranslation_metrics_v1.json",
                    data={"claims_with_warnings": back_warnings},
                )
            )

    diagnostic = reports.get("diagnostic_suite_v1.json") or {}
    diagnostic_gate = diagnostic.get("gate")
    diagnostic_fail = int(diagnostic.get("n_fail", diagnostic.get("fail", 0)) or 0)
    diagnostic_warn = int(diagnostic.get("n_warning", diagnostic.get("warning", 0)) or 0)
    if reports.get("diagnostic_suite_v1.json") is None:
        findings.append(
            _finding(
                "diagnostic_suite_missing",
                "advisory",
                "diagnostic_suite_v1.json is missing.",
                entry_id=entry_id,
                entry_kind=entry_kind,
                file="diagnostic_suite_v1.json",
            )
        )
    else:
        if diagnostic_fail:
            findings.append(
                _finding(
                    "diagnostic_suite_failures",
                    "hard",
                    "Diagnostic suite has failures.",
                    entry_id=entry_id,
                    entry_kind=entry_kind,
                    file="diagnostic_suite_v1.json",
                    data={"gate": diagnostic_gate, "fail": diagnostic_fail},
                )
            )
        if diagnostic_warn:
            findings.append(
                _finding(
                    "diagnostic_suite_warnings",
                    "advisory",
                    "Diagnostic suite has warnings/inspect items.",
                    entry_id=entry_id,
                    entry_kind=entry_kind,
                    file="diagnostic_suite_v1.json",
                    data={"gate": diagnostic_gate, "warning": diagnostic_warn},
                )
            )

    severity_counts = Counter(f["severity"] for f in findings)
    return {
        "entry_id": entry_id,
        "entry_kind": entry_kind,
        "relative_dir": entry["relative_dir"],
        "parse_warning_count": parse_warning_count,
        "declaration_count": declaration_count,
        "assertion_count": assertion_count,
        "quality": quality,
        "semantic_lint": semantic,
        "provenance_lint": provenance_counts,
        "role_annotation_lint": role_counts,
        "token_provenance": {
            "coverage_rate": token_coverage,
            "uncovered_content_token_count": token_uncovered,
        },
        "family_coverage": {
            "required_gaps": required_gaps,
            "advisory_gaps": advisory_gaps,
        },
        "source_phrase_coverage": {
            "coverage_rate": phrases.get("coverage_rate"),
            "uncovered_count": phrase_uncovered,
        },
        "lowering_audit": {"smells": lowering_smells},
        "diagnostic_suite": {
            "gate": diagnostic_gate,
            "fail": diagnostic_fail,
            "warning": diagnostic_warn,
        },
        "findings": findings,
        "hard_findings": severity_counts.get("hard", 0),
        "soft_findings": severity_counts.get("soft", 0),
        "advisory_findings": severity_counts.get("advisory", 0),
    }


def analyze(run_root: Path) -> dict[str, Any]:
    entries = _discover_entries(run_root)
    entry_reports = [_analyze_entry(entry) for entry in entries]

    all_findings = [finding for report in entry_reports for finding in report["findings"]]
    severity_counts = Counter(f["severity"] for f in all_findings)
    by_entry_kind = Counter(report["entry_kind"] for report in entry_reports)
    clean_gate_counts = Counter((report["quality"] or {}).get("clean_gate") for report in entry_reports)
    hard_entries = [report["entry_id"] for report in entry_reports if report["hard_findings"]]
    soft_entries = [report["entry_id"] for report in entry_reports if report["soft_findings"]]
    advisory_entries = [report["entry_id"] for report in entry_reports if report["advisory_findings"]]

    by_code: dict[str, int] = dict(Counter(f["code"] for f in all_findings))
    by_severity_code: dict[str, dict[str, int]] = defaultdict(dict)
    for finding in all_findings:
        severity = finding["severity"]
        code = finding["code"]
        by_severity_code[severity][code] = by_severity_code[severity].get(code, 0) + 1

    status = "blocked" if severity_counts.get("hard", 0) else "passed_with_review_items"
    if not all_findings:
        status = "passed"

    return {
        "schema": "fragment_readiness_audit_v1",
        "run_root": str(run_root),
        "entry_count": len(entry_reports),
        "entry_count_by_kind": dict(by_entry_kind),
        "clean_gate_counts": dict(clean_gate_counts),
        "hard_findings": severity_counts.get("hard", 0),
        "soft_findings": severity_counts.get("soft", 0),
        "advisory_findings": severity_counts.get("advisory", 0),
        "entries_with_hard_findings": hard_entries,
        "entries_with_soft_findings": soft_entries,
        "entries_with_advisory_findings": advisory_entries,
        "finding_count_by_code": by_code,
        "finding_count_by_severity_code": dict(by_severity_code),
        "entries": entry_reports,
        "findings": all_findings,
        "status": status,
    }


def _write_markdown(report: dict[str, Any], out_path: Path) -> None:
    lines: list[str] = []
    lines.append("# Fragment Readiness Audit v1")
    lines.append("")
    lines.append(f"Status: `{report['status']}`")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    for key in [
        "entry_count",
        "entry_count_by_kind",
        "clean_gate_counts",
        "hard_findings",
        "soft_findings",
        "advisory_findings",
    ]:
        lines.append(f"- `{key}`: `{json.dumps(report.get(key), ensure_ascii=False)}`")
    lines.append("")

    lines.append("## Entry Table")
    lines.append("")
    lines.append("| Entry | Kind | Gate | Hard | Soft | Advisory | Token cov. | Source phrase cov. |")
    lines.append("| --- | --- | --- | ---: | ---: | ---: | ---: | ---: |")
    for entry in report.get("entries", []):
        token_cov = entry.get("token_provenance", {}).get("coverage_rate")
        phrase_cov = entry.get("source_phrase_coverage", {}).get("coverage_rate")
        token_s = "" if token_cov is None else f"{float(token_cov):.3f}"
        phrase_s = "" if phrase_cov is None else f"{float(phrase_cov):.3f}"
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{entry['entry_id']}`",
                    entry["entry_kind"],
                    f"`{entry.get('quality', {}).get('clean_gate')}`",
                    str(entry["hard_findings"]),
                    str(entry["soft_findings"]),
                    str(entry["advisory_findings"]),
                    token_s,
                    phrase_s,
                ]
            )
            + " |"
        )
    lines.append("")

    lines.append("## Findings By Code")
    lines.append("")
    by_code = report.get("finding_count_by_code") or {}
    if not by_code:
        lines.append("No findings.")
    else:
        for code, count in sorted(by_code.items(), key=lambda kv: (-kv[1], kv[0])):
            lines.append(f"- `{code}`: {count}")
    lines.append("")

    lines.append("## Hard Findings")
    lines.append("")
    hard = [f for f in report.get("findings", []) if f["severity"] == "hard"]
    if not hard:
        lines.append("No hard findings.")
    else:
        for i, finding in enumerate(hard, start=1):
            lines.append(
                f"{i}. `{finding['entry_id']}` `{finding['code']}`"
                f" file `{finding.get('file', '')}`: {finding['message']}"
            )
    lines.append("")

    lines.append("## Soft Findings")
    lines.append("")
    soft = [f for f in report.get("findings", []) if f["severity"] == "soft"]
    if not soft:
        lines.append("No soft findings.")
    else:
        for i, finding in enumerate(soft[:80], start=1):
            data = finding.get("data") or {}
            compact = {k: data[k] for k in ("clean_gate", "strong", "soft", "required_gaps", "smells", "coverage_rate", "uncovered_count") if k in data}
            detail = f" Data: `{json.dumps(compact, ensure_ascii=False)}`" if compact else ""
            lines.append(
                f"{i}. `{finding['entry_id']}` `{finding['code']}`"
                f" file `{finding.get('file', '')}`: {finding['message']}{detail}"
            )
        if len(soft) > 80:
            lines.append(f"... {len(soft) - 80} more soft findings omitted from Markdown; see JSON.")
    lines.append("")

    lines.append("## Advisory Findings")
    lines.append("")
    advisory = [f for f in report.get("findings", []) if f["severity"] == "advisory"]
    if not advisory:
        lines.append("No advisory findings.")
    else:
        grouped = Counter(f["code"] for f in advisory)
        for code, count in sorted(grouped.items(), key=lambda kv: (-kv[1], kv[0])):
            lines.append(f"- `{code}`: {count}")
        lines.append("")
        lines.append("Full advisory details are in the JSON report.")
    lines.append("")

    lines.append("## Interpretation")
    lines.append("")
    lines.append(
        "Hard findings block fragment-readiness. Soft findings need a modeling "
        "decision or documented review before relying on the affected fragment "
        "for merge. Advisory findings keep accepted glue, stale reports, and "
        "intentional deferrals visible without blocking the corpus."
    )
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-root", default="case_studies/financial_methodology")
    ap.add_argument("--out-dir", default=None)
    args = ap.parse_args()

    run_root = Path(args.run_root)
    out_dir = Path(args.out_dir) if args.out_dir else run_root / "reasoning"
    out_dir.mkdir(parents=True, exist_ok=True)

    report = analyze(run_root)
    json_path = out_dir / "fragment_readiness_audit_v1.json"
    md_path = out_dir / "fragment_readiness_audit_v1.md"
    json_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    _write_markdown(report, md_path)
    print(
        json.dumps(
            {
                "status": report["status"],
                "entry_count": report["entry_count"],
                "hard_findings": report["hard_findings"],
                "soft_findings": report["soft_findings"],
                "advisory_findings": report["advisory_findings"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
