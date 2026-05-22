# Domain Prelude: Index Methodology v1

Reusable index-methodology primitives for selection, weighting, buffer rules, and starting instrument lists.

This is intentionally separate from `minimal_prelude_v1`: these symbols are useful for index methodologies, but they are not universal cross-domain primitives.

## Included Sorts

- `MethodologyRule`
- `IndexSelectionRule extends MethodologyRule`
- `IndexWeightingRule extends MethodologyRule`
- `IndexBufferRule extends IndexSelectionRule`
- `StartingListOfFinancialInstruments`

## Included Entities

None. Concrete universes and concrete rules should be local entities grounded in the methodology text.

## Included Functions And Relations

None. This prelude only provides reusable types. Local IR or merge-level overlays may add explicit links when the source warrants them.

## Notes

`StartingListOfFinancialInstruments` is the reusable type for a starting list of instruments before methodology-specific eligibility, selection, buffer, and weighting rules are applied.

It may be sourced from another index, a fixed list, a client-provided list, an exchange universe, or another explicit candidate source.

`IndexBufferRule` is a specialized selection rule used when a methodology defines buffer logic, usually to reduce unnecessary turnover or switching.

Concrete examples such as a GBS universe, a current-company buffer rule, or a not-current-company buffer rule belong in local IR, not in this prelude.
