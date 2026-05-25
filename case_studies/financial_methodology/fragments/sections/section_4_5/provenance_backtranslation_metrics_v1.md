# Provenance Back-Translation Metrics: section_4_5

- status: `ok`
- semantic_requested: `False`
- claim_count/source_claim_count: `13` / `11`
- claims_with_warnings/source_claims_with_warnings: `2` / `2`
- mean deterministic score: `0.831`
- mean source-claim deterministic score: `0.831`
- mean source token recall: `0.726`
- mean back-translation token precision: `0.686`
- warning_counts: `{"modal_family_not_preserved": 2}`

## Lowest Deterministic Scores

| claim | origin | score | recall | precision | warnings |
| --- | --- | ---: | ---: | ---: | --- |
| `considered_corporate_actions_result_in_index_adjustment` | `source_claim` | `0.646` | `0.529` | `0.6` | `modal_family_not_preserved` |
| `corporate_action_implementation_period_and_price_effect` | `source_claim` | `0.721` | `0.733` | `0.733` | `modal_family_not_preserved` |
| `account_for_corporate_action_in_index_calculation` | `source_claim` | `0.726` | `0.5` | `0.333` | - |
| `non_conclusive_means_not_conclusive` | `bridge` | `0.734` | `0.667` | `0.25` | - |
| `considered_corporate_actions_have_material_impact` | `source_claim` | `0.787` | `0.7` | `0.438` | - |
| `make_corporate_action_adjustment_in_compliance_with_equity_index_methodology` | `source_claim` | `0.804` | `0.6` | `0.6` | - |
| `corporate_action_deviation_conditions` | `source_claim` | `0.845` | `0.72` | `0.667` | - |
| `equity_index_methodology_material_for_covered_corporate_actions` | `source_claim` | `0.846` | `0.75` | `0.643` | - |
| `deviate_from_standard_procedures` | `source_claim` | `0.866` | `0.7` | `0.778` | - |
| `index_maintenance_scope` | `plumbing` | `0.929` | `0.75` | `1.0` | - |
| `corporate_action_treatment_methodology_aim` | `source_claim` | `0.948` | `0.818` | `1.0` | - |
| `relevant_corporate_action_list` | `source_claim` | `0.956` | `0.966` | `0.875` | - |
