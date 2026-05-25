"""TOOL_REGISTRY and tool_schemas() — single source of truth for the
29 tool names + their OpenAI JSON-schema signatures."""
from __future__ import annotations

from typing import Any, Callable

from ir_agent.tools.analysis import (
    tool_analyze_role_frame, tool_extract_claim_ledger,
    tool_re_analyze_role_frame,
)
from ir_agent.tools.classification import tool_classify_text_intent
from ir_agent.tools.discovery import (
    tool_curate_starter_pack, tool_get_a4v3_family, tool_list_a4v3_families,
    tool_list_sections, tool_read_section, tool_search_corpus,
    tool_search_failures, tool_search_successes, tool_semantic_search,
)
from ir_agent.tools.drafting import (
    tool_check_ir_vs_strategy, tool_submit_ir_for_lint,
)
from ir_agent.tools.history import tool_analyze_attempt_history
from ir_agent.tools.iters import tool_compare_iters, tool_rollback_to_iter
from ir_agent.tools.meta import (
    tool_finalize, tool_meta_evaluate, tool_parallel_critique,
)
from ir_agent.tools.package import (
    tool_run_package_checks, tool_submit_provenance, tool_submit_waivers,
)
from ir_agent.tools.planning import tool_amend_strategy, tool_compose_strategy
from ir_agent.tools.workspace import (
    tool_read_bridge, tool_read_my_notes, tool_read_user_hints, tool_save_note,
)


TOOL_REGISTRY: dict[str, Callable[..., dict[str, Any]]] = {
    "read_section": tool_read_section,
    "list_sections": tool_list_sections,
    "search_corpus": tool_search_corpus,
    "search_successes": tool_search_successes,
    "search_failures": tool_search_failures,
    "semantic_search": tool_semantic_search,
    "curate_starter_pack": tool_curate_starter_pack,
    "get_a4v3_family": tool_get_a4v3_family,
    "list_a4v3_families": tool_list_a4v3_families,
    "classify_text_intent": tool_classify_text_intent,
    "analyze_role_frame": tool_analyze_role_frame,
    "re_analyze_role_frame": tool_re_analyze_role_frame,
    "extract_claim_ledger": tool_extract_claim_ledger,
    "compose_strategy": tool_compose_strategy,
    "amend_strategy": tool_amend_strategy,
    "check_ir_vs_strategy": tool_check_ir_vs_strategy,
    "compare_iters": tool_compare_iters,
    "rollback_to_iter": tool_rollback_to_iter,
    "analyze_attempt_history": tool_analyze_attempt_history,
    "read_user_hints": tool_read_user_hints,
    "read_bridge": tool_read_bridge,
    "save_note": tool_save_note,
    "read_my_notes": tool_read_my_notes,
    "submit_ir_for_lint": tool_submit_ir_for_lint,
    "submit_provenance": tool_submit_provenance,
    "submit_waivers": tool_submit_waivers,
    "run_package_checks": tool_run_package_checks,
    "parallel_critique": tool_parallel_critique,
    "meta_evaluate": tool_meta_evaluate,
    "finalize": tool_finalize,
}


def tool_schemas() -> list[dict[str, Any]]:
    return [
        {"type": "function", "function": {
            "name": "read_section",
            "description": "Read a seed methodology section's artifacts (source/ir/provenance/notes/waivers). Use this to study how a similar section was translated.",
            "parameters": {"type": "object", "properties": {
                "section_id": {"type": "string", "description": "e.g. 'section_5_4', 'definitions/N11', 'N11'"},
                "include": {"type": "array", "items": {"type": "string", "enum": ["source", "ir", "provenance", "notes", "waivers"]}, "default": ["source"]},
            }, "required": ["section_id"]}}},
        {"type": "function", "function": {
            "name": "list_sections",
            "description": "List available seed methodology section IDs and definitions, plus which sections already have a translated IR.",
            "parameters": {"type": "object", "properties": {}}}},
        {"type": "function", "function": {
            "name": "search_corpus",
            "description": "Grep across seed methodology corpus (sections + definitions + bridge + policy by default) for a phrase. Returns line-level context with scope_path. Use to find precedents for a concept ('underlying value', 'permission', 'currency'). NOT included by default: agent_run_* — use search_failures for negative knowledge, search_successes for positive precedents from past auto runs.",
            "parameters": {"type": "object", "properties": {
                "query": {"type": "string"},
                "max_matches": {"type": "integer", "default": 10, "description": "1-30"},
                "scopes": {"type": "array", "items": {"type": "string", "enum": ["sections", "definitions", "bridge", "policy", "appendix", "user_hints"]}, "description": "default: [sections, definitions, bridge, policy]. Add 'user_hints' to grep across all human-provided hints (per IR/index/user_hints_contract.md)."},
            }, "required": ["query"]}}},
        {"type": "function", "function": {
            "name": "search_successes",
            "description": "Search the auto-curated catalog of past agent_accept_candidate runs (POSITIVE patterns). Each entry contains: source phrase + IR sketch + judges' verdict + key insight. Use to find proven patterns on similar phrases. Cheaper / more targeted than search_corpus when looking for 'what worked before'. Catalog file: agent_success_catalog.md.",
            "parameters": {"type": "object", "properties": {
                "query": {"type": "string"},
                "max_matches": {"type": "integer", "default": 5},
            }, "required": ["query"]}}},
        {"type": "function", "function": {
            "name": "search_failures",
            "description": "Search the auto-curated catalog of past failed_after_meta runs (ANTI-PATTERNS to AVOID). Each entry: source phrase + failed IR + WHY it failed (judges' specific complaints) + DO_NOT_REPEAT marker. Use to avoid known mistakes when working on similar source. opt-in — failed runs are NOT included in default search_corpus. Catalog file: agent_failure_catalog.md.",
            "parameters": {"type": "object", "properties": {
                "query": {"type": "string"},
                "max_matches": {"type": "integer", "default": 5},
            }, "required": ["query"]}}},
        {"type": "function", "function": {
            "name": "semantic_search",
            "description": "Embedding-based semantic search over THIS corpus (sections + definitions + bridge + provenance claims + translator notes + policy). Returns top-K most semantically similar chunks. Use for finding similar CONCEPTS or PATTERNS even when wording differs (substring grep won't catch). Cheaper than search_corpus for finding 'how was a similar concept handled'. The index is per-corpus and lives at <corpus_run_dir>/llm/embedding_index_v1.json; if the result includes an 'index not built' error, the index needs to be built once for this corpus via the build CLI.",
            "parameters": {"type": "object", "properties": {
                "query": {"type": "string"},
                "top_k": {"type": "integer", "default": 5},
                "kinds": {"type": "array", "items": {"type": "string", "enum": ["source", "main_ir", "provenance_claim", "translator_notes", "policy"]}, "description": "filter by chunk type"},
                "exclude_current_section": {"type": "boolean", "default": True},
            }, "required": ["query"]}}},
        {"type": "function", "function": {
            "name": "curate_starter_pack",
            "description": "Run a retrieval sub-agent to produce a CURATED bundle of best precedents for the current section. Combines multi-angle semantic searches (semantic match + IR pattern + provenance intent + translator notes) and asks an LLM to organise them by purpose with rationale. Auto-called once at run start (auto-prefetch); call manually only if stuck and need a deeper retrieval pass focused on a specific concern (pass focus_query). Result saved to discovery/curated_starter_pack.json.",
            "parameters": {"type": "object", "properties": {
                "focus_query": {"type": "string", "description": "optional focus query (e.g. 'modal possibility for licensing'); defaults to full source text"},
            }}}},
        {"type": "function", "function": {
            "name": "get_a4v3_family",
            "description": "Extract schema lines mentioning a specific A4V3 family (DeonticDecl, AssertDecl, etc.). Use this when you need to see the exact syntax for a family.",
            "parameters": {"type": "object", "properties": {
                "family_name": {"type": "string", "description": "e.g. 'DeonticDecl', 'permission', 'TemporalDecl'"},
            }, "required": ["family_name"]}}},
        {"type": "function", "function": {
            "name": "list_a4v3_families",
            "description": "Enumerate available A4V3 families and common constructs.",
            "parameters": {"type": "object", "properties": {}}}},
        {"type": "function", "function": {
            "name": "classify_text_intent",
            "description": "Classify the section's text type (legal/methodology/spec/definitional/mixed) and recommended modal-handling policy. Use this EARLY in DISCOVER, before drafting IR. Most methodology text is descriptive — modals are usually grammatical, NOT normative. This tool stops you from reflexively mapping every 'may'/'shall' to DeonticDecl when the source actually wants AssertDecl. Result is also saved as discovery/text_intent_classification.json.",
            "parameters": {"type": "object", "properties": {}}}},
        {"type": "function", "function": {
            "name": "analyze_role_frame",
            "description": "Analyze the source's event-carrier and participant-role structure BEFORE drafting IR. Forces explicit identification of: (a) the event/process the source describes (issuance/computation/classification/...); (b) WHO/WHAT plays each role (agent/recipient/target/instrument/scope); (c) for each entity, its role in the broader methodology corpus AND in general financial knowledge. Output: role_frame.json + role_frame.md + drafter_directives that the drafter MUST follow. CONSERVATISM: each proposed new sort/entity must cite a verbatim source phrase — token-coverage metrics will penalize ontology bloat. Call AFTER classify_text_intent so modality decisions are consistent. After analyze_role_frame, call compose_strategy.",
            "parameters": {"type": "object", "properties": {}}}},
        {"type": "function", "function": {
            "name": "re_analyze_role_frame",
            "description": "Re-analyze role_frame using verify findings as evidence — can CHANGE family.modality (e.g. AssertDecl → DeonticDecl). Use ONLY when 2+ amend_strategy rounds within the same family did not resolve dissent that targets family choice itself (multiple judges saying e.g. 'source is permissive but IR asserts as fact'). Overwrites role_frame.json (prior version archived). After this, call compose_strategy or amend_strategy to regenerate strategy under the new frame, then submit_ir_for_lint.",
            "parameters": {"type": "object", "properties": {}}}},
        {"type": "function", "function": {
            "name": "extract_claim_ledger",
            "description": "Extract source-backed claim ledger BEFORE IR drafting. Each claim has explicit event_status (actual / possible_or_authorized / obligated / prohibited / class_only / definitional) and carrier_policy (class_or_program vs instance vs none). This pins down the source-truth so the drafter cannot silently 'promote' a permissive 'may be issued' into a fact-asserted 'has been issued'. The ledger is consumed by check_ir_vs_strategy and amend_strategy as ground truth. Required after analyze_role_frame, before compose_strategy.",
            "parameters": {"type": "object", "properties": {}}}},
        {"type": "function", "function": {
            "name": "compose_strategy",
            "description": "Consolidate user hints + role_frame + text-intent classification into strategy_v0.md — the single source of truth the drafter follows. Required before submit_ir_for_lint (the gate refuses until at least strategy_v0 exists). Six fixed sections: (1) user hints verbatim, (2) entities and methodology role, (3) relationships, (4) per-clause translation strategy, (5) critic feedback (empty on v0), (6) open questions. The drafter reads ONLY this file — if you forget to write something, the drafter does not know it. Idempotent — calling twice overwrites v0; use amend_strategy for v1+.",
            "parameters": {"type": "object", "properties": {}}}},
        {"type": "function", "function": {
            "name": "amend_strategy",
            "description": "Amend the translation strategy after a failed VERIFY round — writes strategy_v{N+1}.md (NEW file, prior versions preserved for audit). Use when judges raised dissent that local IR fixes did not resolve, or when the structural approach itself appears wrong. The new strategy must propose a CONCRETE different drafter approach (e.g. 'use DeonticDecl block instead of bare fact'). Updates section 5 (critic feedback) with verify findings and section 6 (open questions). The drafter switches to the latest strategy version automatically. After 2-3 amendments without convergence, finalize as failed_after_meta.",
            "parameters": {"type": "object", "properties": {}}}},
        {"type": "function", "function": {
            "name": "check_ir_vs_strategy",
            "description": "Compare current IR against the latest strategy version. Returns structured report listing strategy items present in IR (matches), missing from IR (with severity + concrete fix), and extra in IR (not mentioned in strategy). Use AFTER submit_ir_for_lint comes back clean, BEFORE submit_provenance — to catch drift between strategy intent and IR realisation (e.g. strategy says 'declare 4 role relations' but drafter only declared 2). If n_missing_strong > 0, fix the IR via re-submit_ir_for_lint, then re-check. Persists ir_vs_strategy_check_v{N}.md as audit trail.",
            "parameters": {"type": "object", "properties": {}}}},
        {"type": "function", "function": {
            "name": "compare_iters",
            "description": "Compare two iter_<N>/ snapshots. Returns: declarations diff (added/removed/changed/unchanged) + verdict diff (which complaints resolved/regressed/new) + recommendation (often: rollback to better iter if regression detected). Use when run_package_checks shows regression_hint, or before rollback to confirm target. Iter snapshots are auto-created on every clean DRAFT and every VERIFY.",
            "parameters": {"type": "object", "properties": {
                "iter_a": {"type": "integer", "description": "first iter (typically the better/older one)"},
                "iter_b": {"type": "integer", "description": "second iter (typically the worse/newer one)"},
            }, "required": ["iter_a", "iter_b"]}}},
        {"type": "function", "function": {
            "name": "rollback_to_iter",
            "description": "Restore main_ir.a4v3 + provenance + waivers from iter_<N>/ snapshot. Use when current IR is worse than a prior iter (after compare_iters or regression_hint confirmed). The current IR is preserved as pre_rollback_<timestamp>.a4v3 for audit. After rollback, apply MINIMAL targeted fixes — do NOT rewrite working sections. Re-run package_checks afterward to confirm the verdict on this rolled-back IR (don't trust the iter's old verdict if you've changed anything).",
            "parameters": {"type": "object", "properties": {
                "iter_n": {"type": "integer", "description": "target iter to rollback to"},
                "reason": {"type": "string", "description": "short audit-log reason for the rollback (required)"},
            }, "required": ["iter_n", "reason"]}}},
        {"type": "function", "function": {
            "name": "analyze_attempt_history",
            "description": "Explicit cross-iter narrative: load ALL iter IRs + verdicts + per-judge dissent, synthesize what worked / what regressed / what to do next. Identifies proven_core (declarations in every good iter), regressions with hypothesized causes, persistent open dissent, and a concrete recommended_next_action (rollback_to_best / patch_best_iter / finalize_with_dissent_on_best / stop_iterating_judges_oppose_each_other). Cheap (one LLM call) and complements KDR (which is per-round). Use when stuck after 2+ rounds, OR before finalize when unsure if current IR is the best attempt, OR when regression_hint fires. Persists discovery/attempt_history_analysis.md + refreshes discovery/iter_scoreboard.md.",
            "parameters": {"type": "object", "properties": {}}}},
        {"type": "function", "function": {
            "name": "read_user_hints",
            "description": "Read user hints (plain-text directives from a human reviewer) from <section_dir>/user_hints/active.yaml, <agent_run_dir>/user_hints/active.yaml, or <run_root>/user_hints/active.yaml. Per IR/index/user_hints_contract.md: hints have hint_id, scope, text, status. If a hint changes how you would translate, you MUST cite hint_id in provenance/notes (auditability). If two hints conflict, do NOT guess — flag in agent_notes for human disambiguation. Call this in DISCOVER right after classify_text_intent.",
            "parameters": {"type": "object", "properties": {}}}},
        {"type": "function", "function": {
            "name": "read_bridge",
            "description": "Read the global bridge file (cross-section identity layer) and its provenance/translator notes.",
            "parameters": {"type": "object", "properties": {}}}},
        {"type": "function", "function": {
            "name": "save_note",
            "description": "Save your own intermediate observation to discovery/<name>.md. Use this to externalize what you've learned (text_context, entities, vocabulary_plan, strategy, etc.) so you can refer back without re-reasoning.",
            "parameters": {"type": "object", "properties": {
                "name": {"type": "string", "description": "short filename, e.g. 'text_context', 'entities', 'strategy'"},
                "content": {"type": "string"},
            }, "required": ["name", "content"]}}},
        {"type": "function", "function": {
            "name": "read_my_notes",
            "description": "List your saved notes, or read a specific one by name.",
            "parameters": {"type": "object", "properties": {
                "name": {"type": "string", "description": "optional; if omitted, returns the list of all notes"},
            }}}},
        {"type": "function", "function": {
            "name": "submit_ir_for_lint",
            "description": "Save your A4V3 IR draft to main_ir.a4v3 and run deterministic checks (parser, semantic lint, family coverage, lowering audit). Returns findings — iterate by re-submitting an improved IR.",
            "parameters": {"type": "object", "properties": {
                "ir_text": {"type": "string"},
            }, "required": ["ir_text"]}}},
        {"type": "function", "function": {
            "name": "submit_provenance",
            "description": "Save provenance.yaml. Re-runs provenance_lint + token_provenance + GROUNDING gate. STATUS: never 'human_approved' — use 'agent_drafted'. STRUCTURE: top-level keys typically include `claims:` (list, one per IR declaration with ir_id/source_phrase/back_translation/rationale) AND `vocabulary_notes:` (DICT — required for any IR sort/symbol/entity name not directly traceable to a source word). Every ungrounded name (e.g. `License`, `LicenseRecipientCategory`, `IndexUnderlyingValueLicenseIssuance`) MUST appear under `vocabulary_notes:` with `note:` + `source_phrase:` explaining the link to source — otherwise this tool REFUSES the submission. Example: `vocabulary_notes: { License: { note: 'Generic license carrier grounded by source phrase Licenses', source_phrase: Licenses } }`. Documenting under `sorts:` (list form) does NOT count for grounding.",
            "parameters": {"type": "object", "properties": {
                "yaml_text": {"type": "string"},
            }, "required": ["yaml_text"]}}},
        {"type": "function", "function": {
            "name": "submit_waivers",
            "description": "Submit waiver explanations for tokens not covered by provenance. Each item: {token, suggested_category, comment}. Categories: absorbed_discourse_or_modifier, absorbed_support_verb, modal_absorbed, source_correction_typo, header_or_formatting, structural_referent, quantifier_or_determiner, other_absorbed.",
            "parameters": {"type": "object", "properties": {
                "items": {"type": "array", "items": {"type": "object", "properties": {
                    "token": {"type": "string"},
                    "suggested_category": {"type": "string"},
                    "comment": {"type": "string"},
                }, "required": ["token", "suggested_category", "comment"]}},
            }, "required": ["items"]}}},
        {"type": "function", "function": {
            "name": "run_package_checks",
            "description": "Run the unified package-level check suite (lint + det checks + LLM judges + corpus-aware judge). Use after IR + provenance + waivers are submitted. Returns judges' verdicts.",
            "parameters": {"type": "object", "properties": {
                "with_llm": {"type": "boolean", "default": True},
                "corpus_aware": {"type": "boolean", "description": "defaults to the agent's corpus_aware flag"},
            }}}},
        {"type": "function", "function": {
            "name": "parallel_critique",
            "description": "Run 5 specialist critics in parallel (~10-30s, ~$0.05) against the current submitted IR: modality / quantifier / ontology / source-fidelity / precedent-fit. Each owns one narrow concern + uses a different LLM vendor for diversity. Returns aggregated strong/soft issues with concrete suggested_fix per issue. Cheap targeted feedback BETWEEN submit_ir_for_lint and run_package_checks — use to catch concrete bugs before the heavier 5-judge panel.",
            "parameters": {"type": "object", "properties": {}}}},
        {"type": "function", "function": {
            "name": "meta_evaluate",
            "description": "Step out of the local repair loop. Required when run_package_checks reports meta_required=true (judges' dissent has not changed across multiple verify rounds — local fixes are not working). Shows the FULL verify history + current IR + text-intent classification to an internal LLM and produces a structured 'radical alternative architecture' proposal. After meta_evaluate, the submit_ir_for_lint gate is released for ONE more attempt; if that still fails, finalize as 'failed_after_meta'.",
            "parameters": {"type": "object", "properties": {}}}},
        {"type": "function", "function": {
            "name": "finalize",
            "description": "End the run with a triage decision. Call this when you've finished translating, ran package checks, and are ready to hand off.",
            "parameters": {"type": "object", "properties": {
                "decision": {"type": "string", "enum": ["agent_accept_candidate", "agent_accept_candidate_with_dissent", "needs_human_review", "failed_after_meta"]},
                "summary": {"type": "string", "description": "1-3 sentence summary of what you produced and confidence level"},
                "notes": {"type": "string", "description": "optional: anything else the human reviewer should know"},
            }, "required": ["decision", "summary"]}}},
    ]
