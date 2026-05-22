# Agent v2 — workflow & tools reference v1

This document explains how the autonomous A4V3 IR translator agent works in
practice: its workflow state machine, the 30 tools it has at its disposal,
and what a real successful run on `seed corpus / section_1_5 / Licensing` looked like.

Code location:
- Entry point: [IR/src/ir_agent/cli.py](../src/ir_agent/cli.py)
- Compatibility shim: [IR/src/methodology_section_agent_v2.py](../src/methodology_section_agent_v2.py)
- Loop & system prompt: [IR/src/ir_agent/loop.py](../src/ir_agent/loop.py)
- Phases & tool-to-phase mapping: [IR/src/ir_agent/phases.py](../src/ir_agent/phases.py)
- Tool registry: [IR/src/ir_agent/tools/registry.py](../src/ir_agent/tools/registry.py)

## 1. Overview

Agent v2 is an OpenAI-tools-style autonomous LLM agent. Given a single
methodology section or definition, it iterates through a fixed state
machine and finalises with a triage decision (`agent_accept_candidate`,
`agent_accept_candidate_with_dissent`, `needs_human_review`, or
`failed_after_meta`).

It is **deliberately conservative**: every commit (IR, provenance,
waivers, finalise) is gated by deterministic checks AND, at verify time,
a 5-vendor LLM judge panel. The agent cannot move forward by guessing —
gates refuse and return concrete error messages.

## 2. State machine

```
DISCOVERING → IR_IN_FLUX → PACKAGE_DRAFTING → VERIFYING → FINALIZED
                ↑              ↑                 ↓
                └──────────────┴── META_REQUIRED (auto on stagnation)
```

Phases (from [phases.py](../src/ir_agent/phases.py)):

| Phase           | What happens                                            |
|-----------------|----------------------------------------------------------|
| DISCOVERING     | Read source, classify intent, role-frame, claim ledger, search corpus |
| PLANNING        | Compose / amend `strategy_v{N}.md` (single source of truth for drafter) |
| IR_IN_FLUX      | Iterate IR drafts: `submit_ir_for_lint` until clean      |
| PACKAGE_DRAFTING| Build provenance + waivers (only after IR is clean)     |
| VERIFYING       | 5-vendor judge panel evaluates the package              |
| META_REQUIRED   | Auto-set when judges dissent persists; forces `meta_evaluate` |
| FINALIZED       | `finalize()` called with one of four decisions          |

State is persisted to `agent_state.json` for resume capability.

## 3. Canonical execution sequence

The state machine in §2 says *which* phases the agent passes through.
This section gives the typical *chronological* order of tool calls
within those phases — the canonical sequence the SYSTEM_PROMPT
prescribes and that successful runs (like the 5/5 walkthrough below in
§6) actually follow.

```
─── DISCOVER ─────────────────────────────────────────────────────────
[1] classify_text_intent
        → discovery/text_intent_classification.json
        Decides: legal-or-regulatory / descriptive / definitional / mixed.
        Anchors the modal-handling policy ("preserve every modal as
        DeonticDecl" vs "modals are grammatical, model as fact + waiver").

[2] analyze_role_frame
        → discovery/role_frame.json + role_frame.md
        Decomposes source into:
          - event/process the source describes (issuance, computation,
            classification, rebalance, ...)
          - participants and their roles (agent / recipient / target /
            instrument / scope)
          - ontology budget — each proposed new sort/entity must cite a
            verbatim source phrase, preventing IR bloat
          - drafter_directives the IR MUST follow

[3] extract_claim_ledger
        → discovery/claim_ledger.json
        Per-claim pinning of source truth. For each atomic claim:
          - event_status ∈ {actual, possible_or_authorized, obligated,
                            prohibited, class_only, definitional}
          - carrier_policy ∈ {class_or_program, instance, none}
        Locks the drafter against silent over-promotion of permissive
        "may be issued" into asserted "has been issued".

[4] read_user_hints
        → loaded from <section_dir>/user_hints/active.yaml (if any)
        Plain-text human overrides. Citations are mandatory in
        provenance if a hint changed the translation.

[5] retrieval (any/all of):
        - curate_starter_pack auto-prefetched at run start
        - search_successes / search_failures (catalog look-ups)
        - semantic_search (embedding top-K)
        - search_corpus (substring grep)
        - read_section (study a similar neighbour's full artefacts)
        - read_bridge / get_a4v3_family
        Result is saved as notes (save_note → discovery/<name>.md)
        so the agent can refer back without re-reasoning.

─── PLAN ──────────────────────────────────────────────────────────────
[6] compose_strategy
        → discovery/strategy_v0.md
        Required before submit_ir_for_lint — the gate refuses without it.
        SINGLE source of truth the drafter reads. Six fixed sections:
          1. User hints verbatim
          2. Entities and their methodology role
          3. Relationships
          4. Per-clause translation strategy
          5. Critic feedback (empty on v0)
          6. Open questions
        If you forget to write something here, the drafter does not
        know it.

─── DRAFT loop (repeat up to ~5 cycles) ──────────────────────────────
[7] submit_ir_for_lint
        → main_ir.a4v3 + iter_<N>/ snapshot
        Saves the A4V3 IR and runs four deterministic checks:
          - parser (strict)
          - semantic lint   (lint_strong must be 0 to advance)
          - family coverage (family_gaps must be 0)
          - lowering audit  (blocking smells must be 0)
        If any fails, the result hints at the fix. Loop.

[8] parallel_critique  (recommended after DRAFT is clean)
        → parallel_critique_v<N>.json
        5 specialist critics in parallel (see §5.2), ~$0.05.
        Address strong_issues by re-submitting IR.

[9] check_ir_vs_strategy  (recommended after DRAFT is clean)
        → ir_vs_strategy_check_v<N>.md
        Catches drift between strategy commitments and IR realisation
        ("strategy promised 4 relations, drafter declared 2").

─── PACKAGE DRAFTING ──────────────────────────────────────────────────
[10] submit_provenance
        → provenance.yaml
        Runs provenance_lint + token_provenance + GROUNDING gate.
        REFUSED if any IR symbol/sort/entity name lacks either a
        source phrase or an explicit vocabulary_notes entry.

[11] submit_waivers
        → waivers.json
        Explanations for source tokens not covered by provenance.
        Categories: absorbed_discourse_or_modifier, absorbed_support_verb,
        modal_absorbed, source_correction_typo, header_or_formatting,
        structural_referent, quantifier_or_determiner, other_absorbed.

─── VERIFY (1-5 rounds depending on judge dissent) ────────────────────
[12] run_package_checks
        → run_package_checks_v<N>.json
        Unified suite: lint + det checks + 5-vendor LLM judge panel +
        corpus-aware judge. Returns:
          - verdicts per judge ∈ {corresponds, partially_corresponds,
                                   does_not_correspond}
          - judge_dissent[] with semantic_differences per dissenter
          - meta_required flag (true after stagnation)
        If dissent is non-empty:
          - identify the COMMON specific issue across dissenters
          - submit a NEW IR addressing it (go back to step [7])
          - re-run [12]
        If meta_required becomes true → step [13].

[13] meta_evaluate (only when meta_required=true)
        → discovery/keep_drop_replace_v<N>.md
        Steps out of the local repair loop. Shows full verify history
        to an internal LLM and produces a "radical alternative
        architecture" proposal. After it, submit_ir_for_lint is
        released for ONE more attempt; if that also fails, the run
        finalises as failed_after_meta.

─── FINALIZE ──────────────────────────────────────────────────────────
[14] finalize
        → agent_triage.md + .json (triage layer may override decision —
          see §5.4 triage matrix)
        decision ∈ {agent_accept_candidate,
                    agent_accept_candidate_with_dissent,
                    needs_human_review,
                    failed_after_meta}
```

The sequence is **not** strict-linear: the agent can loop back to
DRAFT from CRITIQUE, VERIFY, or even DISCOVER (`re_analyze_role_frame`
after persistent judge dissent on family choice). But the *first* call
in any clean run is always `classify_text_intent`, and the *last* is
always `finalize`.

What this sequence buys you over a one-shot prompt:

- **Strategy is committed before drafting.** The drafter cannot "drift"
  because there is a written artefact (strategy_v0.md) that captures
  the decisions about entities, relationships, per-clause approach
  *before* the IR is written.
- **Entities are explicitly inventoried** (via role_frame + ontology
  budget) so the IR does not invent IR-internal sorts that have no
  source basis.
- **Claim truth is pinned** (via claim_ledger) so the drafter cannot
  promote a permissive claim into an asserted fact.
- **Judges see provenance**, not just IR text, so their verdict checks
  source-grounding, not only structural validity.

## 4. Tool catalogue (30 tools)

The model sees these tools as OpenAI function-calling definitions. Each
tool has a phase-gate; calling outside the allowed phase returns an
error with a hint about which tool to call instead.

### 4.1 DISCOVER tools (read-only intelligence)

| Tool | Purpose |
|---|---|
| `read_section` | Read another corpus section's source.md / main_ir.a4v3 / provenance / notes |
| `list_sections` | List section/definition ids in this corpus + which have IR |
| `search_corpus` | Grep over corpus (sections + definitions + bridge + policy) |
| `search_successes` | Search auto-curated catalog of past `agent_accept_candidate` runs — positive precedents |
| `search_failures` | Search anti-pattern catalog of past `failed_after_meta` runs — DO_NOT_REPEAT |
| `semantic_search` | Embedding-based top-K retrieval (text-embedding-3-large) over the corpus |
| `curate_starter_pack` | Sub-agent retrieval over multiple angles, grouped by purpose — auto-prefetched at run start |
| `get_a4v3_family` | Extract schema lines for a specific A4V3 family (e.g. `DeonticDecl`) |
| `list_a4v3_families` | Enumerate available A4V3 families |
| `classify_text_intent` | Decide if text is legal/methodology/spec/definitional/mixed; recommends modal-handling policy. **First call** in DISCOVER. |
| `analyze_role_frame` | Decompose source into event-carrier + participant-roles (agent / recipient / target / instrument / scope). Produces `role_frame.json` + drafter_directives. |
| `re_analyze_role_frame` | Re-do role analysis using verify findings (e.g. switch AssertDecl→DeonticDecl after dissent) |
| `extract_claim_ledger` | Pin source-truth per claim: `event_status` ∈ {actual / possible_or_authorized / obligated / prohibited / class_only / definitional}, `carrier_policy` ∈ {class_or_program / instance / none} |
| `read_user_hints` | Read plain-text directives from human reviewer (per `user_hints_contract.md`) |
| `read_bridge` | Read the global bridge file (cross-section identity layer) |

### 4.2 PLAN tools (strategy authoring)

| Tool | Purpose |
|---|---|
| `compose_strategy` | Consolidate hints + role_frame + classification into `strategy_v0.md`. Six fixed sections: hints / entities / relationships / per-clause strategy / critic feedback / open questions. **Required before** `submit_ir_for_lint`. |
| `amend_strategy` | Write `strategy_v{N+1}.md` after a failed verify round (prior preserved for audit). Must propose CONCRETE different approach. |
| `save_note` | Save intermediate observation to `discovery/<name>.md` |
| `read_my_notes` | List or read saved notes |

### 4.3 DRAFT tool

| Tool | Purpose |
|---|---|
| `submit_ir_for_lint` | Save A4V3 IR to `main_ir.a4v3` and run det checks: parser + semantic_lint + family_coverage + lowering_audit. Returns findings; iterate by re-submitting. |

### 4.4 CRITIQUE tools (between DRAFT and PROVENANCE)

| Tool | Purpose |
|---|---|
| `parallel_critique` | Run 5 specialist critics in parallel (modality / quantifier / ontology / source-fidelity / precedent-fit). Each uses a different LLM vendor. ~10-30 s, ~$0.05. |
| `check_ir_vs_strategy` | Compare current IR against the latest strategy. Catches drift like "strategy promised 4 relations, drafter declared 2". Persists `ir_vs_strategy_check_v{N}.md`. |
| `compare_iters` | Diff two iter snapshots: declarations + verdict + recommended action |
| `rollback_to_iter` | Restore IR + provenance + waivers from a prior `iter_<N>/` snapshot. Current IR is preserved as `pre_rollback_<ts>.a4v3`. |
| `analyze_attempt_history` | Cross-iter narrative — what worked, what regressed, recommended next action |

### 4.5 PROVENANCE / WAIVERS / VERIFY tools

| Tool | Purpose |
|---|---|
| `submit_provenance` | Save `provenance.yaml`. Re-runs `provenance_lint` + `token_provenance` + GROUNDING gate. Requires `vocabulary_notes` for any ungrounded sort/symbol/entity name — otherwise refuses. |
| `submit_waivers` | Submit explanations for tokens not covered by provenance. Categories: `absorbed_discourse_or_modifier`, `absorbed_support_verb`, `modal_absorbed`, `source_correction_typo`, `header_or_formatting`, `structural_referent`, `quantifier_or_determiner`, `other_absorbed`. |
| `run_package_checks` | Unified package-level suite: lint + det checks + LLM judges + corpus-aware judge. Returns judges' verdicts + `judge_dissent[]` + `meta_required` flag. |
| `meta_evaluate` | When `meta_required=true`: step out of local repair loop, see full verify history, propose RADICAL ALTERNATIVE architecture. Releases the submit gate for one more attempt. |
| `finalize` | End the run with `decision` ∈ {agent_accept_candidate, agent_accept_candidate_with_dissent, needs_human_review, failed_after_meta} + summary + notes |

## 5. Deterministic checks & LLM judges

The agent's quality bar is enforced by three layers of checks that run
at different points of the workflow:

1. **Deterministic checks** (parser, lints, audits) — invoked by
   `submit_ir_for_lint`, `submit_provenance`, `submit_waivers`, and
   the unified `run_package_checks` suite. Pure Python, no LLM, fast.
2. **`parallel_critique`** — 5 narrow specialist critics, each on a
   different LLM vendor. Optional but recommended between DRAFT and
   PROVENANCE. ~10-30 s, ~$0.05.
3. **5-vendor judge panel** — invoked inside `run_package_checks` at
   VERIFY phase. The authoritative semantic verdict that gates the
   final triage decision.

### 5.1 Deterministic check stack

Invoked automatically by `submit_ir_for_lint` and `submit_provenance`.
None of these use an LLM.

| Check | What it verifies | Source |
|---|---|---|
| **A4V3 parser (strict)** | Syntax: every line is a valid A4V3 declaration. No undeclared symbols. | [a4v3_parser_v1.py](../src/a4v3_parser_v1.py) |
| **Semantic lint** | Structural: arity matches declaration, no orphan references, no shared-name-token without structural carrier, deontic parameter types must be sorts (not entities), etc. Reports `strong` (blocking) vs `soft` (advisory). | [a4v3_semantic_lint_v1.py](../src/a4v3_semantic_lint_v1.py) |
| **Family coverage** | The IR uses A4V3 families the source actually needs (e.g. legal-text intent requires `DeonticDecl`; pure description requires `AssertDecl`). Reports `n_required_gaps`. | [family_coverage_v1.py](../src/family_coverage_v1.py) |
| **Lowering audit** | "Lowering smells" — patterns that would break the downstream lowering pipeline (orphan declarations, redundant subsumption, malformed quantifier scope). Reports `n_smells` with `blocking` vs `soft` severity. | [lowering_audit_v1.py](../src/lowering_audit_v1.py) |
| **Provenance lint** | Run by `submit_provenance`. Every IR symbol/sort/entity must be grounded in either source text or `vocabulary_notes`. Ungrounded names cause REFUSAL. | [provenance_lint_v1.py](../src/provenance_lint_v1.py) |
| **Token provenance** | Run by `submit_provenance`. Every content token in source must be covered by at least one provenance claim, OR explicitly waived. | [token_provenance_v1.py](../src/token_provenance_v1.py) |
| **Modal/temporal preservation** | Run on demand. Checks that modals (`shall`, `may`, `must`), negated modals (`cannot`, `shall not`), temporal markers (`before`, `after`, `until`), and quantifiers (`all`, `any`, `each`) present in source survive into IR. | [modal_temporal_preservation_v1.py](../src/modal_temporal_preservation_v1.py) |

The submit gate (`submit_ir_for_lint`) refuses to advance the phase
machine to `PACKAGE_DRAFTING` until **all four primary det checks**
return clean: `lint_strong=0`, `family_gaps=0`, `lowering_smells=0`,
plus parser warnings = 0.

### 5.2 `parallel_critique` — 5 cross-vendor specialists

Each critic owns one narrow concern and uses a different LLM vendor to
maximise diversity of opinion. They run in parallel via a thread pool.

| Critic | Focus | Model |
|---|---|---|
| `modality` | Modal preservation given the text-intent (deontic-vs-descriptive policy) | deepseek-v4-pro |
| `quantifier` | `forall` / `exists` / conditional scope correctness | gpt-5.4 |
| `ontology` | Sort / entity declarations + subtyping coherence | claude-haiku-4-5 |
| `source_fidelity` | Source-strict vocabulary — no IR-internal inventions | qwen3.6-plus |
| `precedent_fit` | Alignment with seed methodology corpus canonical patterns | gpt-5.4-mini |

Each returns a JSON verdict with `strong_issues[]` (blocking),
`soft_issues[]` (advisory), and `suggested_fix` per issue. Aggregated
output saved to `parallel_critique_v{N}.json`.

Why specialists are not just one judge: cross-vendor diversity means a
bug missed by one model's blind spot (e.g. DeepSeek's tendency to gloss
over modality) is caught by another (Claude's strong ontology focus).

### 5.3 5-vendor judge panel — `run_package_checks` at VERIFY

The authoritative semantic verdict. Default panel
([corpus_aware_multi_judge_v1.py](../src/corpus_aware_multi_judge_v1.py)):

| # | Model | Provider |
|---|---|---|
| 1 | `gpt-5.4-mini` | OpenAI direct |
| 2 | `gpt-5.4` | OpenAI direct |
| 3 | `claude-haiku-4-5` | Anthropic |
| 4 | `deepseek-v4-pro` | DeepSeek native |
| 5 | `qwen3.6-plus` | Alibaba DashScope |

Each judge sees the full package (source.md + main_ir.a4v3 +
provenance.yaml + waivers + sibling-section bridge context) and returns
a verdict ∈ {`corresponds`, `partially_corresponds`,
`does_not_correspond`} with `semantic_differences[]` listing any claims
that did not survive the translation.

The panel runs in parallel via a thread pool. Total wall-clock per
verify round: ~60-300 s (slowest judge dominates).

Cost per verify round: ~$0.30-0.50 depending on the IR size.

The judge call is **corpus-aware**: each judge is given a curated bundle
of analogous translated sections from the same corpus, so it can
calibrate "is this how this corpus translates similar phrases?".

### 5.4 Triage decision matrix

After verify, the agent's `finalize()` call is intercepted by the
triage layer ([triage.py](../src/ir_agent/triage.py)) which can
**override** the agent's proposed decision based on the objective
verdict numbers. Logic:

```
distribution = Counter(judge_verdicts)          # 5 verdicts
n_corresponds = distribution["corresponds"]
agreement = n_corresponds / n_judges
worst = min(verdicts by severity)               # WORST-CASE rule
clean_gate = (lint_strong == 0
              and family_gaps == 0
              and lowering_smells_blocking == 0)
```

| Final decision | Conditions |
|---|---|
| `agent_accept_candidate` | `clean_gate=accepted` AND all 5 verdicts = `corresponds` AND no waivers |
| `agent_accept_candidate_with_dissent` | `clean_gate=accepted` AND `n_corresponds ≥ n_judges - 1` AND `agreement ≥ 0.7` (i.e. at most ONE dissenter, and they said only `partially_corresponds`) |
| `needs_human_review` | `clean_gate` not accepted, OR multiple judges dissent, OR agreement < 0.7 |
| `failed_after_meta` | `meta_evaluate` already ran AND its proposed alternative also failed AND the agent honestly cannot articulate the next step |

In **`--strict-judges`** mode (legacy): ANY non-`corresponds` verdict
blocks acceptance. This is the original conservative rule. The default
mode is "deterministic-primary": the det clean gate is primary, judges
are advisory; one dissenter is signal, not blocker.

The triage layer also detects "actionable language" in
`finalize.summary` ("needs X", "the fix is Y") and refuses
`failed_after_meta` if the agent itself describes the fix — forcing it
back into the DRAFT loop instead of escaping prematurely.

## 6. Walkthrough — `seed corpus / section_1_5 / Licensing` (real successful run)

**Run:** `agent_run_v2_20260515_115325`
**Decision:** `agent_accept_candidate` (unanimous 5/5 `corresponds`,
clean det gate, no waivers, mean judge confidence 0.88)

### 6.1 Headline metrics

| Metric | Value |
|---|---:|
| Total steps | 43 / 80 |
| Total tokens | 1 921 792 (~1.92 M) |
| Total wall-clock | 1756 s ≈ 29.3 min |
| Verify rounds (5-judge panel) | 2 |
| `meta_evaluate` rounds | 0 (converged on round 2 to unanimous) |

### 6.2 Phase distribution

| Phase | Steps | Wall-clock | Share |
|---|---:|---:|---:|
| DISCOVER | 10 | 151 s | 9% |
| PLAN | 7 | 122 s | 7% |
| DRAFT | 14 | 311 s | 18% |
| CRITIQUE | 4 | 424 s | 24% |
| PROVENANCE | 2 | 122 s | 7% |
| WAIVERS | 2 | 79 s | 4% |
| **VERIFY** | **2** | **516 s** | **29%** |
| FINALIZE | 2 | 29 s | 2% |

VERIFY remains the heaviest single phase because each round of
`run_package_checks` invokes 5 LLM judges in parallel — each spending
60-300 s on per-claim verification. Two rounds were enough here because
the agent's IR was structurally clean from the first DRAFT cycle and
the per-judge `semantic_differences` from round 1 were addressed in a
single targeted re-submission.

### 6.3 What the agent produced

The IR for the source sentence

> "Licenses to use the Index as the underlying value for financial
> instruments, investment funds and financial contracts may be issued
> to stock exchanges, banks, financial services providers and
> investment houses by Solactive."

ended up with the canonical singleton-carrier pattern:

- Sorts: `License`, `LicenseClass`, `IndexUnderlyingValueLicenseClass`
  extends `LicenseClass`, `LicenseRecipientCategory` (enum),
  `LicenseUseCategory` (enum), plus prelude `Organization`, `Index`.
- Entities: `Solactive`, `TheIndex`, `SolactiveLicenseIssuanceProgram`
  (singleton-carrier of `LicenseIssuance`), four recipient categories
  (StockExchange, Bank, FinancialServicesProvider, InvestmentHouse),
  three use categories (FinancialInstrument, InvestmentFund,
  FinancialContract).
- Relations: `license_of_index`, `license_for_use`,
  `issuance_to_recipient_category`, `licensor_of`,
  `license_instance_of_class`.
- Role-wiring facts attaching the recipient/use categories to the
  issuance-program singleton rather than to per-occurrence License
  instances.
- One `DeonticDecl_permission` whose target is
  `IndexUnderlyingValueLicenseClass` (narrowed from generic
  `LicenseClass` — this narrowing is what unlocked the unanimous
  verdict on round 2).

### 6.4 Key architectural decisions (from agent_notes)

1. **Added `sort IndexUnderlyingValueLicenseClass extends LicenseClass`**
   to narrow the permission target — this resolved a round-1 dissenter
   complaint about an over-broad permission target.
2. **Singleton-carrier pattern** (`SolactiveLicenseIssuanceProgram :
   LicenseIssuance`) with role-wiring facts — avoids overstating the
   permission with universal quantification.
3. **Enum sorts for recipient and use categories** with
   source-traceable member names.
4. **Reused `TheIndex` from `section_1_1`** and `Organization` from
   prelude — no redeclaration.

### 6.5 Persisted artefacts in the run dir

```
agent_run_v2_20260515_115325/
  main_ir.a4v3                  ← final IR
  provenance.yaml               ← claim ↔ source span links
  agent_state.json              ← state for resume
  agent_transcript.json         ← every LLM exchange
  agent_triage.md, .json        ← final decision + reasoning
  iter_1/ ... iter_N/           ← snapshot after each clean DRAFT / VERIFY
  parallel_critique_*.json      ← 5 critic outputs
  run_package_checks_*.json     ← judge panel verdicts per round
  discovery/
    text_intent_classification.json
    role_frame.json
    claim_ledger.json
    curated_starter_pack.json
    strategy_v0.md, v1.md, v2.md  ← evolution
    keep_drop_replace_v{N}.md   ← KDR memos
```

## 7. Failure modes & their handlers

| Symptom | Handler |
|---|---|
| IR fails parser / semantic_lint | DRAFT loop — iterate up to 5 times on `submit_ir_for_lint` |
| Strategy ↔ IR drift | `check_ir_vs_strategy` highlights gaps; fix IR or `amend_strategy` |
| Specific concern not yet caught (modality, quantifier, ontology, source-fidelity, precedent-fit) | `parallel_critique` — 5 specialist critics, different LLMs, ~$0.05 |
| Judges disagree (≥1 partial/no) | New DRAFT addressing dissenter's `semantic_differences` |
| Judges keep disagreeing on same point across 2-3 rounds | `meta_required` auto-trips → `meta_evaluate` → ONE more attempt with radical alternative |
| Cannot articulate the next concrete step | `finalize(decision="failed_after_meta", ...)` |
| Best iter was earlier than current | `compare_iters` → `rollback_to_iter` → minimal targeted fix |

## 8. Key design principles (from SYSTEM_PROMPT)

1. **Reflection rule.** After each tool result, the model must state in
   1-2 sentences what the result tells it and what it'll do next.
   Silent tool-call chains miss problems.
2. **Strategy as single source of truth.** The drafter reads ONLY
   `strategy_v{latest}.md`. If something is missing from the strategy,
   the drafter does not know it.
3. **State machine gates are deterministic.** Tools refuse outside
   their phase. The model cannot bypass by pretending to be in a
   different phase.
4. **WORST-CASE verdict.** Triage uses worst-case judge verdict, not
   majority. Even one `partially_corresponds` blocks acceptance unless
   det clean-gate + agreement ≥ 0.7 + at most one dissenter.
5. **`failed_after_meta` is rare.** The finalize gate detects
   actionable language in the agent's summary ("needs X", "should
   be Y") and refuses `failed_after_meta` if the model knows the fix.
6. **Source-strict vocabulary.** Every IR identifier must map back to
   a word/phrase in source — provenance lint refuses ungrounded names.
7. **Sculptor model on iter snapshots.** Each clean DRAFT and VERIFY
   auto-snapshots IR + verdict. Regression detection + `rollback_to_iter`
   + minimal targeted fix — never rewrite working sections.

## 9. CLI usage

```
python -m ir_agent <section_dir>
    [--model deepseek-v4-pro]
    [--max-steps 60]
    [--corpus-aware]
    [--corpus-profile <path>]
    [--no-thinking]              # DeepSeek-V4: disable thinking mode
    [--resume <agent_run_dir>]   # continue from prior run
    [--reuse-from <other_run>]   # reuse cached discovery artefacts
    [--strategic-model gpt-5.5-2026-04-23]  # bigger model only for the
                                            # rare strategic tools
    [--strategic-reasoning low|medium|high|xhigh]
    [--strict-judges]            # legacy: any non-corresponds blocks
    [--seed N]
```

Backwards-compat shim:

```
python IR/src/methodology_section_agent_v2.py <section_dir> [flags]
```
