"""Small public facade for the A4V3 IR Toolkit.

The executable research tools are intentionally kept as path-based scripts in
``IR/src`` to preserve the thesis artifact layout. This package provides stable
helpers for discovering those tools from Python or from the command line.
"""

from .paths import ir_src_dir, list_public_tools, repo_root, tool_path

__version__ = "0.1.0"

__all__ = [
    "__version__",
    "ir_src_dir",
    "list_public_tools",
    "repo_root",
    "tool_path",
]
