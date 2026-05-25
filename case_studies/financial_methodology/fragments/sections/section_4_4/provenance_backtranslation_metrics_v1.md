# Provenance Back-Translation Metrics: section_4_4

- status: `ok`
- semantic_requested: `False`
- claim_count/source_claim_count: `13` / `12`
- claims_with_warnings/source_claims_with_warnings: `2` / `2`
- mean deterministic score: `0.861`
- mean source-claim deterministic score: `0.875`
- mean source token recall: `0.807`
- mean back-translation token precision: `0.686`
- warning_counts: `{"low_source_token_recall": 1, "modal_family_not_preserved": 1}`

## Lowest Deterministic Scores

| claim | origin | score | recall | precision | warnings |
| --- | --- | ---: | ---: | ---: | --- |
| `rebalance_interval_order` | `bridge` | `0.69` | `0.4` | `0.25` | - |
| `make_required_index_adjustment` | `source_claim` | `0.719` | `0.3` | `0.5` | `low_source_token_recall` |
| `index_adjustment_implemented_on_notice_effective_day` | `source_claim` | `0.765` | `0.778` | `0.875` | `modal_family_not_preserved` |
| `component_weighting_effect_qualified_by_certain_components` | `source_claim` | `0.811` | `0.75` | `0.5` | - |
| `required_adjustment_effect_scope` | `source_claim` | `0.823` | `0.643` | `0.643` | - |
| `notice_period_at_least_two_trading_days` | `source_claim` | `0.85` | `0.818` | `0.6` | - |
| `index_adjustment_notice_publication` | `source_claim` | `0.873` | `1.0` | `0.556` | - |
| `corporate_action_creates_required_index_adjustment` | `source_claim` | `0.889` | `1.0` | `0.611` | - |
| `announce_index_adjustment` | `source_claim` | `0.893` | `1.0` | `0.625` | - |
| `announcements_section_on_solactive_website` | `source_claim` | `0.943` | `0.8` | `1.0` | - |
| `make_index_adjustment_in_compliance_with_equity_index_methodology` | `source_claim` | `0.964` | `1.0` | `0.875` | - |
| `equity_index_methodology_reference` | `source_claim` | `0.968` | `1.0` | `0.889` | - |
