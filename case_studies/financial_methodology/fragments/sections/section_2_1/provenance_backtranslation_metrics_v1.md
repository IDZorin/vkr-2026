# Provenance Back-Translation Metrics: section_2_1

- status: `ok`
- semantic_requested: `False`
- claim_count/source_claim_count: `24` / `16`
- claims_with_warnings/source_claims_with_warnings: `12` / `7`
- mean deterministic score: `0.756`
- mean source-claim deterministic score: `0.788`
- mean source token recall: `0.684`
- mean back-translation token precision: `0.534`
- warning_counts: `{"low_back_translation_token_precision": 4, "low_source_token_recall": 5, "modal_family_not_preserved": 3, "number_not_preserved": 5, "url_not_preserved": 2}`

## Lowest Deterministic Scores

| claim | origin | score | recall | precision | warnings |
| --- | --- | ---: | ---: | ---: | --- |
| `gbs_index_universe_framework_document_part_url` | `plumbing` | `0.429` | `0.0` | `0.0` | `low_source_token_recall`, `low_back_translation_token_precision`, `url_not_preserved` |
| `gbs_index_universe_framework_document_part` | `plumbing` | `0.612` | `0.667` | `0.333` | `url_not_preserved` |
| `share_class_satisfies_buffer_rule_definition` | `bridge` | `0.614` | `0.167` | `0.077` | `low_source_token_recall`, `low_back_translation_token_precision` |
| `minimum_average_daily_value_traded_over_declared_lookback_windows` | `source_claim` | `0.628` | `0.737` | `0.538` | `number_not_preserved`, `modal_family_not_preserved` |
| `current_company_buffer_rule` | `source_claim` | `0.629` | `0.714` | `0.769` | `number_not_preserved`, `modal_family_not_preserved` |
| `index_universe_bridge` | `bridge` | `0.645` | `0.222` | `0.182` | `low_source_token_recall`, `low_back_translation_token_precision` |
| `highest_minimum_average_daily_value_traded_predicate` | `bridge` | `0.671` | `0.333` | `0.214` | `low_source_token_recall`, `low_back_translation_token_precision` |
| `lookback_month_count_values` | `source_claim` | `0.703` | `0.333` | `0.375` | `low_source_token_recall` |
| `highest_minimum_average_daily_value_traded_definition` | `source_claim` | `0.708` | `0.65` | `0.765` | `number_not_preserved` |
| `not_current_company_buffer_rule` | `source_claim` | `0.716` | `0.708` | `0.739` | `number_not_preserved` |
| `eligible_for_index_universe_requirements` | `source_claim` | `0.73` | `0.683` | `0.827` | `modal_family_not_preserved` |
| `highest_minimum_average_daily_value_traded_share_class_company` | `source_claim` | `0.73` | `0.611` | `0.917` | `number_not_preserved` |
