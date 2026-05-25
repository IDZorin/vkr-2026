# Provenance Back-Translation Metrics: section_4_6

- status: `ok`
- semantic_requested: `False`
- claim_count/source_claim_count: `7` / `7`
- claims_with_warnings/source_claims_with_warnings: `3` / `3`
- mean deterministic score: `0.711`
- mean source-claim deterministic score: `0.711`
- mean source token recall: `0.583`
- mean back-translation token precision: `0.454`
- warning_counts: `{"low_back_translation_token_precision": 1, "low_source_token_recall": 2, "modal_family_not_preserved": 2, "negation_not_preserved": 1}`

## Lowest Deterministic Scores

| claim | origin | score | recall | precision | warnings |
| --- | --- | ---: | ---: | ---: | --- |
| `solactive_greatest_possible_efforts` | `source_claim` | `0.525` | `0.2` | `0.333` | `low_source_token_recall`, `modal_family_not_preserved` |
| `determination_process_errors_may_occur_not_ruled_out` | `source_claim` | `0.54` | `0.714` | `0.588` | `modal_family_not_preserved`, `negation_not_preserved` |
| `efforts_to_accurately_calculate_and_maintain_indices` | `source_claim` | `0.571` | `0.0` | `0.0` | `low_source_token_recall`, `low_back_translation_token_precision` |
| `correction_policy_specifies_period_understanding_and_measures` | `source_claim` | `0.753` | `0.75` | `0.273` | - |
| `identified_errors_correction_endeavor` | `source_claim` | `0.774` | `0.6` | `0.462` | - |
| `correction_policy_reference` | `source_claim` | `0.893` | `1.0` | `0.625` | - |
| `period_understanding_and_measures_depend_on_underlying` | `source_claim` | `0.924` | `0.818` | `0.9` | - |
