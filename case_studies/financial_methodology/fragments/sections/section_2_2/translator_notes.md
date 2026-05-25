# Section 2.2 Translator Notes

This file records translator decisions for the current `main_ir.a4v3`.
It is review memory, not an additional source of methodology claims.

## Changelog

### 2026-05-09T15:59:52+02:00

Decision: make regional country-assignment branches definitional and document scarcity as an explanatory consequence.

Accepted:

- `americas_country_assignment_classification` now uses `iff`: an eligible security is in `Americas` exactly when its GBS Country Assignment is `Canada` or `UnitedStates`.
- `europe_country_assignment_classification` now uses `iff`: an eligible security is in `EuropeRegion` exactly when its GBS Country Assignment is `Europe`.
- The scarcity clause remains existential over regions: if any one of the regional buckets has fewer than 20 eligible securities, the total number of Index Components is below 40.

Rejected / alternatives:

- Do not keep the regional bullets as one-way implications only; in this source, "Americas if..." and "Europe if..." define the two-region classification scheme.
- Do not change the scarcity antecedent to "both regions have fewer than 20 eligible securities". That would understate the explanatory point: one underfilled regional bucket is already enough to make the total below 40 under a top-20-per-region rule.

Rationale: the section gives a deterministic two-region classification and then explains the arithmetic consequence of top-20 selection across two regional buckets. The IR should encode the classification as definitions while preserving the scarcity explanation as "any regional shortfall implies total below 40".

### 2026-05-09T15:47:46+02:00

Decision: encode "one of the two regions" as an explicit source-backed region-domain constraint.

Accepted:

- Added `security_classified_into_one_of_two_regions`.
- For every eligible security, `region(d, s)` must be either `Americas` or `EuropeRegion`.
- Because `region` is a required function, this gives a single region value; the new constraint restricts the value to the two source regions.

Rejected / alternatives:

- Do not rely only on the two country-assignment implications. Those rules say when a security maps to Americas or Europe, but they do not by themselves exclude additional Region values.
- Do not move this to `repair.a4v3`; "one of the two regions" is direct source text, not a backend-only derived invariant.

Rationale: the source phrase "Each security is classified into one of the two regions" contains a domain/exhaustiveness claim in addition to the Americas/Europe mapping rules. The IR now makes that claim visible in the formula body.

### 2026-05-09T15:39:57+02:00

Decision: make the section-local `eligible` scope equivalent to the Index Universe.

Accepted:

- `eligible_iff_index_universe_for_component_requirements` now uses `eligible(d, s) iff index_universe(d, s)`.
- In section 2.2, `eligible` is a local rule-domain alias for securities considered under the Index Component Requirements, not an extra filter narrower than the Index Universe.
- Classification, ranking, top-20 selection, and scarcity formulas can keep the concise `eligible(d, s)` guard without losing the source scope "Based on the Index Universe".

Rejected / alternatives:

- Do not leave only `eligible(d, s) implies index_universe(d, s)`, because that permits Index Universe securities outside the classification/ranking/selection domain and makes the IR look narrower than the source.
- Do not remove the `eligible` predicate everywhere; it is useful source vocabulary for the scarcity clause "less than 20 securities per region are eligible".

Rationale: the source does not quantify over every security in the world. It quantifies over securities in the local section scope: the Index Universe under the Index Component Requirements. The equivalence makes that scope explicit and removes the false reading that `eligible` is an additional eligibility screen.

### 2026-05-09T12:33:33+02:00

Decision: treat the current multi-judge `partially_corresponds` verdict as a review signal, not a blocking rejection.

Accepted:

- The single semantic judge accepts the current IR as `corresponds`.
- The clean gate accepts the current IR with no blocking deterministic findings.
- The multi-judge panel correctly points to modeling choices that deserve human review: `eligible` is used as the local scope guard, and the top-20 / fewer-than-40 logic is formalized with an explicit eligible-security count.

Rejected / alternatives:

- Do not remove the `eligible` guard merely to satisfy the literal phrase "each security"; section 2.2 is scoped by the Index Universe and Index Component Requirements, so the guard is the intended local domain restriction. This is now made explicit by `eligible_iff_index_universe_for_component_requirements`.
- Do not silently strengthen the main IR with backend-only cardinality assumptions; those belong in `repair.a4v3`.

Rationale: the multi-judge complaint is useful but not decisive. It flags that the source text leaves some domain scoping implicit. The current financial methodology decision is to keep the source-backed rule in the main IR, keep the derived cardinality contract in `repair.a4v3`, and preserve this rationale for reviewers. For package-level semantic adequacy, `repair.a4v3` is evaluated together with `main_ir.a4v3`; the split records provenance, not a loss of meaning.

### 2026-05-09T12:04:58+02:00

Decision: separate source-backed top-20 translation from backend repair contracts.

Accepted:

- `selected_top_20_for_each_region` remains in `main_ir.a4v3` as the direct source-backed translation of "The top 20 securities for each region are selected for Index inclusion."
- `at_most_20_selected_per_region` moved to `repair.a4v3` as a `derived_invariant`, not an independent source claim.
- For package-level semantic adequacy, the repair overlay is part of the reviewed semantics; judges should not mark a semantic difference merely because the backend-safety contract lives in `repair.a4v3`.
- `provenance.yaml` now distinguishes `ir_origin_file` and `claim_origin`, so reviewers can see whether a formula came from the main IR or from the repair overlay.

Rejected / alternatives:

- Do not silently keep top-k cardinality guards in the main IR when they are not separate source sentences.
- Do not drop the repair entirely: without a cardinality guard or rank-uniqueness/tie-break contract, a backend can assign the same rank to many securities and still satisfy `rank <= 20`.

Rationale: this keeps the manual financial methodology translation honest while preserving the recommended backend contract. The gap is now explicit: main IR contains the source-backed rank-cut selection; `repair.a4v3` contains the derived contract that makes top-k cardinality semantics backend-safe.

### 2026-05-08T11:38:05+02:00

Decision: fix value typing for ranking/FMC and mark fully-rule-based governance as `fact`.

Accepted:

- `Rank` now extends `Nat`, because rank is compared with numeric literals and other ranks (`rank(...) <= 20`, `rank(...) < rank(...)`).
- `FreeFloatMarketCapizatlization` now extends `MonetaryAmount`, following the same value-sort convention used for ADVT in section 2.1.
- `selection_fully_rule_based` is now a `fact`, because it records a descriptive governance property of the selection process, not a hard numeric/count/ranking constraint.

Rejected / alternatives:

- Do not keep `Rank` or `FreeFloatMarketCapizatlization` as opaque sorts while using them in ordered comparisons.
- Do not encode `fully_rule_based(selection_of_index_components(d))` as a hard `constraint`; hard constraints remain the region, ranking, top-20, count, bridge, and scarcity rules.

Rationale: the source contains actual ordering/count requirements for selection, and those remain constraints. The governance statement is descriptive, while rank and free-float market capitalization are value-like quantities that need ordered/numeric structure.

### 2026-05-06T17:27:25+02:00

Decision: represent component selection as region classification, ranking, top-20 inclusion, scarcity consequence, and no-discretion governance.

Accepted:

- `eligible(d, s) iff index_universe(d, s)` preserves the source basis in the Index Universe and makes `eligible` the local rule-domain alias for section 2.2.
- `security_classified_into_one_of_two_regions` preserves the source restriction that each eligible security is classified into one of the two stated regions.
- Americas and Europe classification are explicit biconditional definitions from GBS country assignment to `region(d, s)`.
- Descending ranking is represented by a pairwise rank ordering constraint: higher Free Float Market Capizatlization implies lower/better rank.
- Top-20 selection is represented by `selected_for_index_inclusion(d, s) iff eligible(d, s) and rank(...) <= 20`.
- `at_most_20_selected_per_region` is explicit to preserve the cap implied by top 20.
- `index_component`, `initial_composition`, and `ordinary_rebalance_selection` are bridged to `selected_for_index_inclusion`.
- The scarcity clause is represented as an explanatory consequence: if any regional bucket has fewer than 20 eligible securities, then total Index Components are fewer than 40.
- No-discretion governance is represented as a `prohibition`.

Rejected / alternatives:

- Do not invent aggregate `sum` semantics here: the source talks about count/top-20 selection, not weights or sums.
- Do not let a long name such as `fewer_than_20_eligible...` carry the rule; the formula body must contain the count condition and total-component consequence.
- Do not model the GBS framework as a large local document object here; section 2.2 only needs the country assignment function.
- Do not treat `fully rule-based` as only a comment; it is represented by `fully_rule_based(selection_of_index_components(d))`.

Rationale: the section is algorithmic but local: classify, rank, select, handle scarcity, prohibit discretion. The current IR keeps those steps explicit and avoids adding financial semantics not present in the source.

Waiver rationale:

- `accordance` and `following` introduce rules already represented by constraints.
- `one` and `two` are absorbed by the two region entities.
- `under` and `framework` are absorbed by `gbs_country_assignment`.
- `case`, `contain`, and `total` are absorbed by the count-based scarcity formula.

Validation:

- clean gate: accepted
- phrase coverage: 14/14
- token accounted coverage: 55/55
- waivers: 9/9
