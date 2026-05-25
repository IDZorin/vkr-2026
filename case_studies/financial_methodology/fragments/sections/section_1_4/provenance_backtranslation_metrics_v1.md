# Provenance Back-Translation Metrics: section_1_4

- status: `ok`
- semantic_requested: `False`
- claim_count/source_claim_count: `18` / `14`
- claims_with_warnings/source_claims_with_warnings: `8` / `5`
- mean deterministic score: `0.725`
- mean source-claim deterministic score: `0.739`
- mean source token recall: `0.588`
- mean back-translation token precision: `0.45`
- warning_counts: `{"low_back_translation_token_precision": 4, "low_source_token_recall": 5, "modal_family_not_preserved": 2, "negation_not_preserved": 3, "number_not_preserved": 1}`

## Lowest Deterministic Scores

| claim | origin | score | recall | precision | warnings |
| --- | --- | ---: | ---: | ---: | --- |
| `closing_price_kept_when_listed_in_index_currency` | `source_claim` | `0.375` | `0.235` | `0.25` | `low_source_token_recall`, `number_not_preserved`, `negation_not_preserved` |
| `intraday_price_kept_when_listed_in_index_currency` | `source_claim` | `0.499` | `0.188` | `0.2` | `low_source_token_recall`, `low_back_translation_token_precision`, `negation_not_preserved` |
| `later_of_returns_a_candidate` | `bridge` | `0.571` | `0.0` | `0.0` | `low_source_token_recall`, `low_back_translation_token_precision` |
| `later_of_selects_temporally_later_candidate` | `bridge` | `0.597` | `0.083` | `0.062` | `low_source_token_recall`, `low_back_translation_token_precision` |
| `current_trading_price_used_when_available` | `source_claim` | `0.599` | `0.556` | `0.357` | `negation_not_preserved` |
| `intraday_level_uses_exchange_trading_prices` | `source_claim` | `0.646` | `0.286` | `0.133` | `low_source_token_recall`, `low_back_translation_token_precision` |
| `closing_price_converted_with_last_available_wm_fixing` | `source_claim` | `0.703` | `0.882` | `0.536` | `modal_family_not_preserved` |
| `closing_level_based_on_closing_prices` | `source_claim` | `0.711` | `0.444` | `0.308` | - |
| `last_available_wm_fixing_4pm_london_quoted_by_reuters` | `derived_invariant` | `0.721` | `0.733` | `0.733` | `modal_family_not_preserved` |
| `ice_alias` | `source_claim` | `0.766` | `0.429` | `0.6` | - |
| `fallback_price_candidates_are_temporally_comparable` | `bridge` | `0.81` | `0.833` | `0.435` | - |
| `closing_price_converted_with_available_wm_fixing` | `source_claim` | `0.819` | `0.765` | `0.52` | - |
