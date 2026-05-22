"""Cross-iter attempt-history analysis tool."""
from __future__ import annotations

import json
from typing import Any

from ir_agent.env import ToolEnv
from ir_agent.helpers import _strip_code_fence
from ir_agent.iter_analysis import (
    _collect_iter_history, _find_best_prior_iter, _write_iter_scoreboard,
)
from ir_agent.prompts.history import _ATTEMPT_HISTORY_SYSTEM


def tool_analyze_attempt_history(env: ToolEnv) -> dict[str, Any]:
    """Explicit cross-iter analysis: load ALL iter IRs + verdicts + per-
    judge dissent and synthesize a narrative of what worked, what
    regressed, and what to do next. Refreshes discovery/iter_scoreboard.md
    and writes discovery/attempt_history_analysis.json.

    Use when:
    - Stuck after 2+ rounds and meta_evaluate's local-fix path has
      already been tried;
    - About to call finalize but unsure whether current IR is the best
      attempt;
    - regression_hint flagged worse-than-prior but you want explicit
      reasoning before rolling back.
    """
    if env.client is None:
        return {"error": "intra-tool LLM client not configured"}
    if not env.verify_history:
        return {
            "error": "no_verify_history: analyze_attempt_history needs at "
                     "least one run_package_checks before it has data.",
            "instruction": "Call run_package_checks() first.",
        }

    # Refresh scoreboard so persisted artifact is current
    try:
        _write_iter_scoreboard(env)
    except Exception:
        pass

    iters = _collect_iter_history(env, include_ir_text=True)
    iters_verified = [it for it in iters if it.get("worst_verdict")]
    if not iters_verified:
        return {
            "error": "no verified iters found — iter snapshots exist but "
                     "none have a verdict.json",
        }

    best = _find_best_prior_iter(env)

    # Compact LLM payload: per-iter {iter, round, tier, distribution,
    # dissent[≤2], ir_text (truncated)}
    compact = []
    for it in iters_verified:
        compact.append({
            "iter": it["iter_idx"],
            "round": it.get("round"),
            "tier": it["quality_tier"],
            "distribution": it["distribution"],
            "agreement": it.get("agreement"),
            "ir_excerpt": (it.get("ir_text") or "")[:1800],
            "declaration_names": it.get("declaration_names", []),
            "judge_dissent": [
                {
                    "model": d.get("model"),
                    "verdict": d.get("verdict"),
                    "specific_differences": (d.get("semantic_differences") or [])[:2],
                }
                for d in (it.get("judge_dissent") or [])[:5]
            ],
        })

    best_meta = None
    if best is not None:
        best_meta = {
            "iter": best["iter_idx"],
            "tier": best["quality_tier"],
            "distribution": best["distribution"],
        }

    user = (
        f"## ITERS (each = one IR attempt + judge verdict)\n\n"
        f"```json\n{json.dumps(compact, indent=2, ensure_ascii=False)[:14000]}\n```\n\n"
        f"## BEST ITER (highest quality_tier so far)\n\n"
        f"```json\n{json.dumps(best_meta, indent=2, ensure_ascii=False)}\n```\n\n"
        f"## YOUR TASK\n\n"
        f"Produce the attempt-history analysis JSON per the schema. Cross-"
        f"reference declarations across iters: identify the proven_core "
        f"(declarations in every accept_with_dissent+ iter), the specific "
        f"regression-causing changes, and the open_dissent patterns. "
        f"Make recommended_next_action a concrete decision the agent can "
        f"act on. Use only declaration names that appear in the IR excerpts."
    )

    _client, _xb, _mt = env.strategic_or_main(4500)
    try:
        result = _client.complete(
            [],
            raw_messages=[{"role": "system", "content": _ATTEMPT_HISTORY_SYSTEM},
                          {"role": "user", "content": user}],
            max_tokens=_mt,
            extra_body=_xb,
            seed=env.seed,
        )
    except Exception as exc:
        return {"error": f"{type(exc).__name__}: {exc}"}

    raw = _strip_code_fence(result.text or "")
    try:
        parsed = json.loads(raw)
    except Exception as exc:
        return {"error": f"analyze_attempt_history returned non-JSON: {exc}",
                "raw_excerpt": raw[:500]}

    out_path = env.discovery_dir / "attempt_history_analysis.json"
    out_path.write_text(json.dumps(parsed, indent=2, ensure_ascii=False) + "\n",
                         encoding="utf-8")

    # Human-readable .md
    md_lines = [f"# Attempt history analysis — {env.original_entry_id}", ""]
    md_lines.append(f"**Best iter:** iter_{parsed.get('best_iter','?')}")
    md_lines.append(f"**Why it worked:** {parsed.get('best_iter_why_it_worked','')}")
    md_lines.append(f"**Residual dissent in best:** "
                     f"{parsed.get('best_iter_residual_dissent','')}")
    md_lines.append("")
    md_lines.append(f"**Recommended action:** "
                     f"`{parsed.get('recommended_next_action','?')}`")
    md_lines.append(f"**Rationale:** "
                     f"{parsed.get('recommended_next_action_rationale','')}")
    md_lines.append("")
    if parsed.get("proven_core"):
        md_lines.append("## Proven core (in every good iter)")
        for d in parsed["proven_core"]:
            md_lines.append(f"- `{d}`")
        md_lines.append("")
    if parsed.get("regressions"):
        md_lines.append("## Regressions")
        for r in parsed["regressions"]:
            md_lines.append(
                f"- iter_{r.get('from_iter')} → iter_{r.get('to_iter')}: "
                f"{r.get('hypothesized_cause','')}")
        md_lines.append("")
    if parsed.get("improvements"):
        md_lines.append("## Improvements")
        for r in parsed["improvements"]:
            md_lines.append(
                f"- iter_{r.get('from_iter')} → iter_{r.get('to_iter')}: "
                f"{r.get('hypothesized_cause','')}")
        md_lines.append("")
    if parsed.get("open_dissent"):
        md_lines.append("## Open dissent (persistent complaints)")
        for od in parsed["open_dissent"]:
            md_lines.append(
                f"- **{od.get('judge_model')}** "
                f"(iters {od.get('iters_where_present')}): "
                f"{od.get('persistent_complaint','')}")
            md_lines.append(
                f"    addressed in iter: {od.get('addressed_in_iter')}, "
                f"fix attempted: {od.get('fix_attempted','')}")
        md_lines.append("")
    if parsed.get("constructive_synthesis"):
        md_lines.append("## Constructive synthesis (concrete patch plan)")
        md_lines.append(parsed["constructive_synthesis"])
        md_lines.append("")
    md_path = env.discovery_dir / "attempt_history_analysis.md"
    md_path.write_text("\n".join(md_lines), encoding="utf-8")

    return {
        "best_iter": parsed.get("best_iter"),
        "best_iter_tier": (best.get("quality_tier") if best else None),
        "recommended_next_action": parsed.get("recommended_next_action"),
        "rationale": parsed.get("recommended_next_action_rationale"),
        "n_proven_core": len(parsed.get("proven_core") or []),
        "n_regressions": len(parsed.get("regressions") or []),
        "n_improvements": len(parsed.get("improvements") or []),
        "n_open_dissent": len(parsed.get("open_dissent") or []),
        "constructive_synthesis": parsed.get("constructive_synthesis"),
        "artifact_md": str(md_path.relative_to(env.agent_run_dir)),
        "scoreboard": "discovery/iter_scoreboard.md",
    }
