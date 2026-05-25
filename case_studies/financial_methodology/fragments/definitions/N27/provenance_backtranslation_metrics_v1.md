# Provenance Back-Translation Metrics: N27

- status: `ok`
- semantic_requested: `False`
- claim_count/source_claim_count: `3` / `3`
- claims_with_warnings/source_claims_with_warnings: `3` / `3`
- mean deterministic score: `0.621`
- mean source-claim deterministic score: `0.621`
- mean source token recall: `0.433`
- mean back-translation token precision: `0.569`
- warning_counts: `{"low_source_token_recall": 1, "number_not_preserved": 3}`

## Lowest Deterministic Scores

| claim | origin | score | recall | precision | warnings |
| --- | --- | ---: | ---: | ---: | --- |
| `twenty_business_days_count` | `source_claim` | `0.525` | `0.2` | `0.333` | `low_source_token_recall`, `number_not_preserved` |
| `rebalance_day_change_disregarded_for_selection_day` | `source_claim` | `0.644` | `0.5` | `0.625` | `number_not_preserved` |
| `selection_day_definition` | `source_claim` | `0.693` | `0.6` | `0.75` | `number_not_preserved` |
