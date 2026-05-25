# Provenance Back-Translation Metrics: section_4_2

- status: `ok`
- semantic_requested: `False`
- claim_count/source_claim_count: `5` / `5`
- claims_with_warnings/source_claims_with_warnings: `2` / `2`
- mean deterministic score: `0.699`
- mean source-claim deterministic score: `0.699`
- mean source token recall: `0.545`
- mean back-translation token precision: `0.493`
- warning_counts: `{"modal_family_not_preserved": 2, "url_not_preserved": 1}`

## Lowest Deterministic Scores

| claim | origin | score | recall | precision | warnings |
| --- | --- | ---: | ---: | ---: | --- |
| `termination_and_announcement_at_zero_or_below` | `source_claim` | `0.465` | `0.444` | `0.5` | `url_not_preserved`, `modal_family_not_preserved` |
| `solactive_terminate_index_for_other_reason` | `source_claim` | `0.65` | `0.4` | `0.4` | `modal_family_not_preserved` |
| `other_reason_termination_in_accordance_with_solactive_policies` | `source_claim` | `0.712` | `0.5` | `0.273` | - |
| `solactive_policies` | `source_claim` | `0.833` | `0.667` | `0.667` | - |
| `news_section_location` | `source_claim` | `0.834` | `0.714` | `0.625` | - |
