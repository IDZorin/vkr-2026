# Provenance Back-Translation Metrics: section_5_5

- status: `ok`
- semantic_requested: `False`
- claim_count/source_claim_count: `9` / `9`
- claims_with_warnings/source_claims_with_warnings: `1` / `1`
- mean deterministic score: `0.812`
- mean source-claim deterministic score: `0.812`
- mean source token recall: `0.682`
- mean back-translation token precision: `0.548`
- warning_counts: `{"low_back_translation_token_precision": 1, "low_source_token_recall": 1}`

## Lowest Deterministic Scores

| claim | origin | score | recall | precision | warnings |
| --- | --- | ---: | ---: | ---: | --- |
| `index_rule_amendment_scope` | `source_claim` | `0.661` | `0.333` | `0.167` | `low_source_token_recall`, `low_back_translation_token_precision` |
| `oversight_committee_responsible_for_index_rule_amendment_decisions` | `source_claim` | `0.754` | `0.571` | `0.4` | - |
| `index_rule_amendments_may_result_in_guideline_amendment` | `source_claim` | `0.763` | `0.667` | `0.364` | - |
| `make_index_rule_amendment_in_compliance_with_methodology_policy` | `source_claim` | `0.8` | `0.625` | `0.556` | - |
| `oversight_committee_prior_approval` | `source_claim` | `0.812` | `0.667` | `0.571` | - |
| `oversight_committee_staff_from_solactive_or_subsidiary` | `source_claim` | `0.827` | `0.833` | `0.5` | - |
| `oversight_committee_has_staff` | `source_claim` | `0.863` | `0.667` | `0.8` | - |
| `submit_index_rule_amendment_for_prior_approval` | `source_claim` | `0.866` | `0.778` | `0.7` | - |
| `methodology_policy_location` | `source_claim` | `0.964` | `1.0` | `0.875` | - |
