# Section 4.6 Translator Notes

This file records translator decisions for the current `main_ir.a4v3`.
It is review memory, not an additional source of methodology claims.

## Changelog

### 2026-05-11T10:25:00+02:00

Decision: use Copy 1 as the base and clean it for explicit polarity, scoped universals, and source-only provenance.

Accepted:

- `cannot be completely ruled out` is represented as `not completely_ruled_out(...)` over a positive polarity relation.
- `errors ... may occur` is represented by an `ErrorPossibility` carrier, not by asserting that an actual error exists.
- `from time to time` and `variety reasons` are retained as `VagueTerm` carriers.
- `internal` and `external` are retained as enum values, in parallel with the vague phrase `variety reasons`.
- `SolactiveDeterminationProcess` is a specific carrier for "the determination process"; correction of identified errors is scoped to errors in this process.
- `GeneralMeasuresToBeTaken` is modeled as a structural `GeneralMeasure`, not as a vague term.
- `incorporated by reference` is directed: `incorporated_by_reference_into(SolactiveCorrectionPolicy, ThisGuideline)`.
- The underlying dependency is modeled as a source-level dependency fact with an existential underlying, not as a universal rule over every index/underlying pair.
- Accurate calculation and accurate maintenance are represented as `IndexEffortGoal` enum values, so "accurately calculate and maintain" is not limited to calculation only and does not rely on repeated relation-name tokens.

Rejected / alternatives:

- Do not include `https://www.solactive.com/documents/correction-policy/` in main IR: the section source names the Solactive website but does not print a URL.
- Do not model `endeavors to correct` as a strict `obligation`; it is treated as a best-effort/process commitment rather than a "shall/must" rule.
- Do not use bare universals over all `Error` or all `GeneralMeasure` instances.

Validation:

- Deterministic checks: `clean_gate=accepted`, semantic lint `0`, token waiver-adjusted coverage `1.0`, phrase coverage `1.0`.
- LLM checks: single semantic judge `corresponds`; corpus-aware multi judge `corresponds`; ordinary multi judge `partially_corresponds`.
- The ordinary multi-judge objection is about expected seed methodology reification (`Description`, `UnderlyingDependency`, `PolicySpecification`, and `IndexEffortGoal` carriers), not about an uncovered source phrase or contradiction. This is accepted because the provenance ledger records why each carrier exists and keeps the source-only / bridge distinction visible.
