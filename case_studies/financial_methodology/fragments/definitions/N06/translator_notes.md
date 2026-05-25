# Definition N06 Translator Notes

This file records translator decisions for the current `main_ir.a4v3`.
It is review memory, not an additional source of methodology claims.

## Changelog

### 2026-05-12T13:25:00+02:00

Decision: represent `"Close of Business" is the calculation time of the closing level of the Index as outlined in Section 1.4` as a named `CalculationTime` entity with source-backed properties.

Accepted:

- `CloseOfBusiness` is a named entity of sort `CalculationTime`, because the source identifies the term as a calculation time.
- The definition is a fact about that named term, not a universal biconditional over all calculation times.
- `Section1_4` is a DocumentPart reference target; the detailed calculation-time logic remains in Section 1.4 and/or the bridge layer.
- Back-translation should preserve the definite source phrase "the calculation time"; the named entity `CloseOfBusiness` carries that specificity without adding a separate uniqueness axiom.

Rejected / alternatives:

- Do not import all Section 1.4 mechanics into this definition.
- Do not model Close of Business as an event here; other sections may use event-like carriers locally, and merge/bridge work can align those local views.
- Do not use `forall t ... iff ...` here; the source names a specific term rather than defining a broad class of calculation times.

Rationale: the source's head noun is "calculation time". A named entity avoids over-committing to a richer event ontology and avoids over-generalizing the definition to arbitrary calculation times.
