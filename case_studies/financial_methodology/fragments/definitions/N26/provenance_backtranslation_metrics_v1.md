# Provenance Back-Translation Metrics: N26

- status: `ok`
- semantic_requested: `False`
- claim_count/source_claim_count: `4` / `4`
- claims_with_warnings/source_claims_with_warnings: `3` / `3`
- mean deterministic score: `0.675`
- mean source-claim deterministic score: `0.675`
- mean source token recall: `0.666`
- mean back-translation token precision: `0.577`
- warning_counts: `{"low_source_token_recall": 1, "modal_family_not_preserved": 3, "negation_not_preserved": 1}`

## Lowest Deterministic Scores

| claim | origin | score | recall | precision | warnings |
| --- | --- | ---: | ---: | ---: | --- |
| `immediately_following_eligible_rebalance_day_definition` | `source_claim` | `0.526` | `0.75` | `0.5` | `modal_family_not_preserved`, `negation_not_preserved` |
| `first_weekday_ordinal_value` | `source_claim` | `0.536` | `0.333` | `0.25` | `low_source_token_recall`, `modal_family_not_preserved` |
| `rebalance_day_definition` | `source_claim` | `0.679` | `0.583` | `0.7` | `modal_family_not_preserved` |
| `scheduled_rebalance_day_definition` | `source_claim` | `0.959` | `1.0` | `0.857` | - |
