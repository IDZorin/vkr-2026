# Section 1.4 Translator Notes

## 2026-05-10T00:10:00+02:00 - Last-available WM Fixing attribution

Decision: keep `last_available_wm_fixing_4pm_london_quoted_by_reuters` in the main IR, but treat it as an explicitly documented inference from the same WM Fixing series.

Accepted:

- `wm_fixing_quoted_by(wm_fixing_4pm_london(src, tgt, d), Reuters)` is source-explicit.
- `wm_fixing_quoted_by(last_available_wm_fixing_4pm_london(src, tgt, d), Reuters)` is a reasonable source-consistent inference, because the fallback is the last available value of the same "04:00 p.m. London time WM Fixing" series.
- The fallback retains the same 04:00 p.m. London time characterization via `fixing_time(..., Time04_00PMLondon, LondonTime)`.

Rejected:

- Do not treat the fallback as an unrelated foreign-exchange rate source.
- Do not silently present the fallback Reuters attribution as a separate explicit source sentence.

Rationale:

The source explicitly says that closing-price conversion uses the "04:00 p.m. London time WM Fixing quoted by Reuters". The next sentence says that, if there is no such fixing for the relevant Calculation Day, "the last available 04:00 p.m. London time WM Fixing" will be used. It does not repeat "quoted by Reuters" in the fallback sentence. The IR interprets the fallback as the last available observation of the same WM Fixing series, rather than a different fixing source. This is a design inference for consistency of the time series and should remain visible in translator notes/provenance.

## 2026-05-10T00:25:00+02:00 - Token waiver review

Decision: approve the remaining uncovered tokens as absorbed by existing IR structure rather than adding new symbols.

Accepted:

- `frequency` is title-level scope and is represented by the intraday calculation window plus the closing-level calculation for each Calculation Day.
- `Should` is represented by the conditional fallback rule for missing current Trading Price.
- `addition` is a discourse marker introducing the separate closing-level flow.
- `respective` is represented by the shared Exchange variable in the closing-price listing/price relation.
- `relevant` is represented by the shared CalculationDay variable in the WM-fallback rule.
- `will` is represented as a hard fallback rule: missing same-day WM Fixing implies use of the last available WM Fixing.

Rejected:

- Do not add standalone relations such as `calculation_frequency`, `in_addition_to`, `relevant_day`, or `respective_exchange` unless they carry new formula-bearing semantics.
- Do not rely on names alone when the token expresses a real link; here the real links are already in formula bodies through shared variables and implications.

## 2026-05-10T11:45:00+02:00 - Explicit `later_of` contract

Decision: keep `later_of : Price, Price -> Price`, but add formula-body bridge constraints that define how it selects the later price.

Accepted:

- `later_of_returns_a_candidate` states that `later_of(p1, p2)` returns either `p1` or `p2`, not an unrelated third price.
- `later_of_selects_temporally_later_candidate` states that the candidate marked by `price_selection_order` is selected.
- `fallback_price_candidates_are_temporally_comparable` states that the two fallback candidates in Section 1.4 are comparable for the source phrase "the later of".

Rejected:

- Do not rely only on the helper name `later_of`.
- Do not model a full market timestamp ontology here; this section only needs the source-local selection contract for the two fallback price candidates.

Rationale:

The source explicitly uses the operator "the later of" between two price candidates. Earlier IR encoded this with a helper function, which preserved the wording but left the helper semantics implicit. The added constraints keep the same abstraction level while making the selection semantics visible to deterministic checks and LLM judges. The helper relation is named `price_selection_order` rather than `price_observed_after` to avoid encoding a temporal primitive as an ordinary relation name.
