# Diagnostic report — section_4_7

- **gate**: `needs_review`
- fail: 0, warning: 35

## [WARNING] `merge_canonicalization` / `callable_symbol_count`

- value: **21**  (from `parameterization.callable_symbol_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 21
  - `<related section in metrics JSON>` → 21

## [WARNING] `merge_canonicalization` / `callable_symbol_with_args_count`

- value: **21**  (from `parameterization.callable_symbol_with_args_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 21
  - `<related section in metrics JSON>` → 21

## [WARNING] `merge_canonicalization` / `cross_reference_dropout_count`

- value: **1**  (from `<search recursive metrics JSON for key `cross_reference_dropout_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `evidence.source_cross_references` → Section 4.7
  - `evidence.ir_cross_references` → entity ThisGuideline : Document

## [WARNING] `merge_canonicalization` / `cross_reference_usage_count`

- value: **1**  (from `<search recursive metrics JSON for key `cross_reference_usage_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `evidence.ir_cross_references` → entity ThisGuideline : Document

## [WARNING] `merge_canonicalization` / `dependency_link_count`

- value: **4**  (from `<search recursive metrics JSON for key `dependency_link_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 4
  - `<related section in metrics JSON>` → 4

## [WARNING] `merge_canonicalization` / `draft_variant_count`

- value: **1**  (from `variants.draft_variant_count`)
- meaning: A merge/variant/gold comparison changed structure or semantics; report exact compared variants or merge rows.
- repair: Use overlay/bridge/conflict split or reject rewrite based on backtest.

## [WARNING] `merge_canonicalization` / `factorization_count`

- value: **21**  (from `parameterization.factorization_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 21
  - `<related section in metrics JSON>` → 21

## [WARNING] `merge_canonicalization` / `focus_signature_unique_count`

- value: **1**  (from `variability.focus_signature_unique_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.

## [WARNING] `merge_canonicalization` / `quantifier_parameter_slot_count`

- value: **14**  (from `parameterization.quantifier_parameter_slot_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `assertion_complexity.top_complex_assertions` → index_determination_may_be_limited_or_impaired; market_stress_generally_results_in_price_conditions; calculation_during_market_stress_follows_arrangements (+1 more)
  - `assertion_complexity.max_assertion_depth` → 9
  - `assertion_complexity.total_quantifier_count` → 14

## [WARNING] `merge_canonicalization` / `top_level_parameter_slot_count`

- value: **42**  (from `parameterization.top_level_parameter_slot_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 42
  - `<related section in metrics JSON>` → 42

## [WARNING] `merge_canonicalization` / `total_parameter_slot_mass`

- value: **56**  (from `parameterization.total_parameter_slot_mass`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 56
  - `<related section in metrics JSON>` → 56

## [WARNING] `merge_canonicalization` / `unique_ir_variant_count`

- value: **1**  (from `variants.unique_ir_variant_count`)
- meaning: A merge/variant/gold comparison changed structure or semantics; report exact compared variants or merge rows.
- repair: Use overlay/bridge/conflict split or reject rewrite based on backtest.

## [WARNING] `merge_canonicalization` / `unique_variant_signature_count`

- value: **1**  (from `variability.unique_variant_signature_count`)
- meaning: A merge/variant/gold comparison changed structure or semantics; report exact compared variants or merge rows.
- repair: Use overlay/bridge/conflict split or reject rewrite based on backtest.

## [WARNING] `merge_canonicalization` / `usable_variant_count`

- value: **1**  (from `variability.usable_variant_count`)
- meaning: A merge/variant/gold comparison changed structure or semantics; report exact compared variants or merge rows.
- repair: Use overlay/bridge/conflict split or reject rewrite based on backtest.

## [WARNING] `ontology_planning` / `compound_identifier_count_content`

- value: **23**  (from `identifier_glue.compound_identifier_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'market_stress_can_arise_due_to_variety_of_reasons', 'raw_piece_c; {'identifier': 'market_stress_generally_results_in_price_conditions', 'raw_piece; {'identifier': 'calculation_during_market_stress_follows_arrangements', 'raw_pie (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'period_of_market_disruption', 'raw_piece_count': 4, 'content_pie; {'identifier': 'price_outcome_component', 'raw_piece_count': 3, 'content_piece_c; {'identifier': 'price_outcome_component_scope', 'raw_piece_count': 4, 'content_p (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'calculates_index_following_arrangement', 'raw_piece_count': 4, '; {'identifier': 'index_determination_may_be_limited_or_impaired', 'raw_piece_coun

## [WARNING] `ontology_planning` / `compound_identifier_count_raw`

- value: **19**  (from `identifier_glue.compound_identifier_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'market_stress_can_arise_due_to_variety_of_reasons', 'raw_piece_c; {'identifier': 'market_stress_generally_results_in_price_conditions', 'raw_piece; {'identifier': 'calculation_during_market_stress_follows_arrangements', 'raw_pie (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'period_of_market_disruption', 'raw_piece_count': 4, 'content_pie; {'identifier': 'price_outcome_component', 'raw_piece_count': 3, 'content_piece_c; {'identifier': 'price_outcome_component_scope', 'raw_piece_count': 4, 'content_p (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'calculates_index_following_arrangement', 'raw_piece_count': 4, '; {'identifier': 'index_determination_may_be_limited_or_impaired', 'raw_piece_coun

## [WARNING] `ontology_planning` / `cross_reference_dropout_count`

- value: **1**  (from `<search recursive metrics JSON for key `cross_reference_dropout_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `evidence.source_cross_references` → Section 4.7
  - `evidence.ir_cross_references` → entity ThisGuideline : Document

## [WARNING] `ontology_planning` / `cross_reference_usage_count`

- value: **1**  (from `<search recursive metrics JSON for key `cross_reference_usage_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `evidence.ir_cross_references` → entity ThisGuideline : Document

## [WARNING] `ontology_planning` / `dependency_link_count`

- value: **4**  (from `<search recursive metrics JSON for key `dependency_link_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 4
  - `<related section in metrics JSON>` → 4

## [WARNING] `ontology_planning` / `identifier_count`

- value: **64**  (from `identifier_glue.identifier_count`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'market_stress_can_arise_due_to_variety_of_reasons', 'raw_piece_c; {'identifier': 'market_stress_generally_results_in_price_conditions', 'raw_piece; {'identifier': 'calculation_during_market_stress_follows_arrangements', 'raw_pie (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'period_of_market_disruption', 'raw_piece_count': 4, 'content_pie; {'identifier': 'price_outcome_component', 'raw_piece_count': 3, 'content_piece_c; {'identifier': 'price_outcome_component_scope', 'raw_piece_count': 4, 'content_p (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'calculates_index_following_arrangement', 'raw_piece_count': 4, '; {'identifier': 'index_determination_may_be_limited_or_impaired', 'raw_piece_coun

## [WARNING] `ontology_planning` / `identifier_glue_excess_mass_content`

- value: **40**  (from `identifier_glue.identifier_glue_excess_mass_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'market_stress_can_arise_due_to_variety_of_reasons', 'raw_piece_c; {'identifier': 'market_stress_generally_results_in_price_conditions', 'raw_piece; {'identifier': 'calculation_during_market_stress_follows_arrangements', 'raw_pie (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'period_of_market_disruption', 'raw_piece_count': 4, 'content_pie; {'identifier': 'price_outcome_component', 'raw_piece_count': 3, 'content_piece_c; {'identifier': 'price_outcome_component_scope', 'raw_piece_count': 4, 'content_p (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'calculates_index_following_arrangement', 'raw_piece_count': 4, '; {'identifier': 'index_determination_may_be_limited_or_impaired', 'raw_piece_coun

## [WARNING] `ontology_planning` / `identifier_glue_excess_mass_raw`

- value: **37**  (from `identifier_glue.identifier_glue_excess_mass_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'market_stress_can_arise_due_to_variety_of_reasons', 'raw_piece_c; {'identifier': 'market_stress_generally_results_in_price_conditions', 'raw_piece; {'identifier': 'calculation_during_market_stress_follows_arrangements', 'raw_pie (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'period_of_market_disruption', 'raw_piece_count': 4, 'content_pie; {'identifier': 'price_outcome_component', 'raw_piece_count': 3, 'content_piece_c; {'identifier': 'price_outcome_component_scope', 'raw_piece_count': 4, 'content_p (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'calculates_index_following_arrangement', 'raw_piece_count': 4, '; {'identifier': 'index_determination_may_be_limited_or_impaired', 'raw_piece_coun

## [WARNING] `ontology_planning` / `low_source_grounded_glued_identifier_count`

- value: **18**  (from `identifier_glue.low_source_grounded_glued_identifier_count`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'market_stress_can_arise_due_to_variety_of_reasons', 'raw_piece_c; {'identifier': 'market_stress_generally_results_in_price_conditions', 'raw_piece; {'identifier': 'calculation_during_market_stress_follows_arrangements', 'raw_pie (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'period_of_market_disruption', 'raw_piece_count': 4, 'content_pie; {'identifier': 'price_outcome_component', 'raw_piece_count': 3, 'content_piece_c; {'identifier': 'price_outcome_component_scope', 'raw_piece_count': 4, 'content_p (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'calculates_index_following_arrangement', 'raw_piece_count': 4, '; {'identifier': 'index_determination_may_be_limited_or_impaired', 'raw_piece_coun

## [WARNING] `ontology_planning` / `max_identifier_piece_count_content`

- value: **7**  (from `identifier_glue.max_identifier_piece_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'market_stress_can_arise_due_to_variety_of_reasons', 'raw_piece_c; {'identifier': 'market_stress_generally_results_in_price_conditions', 'raw_piece; {'identifier': 'calculation_during_market_stress_follows_arrangements', 'raw_pie (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'period_of_market_disruption', 'raw_piece_count': 4, 'content_pie; {'identifier': 'price_outcome_component', 'raw_piece_count': 3, 'content_piece_c; {'identifier': 'price_outcome_component_scope', 'raw_piece_count': 4, 'content_p (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'calculates_index_following_arrangement', 'raw_piece_count': 4, '; {'identifier': 'index_determination_may_be_limited_or_impaired', 'raw_piece_coun

## [WARNING] `ontology_planning` / `max_identifier_piece_count_raw`

- value: **9**  (from `identifier_glue.max_identifier_piece_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'market_stress_can_arise_due_to_variety_of_reasons', 'raw_piece_c; {'identifier': 'market_stress_generally_results_in_price_conditions', 'raw_piece; {'identifier': 'calculation_during_market_stress_follows_arrangements', 'raw_pie (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'period_of_market_disruption', 'raw_piece_count': 4, 'content_pie; {'identifier': 'price_outcome_component', 'raw_piece_count': 3, 'content_piece_c; {'identifier': 'price_outcome_component_scope', 'raw_piece_count': 4, 'content_p (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'calculates_index_following_arrangement', 'raw_piece_count': 4, '; {'identifier': 'index_determination_may_be_limited_or_impaired', 'raw_piece_coun

## [WARNING] `ontology_planning` / `mean_identifier_piece_count_content`

- value: **2.09375**  (from `identifier_glue.mean_identifier_piece_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'market_stress_can_arise_due_to_variety_of_reasons', 'raw_piece_c; {'identifier': 'market_stress_generally_results_in_price_conditions', 'raw_piece; {'identifier': 'calculation_during_market_stress_follows_arrangements', 'raw_pie (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'period_of_market_disruption', 'raw_piece_count': 4, 'content_pie; {'identifier': 'price_outcome_component', 'raw_piece_count': 3, 'content_piece_c; {'identifier': 'price_outcome_component_scope', 'raw_piece_count': 4, 'content_p (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'calculates_index_following_arrangement', 'raw_piece_count': 4, '; {'identifier': 'index_determination_may_be_limited_or_impaired', 'raw_piece_coun

## [WARNING] `ontology_planning` / `mean_identifier_piece_count_raw`

- value: **2.65625**  (from `identifier_glue.mean_identifier_piece_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'market_stress_can_arise_due_to_variety_of_reasons', 'raw_piece_c; {'identifier': 'market_stress_generally_results_in_price_conditions', 'raw_piece; {'identifier': 'calculation_during_market_stress_follows_arrangements', 'raw_pie (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'period_of_market_disruption', 'raw_piece_count': 4, 'content_pie; {'identifier': 'price_outcome_component', 'raw_piece_count': 3, 'content_piece_c; {'identifier': 'price_outcome_component_scope', 'raw_piece_count': 4, 'content_p (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'calculates_index_following_arrangement', 'raw_piece_count': 4, '; {'identifier': 'index_determination_may_be_limited_or_impaired', 'raw_piece_coun

## [WARNING] `ontology_planning` / `new_formula_content_token_count_vs_text_only`

- value: **52**  (from `grounding.new_formula_content_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → arrangement; attimesofmarketdisruption; available_on (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; arrangement; attimesofmarketdisruption (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'period', 'current_count': 18, 'baseline_count': 0, 'delta': 18}; {'token': 'index', 'current_count': 18, 'baseline_count': 2, 'delta': 16}; {'token': 'possibility', 'current_count': 14, 'baseline_count': 0, 'delta': 14} (+17 more)
  - `grounding.origin_error_count` → 36

## [WARNING] `ontology_planning` / `new_formula_token_count_vs_text_only`

- value: **59**  (from `grounding.new_formula_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → arrangement; attimesofmarketdisruption; available_on (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; arrangement; attimesofmarketdisruption (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'period', 'current_count': 18, 'baseline_count': 0, 'delta': 18}; {'token': 'index', 'current_count': 18, 'baseline_count': 2, 'delta': 16}; {'token': 'possibility', 'current_count': 14, 'baseline_count': 0, 'delta': 14} (+17 more)
  - `grounding.origin_error_count` → 36

## [WARNING] `ontology_planning` / `new_full_surface_content_token_count_vs_text_only`

- value: **71**  (from `grounding.new_full_surface_content_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → arrangement; attimesofmarketdisruption; available_on (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; arrangement; attimesofmarketdisruption (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'period', 'current_count': 18, 'baseline_count': 0, 'delta': 18}; {'token': 'index', 'current_count': 18, 'baseline_count': 2, 'delta': 16}; {'token': 'possibility', 'current_count': 14, 'baseline_count': 0, 'delta': 14} (+17 more)
  - `grounding.origin_error_count` → 36

## [WARNING] `ontology_planning` / `new_full_surface_token_count_vs_text_only`

- value: **81**  (from `grounding.new_full_surface_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → arrangement; attimesofmarketdisruption; available_on (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; arrangement; attimesofmarketdisruption (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'period', 'current_count': 18, 'baseline_count': 0, 'delta': 18}; {'token': 'index', 'current_count': 18, 'baseline_count': 2, 'delta': 16}; {'token': 'possibility', 'current_count': 14, 'baseline_count': 0, 'delta': 14} (+17 more)
  - `grounding.origin_error_count` → 36

## [WARNING] `ontology_planning` / `new_surface_content_token_count`

- value: **133**  (from `<search recursive metrics JSON for key `new_surface_content_token_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → arrangement; attimesofmarketdisruption; available_on (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; arrangement; attimesofmarketdisruption (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'period', 'current_count': 18, 'baseline_count': 0, 'delta': 18}; {'token': 'index', 'current_count': 18, 'baseline_count': 2, 'delta': 16}; {'token': 'possibility', 'current_count': 14, 'baseline_count': 0, 'delta': 14} (+17 more)
  - `grounding.origin_error_count` → 36

## [WARNING] `ontology_planning` / `new_surface_token_count`

- value: **133**  (from `<search recursive metrics JSON for key `new_surface_token_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → arrangement; attimesofmarketdisruption; available_on (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; arrangement; attimesofmarketdisruption (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'period', 'current_count': 18, 'baseline_count': 0, 'delta': 18}; {'token': 'index', 'current_count': 18, 'baseline_count': 2, 'delta': 16}; {'token': 'possibility', 'current_count': 14, 'baseline_count': 0, 'delta': 14} (+17 more)
  - `grounding.origin_error_count` → 36

## [WARNING] `ontology_planning` / `ungrounded_sort_count`

- value: **25**  (from `grounding.ungrounded_sort_count`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → arrangement; attimesofmarketdisruption; available_on (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; arrangement; attimesofmarketdisruption (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'period', 'current_count': 18, 'baseline_count': 0, 'delta': 18}; {'token': 'index', 'current_count': 18, 'baseline_count': 2, 'delta': 16}; {'token': 'possibility', 'current_count': 14, 'baseline_count': 0, 'delta': 14} (+17 more)
  - `grounding.origin_error_count` → 36

## [WARNING] `ontology_planning` / `ungrounded_symbol_count`

- value: **10**  (from `grounding.ungrounded_symbol_count`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → arrangement; attimesofmarketdisruption; available_on (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; arrangement; attimesofmarketdisruption (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'period', 'current_count': 18, 'baseline_count': 0, 'delta': 18}; {'token': 'index', 'current_count': 18, 'baseline_count': 2, 'delta': 16}; {'token': 'possibility', 'current_count': 14, 'baseline_count': 0, 'delta': 14} (+17 more)
  - `grounding.origin_error_count` → 36
