"""Workflow phase state machine.

Used to gate which tools agent can call when. Transitions are auto-driven
by tool results, not agent decisions. State is persisted in env.phase and
in agent_state.json for resume capability.
"""
from __future__ import annotations


_PHASE_DISCOVERING = "DISCOVERING"      # initial — explore corpus, classify, hints
_PHASE_PLANNING = "PLANNING"            # writing strategy notes
_PHASE_IR_IN_FLUX = "IR_IN_FLUX"        # IR is being drafted/repaired
_PHASE_PACKAGE_DRAFTING = "PACKAGE_DRAFTING"  # IR stable; writing provenance/waivers
_PHASE_VERIFYING = "VERIFYING"          # package complete; awaiting/got verdict
_PHASE_META_REQUIRED = "META_REQUIRED"  # stagnant verify; must call meta_evaluate
_PHASE_FINALIZED = "FINALIZED"          # finalize() called

_VALID_PHASES = {_PHASE_DISCOVERING, _PHASE_PLANNING, _PHASE_IR_IN_FLUX,
                 _PHASE_PACKAGE_DRAFTING, _PHASE_VERIFYING,
                 _PHASE_META_REQUIRED, _PHASE_FINALIZED}


# Maps each tool name to the phase its invocation represents (for
# transcript turn-tagging in run_agent_loop).
_PHASE_BY_TOOL = {
    "list_sections": "DISCOVER",
    "read_section": "DISCOVER",
    "search_corpus": "DISCOVER",
    "search_successes": "DISCOVER",
    "search_failures": "DISCOVER",
    "semantic_search": "DISCOVER",
    "curate_starter_pack": "DISCOVER",
    "read_bridge": "DISCOVER",
    "list_a4v3_families": "DISCOVER",
    "get_a4v3_family": "DISCOVER",
    "classify_text_intent": "DISCOVER",
    "analyze_role_frame": "DISCOVER",
    "re_analyze_role_frame": "DISCOVER",
    "extract_claim_ledger": "DISCOVER",
    "compose_strategy": "PLAN",
    "amend_strategy": "PLAN",
    "check_ir_vs_strategy": "CRITIQUE",
    "compare_iters": "CRITIQUE",
    "rollback_to_iter": "PLAN",
    "analyze_attempt_history": "CRITIQUE",
    "read_user_hints": "DISCOVER",
    "save_note": "PLAN",
    "read_my_notes": "PLAN",
    "submit_ir_for_lint": "DRAFT",
    "parallel_critique": "CRITIQUE",
    "submit_provenance": "PROVENANCE",
    "submit_waivers": "WAIVERS",
    "run_package_checks": "VERIFY",
    "meta_evaluate": "VERIFY",
    "finalize": "FINALIZE",
}


def _phase_for_turn(tool_names: list[str]) -> str:
    """Tag a turn with a single phase based on the tools it called.
    If a turn mixes phases (rare), pick the latest by canonical order."""
    order = ["DISCOVER", "PLAN", "DRAFT", "CRITIQUE", "PROVENANCE", "WAIVERS", "VERIFY", "FINALIZE"]
    phases = {_PHASE_BY_TOOL.get(t, "OTHER") for t in tool_names}
    for ph in reversed(order):
        if ph in phases:
            return ph
    return "OTHER"
