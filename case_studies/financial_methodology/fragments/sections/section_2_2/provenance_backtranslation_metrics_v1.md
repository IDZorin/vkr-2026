# Provenance Back-Translation Metrics: section_2_2

- status: `ok`
- semantic_requested: `False`
- claim_count/source_claim_count: `13` / `11`
- claims_with_warnings/source_claims_with_warnings: `2` / `1`
- mean deterministic score: `0.82`
- mean source-claim deterministic score: `0.83`
- mean source token recall: `0.721`
- mean back-translation token precision: `0.555`
- warning_counts: `{"low_source_token_recall": 2}`

## Lowest Deterministic Scores

| claim | origin | score | recall | precision | warnings |
| --- | --- | ---: | ---: | ---: | --- |
| `eligible_iff_index_universe_for_component_requirements` | `source_claim` | `0.708` | `0.333` | `0.4` | `low_source_token_recall` |
| `index_components_selected_for_index_inclusion` | `bridge` | `0.716` | `0.333` | `0.444` | `low_source_token_recall` |
| `initial_composition_determined_by_index_component_requirements` | `source_claim` | `0.752` | `0.455` | `0.5` | - |
| `ordinary_rebalance_selection_determined_by_index_component_requirements` | `source_claim` | `0.763` | `0.556` | `0.455` | - |
| `selected_top_20_for_each_region` | `source_claim` | `0.793` | `0.75` | `0.429` | - |
| `at_most_20_selected_per_region` | `derived_invariant` | `0.811` | `0.75` | `0.5` | - |
| `security_classified_into_one_of_two_regions` | `source_claim` | `0.815` | `0.833` | `0.455` | - |
| `descending_order_by_free_float_market_capizatlization` | `source_claim` | `0.85` | `1.0` | `0.474` | - |
| `europe_country_assignment_classification` | `source_claim` | `0.853` | `0.733` | `0.688` | - |
| `less_than_20_per_region_less_than_40_index_components` | `source_claim` | `0.867` | `0.846` | `0.647` | - |
| `americas_country_assignment_classification` | `source_claim` | `0.875` | `0.778` | `0.737` | - |
| `selection_fully_rule_based` | `source_claim` | `0.918` | `1.0` | `0.714` | - |
