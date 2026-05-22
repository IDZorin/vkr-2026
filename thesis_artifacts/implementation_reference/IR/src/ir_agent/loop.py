"""Agent orchestration loop + system prompt + initial-user-message builder."""
from __future__ import annotations

import json
import pathlib
import time
from typing import Any, TYPE_CHECKING

from ir_agent.config import DEFAULT_CORPUS_LLM_BUNDLE_DIR
from ir_agent.corpus_profile import render_methodology_context
from ir_agent.env import ToolEnv
from ir_agent.helpers import _read_text, _truncate, _utcnow
from ir_agent.phases import _PHASE_BY_TOOL, _PHASE_DISCOVERING, _phase_for_turn
from ir_agent.tools.registry import TOOL_REGISTRY, tool_schemas

if TYPE_CHECKING:
    from atomvex.infrastructure.llm.client import LLMClient


SYSTEM_PROMPT = """You are an autonomous A4V3 IR translator agent. You receive a
single methodology section and have tools to: read other corpus sections,
search the corpus, look up A4V3 schema, save your own notes, draft IR, run
checks, and finalize with a triage decision.

WORKFLOW PHASE STATE MACHINE (enforced by tool gates — not optional):

  DISCOVERING → IR_IN_FLUX → PACKAGE_DRAFTING → VERIFYING → FINALIZED
                    ↑              ↑                ↓
                    └──────────────┴── META_REQUIRED (auto on stagnation)

Every tool result includes `current_phase`. Tools have phase gates:
  - submit_provenance / submit_waivers: ONLY in PACKAGE_DRAFTING or VERIFYING.
    If you call them in IR_IN_FLUX, they will be REJECTED with an error
    pointing back to submit_ir_for_lint.
  - run_package_checks: ONLY in PACKAGE_DRAFTING (after submit_provenance +
    submit_waivers) or VERIFYING (for re-verify after fix).
  - meta_evaluate: ONLY in META_REQUIRED state (auto-set after verify
    stagnation across 3+ rounds with same dissent).
  - submit_ir_for_lint: always allowed UNLESS meta_required is set or phase
    is FINALIZED.

The state machine MEANS: provenance/waivers are documentation of a STABLE
IR, not draft-stage artifacts. Don't bother re-writing provenance every
time you tweak the IR — get the IR clean first (auto-transition will move
you to PACKAGE_DRAFTING when lint_strong=0 + family/lowering OK after
intent override). Then write provenance ONCE.

**REFLECTION RULE — read carefully**
After every tool result, briefly state in 1–2 sentences (as your assistant
text) what the result tells you and what you'll do next. Tool results are
EVIDENCE — react to them, do not just barrel ahead to the next step. If a
result returned errors, findings, or unexpected values, ADDRESS them before
moving forward. Silent tool-call chains miss problems.

WORKFLOW (with explicit loops, not a one-shot pipeline):

  1. DISCOVER — understand what this section is about.
     **FIRST CALL: classify_text_intent**. This determines whether the
     section is legal/regulatory (where modals like 'may'/'shall' MUST be
     preserved as DeonticDecl) or descriptive methodology (where modals are
     usually grammatical and should be modeled as AssertDecl/fact, with
     the modal absorbed into a waiver). Most methodology sections are
     descriptive — do NOT reflexively map every 'may' to permission.

     **SECOND CALL: analyze_role_frame**. Decomposes the source into
     event-carrier + participant-roles (agent / recipient / target /
     instrument / scope) and produces drafter_directives the IR MUST
     follow. Outputs role_frame.json + role_frame.md. Why this matters:
     without an explicit frame, the drafter tends to compress all
     participants into a generic 4-arg catch-all relation (e.g.
     may_issue_license_for(org, index, prod, recipient)) instead of
     reifying the event as a 1st-class sort and attaching roles
     individually. The frame also enforces an ontology budget — each new
     sort/entity must cite a verbatim source phrase, so the IR stays
     proportional to the source.

     **THIRD CALL: compose_strategy**. Consolidates user_hints +
     role_frame + classification into strategy_v0.md — a SINGLE source
     of truth (six fixed sections: hints / entities / relationships /
     per-clause strategy / critic feedback / open questions). The
     drafter reads ONLY this file; if you forget to write something, the
     drafter does not know it. The submit_ir_for_lint gate REFUSES until
     strategy_v0.md exists. Versioned: if a VERIFY round fails because
     of a STRUCTURAL strategy issue (multiple judges complain about the
     same thing), call amend_strategy() to write strategy_v1.md (prior
     version preserved). Each amendment must propose a CONCRETE
     different drafter approach, not "try harder".

     **FOURTH CALL: read_user_hints**. Hints are PLAIN-TEXT directives from a
     human reviewer (per IR/index/user_hints_contract.md). They override
     classifier defaults if applicable. If a hint changes how you would
     translate a phrase, you MUST cite hint_id in provenance/notes
     (auditability). If two hints conflict — DO NOT guess: flag in
     agent_notes for human disambiguation. May be empty (no hints set yet).

     Then continue discovery. Several SEARCH tools are available:
     - **A curated starter pack is already in your initial user message**
       (auto-prefetch via curate_starter_pack at run start). It contains
       semantic / structural / ontology / deontic precedents grouped by
       purpose. **Read it first** — it answers most "what's similar in
       this corpus" questions without further tool calls.
     - semantic_search(query) — embedding-based search over corpus. Use
       for CONCEPTS not exact phrases ("modal possibility", "permission
       with conditions"). More flexible than substring grep.
     - curate_starter_pack(focus_query=...) — re-run retrieval sub-agent
       with a SPECIFIC focus if the auto-prefetch wasn't enough.
     - search_corpus(query, scopes=[...]) — substring grep over the
       corpus (sections+definitions+bridge+policy default; add
       'appendix' to widen).
     - search_successes(query) — POSITIVE precedents from past
       agent_accept_candidate runs (auto-curated catalog).
     - search_failures(query) — opt-in NEGATIVE knowledge from past
       failed_after_meta runs (with DO_NOT_REPEAT markers + WHY they failed).
     - read_section / read_bridge / get_a4v3_family / list_sections /
       list_a4v3_families.

     Save observations to notes (text_context, entities, relations) so you
     can refer back.

  2. PLAN — decide which A4V3 families fit each signal, which precedents
     support each choice, what the IR skeleton looks like. Save as
     'strategy.md' note.

  3. DRAFT loop (CRITICAL — most failures happen here):
     a. Call submit_ir_for_lint(ir_text).
     b. Check the result. The IR is NOT ready unless ALL of:
          - parser.returncode == 0
          - semantic_lint.strong == 0
          - family_coverage.n_required_gaps == 0
          - lowering_audit.n_smells == 0
        If any condition fails, the IR has bugs. Fix them and re-submit.
     c. Loop up to 5 attempts. If still not clean after 5, call finalize
        with decision='failed_after_meta' and explain the blocker.
     d. Only proceed to step 4 when the IR is clean.

  3.5 CRITIQUE (recommended after DRAFT loop, before PROVENANCE) — call
     parallel_critique. It runs 5 specialist critics in parallel
     (~10-30s, ~$0.05): modality / quantifier / ontology / source-fidelity /
     precedent-fit. Each owns ONE narrow concern + uses a different LLM
     vendor (DeepSeek/GPT/Claude/Qwen). Read strong_issues; address them
     by re-submitting IR; re-run parallel_critique until strong=0. THEN
     proceed to PROVENANCE. Cheap and targeted — much faster signal than
     waiting for run_package_checks (which costs ~$0.50 per round).

     Also call check_ir_vs_strategy after each clean DRAFT to confirm the
     IR realises ALL strategy commitments (catches drift like "strategy
     said declare 4 relations but drafter only declared 2"). The
     submit_ir_for_lint result will hint when this is needed.

  3.6 ITERATIVE PRESERVATION (sculptor model — only re-do what's broken):
     Each clean DRAFT and each VERIFY auto-snapshots IR + verdict to
     iter_<N>/. If a later iter is WORSE than an earlier one (regression),
     run_package_checks emits regression_hint pointing to the better
     iter. Use compare_iters(better, current) to see exactly what was
     lost. Then call rollback_to_iter(better, reason=...) to restore the
     baseline + apply MINIMAL targeted fixes — NEVER rewrite working
     sections of the IR. The lego principle: change only the wrong piece.

  4. PROVENANCE — submit_provenance documenting each claim with source
     quotes and back-translations. Status MUST be 'agent_drafted'.

  5. WAIVERS — submit_waivers explaining tokens not covered by provenance.
     Each item: {token, suggested_category, comment}. Statuses are added
     by the system as 'agent_suggested_<category>'.

  6. VERIFY — run_package_checks returns BOTH a summary AND
     `judge_dissent[]` (per-judge `semantic_differences` for any judge that
     did NOT say `corresponds`). The triage uses **WORST-CASE verdict**,
     not majority — even one `partially_corresponds` blocks acceptance.
     The result also includes `meta_required` and `verify_round` fields.

     If `meta_required: true` (system detected stagnation — same dissent
     issues across 2+ rounds, or 3+ rounds without convergence):
       - **You MUST call meta_evaluate() before any further submit_ir_for_lint.**
       - submit_ir_for_lint will REFUSE with an error if you skip this.
       - meta_evaluate shows the full verify history + asks you to think
         about RADICAL ALTERNATIVE architecture (different family choice,
         different quantification, removing entire fact blocks, etc).
       - After meta_evaluate, submit ONE new IR implementing the radical
         change. If that also fails — finalize as 'failed_after_meta'.

     If `meta_required: false` and `judge_dissent` is non-empty:
       a. Read each dissenter's `semantic_differences` carefully.
       b. Identify the COMMON specific issue (often: sort-as-entity in fact
          calls, modal-as-factual, missing forall quantification, missing
          subtyping, prelude redeclaration).
       c. Submit a NEW IR (and provenance/waivers) addressing those issues.
       d. Re-run run_package_checks.

     Don't iterate blindly with cosmetic changes — each new IR must
     concretely address dissenters' citations, not paraphrase the same
     structure. The meta_required gate enforces this.

  7. FINALIZE — call finalize() with one of:
        - 'agent_accept_candidate' if IR clean + judge corresponds + no waivers
        - 'agent_accept_candidate_with_dissent' if det checks clean + majority
          corresponds + at most 1 dissenter + agreement >= 0.7
        - 'needs_human_review' if multiple judges dissent or det issues remain
          but you've explored all your options and need human eyes
        - 'failed_after_meta' ONLY when you genuinely DO NOT KNOW how to fix
          the remaining issues — meta_evaluate ran AND its proposed
          alternative also failed AND you cannot articulate the next concrete
          step to take.

WHAT failed_after_meta IS NOT:
  - It is NOT "I tried 3 times and got tired."
  - It is NOT "I see what's wrong but it would take more iterations."
  - It is NOT "the lint keeps complaining about the same anti-pattern."
  - If you can write in your finalize.summary "the IR needs X" or "the fix
    is to use Y" or "should declare Z entities" — that means you KNOW the
    fix. Apply it via submit_ir_for_lint, do NOT use failed_after_meta as
    an escape hatch. failed_after_meta is reserved for the rare case
    where the source genuinely doesn't fit any A4V3 family or canonical
    precedent provides no guidance.
  - You have a budget of max_steps (typically 80). If you've used <50%
    of it, plenty of room remains. Iterate.

The finalize gate now actively detects actionable language in your
summary/notes (phrases like "needs to", "should be", "the fix is",
"use entities"). If you write such language AND choose
failed_after_meta, the gate REJECTS the call and tells you to apply the
fix you described before finalizing.

HARD RULES:
  - You NEVER write status 'human_approved'. Use 'agent_drafted' or
    'agent_suggested_<category>'. (The system also sanitizes this.)
  - You only modify artifacts inside your agent_run dir (handled by tools).
  - When source has a modal verb ("may", "shall", "will be"), do NOT
    mechanically pick DeonticDecl. Look at context: is this a normative
    statement with conditions/consequences, or a descriptive/information-
    disclosure statement? Cite a precedent before deciding.
  - Use source-strict vocabulary: every IR identifier should map back to a
    word/phrase in the source. Avoid IR-internal inventions.
  - When the budget reminder fires, wrap up and finalize — partial work
    is better than a forced cutoff.

Begin by reading your assigned source. Think briefly before each tool call."""


def _load_preludes_block(prelude_dir: pathlib.Path | None = None) -> str:
    """Load all prelude markdown files from `prelude_dir` (defaults to
    DEFAULT_CORPUS_LLM_BUNDLE_DIR — legacy fallback only). Picks up both
    `minimal_prelude_*.md` (cross-methodology base ontology — Day,
    FinancialInstrument, Organization, Period, Event, ...) AND
    `domain_prelude_*.md` (methodology-family-specific layers). Missing
    minimal prelude is the dominant cause of the agent re-declaring
    prelude sorts as local sorts."""
    base = prelude_dir if prelude_dir is not None else DEFAULT_CORPUS_LLM_BUNDLE_DIR
    blocks: list[str] = []
    seen: set[pathlib.Path] = set()
    if base.exists():
        # Order matters: minimal first (it's the base ontology that
        # domain preludes extend), then domain layers.
        for pattern in ("minimal_prelude_*.md", "domain_prelude_*.md"):
            for p in sorted(base.glob(pattern)):
                if p in seen:
                    continue
                seen.add(p)
                text = p.read_text(encoding="utf-8", errors="replace").strip()
                blocks.append(f"#### {p.name}\n\n{text}")
    if not blocks:
        return f"(no minimal_prelude_*.md / domain_prelude_*.md files found under {base})"
    return "\n\n".join(blocks)


def initial_user_message(section_dir: pathlib.Path, max_steps: int,
                         starter_pack: str | None = None,
                         corpus_profile: dict[str, Any] | None = None
                         ) -> str:
    """Render the initial user message. Methodology-specific context
    (corpus name, sibling sections, canonical patterns, prelude path)
    comes from `corpus_profile`. When None, a generic fallback context
    is used so the agent still runs."""
    source = _read_text(section_dir / "source.md")
    starter_block = ""
    if starter_pack:
        starter_block = (
            f"\n### Auto-curated starter pack (from retrieval pre-pass)"
            f"\n\n{starter_pack}\n"
        )
    prelude_dir = None
    if corpus_profile and corpus_profile.get("prelude_dir"):
        prelude_dir = pathlib.Path(corpus_profile["prelude_dir"])
    preludes_block = _load_preludes_block(prelude_dir)
    methodology_context = render_methodology_context(corpus_profile)

    main_ir_present = (
        (section_dir / 'main_ir.a4v3').exists()
        and (section_dir / 'main_ir.a4v3').stat().st_size > 0
    )
    normalized_present = (section_dir / 'normalized.md').exists()
    return f"""## YOUR TASK

Translate this section into A4V3 IR and produce a complete artifact package.

### Section ID
{section_dir.name}

### source.md
{source}

{methodology_context}

## DOMAIN PRELUDES (corpus-wide types/symbols — REUSE, do NOT redeclare)

These define the shared ontology across all sections of the methodology.
Every sort/symbol you see here is already declared corpus-wide; in your
local IR, just USE them. Inventing a local sort that duplicates a prelude
sort triggers `ungrounded_sort` deterministic findings and reviewer
pushback.

{preludes_block}

### NAMING CONVENTION (for entity instances)

Entity names MUST be SOURCE-TRACEABLE — derived from the source phrase
that motivated declaring this entity. NEVER use `Foo1`, `Bar2`, generic
indexed placeholders. The entity for a phrase like "<some long noun
phrase from source>" should be named with the CamelCase rendering of
that source phrase (e.g. `<SourcePhraseAsCamelCase>`), NOT a numbered
placeholder.

The same rule applies to fact/constraint/permission names: source-
traceable, descriptive. NEVER use generic indexed names like `License1`,
`Issuance2`, etc.
{starter_block}
### Step budget
You have {max_steps} tool calls total. Track your usage; finalize before running out.

### Existing artifacts in this section dir
- main_ir.a4v3: {"present" if main_ir_present else "empty/missing — you are the baseline"}
- normalized.md: {"present" if normalized_present else "absent"}

Begin."""


def _build_assistant_msg_from_completion(result: Any) -> dict[str, Any]:
    """Convert CompletionResult.tool_calls back into the OpenAI message format
    expected as the previous assistant turn.

    DeepSeek thinking-mode quirk: the API requires `reasoning_content` from the
    previous turn to be sent back in the next request."""
    msg: dict[str, Any] = {"role": "assistant",
                           "content": result.text or None}
    if result.tool_calls:
        msg["tool_calls"] = [
            {"id": tc.id, "type": "function",
             "function": {"name": tc.name,
                          "arguments": json.dumps(tc.arguments,
                                                   ensure_ascii=False)}}
            for tc in result.tool_calls
        ]
    try:
        raw_message = (result.raw or {}).get("choices", [{}])[0].get("message", {})
        rc = raw_message.get("reasoning_content")
        if rc:
            msg["reasoning_content"] = rc
    except Exception:
        pass
    return msg


def run_agent_loop(client: "LLMClient", env: ToolEnv, system: str,
                   initial_user: str, max_steps: int,
                   transcript_path: pathlib.Path,
                   extra_body: dict[str, Any] | None = None,
                   resume_state: dict[str, Any] | None = None) -> dict[str, Any]:
    state_path = transcript_path.parent / "agent_state.json"
    tools = tool_schemas()

    if resume_state is not None:
        messages = resume_state["messages"]
        transcript = resume_state["transcript"]
        step = resume_state["step"]
        total_tokens = resume_state["total_tokens"]
        phase_counts = dict(resume_state.get("phase_counts", {}))
        phase_durations_s = dict(resume_state.get("phase_durations_s", {}))
        prior_elapsed = float(resume_state.get("elapsed_s_at_checkpoint", 0.0))
        run_started = time.time() - prior_elapsed
        env.verify_history = resume_state.get("verify_history", []) or []
        env.meta_required = bool(resume_state.get("meta_required", False))
        env.meta_required_reason = str(resume_state.get("meta_required_reason", "") or "")
        env.meta_evaluations_done = int(resume_state.get("meta_evaluations_done", 0))
        env.phase = str(resume_state.get("phase") or _PHASE_DISCOVERING)
        env.last_ir_lint_clean = bool(resume_state.get("last_ir_lint_clean", False))
        env.submissions = dict(resume_state.get("submissions", {}))
        if resume_state.get("finalized"):
            env.finalized = resume_state["finalized"]
        transcript.append({"step": step, "kind": "resumed",
                           "resumed_at": _utcnow(),
                           "from_step": step})
        print(f"[v2] RESUMED at step {step}/{max_steps}, "
              f"messages={len(messages)}, tokens={total_tokens}, "
              f"prior_elapsed={prior_elapsed:.0f}s", flush=True)
    else:
        messages = [
            {"role": "system", "content": system},
            {"role": "user", "content": initial_user},
        ]
        transcript = [{"step": 0, "kind": "init",
                       "messages_count": len(messages),
                       "started_at": _utcnow()}]
        step = 0
        total_tokens = 0
        run_started = time.time()
        phase_counts: dict[str, int] = {}
        phase_durations_s: dict[str, float] = {}

    def flush_transcript() -> None:
        transcript_path.write_text(
            json.dumps({"schema": "agent_v2_transcript",
                         "steps": transcript,
                         "messages": messages,
                         "total_tokens": total_tokens,
                         "phase_counts": phase_counts,
                         "phase_durations_s": {k: round(v, 2)
                                               for k, v in phase_durations_s.items()},
                         "elapsed_s": round(time.time() - run_started, 2),
                         }, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8")

    def flush_state() -> None:
        state = {
            "schema": "agent_v2_state",
            "checkpoint_at": _utcnow(),
            "step": step,
            "messages_count": len(messages),
            "total_tokens": total_tokens,
            "elapsed_s_at_checkpoint": round(time.time() - run_started, 2),
            "phase_counts": phase_counts,
            "phase_durations_s": {k: round(v, 2)
                                  for k, v in phase_durations_s.items()},
            "verify_history": env.verify_history,
            "meta_required": env.meta_required,
            "meta_required_reason": env.meta_required_reason,
            "meta_evaluations_done": env.meta_evaluations_done,
            "phase": env.phase,
            "last_ir_lint_clean": env.last_ir_lint_clean,
            "submissions": env.submissions,
            "finalized": env.finalized,
            "extra_body": extra_body,
        }
        state_path.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n",
                              encoding="utf-8")

    flush_transcript()
    flush_state()

    env.max_steps = max_steps
    while step < max_steps and env.finalized is None:
        step += 1
        env.current_step = step
        step_started = time.time()
        if step in {max_steps // 2, max_steps - 10, max_steps - 3}:
            messages.append({"role": "user",
                             "content": f"[budget reminder] You have used {step} of {max_steps} steps. Wrap up and call finalize() soon."})

        try:
            result = client.complete([], raw_messages=messages, tools=tools,
                                     tool_choice="auto", max_tokens=8192,
                                     extra_body=extra_body,
                                     seed=env.seed)
        except Exception as exc:
            transcript.append({"step": step, "kind": "llm_error",
                               "error": f"{type(exc).__name__}: {exc}"})
            flush_transcript()
            flush_state()
            print(f"[v2 step {step:>3}/{max_steps}] LLM ERROR: "
                  f"{type(exc).__name__}: {str(exc)[:120]}", flush=True)
            break

        turn_tokens = result.usage.get("total_tokens", 0)
        total_tokens += turn_tokens
        assistant_msg = _build_assistant_msg_from_completion(result)
        messages.append(assistant_msg)

        if not result.tool_calls:
            duration = time.time() - step_started
            transcript.append({"step": step, "kind": "text_only",
                               "phase": "OTHER",
                               "duration_s": round(duration, 2),
                               "turn_tokens": turn_tokens,
                               "cumul_tokens": total_tokens,
                               "text_chars": len(result.text or ""),
                               "text_excerpt": (result.text or "")[:400]})
            flush_transcript()
            flush_state()
            print(f"[v2 step {step:>3}/{max_steps}] phase=OTHER text-only "
                  f"({len(result.text or '')} chars) tokens={turn_tokens} "
                  f"cumul={total_tokens} ({duration:.1f}s)", flush=True)
            if env.finalized is not None:
                break
            messages.append({"role": "user",
                             "content": "You did not call a tool. If you are done, call finalize(). Otherwise, take the next concrete step."})
            continue

        tool_names_this_turn = [tc.name for tc in result.tool_calls]
        phase = _phase_for_turn(tool_names_this_turn)
        for tc in result.tool_calls:
            fn = TOOL_REGISTRY.get(tc.name)
            if fn is None:
                tool_result = {"error": f"unknown tool: {tc.name}"}
            else:
                try:
                    tool_result = fn(env, **tc.arguments)
                except TypeError as exc:
                    tool_result = {"error": f"bad arguments: {exc}"}
                except Exception as exc:
                    tool_result = {"error": f"{type(exc).__name__}: {exc}"}
            tool_result_text = json.dumps(tool_result, ensure_ascii=False)
            tool_result_text = _truncate(tool_result_text, 6000)
            messages.append({"role": "tool", "tool_call_id": tc.id,
                             "content": tool_result_text})
            transcript.append({"step": step, "kind": "tool_call",
                               "phase": _PHASE_BY_TOOL.get(tc.name, "OTHER"),
                               "tool": tc.name,
                               "arguments_excerpt": _truncate(json.dumps(tc.arguments, ensure_ascii=False), 400),
                               "result_excerpt": _truncate(tool_result_text, 600)})
        duration = time.time() - step_started
        phase_counts[phase] = phase_counts.get(phase, 0) + 1
        phase_durations_s[phase] = phase_durations_s.get(phase, 0.0) + duration
        flush_transcript()
        flush_state()
        tool_summary = ",".join(tool_names_this_turn) if len(tool_names_this_turn) <= 3 \
            else f"{tool_names_this_turn[0]}+{len(tool_names_this_turn)-1}more"
        print(f"[v2 step {step:>3}/{max_steps}] phase={phase:<11} "
              f"tools=[{tool_summary}] tokens={turn_tokens} cumul={total_tokens} "
              f"({duration:.1f}s, total {time.time()-run_started:.0f}s)",
              flush=True)

    if env.finalized is None:
        transcript.append({"step": step, "kind": "exhausted_budget",
                           "max_steps": max_steps})
        env.finalized = {"decision": "needs_human_review",
                         "summary": f"Step budget exhausted at {step}/{max_steps} without finalize().",
                         "notes": "Agent did not complete the workflow.",
                         "finalized_at": _utcnow()}
        flush_transcript()
        flush_state()

    return {"steps_used": step, "total_tokens": total_tokens,
            "finalized": env.finalized}
