"""Iter snapshots + rollback helpers.

Each clean DRAFT and each VERIFY round auto-snapshots IR + verdict to
iter_<N>/. Used by compare_iters, rollback_to_iter, and auto-rollback
detection inside run_package_checks.
"""
from __future__ import annotations

import json
import pathlib
import re
from typing import Any

from ir_agent.env import ToolEnv
from ir_agent.helpers import _hash_text, _utcnow
from ir_agent.phases import _PHASE_PACKAGE_DRAFTING
from ir_agent.strategy_io import _latest_strategy_path


def _snapshot_iter(agent_run_dir: pathlib.Path,
                    iter_idx: int,
                    kind: str,
                    discovery_dir: pathlib.Path | None = None,
                    verdict_data: dict[str, Any] | None = None,
                    extra_artifacts: dict[str, str] | None = None,
                    ) -> pathlib.Path:
    """Snapshot the current state of main_ir.a4v3 (+ provenance/waivers if
    present) into iter_<iter_idx>/ for later comparison or rollback.
    `kind` is one of "draft" (taken when IR passes lint, before verify) or
    "verify" (taken at run_package_checks completion, includes verdict).

    Snapshots are append-only — never overwritten. Re-snapshotting the same
    iter_idx with same kind silently appends a counter suffix.
    Returns the iter dir path.
    """
    base = agent_run_dir / f"iter_{iter_idx}"
    base.mkdir(exist_ok=True)
    # Avoid overwrite — if main_ir already snapshotted there, append .v2/.v3
    target_ir = base / "main_ir.a4v3"
    if target_ir.exists():
        # collisions across same iter_idx → suffix to preserve audit
        n = 2
        while (base / f"main_ir.a4v3.v{n}").exists():
            n += 1
        target_ir = base / f"main_ir.a4v3.v{n}"
    src_ir = agent_run_dir / "main_ir.a4v3"
    if src_ir.exists():
        target_ir.write_text(src_ir.read_text(encoding="utf-8"),
                              encoding="utf-8")
    # Snapshot provenance/waivers if present
    for fname in ("provenance.yaml", "waiver_token_absorption_v1.json"):
        src = agent_run_dir / fname
        dst = base / fname
        if src.exists() and not dst.exists():
            dst.write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
    # Snapshot active strategy
    if discovery_dir is not None:
        latest_strat = _latest_strategy_path(discovery_dir)
        if latest_strat is not None:
            strat_dst = base / "strategy_active.md"
            if not strat_dst.exists():
                strat_dst.write_text(latest_strat.read_text(encoding="utf-8"),
                                       encoding="utf-8")
    # Verdict snapshot if provided
    if verdict_data is not None:
        verdict_path = base / "verdict.json"
        verdict_path.write_text(
            json.dumps(verdict_data, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8")
    # Metadata
    meta_path = base / "iter_meta.json"
    existing_meta = {}
    if meta_path.exists():
        try:
            existing_meta = json.loads(meta_path.read_text(encoding="utf-8"))
        except Exception:
            existing_meta = {}
    existing_meta.update({
        "iter_idx": iter_idx,
        "kind": kind,
        "snapshotted_at": _utcnow(),
        "ir_hash": _hash_text(src_ir.read_text(encoding="utf-8"))
                   if src_ir.exists() else None,
    })
    if extra_artifacts:
        existing_meta["extra"] = extra_artifacts
    meta_path.write_text(
        json.dumps(existing_meta, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8")
    return base


def _list_iters(agent_run_dir: pathlib.Path) -> list[dict[str, Any]]:
    """List all iter_<N>/ snapshots with their metadata. Sorted by iter_idx."""
    out: list[dict[str, Any]] = []
    for d in agent_run_dir.glob("iter_*"):
        if not d.is_dir():
            continue
        m = re.match(r"iter_(\d+)$", d.name)
        if not m:
            continue
        meta_path = d / "iter_meta.json"
        meta = {}
        if meta_path.exists():
            try:
                meta = json.loads(meta_path.read_text(encoding="utf-8"))
            except Exception:
                pass
        out.append({
            "iter_idx": int(m.group(1)),
            "path": str(d.relative_to(agent_run_dir)),
            "kind": meta.get("kind"),
            "ir_hash": meta.get("ir_hash"),
            "has_verdict": (d / "verdict.json").exists(),
            "snapshotted_at": meta.get("snapshotted_at"),
        })
    out.sort(key=lambda x: x["iter_idx"])
    return out


def _do_rollback(env: ToolEnv, iter_n: int, reason: str,
                  source: str = "tool") -> dict[str, Any]:
    """Core rollback logic. Used by both tool_rollback_to_iter (agent
    invokes) and the auto-rollback path inside run_package_checks
    (system-initiated on strong regression).

    `source` ∈ {"tool", "auto"} — recorded in the rollback log so
    human reviewer can distinguish agent-driven vs auto-driven
    rollbacks.
    """
    if not reason or not reason.strip():
        return {"error": "reason is required (non-empty short string)"}
    base = env.agent_run_dir / f"iter_{iter_n}"
    if not base.exists():
        return {"error": f"iter_{iter_n} does not exist",
                "available": _list_iters(env.agent_run_dir)}
    src_ir = base / "main_ir.a4v3"
    if not src_ir.exists():
        return {"error": f"iter_{iter_n}/main_ir.a4v3 missing — cannot rollback"}

    # Save a pre-rollback snapshot so user can audit what was discarded
    pre_rb_snapshot = env.agent_run_dir / f"pre_rollback_{_utcnow().replace(':','-')}.a4v3"
    cur_ir_path = env.agent_run_dir / "main_ir.a4v3"
    if cur_ir_path.exists():
        pre_rb_snapshot.write_text(cur_ir_path.read_text(encoding="utf-8"),
                                    encoding="utf-8")

    # Restore IR
    ir_text = src_ir.read_text(encoding="utf-8")
    cur_ir_path.write_text(ir_text, encoding="utf-8")
    env.current_ir_hash = _hash_text(ir_text)

    # Restore provenance/waivers if present in iter
    restored = ["main_ir.a4v3"]
    for fname in ("provenance.yaml", "waiver_token_absorption_v1.json"):
        src = base / fname
        if src.exists():
            (env.agent_run_dir / fname).write_text(
                src.read_text(encoding="utf-8"), encoding="utf-8")
            restored.append(fname)

    # Reset last_verified_ir_hash to match — iter snapshot was verified at
    # iter_n, so this IR is now "verified" again. Phase: PACKAGE_DRAFTING
    # so agent can re-run package_checks if needed (and it should, to
    # re-confirm verdict on this rolled-back IR).
    env.last_verified_ir_hash = env.current_ir_hash
    env.phase = _PHASE_PACKAGE_DRAFTING
    # KDR contract context is stale after rollback (last KDR was for the
    # rolled-away IR). Clear so agent isn't blocked by drop-items that
    # were specific to the discarded attempt. A fresh run_package_checks
    # on the restored IR will populate a new KDR if needed.
    env.last_kdr_drops = []
    env.last_kdr_version = None
    env.last_kdr_ir_hash = None
    # last_check_ir_hash is stale too — strategy was checked on the
    # rolled-away IR. Force agent to re-run check_ir_vs_strategy before
    # finalize (via Fix #1 gate).
    env.last_check_ir_hash = None
    env.last_check_strong_missing = None

    # Append to rollback log artifact
    log_path = env.agent_run_dir / "rollback_log.md"
    log_entry = (
        f"\n## Rollback to iter_{iter_n} at {_utcnow()} (source={source})\n"
        f"- Reason: {reason}\n"
        f"- Pre-rollback IR snapshot saved as {pre_rb_snapshot.name}\n"
        f"- Restored: {restored}\n"
        f"- IR hash: {env.current_ir_hash}\n"
    )
    if log_path.exists():
        log_path.write_text(log_path.read_text(encoding="utf-8") + log_entry,
                              encoding="utf-8")
    else:
        log_path.write_text("# Rollback log\n" + log_entry, encoding="utf-8")

    return {
        "rolled_back_to": iter_n,
        "source": source,
        "reason": reason,
        "ir_hash": env.current_ir_hash,
        "restored_artifacts": restored,
        "pre_rollback_snapshot": pre_rb_snapshot.name,
        "rollback_log": "rollback_log.md",
        "current_phase": env.phase,
    }
