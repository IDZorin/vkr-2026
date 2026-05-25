# Provenance Back-Translation Metrics: N30

- status: `ok`
- semantic_requested: `False`
- claim_count/source_claim_count: `10` / `10`
- claims_with_warnings/source_claims_with_warnings: `3` / `3`
- mean deterministic score: `0.762`
- mean source-claim deterministic score: `0.762`
- mean source token recall: `0.764`
- mean back-translation token precision: `0.458`
- warning_counts: `{"low_back_translation_token_precision": 1, "low_source_token_recall": 1, "negation_not_preserved": 3}`

## Lowest Deterministic Scores

| claim | origin | score | recall | precision | warnings |
| --- | --- | ---: | ---: | ---: | --- |
| `trading_day_definition` | `source_claim` | `0.502` | `0.333` | `0.1` | `low_source_token_recall`, `low_back_translation_token_precision`, `negation_not_preserved` |
| `market_disruption_counterfactual_condition` | `source_claim` | `0.617` | `0.667` | `0.353` | `negation_not_preserved` |
| `early_cessation_exclusion` | `source_claim` | `0.678` | `0.8` | `0.5` | `negation_not_preserved` |
| `trading_day_context_definition` | `source_claim` | `0.793` | `0.727` | `0.444` | - |
| `scheduled_shortened_period_exclusion` | `source_claim` | `0.805` | `0.833` | `0.417` | - |
| `new_index_components_close_of_trading_clarification` | `source_claim` | `0.825` | `0.688` | `0.611` | - |
| `rebalance_day_component_scope` | `source_claim` | `0.827` | `0.833` | `0.5` | - |
| `open_for_trading_condition` | `source_claim` | `0.844` | `1.0` | `0.455` | - |
| `index_administrator_responsibility_for_trading_day_determination` | `source_claim` | `0.857` | `0.875` | `0.583` | - |
| `following_calculation_day_component_scope` | `source_claim` | `0.868` | `0.889` | `0.615` | - |
