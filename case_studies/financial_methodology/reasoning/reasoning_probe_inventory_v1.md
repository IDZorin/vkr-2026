# Financial Methodology Reasoning Probe Inventory v1

This inventory defines the first deterministic reasoning/validation probes for
the seed methodology methodology process layer. It checks the workflow model that sits above
local IR, bridge, canonical ontology, and process files. It does not replace any
source-of-truth artifact.

## Probe Families

### Parse Probes

- Every process `.a4v3` file must parse through `a4v3_parser_v1.py`.
- Parser warnings are hard findings because downstream graph extraction may be
  incomplete when a block is skipped.

### Step Completeness Probes

- Every declared `ProcessStep` must belong to at least one workflow through
  `workflow_step`.
- Every `ProcessStep` must have `step_grounded_in`.
- Every `ProcessStep` must have `step_modality`.
- Every `ProcessStep` must have `step_iteration_status`.
- Every overlay step must have `step_overlay_behavior`.

### Edge Probes

- Every `step_precedes(a, b)` edge must have `step_edge_kind(a, b, ...)`.
- Every `step_precedes(a, b)` edge must have `step_temporal_relation(a, b, ...)`.
- Every `step_precedes(a, b)` edge must have `edge_grounded_in(a, b, ...)`.
- `InferredMergeEdge` is not forbidden, but each use requires explicit review.

### Reachability Probes

- Every workflow must have at least one step.
- Every workflow may have start steps with no incoming edge.
- Non-start steps should have an incoming edge from another step in the same
  workflow.
- Non-terminal steps should have an outgoing edge in the same workflow.
- Known terminal steps are allowed when explicitly modeled as final outputs or
  terminal states.

### Input / Output Probes

- Every `step_requires(step, input)` must have `input_kind(input, ...)`.
- Every `step_produces(step, output)` must have `output_kind(output, ...)`.
- Inputs may be internally produced by an earlier step or externally supplied.
- External/source-backed inputs are accepted for domain observations, policies,
  calendar/source events, and canonical concepts.

### Overlay Behavior Probes

- `Preempt` workflows should enter a terminal/preempt state.
- `Fallback` steps should produce a route, value, or state output.
- `InterruptAndResume` workflows should have a state exit or a resolved,
  approved, or terminal output.
- `ModifyAndContinue` workflows should produce an adjusted/changed output or
  enter an adjusted/changed state.

### Grounding Probes

- Every grounding target must have `grounding_kind`.
- Every grounding target must have a concrete grounding relation.
- Bridge grounding targets must reference bridge families.
- Source-backed trigger relations should have `trigger_relation_grounded_in`.

## Severity Policy

- `hard`: graph is structurally broken, a required grounding is missing, a
  process file has parser warnings, or a required edge annotation is missing.
- `soft`: workflow semantics need a review decision, such as multiple starts,
  unproduced non-external inputs, or inferred merge edges.
- `advisory`: intentional deferrals and useful review prompts that do not block
  process-layer use.

## Generated Reports

The deterministic runner is `IR/src/process_reasoning_audit_v1.py`.

Expected outputs:

- `case_studies/financial_methodology/reasoning/process_reasoning_audit_v1.json`
- `case_studies/financial_methodology/reasoning/process_reasoning_audit_v1.md`

Acceptance for the current financial methodology process layer:

- hard findings: `0`;
- soft findings: either fixed or documented in process validation notes;
- process `.a4v3` files still parse with warnings `0`.
