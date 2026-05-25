# Provenance Back-Translation Metrics: N14

- status: `ok`
- semantic_requested: `False`
- claim_count/source_claim_count: `3` / `3`
- claims_with_warnings/source_claims_with_warnings: `1` / `1`
- mean deterministic score: `0.89`
- mean source-claim deterministic score: `0.89`
- mean source token recall: `0.952`
- mean back-translation token precision: `0.831`
- warning_counts: `{"url_not_preserved": 1}`

## Lowest Deterministic Scores

| claim | origin | score | recall | precision | warnings |
| --- | --- | ---: | ---: | ---: | --- |
| `gbs_index_universe_definition` | `source_claim` | `0.816` | `0.857` | `1.0` | `url_not_preserved` |
| `gbs_index_specified_in_section_2_1` | `source_claim` | `0.918` | `1.0` | `0.714` | - |
| `solactive_gbs_benchmark_series_guideline_url` | `source_claim` | `0.937` | `1.0` | `0.778` | - |
