# Provenance Back-Translation Metrics: section_1_2

- status: `ok`
- semantic_requested: `False`
- claim_count/source_claim_count: `16` / `15`
- claims_with_warnings/source_claims_with_warnings: `3` / `2`
- mean deterministic score: `0.823`
- mean source-claim deterministic score: `0.832`
- mean source token recall: `0.848`
- mean back-translation token precision: `0.542`
- warning_counts: `{"low_back_translation_token_precision": 1, "modal_family_not_preserved": 1, "url_not_preserved": 1}`

## Lowest Deterministic Scores

| claim | origin | score | recall | precision | warnings |
| --- | --- | ---: | ---: | ---: | --- |
| `vendor_decides_distribution_or_display` | `source_claim` | `0.554` | `0.385` | `0.294` | `modal_family_not_preserved` |
| `section_4_location` | `plumbing` | `0.687` | `0.5` | `0.167` | `low_back_translation_token_precision` |
| `index_publications_available_at_announcements_website` | `source_claim` | `0.703` | `0.643` | `0.75` | `url_not_preserved` |
| `index_tr_identifiers` | `source_claim` | `0.793` | `0.9` | `0.333` | - |
| `solactive_website` | `source_claim` | `0.804` | `0.6` | `0.6` | - |
| `index_distribution_to_affiliated_vendors` | `source_claim` | `0.806` | `0.8` | `0.444` | - |
| `bbg_ticker_at_most_one` | `source_claim` | `0.809` | `1.0` | `0.333` | - |
| `index_pr_identifiers` | `source_claim` | `0.813` | `1.0` | `0.346` | - |
| `index_ntr_identifiers` | `source_claim` | `0.817` | `1.0` | `0.36` | - |
| `index_5_percent_ar_identifiers` | `source_claim` | `0.82` | `1.0` | `0.37` | - |
| `index_50_ar_identifiers` | `source_claim` | `0.873` | `0.895` | `0.63` | - |
| `listed_indices_publication_channels` | `source_claim` | `0.876` | `1.0` | `0.565` | - |
