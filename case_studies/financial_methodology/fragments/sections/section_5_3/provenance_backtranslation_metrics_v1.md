# Provenance Back-Translation Metrics: section_5_3

- status: `ok`
- semantic_requested: `False`
- claim_count/source_claim_count: `13` / `12`
- claims_with_warnings/source_claims_with_warnings: `8` / `7`
- mean deterministic score: `0.735`
- mean source-claim deterministic score: `0.754`
- mean source token recall: `0.577`
- mean back-translation token precision: `0.696`
- warning_counts: `{"low_back_translation_token_precision": 1, "low_source_token_recall": 5, "modal_family_not_preserved": 7, "negation_not_preserved": 2}`

## Lowest Deterministic Scores

| claim | origin | score | recall | precision | warnings |
| --- | --- | ---: | ---: | ---: | --- |
| `withhold_information_on_modification_or_change` | `source_claim` | `0.411` | `0.3` | `0.375` | `low_source_token_recall`, `modal_family_not_preserved`, `negation_not_preserved` |
| `information_withheld_means_information_not_provided` | `bridge` | `0.506` | `0.2` | `0.222` | `low_source_token_recall`, `low_back_translation_token_precision`, `modal_family_not_preserved` |
| `make_deemed_modification_or_change` | `source_claim` | `0.596` | `0.13` | `0.429` | `low_source_token_recall`, `modal_family_not_preserved` |
| `index_administrator_for_index` | `source_claim` | `0.615` | `0.154` | `1.0` | `low_source_token_recall`, `modal_family_not_preserved` |
| `deemed_modification_or_change_scope` | `source_claim` | `0.646` | `0.565` | `0.565` | `modal_family_not_preserved` |
| `potential_method_change_reasons` | `source_claim` | `0.677` | `0.714` | `0.769` | `modal_family_not_preserved`, `negation_not_preserved` |
| `take_appropriate_steps_for_consistent_calculation_method` | `source_claim` | `0.731` | `0.312` | `0.556` | `low_source_token_recall` |
| `appropriate_steps_consistency_target` | `source_claim` | `0.769` | `0.692` | `1.0` | `modal_family_not_preserved` |
| `apply_described_method` | `source_claim` | `0.841` | `0.556` | `0.833` | - |
| `described_method_for_composition_and_calculation` | `source_claim` | `0.857` | `1.0` | `0.5` | - |
| `described_method_reference` | `source_claim` | `0.943` | `1.0` | `0.8` | - |
| `described_method_application_final_and_binding` | `source_claim` | `0.964` | `0.875` | `1.0` | - |
