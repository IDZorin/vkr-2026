"""IR drafting + strategy-vs-IR check tools."""
from __future__ import annotations

import json
import re
import sys
from typing import Any

from ir_agent.anti_patterns import _check_anti_patterns
from ir_agent.config import PYTHON, SRC
from ir_agent.env import ToolEnv
from ir_agent.helpers import (
    _hash_text, _load_json, _read_text, _run_subprocess,
    _strip_code_fence, _truncate,
)
from ir_agent.parts_inventory import (
    ensure_parts_inventory,
    evaluate_inventory_coverage,
)
from ir_agent.phases import (
    _PHASE_FINALIZED, _PHASE_IR_IN_FLUX, _PHASE_PACKAGE_DRAFTING,
)
from ir_agent.prompts.check import _CHECK_IR_VS_STRATEGY_SYSTEM
from ir_agent.snapshots import _snapshot_iter
from ir_agent.strategy_io import _latest_strategy_path


def tool_submit_ir_for_lint(env: ToolEnv, *, ir_text: str) -> dict[str, Any]:
    """Save IR, run lint + det checks, return findings."""
    # Lazy import to avoid circular dep with triage.py
    from ir_agent.triage import (
        _intent_overrides_family_gap, _intent_overrides_lowering_smell,
    )

    if not ir_text.strip():
        return {"error": "empty IR"}
    if env.phase == _PHASE_FINALIZED:
        return {"error": "phase=FINALIZED — run already complete; cannot submit more IR"}
    role_frame_path = env.discovery_dir / "role_frame.json"
    if not role_frame_path.exists():
        return {
            "error": "role_frame missing — call analyze_role_frame() before drafting IR",
            "instruction": (
                "analyze_role_frame() forces you to identify: (a) the event/"
                "process this source describes; (b) the agent/recipient/"
                "target/scope roles; (c) for each entity, its role in the "
                "methodology AND general financial knowledge. Without this "
                "frame, the IR collapses participants into a generic "
                "catch-all relation. The frame also documents an ontology "
                "budget so you don't bloat sorts. After analyze_role_frame, "
                "call compose_strategy(), then this gate opens."
            ),
        }
    latest_strategy = _latest_strategy_path(env.discovery_dir)
    if latest_strategy is None:
        return {
            "error": "strategy_v0.md missing — call compose_strategy() before drafting IR",
            "instruction": (
                "compose_strategy() takes user_hints + role_frame + "
                "classification and writes strategy_v0.md — the single "
                "source of truth the drafter follows. Without it the "
                "drafter has to re-derive intent from scattered artifacts "
                "and may contradict role_frame's modality decision. After "
                "compose_strategy, this gate opens."
            ),
        }
    if env.meta_required:
        return {
            "error": "meta_required: cannot submit new IR until meta_evaluate is called",
            "current_phase": env.phase,
            "reason": env.meta_required_reason,
            "instruction": (
                "Local IR fixes have not changed judges' dissent across "
                "multiple verify rounds. STOP doing micro-edits. Call "
                "meta_evaluate() — it will show full verify history and "
                "force you to think about RADICAL alternative architecture. "
                "After meta_evaluate, you may submit one new IR drawing on "
                "the radical refactor; if that still fails, finalize as "
                "'failed_after_meta'."
            ),
        }
    # KDR-as-contract gate: if the previous run_package_checks generated
    # a KDR memo with `drop` items, refuse a new IR that still contains
    # those items (substring match — KDR phrases are short and specific
    # enough that substring is a low-false-positive signal). This closes
    # the loop where KDR was advisory and the agent could re-submit
    # ignoring it. Bypass only when no KDR memo has been produced yet.
    ir_text_for_check = _strip_code_fence(ir_text)
    if env.last_kdr_drops:
        # Extract only the SPECIFIC named declaration being dropped — NOT
        # generic type identifiers that may appear in the replace.from
        # body (e.g. `permission X(agent: Organization)` — `Organization`
        # is a type reference, not the dropped item; `X` is). False
        # positives on generic types caused 16 spurious refusals in run
        # v3, so this gate is INTENTIONALLY narrow: a violation only
        # if the dropped declaration's exact name + same kind appears
        # in the new IR.
        import re as _re
        haystack = ir_text_for_check
        violations: list[str] = []
        for drop_item in env.last_kdr_drops:
            m = _re.search(
                r"\b(fact|rel|entity|sort|permission|obligation|"
                r"prohibition|constraint|fun)\s+([A-Za-z_][A-Za-z_0-9]*)",
                drop_item)
            if not m:
                # Drop item is non-decl text — skip (too vague to gate on)
                continue
            kind, name = m.group(1), m.group(2)
            # Match `<kind> <name>` declaration in new IR (line-start to
            # avoid matching inside formula bodies). Whole-word for `name`.
            decl_re = _re.compile(
                rf"^\s*{_re.escape(kind)}\s+{_re.escape(name)}\b",
                _re.MULTILINE)
            if decl_re.search(haystack):
                violations.append(
                    f"KDR memo v{env.last_kdr_version} said drop "
                    f"'{kind} {name}' — declaration still present in "
                    f"submitted IR (line-start match)")
        if violations:
            return {
                "error": "kdr_drop_items_still_present: the KDR memo from "
                         "the most recent run_package_checks explicitly "
                         "marked items to drop, but the new IR still "
                         "contains them.",
                "kdr_version": env.last_kdr_version,
                "violations": violations,
                "instruction": (
                    "KDR memos are now CONTRACTUAL: drop items MUST be "
                    "removed or replaced before re-submitting IR. Open "
                    f"keep_drop_replace_v{env.last_kdr_version}.md and "
                    f"address each `Drop` and `Replace.from` item. If you "
                    f"believe a KDR recommendation is wrong, call "
                    f"amend_strategy() to revise the strategy first — that "
                    f"clears the KDR drops for the next VERIFY cycle."
                ),
            }
    env.phase = _PHASE_IR_IN_FLUX
    ir_text = ir_text_for_check
    (env.agent_run_dir / "main_ir.a4v3").write_text(ir_text, encoding="utf-8")
    env.current_ir_hash = _hash_text(ir_text)
    steps = []
    for name, cmd in [
        ("parser_strict", [PYTHON, str(SRC / "a4v3_parser_v1.py"),
                           str(env.agent_run_dir / "main_ir.a4v3"), "--strict"]),
        ("semantic_lint", [PYTHON, str(SRC / "a4v3_semantic_lint_v1.py"),
                           str(env.agent_run_dir)]),
        ("family_coverage", [PYTHON, str(SRC / "family_coverage_v1.py"),
                             str(env.agent_run_dir)]),
        ("lowering_audit", [PYTHON, str(SRC / "lowering_audit_v1.py"),
                            str(env.agent_run_dir)]),
    ]:
        steps.append({"name": name, **_run_subprocess(cmd, timeout_s=120)})
    lint = _load_json(env.agent_run_dir / "a4v3_semantic_lint_v1.json")
    family = _load_json(env.agent_run_dir / "metrics_family_coverage_v1.json")
    lowering = _load_json(env.agent_run_dir / "lowering_audit_v1.json")
    lint_md = _truncate(_read_text(env.agent_run_dir / "a4v3_semantic_lint_v1.md"),
                         3000)
    env.submissions["ir"] = {"chars": len(ir_text), "lines": ir_text.count("\n")}

    classification = _load_json(env.discovery_dir / "text_intent_classification.json")
    raw_required_gaps = family.get("required_gaps") or []
    raw_smells = lowering.get("smells") or []
    family_blocking = [g for g in raw_required_gaps
                       if _intent_overrides_family_gap(classification, g) is None]
    smells_blocking = [s for s in raw_smells
                       if _intent_overrides_lowering_smell(classification, s) is None]
    lint_strong = lint.get("summary", {}).get("strong_findings") or 0

    anti_pattern_findings = _check_anti_patterns(ir_text)
    ap_strong = [f for f in anti_pattern_findings if f["severity"] == "strong"]
    ap_soft = [f for f in anti_pattern_findings if f["severity"] == "soft"]

    # Run extended grounding check (cheap — pure regex + set membership, no
    # LLM or subprocess). Surfaces ungrounded sort/symbol names ASAP so the
    # agent can either rename to use source words OR plan to document via
    # provenance.yaml `vocabulary_notes:` BEFORE submit_provenance gates on
    # the same check. Advisory at this stage (does NOT affect ir_clean) —
    # otherwise creates a deadlock with provenance-only grounding paths.
    grounding_summary: dict[str, Any] = {}
    try:
        sys.path.insert(0, str(SRC))
        import extended_grounding_check_v1 as _eg
        _g = _eg.check_entry(env.agent_run_dir)
        grounding_summary = {
            "ungrounded_sorts": _g["ungrounded"]["sorts"],
            "ungrounded_symbols": _g["ungrounded"]["symbols"],
            "ungrounded_entities": _g["ungrounded"]["entities"],
            "n_ungrounded": (len(_g["ungrounded"]["sorts"])
                              + len(_g["ungrounded"]["symbols"])
                              + len(_g["ungrounded"]["entities"])),
            "grounded_via_overlay": _g.get("grounded_via_overlay", {}),
        }
    except Exception as exc:
        grounding_summary = {"error": f"{type(exc).__name__}: {exc}"}

    try:
        inventory = ensure_parts_inventory(env)
        parts_coverage = evaluate_inventory_coverage(env, ir_text, inventory)
    except Exception as exc:
        parts_coverage = {"error": f"{type(exc).__name__}: {exc}",
                          "unsatisfied_required_count": 0,
                          "status": "error"}
    parts_unsatisfied = parts_coverage.get("unsatisfied_required_count") or 0

    ir_clean = (lint_strong == 0 and len(family_blocking) == 0
                and len(smells_blocking) == 0
                and len(ap_strong) == 0
                and parts_unsatisfied == 0)
    env.last_ir_lint_clean = ir_clean
    env.last_parts_unsatisfied_count = int(parts_unsatisfied)
    env.last_parts_ir_hash = env.current_ir_hash
    snapshot_iter_idx = None
    if ir_clean:
        env.phase = _PHASE_PACKAGE_DRAFTING
        snapshot_iter_idx = len(env.verify_history)
        try:
            _snapshot_iter(env.agent_run_dir, snapshot_iter_idx,
                           kind="draft_clean",
                           discovery_dir=env.discovery_dir)
        except Exception as exc:
            print(f"[snapshot] failed iter_{snapshot_iter_idx}: {exc}",
                  flush=True)
        # Surface grounding warning even when ir_clean — submit_provenance
        # WILL refuse if these names are still ungrounded (no
        # vocabulary_notes entry).
        grounding_advisory = ""
        n_ung = grounding_summary.get("n_ungrounded", 0)
        if n_ung:
            grounding_advisory = (
                f" **GROUNDING WARNING**: {n_ung} declared name(s) are "
                f"ungrounded "
                f"(sorts={grounding_summary.get('ungrounded_sorts')}, "
                f"symbols={grounding_summary.get('ungrounded_symbols')}). "
                f"submit_provenance will REFUSE until each ungrounded name "
                f"is either (a) renamed to use a source token (e.g. "
                f"'LicenseRecipient' → 'LicenseRecipientCategory' if 'Category' "
                f"is canonical, or use source words like 'StockExchange' "
                f"directly) OR (b) documented in provenance.yaml under "
                f"`vocabulary_notes:` with explicit `note:` + `source_phrase:` "
                f"explaining which source phrase grounds the structural "
                f"abstraction. Plan now: rename or document. Canonical "
                f"convention names category sorts as `Xxx*Category` "
                f"(see canonical section_1_5)."
            )
        next_step_hint = (
            f"IR is clean (lint_strong=0, family/lowering OK after intent "
            f"override, no anti-patterns). PHASE → PACKAGE_DRAFTING. "
            f"Snapshot saved as iter_{snapshot_iter_idx}/. "
            f"**RECOMMENDED next step: call check_ir_vs_strategy()** to "
            f"verify the IR realises the strategy commitments (catches "
            f"drift like strategy saying 'declare 4 relations' when IR has "
            f"only 2). If consistent/minor_drift, proceed to "
            f"submit_provenance → submit_waivers → run_package_checks. If "
            f"n_missing_strong > 0, re-submit IR with the missing items."
            + grounding_advisory
        )
    else:
        ap_summary = ""
        if ap_strong:
            ap_kinds = sorted({f["kind"] for f in ap_strong})
            ap_summary = (
                f", anti_patterns_strong={len(ap_strong)} "
                f"({','.join(ap_kinds)})")
        budget_used_pct = (env.current_step / env.max_steps) if env.max_steps else 0
        if budget_used_pct < 0.5:
            budget_msg = (
                f" [step {env.current_step}/{env.max_steps}, only "
                f"{int(budget_used_pct * 100)}% of budget used — plenty "
                f"of room to iterate. Read the anti-pattern fix messages "
                f"above and apply them; do NOT finalize as failed_after_meta]")
        else:
            budget_msg = (
                f" [step {env.current_step}/{env.max_steps}, "
                f"{int(budget_used_pct * 100)}% of budget used — be "
                f"efficient but still iterate, don't bail prematurely]")
        next_step_hint = (
            f"IR is NOT clean (lint_strong={lint_strong}, "
            f"family_blocking={len(family_blocking)}, smells_blocking="
            f"{len(smells_blocking)}{ap_summary}). PHASE = IR_IN_FLUX. "
            f"Fix the issues and re-submit. submit_provenance/submit_waivers/"
            f"run_package_checks will be REJECTED until IR clean."
            + budget_msg
        )
    latest = _latest_strategy_path(env.discovery_dir)
    strategy_excerpt = ""
    strategy_version = None
    if latest is not None:
        strategy_text = latest.read_text(encoding="utf-8")
        strategy_version = int(re.match(r"strategy_v(\d+)\.md$", latest.name).group(1))

        def extract_section(num: int) -> str:
            m = re.search(rf"^##\s+{num}\.[^\n]*\n(.*?)(?=^##\s+\d+\.|^# |\Z)",
                          strategy_text, flags=re.MULTILINE | re.DOTALL)
            return m.group(0).strip() if m else ""
        s4 = extract_section(4)[:1500]
        s5 = extract_section(5)[:1500]
        strategy_excerpt = (
            f"### strategy_v{strategy_version}.md — Section 4 (per-clause):\n"
            f"{s4}\n\n"
            f"### strategy_v{strategy_version}.md — Section 5 (critic feedback):\n"
            f"{s5}"
        )

    role_frame = _load_json(env.discovery_dir / "role_frame.json") or {}
    directives = role_frame.get("drafter_directives") or []
    expected_sorts = (role_frame.get("ontology_budget") or {}).get(
        "expected_total_sorts")
    expected_entities = (role_frame.get("ontology_budget") or {}).get(
        "expected_total_entities")
    actual_sorts = len(re.findall(r"^\s*sort\s+\w+", ir_text, flags=re.MULTILINE))
    actual_entities = len(re.findall(r"^\s*entity\s+\w+", ir_text, flags=re.MULTILINE))

    role_frame_compliance: dict[str, Any] = {
        "active_strategy_version": strategy_version,
        "active_strategy_excerpt": strategy_excerpt,
        "drafter_directives": directives,
        "ontology_budget_check": {
            "expected_sorts": expected_sorts,
            "actual_sorts": actual_sorts,
            "expected_entities": expected_entities,
            "actual_entities": actual_entities,
        },
    }
    budget_warnings: list[str] = []
    if isinstance(expected_sorts, int) and actual_sorts > expected_sorts + 2:
        budget_warnings.append(
            f"sort count ({actual_sorts}) exceeds role_frame budget "
            f"({expected_sorts}) by >2 — possible ontology inflation")
    if isinstance(expected_entities, int) and actual_entities > expected_entities + 2:
        budget_warnings.append(
            f"entity count ({actual_entities}) exceeds role_frame budget "
            f"({expected_entities}) by >2 — possible ontology inflation")
    if budget_warnings:
        role_frame_compliance["budget_warnings"] = budget_warnings

    return {
        "ir_chars": len(ir_text),
        "ir_lines": ir_text.count("\n"),
        "parser": {"returncode": steps[0]["returncode"]},
        "semantic_lint": {
            "total": lint.get("summary", {}).get("total_findings"),
            "strong": lint_strong,
            "soft": lint.get("summary", {}).get("soft_findings"),
            "report_excerpt": lint_md,
        },
        "family_coverage": {
            "n_required_gaps": family.get("n_required_gaps"),
            "n_advisory_gaps": family.get("n_advisory_gaps"),
            "required_gaps": raw_required_gaps,
            "blocking_after_intent_override": len(family_blocking),
        },
        "lowering_audit": {
            "n_smells": lowering.get("n_smells"),
            "blocking_after_intent_override": len(smells_blocking),
        },
        "anti_patterns": {
            "strong": ap_strong,
            "soft": ap_soft,
            "n_strong": len(ap_strong),
            "n_soft": len(ap_soft),
        },
        "grounding": grounding_summary,
        "parts_inventory": {
            "status": parts_coverage.get("status"),
            "required_count": parts_coverage.get("required_count"),
            "unsatisfied_required_count": parts_unsatisfied,
            "unsatisfied_required": parts_coverage.get("unsatisfied_required", [])[:8],
            "artifact_md": "parts_inventory_coverage_v1.md",
        },
        "role_frame_compliance": role_frame_compliance,
        "iter_snapshot_idx": snapshot_iter_idx,
        "current_phase": env.phase,
        "ir_clean": ir_clean,
        "next_step": next_step_hint,
    }


def tool_check_ir_vs_strategy(env: ToolEnv) -> dict[str, Any]:
    """Compare current IR against latest strategy version."""
    if env.client is None:
        return {"error": "intra-tool LLM client not configured"}
    ir_path = env.agent_run_dir / "main_ir.a4v3"
    if not ir_path.exists() or ir_path.stat().st_size == 0:
        return {"error": "no IR submitted yet — call submit_ir_for_lint first"}
    latest = _latest_strategy_path(env.discovery_dir)
    if latest is None:
        return {"error": "no strategy_v*.md — call compose_strategy first"}

    ir_text = ir_path.read_text(encoding="utf-8")
    strategy_text = latest.read_text(encoding="utf-8")
    strategy_version = int(re.match(r"strategy_v(\d+)\.md$", latest.name).group(1))
    claim_ledger = _load_json(env.discovery_dir / "claim_ledger.json")
    parts_inventory = ensure_parts_inventory(env)

    ledger_block = ""
    if claim_ledger:
        ledger_block = (
            f"## CLAIM LEDGER (source-truth — IR MUST honor each claim's "
            f"event_status / carrier_policy)\n\n"
            f"```json\n"
            f"{json.dumps(claim_ledger, indent=2, ensure_ascii=False)[:3500]}\n"
            f"```\n\n"
            f"For any claim with event_status='possible_or_authorized' "
            f"or 'obligated': the canonical pattern (e.g. section_1_5) "
            f"uses ONE singleton class/program entity per carrier (e.g. "
            f"`entity LicensesToUseIndex... : LicenseClass`, `entity "
            f"...Issuance : LicenseIssuance`) PLUS role-wiring facts "
            f"between this singleton and recipient/use enums. This is "
            f"EXPECTED — not over-assertion. Flag (severity=strong) ONLY "
            f"if the IR declares MULTIPLE per-occurrence entities of the "
            f"same carrier sort with facts asserting each happened "
            f"(e.g. `entity IssuanceJan15`, `entity IssuanceFeb22` + "
            f"`fact occurred_1: issuance_by(IssuanceJan15, ...)`). "
            f"That's the over-assertion. Do NOT flag canonical singleton+"
            f"wire-fact pattern.\n\n"
        )

    inventory_block = ""
    if parts_inventory:
        inventory_block = (
            f"## PARTS INVENTORY (deterministic contract)\n\n"
            f"```json\n"
            f"{json.dumps(parts_inventory, indent=2, ensure_ascii=False)[:5000]}\n"
            f"```\n\n"
            f"Every required card must be formalized, bridged, repaired, "
            f"or waived. Do not count comment/name-only mentions as "
            f"coverage.\n\n"
        )

    user = (
        f"## IR (current)\n\n```\n{ir_text}\n```\n\n"
        f"## STRATEGY (strategy_v{strategy_version}.md — latest version)\n\n"
        f"```markdown\n{strategy_text}\n```\n\n"
        + ledger_block
        + inventory_block
        + f"## YOUR TASK\n\n"
        f"Compare IR vs strategy AND vs claim_ledger. Report what items "
        f"appear in IR, what's missing, and what IR has extra. Apply the "
        f"3 anti-patterns from your prompt: (1) concrete-instance-of-"
        f"deontic-carrier, (2) generic-indexed-entity-name, (3) "
        f"permission-as-value. Severity per guide. Output JSON per schema."
    )
    try:
        result = env.client.complete(
            [],
            raw_messages=[{"role": "system", "content": _CHECK_IR_VS_STRATEGY_SYSTEM},
                          {"role": "user", "content": user}],
            max_tokens=4500,
            extra_body=env.extra_body,
            seed=env.seed,
        )
    except Exception as exc:
        return {"error": f"{type(exc).__name__}: {exc}"}

    raw = _strip_code_fence(result.text or "")
    try:
        parsed = json.loads(raw)
    except Exception as exc:
        return {"error": f"check returned non-JSON: {exc}",
                "raw_excerpt": raw[:500]}

    parts_coverage = evaluate_inventory_coverage(env, ir_text, parts_inventory)
    parts_unsatisfied = parts_coverage.get("unsatisfied_required_count") or 0
    if parts_unsatisfied:
        missing = parsed.setdefault("missing_from_ir", [])
        for item in parts_coverage.get("unsatisfied_required") or []:
            missing.append({
                "item": f"parts_inventory:{item.get('id')} - {item.get('source_phrase')}",
                "severity": "strong",
                "where_in_strategy": "discovery/parts_inventory.json",
                "fix": (
                    f"Formalize relation/symbol/card in IR, or mark bridge/"
                    f"repair/waiver with artifact. Reason: {item.get('reason')}"
                ),
            })
        parsed["verdict"] = "major_drift"
        parsed["parts_inventory_coverage"] = {
            "status": parts_coverage.get("status"),
            "unsatisfied_required_count": parts_unsatisfied,
            "artifact": "parts_inventory_coverage_v1.md",
        }

    check_n = len(list(env.agent_run_dir.glob("ir_vs_strategy_check_v*.json")))
    out_json = env.agent_run_dir / f"ir_vs_strategy_check_v{check_n}.json"
    out_json.write_text(json.dumps(parsed, indent=2, ensure_ascii=False) + "\n",
                        encoding="utf-8")

    md_lines = [
        f"# IR vs Strategy v{strategy_version} consistency check (run {check_n})",
        "",
        f"- Verdict: **{parsed.get('verdict', 'unknown')}**",
        f"- Summary: {parsed.get('summary', '')}",
        "",
        "## Matches", "",
    ]
    for m in parsed.get("matches") or []:
        md_lines.append(f"- ✓ {m.get('item')} ({m.get('where_in_strategy')} → {m.get('where_in_ir')})")
    md_lines.extend(["", "## Missing from IR", ""])
    for m in parsed.get("missing_from_ir") or []:
        md_lines.append(
            f"- [{m.get('severity','?')}] **{m.get('item')}** "
            f"(strategy {m.get('where_in_strategy')})\n"
            f"    fix: {m.get('fix')}")
    md_lines.extend(["", "## Extra in IR (not in strategy)", ""])
    for m in parsed.get("extra_in_ir") or []:
        md_lines.append(
            f"- [{m.get('severity','?')}] {m.get('item')} "
            f"(IR {m.get('where_in_ir')})\n"
            f"    rationale: {m.get('rationale')}")
    out_md = env.agent_run_dir / f"ir_vs_strategy_check_v{check_n}.md"
    out_md.write_text("\n".join(md_lines), encoding="utf-8")

    n_strong_missing = sum(1 for m in (parsed.get("missing_from_ir") or [])
                            if m.get("severity") == "strong")
    n_soft_missing = sum(1 for m in (parsed.get("missing_from_ir") or [])
                          if m.get("severity") == "soft")

    llm_verdict = parsed.get("verdict")
    if n_strong_missing > 0:
        effective_verdict = "major_drift"
        verdict_override_reason = (
            f"forced to major_drift: {n_strong_missing} strong-severity "
            f"items missing (LLM said {llm_verdict!r} but that contradicts "
            f"the counts)") if llm_verdict != "major_drift" else None
    elif n_soft_missing > 2:
        effective_verdict = "minor_drift"
        verdict_override_reason = (
            f"forced to minor_drift: {n_soft_missing} soft items missing"
            ) if llm_verdict == "consistent" else None
    else:
        effective_verdict = llm_verdict or "consistent"
        verdict_override_reason = None

    can_proceed = (effective_verdict in {"consistent", "minor_drift"}
                   and n_strong_missing == 0)

    env.last_check_strong_missing = n_strong_missing
    env.last_check_ir_hash = env.current_ir_hash
    env.last_parts_unsatisfied_count = int(parts_unsatisfied)
    env.last_parts_ir_hash = env.current_ir_hash

    return {
        "verdict": effective_verdict,
        "llm_verdict_raw": llm_verdict,
        "verdict_override_reason": verdict_override_reason,
        "summary": parsed.get("summary"),
        "n_matches": len(parsed.get("matches") or []),
        "n_missing_strong": n_strong_missing,
        "n_missing_soft": n_soft_missing,
        "n_extra": len(parsed.get("extra_in_ir") or []),
        "parts_inventory": {
            "unsatisfied_required_count": parts_unsatisfied,
            "status": parts_coverage.get("status"),
            "artifact_md": "parts_inventory_coverage_v1.md",
        },
        "missing_strong": [
            {"item": m.get("item"), "fix": m.get("fix")}
            for m in (parsed.get("missing_from_ir") or [])
            if m.get("severity") == "strong"
        ],
        "can_proceed_to_provenance": can_proceed,
        "artifact_md": str(out_md.relative_to(env.agent_run_dir)),
        "instruction": (
            f"Strategy↔IR check: verdict={effective_verdict}, "
            f"strong_missing={n_strong_missing}. "
            + (
                "**STOP — n_missing_strong > 0**. Do NOT proceed to "
                "submit_provenance/run_package_checks. Re-submit_ir_for_lint "
                "with the strong-missing items added (see missing_strong "
                "list above for fixes). Then re-run check_ir_vs_strategy. "
                "Only when n_missing_strong == 0 may you proceed."
                if n_strong_missing > 0 else
                "✓ OK to proceed to submit_provenance → submit_waivers → "
                "run_package_checks."
            )
        ),
    }
