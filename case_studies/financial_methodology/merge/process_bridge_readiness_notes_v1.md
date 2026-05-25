# Financial Methodology Process Bridge Readiness Notes v1

This note records the remaining review tails that matter before drafting
`process/*.a4v3`.

## Status

The local IR, bridge, canonical ontology, and resolved methodology view are
ready for process-layer drafting.

Current deterministic gates:

- `bridge_lint_v1`: passed, hard 0, soft 0.
- `merge_readiness_audit_v1`: passed, hard 0, soft 0, advisory 0.
- `bridge_candidate_audit_v1`: no parser warnings, no unbridged repeated exact
  declarations, no assertion external identifiers.

The remaining review items are not process blockers. They are guardrails for
the future merge and reasoning layers.

## Process-Critical Calendar Bridge

The process layer needs a stable calendar spine. The following source-phrase
recurrences are now explicitly bridged:

- `Business Day`: N04 defines the business-day predicate; N27 uses business-day
  counting for Selection Day. These are related process-calendar concepts, not
  exact aliases.
- `Close of Business`: N06 defines the term as the calculation time of the
  closing level; section 3.1 uses Close of Business as the temporal marker after
  which the ordinary rebalance adjusts the Index. These are related concepts,
  not an exact sort/entity identity.
- `Fixing Day`: N11 defines Fixing Day as Selection Day; section 3.1 uses
  Fixing Day as the day on which shares are determined for a rebalance.

## Review Tails To Keep Visible

### Same Name, Different Signature

There are 27 same-name/different-signature cases. They are explicitly covered
by bridge decisions, but they should stay visible because exact name-based merge
would be unsafe.

Process-relevant examples:

- `index_component` / `index_component_of` are projected to membership-state
  frames rather than exact-merged.
- `closing_price`, `trading_price`, `weight`, `region`, and FFMC
  functions are projected to observation frames rather than force-merged.
- `Business Day`, `Close of Business`, and `Fixing Day` are now bridged through
  process-calendar families.

### Lexical And Source-Phrase Candidates

Lexical/source-phrase candidates remain review prompts, not automatic merge
instructions. They should be checked when a process rule needs the corresponding
concept.

Resolved examples:

- `Float Market Capizatlization` in section 2.3 is treated as shorthand for
  Free Float Market Capitalization, because N13 defines FFMC and no separate
  Float Market Capitalization definition exists in the methodology.

Still-visible examples:

- Section reference entities remain document pointers, not domain concepts.

## Process-Layer Boundary

The process layer should model transitions and ordering:

- universe construction;
- component selection;
- weight calculation;
- fixing-day share determination;
- rebalance execution;
- corporate-action-driven changes;
- disruption, correction, and termination flows.

It should not retroactively rewrite local source-faithful IR. When process rules
need cross-fragment concepts, they should consume the resolved methodology view,
bridge families, and canonical frames.
