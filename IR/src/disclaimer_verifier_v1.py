"""disclaimer_verifier_v1.py

Verifies disclaimer entries against diagnostic findings, then re-classifies
fail-level findings:

  - if a finding has a matching disclaimer entry (by token + metric_rule):
        finding's effective level becomes `documented`
  - otherwise:
        finding stays `fail`

Disclaimer file format (per entry_dir/disclaimers_v1.json):

  {
    "entry_id": "<id>",
    "spec_version": "v1",
    "disclaimers": [
      {
        "token": "<source token like 'must'>",
        "source_phrase": "<longer source phrase containing token>",
        "metric_rule": "<rule name like 'expected_family_present'>",
        "metric_module": "<optional, for matching>",
        "expected_family": "<optional, for context>",
        "ir_decision": "<short tag like 'lowered_as_value_constraint'>",
        "ir_location": "<short pointer to IR decl/constraint>",
        "explanation": "<text >= 10 chars explaining the decision>"
      }
    ]
  }

Each disclaimer entry MUST satisfy:
  - non-empty `token`
  - non-empty `metric_rule`
  - `explanation` length >= 10 chars

A finding is matched by a disclaimer if:
  - finding's rule == disclaimer's metric_rule, AND
  - the disclaimer's token (case-insensitive) appears in either:
      * finding's evidence_summary, OR
      * finding's value (when value is a string/list)
  - if disclaimer specifies metric_module, finding's module must match.

CLI:
  python disclaimer_verifier_v1.py <entry_dir>
"""
from __future__ import annotations
import argparse
import json
import pathlib
import sys
from typing import Any


def _validate_disclaimer_entry(entry: dict, idx: int) -> list[str]:
    errors: list[str] = []
    token = (entry.get("token") or "").strip()
    if not token:
        errors.append(f"[{idx}] missing or empty `token`")
    rule = (entry.get("metric_rule") or "").strip()
    if not rule:
        errors.append(f"[{idx}] missing or empty `metric_rule`")
    expl = entry.get("explanation") or ""
    if not isinstance(expl, str) or len(expl.strip()) < 10:
        errors.append(
            f"[{idx}] `explanation` must be a string of length >= 10 "
            f"(got {len(expl) if isinstance(expl, str) else 'non-string'})"
        )
    return errors


def load_disclaimers(entry_dir: pathlib.Path) -> tuple[list[dict], list[str]]:
    """Load disclaimers from <entry_dir>/disclaimers_v1.json.

    Returns (disclaimers, validation_errors). On schema errors, the
    offending entries are skipped from the returned list.
    """
    p = entry_dir / "disclaimers_v1.json"
    if not p.exists():
        return [], []
    try:
        d = json.loads(p.read_text(encoding="utf-8"))
    except Exception as e:
        return [], [f"failed to parse disclaimers_v1.json: {e}"]
    items = d.get("disclaimers") or []
    out: list[dict] = []
    errs: list[str] = []
    for i, entry in enumerate(items):
        if not isinstance(entry, dict):
            errs.append(f"[{i}] not an object")
            continue
        e_errs = _validate_disclaimer_entry(entry, i)
        if e_errs:
            errs.extend(e_errs)
            continue
        out.append(entry)
    return out, errs


def _evidence_string(finding: dict) -> str:
    """Concatenate searchable string from finding fields for token matching."""
    parts: list[str] = []
    for k in ("evidence_summary", "value", "what_it_counts", "bad_value_means"):
        v = finding.get(k)
        if v is None:
            continue
        parts.append(str(v))
    return " ".join(parts).lower()


def _disclaimer_matches_finding(disclaimer: dict, finding: dict) -> bool:
    rule = (finding.get("rule") or "").strip()
    d_rule = (disclaimer.get("metric_rule") or "").strip()
    if rule != d_rule:
        return False
    d_module = (disclaimer.get("metric_module") or "").strip()
    if d_module:
        f_module = (finding.get("module") or "").strip()
        if d_module != f_module:
            return False
    token = (disclaimer.get("token") or "").strip().lower()
    if not token:
        return False
    return token in _evidence_string(finding)


def verify_entry(entry_dir: pathlib.Path) -> dict:
    """Cross-reference disclaimers against the entry's diagnostic_suite_v1.json.

    Returns:
      {
        "entry_id": str,
        "n_disclaimers": int,
        "schema_errors": [...],         # disclaimer entries with bad shape
        "matched_findings": [...],       # findings reclassified as documented
        "unmatched_disclaimers": [...],  # disclaimers without any finding match
        "remaining_fails": [...],        # findings still fail-level after match
        "summary": {
          "n_fails_before": int,
          "n_fails_after_disclaimer": int,
          "n_documented": int,
        }
      }
    """
    suite_p = entry_dir / "diagnostic_suite_v1.json"
    if not suite_p.exists():
        return {"error": f"no diagnostic_suite_v1.json in {entry_dir}",
                "entry_id": entry_dir.name}
    suite = json.loads(suite_p.read_text(encoding="utf-8"))
    findings = suite.get("findings", [])

    disclaimers, schema_errors = load_disclaimers(entry_dir)

    matched: list[dict] = []
    unmatched_disclaimers: list[dict] = []
    used_disclaimer_idx: set[int] = set()
    remaining_fails: list[dict] = []

    fails = [f for f in findings if f.get("level") == "fail"]
    n_fails_before = len(fails)

    for f in fails:
        # Multi-match: a single finding can carry multiple flagged tokens
        # (e.g. expected_family_present with value=2 carries both 'must'
        # and 'exactly 50'). Any disclaimer that matches the finding by
        # rule + token consumes the disclaimer; the finding is documented
        # if at least one disclaimer matched.
        matched_idxs: list[int] = []
        for i, d in enumerate(disclaimers):
            if _disclaimer_matches_finding(d, f):
                matched_idxs.append(i)
        if not matched_idxs:
            remaining_fails.append({
                "module": f.get("module"),
                "rule": f.get("rule"),
                "value": f.get("value"),
                "evidence_summary": (f.get("evidence_summary") or "")[:200],
            })
        else:
            for i in matched_idxs:
                used_disclaimer_idx.add(i)
            matched.append({
                "finding": {
                    "module": f.get("module"),
                    "rule": f.get("rule"),
                    "value": f.get("value"),
                },
                "disclaimers": [disclaimers[i] for i in matched_idxs],
            })

    for i, d in enumerate(disclaimers):
        if i not in used_disclaimer_idx:
            unmatched_disclaimers.append(d)

    return {
        "entry_id": entry_dir.name,
        "n_disclaimers": len(disclaimers),
        "schema_errors": schema_errors,
        "matched_findings": matched,
        "unmatched_disclaimers": unmatched_disclaimers,
        "remaining_fails": remaining_fails,
        "summary": {
            "n_fails_before": n_fails_before,
            "n_fails_after_disclaimer": len(remaining_fails),
            "n_documented": len(matched),
        },
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("entry_dir")
    ap.add_argument("--save", action="store_true",
                    help="write report to <entry_dir>/disclaimer_verification_v1.json")
    args = ap.parse_args()
    entry_dir = pathlib.Path(args.entry_dir)
    res = verify_entry(entry_dir)
    print(json.dumps(res, indent=2, ensure_ascii=False, default=str))
    if args.save and "error" not in res:
        out_p = entry_dir / "disclaimer_verification_v1.json"
        out_p.write_text(json.dumps(res, indent=2, ensure_ascii=False, default=str),
                         encoding="utf-8")
        print(f"\nSaved: {out_p}")


if __name__ == "__main__":
    main()
