"""Meta-evaluator, parallel critique, and finalize tools."""
from __future__ import annotations

import json
import pathlib
import re
import sys
from typing import Any

from ir_agent.config import MAX_META_EVALUATIONS, SRC
from ir_agent.env import ToolEnv
from ir_agent.helpers import (
    _load_json, _read_text, _strip_code_fence, _utcnow,
)
from ir_agent.iter_analysis import (
    _TIER_RANK, _find_best_prior_iter, _quality_tier,
)
from ir_agent.parts_inventory import evaluate_inventory_coverage, ensure_parts_inventory
from ir_agent.phases import _PHASE_FINALIZED, _PHASE_IR_IN_FLUX
from ir_agent.prompts.meta import _META_EVAL_SYSTEM
from ir_agent.snapshots import _list_iters
from ir_agent.strategy_io import _write_strategy_from_meta


def tool_meta_evaluate(env: ToolEnv) -> dict[str, Any]:
    """Step out of the local repair loop. Show full verify history + current
    IR + text-intent + classifier output to LLM, ask for RADICAL alternative
    architecture. Hard cap: MAX_META_EVALUATIONS attempts."""
    if env.client is None:
        return {"error": "intra-tool LLM client not configured"}
    if env.meta_evaluations_done >= MAX_META_EVALUATIONS:
        return {
            "error": f"max_meta_evaluations_reached: already done {env.meta_evaluations_done} of {MAX_META_EVALUATIONS}",
            "instruction": (
                "The architectural search has saturated. Multiple radical "
                "refactors have not converged judges to corresponds. The "
                "current IR is your best attempt. Call "
                "finalize(decision='failed_after_meta', summary=<honest "
                "explanation of remaining dissent>) — partial work is more "
                "honest than another speculative refactor."
            ),
        }
    if not env.verify_history:
        return {
            "error": "no_verify_history: meta_evaluate has no evidence to work from",
            "instruction": (
                "meta_evaluate is for stepping out of a STAGNANT verify loop "
                "(2+ rounds with same dissent). It needs verify history as "
                "input. If you have NOT run run_package_checks yet, that is "
                "the next step — not meta_evaluate. Call run_package_checks() "
                "to get judges' verdict; if it shows persistent dissent that "
                "amend_strategy can't resolve, then call meta_evaluate."
            ),
            "verify_history_size": 0,
        }

    source = _read_text(env.section_dir / "source.md")
    current_ir = _read_text(env.agent_run_dir / "main_ir.a4v3")
    intent = _load_json(env.discovery_dir / "text_intent_classification.json")

    history_summary = json.dumps([
        {
            "round": h["round"],
            "worst_verdict": h["worst_verdict"],
            "distribution": h["distribution"],
            "judge_dissent": [
                {
                    "model": d.get("model"),
                    "verdict": d.get("verdict"),
                    "reason_short": d.get("reason_short", "")[:300],
                    "semantic_differences": d.get("semantic_differences", [])[:3],
                }
                for d in h.get("judge_dissent", [])
            ],
        }
        for h in env.verify_history
    ], indent=2, ensure_ascii=False)

    iter_history = _list_iters(env.agent_run_dir)
    iter_history_with_verdicts = []
    for it in iter_history:
        verdict = _load_json(env.agent_run_dir / it["path"] / "verdict.json") or {}
        iter_history_with_verdicts.append({
            "iter_idx": it["iter_idx"],
            "kind": it["kind"],
            "ir_hash": it["ir_hash"],
            "worst_verdict": verdict.get("worst_verdict"),
            "distribution": verdict.get("distribution"),
        })

    user = (
        f"## SECTION SOURCE\n\n{source}\n\n"
        f"## TEXT INTENT CLASSIFICATION\n\n"
        + (json.dumps(intent, indent=2, ensure_ascii=False) if intent else "[not classified]")
        + f"\n\n## CURRENT IR (last submission)\n\n```\n{current_ir}\n```\n\n"
        + f"## ITER SNAPSHOTS (each entry is a verified IR + its verdict)\n\n"
        + f"```json\n{json.dumps(iter_history_with_verdicts, indent=2, ensure_ascii=False)}\n```\n\n"
        + "If one of these iters has a strictly better worst_verdict than "
          "current AND a higher corresponds count, that's a strong "
          "ROLLBACK_CANDIDATE — name it in rollback_target_iter.\n\n"
        f"## FULL VERIFY HISTORY ({len(env.verify_history)} rounds)\n\n"
        f"{history_summary}\n\n"
        "Diagnose the ROOT cause and propose a RADICAL alternative."
    )

    _client, _xb, _mt = env.strategic_or_main(4096)
    try:
        result = _client.complete(
            [],
            raw_messages=[{"role": "system", "content": _META_EVAL_SYSTEM},
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
        return {"error": f"meta_evaluate returned non-JSON: {exc}",
                "raw_excerpt": raw[:600]}

    valid_stages = {"SCOUT", "PLAN", "BUILD", "INSPECT", "ROLLBACK_CANDIDATE"}
    valid_actions = {"re_analyze_role_frame", "amend_strategy_targeted",
                     "re_submit_ir_with_specific_changes",
                     "rollback_to_iter_then_patch", "finalize_with_dissent"}
    failed_stage = parsed.get("failed_stage", "BUILD")
    if failed_stage not in valid_stages:
        parsed["_warning_invalid_failed_stage"] = (
            f"got {failed_stage!r}, expected one of {sorted(valid_stages)}; "
            f"defaulting to BUILD")
        failed_stage = "BUILD"
        parsed["failed_stage"] = failed_stage
    rec_action = parsed.get("recommended_action", "re_submit_ir_with_specific_changes")
    if rec_action not in valid_actions:
        parsed["_warning_invalid_action"] = (
            f"got {rec_action!r}, expected one of {sorted(valid_actions)}; "
            f"defaulting to re_submit_ir_with_specific_changes")
        rec_action = "re_submit_ir_with_specific_changes"
        parsed["recommended_action"] = rec_action

    rollback_target = parsed.get("rollback_target_iter")
    if rollback_target is not None:
        existing_iters = {it["iter_idx"] for it in _list_iters(env.agent_run_dir)}
        if rollback_target not in existing_iters:
            parsed["_warning_invalid_rollback_target"] = (
                f"iter_{rollback_target} does not exist; clearing")
            rollback_target = None
            parsed["rollback_target_iter"] = None

    env.meta_evaluations_done += 1
    env.meta_required = False
    env.meta_required_reason = ""
    env.phase = _PHASE_IR_IN_FLUX

    out_path = env.discovery_dir / f"meta_evaluation_{env.meta_evaluations_done}.json"
    out_path.write_text(json.dumps(parsed, indent=2, ensure_ascii=False) + "\n",
                        encoding="utf-8")

    strategy_write_result = None
    if rec_action != "rollback_to_iter_then_patch":
        strategy_write_result = _write_strategy_from_meta(env, parsed)
        parsed["_strategy_auto_written"] = strategy_write_result

    if rec_action == "rollback_to_iter_then_patch" and rollback_target is not None:
        parsed["_instruction"] = (
            f"Meta diagnosis: stage={failed_stage}. Recommended action: "
            f"rollback_to_iter({rollback_target}) THEN apply targeted patch. "
            f"Call rollback_to_iter(iter_n={rollback_target}, "
            f"reason='meta diagnosis: <stage_diagnosis>'). After rollback, "
            f"submit_ir_for_lint with ONLY the targeted change "
            f"(see specific_changes), then run_package_checks. Do NOT "
            f"rewrite the whole IR — preserve the rolled-back baseline."
        )
    elif rec_action == "re_analyze_role_frame":
        parsed["_instruction"] = (
            f"Meta diagnosis: stage=SCOUT (role_frame was wrong). "
            f"Call re_analyze_role_frame to revise family/roles based on "
            f"verify findings, then compose_strategy/amend_strategy, then "
            f"submit_ir_for_lint."
        )
    elif rec_action == "amend_strategy_targeted":
        path = strategy_write_result.get('path') if strategy_write_result else 'discovery/strategy_v?.md'
        parsed["_instruction"] = (
            f"Meta diagnosis: stage=PLAN (strategy was wrong). New strategy "
            f"version auto-written: {path}. Re-read it, then "
            f"submit_ir_for_lint following the revised strategy."
        )
    elif rec_action == "finalize_with_dissent":
        parsed["_instruction"] = (
            f"Meta diagnosis: stage=INSPECT (judges disagree but IR is OK). "
            f"Call finalize(decision='agent_accept_candidate_with_dissent', "
            f"summary=<honest description>). The dissent is structural and "
            f"local fixes won't change it."
        )
    else:
        path = strategy_write_result.get('path') if strategy_write_result else 'discovery/strategy_v?.md'
        parsed["_instruction"] = (
            f"Meta diagnosis: stage={failed_stage}. New strategy version: "
            f"{path}. Submit ONE new IR draft implementing the specific "
            f"changes. Do NOT revert to prior structure cosmetically. If "
            f"this attempt also fails, consider rollback or finalize."
        )
    parsed["meta_evaluations_done"] = env.meta_evaluations_done
    return parsed


def tool_parallel_critique(env: ToolEnv) -> dict[str, Any]:
    """Run 5 specialist critics in parallel against the current IR.
    Cross-vendor for diversity."""
    if "ir" not in env.submissions:
        return {"error": "submit_ir_for_lint must be called first"}
    ir_text = _read_text(env.agent_run_dir / "main_ir.a4v3")
    source_text = _read_text(env.section_dir / "source.md")
    intent = _load_json(env.discovery_dir / "text_intent_classification.json")
    try:
        sys.path.insert(0, str(SRC))
        import critic_swarm_v1
        result = critic_swarm_v1.run_swarm(ir_text, source_text, intent,
                                            seed=env.seed)
    except Exception as exc:
        return {"error": f"{type(exc).__name__}: {exc}"}
    (env.agent_run_dir / "critic_swarm_v1.json").write_text(
        json.dumps(result, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8")
    return result


def tool_finalize(env: ToolEnv, *, decision: str, summary: str,
                  notes: str | None = None) -> dict[str, Any]:
    """End the loop with a triage decision."""
    valid = {"agent_accept_candidate",
             "agent_accept_candidate_with_dissent",
             "needs_human_review", "failed_after_meta"}
    if decision not in valid:
        return {"error": f"decision must be one of {sorted(valid)}"}
    if not env.verify_history and decision != "failed_after_meta":
        return {
            "error": (
                "no_verify_history: finalize requires at least one "
                "successful run_package_checks before declaring a triage "
                "decision. The decision would describe an unjudged IR."
            ),
            "instruction": (
                "Call run_package_checks() first to get judges' verdict + "
                "deterministic-check report, THEN finalize. If the IR gate "
                "never cleared (lint_strong > 0 or family_blocking > 0), "
                "the only legitimate finalize decision is "
                "'failed_after_meta' with a summary explaining the blocker."
            ),
        }
    if decision == "failed_after_meta":
        actionable_phrases = [
            "i need to", "the fix is", "should use", "should be",
            "use entities", "use concrete", "concrete entity instances",
            "needs to be", "needs to declare", "missing fields",
            "missing field", "must be", "structural simplification",
            "needs a more canonical", "needs different modeling",
            "the remaining issue", "still passing sorts",
            "could be fixed", "would need to", "i should",
            "one more structural", "one final iteration",
        ]
        haystack = ((summary or "") + " " + (notes or "")).lower()
        matched = [p for p in actionable_phrases if p in haystack]
        if matched:
            return {
                "error": (
                    "failed_after_meta_with_actionable_plan: your summary/"
                    "notes describe a concrete fix you understand. "
                    "failed_after_meta is reserved for cases where you "
                    "genuinely DO NOT KNOW how to proceed. You wrote "
                    f"actionable phrases: {matched[:3]}. Apply that fix "
                    f"via submit_ir_for_lint, then re-VERIFY, then "
                    f"finalize with an honest decision (probably "
                    f"agent_accept_candidate_with_dissent or "
                    f"needs_human_review). Do not use failed_after_meta "
                    f"as an escape hatch."
                ),
                "matched_actionable_phrases": matched,
                "instruction": (
                    "Re-read your last reasoning. Identify the specific "
                    "change you described (e.g. 'declare entities for "
                    "recipient categories'). Implement it via a new "
                    "submit_ir_for_lint call. If the fix actually does "
                    "not work after applying, you can finalize as "
                    "failed_after_meta — but only after trying."
                ),
            }
    # Best-prior gate: if some earlier iter had a strictly better triage
    # tier than the current verify result, refuse and hint at rollback.
    # Bypass only when decision is failed_after_meta (acknowledged dead-end)
    # or accept_with_dissent (agent explicitly choosing dissent path on
    # current quality). Never block agent_accept_candidate or worse-than-
    # current decisions that already match reality.
    if env.verify_history and decision in {"needs_human_review",
                                            "agent_accept_candidate_with_dissent"}:
        latest = env.verify_history[-1]
        current_tier = _quality_tier(latest)
        best = _find_best_prior_iter(env, exclude_current_hash=latest.get("ir_hash"))
        if (best is not None
                and _TIER_RANK[best["quality_tier"]] > _TIER_RANK[current_tier]):
            return {
                "error": (
                    "best_prior_iter_better_than_current: an earlier iter "
                    "had a stronger triage tier than the current verify "
                    "result. Finalize would lock in a worse outcome than "
                    "you already produced."
                ),
                "current_quality": {
                    "tier": current_tier,
                    "round": latest.get("round"),
                    "distribution": latest.get("distribution"),
                    "worst_verdict": latest.get("worst_verdict"),
                    "agreement": latest.get("distribution")
                                  and round(max(latest["distribution"].values())
                                            / sum(latest["distribution"].values()), 2),
                },
                "best_prior": {
                    "iter_idx": best["iter_idx"],
                    "tier": best["quality_tier"],
                    "round": best.get("round"),
                    "distribution": best["distribution"],
                    "worst_verdict": best["worst_verdict"],
                    "agreement": best.get("agreement"),
                },
                "instruction": (
                    f"Call rollback_to_iter(iter_n={best['iter_idx']}, "
                    f"reason='best prior verdict, current regressed') — this "
                    f"restores main_ir/provenance/waivers from iter_"
                    f"{best['iter_idx']}. Then re-run run_package_checks to "
                    f"re-confirm the verdict on the rolled-back IR (gate "
                    f"requires current_ir_hash == last_verified_ir_hash). "
                    f"Then call finalize again — it will succeed because the "
                    f"current verify result will equal the best prior. "
                    f"Read discovery/iter_scoreboard.md for the full "
                    f"per-iter quality breakdown."
                ),
            }

    # Mandatory fresh strategy-check: agent often re-submits IR many times
    # after the last check_ir_vs_strategy and finalizes on stale assurance.
    # Refuse finalize unless the most recent check matches the current IR
    # hash. Bypass for failed_after_meta (acknowledged dead-end). Bypass
    # when no check has ever run yet (env.last_check_ir_hash is None) AND
    # decision is failed_after_meta — but for all other decisions, require
    # at least one fresh check.
    if (decision != "failed_after_meta"
            and env.current_ir_hash is not None
            and env.last_check_ir_hash != env.current_ir_hash):
        return {
            "error": (
                "stale_strategy_check: the most recent check_ir_vs_strategy "
                "was on a DIFFERENT IR hash than the current main_ir.a4v3. "
                "Finalize would lock in a verdict on an IR whose conformance "
                "to the strategy was never re-confirmed after the last edit."
            ),
            "current_ir_hash": env.current_ir_hash,
            "last_check_ir_hash": env.last_check_ir_hash,
            "instruction": (
                "Call check_ir_vs_strategy() to re-verify the current IR "
                "realises the latest strategy. If n_missing_strong == 0, "
                "you may then finalize. If n_missing_strong > 0, either "
                "re-submit_ir_for_lint with the missing items added OR "
                "(after 2 such drifts) call amend_strategy to revise the "
                "strategy itself."
            ),
        }

    if env.current_ir_hash is not None and env.last_verified_ir_hash is not None:
        if env.current_ir_hash != env.last_verified_ir_hash:
            return {
                "error": (
                    "ir_changed_since_last_verify: the IR on disk has changed "
                    "since the most recent run_package_checks. The triage "
                    "would describe a stale verdict. Run run_package_checks "
                    "again on the current IR before finalizing."
                ),
                "current_ir_hash": env.current_ir_hash,
                "last_verified_ir_hash": env.last_verified_ir_hash,
                "instruction": (
                    "Call run_package_checks() to verify the latest IR, then "
                    "finalize. If the new verify result is much worse than "
                    "the previous one, you may revert by re-submitting the "
                    "previously-verified IR (the one whose hash matches "
                    "last_verified_ir_hash) and re-running package_checks."
                ),
            }
    if decision in {"agent_accept_candidate",
                    "agent_accept_candidate_with_dissent"}:
        ir_text = _read_text(env.agent_run_dir / "main_ir.a4v3")
        inventory = ensure_parts_inventory(env)
        coverage = evaluate_inventory_coverage(env, ir_text, inventory)
        env.last_parts_unsatisfied_count = (
            coverage.get("unsatisfied_required_count") or 0
        )
        env.last_parts_ir_hash = env.current_ir_hash
        if env.last_parts_unsatisfied_count > 0:
            return {
                "error": (
                    "parts_inventory_unsatisfied: finalize acceptance is "
                    "blocked because required source/role parts are not "
                    "formalized, bridged, repaired, or waived."
                ),
                "unsatisfied_required_count": env.last_parts_unsatisfied_count,
                "artifact_md": "parts_inventory_coverage_v1.md",
                "instruction": (
                    "Open parts_inventory_coverage_v1.md. Re-submit IR with "
                    "the missing required cards formalized, or add a bridge/"
                    "repair/waiver artifact and re-run check_ir_vs_strategy "
                    "and run_package_checks before finalizing."
                ),
            }
    env.finalized = {"decision": decision, "summary": summary, "notes": notes,
                     "finalized_at": _utcnow()}
    env.phase = _PHASE_FINALIZED

    # Reconciliation is written later by triage, after deterministic
    # recent check_ir_vs_strategy reported drift, the strategy is the
    # one that's wrong — not the IR. Write a reconciliation memo so the
    # accepted IR's shape is documented, and the stale strategy is
    # explicitly superseded. No LLM call; pure file synthesis.
    return {
        "finalized": True,
        "decision": decision,
        "current_phase": env.phase,
        "strategy_reconciliation": "deferred_until_triage_final_decision",
    }


def _write_strategy_reconciliation(env: ToolEnv, decision: str
                                     ) -> dict[str, Any] | None:
    """When IR was accepted by judges but check_ir_vs_strategy reported
    drift, write a deterministic memo documenting that the strategy is
    superseded by the accepted IR. Returns summary dict or None when no
    drift was detected (nothing to reconcile)."""
    checks = sorted(env.agent_run_dir.glob("ir_vs_strategy_check_v*.json"),
                    key=lambda p: int(re.search(r"_v(\d+)\.", p.name).group(1))
                                  if re.search(r"_v(\d+)\.", p.name) else -1)
    if not checks:
        return None
    last_check_path = checks[-1]
    try:
        check = json.loads(last_check_path.read_text(encoding="utf-8"))
    except Exception:
        return None
    verdict = (check.get("verdict") or "").lower()
    if "drift" not in verdict and verdict not in {"major_drift",
                                                    "partial_drift",
                                                    "minor_drift"}:
        # No drift to reconcile.
        return {"reconciled": False, "verdict": verdict,
                "note": "no drift detected by last check_ir_vs_strategy; "
                        "nothing to reconcile"}

    # Find the strategy version the check was made against.
    strategies = sorted(env.discovery_dir.glob("strategy_v*.md"),
                        key=lambda p: int(re.search(r"_v(\d+)\.", p.name).group(1))
                                      if re.search(r"_v(\d+)\.", p.name) else -1)
    latest_strategy_name = strategies[-1].name if strategies else "(none)"

    latest_verify = env.verify_history[-1] if env.verify_history else {}
    distribution = latest_verify.get("distribution") or {}
    dissent_short = []
    for d in latest_verify.get("judge_dissent") or []:
        dissent_short.append(
            f"{d.get('model','?')}: {d.get('verdict','?')} — "
            f"{(d.get('semantic_differences') or [''])[0][:200]}"
        )

    md_lines = [
        "# Strategy reconciliation memo",
        "",
        f"Decision: **{decision}**",
        f"Reconciled against: `{last_check_path.name}` (verdict: `{verdict}`)",
        f"Strategy version checked: `{latest_strategy_name}`",
        "",
        "## Why reconciliation",
        "",
        f"The judge panel accepted the IR (distribution: {distribution}), "
        f"but `check_ir_vs_strategy` reports drift between the strategy "
        f"and the accepted IR. Per pipeline contract, judge consensus "
        f"trumps strategy when they conflict — strategy is superseded by "
        f"the accepted IR shape.",
        "",
        "## What the check flagged",
        "",
        "```",
        (check.get("summary") or "(no summary in check artifact)")[:1500],
        "```",
        "",
        "## Items the IR added beyond strategy (`extra_in_ir`)",
        "",
    ]
    for item in (check.get("extra_in_ir") or [])[:20]:
        if isinstance(item, dict):
            md_lines.append(f"- {item.get('item','?')}")
        else:
            md_lines.append(f"- {item}")
    md_lines.append("")
    md_lines.append("## Items the strategy asked for but IR omitted (`missing_from_ir`)")
    md_lines.append("")
    for item in (check.get("missing_from_ir") or [])[:20]:
        if isinstance(item, dict):
            md_lines.append(f"- {item.get('item','?')}")
        else:
            md_lines.append(f"- {item}")
    md_lines.extend([
        "",
        "## Dissent on the accepted IR",
        "",
        (
            "\n".join(f"- {d}" for d in dissent_short)
            if dissent_short else "(no dissenters — all judges agreed corresponds)"
        ),
        "",
        "## Outcome",
        "",
        f"The strategy file `{latest_strategy_name}` is hereby marked "
        f"**superseded by the accepted IR**. Any KDR memo whose drop "
        f"items would have removed constructs the judges accepted (see "
        f"`extra_in_ir` above) was a **wrong hypothesis** and should not "
        f"be re-applied to this section. Future re-runs that use this "
        f"strategy as a precedent should regenerate the strategy from "
        f"the accepted IR's shape, not from `{latest_strategy_name}`.",
        "",
        f"_Auto-generated by `_write_strategy_reconciliation` at "
        f"{_utcnow()}._",
        "",
    ])

    out_path = env.agent_run_dir / "strategy_reconciliation.md"
    out_path.write_text("\n".join(md_lines), encoding="utf-8")
    return {
        "reconciled": True,
        "verdict": verdict,
        "check_artifact": last_check_path.name,
        "strategy_checked": latest_strategy_name,
        "extra_in_ir_count": len(check.get("extra_in_ir") or []),
        "missing_from_ir_count": len(check.get("missing_from_ir") or []),
        "reconciliation_memo": out_path.name,
    }
