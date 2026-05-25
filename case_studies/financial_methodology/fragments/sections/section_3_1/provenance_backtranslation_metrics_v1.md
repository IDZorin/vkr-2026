# Provenance Back-Translation Metrics: section_3_1

- status: `ok`
- semantic_requested: `False`
- claim_count/source_claim_count: `8` / `7`
- claims_with_warnings/source_claims_with_warnings: `4` / `3`
- mean deterministic score: `0.779`
- mean source-claim deterministic score: `0.794`
- mean source token recall: `0.67`
- mean back-translation token precision: `0.566`
- warning_counts: `{"low_back_translation_token_precision": 2, "modal_family_not_preserved": 1, "number_not_preserved": 1}`

## Lowest Deterministic Scores

| claim | origin | score | recall | precision | warnings |
| --- | --- | ---: | ---: | ---: | --- |
| `ordinary_rebalance_adjusts_index_after_close_of_business` | `source_claim` | `0.627` | `0.471` | `0.571` | `number_not_preserved` |
| `solactive_publishes_index_component_changes_with_notice` | `source_claim` | `0.667` | `0.647` | `0.579` | `modal_family_not_preserved` |
| `section_3_1_index_component_change_scope` | `plumbing` | `0.671` | `0.4` | `0.167` | `low_back_translation_token_precision` |
| `publish_index_component_change` | `source_claim` | `0.678` | `0.375` | `0.214` | `low_back_translation_token_precision` |
| `ordinary_rebalance_implements_fixing_day_shares` | `source_claim` | `0.856` | `0.909` | `0.556` | - |
| `announcement_section_location` | `source_claim` | `0.896` | `0.75` | `0.857` | - |
| `more_information_refer_to_equity_index_methodology` | `source_claim` | `0.901` | `0.812` | `0.812` | - |
| `new_selection_determined_in_accordance_with_sections` | `source_claim` | `0.934` | `1.0` | `0.769` | - |
