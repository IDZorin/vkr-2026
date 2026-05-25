# Section 1.3 Translator Notes

## 2026-05-09T22:08:00+02:00 - Direct cross-section index references

Decision: section 1.3 directly reuses the canonical index entities introduced in section 1.2.

Accepted:

- `SolactiveTransatlanticCleanEnergyEURIndexPR`
- `SolactiveTransatlanticCleanEnergyEURIndexNTR`
- `SolactiveTransatlanticCleanEnergyEURIndexTR`
- `SolactiveTransatlanticCleanEnergyEURIndex50AR`
- `SolactiveTransatlanticCleanEnergyEURIndex5PercentAR`

Rejected:

- Do not introduce a local abstract `TheIndex` entity for section 1.3 and bridge it later.
- Do not introduce a separate local alias for `Solactive Transatlantic Clean Energy EUR Index 50 AR`.

Rationale:

Section 1.3 uses the source phrase "the Index" for the index family, but it also explicitly names `Solactive Transatlantic Clean Energy EUR Index 50 AR`. Because section 1.2 already establishes the canonical index entities, direct reuse is clearer than creating section-local aliases. This differs from section 4.1, where the source uses local calculation names such as `SOLTCA50`, `NTR Index version`, and `GTR Index version`; those require a separate bridge layer.

## 2026-05-09T22:08:00+02:00 - Start Date and Live Date representation

Decision: encode the two dates as role-bearing date entities:

- `StartDate05_08_2017 : Day`
- `LiveDate29_09_2025 : Day`

Accepted:

- Use `start_date(StartDate05_08_2017)` and `live_date(LiveDate29_09_2025)` as role tags.
- Use the same date entities in formula bodies, for example `initial_level(i, StartDate05_08_2017)`.

Rejected:

- Do not split each date into a separate role entity and value entity, such as `StartDate = D2017_08_05`, unless a later backend requires explicit calendar arithmetic.
- Do not make `start_date_of : Index -> Day` unless the methodology later distinguishes start dates per index.

Rationale:

The source gives one Start Date and one Live Date for the section. The IR therefore keeps the date values first-class and token-visible without inventing per-index date variation. The date-bearing names also keep token provenance auditable for `05/08/2017` and `29/09/2025`.

## 2026-05-09T22:08:00+02:00 - "will be recorded" as a hard source assertion

Decision: treat "Historical values from the Live Date will be recorded in accordance with Article 8 of the BMR" as a hard source-backed rule.

Accepted:

- `historical_values_from_live_date_recorded_in_accordance_with_article_8_of_bmr` is a `constraint`.
- The token `will` is absorbed into the hard legal/future assertion rather than represented by a separate modal declaration.

Rejected:

- Do not model `will` as a separate deontic obligation without an explicit actor.
- Do not weaken the statement to a mere descriptive fact about Article 8.

Rationale:

In this section, "will be recorded" specifies how historical values from the Live Date are to be handled. The important semantics are the temporal scope from the Live Date and the required Article 8 / BMR recording basis, both of which are present in the formula body.

## 2026-05-09T22:08:00+02:00 - Static "prior to the Live Date" relation

Decision: encode "period prior to the Live Date" as a static period/date relation, not as a TemporalDecl.

Accepted:

- `period_prior_to(p, LiveDate29_09_2025)` is used in the back-tested-level constraint.
- `day_before(d, LiveDate29_09_2025)` is used for the from-Live-Date historical-values rule.

Rejected:

- Do not add a dummy `prop` solely to satisfy a family-coverage heuristic.

Rationale:

The source does not describe a temporal process, trace property, or LTL-style sequence. It describes a static partition between values from the Live Date and levels published for a period before the Live Date. The minimal prelude already provides `Day`, `Period`, and `day_before`; `period_prior_to` is the section-local relation that connects a published period to the Live Date.
