"""Role-frame, re-analysis, and claim-ledger tools."""
from __future__ import annotations

import json
from typing import Any

from ir_agent.env import ToolEnv
from ir_agent.helpers import _load_json, _read_text, _strip_code_fence, _utcnow
from ir_agent.modal_patterns import _collect_corpus_precedents_for_classifier
from ir_agent.parts_inventory import ensure_parts_inventory
from ir_agent.prompts.claim_ledger import _CLAIM_LEDGER_SYSTEM
from ir_agent.prompts.role_frame import (
    _RE_ANALYZE_ROLE_FRAME_SYSTEM,
    _ROLE_FRAME_SYSTEM,
)


def tool_analyze_role_frame(env: ToolEnv) -> dict[str, Any]:
    """Analyze the section's source to extract event-carrier and participant
    role structure BEFORE drafting IR. Persists to discovery/role_frame.json.

    GATE: submit_ir_for_lint will REFUSE until role_frame.json exists.

    Cached: if `discovery/role_frame.json` already exists with valid
    content, reuse it (no LLM call). Lets `--reuse-from <prior_run>`
    skip expensive xhigh re-runs of strategic analysis."""
    cached_path = env.discovery_dir / "role_frame.json"
    if cached_path.exists():
        cached = _load_json(cached_path)
        if cached and "error" not in cached and "_load_error" not in cached:
            mod = cached.get("modality") or {}
            ev = cached.get("event") or {}
            budget = cached.get("ontology_budget") or {}
            return {
                "_reused_cached": True,
                "event_carrier_sort": ev.get("reify_as_sort"),
                "event_carrier_kind": ev.get("carrier_kind"),
                "modality_family": mod.get("family"),
                "modality_kind": mod.get("kind"),
                "participant_count": len(cached.get("participants") or []),
                "expected_total_sorts": budget.get("expected_total_sorts"),
                "expected_total_entities": budget.get("expected_total_entities"),
                "drafter_directives": cached.get("drafter_directives") or [],
                "instruction": (
                    "role_frame.json reused from cache. Re-read full detail "
                    "via read_my_notes('role_frame'). Next: compose_strategy."
                ),
            }
    if env.client is None:
        return {"error": "intra-tool LLM client not configured"}
    source = _read_text(env.section_dir / "source.md")
    if not source.strip():
        return {"error": "source.md missing or empty"}

    corpus_block = _collect_corpus_precedents_for_classifier(env, source)

    classification = _load_json(env.discovery_dir / "text_intent_classification.json")
    classification_excerpt = ""
    if classification:
        classification_excerpt = (
            "\n## TEXT-INTENT CLASSIFICATION (already done)\n"
            "Use this for modality consistency — your role_frame.modality "
            "should match the classifier's recommended_family.\n"
            f"```json\n{json.dumps({k: v for k, v in classification.items() if k != '_corpus_precedents_used'}, indent=2, ensure_ascii=False)[:1500]}\n```\n"
        )

    user = (
        f"## SECTION SOURCE\n\n{source}\n\n"
        f"## CORPUS PRECEDENTS (similar sections in DZ — how they reified events/roles)\n\n{corpus_block}\n"
        f"{classification_excerpt}\n"
        f"Produce the role_frame JSON per the schema. Be CONSERVATIVE on "
        f"ontology — each new sort/entity must cite a verbatim source "
        f"phrase. Document rejected_temptations explicitly so the human "
        f"reviewer can see what you considered but deliberately did not "
        f"add."
    )
    _client, _xb, _mt = env.strategic_or_main(4000)
    try:
        result = _client.complete(
            [],
            raw_messages=[{"role": "system", "content": _ROLE_FRAME_SYSTEM},
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
        return {"error": f"role_frame returned non-JSON: {exc}",
                "raw_excerpt": raw[:500]}

    forbidden_pm_phrases = [
        "as text", "as a string", "as a phrase", "as a quote",
        "string-valued", "string field", "text field", "phrase-level",
        "preserve as quote", "preserve as text", "preserve the phrase",
        "carry the quoted", "scope/purpose text", "purpose text",
        "purpose phrase", "vague slot", "scope text", "scope phrase",
        "scope/purpose field", "scope field",
    ]
    pm_violations: list[str] = []
    for i, p in enumerate(parsed.get("participants") or []):
        pm = (p.get("proposed_modeling") or "").lower()
        for phrase in forbidden_pm_phrases:
            if phrase in pm:
                pm_violations.append(
                    f"participant[{i}].role={p.get('role')!r} "
                    f"proposed_modeling contains forbidden phrase {phrase!r}: "
                    f"{p.get('proposed_modeling')[:140]!r}. Replace with "
                    f"a typed sort/entity/enum (e.g. 'sort LicenseUseCategory "
                    f"with enum subtypes [...]').")
                break
    if pm_violations:
        return {
            "error": (
                "role_frame violates HARD RULE on proposed_modeling: "
                "vague typing words detected which lead to string literals "
                "in IR. Re-run with concrete sort/entity/enum proposals."
            ),
            "violations": pm_violations,
        }

    mod = parsed.get("modality") or {}
    fam = (mod.get("family") or "").strip()
    abs_dec = (mod.get("absorption_decision") or "").strip()
    if fam == "DeonticDecl" and abs_dec != "preserve_as_first_class":
        return {
            "error": (
                f"role_frame violates HARD RULE on modality: family="
                f"'DeonticDecl' requires absorption='preserve_as_first_class' "
                f"(use a permission/obligation/prohibition block), but "
                f"frame proposed absorption='{abs_dec}'. This conflict is "
                f"empirically grounded: all 5 DZ canonical sections with "
                f"may/shall modals use DeonticDecl blocks; bare-fact + "
                f"waiver makes judges read the IR as 'agent claims this "
                f"HAS occurred' which over-asserts a permission. Re-run "
                f"analyze_role_frame and choose preserve_as_first_class."
            ),
            "rejected_frame_excerpt": json.dumps(mod, ensure_ascii=False),
        }
    event_obj = parsed.get("event") or {}
    reify_as_what = (event_obj.get("reify_as_what") or "").strip()
    if fam == "DeonticDecl" and reify_as_what == "event_instance":
        return {
            "error": (
                f"role_frame violates HARD RULE on event.reify_as_what: "
                f"family='DeonticDecl' (kind={mod.get('kind')!r}) demands "
                f"reify_as_what ∈ {{event_class, scope_carrier}}, NEVER "
                f"event_instance. event_instance means MULTIPLE per-"
                f"occurrence entities each asserting a specific event "
                f"happened, which over-states a permissive source. "
                f"Re-run with reify_as_what='event_class' — canonical "
                f"(e.g. section_1_5) declares ONE singleton class/program "
                f"entity per carrier (e.g. `entity ...Issuance : "
                f"LicenseIssuance`) PLUS role-wiring facts between it "
                f"and recipient/use enums. The singleton represents THE "
                f"class of permissible events; the wire-facts define "
                f"class structure (not occurrence). Permission references "
                f"the singleton via `scope: <singleton_entity>`."
            ),
            "rejected_frame_excerpt": json.dumps(event_obj, ensure_ascii=False),
        }
    conservatism_warnings: list[str] = []
    for i, p in enumerate(parsed.get("participants") or []):
        just = (p.get("source_phrase_justifying_each_new_sort") or "").strip()
        if not just:
            conservatism_warnings.append(
                f"participant[{i}].role={p.get('role')!r} has no "
                f"source_phrase_justifying_each_new_sort — drafter cannot "
                f"verify the new sort was demanded by source")
            continue
        if just.lower().startswith("no new sort"):
            continue
        words = just.split()[:4]
        probe = " ".join(words).lower()
        if probe and probe not in source.lower():
            conservatism_warnings.append(
                f"participant[{i}].role={p.get('role')!r}: cited "
                f"justification '{just[:80]}' does not match any verbatim "
                f"source phrase — possible ontology inflation")

    parsed["_conservatism_warnings"] = conservatism_warnings
    parsed["_corpus_precedents_used"] = corpus_block[:2000]
    (env.discovery_dir / "role_frame.json").write_text(
        json.dumps(parsed, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8")

    summary_lines: list[str] = []
    ev = parsed.get("event") or {}
    summary_lines.append(f"## Event")
    summary_lines.append(f"- carrier_kind: {ev.get('carrier_kind')}")
    summary_lines.append(f"- reify_as_sort: {ev.get('reify_as_sort')}")
    summary_lines.append(f"- source_phrase: \"{ev.get('source_phrase','')}\"")
    summary_lines.append(f"- rationale: {ev.get('reify_rationale','')}")
    mod = parsed.get("modality") or {}
    summary_lines.append("\n## Modality")
    summary_lines.append(f"- in_source: {mod.get('expression_in_source')}")
    summary_lines.append(f"- family: {mod.get('family')} / kind: {mod.get('kind')}")
    summary_lines.append(f"- absorption: {mod.get('absorption_decision')}")
    summary_lines.append(f"- rationale: {mod.get('absorption_rationale','')}")
    summary_lines.append("\n## Participants")
    for p in parsed.get("participants") or []:
        summary_lines.append(
            f"- role={p.get('role')!r} :: source=\"{p.get('source_phrase','')}\"\n"
            f"    methodology_ctx: {p.get('methodology_context','')}\n"
            f"    general_role: {p.get('general_world_role','')}\n"
            f"    proposed_modeling: {p.get('proposed_modeling','')}\n"
            f"    justification: {p.get('source_phrase_justifying_each_new_sort','')}")
    budget = parsed.get("ontology_budget") or {}
    summary_lines.append("\n## Ontology budget")
    summary_lines.append(f"- new_sorts: {budget.get('proposed_new_sorts')}")
    summary_lines.append(f"- new_entities: {budget.get('proposed_new_entities')}")
    summary_lines.append(f"- expected_total_sorts: {budget.get('expected_total_sorts')}")
    summary_lines.append(f"- expected_total_entities: {budget.get('expected_total_entities')}")
    rej = budget.get("rejected_temptations") or []
    if rej:
        summary_lines.append("- rejected_temptations:")
        for r in rej:
            summary_lines.append(f"    - {r.get('considered')!r}: {r.get('why_rejected','')}")
    summary_lines.append("\n## Drafter directives (MUST follow)")
    for d in parsed.get("drafter_directives") or []:
        summary_lines.append(f"- {d}")
    if conservatism_warnings:
        summary_lines.append("\n## Conservatism warnings (review before drafting)")
        for w in conservatism_warnings:
            summary_lines.append(f"- {w}")
    summary_md = "\n".join(summary_lines)
    (env.discovery_dir / "role_frame.md").write_text(summary_md, encoding="utf-8")

    return {
        "event_carrier_sort": ev.get("reify_as_sort"),
        "event_carrier_kind": ev.get("carrier_kind"),
        "modality_family": mod.get("family"),
        "modality_kind": mod.get("kind"),
        "participant_count": len(parsed.get("participants") or []),
        "expected_total_sorts": budget.get("expected_total_sorts"),
        "expected_total_entities": budget.get("expected_total_entities"),
        "drafter_directives": parsed.get("drafter_directives") or [],
        "conservatism_warnings": conservatism_warnings,
        "summary_md": summary_md,
        "instruction": (
            "role_frame.json saved. Next step: call compose_strategy() "
            "to consolidate hints + role_frame + classification into "
            "strategy_v0.md, which is the single source of truth the "
            "drafter follows. The submit_ir_for_lint gate is OPEN only "
            "after strategy_v0.md exists."
        ),
    }


def tool_re_analyze_role_frame(env: ToolEnv) -> dict[str, Any]:
    """Re-analyze role_frame using verify findings as evidence — can
    CHANGE family.modality. Overwrites role_frame.json (prior version archived)."""
    if env.client is None:
        return {"error": "intra-tool LLM client not configured"}
    if not env.verify_history:
        return {"error": ("re_analyze_role_frame is only meaningful after "
                          "at least one run_package_checks; verify_history "
                          "is empty")}

    role_frame_path = env.discovery_dir / "role_frame.json"
    if not role_frame_path.exists():
        return {"error": "role_frame.json missing — call analyze_role_frame() first"}

    prev_frame = _load_json(role_frame_path) or {}
    source = _read_text(env.section_dir / "source.md")
    classification = _load_json(env.discovery_dir / "text_intent_classification.json")
    corpus_block = _collect_corpus_precedents_for_classifier(env, source)

    history_dissent = []
    for h in env.verify_history:
        for d in h.get("judge_dissent", []) or []:
            history_dissent.append({
                "round": h.get("round"),
                "model": d.get("model"),
                "verdict": d.get("verdict"),
                "specific_differences": (d.get("semantic_differences") or [])[:2],
            })

    user = (
        f"## SECTION SOURCE\n\n{source}\n\n"
        f"## PREVIOUS ROLE_FRAME (the one verify findings discredit)\n\n"
        f"```json\n{json.dumps(prev_frame, indent=2, ensure_ascii=False)[:4000]}\n```\n\n"
        f"## VERIFY DISSENT ACROSS ALL ROUNDS\n\n"
        f"```json\n{json.dumps(history_dissent, indent=2, ensure_ascii=False)[:5000]}\n```\n\n"
        f"## CLASSIFIER OUTPUT (may also be wrong)\n\n"
        f"```json\n{json.dumps(classification or {}, indent=2, ensure_ascii=False)[:2500]}\n```\n\n"
        f"## CORPUS PRECEDENTS\n\n{corpus_block[:3000]}\n\n"
        f"## YOUR TASK\n\n"
        f"Produce a NEW role_frame JSON. Treat the dissent as evidence "
        f"about which family the source actually demands. If multiple "
        f"judges across rounds say the same thing about modality "
        f"(e.g. 'source is permissive, IR over-asserts'), that's strong "
        f"evidence to switch family. Add 'reanalysis_rationale' field."
    )
    _client, _xb, _mt = env.strategic_or_main(4500)
    try:
        result = _client.complete(
            [],
            raw_messages=[{"role": "system", "content": _RE_ANALYZE_ROLE_FRAME_SYSTEM},
                          {"role": "user", "content": user}],
            max_tokens=_mt,
            extra_body=_xb,
            seed=env.seed,
        )
    except Exception as exc:
        return {"error": f"{type(exc).__name__}: {exc}"}

    raw = _strip_code_fence(result.text or "")
    try:
        new_frame = json.loads(raw)
    except Exception as exc:
        return {"error": f"re_analyze returned non-JSON: {exc}",
                "raw_excerpt": raw[:500]}

    new_mod = new_frame.get("modality") or {}
    fam = (new_mod.get("family") or "").strip()
    abs_dec = (new_mod.get("absorption_decision") or "").strip()
    if fam == "DeonticDecl" and abs_dec != "preserve_as_first_class":
        return {
            "error": (
                f"re_analyzed frame violates HARD RULE: family='DeonticDecl' "
                f"requires absorption='preserve_as_first_class'; got "
                f"absorption='{abs_dec}'. Re-run."
            ),
        }

    prev_fam = (prev_frame.get("modality") or {}).get("family")
    family_changed = prev_fam != fam
    prev_kind = (prev_frame.get("modality") or {}).get("kind")
    new_kind = new_mod.get("kind")
    kind_changed = prev_kind != new_kind

    archive_path = env.discovery_dir / f"role_frame_pre_reanalysis_v{env.meta_evaluations_done}.json"
    if not archive_path.exists():
        archive_path.write_text(json.dumps(prev_frame, indent=2, ensure_ascii=False),
                                encoding="utf-8")

    new_frame["_reanalysis_run_at"] = _utcnow()
    new_frame["_previous_family"] = prev_fam
    new_frame["_previous_kind"] = prev_kind
    role_frame_path.write_text(json.dumps(new_frame, indent=2, ensure_ascii=False) + "\n",
                                encoding="utf-8")

    if (env.discovery_dir / "claim_ledger.json").exists():
        ensure_parts_inventory(env, force=True)

    env.amends_within_same_family = 0

    return {
        "previous_family": prev_fam,
        "new_family": fam,
        "family_changed": family_changed,
        "previous_kind": prev_kind,
        "new_kind": new_kind,
        "kind_changed": kind_changed,
        "reanalysis_rationale": new_frame.get("reanalysis_rationale", ""),
        "instruction": (
            "role_frame.json overwritten with new family/modality decision. "
            "The previous frame was archived to "
            f"{archive_path.name}. **Now call compose_strategy() (or "
            "amend_strategy if you prefer to inherit prior sections)** to "
            "regenerate the strategy under the new frame, THEN submit_ir_for_lint."
        ),
    }


def tool_extract_claim_ledger(env: ToolEnv) -> dict[str, Any]:
    """Extract a source-backed claim ledger BEFORE IR drafting.

    Cached: if `discovery/claim_ledger.json` exists and valid, reuse."""
    cached_path = env.discovery_dir / "claim_ledger.json"
    if cached_path.exists():
        cached = _load_json(cached_path)
        if cached and "error" not in cached and "_load_error" not in cached:
            inventory = ensure_parts_inventory(env)
            n_claims = len(cached.get("claims") or [])
            n_deontic = sum(
                1 for c in (cached.get("claims") or [])
                if c.get("event_status") in {"possible_or_authorized",
                                              "obligated", "prohibited"})
            return {
                "_reused_cached": True,
                "n_claims": n_claims,
                "n_deontic_claims": n_deontic,
                "parts_inventory_cards": len(inventory.get("cards") or []),
                "summary": cached.get("ledger_summary"),
                "instruction": (
                    "claim_ledger.json reused from cache. parts_inventory "
                    "is present/refreshed if needed. Next step: "
                    "compose_strategy."
                ),
            }
    if env.client is None:
        return {"error": "intra-tool LLM client not configured"}
    role_frame = _load_json(env.discovery_dir / "role_frame.json")
    if not role_frame:
        return {"error": "role_frame.json missing — call analyze_role_frame() first"}
    source = _read_text(env.section_dir / "source.md")
    if not source.strip():
        return {"error": "source.md empty"}

    user = (
        f"## SECTION SOURCE\n\n{source}\n\n"
        f"## ROLE_FRAME (compact)\n\n```json\n"
        f"{json.dumps({k: v for k, v in role_frame.items() if not k.startswith('_')}, indent=2, ensure_ascii=False)[:3000]}\n"
        f"```\n\n"
        f"## YOUR TASK\n\n"
        f"Extract the claim ledger per the schema. Be especially careful "
        f"with event_status: 'may be Xed by Y' is "
        f"possible_or_authorized + class_or_program, NOT actual + instance."
    )
    try:
        result = env.client.complete(
            [],
            raw_messages=[{"role": "system", "content": _CLAIM_LEDGER_SYSTEM},
                          {"role": "user", "content": user}],
            max_tokens=4000,
            extra_body=env.extra_body,
            seed=env.seed,
        )
    except Exception as exc:
        return {"error": f"{type(exc).__name__}: {exc}"}

    raw = _strip_code_fence(result.text or "")
    try:
        parsed = json.loads(raw)
    except Exception as exc:
        return {"error": f"claim_ledger returned non-JSON: {exc}",
                "raw_excerpt": raw[:500]}

    violations = []
    valid_status = {"actual", "possible_or_authorized", "obligated",
                    "prohibited", "class_only", "definitional"}
    valid_policy = {"class_or_program", "instance", "none"}
    for i, c in enumerate(parsed.get("claims") or []):
        es = c.get("event_status", "")
        cp = c.get("carrier_policy", "")
        if es not in valid_status:
            violations.append(f"claim[{i}]: invalid event_status={es!r}")
        if cp not in valid_policy:
            violations.append(f"claim[{i}]: invalid carrier_policy={cp!r}")
        if es in {"possible_or_authorized", "obligated", "prohibited"} \
                and cp == "instance":
            violations.append(
                f"claim[{i}] (text={c.get('text','')[:80]!r}): "
                f"event_status={es!r} requires carrier_policy="
                f"'class_or_program', got 'instance'. This combination "
                f"creates a concrete instance of a deontic event, "
                f"contradicting its modal force.")
    if violations:
        return {"error": "claim_ledger has invalid combinations",
                "violations": violations}

    out_json = env.discovery_dir / "claim_ledger.json"
    out_json.write_text(json.dumps(parsed, indent=2, ensure_ascii=False) + "\n",
                         encoding="utf-8")
    md_lines = [f"# Claim ledger — {env.original_entry_id}", "",
                f"Summary: {parsed.get('ledger_summary','')}", ""]
    for c in parsed.get("claims") or []:
        md_lines.append(f"## {c.get('id','?')}")
        md_lines.append(f"- text: \"{c.get('text','')}\"")
        md_lines.append(f"- modality: {c.get('modality')}")
        md_lines.append(f"- event_status: **{c.get('event_status')}**")
        md_lines.append(f"- carrier_policy: **{c.get('carrier_policy')}**")
        md_lines.append(f"- explicit_modal: {c.get('explicit_modal')}")
        md_lines.append(f"- roles: {json.dumps(c.get('roles') or {}, ensure_ascii=False)}")
        md_lines.append(f"- rationale: {c.get('rationale')}")
        md_lines.append("")
    out_md = env.discovery_dir / "claim_ledger.md"
    out_md.write_text("\n".join(md_lines), encoding="utf-8")
    inventory = ensure_parts_inventory(env, force=True)

    n_claims = len(parsed.get("claims") or [])
    n_deontic = sum(1 for c in (parsed.get("claims") or [])
                     if c.get("event_status") in {"possible_or_authorized",
                                                    "obligated", "prohibited"})
    return {
        "n_claims": n_claims,
        "n_deontic_claims": n_deontic,
        "summary": parsed.get("ledger_summary"),
        "parts_inventory_cards": len(inventory.get("cards") or []),
        "parts_inventory_unknown_symbols": (
            (inventory.get("symbol_resolution") or {}).get("unknown_count")
        ),
        "artifact_md": str(out_md.relative_to(env.agent_run_dir)),
        "instruction": (
            "Claim ledger and parts_inventory saved. The drafter and "
            "check_ir_vs_strategy now have an explicit source-truth about each claim's "
            "event_status (actual / possible_or_authorized / etc.) and "
            "carrier_policy (instance vs class_or_program). The drafter "
            f"MUST NOT promote {n_deontic} possible_or_authorized/"
            f"obligated/prohibited claim(s) to concrete-instance facts. "
            "Next step: compose_strategy → submit_ir_for_lint."
        ),
    }
