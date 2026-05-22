"""Workspace tools: user hints, bridge, agent notes."""
from __future__ import annotations

import re
from typing import Any

from ir_agent.config import ROOT
from ir_agent.env import ToolEnv
from ir_agent.helpers import _read_text, _truncate


def tool_read_user_hints(env: ToolEnv) -> dict[str, Any]:
    """Read user hints active for this translation, per IR/index/user_hints_contract.md.
    Hints are plain-text directives from a human reviewer that should be honored
    by the agent during translation and explicitly cited in provenance/notes.

    Search locations (in priority order):
      1. <section_dir>/user_hints/active.yaml — section-specific hints
      2. <agent_run_dir>/user_hints/active.yaml — run-specific overrides
      3. <corpus_run_dir>/user_hints/active.yaml — global hints for the corpus

    Returns combined hints with source_path per hint. Empty if none found."""
    candidates = [
        ("section", env.section_dir / "user_hints" / "active.yaml"),
        ("agent_run", env.agent_run_dir / "user_hints" / "active.yaml"),
        ("corpus_global", env.corpus_paths.run_dir / "user_hints" / "active.yaml"),
    ]
    found_files = [(scope, p) for scope, p in candidates if p.exists()]
    if not found_files:
        return {
            "hints_found": 0,
            "note": (
                "No user_hints/active.yaml in any expected location. Per "
                "IR/index/user_hints_contract.md, hints would live at "
                "<section_dir>/user_hints/active.yaml, "
                "<agent_run_dir>/user_hints/active.yaml, or "
                "<run_root>/user_hints/active.yaml. Proceeding without hints."
            ),
            "expected_paths": [str(p) for _, p in candidates],
        }

    out_hints: list[dict[str, Any]] = []
    for scope, p in found_files:
        text = _read_text(p, max_chars=24000)
        out_hints.append({
            "scope_origin": scope,
            "path": str(p.relative_to(ROOT)) if ROOT in p.parents else str(p),
            "raw_yaml": text,
        })
    return {
        "hints_found": len(out_hints),
        "files": out_hints,
        "instruction": (
            "Hints are PLAIN-TEXT directives. If a hint changes how you would "
            "translate a phrase, the resulting IR (or its provenance/notes) "
            "MUST cite the hint_id (so the change is auditable). If two hints "
            "conflict — DO NOT guess: flag in agent_notes/finalize and request "
            "human disambiguation."
        ),
    }


def tool_read_bridge(env: ToolEnv) -> dict[str, Any]:
    bridge_dir = env.corpus_paths.bridge_dir
    if bridge_dir is None or not bridge_dir.exists():
        return {"error": "no bridge dir in this corpus"}
    return {
        "main_bridge": _truncate(_read_text(bridge_dir / "main_bridge.a4v3"), 8000),
        "provenance": _truncate(_read_text(bridge_dir / "provenance.yaml"), 6000),
        "translator_notes": _truncate(_read_text(bridge_dir / "translator_notes.md"), 6000),
    }


def tool_save_note(env: ToolEnv, *, name: str, content: str) -> dict[str, Any]:
    safe_name = re.sub(r"[^a-zA-Z0-9_.-]", "_", name)[:80]
    if not safe_name.endswith(".md") and not safe_name.endswith(".json"):
        safe_name += ".md"
    path = env.discovery_dir / safe_name
    path.write_text(content, encoding="utf-8")
    return {"saved": safe_name, "chars": len(content),
            "path": str(path.relative_to(env.agent_run_dir))}


def tool_read_my_notes(env: ToolEnv,
                       *, name: str | None = None) -> dict[str, Any]:
    if name:
        safe_name = re.sub(r"[^a-zA-Z0-9_.-]", "_", name)
        path = env.discovery_dir / safe_name
        if not path.exists() and not safe_name.endswith((".md", ".json")):
            for ext in [".md", ".json"]:
                if (env.discovery_dir / (safe_name + ext)).exists():
                    path = env.discovery_dir / (safe_name + ext)
                    break
        if not path.exists():
            return {"error": f"note not found: {name}"}
        return {"name": path.name,
                "content": _truncate(path.read_text(encoding="utf-8"), 6000)}
    notes = []
    for p in sorted(env.discovery_dir.iterdir()):
        if p.is_file():
            notes.append({"name": p.name, "chars": p.stat().st_size})
    return {"notes_count": len(notes), "notes": notes}
