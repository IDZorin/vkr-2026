"""Command-line entry point for lightweight toolkit discovery."""

from __future__ import annotations

import argparse

from . import __version__
from .paths import ir_src_dir, list_public_tools, repo_root, tool_path


def main() -> int:
    parser = argparse.ArgumentParser(prog="a4v3-toolkit")
    parser.add_argument("--version", action="store_true", help="print package version")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("root", help="print repository root")
    subparsers.add_parser("src", help="print IR/src tool directory")
    subparsers.add_parser("tools", help="list public tool scripts")

    path_parser = subparsers.add_parser("path", help="print path to one tool script")
    path_parser.add_argument("tool_name", help="tool name, with or without .py")

    args = parser.parse_args()

    if args.version:
        print(__version__)
        return 0
    if args.command == "root":
        print(repo_root())
        return 0
    if args.command == "src":
        print(ir_src_dir())
        return 0
    if args.command == "tools":
        for name in list_public_tools():
            print(name)
        return 0
    if args.command == "path":
        print(tool_path(args.tool_name))
        return 0

    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
