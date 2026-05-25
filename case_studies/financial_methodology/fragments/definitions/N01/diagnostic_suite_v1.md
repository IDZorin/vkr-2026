# Diagnostic report — N01

- **gate**: `needs_review`
- fail: 0, warning: 30

## [WARNING] `merge_canonicalization` / `callable_symbol_count`

- value: **5**  (from `parameterization.callable_symbol_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 5
  - `<related section in metrics JSON>` → 5

## [WARNING] `merge_canonicalization` / `callable_symbol_with_args_count`

- value: **5**  (from `parameterization.callable_symbol_with_args_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 5
  - `<related section in metrics JSON>` → 5

## [WARNING] `merge_canonicalization` / `draft_variant_count`

- value: **1**  (from `variants.draft_variant_count`)
- meaning: A merge/variant/gold comparison changed structure or semantics; report exact compared variants or merge rows.
- repair: Use overlay/bridge/conflict split or reject rewrite based on backtest.

## [WARNING] `merge_canonicalization` / `factorization_count`

- value: **5**  (from `parameterization.factorization_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 5
  - `<related section in metrics JSON>` → 5

## [WARNING] `merge_canonicalization` / `focus_signature_unique_count`

- value: **1**  (from `variability.focus_signature_unique_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.

## [WARNING] `merge_canonicalization` / `quantifier_parameter_slot_count`

- value: **5**  (from `parameterization.quantifier_parameter_slot_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `assertion_complexity.top_complex_assertions` → average_daily_value_traded_divided_by_trading_day_count_definition; daily_value_traded_sum_over_period_definition; trading_day_count_in_period_definition
  - `assertion_complexity.max_assertion_depth` → 6
  - `assertion_complexity.total_quantifier_count` → 5

## [WARNING] `merge_canonicalization` / `top_level_parameter_slot_count`

- value: **9**  (from `parameterization.top_level_parameter_slot_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 9
  - `<related section in metrics JSON>` → 9

## [WARNING] `merge_canonicalization` / `total_parameter_slot_mass`

- value: **14**  (from `parameterization.total_parameter_slot_mass`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 14
  - `<related section in metrics JSON>` → 14

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

- value: **8**  (from `identifier_glue.compound_identifier_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'average_daily_value_traded_divided_by_trading_day_count_definiti; {'identifier': 'daily_value_traded_sum_over_period_definition', 'raw_piece_count; {'identifier': 'daily_value_traded_sum_over_period', 'raw_piece_count': 6, 'cont (+13 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'trading_day_count_in_period_definition', 'raw_piece_count': 6, '; {'identifier': 'trading_day_falls_in_period', 'raw_piece_count': 5, 'content_pie; {'identifier': 'daily_value_traded_sum_over_period_definition', 'raw_piece_count (+9 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `compound_identifier_count_raw`

- value: **7**  (from `identifier_glue.compound_identifier_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'average_daily_value_traded_divided_by_trading_day_count_definiti; {'identifier': 'daily_value_traded_sum_over_period_definition', 'raw_piece_count; {'identifier': 'daily_value_traded_sum_over_period', 'raw_piece_count': 6, 'cont (+13 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'trading_day_count_in_period_definition', 'raw_piece_count': 6, '; {'identifier': 'trading_day_falls_in_period', 'raw_piece_count': 5, 'content_pie; {'identifier': 'daily_value_traded_sum_over_period_definition', 'raw_piece_count (+9 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `identifier_count`

- value: **16**  (from `identifier_glue.identifier_count`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'average_daily_value_traded_divided_by_trading_day_count_definiti; {'identifier': 'daily_value_traded_sum_over_period_definition', 'raw_piece_count; {'identifier': 'daily_value_traded_sum_over_period', 'raw_piece_count': 6, 'cont (+13 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'trading_day_count_in_period_definition', 'raw_piece_count': 6, '; {'identifier': 'trading_day_falls_in_period', 'raw_piece_count': 5, 'content_pie; {'identifier': 'daily_value_traded_sum_over_period_definition', 'raw_piece_count (+9 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `identifier_glue_excess_mass_content`

- value: **23**  (from `identifier_glue.identifier_glue_excess_mass_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'average_daily_value_traded_divided_by_trading_day_count_definiti; {'identifier': 'daily_value_traded_sum_over_period_definition', 'raw_piece_count; {'identifier': 'daily_value_traded_sum_over_period', 'raw_piece_count': 6, 'cont (+13 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'trading_day_count_in_period_definition', 'raw_piece_count': 6, '; {'identifier': 'trading_day_falls_in_period', 'raw_piece_count': 5, 'content_pie; {'identifier': 'daily_value_traded_sum_over_period_definition', 'raw_piece_count (+9 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `identifier_glue_excess_mass_raw`

- value: **22**  (from `identifier_glue.identifier_glue_excess_mass_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'average_daily_value_traded_divided_by_trading_day_count_definiti; {'identifier': 'daily_value_traded_sum_over_period_definition', 'raw_piece_count; {'identifier': 'daily_value_traded_sum_over_period', 'raw_piece_count': 6, 'cont (+13 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'trading_day_count_in_period_definition', 'raw_piece_count': 6, '; {'identifier': 'trading_day_falls_in_period', 'raw_piece_count': 5, 'content_pie; {'identifier': 'daily_value_traded_sum_over_period_definition', 'raw_piece_count (+9 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `max_identifier_piece_count_content`

- value: **8**  (from `identifier_glue.max_identifier_piece_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'average_daily_value_traded_divided_by_trading_day_count_definiti; {'identifier': 'daily_value_traded_sum_over_period_definition', 'raw_piece_count; {'identifier': 'daily_value_traded_sum_over_period', 'raw_piece_count': 6, 'cont (+13 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'trading_day_count_in_period_definition', 'raw_piece_count': 6, '; {'identifier': 'trading_day_falls_in_period', 'raw_piece_count': 5, 'content_pie; {'identifier': 'daily_value_traded_sum_over_period_definition', 'raw_piece_count (+9 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `max_identifier_piece_count_raw`

- value: **10**  (from `identifier_glue.max_identifier_piece_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'average_daily_value_traded_divided_by_trading_day_count_definiti; {'identifier': 'daily_value_traded_sum_over_period_definition', 'raw_piece_count; {'identifier': 'daily_value_traded_sum_over_period', 'raw_piece_count': 6, 'cont (+13 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'trading_day_count_in_period_definition', 'raw_piece_count': 6, '; {'identifier': 'trading_day_falls_in_period', 'raw_piece_count': 5, 'content_pie; {'identifier': 'daily_value_traded_sum_over_period_definition', 'raw_piece_count (+9 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `mean_identifier_piece_count_content`

- value: **3**  (from `identifier_glue.mean_identifier_piece_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'average_daily_value_traded_divided_by_trading_day_count_definiti; {'identifier': 'daily_value_traded_sum_over_period_definition', 'raw_piece_count; {'identifier': 'daily_value_traded_sum_over_period', 'raw_piece_count': 6, 'cont (+13 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'trading_day_count_in_period_definition', 'raw_piece_count': 6, '; {'identifier': 'trading_day_falls_in_period', 'raw_piece_count': 5, 'content_pie; {'identifier': 'daily_value_traded_sum_over_period_definition', 'raw_piece_count (+9 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `mean_identifier_piece_count_raw`

- value: **3.6875**  (from `identifier_glue.mean_identifier_piece_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'average_daily_value_traded_divided_by_trading_day_count_definiti; {'identifier': 'daily_value_traded_sum_over_period_definition', 'raw_piece_count; {'identifier': 'daily_value_traded_sum_over_period', 'raw_piece_count': 6, 'cont (+13 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'trading_day_count_in_period_definition', 'raw_piece_count': 6, '; {'identifier': 'trading_day_falls_in_period', 'raw_piece_count': 5, 'content_pie; {'identifier': 'daily_value_traded_sum_over_period_definition', 'raw_piece_count (+9 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `new_formula_content_token_count_vs_text_only`

- value: **17**  (from `grounding.new_formula_content_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → average_daily_value_traded; average_daily_value_traded_divided_by_trading_day_count_definition; averagedailyvaluetraded (+14 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; average_daily_value_traded; average_daily_value_traded_divided_by_trading_day_count_definition (+34 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'period', 'current_count': 12, 'baseline_count': 2, 'delta': 10}; {'token': 'specifiedperiod', 'current_count': 8, 'baseline_count': 0, 'delta': 8; {'token': 'daily', 'current_count': 9, 'baseline_count': 2, 'delta': 7} (+15 more)
  - `grounding.origin_error_count` → 4

## [WARNING] `ontology_planning` / `new_formula_token_count_vs_text_only`

- value: **21**  (from `grounding.new_formula_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → average_daily_value_traded; average_daily_value_traded_divided_by_trading_day_count_definition; averagedailyvaluetraded (+14 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; average_daily_value_traded; average_daily_value_traded_divided_by_trading_day_count_definition (+34 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'period', 'current_count': 12, 'baseline_count': 2, 'delta': 10}; {'token': 'specifiedperiod', 'current_count': 8, 'baseline_count': 0, 'delta': 8; {'token': 'daily', 'current_count': 9, 'baseline_count': 2, 'delta': 7} (+15 more)
  - `grounding.origin_error_count` → 4

## [WARNING] `ontology_planning` / `new_full_surface_content_token_count_vs_text_only`

- value: **37**  (from `grounding.new_full_surface_content_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → average_daily_value_traded; average_daily_value_traded_divided_by_trading_day_count_definition; averagedailyvaluetraded (+14 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; average_daily_value_traded; average_daily_value_traded_divided_by_trading_day_count_definition (+34 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'period', 'current_count': 12, 'baseline_count': 2, 'delta': 10}; {'token': 'specifiedperiod', 'current_count': 8, 'baseline_count': 0, 'delta': 8; {'token': 'daily', 'current_count': 9, 'baseline_count': 2, 'delta': 7} (+15 more)
  - `grounding.origin_error_count` → 4

## [WARNING] `ontology_planning` / `new_full_surface_token_count_vs_text_only`

- value: **45**  (from `grounding.new_full_surface_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → average_daily_value_traded; average_daily_value_traded_divided_by_trading_day_count_definition; averagedailyvaluetraded (+14 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; average_daily_value_traded; average_daily_value_traded_divided_by_trading_day_count_definition (+34 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'period', 'current_count': 12, 'baseline_count': 2, 'delta': 10}; {'token': 'specifiedperiod', 'current_count': 8, 'baseline_count': 0, 'delta': 8; {'token': 'daily', 'current_count': 9, 'baseline_count': 2, 'delta': 7} (+15 more)
  - `grounding.origin_error_count` → 4

## [WARNING] `ontology_planning` / `new_surface_content_token_count`

- value: **58**  (from `<search recursive metrics JSON for key `new_surface_content_token_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → average_daily_value_traded; average_daily_value_traded_divided_by_trading_day_count_definition; averagedailyvaluetraded (+14 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; average_daily_value_traded; average_daily_value_traded_divided_by_trading_day_count_definition (+34 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'period', 'current_count': 12, 'baseline_count': 2, 'delta': 10}; {'token': 'specifiedperiod', 'current_count': 8, 'baseline_count': 0, 'delta': 8; {'token': 'daily', 'current_count': 9, 'baseline_count': 2, 'delta': 7} (+15 more)
  - `grounding.origin_error_count` → 4

## [WARNING] `ontology_planning` / `new_surface_token_count`

- value: **58**  (from `<search recursive metrics JSON for key `new_surface_token_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → average_daily_value_traded; average_daily_value_traded_divided_by_trading_day_count_definition; averagedailyvaluetraded (+14 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; average_daily_value_traded; average_daily_value_traded_divided_by_trading_day_count_definition (+34 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'period', 'current_count': 12, 'baseline_count': 2, 'delta': 10}; {'token': 'specifiedperiod', 'current_count': 8, 'baseline_count': 0, 'delta': 8; {'token': 'daily', 'current_count': 9, 'baseline_count': 2, 'delta': 7} (+15 more)
  - `grounding.origin_error_count` → 4

## [WARNING] `ontology_planning` / `ungrounded_callee_count`

- value: **1**  (from `grounding.ungrounded_callee_count`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → average_daily_value_traded; average_daily_value_traded_divided_by_trading_day_count_definition; averagedailyvaluetraded (+14 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; average_daily_value_traded; average_daily_value_traded_divided_by_trading_day_count_definition (+34 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'period', 'current_count': 12, 'baseline_count': 2, 'delta': 10}; {'token': 'specifiedperiod', 'current_count': 8, 'baseline_count': 0, 'delta': 8; {'token': 'daily', 'current_count': 9, 'baseline_count': 2, 'delta': 7} (+15 more)
  - `grounding.origin_error_count` → 4

## [WARNING] `ontology_planning` / `ungrounded_ref_count`

- value: **1**  (from `grounding.ungrounded_ref_count`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → average_daily_value_traded; average_daily_value_traded_divided_by_trading_day_count_definition; averagedailyvaluetraded (+14 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; average_daily_value_traded; average_daily_value_traded_divided_by_trading_day_count_definition (+34 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'period', 'current_count': 12, 'baseline_count': 2, 'delta': 10}; {'token': 'specifiedperiod', 'current_count': 8, 'baseline_count': 0, 'delta': 8; {'token': 'daily', 'current_count': 9, 'baseline_count': 2, 'delta': 7} (+15 more)
  - `grounding.origin_error_count` → 4

## [WARNING] `ontology_planning` / `ungrounded_sort_count`

- value: **1**  (from `grounding.ungrounded_sort_count`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → average_daily_value_traded; average_daily_value_traded_divided_by_trading_day_count_definition; averagedailyvaluetraded (+14 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; average_daily_value_traded; average_daily_value_traded_divided_by_trading_day_count_definition (+34 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'period', 'current_count': 12, 'baseline_count': 2, 'delta': 10}; {'token': 'specifiedperiod', 'current_count': 8, 'baseline_count': 0, 'delta': 8; {'token': 'daily', 'current_count': 9, 'baseline_count': 2, 'delta': 7} (+15 more)
  - `grounding.origin_error_count` → 4

## [WARNING] `ontology_planning` / `ungrounded_symbol_count`

- value: **2**  (from `grounding.ungrounded_symbol_count`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → average_daily_value_traded; average_daily_value_traded_divided_by_trading_day_count_definition; averagedailyvaluetraded (+14 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; average_daily_value_traded; average_daily_value_traded_divided_by_trading_day_count_definition (+34 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'period', 'current_count': 12, 'baseline_count': 2, 'delta': 10}; {'token': 'specifiedperiod', 'current_count': 8, 'baseline_count': 0, 'delta': 8; {'token': 'daily', 'current_count': 9, 'baseline_count': 2, 'delta': 7} (+15 more)
  - `grounding.origin_error_count` → 4
