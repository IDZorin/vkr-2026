from __future__ import annotations

import unittest

import a4v3_ir_toolkit as toolkit


class PackageFacadeTests(unittest.TestCase):
    def test_public_tool_discovery(self) -> None:
        tools = toolkit.list_public_tools()
        self.assertIn("a4v3_parser_v1.py", tools)
        self.assertTrue(toolkit.tool_path("a4v3_parser_v1").exists())


if __name__ == "__main__":
    unittest.main()
