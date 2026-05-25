# Financial Methodology Process Inventory v1

This inventory is the first concrete implementation artifact for the seed methodology
process/workflow layer. It maps source-grounded methodology activities before
we encode them in `process_ontology_v1.a4v3` and workflow files.

This is not a source of truth by itself. It is a review map over:

- local source and `main_ir.a4v3` files;
- local audit envelopes;
- `bridge/main_bridge.a4v3`;
- `merge/canonical_ontology_v1.a4v3`;
- `process/process_strategy_v1.md`.

## Inventory Status

Status: first pass, happy-path oriented.

Primary goal: identify workflow steps, triggers, inputs, outputs, states,
exception overlays, and grounding targets.

Not yet attempted:

- full process A4V3 formalization;
- operational lowering;
- final exception overlay semantics;
- full fixed-point formalization for weighting;
- state-per-entity carrier modeling.

## Grounding Legend

Grounding levels used below:

- `source`: source text directly states the step.
- `local_ir`: local `main_ir.a4v3` formalizes the step or relation.
- `bridge`: bridge/canonical decision connects local symbols across entries.
- `canonical`: canonical ontology provides shared concept/frame/state.
- `inferred`: process-level interpretation from multiple grounded claims.

Edge kinds:

- `explicit`: stated directly by source wording.
- `structural`: follows from source-backed data dependency.
- `inferred`: merge-level workflow reconstruction.
- `operational`: needed for executable lowering, not asserted by source.

## Happy Path Inventory

### H0 Calendar And Date Setup

Purpose: establish the calendar markers used by later workflow steps.

Grounding:

- `definitions/N04`: Business Day.
- `definitions/N05`: Calculation Day.
- `definitions/N06`: Close of Business.
- `definitions/N09`: Eligible Rebalance Day.
- `definitions/N11`: Fixing Day is Selection Day.
- `definitions/N26`: Rebalance Day schedule and fallback.
- `definitions/N27`: Selection Day is 20 Business Days before Rebalance Day.
- `definitions/N30`: Trading Day with component/exchange context.

Process triggers:

- Business Day.
- Calculation Day.
- Trading Day.
- Selection Day.
- Fixing Day.
- Rebalance Day.
- Close of Business.

Outputs:

- calendar trigger set for ordinary workflow;
- date offsets needed for ordinary rebalance;
- eligible-day condition for Rebalance Day determination.

Notes:

- `EligibleRebalanceDay` is eligibility input, not the actual `RebalanceDay`
  state by itself.
- `FixingDay` currently aliases Selection Day by definition.
- N30 reifies Trading Day through component/exchange context; process lowering
  must not treat `TradingDayContext` as a bare `Day`.

### H1 Construct Or Identify Index Universe

Purpose: determine the universe of instruments from which components can be
selected.

Grounding:

- `sections/section_2_1`: Index Universe Requirements.
- `definitions/N14`: GBS Index Universe.
- `definitions/N22`: Index Universe Requirements term.
- `definitions/N23`: Index Universe.
- `appendix/appendix_8_1`: RBICS level-6 subindustry classifications.
- Bridge RBICS appendix mapping.

Trigger:

- Selection Day.

Inputs:

- GBS Index Universe reference.
- country or region classification.
- ADVT observations over one-month and six-month windows.
- share-class eligibility/buffer logic.
- RBICS subindustry membership.

Outputs:

- `EligibleUniverseCandidate` state for securities/share classes that pass
  universe-level requirements.
- Index Universe membership candidates.

Edge kind to next step:

- H1 -> H2: `structural`, because component requirements operate on the Index
  Universe.

Open modeling point:

- Section 2.1 has share-class-specific logic. The process layer should keep
  share class as a security subtype and avoid collapsing company/share-class
  selection into a single entity.

### H2 Apply Index Component Requirements

Purpose: select candidate components from the Index Universe.

Grounding:

- `sections/section_2_2`: Selection of the Index Components.
- `definitions/N20`: Index Component Requirements.
- Canonical membership state projection.

Trigger:

- Selection Day.

Inputs:

- Index Universe from H1.
- region assignment.
- FFMC observations.
- top-20-per-region ranking logic.

Outputs:

- `EligibleComponentCandidate` process state.
- `SelectedComponent` process state.
- canonical `SelectedMembership` correspondence for selected component roles.

Edge kind to next step:

- H2 -> H3: `structural`, because weighting is assigned to selected Index
  Components on Selection Day.

Notes:

- Section 2.2 says selection is fully rule-based; the corresponding step should
  be `DescriptiveStep` plus a no-discretion grounding, not a discretionary
  process step.
- The relation between selected securities and component-role assignments must
  use the canonical membership frame roles, not a direct `Security = IndexComponent`
  identity.

### H3 Calculate Weights

Purpose: assign and redistribute weights for selected components.

Grounding:

- `sections/section_2_3`: Weighting of the Index Components.
- Canonical observation frames:
  - `FreeFloatMarketCapitalizationObservationFrame`;
  - `ComponentWeightObservationFrame`;
  - `RegionClassificationObservationFrame`.

Trigger:

- Selection Day.

Inputs:

- selected components from H2;
- FFMC observations;
- region assignment;
- regional 50% total weight constraint;
- 5% per-component cap.

Outputs:

- component weights on Selection Day;
- `IterationSemanticsDeferred` marker until fixed-point logic is formalized.

Edge kind to next step:

- H3 -> H4: `explicit/structural`; section 3.1 says Fixing Day shares are based
  on weights calculated on Selection Day.

Notes:

- Section 2.3 explicitly contains iterative redistribution until both
  constraints are satisfied. This is the first fixed-point candidate for the
  process ontology.

### H4 Determine Fixing Day Shares

Purpose: determine implementation shares from Selection Day weights.

Grounding:

- `sections/section_3_1`: shares are determined on Fixing Day based on weights
  calculated on Selection Day.
- `definitions/N11`: Fixing Day is Selection Day.
- Bridge calendar/process links.

Trigger:

- Fixing Day.

Inputs:

- Selection Day weights from H3.

Outputs:

- implementing shares for ordinary rebalance.

Edge kind to next step:

- H4 -> H5: `explicit`; section 3.1 states these shares are implemented in the
  rebalance adjustment.

Open modeling point:

- The process ontology must decide whether shares are a value observation frame
  or a process output carrier. This should be resolved in the first concrete
  workflow slice.

### H5 Implement Ordinary Rebalance

Purpose: adjust the Index to reflect the new selection of components.

Grounding:

- `sections/section_3_1`: ordinary rebalance procedure.
- `definitions/N26`: Rebalance Day.
- `definitions/N27`: Selection Day relation.
- `definitions/N06`: Close of Business.
- Equity Index Methodology document bridge.

Trigger:

- Rebalance Day after Close of Business.

Inputs:

- selected components from H2;
- weights from H3;
- implementing shares from H4.

Outputs:

- `ImplementedComponent` process state;
- canonical `ImplementedMembership` correspondence;
- updated component set for subsequent calculation.

Edge kind to next step:

- H5 -> H6: `structural`; ongoing calculation uses current Index Components.

Notes:

- Section 3.1 also includes an announcement obligation for changes to Index
  Components. This may be a separate publication step attached to H5.

### H6 Publish Rebalance Changes

Purpose: publish changes made to Index Components.

Grounding:

- `sections/section_3_1`: Solactive will publish changes with sufficient notice
  before Rebalance Day under Announcement.
- Announcement section bridge.

Trigger:

- before Rebalance Day, with `SufficientNoticeBeforeRebalanceDay` as a vague
  temporal constraint.

Inputs:

- planned component changes.

Outputs:

- publication/announcement event.

Step modality:

- `ObligatoryStep`, grounded in local deontic treatment of the section 3.1
  publication claim.

Edge kind:

- H6 must precede H5: `explicit`, with vague temporal grounding.

### H7 Ongoing Index Calculation

Purpose: calculate intraday and closing index levels.

Grounding:

- `sections/section_1_4`: intraday and closing level calculation.
- `sections/section_4_1`: index calculation formula/version context.
- `sections/section_4_3`: publication rounding.
- `definitions/N05`: Calculation Day.
- `definitions/N07`, `N08`, `N10`, `N21`, `N31`, `N32`: price, DVT,
  exchange, currency, trading price, and WM/Refinitiv rate concepts.
- Canonical observation frames for price, FX/fixing, currency, exchange, and
  index level.

Trigger:

- each Calculation Day;
- intraday calculation window;
- closing calculation context.

Inputs:

- calculation-day component membership;
- trading prices and fallback prices;
- closing prices;
- listed currency and index currency;
- ICE spot FX rate;
- WM/Refinitiv fixing and fallback.

Outputs:

- intraday index levels;
- closing index level;
- rounded published index level.

Edge kind:

- H5 -> H7: `structural`;
- H7 repeats on Calculation Days: iteration over calendar triggers.

Failure/fallback notes:

- no current Trading Price triggers a price fallback;
- no WM fixing triggers last-available fixing fallback;
- these are fallback overlays inside calculation, not ordinary rebalance steps.

## Exception Overlay Inventory

### E1 Corporate Action Adjustment Need

Grounding:

- `sections/section_4_4`: adjustment may be necessary between regular Rebalance Days when a corporate action occurs.
- `sections/section_4_5`: corporate actions considered in maintenance and accounted for in calculation.

Trigger:

- corporate action related to an Index Component.

Behavior:

- `ModifyAndContinue`.

Inputs:

- affected component;
- corporate action kind;
- effective day / notice;
- Equity Index Methodology adjustment rules.

Outputs:

- required index adjustment;
- possible change to components, number of components, and/or weights.

Notes:

- section 4.4 announcement with at least two Trading Days notice is an
  obligatory publication substep.

### E2 Corporate Action Implementation

Grounding:

- `sections/section_4_5`: corporate actions implemented from cum-day to ex-day
  so adjustment coincides with price effect.

Trigger:

- cum-day/ex-day corporate-action window.

Behavior:

- `ModifyAndContinue`.

Inputs:

- corporate action event;
- price effect;
- relevant adjustment to index variables.

Outputs:

- adjusted index variables.

Open modeling point:

- The process ontology should distinguish event occurrence from value adjustment
  and from method deviation permission.

### E3 Market Disruption

Grounding:

- `sections/section_4_7`: disruption arrangements, market stress, illiquid or
  fragmented markets.

Trigger:

- market stress, illiquid market, fragmented market, inaccurate or delayed
  prices.

Behavior:

- usually `Fallback` or `ModifyAndContinue`; exact behavior depends on the
  disruption arrangement being applied.

Inputs:

- affected prices/components;
- Solactive Disruption Policy.

Outputs:

- modified calculation route or impaired/limited determination state.

Notes:

- This overlay should not stop the happy path by default; it changes the
  calculation conditions.

### E4 Correction Handling

Grounding:

- `sections/section_4_6`: errors may occur and Solactive endeavors to correct
  identified errors within a reasonable period.

Trigger:

- identified error in determination process.

Behavior:

- `InterruptAndResume` or `ModifyAndContinue`, depending on correction impact.

Inputs:

- identified error;
- Solactive Correction Policy;
- reasonable period and measures.

Outputs:

- correction endeavor or corrected value/process state.

Notes:

- Exact correction mechanics are policy-referenced and may remain abstract in
  the first process pass.

### E5 Termination

Grounding:

- `sections/section_4_2`: adjusted return index level at zero or below triggers
  termination and announcement.

Trigger:

- adjusted return index level calculated as zero or below zero.

Behavior:

- `Preempt`.

Inputs:

- adjusted return index calculation;
- termination announcement target.

Outputs:

- terminated index state;
- termination announcement.

Notes:

- This overlay can stop the calculation/rebalance happy path for the affected
  index variant.

### E6 Methodology Review And Change

Grounding:

- `sections/section_5_2`: methodology review at least annually and changes when
  need is identified.
- `sections/section_5_3`: Index Administrator application and modification
  powers.

Trigger:

- regular methodology review;
- identified need for methodology change;
- supervisory, legal, financial, tax, market, or error-correction reasons.

Behavior:

- `ModifyAndContinue`.

Inputs:

- review result;
- methodology policy;
- identified change need.

Outputs:

- methodology change;
- announcement;
- updated guideline amendment date.

Notes:

- Deontic modality matters here: some steps are obligatory, some permitted, and
  some descriptive.

### E7 Oversight And Rule Amendment

Grounding:

- `sections/section_5_5`: Oversight Committee responsibility and prior approval
  for amendments.
- `definitions/N25`: Oversight Committee term.

Trigger:

- proposed amendment to Index rules or Guideline.

Behavior:

- `InterruptAndResume` for approval-gated changes.

Inputs:

- proposed amendment;
- Oversight Committee;
- Methodology Policy.

Outputs:

- prior approval state;
- approved rule or guideline amendment.

Notes:

- This is governance process rather than daily calculation process, but it can
  affect methodology state used by other workflows.

## Cross-Workflow Composition Candidates

These are not formalized yet, but must be handled when the workflow graph is
encoded:

- H5 implemented component state feeds H7 ongoing calculation.
- E1/E2 corporate-action overlays can modify H7 calculation inputs between
  Rebalance Days.
- E3 disruption overlay can modify H7 price/calculation paths.
- E4 correction overlay can revise outputs of H7 or previous determinations.
- E5 termination preempts future H7/H5 execution for the affected index variant.
- E6/E7 governance flows can change rules used by H1-H7.

## First-Slice Discovery Hooks

These are expected to emerge during `ordinary_rebalance_workflow_v1.a4v3`.

### State Per Entity

Process states must be attached to a carrier instance.

Example shape to test:

```a4v3
rel process_state_carrier : ProcessState, Entity
```

The exact carrier type may need to be canonical `Security`,
`IndexComponentRoleAssignment`, or a reified workflow object. Do not model
`SelectedComponent` as a global singleton state.

### Workflow Composition

Ordinary rebalance, ongoing calculation, corporate actions, and disruptions are
separate workflows that need composition edges. The first pass may use
cross-workflow `step_precedes`, but a later ontology refinement may need
`workflow_invokes`, `workflow_interrupts`, or `workflow_modifies`.

### Step Failure Modes

Fallback cases are known in section 1.4 and governance/correction sections, but
the general failure mechanism is not modeled yet.

First pass policy:

- model known source-grounded fallback steps explicitly;
- do not introduce a generic failure state until a concrete workflow slice needs it.

## Candidate First Implementation Slice

The first formal workflow file should cover:

1. Selection Day trigger.
2. Index Universe construction.
3. Component selection.
4. Weight calculation with `IterationSemanticsDeferred`.
5. Fixing Day shares.
6. Rebalance Day after Close of Business implementation.
7. Output `ImplementedComponent` state.

This slice is small enough to test state carriers, temporal edges, and canonical
membership-state mapping without pulling in every exception overlay.

