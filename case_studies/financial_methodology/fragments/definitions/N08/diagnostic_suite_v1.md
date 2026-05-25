# Diagnostic report — N08

- **gate**: `needs_review`
- fail: 0, warning: 26

## [WARNING] `merge_canonicalization` / `callable_symbol_count`

- value: **4**  (from `parameterization.callable_symbol_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 4
  - `<related section in metrics JSON>` → 4

## [WARNING] `merge_canonicalization` / `callable_symbol_with_args_count`

- value: **4**  (from `parameterization.callable_symbol_with_args_count`)
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

- value: **4**  (from `parameterization.factorization_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 4
  - `<related section in metrics JSON>` → 4

## [WARNING] `merge_canonicalization` / `focus_signature_unique_count`

- value: **1**  (from `variability.focus_signature_unique_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.

## [WARNING] `merge_canonicalization` / `quantifier_parameter_slot_count`

- value: **2**  (from `parameterization.quantifier_parameter_slot_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `assertion_complexity.top_complex_assertions` → daily_value_traded_product_definition
  - `assertion_complexity.max_assertion_depth` → 7
  - `assertion_complexity.total_quantifier_count` → 2

## [WARNING] `merge_canonicalization` / `top_level_parameter_slot_count`

- value: **8**  (from `parameterization.top_level_parameter_slot_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 8
  - `<related section in metrics JSON>` → 8

## [WARNING] `merge_canonicalization` / `total_parameter_slot_mass`

- value: **10**  (from `parameterization.total_parameter_slot_mass`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 10
  - `<related section in metrics JSON>` → 10

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

- value: **4**  (from `identifier_glue.compound_identifier_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'volume_traded_on_exchange_during_trading_day', 'raw_piece_count'; {'identifier': 'daily_value_traded_product_definition', 'raw_piece_count': 5, 'c; {'identifier': 'VolumeNumberOfShares', 'raw_piece_count': 4, 'content_piece_coun (+8 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'respective_exchange', 'raw_piece_count': 2, 'content_piece_count; {'identifier': 'daily_value_traded_product_definition', 'raw_piece_count': 5, 'c; {'identifier': 'volume_traded_on_exchange_during_trading_day', 'raw_piece_count' (+5 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `compound_identifier_count_raw`

- value: **3**  (from `identifier_glue.compound_identifier_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'volume_traded_on_exchange_during_trading_day', 'raw_piece_count'; {'identifier': 'daily_value_traded_product_definition', 'raw_piece_count': 5, 'c; {'identifier': 'VolumeNumberOfShares', 'raw_piece_count': 4, 'content_piece_coun (+8 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'respective_exchange', 'raw_piece_count': 2, 'content_piece_count; {'identifier': 'daily_value_traded_product_definition', 'raw_piece_count': 5, 'c; {'identifier': 'volume_traded_on_exchange_during_trading_day', 'raw_piece_count' (+5 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `identifier_count`

- value: **11**  (from `identifier_glue.identifier_count`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'volume_traded_on_exchange_during_trading_day', 'raw_piece_count'; {'identifier': 'daily_value_traded_product_definition', 'raw_piece_count': 5, 'c; {'identifier': 'VolumeNumberOfShares', 'raw_piece_count': 4, 'content_piece_coun (+8 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'respective_exchange', 'raw_piece_count': 2, 'content_piece_count; {'identifier': 'daily_value_traded_product_definition', 'raw_piece_count': 5, 'c; {'identifier': 'volume_traded_on_exchange_during_trading_day', 'raw_piece_count' (+5 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `identifier_glue_excess_mass_content`

- value: **9**  (from `identifier_glue.identifier_glue_excess_mass_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'volume_traded_on_exchange_during_trading_day', 'raw_piece_count'; {'identifier': 'daily_value_traded_product_definition', 'raw_piece_count': 5, 'c; {'identifier': 'VolumeNumberOfShares', 'raw_piece_count': 4, 'content_piece_coun (+8 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'respective_exchange', 'raw_piece_count': 2, 'content_piece_count; {'identifier': 'daily_value_traded_product_definition', 'raw_piece_count': 5, 'c; {'identifier': 'volume_traded_on_exchange_during_trading_day', 'raw_piece_count' (+5 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `identifier_glue_excess_mass_raw`

- value: **7**  (from `identifier_glue.identifier_glue_excess_mass_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'volume_traded_on_exchange_during_trading_day', 'raw_piece_count'; {'identifier': 'daily_value_traded_product_definition', 'raw_piece_count': 5, 'c; {'identifier': 'VolumeNumberOfShares', 'raw_piece_count': 4, 'content_piece_coun (+8 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'respective_exchange', 'raw_piece_count': 2, 'content_piece_count; {'identifier': 'daily_value_traded_product_definition', 'raw_piece_count': 5, 'c; {'identifier': 'volume_traded_on_exchange_during_trading_day', 'raw_piece_count' (+5 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `max_identifier_piece_count_content`

- value: **6**  (from `identifier_glue.max_identifier_piece_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'volume_traded_on_exchange_during_trading_day', 'raw_piece_count'; {'identifier': 'daily_value_traded_product_definition', 'raw_piece_count': 5, 'c; {'identifier': 'VolumeNumberOfShares', 'raw_piece_count': 4, 'content_piece_coun (+8 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'respective_exchange', 'raw_piece_count': 2, 'content_piece_count; {'identifier': 'daily_value_traded_product_definition', 'raw_piece_count': 5, 'c; {'identifier': 'volume_traded_on_exchange_during_trading_day', 'raw_piece_count' (+5 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `max_identifier_piece_count_raw`

- value: **7**  (from `identifier_glue.max_identifier_piece_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'volume_traded_on_exchange_during_trading_day', 'raw_piece_count'; {'identifier': 'daily_value_traded_product_definition', 'raw_piece_count': 5, 'c; {'identifier': 'VolumeNumberOfShares', 'raw_piece_count': 4, 'content_piece_coun (+8 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'respective_exchange', 'raw_piece_count': 2, 'content_piece_count; {'identifier': 'daily_value_traded_product_definition', 'raw_piece_count': 5, 'c; {'identifier': 'volume_traded_on_exchange_during_trading_day', 'raw_piece_count' (+5 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `mean_identifier_piece_count_content`

- value: **2.3636363636363638**  (from `identifier_glue.mean_identifier_piece_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'volume_traded_on_exchange_during_trading_day', 'raw_piece_count'; {'identifier': 'daily_value_traded_product_definition', 'raw_piece_count': 5, 'c; {'identifier': 'VolumeNumberOfShares', 'raw_piece_count': 4, 'content_piece_coun (+8 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'respective_exchange', 'raw_piece_count': 2, 'content_piece_count; {'identifier': 'daily_value_traded_product_definition', 'raw_piece_count': 5, 'c; {'identifier': 'volume_traded_on_exchange_during_trading_day', 'raw_piece_count' (+5 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `mean_identifier_piece_count_raw`

- value: **2.727272727272727**  (from `identifier_glue.mean_identifier_piece_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'volume_traded_on_exchange_during_trading_day', 'raw_piece_count'; {'identifier': 'daily_value_traded_product_definition', 'raw_piece_count': 5, 'c; {'identifier': 'VolumeNumberOfShares', 'raw_piece_count': 4, 'content_piece_coun (+8 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'respective_exchange', 'raw_piece_count': 2, 'content_piece_count; {'identifier': 'daily_value_traded_product_definition', 'raw_piece_count': 5, 'c; {'identifier': 'volume_traded_on_exchange_during_trading_day', 'raw_piece_count' (+5 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `new_formula_content_token_count_vs_text_only`

- value: **13**  (from `grounding.new_formula_content_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → closing_price; closingprice; daily_value_traded (+10 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; canonical; closing_price (+30 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'exchange', 'current_count': 7, 'baseline_count': 1, 'delta': 6}; {'token': 'indexcomponent', 'current_count': 6, 'baseline_count': 0, 'delta': 6}; {'token': 'tradingday', 'current_count': 5, 'baseline_count': 0, 'delta': 5} (+15 more)
  - `grounding.origin_error_count` → 0

## [WARNING] `ontology_planning` / `new_formula_token_count_vs_text_only`

- value: **15**  (from `grounding.new_formula_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → closing_price; closingprice; daily_value_traded (+10 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; canonical; closing_price (+30 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'exchange', 'current_count': 7, 'baseline_count': 1, 'delta': 6}; {'token': 'indexcomponent', 'current_count': 6, 'baseline_count': 0, 'delta': 6}; {'token': 'tradingday', 'current_count': 5, 'baseline_count': 0, 'delta': 5} (+15 more)
  - `grounding.origin_error_count` → 0

## [WARNING] `ontology_planning` / `new_full_surface_content_token_count_vs_text_only`

- value: **33**  (from `grounding.new_full_surface_content_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → closing_price; closingprice; daily_value_traded (+10 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; canonical; closing_price (+30 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'exchange', 'current_count': 7, 'baseline_count': 1, 'delta': 6}; {'token': 'indexcomponent', 'current_count': 6, 'baseline_count': 0, 'delta': 6}; {'token': 'tradingday', 'current_count': 5, 'baseline_count': 0, 'delta': 5} (+15 more)
  - `grounding.origin_error_count` → 0

## [WARNING] `ontology_planning` / `new_full_surface_token_count_vs_text_only`

- value: **39**  (from `grounding.new_full_surface_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → closing_price; closingprice; daily_value_traded (+10 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; canonical; closing_price (+30 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'exchange', 'current_count': 7, 'baseline_count': 1, 'delta': 6}; {'token': 'indexcomponent', 'current_count': 6, 'baseline_count': 0, 'delta': 6}; {'token': 'tradingday', 'current_count': 5, 'baseline_count': 0, 'delta': 5} (+15 more)
  - `grounding.origin_error_count` → 0

## [WARNING] `ontology_planning` / `new_surface_content_token_count`

- value: **31**  (from `<search recursive metrics JSON for key `new_surface_content_token_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → closing_price; closingprice; daily_value_traded (+10 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; canonical; closing_price (+30 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'exchange', 'current_count': 7, 'baseline_count': 1, 'delta': 6}; {'token': 'indexcomponent', 'current_count': 6, 'baseline_count': 0, 'delta': 6}; {'token': 'tradingday', 'current_count': 5, 'baseline_count': 0, 'delta': 5} (+15 more)
  - `grounding.origin_error_count` → 0

## [WARNING] `ontology_planning` / `new_surface_token_count`

- value: **31**  (from `<search recursive metrics JSON for key `new_surface_token_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → closing_price; closingprice; daily_value_traded (+10 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; canonical; closing_price (+30 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'exchange', 'current_count': 7, 'baseline_count': 1, 'delta': 6}; {'token': 'indexcomponent', 'current_count': 6, 'baseline_count': 0, 'delta': 6}; {'token': 'tradingday', 'current_count': 5, 'baseline_count': 0, 'delta': 5} (+15 more)
  - `grounding.origin_error_count` → 0
