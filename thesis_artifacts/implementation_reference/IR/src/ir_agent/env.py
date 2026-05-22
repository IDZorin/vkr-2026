"""ToolEnv: per-run state bundle passed to every tool function."""
from __future__ import annotations

import pathlib
import sys
from typing import Any, TYPE_CHECKING

from ir_agent.config import DEFAULT_MODEL, ROOT
from ir_agent.corpus_paths import DEFAULT_CORPUS_PATHS, CorpusPaths

# atomvex.infrastructure.llm.client lives under <repo>/src — sys.path
# adjustment needed since ir_agent is invoked from IR/src as cwd or via
# PYTHONPATH. Add the inner src to path so the LLMClient import resolves.
sys.path.insert(0, str(ROOT / "src"))
if TYPE_CHECKING:
    from atomvex.infrastructure.llm.client import LLMClient  # noqa: F401


class ToolEnv:
    """Bundles paths + state passed to every tool call."""
    def __init__(self, agent_run_dir: pathlib.Path, section_dir: pathlib.Path,
                 corpus_aware: bool, client: "LLMClient | None" = None,
                 model: str = DEFAULT_MODEL,
                 extra_body: dict[str, Any] | None = None,
                 corpus_paths: CorpusPaths | None = None):
        self.agent_run_dir = agent_run_dir
        self.section_dir = section_dir
        self.corpus_aware = corpus_aware
        self.discovery_dir = agent_run_dir / "discovery"
        self.discovery_dir.mkdir(exist_ok=True)
        self.original_entry_id = section_dir.name
        # Resolved per-run corpus filesystem layout (sections/definitions/
        # bridge/prelude roots). Tools that walk the corpus must read paths
        # from here, not from module-level DEFAULT_CORPUS_* constants.
        # `dz` is just one corpus instance — agent must stay corpus-agnostic.
        self.corpus_paths: CorpusPaths = corpus_paths or DEFAULT_CORPUS_PATHS
        self.finalized: dict[str, Any] | None = None
        self.submissions: dict[str, dict[str, Any]] = {}  # ir/provenance/waivers
        # For intra-tool LLM calls (e.g. classify_text_intent):
        self.client = client
        self.model = model
        self.extra_body = extra_body
        self.seed: int | None = None  # set by run_agent
        # Workflow phase state machine. Transitions are auto-driven by tool
        # results, not agent decisions. See ir_agent.phases for valid values.
        self.phase: str = "DISCOVERING"
        self.last_ir_lint_clean: bool = False
        # Meta-mode state: track verify history, force radical refactor when
        # local fixes don't move the needle.
        self.verify_history: list[dict[str, Any]] = []
        self.meta_required: bool = False
        self.meta_required_reason: str = ""
        self.meta_evaluations_done: int = 0
        # Track IR identity to enforce: FINALIZE rejected if current IR has
        # not been verified by the most-recent run_package_checks. Hash =
        # sha1 of IR text. None if no IR submitted yet.
        self.current_ir_hash: str | None = None
        self.last_verified_ir_hash: str | None = None
        # After meta_evaluate completes, this flag is set; submit_ir_for_lint
        # then refuses until the agent calls amend_strategy (or meta itself
        # auto-writes a strategy_v{N+1}, which clears the flag).
        self.meta_pending_strategy_amend: bool = False
        # Detector for "stuck in same family across amendments": when this
        # exceeds 1, hint at re_analyze_role_frame.
        self.amends_within_same_family: int = 0
        # Step budget tracking — set by run_agent_loop on each iteration.
        # Used by submit_ir_for_lint to remind agent that plenty of budget
        # remains, fighting "give up after N tries" psychology.
        self.current_step: int = 0
        self.max_steps: int = 80
        # Auto-rollback tracking. Triggered by strong regression in
        # run_package_checks; capped to prevent oscillation loops.
        self.auto_rollbacks_done: int = 0
        self.max_auto_rollbacks: int = 2
        # Latest check_ir_vs_strategy result — used by submit_provenance
        # gate to refuse advancement when strategy↔IR drift is unresolved
        # (closes the rationalization "this is strategy-level not lint-level,
        # I can skip"). None = no check run yet.
        self.last_check_strong_missing: int | None = None
        self.last_check_ir_hash: str | None = None
        # Latest deterministic parts_inventory coverage for current IR.
        # Finalize/provenance gates refuse acceptance while required cards
        # are missing, even if judges have a majority "corresponds".
        self.last_parts_unsatisfied_count: int | None = None
        self.last_parts_ir_hash: str | None = None
        # KDR-as-contract: after each run_package_checks generates a KDR
        # memo, its `drop` list and `replace.from` items are stashed here.
        # submit_ir_for_lint then refuses if any item still appears
        # (substring match) in the new IR — closes the loop where KDR
        # was advisory and the agent could finalize while drops were
        # still present.
        self.last_kdr_drops: list[str] = []
        self.last_kdr_version: int | None = None
        self.last_kdr_ir_hash: str | None = None
        # Strategic tier: optional separate client+model for the rare,
        # high-stakes calls (meta_evaluate, analyze_attempt_history,
        # analyze_role_frame, re_analyze_role_frame, compose_strategy,
        # classify_text_intent). When None, those tools fall back to the
        # main `self.client`. Set via --strategic-model CLI flag.
        self.strategic_client: "LLMClient | None" = None
        self.strategic_model: str | None = None
        self.strategic_extra_body: dict[str, Any] | None = None

    def strategic_or_main(self, base_max_tokens: int
                          ) -> tuple["LLMClient", dict[str, Any] | None, int]:
        """Pick (client, extra_body, max_tokens) for a strategic call.
        Falls back to main client if strategic-tier not configured.
        For reasoning models, max_tokens (== max_completion_tokens at API
        level) must cover BOTH reasoning_tokens AND visible output —
        otherwise the model spends entire budget on reasoning and returns
        empty string. Inflate by 5x when on strategic tier."""
        if self.strategic_client is None:
            return self.client, self.extra_body, base_max_tokens
        return self.strategic_client, self.strategic_extra_body, base_max_tokens * 5
