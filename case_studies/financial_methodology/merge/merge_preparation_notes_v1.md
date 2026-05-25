# seed methodology Merge Preparation Notes v1

This directory contains the first canonicalization layer for the seed methodology corpus.

For the full layer model, see `methodology_architecture_v1.md`.

## What This Is

`canonical_ontology_v1.a4v3` is a merge target ontology. It does not replace
local `main_ir.a4v3` files. Local files remain the source-faithful gold layer;
the canonical ontology gives the merge step a shared vocabulary for cross-entry
reasoning.

`canonical_bridge_decisions_v1.yaml` records the current human-readable merge
decisions: exact aliases, variant links, related-only links, local placeholders,
and review items.

## Merge Boundary

Bridge answers: which local symbols are connected.

Canonical ontology answers: what the shared world looks like after those
connections are applied.

Merge answers: how to rewrite or import local facts into one combined theory.

Post-merge reasoning answers: whether the combined theory has contradictions,
vacuous rules, missing type links, or variant-specific conflicts.

## Important Design Decision

Generic local `TheIndex` placeholders map to the canonical index family, not
blindly to a single published variant. Family-level methodology rules are then
propagated to the five published variants unless a section contains
variant-specific facts. This prevents the initial-level rule for the 50 AR
variant from being overwritten by the default 1000 rule.

## Type-Gap Risk

The merge must not claim "no contradiction" merely because a required type edge
is missing. If a rule is scoped to `Girl` and a local fact is about `Alena`, the
merged theory can only derive a contradiction if it knows that `Alena` is a
`Girl`. Missing type or membership edges should therefore become explicit
merge-readiness findings.

## Current Status

The existing bridge candidate audit reports:

- no unbridged repeated exact declarations;
- no undeclared external identifiers in assertion bodies;
- remaining lexical and source-phrase candidates that require semantic review.

The next step is to run `merge_readiness_audit_v1.py`, then review the soft
findings before performing a mechanical merged-IR construction.

## Resolved Methodology View

`resolved_methodology_view_v1.json` and `resolved_methodology_view_v1.md` are
derived inspection artifacts. They show how local declarations resolve through
bridge families, same-symbol pair groups, standalone bridge symbols, or remain
local-only.

This view is intentionally not a renamed copy of every local formula. The source
of truth remains:

- local `main_ir.a4v3` files;
- local audit envelope files;
- `bridge/main_bridge.a4v3`;
- `canonical_ontology_v1.a4v3`;
- future `process/*.a4v3` workflow rules.

The resolved view is the safe merge-facing surface for answering: "if this local
rule mentions `Index`, `TradingDay`, `Security`, or `IndexComponent`, which
cross-fragment concept does that symbol currently reach?"

## Frame Projection Layer

The first backend-friendly merge extension is an observation-frame layer. Local
A4V3 functions can stay compact, but canonical merge and RDF/OWL lowering need
explicit frames and roles rather than large arity-specific predicates.

Example:

- local: `closing_price(component, day) -> price`;
- canonical frame: `ClosingPriceObservationFrame`;
- bridge roles: argument 1 is `ObservationSubjectRole`, argument 2 is
  `ObservationDayContextRole`, return value is `ObservedClosingPriceRole`.

Projection to the same frame is intentionally weaker than exact aliasing. It
means "these local declarations can be interpreted through the same
role-explicit frame"; it does not erase context differences such as Trading Day
versus Calculation Day.

Section 2.2 uses the source phrase "Free Float Market Capizatlization" and
projects to the FFMC frame. Section 2.3 uses "Float Market Capizatlization" for
the weighting basis of already-selected Index Components. In this document that
is treated as the same FFMC measure: N13 defines Free Float Market
Capitalization, section 2.2 ranks eligible securities by it, and section 2.3
uses the capitalization measure for weights. The remaining difference is
workflow context, not a distinct value type. This consolidation is why there is
no separate `FloatMarketCapitalizationObservationFrame`; the bridge/canonical
frame count is 18.

The bridge and canonical ontology both declare frame names on purpose. A
`BridgeFrame` is a bridge-local target label for projection mappings; a
`CanonicalFrame` is the shared ontology concept. Matching names coordinate the
two layers without making the bridge import or replace the canonical ontology.

## Membership State Projection

`IndexComponent` is modeled as a canonical role-assignment type, not as a
physical subtype of `Security`. The underlying instrument is represented
separately through `index_component_security(component, security)`, and the
index for which the role is held through `index_component_index(component,
index)`. This avoids silently treating every security as a component, or every
component role as the underlying security itself.

Local `index_component` relations are not all the same predicate. Some local
formulas describe generic membership, some describe selection-day inclusion,
and some describe calculation-day component scope.

The merge layer therefore uses membership frames:

- `GenericIndexComponentMembershipFrame`;
- `SelectionDayIndexComponentMembershipFrame`;
- `CalculationDayIndexComponentMembershipFrame`.

Bridge projections assign roles such as `MembershipSecurityRole`,
`MembershipComponentAssignmentRole`, `MembershipIndexRole`,
`MembershipSelectionDayRole`, and `MembershipCalculationDayRole`. This is the
state/lifecycle model for component membership: it preserves the local source
translation while giving the merged theory a way to distinguish "this security
is reflected in the Index", "this component role was selected on Selection
Day", and "this component role is in calculation-day scope".

The earlier generic `MembershipComponentRole` was removed after this split. A
membership projection must now say whether the local argument is the underlying
`Security` or the component-role assignment object.

## Eligible Rebalance Day

`EligibleRebalanceDay` is not modeled as a subtype of `RebalanceDay` in the
canonical ontology. N09 defines day eligibility across exchanges; N26 defines
when an eligible day becomes the actual Rebalance Day under the schedule and
fallback rule. Treating eligibility as a Rebalance Day subtype would incorrectly
make every eligible candidate day an actual rebalance event/day.

## Process Readiness Notes

See `process_bridge_readiness_notes_v1.md` for the process-layer review queue.
The important pre-process calendar links are now explicit in the bridge:

- `BusinessDayProcessFamily`;
- `CloseOfBusinessProcessFamily`;
- `FixingDayProcessFamily`.

These are related-concept families, not blanket exact aliases. They are meant to
support workflow drafting without rewriting local source-faithful definitions.

## Lexical Candidate Closure

The latest bridge candidate review closed the seven lexical candidates that had
no explicit bridge-symbol coverage.

Exact aliases:

- Section 2.1 GBS Benchmark Series PDF document = N14 GBS Benchmark Series
  guideline document.
- Section 2.1 `www` URL = N14 no-`www` URL for the same GBS Benchmark Series
  PDF path.
- Section 2.2 Free Float Market Capizatlization = section 2.3 Float Market
  Capizatlization as the same FFMC value.
- Section 4.6 `VarietyReasons` = section 4.7 `VarietyOfReasons`.

Related-only, not exact aliases:

- Section 1.3 and section 4.1 local index-scope predicates.
- Section 4.4 generic index adjustment and section 4.5 corporate-action
  adjustment.
- N15 GBS-index reflection and N19 methodology-index reflection.
