"""Iter snapshot compare + rollback tools."""
from __future__ import annotations

import re
from typing import Any

from ir_agent.env import ToolEnv
from ir_agent.helpers import _load_json
from ir_agent.snapshots import _do_rollback, _list_iters


def _parse_decls(ir_text: str) -> dict[str, dict[str, Any]]:
    """Parse top-level A4V3 declarations into a name→info map. Used by
    compare_iters to compute structural diffs.

    Recognized kinds: sort, entity, rel, fact, constraint, permission,
    obligation, prohibition. Returns {name: {kind, line_no, signature}}."""
    out: dict[str, dict[str, Any]] = {}
    decl_re = re.compile(
        r"^\s*(sort|entity|rel|fact|constraint|permission|obligation|"
        r"prohibition|fun)\s+([A-Za-z_]\w*)",
        re.MULTILINE)
    lines = ir_text.split("\n")
    for m in decl_re.finditer(ir_text):
        kind = m.group(1)
        name = m.group(2)
        line_no = ir_text[:m.start()].count("\n") + 1
        signature = lines[line_no - 1].strip() if line_no <= len(lines) else ""
        if name not in out:
            out[name] = {"kind": kind, "line_no": line_no,
                          "signature": signature}
    return out


def tool_compare_iters(env: ToolEnv, *, iter_a: int, iter_b: int
                        ) -> dict[str, Any]:
    """Compare two IR snapshots (iter_<a> vs iter_<b>) and surface what
    changed structurally + how the verdict changed."""
    base_a = env.agent_run_dir / f"iter_{iter_a}"
    base_b = env.agent_run_dir / f"iter_{iter_b}"
    if not base_a.exists():
        return {"error": f"iter_{iter_a} does not exist", "available": _list_iters(env.agent_run_dir)}
    if not base_b.exists():
        return {"error": f"iter_{iter_b} does not exist", "available": _list_iters(env.agent_run_dir)}

    ir_a = (base_a / "main_ir.a4v3").read_text(encoding="utf-8") if (base_a / "main_ir.a4v3").exists() else ""
    ir_b = (base_b / "main_ir.a4v3").read_text(encoding="utf-8") if (base_b / "main_ir.a4v3").exists() else ""
    if not ir_a or not ir_b:
        return {"error": "missing main_ir.a4v3 in one of the iters",
                "iter_a_has_ir": bool(ir_a), "iter_b_has_ir": bool(ir_b)}

    decls_a = _parse_decls(ir_a)
    decls_b = _parse_decls(ir_b)
    names_a = set(decls_a.keys())
    names_b = set(decls_b.keys())
    added = sorted(names_b - names_a)
    removed = sorted(names_a - names_b)
    common = names_a & names_b
    changed = []
    unchanged = []
    for n in sorted(common):
        if decls_a[n]["signature"] != decls_b[n]["signature"]:
            changed.append({
                "name": n,
                "kind": decls_a[n]["kind"],
                "before": decls_a[n]["signature"],
                "after": decls_b[n]["signature"],
            })
        else:
            unchanged.append(n)

    decl_summary = {
        "added": [{"name": n, "kind": decls_b[n]["kind"],
                   "signature": decls_b[n]["signature"]} for n in added],
        "removed": [{"name": n, "kind": decls_a[n]["kind"],
                     "signature": decls_a[n]["signature"]} for n in removed],
        "changed": changed,
        "n_unchanged": len(unchanged),
        "n_added": len(added),
        "n_removed": len(removed),
        "n_changed": len(changed),
        "total_a": len(decls_a),
        "total_b": len(decls_b),
    }

    verdict_a = _load_json(base_a / "verdict.json") or {}
    verdict_b = _load_json(base_b / "verdict.json") or {}
    verdict_summary = {}
    if verdict_a or verdict_b:
        VERDICT_RANK = {"corresponds": 0, "partially_corresponds": 1,
                        "does_not_correspond": 2}
        wa = verdict_a.get("worst_verdict")
        wb = verdict_b.get("worst_verdict")
        rank_a = VERDICT_RANK.get(wa, 99)
        rank_b = VERDICT_RANK.get(wb, 99)
        verdict_summary = {
            "iter_a_worst": wa,
            "iter_b_worst": wb,
            "iter_a_distribution": verdict_a.get("distribution"),
            "iter_b_distribution": verdict_b.get("distribution"),
            "verdict_change": (
                "improved" if rank_b < rank_a else
                "regressed" if rank_b > rank_a else
                "same"
            ),
        }
        fp_a = set(verdict_a.get("issue_fingerprint", []) or [])
        fp_b = set(verdict_b.get("issue_fingerprint", []) or [])
        verdict_summary["resolved_complaints"] = sorted(fp_a - fp_b)[:10]
        verdict_summary["new_complaints"] = sorted(fp_b - fp_a)[:10]
        verdict_summary["persistent_complaints"] = sorted(fp_a & fp_b)[:10]

    recommendation = ""
    if verdict_summary.get("verdict_change") == "regressed":
        recommendation = (
            f"iter_{iter_b} is WORSE than iter_{iter_a}. Strongly consider "
            f"rollback_to_iter({iter_a}) and applying targeted fixes to "
            f"only the persistent_complaints, NOT a full rewrite."
        )
    elif verdict_summary.get("verdict_change") == "improved":
        recommendation = (
            f"iter_{iter_b} is BETTER than iter_{iter_a}. No rollback "
            f"needed. New complaints (if any) are now the targets to fix "
            f"on top of iter_{iter_b}."
        )
    elif decl_summary["n_removed"] > decl_summary["n_added"] + 2:
        recommendation = (
            f"iter_{iter_b} dropped {decl_summary['n_removed']} declarations "
            f"vs only adding {decl_summary['n_added']}. This is the "
            f"'oversimplification on amend' anti-pattern. Likely worse for "
            f"judges; consider rollback if verdict regressed."
        )

    out_md = env.agent_run_dir / f"compare_iter_{iter_a}_vs_{iter_b}.md"
    md_lines = [f"# Compare iter_{iter_a} vs iter_{iter_b}", ""]
    md_lines.append(f"- Verdict change: {verdict_summary.get('verdict_change', 'n/a')}")
    md_lines.append(f"- Decls in iter_a: {decl_summary['total_a']}, "
                     f"iter_b: {decl_summary['total_b']}")
    md_lines.append(f"- Added: {decl_summary['n_added']}, "
                     f"Removed: {decl_summary['n_removed']}, "
                     f"Changed: {decl_summary['n_changed']}, "
                     f"Unchanged: {decl_summary['n_unchanged']}")
    md_lines.extend(["", "## Removed declarations (lost in iter_b)", ""])
    for d in decl_summary["removed"]:
        md_lines.append(f"- `{d['signature']}`")
    md_lines.extend(["", "## Added declarations (new in iter_b)", ""])
    for d in decl_summary["added"]:
        md_lines.append(f"- `{d['signature']}`")
    md_lines.extend(["", "## Changed declarations", ""])
    for d in decl_summary["changed"]:
        md_lines.append(f"- {d['name']}:\n    before: `{d['before']}`\n    after:  `{d['after']}`")
    md_lines.extend(["", "## Recommendation", "", recommendation or "(no specific recommendation)"])
    out_md.write_text("\n".join(md_lines), encoding="utf-8")

    return {
        "iter_a": iter_a,
        "iter_b": iter_b,
        "decl_summary": decl_summary,
        "verdict_summary": verdict_summary,
        "recommendation": recommendation,
        "artifact_md": str(out_md.relative_to(env.agent_run_dir)),
    }


def tool_rollback_to_iter(env: ToolEnv, *, iter_n: int,
                            reason: str) -> dict[str, Any]:
    """Restore main_ir.a4v3 (and provenance/waivers) from iter_<N>/."""
    result = _do_rollback(env, iter_n, reason, source="tool")
    if "error" not in result:
        result["instruction"] = (
            f"IR rolled back to iter_{iter_n}. The agent_run_dir now "
            f"contains the iter_{iter_n} state. Apply MINIMAL targeted "
            f"fixes — do NOT rewrite working sections. After your fix, "
            f"re-submit_ir_for_lint, then re-run_package_checks to "
            f"confirm verdict (don't rely on the iter_{iter_n} verdict — "
            f"any change you make needs fresh verification)."
        )
    return result
