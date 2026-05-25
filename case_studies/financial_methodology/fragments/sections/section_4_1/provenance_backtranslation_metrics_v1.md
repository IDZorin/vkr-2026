# Provenance Back-Translation Metrics: section_4_1

- status: `ok`
- semantic_requested: `False`
- claim_count/source_claim_count: `10` / `10`
- claims_with_warnings/source_claims_with_warnings: `5` / `5`
- mean deterministic score: `0.76`
- mean source-claim deterministic score: `0.76`
- mean source token recall: `0.68`
- mean back-translation token precision: `0.669`
- warning_counts: `{"modal_family_not_preserved": 2, "negation_not_preserved": 2, "number_not_preserved": 2}`

## Lowest Deterministic Scores

| claim | origin | score | recall | precision | warnings |
| --- | --- | ---: | ---: | ---: | --- |
| `section_4_1_index_scope` | `source_claim` | `0.615` | `0.381` | `0.615` | `number_not_preserved` |
| `soltca50_adjusted_return_index_formula` | `source_claim` | `0.649` | `0.68` | `0.68` | `number_not_preserved`, `negation_not_preserved` |
| `equity_index_methodology_reference` | `source_claim` | `0.666` | `0.56` | `0.667` | `modal_family_not_preserved` |
| `calendar_day_count_for_adjusted_return_formula` | `source_claim` | `0.692` | `0.727` | `0.615` | `negation_not_preserved` |
| `adjusted_return_version_decrement_from_ntr` | `source_claim` | `0.762` | `0.708` | `0.944` | `modal_family_not_preserved` |
| `calculation_performed_according_to_equity_index_methodology` | `source_claim` | `0.818` | `0.667` | `0.6` | - |
| `distributions_reinvested_back_at_opening_of_effective_ex_date` | `source_claim` | `0.827` | `0.579` | `0.733` | - |
| `standard_index_formula_basis` | `source_claim` | `0.83` | `0.739` | `0.586` | - |
| `index_calculated_as_return_forms` | `source_claim` | `0.845` | `0.875` | `0.538` | - |
| `soltca50_decrement_from_gtr` | `source_claim` | `0.893` | `0.882` | `0.714` | - |
