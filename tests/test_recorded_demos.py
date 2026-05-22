from __future__ import annotations

import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class RecordedDemoTests(unittest.TestCase):
    def test_recorded_demo_expectations_match(self) -> None:
        files = sorted((ROOT / "demos").glob("*/expected_results.json"))
        self.assertTrue(files, "No recorded demo files found")
        for path in files:
            with self.subTest(path=path):
                data = json.loads(path.read_text(encoding="utf-8"))
                for item in data.get("results", []):
                    self.assertEqual(item.get("final"), item.get("expected"), item)


if __name__ == "__main__":
    unittest.main()

