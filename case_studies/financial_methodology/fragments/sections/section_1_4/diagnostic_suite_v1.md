# Diagnostic report — section_1_4

- **gate**: `needs_review`
- fail: 0, warning: 31

## [WARNING] `merge_canonicalization` / `callable_symbol_count`

- value: **33**  (from `parameterization.callable_symbol_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 33
  - `<related section in metrics JSON>` → 33

## [WARNING] `merge_canonicalization` / `callable_symbol_with_args_count`

- value: **33**  (from `parameterization.callable_symbol_with_args_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 33
  - `<related section in metrics JSON>` → 33

## [WARNING] `merge_canonicalization` / `dependency_link_count`

- value: **13**  (from `<search recursive metrics JSON for key `dependency_link_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 13
  - `<related section in metrics JSON>` → 13

## [WARNING] `merge_canonicalization` / `draft_variant_count`

- value: **1**  (from `variants.draft_variant_count`)
- meaning: A merge/variant/gold comparison changed structure or semantics; report exact compared variants or merge rows.
- repair: Use overlay/bridge/conflict split or reject rewrite based on backtest.

## [WARNING] `merge_canonicalization` / `factorization_count`

- value: **33**  (from `parameterization.factorization_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 33
  - `<related section in metrics JSON>` → 33

## [WARNING] `merge_canonicalization` / `focus_signature_unique_count`

- value: **1**  (from `variability.focus_signature_unique_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.

## [WARNING] `merge_canonicalization` / `quantifier_parameter_slot_count`

- value: **32**  (from `parameterization.quantifier_parameter_slot_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `assertion_complexity.top_complex_assertions` → closing_price_converted_with_last_available_wm_fixing; closing_price_converted_with_available_wm_fixing; intraday_price_converted_when_not_listed_in_index_currency (+7 more)
  - `assertion_complexity.max_assertion_depth` → 9
  - `assertion_complexity.total_quantifier_count` → 32

## [WARNING] `merge_canonicalization` / `top_level_parameter_slot_count`

- value: **83**  (from `parameterization.top_level_parameter_slot_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 83
  - `<related section in metrics JSON>` → 83

## [WARNING] `merge_canonicalization` / `total_parameter_slot_mass`

- value: **115**  (from `parameterization.total_parameter_slot_mass`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 115
  - `<related section in metrics JSON>` → 115

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

- value: **32**  (from `identifier_glue.compound_identifier_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'intraday_price_converted_when_not_listed_in_index_currency', 'ra; {'identifier': 'closing_price_kept_when_listed_in_index_currency', 'raw_piece_co; {'identifier': 'intraday_price_kept_when_listed_in_index_currency', 'raw_piece_c (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'CalculationMode', 'raw_piece_count': 2, 'content_piece_count': 2; {'identifier': 'Time04_00PMLondon', 'raw_piece_count': 3, 'content_piece_count':; {'identifier': 'Time10_50PMCET', 'raw_piece_count': 3, 'content_piece_count': 2, (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'intraday_price_converted_when_not_listed_in_index_currency', 'ra
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'current_trading_price_used_when_available', 'raw_piece_count': 6

## [WARNING] `ontology_planning` / `compound_identifier_count_raw`

- value: **27**  (from `identifier_glue.compound_identifier_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'intraday_price_converted_when_not_listed_in_index_currency', 'ra; {'identifier': 'closing_price_kept_when_listed_in_index_currency', 'raw_piece_co; {'identifier': 'intraday_price_kept_when_listed_in_index_currency', 'raw_piece_c (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'CalculationMode', 'raw_piece_count': 2, 'content_piece_count': 2; {'identifier': 'Time04_00PMLondon', 'raw_piece_count': 3, 'content_piece_count':; {'identifier': 'Time10_50PMCET', 'raw_piece_count': 3, 'content_piece_count': 2, (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'intraday_price_converted_when_not_listed_in_index_currency', 'ra
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'current_trading_price_used_when_available', 'raw_piece_count': 6

## [WARNING] `ontology_planning` / `dependency_link_count`

- value: **13**  (from `<search recursive metrics JSON for key `dependency_link_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 13
  - `<related section in metrics JSON>` → 13

## [WARNING] `ontology_planning` / `identifier_count`

- value: **76**  (from `identifier_glue.identifier_count`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'intraday_price_converted_when_not_listed_in_index_currency', 'ra; {'identifier': 'closing_price_kept_when_listed_in_index_currency', 'raw_piece_co; {'identifier': 'intraday_price_kept_when_listed_in_index_currency', 'raw_piece_c (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'CalculationMode', 'raw_piece_count': 2, 'content_piece_count': 2; {'identifier': 'Time04_00PMLondon', 'raw_piece_count': 3, 'content_piece_count':; {'identifier': 'Time10_50PMCET', 'raw_piece_count': 3, 'content_piece_count': 2, (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'intraday_price_converted_when_not_listed_in_index_currency', 'ra
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'current_trading_price_used_when_available', 'raw_piece_count': 6

## [WARNING] `ontology_planning` / `identifier_glue_excess_mass_content`

- value: **73**  (from `identifier_glue.identifier_glue_excess_mass_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'intraday_price_converted_when_not_listed_in_index_currency', 'ra; {'identifier': 'closing_price_kept_when_listed_in_index_currency', 'raw_piece_co; {'identifier': 'intraday_price_kept_when_listed_in_index_currency', 'raw_piece_c (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'CalculationMode', 'raw_piece_count': 2, 'content_piece_count': 2; {'identifier': 'Time04_00PMLondon', 'raw_piece_count': 3, 'content_piece_count':; {'identifier': 'Time10_50PMCET', 'raw_piece_count': 3, 'content_piece_count': 2, (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'intraday_price_converted_when_not_listed_in_index_currency', 'ra
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'current_trading_price_used_when_available', 'raw_piece_count': 6

## [WARNING] `ontology_planning` / `identifier_glue_excess_mass_raw`

- value: **65**  (from `identifier_glue.identifier_glue_excess_mass_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'intraday_price_converted_when_not_listed_in_index_currency', 'ra; {'identifier': 'closing_price_kept_when_listed_in_index_currency', 'raw_piece_co; {'identifier': 'intraday_price_kept_when_listed_in_index_currency', 'raw_piece_c (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'CalculationMode', 'raw_piece_count': 2, 'content_piece_count': 2; {'identifier': 'Time04_00PMLondon', 'raw_piece_count': 3, 'content_piece_count':; {'identifier': 'Time10_50PMCET', 'raw_piece_count': 3, 'content_piece_count': 2, (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'intraday_price_converted_when_not_listed_in_index_currency', 'ra
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'current_trading_price_used_when_available', 'raw_piece_count': 6

## [WARNING] `ontology_planning` / `low_source_grounded_glued_identifier_count`

- value: **9**  (from `identifier_glue.low_source_grounded_glued_identifier_count`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'intraday_price_converted_when_not_listed_in_index_currency', 'ra; {'identifier': 'closing_price_kept_when_listed_in_index_currency', 'raw_piece_co; {'identifier': 'intraday_price_kept_when_listed_in_index_currency', 'raw_piece_c (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'CalculationMode', 'raw_piece_count': 2, 'content_piece_count': 2; {'identifier': 'Time04_00PMLondon', 'raw_piece_count': 3, 'content_piece_count':; {'identifier': 'Time10_50PMCET', 'raw_piece_count': 3, 'content_piece_count': 2, (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'intraday_price_converted_when_not_listed_in_index_currency', 'ra
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'current_trading_price_used_when_available', 'raw_piece_count': 6

## [WARNING] `ontology_planning` / `max_identifier_piece_count_content`

- value: **7**  (from `identifier_glue.max_identifier_piece_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'intraday_price_converted_when_not_listed_in_index_currency', 'ra; {'identifier': 'closing_price_kept_when_listed_in_index_currency', 'raw_piece_co; {'identifier': 'intraday_price_kept_when_listed_in_index_currency', 'raw_piece_c (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'CalculationMode', 'raw_piece_count': 2, 'content_piece_count': 2; {'identifier': 'Time04_00PMLondon', 'raw_piece_count': 3, 'content_piece_count':; {'identifier': 'Time10_50PMCET', 'raw_piece_count': 3, 'content_piece_count': 2, (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'intraday_price_converted_when_not_listed_in_index_currency', 'ra
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'current_trading_price_used_when_available', 'raw_piece_count': 6

## [WARNING] `ontology_planning` / `max_identifier_piece_count_raw`

- value: **9**  (from `identifier_glue.max_identifier_piece_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'intraday_price_converted_when_not_listed_in_index_currency', 'ra; {'identifier': 'closing_price_kept_when_listed_in_index_currency', 'raw_piece_co; {'identifier': 'intraday_price_kept_when_listed_in_index_currency', 'raw_piece_c (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'CalculationMode', 'raw_piece_count': 2, 'content_piece_count': 2; {'identifier': 'Time04_00PMLondon', 'raw_piece_count': 3, 'content_piece_count':; {'identifier': 'Time10_50PMCET', 'raw_piece_count': 3, 'content_piece_count': 2, (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'intraday_price_converted_when_not_listed_in_index_currency', 'ra
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'current_trading_price_used_when_available', 'raw_piece_count': 6

## [WARNING] `ontology_planning` / `mean_identifier_piece_count_content`

- value: **2.6578947368421053**  (from `identifier_glue.mean_identifier_piece_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'intraday_price_converted_when_not_listed_in_index_currency', 'ra; {'identifier': 'closing_price_kept_when_listed_in_index_currency', 'raw_piece_co; {'identifier': 'intraday_price_kept_when_listed_in_index_currency', 'raw_piece_c (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'CalculationMode', 'raw_piece_count': 2, 'content_piece_count': 2; {'identifier': 'Time04_00PMLondon', 'raw_piece_count': 3, 'content_piece_count':; {'identifier': 'Time10_50PMCET', 'raw_piece_count': 3, 'content_piece_count': 2, (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'intraday_price_converted_when_not_listed_in_index_currency', 'ra
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'current_trading_price_used_when_available', 'raw_piece_count': 6

## [WARNING] `ontology_planning` / `mean_identifier_piece_count_raw`

- value: **3.210526315789474**  (from `identifier_glue.mean_identifier_piece_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'intraday_price_converted_when_not_listed_in_index_currency', 'ra; {'identifier': 'closing_price_kept_when_listed_in_index_currency', 'raw_piece_co; {'identifier': 'intraday_price_kept_when_listed_in_index_currency', 'raw_piece_c (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'CalculationMode', 'raw_piece_count': 2, 'content_piece_count': 2; {'identifier': 'Time04_00PMLondon', 'raw_piece_count': 3, 'content_piece_count':; {'identifier': 'Time10_50PMCET', 'raw_piece_count': 3, 'content_piece_count': 2, (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'intraday_price_converted_when_not_listed_in_index_currency', 'ra
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'current_trading_price_used_when_available', 'raw_piece_count': 6

## [WARNING] `ontology_planning` / `new_formula_content_token_count_vs_text_only`

- value: **76**  (from `grounding.new_formula_content_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → calculation_mode; calculation_time_from_to; calculationday (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; calculation_mode; calculation_time_from_to (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'price', 'current_count': 71, 'baseline_count': 3, 'delta': 68}; {'token': 'currency', 'current_count': 51, 'baseline_count': 2, 'delta': 49}; {'token': 'calculationday', 'current_count': 37, 'baseline_count': 0, 'delta': 3 (+17 more)
  - `grounding.origin_error_count` → 18

## [WARNING] `ontology_planning` / `new_formula_token_count_vs_text_only`

- value: **84**  (from `grounding.new_formula_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → calculation_mode; calculation_time_from_to; calculationday (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; calculation_mode; calculation_time_from_to (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'price', 'current_count': 71, 'baseline_count': 3, 'delta': 68}; {'token': 'currency', 'current_count': 51, 'baseline_count': 2, 'delta': 49}; {'token': 'calculationday', 'current_count': 37, 'baseline_count': 0, 'delta': 3 (+17 more)
  - `grounding.origin_error_count` → 18

## [WARNING] `ontology_planning` / `new_full_surface_content_token_count_vs_text_only`

- value: **95**  (from `grounding.new_full_surface_content_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → calculation_mode; calculation_time_from_to; calculationday (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; calculation_mode; calculation_time_from_to (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'price', 'current_count': 71, 'baseline_count': 3, 'delta': 68}; {'token': 'currency', 'current_count': 51, 'baseline_count': 2, 'delta': 49}; {'token': 'calculationday', 'current_count': 37, 'baseline_count': 0, 'delta': 3 (+17 more)
  - `grounding.origin_error_count` → 18

## [WARNING] `ontology_planning` / `new_full_surface_token_count_vs_text_only`

- value: **105**  (from `grounding.new_full_surface_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → calculation_mode; calculation_time_from_to; calculationday (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; calculation_mode; calculation_time_from_to (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'price', 'current_count': 71, 'baseline_count': 3, 'delta': 68}; {'token': 'currency', 'current_count': 51, 'baseline_count': 2, 'delta': 49}; {'token': 'calculationday', 'current_count': 37, 'baseline_count': 0, 'delta': 3 (+17 more)
  - `grounding.origin_error_count` → 18

## [WARNING] `ontology_planning` / `new_surface_content_token_count`

- value: **231**  (from `<search recursive metrics JSON for key `new_surface_content_token_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → calculation_mode; calculation_time_from_to; calculationday (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; calculation_mode; calculation_time_from_to (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'price', 'current_count': 71, 'baseline_count': 3, 'delta': 68}; {'token': 'currency', 'current_count': 51, 'baseline_count': 2, 'delta': 49}; {'token': 'calculationday', 'current_count': 37, 'baseline_count': 0, 'delta': 3 (+17 more)
  - `grounding.origin_error_count` → 18

## [WARNING] `ontology_planning` / `new_surface_token_count`

- value: **231**  (from `<search recursive metrics JSON for key `new_surface_token_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → calculation_mode; calculation_time_from_to; calculationday (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; calculation_mode; calculation_time_from_to (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'price', 'current_count': 71, 'baseline_count': 3, 'delta': 68}; {'token': 'currency', 'current_count': 51, 'baseline_count': 2, 'delta': 49}; {'token': 'calculationday', 'current_count': 37, 'baseline_count': 0, 'delta': 3 (+17 more)
  - `grounding.origin_error_count` → 18

## [WARNING] `ontology_planning` / `ungrounded_sort_count`

- value: **8**  (from `grounding.ungrounded_sort_count`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → calculation_mode; calculation_time_from_to; calculationday (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; calculation_mode; calculation_time_from_to (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'price', 'current_count': 71, 'baseline_count': 3, 'delta': 68}; {'token': 'currency', 'current_count': 51, 'baseline_count': 2, 'delta': 49}; {'token': 'calculationday', 'current_count': 37, 'baseline_count': 0, 'delta': 3 (+17 more)
  - `grounding.origin_error_count` → 18

## [WARNING] `ontology_planning` / `ungrounded_symbol_count`

- value: **7**  (from `grounding.ungrounded_symbol_count`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → calculation_mode; calculation_time_from_to; calculationday (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; calculation_mode; calculation_time_from_to (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'price', 'current_count': 71, 'baseline_count': 3, 'delta': 68}; {'token': 'currency', 'current_count': 51, 'baseline_count': 2, 'delta': 49}; {'token': 'calculationday', 'current_count': 37, 'baseline_count': 0, 'delta': 3 (+17 more)
  - `grounding.origin_error_count` → 18
