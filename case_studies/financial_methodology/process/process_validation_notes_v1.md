# Financial Methodology Process Validation Notes v1

This note records the current validation status of the financial methodology process/workflow
layer. It is an audit envelope for process files, not a replacement for local
IR, bridge, canonical ontology, or provenance.

## Files In Scope

- `process_ontology_v1.a4v3`
- `ordinary_rebalance_workflow_v1.a4v3`
- `exception_overlays_v1.a4v3`

## Parser Status

All process files parse with zero warnings:

- `process_ontology_v1.a4v3`: parser warnings `0`
- `ordinary_rebalance_workflow_v1.a4v3`: parser warnings `0`
- `exception_overlays_v1.a4v3`: parser warnings `0`

## Reasoning Probe Status

The deterministic reasoning report is generated at:

- `../reasoning/process_reasoning_audit_v1.json`
- `../reasoning/process_reasoning_audit_v1.md`

Current status:

- hard findings: `0`
- soft findings: `0`
- advisory findings: `29`

The advisory findings are accepted review prompts: mainly external/source-backed
process inputs, intentional modify-detection steps without direct adjusted
artifacts, and trigger timing relations whose grounding remains at the broader
calendar/source-fragment level.

## Structural Sanity Checks

For `exception_overlays_v1.a4v3`:

- every `ProcessStep` has `step_grounded_in`;
- every `ProcessStep` has `step_modality`;
- every `ProcessStep` has `step_iteration_status`;
- every `ProcessStep` has `step_overlay_behavior`;
- every `step_precedes` edge has `step_edge_kind`;
- every `step_precedes` edge has `step_temporal_relation`;
- every `step_precedes` edge has `edge_grounded_in`.

## Review Follow-Ups Closed

- `trigger_relation_grounded_in` is promoted to `process_ontology_v1.a4v3`
  and used for source-grounded trigger relations.
- The corporate-action cum-day to ex-day period is modeled as
  `CorporateActionImplementationWindow`, with explicit start and end markers.
- `EvaluateCorporateActionProcedureDeviation` rejoins the corporate-action
  adjustment flow before the announcement step, so it is no longer a dead-end
  branch in workflow visualizations.
- Announcement-related overlay steps also reference bridge-level announcement
  families through `AnnouncementBridgeGrounding`.
- Overlay calendar markers have explicit grounding targets where the timing
  relation is source-backed.

## Covered Workflows

The happy path is represented by `OrdinaryRebalanceWorkflow`.

The exception/process overlays are represented by:

- `CorporateActionOverlayWorkflow`
- `MarketDisruptionOverlayWorkflow`
- `CorrectionOverlayWorkflow`
- `TerminationOverlayWorkflow`
- `MethodologyChangeOverlayWorkflow`
- `OversightRuleAmendmentOverlayWorkflow`

## Intended Deferrals

These are not treated as process defects:

- `SufficientNoticeBeforeRebalanceDayTrigger` remains vague because section 3.1
  does not specify a numeric notice period.
- Market disruption, correction measures, and methodology policy mechanics stay
  abstract where the source delegates detail to external Solactive policies.
- `step_exits_state` is used only where the overlay has a clear lifecycle
  transition, such as corporate-action adjustment, correction resolution,
  termination, methodology change, and approval gating.
- `ActiveIndexState` is treated as an implicit initial state for a published
  index before the termination overlay exits it.
- The correction overlay is modeled as `InterruptAndResume`: an identified
  error interrupts the ordinary determination path until correction measures
  are chosen and the error is corrected.
- The oversight rule-amendment overlay is also modeled as
  `InterruptAndResume`: proposed amendments are approval-gated before they may
  be made.
- Operational SHACL/RDF/SMT lowering is not part of this layer. It should be
  generated from the resolved methodology theory plus these process files.

## Manual Semantic Review

The overlay behavior choices have been reviewed against the local source
fragments:

- Corporate actions: `ModifyAndContinue` is appropriate because sections 4.4
  and 4.5 describe adjustments that alter components, weights, variables, or
  calculation inputs between regular rebalance days without stopping the
  methodology.
- Market disruption: `Fallback` is appropriate for applying disruption policy
  arrangements; `ModifyAndContinue` is appropriate for the resulting
  determination under disrupted market conditions.
- Correction: `InterruptAndResume` is appropriate because identified errors
  pause or reopen the determination path until correction is handled within a
  reasonable period.
- Termination: `Preempt` is appropriate because section 4.2 terminates the
  affected index when the adjusted return index level is zero or below zero.
- Methodology change: `ModifyAndContinue` is appropriate because sections 5.2
  and 5.3 change the methodology while preserving a consistent calculation
  method.
- Oversight amendment approval: `InterruptAndResume` is appropriate because
  section 5.5 creates a prior-approval gate before amendments are made.

No `InferredMergeEdge` remains in the current process files. All current edges
are either source-explicit or structural dependencies introduced to connect a
source-grounded branch back to the workflow.

## Current Readiness

The process layer is ready for review as a source-grounded workflow model:

- ordinary rebalance happy path is explicit;
- major overlays are separated from the happy path;
- overlay behavior is explicit (`ModifyAndContinue`, `Fallback`,
  `InterruptAndResume`, `Preempt`);
- source grounding is present for each step and edge.

The next stage is either human/LLM review of process semantics or operational
lowering design.
