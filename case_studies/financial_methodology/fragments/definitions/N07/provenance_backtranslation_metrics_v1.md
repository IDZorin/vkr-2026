# Provenance Back-Translation Metrics: N07

- status: `ok`
- semantic_requested: `False`
- claim_count/source_claim_count: `2` / `2`
- claims_with_warnings/source_claims_with_warnings: `1` / `1`
- mean deterministic score: `0.734`
- mean source-claim deterministic score: `0.734`
- mean source token recall: `0.673`
- mean back-translation token precision: `0.695`
- warning_counts: `{"modal_family_not_preserved": 1, "negation_not_preserved": 1}`

## Lowest Deterministic Scores

| claim | origin | score | recall | precision | warnings |
| --- | --- | ---: | ---: | ---: | --- |
| `last_trading_price_used_when_closing_price_not_published` | `source_claim` | `0.589` | `0.533` | `0.667` | `modal_family_not_preserved`, `negation_not_preserved` |
| `closing_price_definition_when_published` | `source_claim` | `0.879` | `0.812` | `0.722` | - |
