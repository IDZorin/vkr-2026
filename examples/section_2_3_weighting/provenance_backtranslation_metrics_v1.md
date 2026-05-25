# Provenance Back-Translation Metrics: section_2_3_weighting

- status: `ok`
- semantic_requested: `False`
- claim_count/source_claim_count: `5` / `5`
- claims_with_warnings/source_claims_with_warnings: `1` / `1`
- mean deterministic score: `0.833`
- mean source-claim deterministic score: `0.833`
- mean source token recall: `0.754`
- mean back-translation token precision: `0.571`
- warning_counts: `{"low_back_translation_token_precision": 1}`

## Lowest Deterministic Scores

| claim | origin | score | recall | precision | warnings |
| --- | --- | ---: | ---: | ---: | --- |
| `weights_redistributed_proportionally` | `source_claim` | `0.684` | `0.4` | `0.222` | `low_back_translation_token_precision` |
| `region_represents_exactly_50_percent` | `source_claim` | `0.802` | `0.75` | `0.462` | - |
| `weight_redistribution_process_is_iterative` | `source_claim` | `0.839` | `0.8` | `0.571` | - |
| `single_index_component_weight_capped` | `source_claim` | `0.914` | `1.0` | `0.7` | - |
| `weight_based_on_float_market_capitalization` | `source_claim` | `0.924` | `0.818` | `0.9` | - |
