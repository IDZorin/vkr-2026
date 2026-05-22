"""Run the public deterministic A4V3 checks for one local entry.

This is intentionally smaller than the private research runner. It does not
call LLM judges or legacy experiment metrics.
"""
from __future__ import annotations

import argparse
import json
import os
import pathlib
import subprocess
import sys
import time
from datetime import datetime
from typing import Any


ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC = ROOT / "IR" / "src"


def _tail(text: str, max_chars: int = 3000) -> str:
    return text if len(text) <= max_chars else text[-max_chars:]


def _run(name: str, cmd: list[str]) -> dict[str, Any]:
    started = time.time()
    env = os.environ.copy()
    env.setdefault("PYTHONIOENCODING", "utf-8")
    proc = subprocess.run(
        cmd,
        cwd=str(ROOT),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        env=env,
    )
    return {
        "name": name,
        "status": "ok" if proc.returncode == 0 else "error",
        "returncode": proc.returncode,
        "duration_s": round(time.time() - started, 3),
        "cmd": cmd,
        "stdout_tail": _tail(proc.stdout or ""),
        "stderr_tail": _tail(proc.stderr or ""),
    }


def _load_json(path: pathlib.Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return {"_load_error": f"{type(exc).__name__}: {exc}"}


def _write_report(entry: pathlib.Path, steps: list[dict[str, Any]]) -> None:
    payload = {
        "schema": "a4v3_public_check_report_v1",
        "generated_at": datetime.utcnow().isoformat(timespec="seconds") + "Z",
        "entry": str(entry),
        "overall_status": "ok" if all(s["status"] == "ok" for s in steps) else "error",
        "steps": steps,
        "quality_snapshot": _load_json(entry / "quality_snapshot_v1.json"),
    }
    (entry / "release_check_report.json").write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    lines = [
        f"# Public A4V3 Check Report: {entry.name}",
        "",
        f"- generated_at: `{payload['generated_at']}`",
        f"- overall_status: `{payload['overall_status']}`",
        "",
        "| step | status | returncode | duration_s |",
        "| --- | --- | ---: | ---: |",
    ]
    for step in steps:
        lines.append(
            f"| {step['name']} | {step['status']} | "
            f"{step['returncode']} | {step['duration_s']} |"
        )
    (entry / "release_check_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("entry", type=pathlib.Path, help="Directory with main_ir.a4v3")
    args = ap.parse_args()

    entry = args.entry.resolve()
    if not (entry / "main_ir.a4v3").exists():
        raise SystemExit(f"No main_ir.a4v3 in {entry}")

    py = sys.executable
    steps = [
        _run("parser_strict", [py, str(SRC / "a4v3_parser_v1.py"), str(entry / "main_ir.a4v3"), "--strict"]),
        _run("semantic_lint", [py, str(SRC / "a4v3_semantic_lint_v1.py"), str(entry)]),
        _run("token_provenance", [py, str(SRC / "token_provenance_v1.py"), str(entry)]),
        _run("provenance_lint", [py, str(SRC / "provenance_lint_v1.py"), str(entry)]),
        _run("provenance_backtranslation", [py, str(SRC / "provenance_backtranslation_metrics_v1.py"), str(entry)]),
        _run("family_coverage", [py, str(SRC / "family_coverage_v1.py"), str(entry)]),
        _run("source_phrase_coverage", [py, str(SRC / "source_phrase_coverage_v1.py"), str(entry)]),
        _run("lowering_audit", [py, str(SRC / "lowering_audit_v1.py"), str(entry)]),
        _run("quality_snapshot", [py, str(SRC / "quality_snapshot_v1.py"), str(entry)]),
    ]
    _write_report(entry, steps)
    for step in steps:
        print(f"{step['name']}: {step['status']} ({step['duration_s']}s)")
        if step["status"] != "ok":
            print(step["stderr_tail"] or step["stdout_tail"])
    return 0 if all(step["status"] == "ok" for step in steps) else 1


if __name__ == "__main__":
    raise SystemExit(main())
