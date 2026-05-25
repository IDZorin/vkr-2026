# Financial Methodology Process Workflow Strategy v1

This document fixes the strategy for creating the financial methodology process/workflow layer.
It is a design and audit artifact, not a replacement for local IR, bridge, or
canonical ontology files.

## Position In The Architecture

The process/workflow layer starts after these layers are already available:

- Source fragments: `source.md` and `normalized.md`.
- Local IR: source-faithful `main_ir.a4v3` files.
- Audit envelope: provenance, translator notes, waivers, role annotations, deterministic checks, and review.
- Bridge layer: `bridge/main_bridge.a4v3`.
- Canonical ontology: `merge/canonical_ontology_v1.a4v3`.
- Resolved methodology theory: local IR plus bridge plus canonical ontology.

The process/workflow layer adds workflow interpretation: steps, triggers,
dependencies, inputs, outputs, states, and transitions.

## Core Principle

Do not copy all local formulas into the process layer.

Local IR states what the source says. The process layer states how methodology
activities are ordered and connected. Domain concepts such as `Security`,
`IndexComponent`, `TradingPrice`, `FreeFloatMarketCapitalization`, `Exchange`,
and `CorporateAction` stay in the canonical ontology. Process concepts such as
`ConstructIndexUniverse`, `SelectIndexComponents`, `CalculateWeights`, and
`ImplementOrdinaryRebalance` live in the process layer.

## Source Of Truth

The source of truth remains:

- local `main_ir.a4v3` files;
- local audit envelope files;
- `bridge/main_bridge.a4v3`;
- `merge/canonical_ontology_v1.a4v3`;
- process files created under `process/`.

The process layer is source-grounded but not source-local. If a process edge or
state is inferred from several sections, the grounding must say so explicitly.

## Grounding Rules

Every process step must have at least one source grounding:

- a section or definition that states the activity directly;
- a source-backed local IR claim that entails the activity;
- a bridge or canonical decision that connects the local symbols used by the step.

Every process edge must say whether it is:

- `explicit`: directly stated by source wording;
- `structural`: required by the source-backed data dependency;
- `inferred`: a merge-level interpretation from multiple grounded claims;
- `operational`: needed only for executable lowering and not asserted by the source.

Inferred and operational edges require notes.

Grounding is not limited to whole document parts. A step or edge may be
grounded in:

- a document part;
- a named local constraint or fact;
- a bridge family or bridge decision;
- a canonical concept, frame, or role;
- a local provenance note when the step uses an accepted inference.

The formal process ontology should therefore support either a generic
`GroundingTarget` carrier or separate grounding relations for these target
types. Whole-section grounding is acceptable for the first inventory pass, but
not precise enough for final workflow review.

## What Belongs In Process Layer

Include:

- workflow steps;
- triggers such as Selection Day, Fixing Day, Rebalance Day, Calculation Day, market disruption, corporate action, correction event, termination condition;
- inputs and outputs of steps;
- lifecycle states such as eligible security, selected component, calculation-day component, implemented component;
- dependencies between steps;
- exception overlays that modify or interrupt the happy path;
- grounding links to sections, definitions, bridge decisions, and canonical concepts.
- process edge behavior for exception overlays;
- temporal ordering and iteration/fixed-point markers where the methodology needs them.

Do not include:

- full restatement of local IR formulas;
- ungrounded business assumptions;
- executable SHACL/RDF/SMT-specific details;
- raw data validation rules unless they express process structure;
- new domain identities that belong in bridge or canonical ontology.

## Happy Path First

Build the ordinary methodology workflow first:

1. Determine relevant calendar dates.
2. Construct or identify the Index Universe.
3. Apply Index Universe Requirements.
4. Apply Index Component Requirements.
5. Select Index Components on Selection Day.
6. Calculate weights from FFMC and constraints.
7. Determine Fixing Day shares based on Selection Day weights.
8. Implement ordinary rebalance after Close of Business on Rebalance Day.
9. Calculate ongoing intraday and closing index levels.

Only after the happy path is stable, add exception overlays.

Use an iterative workflow-first style. The first ontology pass should be only a
seed vocabulary. Draft a small concrete happy-path workflow, then refine the
ontology when the workflow exposes a real need. Avoid designing a large abstract
process ontology before it is exercised by at least one grounded workflow slice.

## Exception Overlays

Model these as separate subflows that can modify, interrupt, or provide fallback
behavior for the happy path:

- Corporate action adjustments: sections 4.4 and 4.5.
- Market disruption handling: section 4.7.
- Correction handling: section 4.6.
- Termination flow: section 4.2.
- Methodology review and changes: sections 5.2 and 5.3.
- Oversight and rule amendment flow: section 5.5.

Exception overlays should not be mixed into the happy path unless the source
explicitly makes them part of the ordinary flow.

Overlay behavior must be explicit. Initial behavior categories:

- `Preempt`: the overlay stops or replaces the happy path, e.g. termination.
- `ModifyAndContinue`: the overlay changes an input, output, or formula and the happy path continues, e.g. many corporate-action adjustments.
- `InterruptAndResume`: the overlay pauses a flow and resumes it after a condition is resolved.
- `Fallback`: the overlay supplies an alternative value or procedure, e.g. price or fixing fallback logic.

These behavior categories should become formal enum values in
`process_ontology_v1.a4v3` when exception overlays are modeled.

## State Modeling

Use explicit states when a concept changes lifecycle position over time.

Important initial states:

- `EligibleUniverseCandidate`: a security or financial instrument passes universe-level constraints.
- `EligibleComponentCandidate`: a security passes component-level constraints.
- `SelectedComponent`: a security has been selected on Selection Day.
- `CalculationDayComponent`: a component is in scope for a Calculation Day calculation.
- `ImplementedComponent`: a component is in the Index after rebalance implementation.

These process states should connect to canonical membership frames rather than
directly rewriting local `index_component` predicates.

Initial state-to-canonical binding policy:

- `SelectedComponent` corresponds to canonical `SelectedMembership`.
- `CalculationDayComponent` corresponds to canonical `CalculationMembership`.
- `ImplementedComponent` corresponds to canonical `ImplementedMembership`.
- `EligibleUniverseCandidate` and `EligibleComponentCandidate` are pre-membership process states; they do not correspond to a canonical membership state unless a later bridge/canonical decision introduces one.

The process ontology should make this binding explicit with a relation such as:

```a4v3
rel process_state_corresponds_to_membership_state : ProcessState, IndexComponentMembershipState
```

Do not rely on similar names to connect process states to canonical membership
states.

## Temporal And Iterative Semantics

Process workflow is temporal. The first ontology pass should include primitives
for:

- ordering between process steps;
- ordering between triggers;
- binding steps to calendar markers such as Selection Day, Fixing Day, Rebalance Day, Close of Business, and Calculation Day;
- business-day offsets such as "20 Business Days before";
- iteration or fixed-point semantics where the method repeats until constraints are satisfied.

The weight calculation flow is the first likely fixed-point candidate, because
section 2.3 contains redistribution logic that may need to repeat until the
region and component constraints are satisfied.

If iteration is not fully formalized in the first pass, mark it explicitly as
`IterationSemanticsDeferred` rather than hiding it in prose.

## Observation Frames As Process Inputs And Outputs

Process inputs and outputs should reference canonical observation frames where
possible, not local relation names.

Examples:

- weight calculation should consume `FreeFloatMarketCapitalizationObservationFrame`;
- weight calculation should produce `ComponentWeightObservationFrame`;
- ongoing calculation should consume price and FX observation frames;
- index calculation should produce `IndexLevelObservationFrame`.

This keeps process workflow aligned with the bridge/canonical value-observation
layer and avoids reintroducing section-local function names as operational
interfaces.

## Deontic Attributes

Some process steps are not merely descriptive. The source may say that a step is
required, permitted, prohibited, or discretionary.

The process layer should not duplicate local deontic formulas, but it may need a
lightweight attribute that points back to the source-grounded deontic claim:

- `ObligatoryStep`;
- `PermittedStep`;
- `ProhibitedStep`;
- `DiscretionaryStep`;
- `DescriptiveStep`.

Use these only when the local IR already contains the corresponding deontic
structure or the source wording is explicitly deontic. Otherwise leave the step
descriptive and add a review note.

## Relation To Bridge And Canonical Ontology

Bridge answers: which local symbols are connected.

Canonical ontology answers: what shared concepts and role shapes exist.

Process layer answers: how methodology activities move from one state to the
next.

If process modeling discovers a missing identity or type link, do not patch it
inside process files. Add or revise bridge/canonical decisions, then reference
the resolved concept from process.

## Initial Process Files

Create files in this order:

1. `process_inventory_v1.md`: human-readable map of workflow fragments and their source grounding.
2. `process_ontology_v1.a4v3`: seed process vocabulary, kept intentionally small.
3. `ordinary_rebalance_workflow_v1.a4v3`: first concrete happy-path workflow slice from Selection Day through implementation and calculation.
4. Revise `process_ontology_v1.a4v3` based on needs discovered by the concrete workflow slice.
5. `exception_overlays_v1.a4v3`: corporate actions, disruption, correction, termination, and methodology-change overlays.
6. `process_validation_notes_v1.md`: checks, unresolved questions, and lowering-readiness notes.

## Minimum Process Ontology Shape

The first ontology pass should include:

```a4v3
sort Workflow
sort ProcessStep
sort ProcessTrigger
sort ProcessInput
sort ProcessOutput
sort ProcessState
sort ProcessGroundingTarget
sort ProcessEdgeKind =
  ExplicitSourceEdge
| StructuralDependencyEdge
| InferredMergeEdge
| OperationalLoweringEdge
sort OverlayBehavior =
  Preempt
| ModifyAndContinue
| InterruptAndResume
| Fallback
sort StepModality =
  ObligatoryStep
| PermittedStep
| ProhibitedStep
| DiscretionaryStep
| DescriptiveStep

rel workflow_step : Workflow, ProcessStep
rel step_precedes : ProcessStep, ProcessStep
rel step_edge_kind : ProcessStep, ProcessStep, ProcessEdgeKind
rel step_overlay_behavior : ProcessStep, OverlayBehavior
rel step_modality : ProcessStep, StepModality
rel step_triggered_by : ProcessStep, ProcessTrigger
rel step_requires : ProcessStep, ProcessInput
rel step_produces : ProcessStep, ProcessOutput
rel step_enters_state : ProcessStep, ProcessState
rel step_exits_state : ProcessStep, ProcessState
rel step_grounded_in_document_part : ProcessStep, DocumentPart
rel step_grounded_in : ProcessStep, ProcessGroundingTarget
rel process_state_corresponds_to_membership_state : ProcessState, IndexComponentMembershipState
```

This is a starting shape, not a commitment to final naming.

## Validation Checklist

A process workflow is ready for review only if:

- every step has source grounding;
- every edge has an edge kind;
- inferred and operational edges have notes;
- no local formulas are silently rewritten;
- states are explicit where lifecycle matters;
- exception overlays are separated from the happy path;
- bridge/canonical gaps discovered during process drafting are routed back to bridge/canonical files;
- generated operational artifacts are not treated as source of truth.
