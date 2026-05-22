"""Replay recorded public demo results.

This script is intentionally offline: it does not call an LLM provider and does
not run Z3. It verifies that the checked demonstration records bundled with the
repository have the expected outcomes, then prints a compact report.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def _load_demo(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _iter_demo_files(selected: str | None):
    demos = ["russian_law", "draughts_64"] if selected is None else [selected]
    for name in demos:
        yield ROOT / name / "expected_results.json"


def _report_demo(data: dict) -> tuple[int, int]:
    results = data.get("results", [])
    passed = 0
    print(f"\n== {data.get('name', 'demo')} ==")
    print(data.get("summary", ""))
    for item in results:
        actual = item.get("final")
        expected = item.get("expected")
        ok = actual == expected
        passed += int(ok)
        mark = "OK" if ok else "FAIL"
        print(f"{mark:4} {item.get('id')}: {actual} (expected {expected})")
    print(f"score: {passed}/{len(results)}")
    return passed, len(results)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "demo",
        nargs="?",
        choices=["russian_law", "draughts_64"],
        help="Replay one demo. By default, replay all public demos.",
    )
    args = parser.parse_args()

    total_passed = 0
    total = 0
    for path in _iter_demo_files(args.demo):
        data = _load_demo(path)
        passed, count = _report_demo(data)
        total_passed += passed
        total += count

    print(f"\nTOTAL: {total_passed}/{total}")
    return 0 if total_passed == total else 1


if __name__ == "__main__":
    raise SystemExit(main())

