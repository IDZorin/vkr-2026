# Provenance Back-Translation Metrics: section_1_5

- status: `ok`
- semantic_requested: `False`
- claim_count/source_claim_count: `3` / `2`
- claims_with_warnings/source_claims_with_warnings: `2` / `2`
- mean deterministic score: `0.73`
- mean source-claim deterministic score: `0.659`
- mean source token recall: `0.715`
- mean back-translation token precision: `0.461`
- warning_counts: `{"low_back_translation_token_precision": 1, "low_source_token_recall": 1, "modal_family_not_preserved": 2}`

## Lowest Deterministic Scores

| claim | origin | score | recall | precision | warnings |
| --- | --- | ---: | ---: | ---: | --- |
| `issue_index_underlying_value_license` | `source_claim` | `0.55` | `0.25` | `0.053` | `low_source_token_recall`, `low_back_translation_token_precision`, `modal_family_not_preserved` |
| `index_underlying_value_license_class_scope` | `source_claim` | `0.768` | `0.895` | `0.773` | `modal_family_not_preserved` |
| `index_underlying_value_license_instance_class` | `bridge` | `0.873` | `1.0` | `0.556` | - |
