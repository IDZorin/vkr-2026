"""Path helpers for the public A4V3 toolkit repository."""

from __future__ import annotations

from pathlib import Path


def repo_root() -> Path:
    """Return the repository root that contains ``IR/src`` and public demos."""

    return Path(__file__).resolve().parents[1]


def ir_src_dir() -> Path:
    """Return the directory containing path-based A4V3 tool scripts."""

    return repo_root() / "IR" / "src"


def tool_path(tool_name: str) -> Path:
    """Return the path to an A4V3 tool script in ``IR/src``.

    ``tool_name`` may be passed either with or without the ``.py`` suffix.
    A ``FileNotFoundError`` is raised if the tool is not part of the public
    bundle.
    """

    name = tool_name if tool_name.endswith(".py") else f"{tool_name}.py"
    path = ir_src_dir() / name
    if not path.exists():
        raise FileNotFoundError(f"No public A4V3 tool named {name!r} in {ir_src_dir()}")
    return path


def list_public_tools() -> list[str]:
    """Return sorted public tool script names available under ``IR/src``."""

    src = ir_src_dir()
    if not src.exists():
        return []
    return sorted(path.name for path in src.glob("*.py") if path.name != "__init__.py")
