# Diagnostic report — section_4_1

- **gate**: `needs_review`
- fail: 0, warning: 33

## [WARNING] `merge_canonicalization` / `callable_symbol_count`

- value: **40**  (from `parameterization.callable_symbol_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 40
  - `<related section in metrics JSON>` → 40

## [WARNING] `merge_canonicalization` / `callable_symbol_with_args_count`

- value: **40**  (from `parameterization.callable_symbol_with_args_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 40
  - `<related section in metrics JSON>` → 40

## [WARNING] `merge_canonicalization` / `cross_reference_usage_count`

- value: **5**  (from `<search recursive metrics JSON for key `cross_reference_usage_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `evidence.ir_cross_references` → body of calculation_performed_according_to_equity_index_methodology mentions sec; body of section_4_1_index mentions section/annex; body of section_4_1_index_scope mentions section/annex (+2 more)

## [WARNING] `merge_canonicalization` / `dependency_link_count`

- value: **6**  (from `<search recursive metrics JSON for key `dependency_link_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 6
  - `<related section in metrics JSON>` → 6

## [WARNING] `merge_canonicalization` / `draft_variant_count`

- value: **1**  (from `variants.draft_variant_count`)
- meaning: A merge/variant/gold comparison changed structure or semantics; report exact compared variants or merge rows.
- repair: Use overlay/bridge/conflict split or reject rewrite based on backtest.

## [WARNING] `merge_canonicalization` / `factorization_count`

- value: **40**  (from `parameterization.factorization_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 40
  - `<related section in metrics JSON>` → 40

## [WARNING] `merge_canonicalization` / `focus_signature_unique_count`

- value: **1**  (from `variability.focus_signature_unique_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.

## [WARNING] `merge_canonicalization` / `quantifier_parameter_slot_count`

- value: **5**  (from `parameterization.quantifier_parameter_slot_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `assertion_complexity.top_complex_assertions` → soltca50_adjusted_return_index_formula; distributions_reinvested_back_at_opening_of_effective_ex_date
  - `assertion_complexity.max_assertion_depth` → 10
  - `assertion_complexity.total_quantifier_count` → 5

## [WARNING] `merge_canonicalization` / `top_level_parameter_slot_count`

- value: **76**  (from `parameterization.top_level_parameter_slot_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 76
  - `<related section in metrics JSON>` → 76

## [WARNING] `merge_canonicalization` / `total_parameter_slot_mass`

- value: **81**  (from `parameterization.total_parameter_slot_mass`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 81
  - `<related section in metrics JSON>` → 81

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

- value: **22**  (from `identifier_glue.compound_identifier_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'formula_level_change_based_on_price_change', 'raw_piece_count': ; {'identifier': 'formula_level_change_takes_currency_conversion', 'raw_piece_coun; {'identifier': 'distributions_reinvested_back_at_opening_of_effective_ex_date',  (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'formula_applies_to_index', 'raw_piece_count': 4, 'content_piece_; {'identifier': 'IndexPointAmount', 'raw_piece_count': 3, 'content_piece_count': ; {'identifier': 'DocumentLocator', 'raw_piece_count': 2, 'content_piece_count': 2 (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `compound_identifier_count_raw`

- value: **16**  (from `identifier_glue.compound_identifier_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'formula_level_change_based_on_price_change', 'raw_piece_count': ; {'identifier': 'formula_level_change_takes_currency_conversion', 'raw_piece_coun; {'identifier': 'distributions_reinvested_back_at_opening_of_effective_ex_date',  (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'formula_applies_to_index', 'raw_piece_count': 4, 'content_piece_; {'identifier': 'IndexPointAmount', 'raw_piece_count': 3, 'content_piece_count': ; {'identifier': 'DocumentLocator', 'raw_piece_count': 2, 'content_piece_count': 2 (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `cross_reference_usage_count`

- value: **5**  (from `<search recursive metrics JSON for key `cross_reference_usage_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `evidence.ir_cross_references` → body of calculation_performed_according_to_equity_index_methodology mentions sec; body of section_4_1_index mentions section/annex; body of section_4_1_index_scope mentions section/annex (+2 more)

## [WARNING] `ontology_planning` / `dependency_link_count`

- value: **6**  (from `<search recursive metrics JSON for key `dependency_link_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 6
  - `<related section in metrics JSON>` → 6

## [WARNING] `ontology_planning` / `identifier_count`

- value: **76**  (from `identifier_glue.identifier_count`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'formula_level_change_based_on_price_change', 'raw_piece_count': ; {'identifier': 'formula_level_change_takes_currency_conversion', 'raw_piece_coun; {'identifier': 'distributions_reinvested_back_at_opening_of_effective_ex_date',  (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'formula_applies_to_index', 'raw_piece_count': 4, 'content_piece_; {'identifier': 'IndexPointAmount', 'raw_piece_count': 3, 'content_piece_count': ; {'identifier': 'DocumentLocator', 'raw_piece_count': 2, 'content_piece_count': 2 (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `identifier_glue_excess_mass_content`

- value: **42**  (from `identifier_glue.identifier_glue_excess_mass_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'formula_level_change_based_on_price_change', 'raw_piece_count': ; {'identifier': 'formula_level_change_takes_currency_conversion', 'raw_piece_coun; {'identifier': 'distributions_reinvested_back_at_opening_of_effective_ex_date',  (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'formula_applies_to_index', 'raw_piece_count': 4, 'content_piece_; {'identifier': 'IndexPointAmount', 'raw_piece_count': 3, 'content_piece_count': ; {'identifier': 'DocumentLocator', 'raw_piece_count': 2, 'content_piece_count': 2 (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `identifier_glue_excess_mass_raw`

- value: **35**  (from `identifier_glue.identifier_glue_excess_mass_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'formula_level_change_based_on_price_change', 'raw_piece_count': ; {'identifier': 'formula_level_change_takes_currency_conversion', 'raw_piece_coun; {'identifier': 'distributions_reinvested_back_at_opening_of_effective_ex_date',  (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'formula_applies_to_index', 'raw_piece_count': 4, 'content_piece_; {'identifier': 'IndexPointAmount', 'raw_piece_count': 3, 'content_piece_count': ; {'identifier': 'DocumentLocator', 'raw_piece_count': 2, 'content_piece_count': 2 (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `low_source_grounded_glued_identifier_count`

- value: **13**  (from `identifier_glue.low_source_grounded_glued_identifier_count`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'formula_level_change_based_on_price_change', 'raw_piece_count': ; {'identifier': 'formula_level_change_takes_currency_conversion', 'raw_piece_coun; {'identifier': 'distributions_reinvested_back_at_opening_of_effective_ex_date',  (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'formula_applies_to_index', 'raw_piece_count': 4, 'content_piece_; {'identifier': 'IndexPointAmount', 'raw_piece_count': 3, 'content_piece_count': ; {'identifier': 'DocumentLocator', 'raw_piece_count': 2, 'content_piece_count': 2 (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `max_identifier_piece_count_content`

- value: **6**  (from `identifier_glue.max_identifier_piece_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'formula_level_change_based_on_price_change', 'raw_piece_count': ; {'identifier': 'formula_level_change_takes_currency_conversion', 'raw_piece_coun; {'identifier': 'distributions_reinvested_back_at_opening_of_effective_ex_date',  (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'formula_applies_to_index', 'raw_piece_count': 4, 'content_piece_; {'identifier': 'IndexPointAmount', 'raw_piece_count': 3, 'content_piece_count': ; {'identifier': 'DocumentLocator', 'raw_piece_count': 2, 'content_piece_count': 2 (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `max_identifier_piece_count_raw`

- value: **9**  (from `identifier_glue.max_identifier_piece_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'formula_level_change_based_on_price_change', 'raw_piece_count': ; {'identifier': 'formula_level_change_takes_currency_conversion', 'raw_piece_coun; {'identifier': 'distributions_reinvested_back_at_opening_of_effective_ex_date',  (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'formula_applies_to_index', 'raw_piece_count': 4, 'content_piece_; {'identifier': 'IndexPointAmount', 'raw_piece_count': 3, 'content_piece_count': ; {'identifier': 'DocumentLocator', 'raw_piece_count': 2, 'content_piece_count': 2 (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `mean_identifier_piece_count_content`

- value: **2.1447368421052633**  (from `identifier_glue.mean_identifier_piece_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'formula_level_change_based_on_price_change', 'raw_piece_count': ; {'identifier': 'formula_level_change_takes_currency_conversion', 'raw_piece_coun; {'identifier': 'distributions_reinvested_back_at_opening_of_effective_ex_date',  (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'formula_applies_to_index', 'raw_piece_count': 4, 'content_piece_; {'identifier': 'IndexPointAmount', 'raw_piece_count': 3, 'content_piece_count': ; {'identifier': 'DocumentLocator', 'raw_piece_count': 2, 'content_piece_count': 2 (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `mean_identifier_piece_count_raw`

- value: **2.6710526315789473**  (from `identifier_glue.mean_identifier_piece_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'formula_level_change_based_on_price_change', 'raw_piece_count': ; {'identifier': 'formula_level_change_takes_currency_conversion', 'raw_piece_coun; {'identifier': 'distributions_reinvested_back_at_opening_of_effective_ex_date',  (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'formula_applies_to_index', 'raw_piece_count': 4, 'content_piece_; {'identifier': 'IndexPointAmount', 'raw_piece_count': 3, 'content_piece_count': ; {'identifier': 'DocumentLocator', 'raw_piece_count': 2, 'content_piece_count': 2 (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `new_formula_content_token_count_vs_text_only`

- value: **88**  (from `grounding.new_formula_content_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → adjusted_return_formula; adjusted_return_version_decrement_from_ntr; adjustedreturnformula (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; adjusted_return_formula; adjusted_return_version_decrement_from_ntr (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'calculationday', 'current_count': 21, 'baseline_count': 0, 'delta': 2; {'token': 'decrement', 'current_count': 20, 'baseline_count': 3, 'delta': 17}; {'token': 'soltca50', 'current_count': 17, 'baseline_count': 1, 'delta': 16} (+17 more)
  - `grounding.origin_error_count` → 25

## [WARNING] `ontology_planning` / `new_formula_token_count_vs_text_only`

- value: **92**  (from `grounding.new_formula_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → adjusted_return_formula; adjusted_return_version_decrement_from_ntr; adjustedreturnformula (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; adjusted_return_formula; adjusted_return_version_decrement_from_ntr (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'calculationday', 'current_count': 21, 'baseline_count': 0, 'delta': 2; {'token': 'decrement', 'current_count': 20, 'baseline_count': 3, 'delta': 17}; {'token': 'soltca50', 'current_count': 17, 'baseline_count': 1, 'delta': 16} (+17 more)
  - `grounding.origin_error_count` → 25

## [WARNING] `ontology_planning` / `new_full_surface_content_token_count_vs_text_only`

- value: **107**  (from `grounding.new_full_surface_content_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → adjusted_return_formula; adjusted_return_version_decrement_from_ntr; adjustedreturnformula (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; adjusted_return_formula; adjusted_return_version_decrement_from_ntr (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'calculationday', 'current_count': 21, 'baseline_count': 0, 'delta': 2; {'token': 'decrement', 'current_count': 20, 'baseline_count': 3, 'delta': 17}; {'token': 'soltca50', 'current_count': 17, 'baseline_count': 1, 'delta': 16} (+17 more)
  - `grounding.origin_error_count` → 25

## [WARNING] `ontology_planning` / `new_full_surface_token_count_vs_text_only`

- value: **113**  (from `grounding.new_full_surface_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → adjusted_return_formula; adjusted_return_version_decrement_from_ntr; adjustedreturnformula (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; adjusted_return_formula; adjusted_return_version_decrement_from_ntr (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'calculationday', 'current_count': 21, 'baseline_count': 0, 'delta': 2; {'token': 'decrement', 'current_count': 20, 'baseline_count': 3, 'delta': 17}; {'token': 'soltca50', 'current_count': 17, 'baseline_count': 1, 'delta': 16} (+17 more)
  - `grounding.origin_error_count` → 25

## [WARNING] `ontology_planning` / `new_surface_content_token_count`

- value: **210**  (from `<search recursive metrics JSON for key `new_surface_content_token_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → adjusted_return_formula; adjusted_return_version_decrement_from_ntr; adjustedreturnformula (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; adjusted_return_formula; adjusted_return_version_decrement_from_ntr (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'calculationday', 'current_count': 21, 'baseline_count': 0, 'delta': 2; {'token': 'decrement', 'current_count': 20, 'baseline_count': 3, 'delta': 17}; {'token': 'soltca50', 'current_count': 17, 'baseline_count': 1, 'delta': 16} (+17 more)
  - `grounding.origin_error_count` → 25

## [WARNING] `ontology_planning` / `new_surface_token_count`

- value: **210**  (from `<search recursive metrics JSON for key `new_surface_token_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → adjusted_return_formula; adjusted_return_version_decrement_from_ntr; adjustedreturnformula (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; adjusted_return_formula; adjusted_return_version_decrement_from_ntr (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'calculationday', 'current_count': 21, 'baseline_count': 0, 'delta': 2; {'token': 'decrement', 'current_count': 20, 'baseline_count': 3, 'delta': 17}; {'token': 'soltca50', 'current_count': 17, 'baseline_count': 1, 'delta': 16} (+17 more)
  - `grounding.origin_error_count` → 25

## [WARNING] `ontology_planning` / `ungrounded_sort_count`

- value: **16**  (from `grounding.ungrounded_sort_count`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → adjusted_return_formula; adjusted_return_version_decrement_from_ntr; adjustedreturnformula (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; adjusted_return_formula; adjusted_return_version_decrement_from_ntr (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'calculationday', 'current_count': 21, 'baseline_count': 0, 'delta': 2; {'token': 'decrement', 'current_count': 20, 'baseline_count': 3, 'delta': 17}; {'token': 'soltca50', 'current_count': 17, 'baseline_count': 1, 'delta': 16} (+17 more)
  - `grounding.origin_error_count` → 25

## [WARNING] `ontology_planning` / `ungrounded_symbol_count`

- value: **6**  (from `grounding.ungrounded_symbol_count`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → adjusted_return_formula; adjusted_return_version_decrement_from_ntr; adjustedreturnformula (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; adjusted_return_formula; adjusted_return_version_decrement_from_ntr (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'calculationday', 'current_count': 21, 'baseline_count': 0, 'delta': 2; {'token': 'decrement', 'current_count': 20, 'baseline_count': 3, 'delta': 17}; {'token': 'soltca50', 'current_count': 17, 'baseline_count': 1, 'delta': 16} (+17 more)
  - `grounding.origin_error_count` → 25
