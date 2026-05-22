"""Provenance / waivers / package-checks tools + KDR memo generator."""
from __future__ import annotations

import json
import sys
from typing import Any

from ir_agent.config import AGENT_VERSION, PYTHON, SRC
from ir_agent.env import ToolEnv
from ir_agent.helpers import (
    _hash_text, _load_json, _read_text, _run_subprocess, _strip_code_fence,
    _truncate,
)
from ir_agent.iter_analysis import (
    _collect_iter_history, _find_best_prior_iter, _write_iter_scoreboard,
)
from ir_agent.parts_inventory import (
    ensure_parts_inventory,
    evaluate_inventory_coverage,
    ingest_kdr_cards,
    write_inventory,
)
from ir_agent.phases import (
    _PHASE_META_REQUIRED, _PHASE_PACKAGE_DRAFTING, _PHASE_VERIFYING,
)
from ir_agent.prompts.kdr import _KDR_MEMO_SYSTEM
from ir_agent.snapshots import _do_rollback, _list_iters, _snapshot_iter

MAX_META_EVALUATIONS = 2


def tool_submit_provenance(env: ToolEnv, *, yaml_text: str) -> dict[str, Any]:
    if not yaml_text.strip():
        return {"error": "empty provenance"}
    if env.phase not in {_PHASE_PACKAGE_DRAFTING, _PHASE_VERIFYING}:
        return {
            "error": f"phase_gate: cannot submit_provenance in phase={env.phase}",
            "current_phase": env.phase,
            "instruction": (
                "Provenance documents the FINALIZED IR. You must first reach "
                "PACKAGE_DRAFTING phase. Call submit_ir_for_lint until "
                "ir_clean=true (lint_strong=0 + family/lowering OK after "
                "intent override). Then submit_provenance is allowed."
            ),
        }
    if (env.last_check_strong_missing is not None
            and env.last_check_strong_missing > 0
            and env.last_check_ir_hash == env.current_ir_hash):
        return {
            "error": "ir_vs_strategy_drift_unresolved: latest check_ir_vs_strategy reports n_missing_strong > 0; cannot advance to provenance",
            "n_missing_strong": env.last_check_strong_missing,
            "instruction": (
                f"check_ir_vs_strategy found "
                f"{env.last_check_strong_missing} strong-severity missing "
                f"item(s) on the CURRENT IR. The strategy explicitly "
                f"commits to these constructs — skipping to provenance "
                f"would document an IR that doesn't realise the strategy. "
                f"Two paths forward:\n"
                f"  (a) Re-submit_ir_for_lint with the missing items added "
                f"(see check artifact `ir_vs_strategy_check_v*.md` for "
                f"each missing_strong item's `fix:` instruction). Then "
                f"re-run check_ir_vs_strategy → if can_proceed=true → "
                f"submit_provenance.\n"
                f"  (b) If the missing items genuinely can't be expressed "
                f"in valid A4V3 syntax (rare — confirm by reading "
                f"get_a4v3_family + the check_ir_vs_strategy.md report), "
                f"call amend_strategy to remove the unrealizable "
                f"commitment from the strategy. amend_strategy is "
                f"normally gated on verify_history but UNLOCKS pre-verify "
                f"after 2 check_ir_vs_strategy artifacts with "
                f"strong_missing > 0 (so multiple failed IR attempts "
                f"signal that strategy itself is at fault). After amend "
                f"→ re-check → if can_proceed → submit_provenance.\n"
                f"Do NOT advance to provenance with strong drift "
                f"unresolved — that produces a triage decision that "
                f"misrepresents the actual state."
            ),
        }
    ir_text = _read_text(env.agent_run_dir / "main_ir.a4v3")
    if ir_text:
        inventory = ensure_parts_inventory(env)
        coverage = evaluate_inventory_coverage(env, ir_text, inventory)
        env.last_parts_unsatisfied_count = coverage.get("unsatisfied_required_count") or 0
        env.last_parts_ir_hash = env.current_ir_hash
        if env.last_parts_unsatisfied_count > 0:
            return {
                "error": "parts_inventory_drift_unresolved: required source/role parts are not formalized; cannot advance to provenance",
                "unsatisfied_required_count": env.last_parts_unsatisfied_count,
                "artifact_md": "parts_inventory_coverage_v1.md",
                "instruction": (
                    "Open parts_inventory_coverage_v1.md. Each required "
                    "card must be formalized in IR, or explicitly handled "
                    "through bridge, repair, or waiver with an artifact. "
                    "Judges cannot override this deterministic blocker."
                ),
            }
    yaml_text = _strip_code_fence(yaml_text)
    if "human_approved" in yaml_text:
        yaml_text = yaml_text.replace("human_approved", "agent_drafted")
    (env.agent_run_dir / "provenance.yaml").write_text(yaml_text, encoding="utf-8")

    provenance_lint_res = _run_subprocess(
        [PYTHON, str(SRC / "provenance_lint_v1.py"), str(env.agent_run_dir)],
        timeout_s=120,
    )
    provenance_lint = _load_json(env.agent_run_dir / "provenance_lint_v1.json")
    provenance_lint_summary = provenance_lint.get("summary", {})
    provenance_lint_strong = provenance_lint_summary.get("strong_findings") or 0
    if provenance_lint_res.get("returncode") != 0 or provenance_lint_strong > 0:
        lint_md = _truncate(
            _read_text(env.agent_run_dir / "provenance_lint_v1.md"),
            3000,
        )
        return {
            "error": "provenance_lint_failed",
            "current_phase": env.phase,
            "provenance_lint_returncode": provenance_lint_res.get("returncode"),
            "strong_findings": provenance_lint_strong,
            "summary": provenance_lint_summary,
            "report_excerpt": lint_md,
            "instruction": (
                "Fix provenance.yaml before continuing. Common causes: "
                "unquoted `ir_element` strings containing ':'; CamelCase IR "
                "identifiers leaking into back_translation; or source_only "
                "vocabulary fields that reuse IR identifiers. Re-submit "
                "provenance after fixing the YAML/lint findings."
            ),
        }

    # Grounding gate: every IR sort/symbol/entity must be either source-
    # traceable (name overlap with source tokens), in prelude/canonical
    # overlay, OR documented in this provenance.yaml under
    # `vocabulary_notes:` (dict form). Refuse submission if any names
    # remain ungrounded — this closes the loop where the agent's ungrounded
    # names only blocked at run_package_checks (after $0.50 of LLM judges).
    try:
        sys.path.insert(0, str(SRC))
        import extended_grounding_check_v1 as _eg
        _g = _eg.check_entry(env.agent_run_dir)
        ung_sorts = _g["ungrounded"]["sorts"]
        ung_syms = _g["ungrounded"]["symbols"]
        ung_ents = _g["ungrounded"]["entities"]
        if ung_sorts or ung_syms or ung_ents:
            return {
                "error": "ungrounded_names_in_ir: provenance does not "
                         "ground every IR sort/symbol/entity name.",
                "ungrounded_sorts": ung_sorts,
                "ungrounded_symbols": ung_syms,
                "ungrounded_entities": ung_ents,
                "current_phase": env.phase,
                "instruction": (
                    "Each ungrounded name must be EITHER:\n"
                    "  (a) RENAMED in the IR to use a source-text token "
                    "(re-submit_ir_for_lint with renamed declarations). "
                    "Example: 'LicenseRecipient' is ungrounded because "
                    "'recipient' is not a source word — canonical convention "
                    "uses 'LicenseRecipientCategory' (the 'Category' suffix "
                    "is grounded as an enum-of-categories).\n"
                    "  (b) DOCUMENTED in this provenance.yaml under a "
                    "top-level `vocabulary_notes:` key — DICT form (NOT a "
                    "list, and NOT inside `sorts:`). Each entry is keyed by "
                    "the IR identifier, value is `{note: <why this name>, "
                    "source_phrase: <verbatim source phrase>}`. Example:\n\n"
                    "    vocabulary_notes:\n"
                    "      License:\n"
                    "        note: 'Generic license carrier grounded by source phrase \"Licenses\".'\n"
                    "        source_phrase: 'Licenses'\n"
                    "      LicenseRecipientCategory:\n"
                    "        note: 'Enum for source-listed recipient categories.'\n"
                    "        source_phrase: 'stock exchanges, banks, financial services providers and investment houses'\n\n"
                    "Re-submit_provenance after adding `vocabulary_notes:` "
                    "for every name listed above (or after re-submit_ir "
                    "with renamed declarations)."
                ),
            }
    except Exception as exc:
        # Don't block on tool failure — log and proceed
        print(f"[grounding_gate] check failed: {type(exc).__name__}: {exc}",
              flush=True)

    res = _run_subprocess([PYTHON, str(SRC / "token_provenance_v1.py"),
                            str(env.agent_run_dir)], timeout_s=120)
    token = _load_json(env.agent_run_dir / "metrics_token_provenance_v1.json")
    env.submissions["provenance"] = {"chars": len(yaml_text)}
    return {
        "saved": True,
        "chars": len(yaml_text),
        "token_provenance": {
            "covered_content": token.get("summary", {}).get("covered_content_token_count"),
            "content_total": token.get("summary", {}).get("content_token_count"),
            "uncovered": [t.get("token") for t in token.get("uncovered_tokens", [])][:20],
        },
        "provenance_lint": {
            "strong": provenance_lint_strong,
            "total": provenance_lint_summary.get("total_findings"),
        },
        "subprocess_returncode": res["returncode"],
    }


def tool_submit_waivers(env: ToolEnv, *,
                        items: list[dict[str, Any]]) -> dict[str, Any]:
    """Items shape: [{token, suggested_category, comment}, ...]."""
    if env.phase not in {_PHASE_PACKAGE_DRAFTING, _PHASE_VERIFYING}:
        return {
            "error": f"phase_gate: cannot submit_waivers in phase={env.phase}",
            "current_phase": env.phase,
            "instruction": (
                "Waivers complete the package; only allowed in "
                "PACKAGE_DRAFTING (after submit_provenance) or VERIFYING "
                "(when patching specific waiver issues from judge dissent)."
            ),
        }
    token_metrics = _load_json(env.agent_run_dir / "metrics_token_provenance_v1.json")
    uncovered = {t.get("token"): t for t in token_metrics.get("uncovered_tokens", [])}
    out_items = []
    for item in items:
        tok = item.get("token")
        if not tok:
            continue
        original = uncovered.get(tok, {})
        category = item.get("suggested_category", "other_absorbed")
        comment = item.get("comment", "")
        if "human_approved" in comment:
            comment = comment.replace("human_approved", "agent_suggested")
        out_items.append({
            "token": tok,
            "surface_forms": original.get("surface_forms", [tok]),
            "source_locations": original.get("source_locations", []),
            "status": f"agent_suggested_{category}",
            "suggested_category": category,
            "comment": comment,
            "reviewer": "agent",
        })
    payload = {
        "entry_id": env.original_entry_id,
        "schema": "waiver_token_absorption_v1",
        "generated_from": "metrics_token_provenance_v1.json",
        "generated_by": f"methodology_section_agent_{AGENT_VERSION}",
        "items": out_items,
    }
    (env.agent_run_dir / "waiver_token_absorption_v1.json").write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    env.submissions["waivers"] = {"items": len(out_items)}
    return {"saved": True, "items_count": len(out_items)}


def _generate_keep_drop_replace_memo(env: ToolEnv,
                                       latest_verify: dict[str, Any]
                                       ) -> dict[str, Any] | None:
    """Auto-generated after each VERIFY with dissent."""
    if env.client is None:
        return None
    ir_text = _read_text(env.agent_run_dir / "main_ir.a4v3")
    if not ir_text:
        return None

    dissent = latest_verify.get("judge_dissent", []) or []
    dissent_compact = [
        {
            "model": d.get("model"),
            "verdict": d.get("verdict"),
            "differences": (d.get("semantic_differences") or [])[:3],
        }
        for d in dissent
    ]

    # Cross-iter context: surface best prior iter (if better than current)
    # + its IR + its dissent pattern so the LLM can reason "what did the
    # change in current break vs best".
    cross_iter_block = ""
    best = _find_best_prior_iter(env, exclude_current_hash=latest_verify.get("ir_hash"))
    if best is not None:
        # Only attach when best is actually better than current
        best_score = best.get("quality_score")
        cur_score = (
            ({"corresponds":3,"ambiguous":2,"partially_corresponds":1,
              "does_not_correspond":0}.get(latest_verify.get("worst_verdict"), -1)),
            (latest_verify.get("distribution") or {}).get("corresponds", 0),
        )
        if best_score and best_score > cur_score:
            best_ir_path = env.agent_run_dir / f"iter_{best['iter_idx']}" / "main_ir.a4v3"
            best_ir_text = best_ir_path.read_text(encoding="utf-8") \
                if best_ir_path.exists() else "(missing)"
            best_dissent_compact = [
                {
                    "model": d.get("model"),
                    "verdict": d.get("verdict"),
                    "differences": (d.get("semantic_differences") or [])[:2],
                }
                for d in (best.get("judge_dissent") or [])
            ]
            cross_iter_block = (
                f"## BEST PRIOR ITER (iter_{best['iter_idx']}, "
                f"round {best.get('round','?')}, tier="
                f"{best['quality_tier']}, distribution={best['distribution']})\n\n"
                f"Quality regressed from this iter to current. The IR below "
                f"was better — analyse what got DROPPED or REPLACED in the "
                f"current IR that those judges had no problem with.\n\n"
                f"```a4v3\n{best_ir_text[:3000]}\n```\n\n"
                f"Best-iter dissent (only complaint(s) to address — keep "
                f"everything else):\n"
                f"```json\n{json.dumps(best_dissent_compact, indent=2, ensure_ascii=False)[:1500]}\n```\n\n"
            )

    # Per-iter history (compact — verdicts + brief judge dissent) to help
    # LLM reason about cross-round patterns.
    iter_summary = []
    for it in _collect_iter_history(env):
        if it.get("worst_verdict") is None:
            continue
        compact_dissent = [
            f"{d.get('model')}:{(d.get('semantic_differences') or [''])[0][:140]}"
            for d in (it.get("judge_dissent") or [])[:2]
        ]
        iter_summary.append({
            "iter": it["iter_idx"],
            "round": it.get("round"),
            "tier": it["quality_tier"],
            "distribution": it["distribution"],
            "agreement": it.get("agreement"),
            "top_dissent": compact_dissent,
        })

    user = (
        f"## CURRENT IR\n\n```\n{ir_text}\n```\n\n"
        f"## LATEST VERIFY ROUND\n\n"
        f"- worst_verdict: {latest_verify.get('worst_verdict')}\n"
        f"- distribution: {latest_verify.get('distribution')}\n\n"
        f"## JUDGE DISSENT (per-judge, with specific complaints)\n\n"
        f"```json\n{json.dumps(dissent_compact, indent=2, ensure_ascii=False)[:4000]}\n```\n\n"
        f"{cross_iter_block}"
        f"## ITER HISTORY (verdicts + top-2 complaints per iter)\n\n"
        f"```json\n{json.dumps(iter_summary, indent=2, ensure_ascii=False)[:3500]}\n```\n\n"
        f"## YOUR TASK\n\n"
        f"Write the Keep/Drop/Replace memo per the schema. Be specific "
        f"and incremental — name exact IR constructs, not vague concepts.\n"
        f"\nCRITICAL when a BEST PRIOR ITER block is present above: that iter "
        f"was JUDGED BETTER than current. Cross-reference what changed between "
        f"that IR and the current IR — if the regression correlates with a "
        f"specific replacement, your `keep` should explicitly preserve the "
        f"best-iter construct, and `replace` should undo the offending change. "
        f"Do NOT propose more changes on top of a regression — fix the regression first."
    )
    try:
        result = env.client.complete(
            [],
            raw_messages=[{"role": "system", "content": _KDR_MEMO_SYSTEM},
                          {"role": "user", "content": user}],
            max_tokens=3500,
            extra_body=env.extra_body,
            seed=env.seed,
        )
    except Exception as exc:
        return {"error": str(exc)}

    raw = _strip_code_fence(result.text or "")
    try:
        parsed = json.loads(raw)
    except Exception as exc:
        return {"error": f"non-JSON: {exc}", "raw_excerpt": raw[:300]}

    n = len(list(env.agent_run_dir.glob("keep_drop_replace_v*.json")))
    out_path = env.agent_run_dir / f"keep_drop_replace_v{n}.json"
    out_path.write_text(json.dumps(parsed, indent=2, ensure_ascii=False) + "\n",
                         encoding="utf-8")
    md_lines = [f"# Keep/Drop/Replace memo v{n}", "",
                f"Summary: {parsed.get('summary','')}", ""]
    md_lines.append("## Keep (these worked, don't touch)")
    for k in parsed.get("keep") or []:
        md_lines.append(f"- ✓ {k}")
    md_lines.append("\n## Drop (remove these)")
    for d in parsed.get("drop") or []:
        md_lines.append(f"- ✗ {d}")
    md_lines.append("\n## Replace (swap these)")
    for r in parsed.get("replace") or []:
        md_lines.append(f"- {r.get('from')} → {r.get('to')}")
        md_lines.append(f"    rationale: {r.get('rationale')}")
    md_lines.append("\n## Unresolved (open questions)")
    for u in parsed.get("unresolved") or []:
        md_lines.append(f"- ? {u}")
    md_path = env.agent_run_dir / f"keep_drop_replace_v{n}.md"
    md_path.write_text("\n".join(md_lines), encoding="utf-8")
    try:
        inventory = ensure_parts_inventory(env)
        if inventory:
            inventory = ingest_kdr_cards(inventory, parsed, required=False)
            write_inventory(env, inventory)
    except Exception as exc:
        print(f"[parts_inventory] failed to ingest KDR cards: {exc}",
              flush=True)

    # KDR-as-hypothesis gate: drop items become CONTRACTUAL (enforced by
    # submit_ir_for_lint refusal) only when CONFIRMED by independent
    # signals. Otherwise they remain ADVISORY in the memo (agent reads
    # them, can act, but next submit is not refused).
    #
    # Confirmation requires AT LEAST ONE of:
    #   1. ≥2 distinct judge dissenters in latest verify
    #   2. ≥1 strong/blocking finding from deterministic checks (lint
    #      strong_findings, family_coverage required_gaps, lowering
    #      audit smells, missing_instance_layer advisory etc.)
    # Rationale: a single judge dissent + LLM-generated KDR can lock the
    # pipeline into a wrong direction (e.g. drop the singleton issuance
    # program when judges later accept it 5/5). Require independent
    # signal before treating KDR's drops as binding.
    drop_items: list[str] = list(parsed.get("drop") or [])
    for r in parsed.get("replace") or []:
        if isinstance(r, dict) and r.get("from"):
            drop_items.append(str(r["from"]))
    drop_items = [d.strip() for d in drop_items if d and d.strip()]

    dissenter_count = len(dissent)
    lint = _load_json(env.agent_run_dir / "a4v3_semantic_lint_v1.json")
    family = _load_json(env.agent_run_dir / "metrics_family_coverage_v1.json")
    lowering = _load_json(env.agent_run_dir / "lowering_audit_v1.json")
    det_blocking_signals = {
        "lint_strong_findings": (lint.get("summary") or {}).get("strong_findings", 0) or 0,
        "family_required_gaps": family.get("n_required_gaps", 0) or 0,
        "lowering_smells": lowering.get("n_smells", 0) or 0,
    }
    det_blocking_count = sum(int(v or 0) for v in det_blocking_signals.values())

    kdr_confirmed = (dissenter_count >= 2) or (det_blocking_count >= 1)
    kdr_confirmation_reason: str
    if dissenter_count >= 2:
        kdr_confirmation_reason = (
            f"confirmed by {dissenter_count} judge dissenters "
            f"(threshold ≥2)"
        )
    elif det_blocking_count >= 1:
        kdr_confirmation_reason = (
            f"confirmed by deterministic checks "
            f"({det_blocking_signals})"
        )
    else:
        kdr_confirmation_reason = (
            f"NOT confirmed: only {dissenter_count} dissenter(s) and "
            f"0 det-blocking findings ({det_blocking_signals}); "
            f"KDR demoted to advisory — drops NOT enforced by "
            f"submit_ir_for_lint. Agent may still apply them but next "
            f"draft will not be refused if drops survive."
        )

    if kdr_confirmed:
        env.last_kdr_drops = drop_items
    else:
        # Clear any prior contract; KDR is hypothesis-only this round.
        env.last_kdr_drops = []
    env.last_kdr_version = n
    env.last_kdr_ir_hash = env.current_ir_hash

    return {
        "version": n,
        "n_keep": len(parsed.get("keep") or []),
        "n_drop": len(parsed.get("drop") or []),
        "n_replace": len(parsed.get("replace") or []),
        "n_unresolved": len(parsed.get("unresolved") or []),
        "artifact_md": str(md_path.relative_to(env.agent_run_dir)),
        "summary": parsed.get("summary"),
        "drop_items_now_contractual": env.last_kdr_drops[:10],
        "drop_items_suggested_but_not_enforced": (
            drop_items[:10] if not kdr_confirmed else []),
        "kdr_confirmed": kdr_confirmed,
        "kdr_confirmation_reason": kdr_confirmation_reason,
        "kdr_dissenter_count": dissenter_count,
        "kdr_det_blocking_signals": det_blocking_signals,
    }


def tool_run_package_checks(env: ToolEnv, *, with_llm: bool = True,
                             corpus_aware: bool | None = None) -> dict[str, Any]:
    """Run unified package-level checks (Stage 9 equivalent)."""
    if "ir" not in env.submissions:
        return {"error": "submit_ir_for_lint must be called first"}
    if env.phase not in {_PHASE_PACKAGE_DRAFTING, _PHASE_VERIFYING}:
        return {
            "error": f"phase_gate: cannot run_package_checks in phase={env.phase}",
            "current_phase": env.phase,
            "instruction": (
                "Package checks need a complete package: IR clean + "
                "provenance + waivers. Either IR is not yet clean (call "
                "submit_ir_for_lint until ir_clean=true) or you haven't "
                "submitted provenance/waivers yet."
            ),
        }
    if "provenance" not in env.submissions:
        return {
            "error": "missing_provenance: submit_provenance is required before run_package_checks",
            "current_phase": env.phase,
            "instruction": (
                "Call submit_provenance(yaml_text=...) first to document "
                "each IR claim with source_quotes + back_translation. "
                "Without provenance, quality_snapshot flags "
                "`missing_required_artifacts` and the triage override "
                "blocks acceptance for a process gap. After provenance, "
                "submit_waivers, THEN run_package_checks."
            ),
        }
    if "waivers" not in env.submissions:
        return {
            "error": "missing_waivers: submit_waivers is required before run_package_checks",
            "current_phase": env.phase,
            "instruction": (
                "Call submit_waivers(items=[...]) — even an empty list "
                "is acceptable if no source tokens need waiving. The "
                "submission marks the package as deliberately complete. "
                "Then run_package_checks."
            ),
        }
    env.phase = _PHASE_VERIFYING
    cmd = [PYTHON, str(SRC / "run_dz_entry_checks_v1.py"), str(env.agent_run_dir)]
    if with_llm:
        cmd.append("--with-llm")
    use_corpus_aware = env.corpus_aware if corpus_aware is None else corpus_aware
    if use_corpus_aware and with_llm:
        cmd.append("--corpus-aware")
    cmd.extend(["--timeout-s", "300"])
    res = _run_subprocess(cmd, timeout_s=1500)
    report = _load_json(env.agent_run_dir / "dz_entry_checks_v1.json")
    summary = report.get("summary", {})

    corpus_full = _load_json(env.agent_run_dir / "metrics_corpus_aware_multi_judge_v1.json")
    judge_dissent = []
    distribution: dict[str, int] = {}
    local_source_distribution: dict[str, int] = {}
    local_source_dissent: list[dict[str, Any]] = []
    for j in corpus_full.get("judges", []) or []:
        if not isinstance(j, dict) or j.get("error"):
            continue
        # Corpus-alignment dimension: does the IR follow the corpus's
        # canonical structural pattern? Used as primary triage signal.
        verdict = j.get("corpus_alignment")
        if verdict:
            distribution[verdict] = distribution.get(verdict, 0) + 1
        if verdict and verdict != "corresponds":
            judge_dissent.append({
                "model": j.get("model"),
                "verdict": verdict,
                "confidence": j.get("confidence"),
                "reason_short": (j.get("reason_short") or "")[:600],
                "semantic_differences": (j.get("semantic_differences") or [])[:5],
            })
        # Local-source dimension: does the IR say what the LOCAL section
        # text says? Independent of corpus pattern. Surfaced separately
        # so agent can distinguish "semantic translation imperfect" from
        # "structurally diverges from corpus canonical".
        local_v = j.get("local_source_alignment")
        if local_v:
            local_source_distribution[local_v] = \
                local_source_distribution.get(local_v, 0) + 1
        if local_v and local_v != "corresponds":
            local_source_dissent.append({
                "model": j.get("model"),
                "verdict": local_v,
                "confidence": j.get("confidence"),
                "reason_short": (j.get("reason_short") or "")[:600],
                "semantic_differences": (j.get("semantic_differences") or [])[:5],
            })
    rank = {"does_not_correspond": 0, "partially_corresponds": 1,
            "ambiguous": 2, "corresponds": 3}
    verdicts = [j.get("corpus_alignment") for j in corpus_full.get("judges", [])
                if isinstance(j, dict) and j.get("corpus_alignment")]
    worst = min(verdicts, key=lambda v: rank.get(v, 999)) if verdicts else None
    local_verdicts = [j.get("local_source_alignment") for j in corpus_full.get("judges", [])
                       if isinstance(j, dict) and j.get("local_source_alignment")]
    local_worst = (min(local_verdicts, key=lambda v: rank.get(v, 999))
                    if local_verdicts else None)

    round_idx = len(env.verify_history) + 1
    issue_fingerprint = sorted({
        f"{d.get('model','?')}::{(d.get('semantic_differences') or [''])[0][:140]}"
        for d in judge_dissent
    })
    ir_text_at_verify = _read_text(env.agent_run_dir / "main_ir.a4v3")
    env.last_verified_ir_hash = _hash_text(ir_text_at_verify) if ir_text_at_verify else None

    env.verify_history.append({
        "round": round_idx,
        "worst_verdict": worst,
        "distribution": distribution,
        "issue_fingerprint": issue_fingerprint,
        "judge_dissent": judge_dissent,
        "ir_hash": env.last_verified_ir_hash,
    })

    iter_idx = round_idx
    verdict_payload = {
        "round": round_idx,
        "worst_verdict": worst,
        "distribution": distribution,
        "judge_dissent": judge_dissent,
        "issue_fingerprint": issue_fingerprint,
        "ir_hash": env.last_verified_ir_hash,
    }
    try:
        _snapshot_iter(env.agent_run_dir, iter_idx,
                       kind="verify_done",
                       discovery_dir=env.discovery_dir,
                       verdict_data=verdict_payload)
    except Exception as exc:
        print(f"[snapshot] verify {iter_idx} failed: {exc}", flush=True)

    # Refresh persistent cross-iter scoreboard. Cheap (no LLM calls) and
    # gives the agent a stable artifact it can re-read at any time via
    # read_my_notes('iter_scoreboard') instead of re-deriving from
    # verify_history each turn.
    try:
        _write_iter_scoreboard(env)
    except Exception as exc:
        print(f"[scoreboard] write failed: {exc}", flush=True)

    stagnant = False
    stagnation_reason = ""
    if round_idx >= 2:
        prev_fp = env.verify_history[-2]["issue_fingerprint"]
        same_issues = set(issue_fingerprint) & set(prev_fp)
        if len(same_issues) >= max(1, len(prev_fp) // 2):
            stagnant = True
            stagnation_reason = (
                f"Round {round_idx} has the same dissent issues as round "
                f"{round_idx-1} (overlap: {len(same_issues)} of "
                f"{len(prev_fp)} previous issues). Local fixes are not "
                f"moving the needle — judges complain about the SAME thing."
            )
    if round_idx >= 3 and worst != "corresponds":
        stagnant = True
        stagnation_reason = (stagnation_reason + " ") if stagnation_reason else ""
        stagnation_reason += (
            f"3+ verify rounds completed and worst verdict is still "
            f"'{worst}'. Repair loop exhausted for cosmetic fixes."
        )

    if stagnant and worst != "corresponds":
        if env.meta_evaluations_done >= MAX_META_EVALUATIONS:
            env.meta_required = False
            env.meta_required_reason = (
                f"meta cap reached ({env.meta_evaluations_done}/"
                f"{MAX_META_EVALUATIONS}); finalize as failed_after_meta"
            )
        else:
            env.meta_required = True
            env.meta_required_reason = stagnation_reason
            env.phase = _PHASE_META_REQUIRED

    actionable = (
        f"WORST verdict among {len(verdicts)} judges: {worst}. "
        f"Distribution: {distribution}. Round {round_idx}/N. "
        f"Phase: {env.phase}. "
    )
    cap_reached = env.meta_evaluations_done >= MAX_META_EVALUATIONS
    if env.meta_required:
        actionable += (
            "**META MODE TRIGGERED**: " + stagnation_reason + " "
            "BEFORE submitting another IR draft, you MUST call "
            "meta_evaluate(). It will show full verify history and force "
            "you to think about RADICAL ALTERNATIVE ARCHITECTURE (not local "
            "patches). submit_ir_for_lint will refuse until meta_evaluate "
            "is called."
        )
    elif cap_reached and worst != "corresponds":
        actionable += (
            "**META CAP REACHED** "
            f"({env.meta_evaluations_done}/{MAX_META_EVALUATIONS}). The "
            "architectural search has saturated — multiple radical refactors "
            "have not converged judges. STOP iterating. Call finalize("
            "decision='failed_after_meta', summary=<honest explanation of "
            "remaining dissent>) NOW. Further IR submissions are unlikely "
            "to help and will exhaust your step budget."
        )
    elif judge_dissent:
        n_corr = (distribution or {}).get("corresponds", 0)
        n_total = sum(distribution.values()) if distribution else 0
        agreement_val = corpus_full.get("summary", {}).get("corpus_alignment_agreement")
        try:
            agreement_val = float(agreement_val) if agreement_val is not None else None
        except Exception:
            agreement_val = None
        worst_is_does_not = worst == "does_not_correspond"
        majority_with_high_agreement = (
            agreement_val is not None and agreement_val >= 0.7
            and n_corr >= max(1, n_total - 1)
            and not worst_is_does_not
        )
        if majority_with_high_agreement:
            actionable += (
                f"deterministic-primary triage: {n_corr}/{n_total} corresponds with agreement "
                f"{agreement_val}, no does_not_correspond. Single dissent is "
                f"advisory not blocking. **You may finalize NOW** as "
                f"`agent_accept_candidate_with_dissent` if det checks (lint, "
                f"family, lowering) are clean — further repair attempts unlikely "
                f"to flip the dissenter (often a structural ceiling). Read "
                f"judge_dissent[*].semantic_differences ONLY if you see a "
                f"genuinely fixable specific issue."
            )
        else:
            actionable += (
                "Read judge_dissent[*].semantic_differences for SPECIFIC issues "
                "to fix. **If multiple judges complain about the SAME structural "
                "issue (e.g. modal absorption, cross-product over-commitment), "
                "this is likely a STRATEGY problem, not a local IR bug — call "
                "amend_strategy() to write strategy_v{N+1}.md addressing the "
                "concern, THEN re-DRAFT.** If dissent says a source concept, "
                "basis, process, or carrier is missing from the ontology, "
                "call re_analyze_role_frame() first: that is a SCOUT/role "
                "gap, not a strategy wording gap. If amend_strategy keeps the same "
                "family choice and judges keep complaining about modality "
                "mismatch (e.g. 'source is permissive but IR asserts as "
                "fact'), call re_analyze_role_frame() — it can change "
                "family.modality which amend cannot. If only one judge "
                "dissents and the issue looks like a local typo or one-line "
                "fix, just re-submit IR. Triage uses deterministic-primary "
                "decision rule (det primary, judges advisory) — see "
                "finalize() docs. If clean_gate accepted + majority corresponds "
                "+ no does_not + agreement >=0.7, consider finalize as "
                "`agent_accept_candidate_with_dissent`."
            )
    else:
        actionable = (f"All {len(verdicts)} judges agree on '{worst}'. "
                      f"No dissent. Phase={env.phase}. Call finalize() now.")

    kdr_artifact = None
    if env.client is not None and judge_dissent:
        try:
            kdr_artifact = _generate_keep_drop_replace_memo(
                env, env.verify_history[-1])
        except Exception as exc:
            print(f"[kdr] failed: {exc}", flush=True)

    regression_hint = None
    auto_rollback_performed = None
    if len(env.verify_history) >= 2:
        VERDICT_RANK = {"corresponds": 0, "partially_corresponds": 1,
                        "does_not_correspond": 2}
        cur = env.verify_history[-1]
        prior = env.verify_history[:-1]

        def _round_score(r):
            wr = VERDICT_RANK.get(r.get("worst_verdict"), 99)
            corr_count = (r.get("distribution") or {}).get("corresponds", 0)
            return (wr, -corr_count)
        best_prior = min(prior, key=_round_score)
        cur_score = _round_score(cur)
        best_score = _round_score(best_prior)
        if cur_score > best_score:
            best_iter = best_prior.get("round")
            cur_corr = (cur.get("distribution") or {}).get("corresponds", 0)
            best_corr = (best_prior.get("distribution") or {}).get("corresponds", 0)
            cur_rank = cur_score[0]
            best_rank = best_score[0]
            corresponds_dropped = best_corr - cur_corr
            is_strong_regression = (
                cur_rank > best_rank
                or corresponds_dropped >= 2
            )
            regression_hint = (
                f"REGRESSION DETECTED: current round {cur.get('round')} is "
                f"worse than best prior round {best_iter} "
                f"(now: worst={cur.get('worst_verdict')}, corresponds="
                f"{cur_corr}; best prior: worst={best_prior.get('worst_verdict')}, "
                f"corresponds={best_corr})."
            )
            if is_strong_regression and env.auto_rollbacks_done < env.max_auto_rollbacks:
                auto_reason = (
                    f"strong regression in round {cur.get('round')}: "
                    f"worst {best_prior.get('worst_verdict')}→"
                    f"{cur.get('worst_verdict')}, corresponds {best_corr}→"
                    f"{cur_corr}. Auto-rollback to iter_{best_iter}."
                )
                rb_result = _do_rollback(env, best_iter, auto_reason,
                                          source="auto")
                if "error" not in rb_result:
                    env.auto_rollbacks_done += 1
                    auto_rollback_performed = {
                        "rolled_back_to": best_iter,
                        "reason": auto_reason,
                        "auto_rollbacks_done": env.auto_rollbacks_done,
                        "max_auto_rollbacks": env.max_auto_rollbacks,
                        "ir_hash": rb_result.get("ir_hash"),
                    }
                    regression_hint = (
                        regression_hint
                        + f" **AUTO-ROLLBACK EXECUTED**: IR restored from "
                        f"iter_{best_iter}. The current main_ir.a4v3 + "
                        f"provenance + waivers now match iter_{best_iter}. "
                        f"Apply MINIMAL targeted fixes addressing the "
                        f"specific dissent issues — do NOT rewrite working "
                        f"sections. After your fix, re-submit_ir_for_lint, "
                        f"then re-run_package_checks. "
                        f"({env.auto_rollbacks_done}/"
                        f"{env.max_auto_rollbacks} auto-rollbacks used.)"
                    )
                else:
                    regression_hint += (
                        f" Auto-rollback attempted to iter_{best_iter} but "
                        f"failed: {rb_result.get('error')}. "
                        f"Call rollback_to_iter({best_iter}) manually."
                    )
            elif is_strong_regression:
                regression_hint += (
                    f" STRONG regression but auto-rollback cap reached "
                    f"({env.auto_rollbacks_done}/{env.max_auto_rollbacks}). "
                    f"Call rollback_to_iter({best_iter}) manually if you "
                    f"want to restore, OR finalize as failed_after_meta."
                )
            else:
                regression_hint += (
                    f" Mild regression (no auto-rollback). Consider "
                    f"compare_iters({best_iter}, {cur.get('round')}) to see "
                    f"changes, then rollback_to_iter({best_iter}) if needed."
                )

    uncovered_phrases_hint = None
    spc_path = env.agent_run_dir / "metrics_source_phrase_coverage_v1.json"
    if spc_path.exists():
        try:
            spc = json.loads(spc_path.read_text(encoding="utf-8"))
            uncovered = spc.get("uncovered") or []
            if uncovered:
                phrases = [u.get("phrase", "?") for u in uncovered][:5]
                uncovered_phrases_hint = (
                    f"{len(uncovered)} source phrase(s) unmatched by the "
                    f"token-coverage matcher: {phrases}. Triage will pass "
                    f"this through (often singular/plural mismatches like "
                    f"'Licenses' vs 'License' that the matcher's stem "
                    f"comparison misses). When you finalize, write in "
                    f"finalize.notes a one-line explanation per phrase: "
                    f"either 'matcher false-positive: IR has X' or 'real "
                    f"omission: source phrase Y not represented'. The "
                    f"human reviewer relies on this audit trail."
                )
        except Exception:
            pass

    # Snapshot "best iter so far" for the return payload — agent should see
    # this inline, not have to derive it from iter_history each turn.
    best_iter = _find_best_prior_iter(env)
    best_iter_summary = None
    if best_iter is not None:
        best_iter_summary = {
            "iter_idx": best_iter["iter_idx"],
            "round": best_iter.get("round"),
            "worst_verdict": best_iter["worst_verdict"],
            "distribution": best_iter["distribution"],
            "agreement": best_iter.get("agreement"),
            "quality_tier": best_iter["quality_tier"],
            "is_current": best_iter.get("ir_hash") == env.last_verified_ir_hash,
        }

    # Dual-dimension surface: distinguish corpus-canonical alignment
    # from local-source alignment. When they diverge, the agent should
    # see the distinction explicitly — judges may unanimously accept
    # corpus pattern (5/5) yet flag local divergence (4/5), or vice
    # versa. Each pattern needs different remediation.
    dimension_divergence_hint: str | None = None
    if local_worst is not None and worst is not None:
        if local_worst != worst:
            if rank.get(worst, 99) > rank.get(local_worst, 99):
                # Corpus alignment better than local — IR matches corpus
                # canonical but local-source has issues. Often a sign of
                # over-canonicalization (IR added structure not in source).
                dimension_divergence_hint = (
                    f"DIMENSION DIVERGENCE: corpus_alignment worst="
                    f"{worst} ({distribution}), local_source_alignment "
                    f"worst={local_worst} ({local_source_distribution}). "
                    f"Local source is the weaker dimension — IR may have "
                    f"over-canonicalized (added structure not warranted "
                    f"by section text). Read local_source_dissent below "
                    f"for specific source-vs-IR mismatches."
                )
            else:
                # Local alignment better than corpus — IR captures local
                # source well but diverges from corpus canonical pattern.
                # Often a sign of under-canonicalization (missing
                # standard structural shape).
                dimension_divergence_hint = (
                    f"DIMENSION DIVERGENCE: corpus_alignment worst="
                    f"{worst} ({distribution}), local_source_alignment "
                    f"worst={local_worst} ({local_source_distribution}). "
                    f"Corpus alignment is the weaker dimension — IR "
                    f"translates the source meaning but doesn't match "
                    f"the corpus's canonical structural shape (e.g. "
                    f"missing instance-layer in three-layer pattern). "
                    f"Consider whether structural shape matters for "
                    f"future cross-section references; check corpus_"
                    f"profile canonical_patterns."
                )

    return {
        "subprocess_returncode": res["returncode"],
        "with_llm": with_llm,
        "corpus_aware": use_corpus_aware,
        "summary": {
            "lint": summary.get("semantic_lint"),
            "quality_snapshot": summary.get("quality_snapshot"),
            "multi_judge": summary.get("multi_judge"),
            "corpus_aware_multi_judge": summary.get("corpus_aware_multi_judge"),
            "corpus_alignment_distribution": distribution,
            "corpus_alignment_worst_verdict": worst,
            "local_source_alignment_distribution": local_source_distribution,
            "local_source_alignment_worst_verdict": local_worst,
        },
        "judge_dissent": judge_dissent,
        "local_source_dissent": local_source_dissent,
        "dimension_divergence_hint": dimension_divergence_hint,
        "verify_round": round_idx,
        "meta_required": env.meta_required,
        "meta_required_reason": env.meta_required_reason if env.meta_required else "",
        "actionable_hint": actionable,
        "uncovered_phrases_hint": uncovered_phrases_hint,
        "regression_hint": regression_hint,
        "auto_rollback_performed": auto_rollback_performed,
        "keep_drop_replace_memo": kdr_artifact,
        "iter_history": _list_iters(env.agent_run_dir),
        "best_iter_so_far": best_iter_summary,
        "iter_scoreboard_path": "discovery/iter_scoreboard.md",
    }
