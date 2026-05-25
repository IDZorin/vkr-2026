# Provenance Back-Translation Metrics: section_5_2

- status: `ok`
- semantic_requested: `False`
- claim_count/source_claim_count: `12` / `11`
- claims_with_warnings/source_claims_with_warnings: `3` / `3`
- mean deterministic score: `0.844`
- mean source-claim deterministic score: `0.852`
- mean source token recall: `0.721`
- mean back-translation token precision: `0.762`
- warning_counts: `{"low_source_token_recall": 2, "modal_family_not_preserved": 1, "negation_not_preserved": 1}`

## Lowest Deterministic Scores

| claim | origin | score | recall | precision | warnings |
| --- | --- | ---: | ---: | ---: | --- |
| `methodology_change_need_example_condition_scope` | `source_claim` | `0.551` | `0.161` | `0.556` | `low_source_token_recall`, `negation_not_preserved` |
| `identified_need_has_review_identified_change` | `source_claim` | `0.668` | `0.538` | `0.7` | `modal_family_not_preserved` |
| `no_longer_reflects_reality_condition_means_not_reflects_reality_as_before` | `bridge` | `0.754` | `0.625` | `0.357` | - |
| `index_methodology_scope` | `source_claim` | `0.796` | `0.286` | `1.0` | `low_source_token_recall` |
| `announcement_section_location` | `source_claim` | `0.839` | `0.8` | `0.571` | - |
| `methodology_change_need_example_condition_catalog` | `source_claim` | `0.858` | `0.75` | `0.692` | - |
| `make_methodology_change_in_accordance_with_policy` | `source_claim` | `0.908` | `0.875` | `0.778` | - |
| `methodology_reviews_are_regular_at_least_annually` | `source_claim` | `0.923` | `0.857` | `0.857` | - |
| `announce_methodology_change_on_solactive_website` | `source_claim` | `0.924` | `0.9` | `0.818` | - |
| `methodology_policy_location` | `source_claim` | `0.948` | `1.0` | `0.818` | - |
| `methodology_subject_to_regular_review_at_least_annually` | `source_claim` | `0.959` | `0.857` | `1.0` | - |
| `last_amendment_date_contained_in_guideline` | `source_claim` | `1.0` | `1.0` | `1.0` | - |
