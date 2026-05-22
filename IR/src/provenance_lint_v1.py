"""provenance_lint_v1.py

Deterministic lint checks for DZ provenance.yaml files.

The first check catches a recurring translator error: leaking A4V3 CamelCase
identifiers into the human-readable back_translation field. Back-translations
should read like source-facing English, not like IR code.

Outputs:
  <entry>/provenance_lint_v1.json
  <entry>/provenance_lint_v1.md

CLI:
  python provenance_lint_v1.py [entry_dir|run_root]
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys
from collections import Counter
from datetime import datetime
from typing import Any

import yaml


CAMELCASE_RE = re.compile(r"\b[A-Z][a-z]+(?:[A-Z][A-Za-z0-9]*|[a-z]+[A-Z][A-Za-z0-9]*)+\b")
DECL_RE = re.compile(
    r"^(?P<kind>sort|entity|rel|fun|val|fact|constraint|axiom|prop|action|"
    r"obligation|permission|prohibition|theorem)(?:\[[^\]]+\])?\s+"
    r"(?P<name>[A-Za-z_][A-Za-z0-9_]*)\b"
)

DEFAULT_ALLOWLIST = {
    # Source/proper names and common external identifiers that may reasonably
    # appear unspaced in prose.
    "BoerseStuttgart",
    "IntercontinentalExchange",
    "Reuters",
}


def _read_text(path: pathlib.Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="replace")


def _load_yaml(path: pathlib.Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        return data if isinstance(data, dict) else {"_load_error": "top-level YAML is not a mapping"}
    except Exception as exc:
        return {"_load_error": f"{type(exc).__name__}: {exc}"}


def _main_ir_identifiers(text: str) -> set[str]:
    out: set[str] = set()
    for raw in text.splitlines():
        line = raw.split("--", 1)[0].strip()
        if not line:
            continue
        m = DECL_RE.match(line)
        if m:
            out.add(m.group("name"))
            rest = line[m.end():]
            if m.group("kind") == "sort" and "=" in rest:
                for part in rest.split("=", 1)[1].split("|"):
                    name = part.strip()
                    if re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", name):
                        out.add(name)
    return out


def _entry_dirs(target: pathlib.Path) -> list[pathlib.Path]:
    target = target.resolve()
    if (target / "provenance.yaml").exists() or (target / "main_ir.a4v3").exists():
        return [target]
    return [
        p.parent
        for p in sorted(target.rglob("provenance.yaml"))
        if (p.parent / "main_ir.a4v3").exists()
        and not p.parent.name.startswith("_")
    ]


def _note_mentions_source_phrase(note: Any) -> bool:
    blob = ""
    if isinstance(note, dict):
        blob = " ".join(str(v) for v in note.values())
    else:
        blob = str(note or "")
    lowered = blob.lower()
    return "source phrase" in lowered or "source uses" in lowered or "source's" in lowered


def lint_entry(entry_dir: pathlib.Path) -> dict[str, Any]:
    prov_path = entry_dir / "provenance.yaml"
    data = _load_yaml(prov_path)
    findings: list[dict[str, Any]] = []
    if not prov_path.exists():
        return {
            "schema": "provenance_lint_v1",
            "entry_id": entry_dir.name,
            "generated_at": datetime.now().isoformat(timespec="seconds"),
            "status": "missing_provenance",
            "findings": [],
            "summary": {
                "total_findings": 0,
                "strong_findings": 0,
                "soft_findings": 0,
                "advisory_findings": 0,
                "by_check": {},
            },
        }
    if data.get("_load_error"):
        findings.append({
            "check": "provenance_yaml_parse_error",
            "severity": "strong",
            "reason": data["_load_error"],
        })
    main_ir = _read_text(entry_dir / "main_ir.a4v3")
    declared = _main_ir_identifiers(main_ir)
    vocabulary_notes = data.get("vocabulary_notes") if isinstance(data, dict) else {}
    if not isinstance(vocabulary_notes, dict):
        vocabulary_notes = {}
    vocab_keys = set(vocabulary_notes.keys())
    source_phrase_vocab = {
        key for key, note in (vocabulary_notes or {}).items()
        if isinstance(key, str) and _note_mentions_source_phrase(note)
    }
    allowlist = set(DEFAULT_ALLOWLIST)
    extra_allow = data.get("back_translation_camelcase_allowlist") if isinstance(data, dict) else None
    if isinstance(extra_allow, list):
        allowlist.update(str(item) for item in extra_allow)

    claims = data.get("claims") if isinstance(data, dict) else {}
    if not isinstance(claims, dict):
        claims = {}

    for claim_id, claim in claims.items():
        if not isinstance(claim, dict):
            continue
        bt = str(claim.get("back_translation") or "")
        if not bt.strip():
            continue
        matches = sorted(set(CAMELCASE_RE.findall(bt)))
        leaks: list[str] = []
        for match in matches:
            if match in allowlist:
                continue
            if match in declared or match in vocab_keys:
                leaks.append(match)
        if leaks:
            vocab_basis = str(claim.get("vocabulary_basis") or "")
            severity = "strong" if vocab_basis == "source_only" else "soft"
            findings.append({
                "check": "back_translation_camelcase_identifier_leak",
                "severity": severity,
                "claim_id": str(claim_id),
                "vocabulary_basis": vocab_basis or None,
                "leaks": leaks,
                "reason": (
                    "back_translation contains CamelCase IR identifiers; use "
                    "source-facing spaced phrases instead."
                ),
            })
            if vocab_basis == "source_only":
                findings.append({
                    "check": "vocabulary_basis_consistency",
                    "severity": "strong",
                    "claim_id": str(claim_id),
                    "vocabulary_basis": vocab_basis,
                    "leaks": leaks,
                    "reason": (
                        "claim is marked source_only but its back_translation "
                        "contains IR identifiers."
                    ),
                })
        source_phrase_leaks = [m for m in matches if m in source_phrase_vocab and m not in allowlist]
        if source_phrase_leaks:
            findings.append({
                "check": "back_translation_uses_source_phrase_for_named_entity",
                "severity": "strong",
                "claim_id": str(claim_id),
                "leaks": sorted(set(source_phrase_leaks)),
                "reason": (
                    "vocabulary_notes describe this identifier as source-facing; "
                    "back_translation should use the source phrase, not the IR identifier."
                ),
            })

    counts = Counter(f["check"] for f in findings)
    summary = {
        "total_findings": len(findings),
        "strong_findings": sum(1 for f in findings if f.get("severity") == "strong"),
        "soft_findings": sum(1 for f in findings if f.get("severity") == "soft"),
        "advisory_findings": sum(1 for f in findings if f.get("severity") == "advisory"),
        "by_check": dict(sorted(counts.items())),
    }
    return {
        "schema": "provenance_lint_v1",
        "entry_id": entry_dir.name,
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "status": "ok",
        "summary": summary,
        "allowlist": sorted(allowlist),
        "findings": findings,
    }


def write_report(entry_dir: pathlib.Path, report: dict[str, Any]) -> None:
    json_p = entry_dir / "provenance_lint_v1.json"
    md_p = entry_dir / "provenance_lint_v1.md"
    json_p.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    summary = report.get("summary") or {}
    lines = [
        f"# Provenance Lint: {report.get('entry_id')}",
        "",
        f"- total_findings: `{summary.get('total_findings', 0)}`",
        f"- strong/soft/advisory: `{summary.get('strong_findings', 0)}` / "
        f"`{summary.get('soft_findings', 0)}` / `{summary.get('advisory_findings', 0)}`",
        f"- by_check: `{summary.get('by_check', {})}`",
    ]
    findings = report.get("findings") or []
    if findings:
        lines.extend(["", "## Findings", ""])
        for f in findings:
            lines.append(f"### `{f.get('check')}` / `{f.get('claim_id', '')}`")
            lines.append("")
            lines.append(f"- severity: `{f.get('severity')}`")
            if f.get("vocabulary_basis"):
                lines.append(f"- vocabulary_basis: `{f.get('vocabulary_basis')}`")
            if f.get("leaks"):
                lines.append(f"- leaks: `{', '.join(f.get('leaks') or [])}`")
            lines.append(f"- reason: {f.get('reason')}")
            lines.append("")
    else:
        lines.extend(["", "No provenance-lint findings.", ""])
    md_p.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("target", help="DZ entry dir or run root")
    args = ap.parse_args()
    target = pathlib.Path(args.target)
    entries = _entry_dirs(target)
    if not entries:
        raise SystemExit(f"No provenance.yaml/main_ir.a4v3 entries found under {target}")
    corpus = []
    for entry in entries:
        report = lint_entry(entry)
        write_report(entry, report)
        corpus.append(report)
        s = report.get("summary") or {}
        print(
            f"{entry}: findings={s.get('total_findings', 0)} "
            f"strong={s.get('strong_findings', 0)}"
        )
    if len(corpus) > 1:
        out = {
            "schema": "provenance_lint_corpus_v1",
            "generated_at": datetime.now().isoformat(timespec="seconds"),
            "entry_count": len(corpus),
            "entries": [
                {
                    "entry_id": r.get("entry_id"),
                    "total_findings": (r.get("summary") or {}).get("total_findings", 0),
                    "strong_findings": (r.get("summary") or {}).get("strong_findings", 0),
                    "soft_findings": (r.get("summary") or {}).get("soft_findings", 0),
                }
                for r in corpus
            ],
        }
        (target / "provenance_lint_corpus_v1.json").write_text(
            json.dumps(out, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )


if __name__ == "__main__":
    main()
