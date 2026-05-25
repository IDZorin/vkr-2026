# Diagnostic report — N07

- **gate**: `needs_review`
- fail: 0, warning: 31

## [WARNING] `merge_canonicalization` / `callable_symbol_count`

- value: **8**  (from `parameterization.callable_symbol_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 8
  - `<related section in metrics JSON>` → 8

## [WARNING] `merge_canonicalization` / `callable_symbol_with_args_count`

- value: **8**  (from `parameterization.callable_symbol_with_args_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 8
  - `<related section in metrics JSON>` → 8

## [WARNING] `merge_canonicalization` / `dependency_link_count`

- value: **2**  (from `<search recursive metrics JSON for key `dependency_link_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 2
  - `<related section in metrics JSON>` → 2

## [WARNING] `merge_canonicalization` / `draft_variant_count`

- value: **1**  (from `variants.draft_variant_count`)
- meaning: A merge/variant/gold comparison changed structure or semantics; report exact compared variants or merge rows.
- repair: Use overlay/bridge/conflict split or reject rewrite based on backtest.

## [WARNING] `merge_canonicalization` / `factorization_count`

- value: **8**  (from `parameterization.factorization_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 8
  - `<related section in metrics JSON>` → 8

## [WARNING] `merge_canonicalization` / `focus_signature_unique_count`

- value: **1**  (from `variability.focus_signature_unique_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.

## [WARNING] `merge_canonicalization` / `quantifier_parameter_slot_count`

- value: **4**  (from `parameterization.quantifier_parameter_slot_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `assertion_complexity.top_complex_assertions` → closing_price_definition_when_published; last_trading_price_used_when_closing_price_not_published
  - `assertion_complexity.max_assertion_depth` → 7
  - `assertion_complexity.total_quantifier_count` → 4

## [WARNING] `merge_canonicalization` / `top_level_parameter_slot_count`

- value: **14**  (from `parameterization.top_level_parameter_slot_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 14
  - `<related section in metrics JSON>` → 14

## [WARNING] `merge_canonicalization` / `total_parameter_slot_mass`

- value: **18**  (from `parameterization.total_parameter_slot_mass`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 18
  - `<related section in metrics JSON>` → 18

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

- value: **6**  (from `identifier_glue.compound_identifier_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'last_trading_price_used_when_closing_price_not_published', 'raw_; {'identifier': 'closing_price_definition_when_published', 'raw_piece_count': 5, ; {'identifier': 'final_regular_hours_trading_price', 'raw_piece_count': 5, 'conte (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'AccordanceStandard', 'raw_piece_count': 2, 'content_piece_count'; {'identifier': 'respective_exchange', 'raw_piece_count': 2, 'content_piece_count; {'identifier': 'closing_price_definition_when_published', 'raw_piece_count': 5,  (+12 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'last_trading_price_used_when_closing_price_not_published', 'raw_
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'last_trading_price_used_when_closing_price_not_published', 'raw_

## [WARNING] `ontology_planning` / `compound_identifier_count_raw`

- value: **4**  (from `identifier_glue.compound_identifier_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'last_trading_price_used_when_closing_price_not_published', 'raw_; {'identifier': 'closing_price_definition_when_published', 'raw_piece_count': 5, ; {'identifier': 'final_regular_hours_trading_price', 'raw_piece_count': 5, 'conte (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'AccordanceStandard', 'raw_piece_count': 2, 'content_piece_count'; {'identifier': 'respective_exchange', 'raw_piece_count': 2, 'content_piece_count; {'identifier': 'closing_price_definition_when_published', 'raw_piece_count': 5,  (+12 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'last_trading_price_used_when_closing_price_not_published', 'raw_
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'last_trading_price_used_when_closing_price_not_published', 'raw_

## [WARNING] `ontology_planning` / `dependency_link_count`

- value: **2**  (from `<search recursive metrics JSON for key `dependency_link_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 2
  - `<related section in metrics JSON>` → 2

## [WARNING] `ontology_planning` / `identifier_count`

- value: **21**  (from `identifier_glue.identifier_count`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'last_trading_price_used_when_closing_price_not_published', 'raw_; {'identifier': 'closing_price_definition_when_published', 'raw_piece_count': 5, ; {'identifier': 'final_regular_hours_trading_price', 'raw_piece_count': 5, 'conte (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'AccordanceStandard', 'raw_piece_count': 2, 'content_piece_count'; {'identifier': 'respective_exchange', 'raw_piece_count': 2, 'content_piece_count; {'identifier': 'closing_price_definition_when_published', 'raw_piece_count': 5,  (+12 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'last_trading_price_used_when_closing_price_not_published', 'raw_
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'last_trading_price_used_when_closing_price_not_published', 'raw_

## [WARNING] `ontology_planning` / `identifier_glue_excess_mass_content`

- value: **15**  (from `identifier_glue.identifier_glue_excess_mass_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'last_trading_price_used_when_closing_price_not_published', 'raw_; {'identifier': 'closing_price_definition_when_published', 'raw_piece_count': 5, ; {'identifier': 'final_regular_hours_trading_price', 'raw_piece_count': 5, 'conte (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'AccordanceStandard', 'raw_piece_count': 2, 'content_piece_count'; {'identifier': 'respective_exchange', 'raw_piece_count': 2, 'content_piece_count; {'identifier': 'closing_price_definition_when_published', 'raw_piece_count': 5,  (+12 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'last_trading_price_used_when_closing_price_not_published', 'raw_
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'last_trading_price_used_when_closing_price_not_published', 'raw_

## [WARNING] `ontology_planning` / `identifier_glue_excess_mass_raw`

- value: **11**  (from `identifier_glue.identifier_glue_excess_mass_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'last_trading_price_used_when_closing_price_not_published', 'raw_; {'identifier': 'closing_price_definition_when_published', 'raw_piece_count': 5, ; {'identifier': 'final_regular_hours_trading_price', 'raw_piece_count': 5, 'conte (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'AccordanceStandard', 'raw_piece_count': 2, 'content_piece_count'; {'identifier': 'respective_exchange', 'raw_piece_count': 2, 'content_piece_count; {'identifier': 'closing_price_definition_when_published', 'raw_piece_count': 5,  (+12 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'last_trading_price_used_when_closing_price_not_published', 'raw_
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'last_trading_price_used_when_closing_price_not_published', 'raw_

## [WARNING] `ontology_planning` / `low_source_grounded_glued_identifier_count`

- value: **3**  (from `identifier_glue.low_source_grounded_glued_identifier_count`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'last_trading_price_used_when_closing_price_not_published', 'raw_; {'identifier': 'closing_price_definition_when_published', 'raw_piece_count': 5, ; {'identifier': 'final_regular_hours_trading_price', 'raw_piece_count': 5, 'conte (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'AccordanceStandard', 'raw_piece_count': 2, 'content_piece_count'; {'identifier': 'respective_exchange', 'raw_piece_count': 2, 'content_piece_count; {'identifier': 'closing_price_definition_when_published', 'raw_piece_count': 5,  (+12 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'last_trading_price_used_when_closing_price_not_published', 'raw_
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'last_trading_price_used_when_closing_price_not_published', 'raw_

## [WARNING] `ontology_planning` / `max_identifier_piece_count_content`

- value: **8**  (from `identifier_glue.max_identifier_piece_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'last_trading_price_used_when_closing_price_not_published', 'raw_; {'identifier': 'closing_price_definition_when_published', 'raw_piece_count': 5, ; {'identifier': 'final_regular_hours_trading_price', 'raw_piece_count': 5, 'conte (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'AccordanceStandard', 'raw_piece_count': 2, 'content_piece_count'; {'identifier': 'respective_exchange', 'raw_piece_count': 2, 'content_piece_count; {'identifier': 'closing_price_definition_when_published', 'raw_piece_count': 5,  (+12 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'last_trading_price_used_when_closing_price_not_published', 'raw_
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'last_trading_price_used_when_closing_price_not_published', 'raw_

## [WARNING] `ontology_planning` / `max_identifier_piece_count_raw`

- value: **9**  (from `identifier_glue.max_identifier_piece_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'last_trading_price_used_when_closing_price_not_published', 'raw_; {'identifier': 'closing_price_definition_when_published', 'raw_piece_count': 5, ; {'identifier': 'final_regular_hours_trading_price', 'raw_piece_count': 5, 'conte (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'AccordanceStandard', 'raw_piece_count': 2, 'content_piece_count'; {'identifier': 'respective_exchange', 'raw_piece_count': 2, 'content_piece_count; {'identifier': 'closing_price_definition_when_published', 'raw_piece_count': 5,  (+12 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'last_trading_price_used_when_closing_price_not_published', 'raw_
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'last_trading_price_used_when_closing_price_not_published', 'raw_

## [WARNING] `ontology_planning` / `mean_identifier_piece_count_content`

- value: **2.3333333333333335**  (from `identifier_glue.mean_identifier_piece_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'last_trading_price_used_when_closing_price_not_published', 'raw_; {'identifier': 'closing_price_definition_when_published', 'raw_piece_count': 5, ; {'identifier': 'final_regular_hours_trading_price', 'raw_piece_count': 5, 'conte (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'AccordanceStandard', 'raw_piece_count': 2, 'content_piece_count'; {'identifier': 'respective_exchange', 'raw_piece_count': 2, 'content_piece_count; {'identifier': 'closing_price_definition_when_published', 'raw_piece_count': 5,  (+12 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'last_trading_price_used_when_closing_price_not_published', 'raw_
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'last_trading_price_used_when_closing_price_not_published', 'raw_

## [WARNING] `ontology_planning` / `mean_identifier_piece_count_raw`

- value: **2.619047619047619**  (from `identifier_glue.mean_identifier_piece_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'last_trading_price_used_when_closing_price_not_published', 'raw_; {'identifier': 'closing_price_definition_when_published', 'raw_piece_count': 5, ; {'identifier': 'final_regular_hours_trading_price', 'raw_piece_count': 5, 'conte (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'AccordanceStandard', 'raw_piece_count': 2, 'content_piece_count'; {'identifier': 'respective_exchange', 'raw_piece_count': 2, 'content_piece_count; {'identifier': 'closing_price_definition_when_published', 'raw_piece_count': 5,  (+12 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'last_trading_price_used_when_closing_price_not_published', 'raw_
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'last_trading_price_used_when_closing_price_not_published', 'raw_

## [WARNING] `ontology_planning` / `new_formula_content_token_count_vs_text_only`

- value: **20**  (from `grounding.new_formula_content_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → accordancestandard; closing_price; closing_price_available (+17 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; accordancestandard; canonical (+37 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'price', 'current_count': 26, 'baseline_count': 4, 'delta': 22}; {'token': 'closing', 'current_count': 12, 'baseline_count': 2, 'delta': 10}; {'token': 'indexcomponent', 'current_count': 8, 'baseline_count': 0, 'delta': 8} (+17 more)
  - `grounding.origin_error_count` → 2

## [WARNING] `ontology_planning` / `new_formula_token_count_vs_text_only`

- value: **22**  (from `grounding.new_formula_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → accordancestandard; closing_price; closing_price_available (+17 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; accordancestandard; canonical (+37 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'price', 'current_count': 26, 'baseline_count': 4, 'delta': 22}; {'token': 'closing', 'current_count': 12, 'baseline_count': 2, 'delta': 10}; {'token': 'indexcomponent', 'current_count': 8, 'baseline_count': 0, 'delta': 8} (+17 more)
  - `grounding.origin_error_count` → 2

## [WARNING] `ontology_planning` / `new_full_surface_content_token_count_vs_text_only`

- value: **40**  (from `grounding.new_full_surface_content_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → accordancestandard; closing_price; closing_price_available (+17 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; accordancestandard; canonical (+37 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'price', 'current_count': 26, 'baseline_count': 4, 'delta': 22}; {'token': 'closing', 'current_count': 12, 'baseline_count': 2, 'delta': 10}; {'token': 'indexcomponent', 'current_count': 8, 'baseline_count': 0, 'delta': 8} (+17 more)
  - `grounding.origin_error_count` → 2

## [WARNING] `ontology_planning` / `new_full_surface_token_count_vs_text_only`

- value: **45**  (from `grounding.new_full_surface_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → accordancestandard; closing_price; closing_price_available (+17 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; accordancestandard; canonical (+37 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'price', 'current_count': 26, 'baseline_count': 4, 'delta': 22}; {'token': 'closing', 'current_count': 12, 'baseline_count': 2, 'delta': 10}; {'token': 'indexcomponent', 'current_count': 8, 'baseline_count': 0, 'delta': 8} (+17 more)
  - `grounding.origin_error_count` → 2

## [WARNING] `ontology_planning` / `new_surface_content_token_count`

- value: **53**  (from `<search recursive metrics JSON for key `new_surface_content_token_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → accordancestandard; closing_price; closing_price_available (+17 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; accordancestandard; canonical (+37 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'price', 'current_count': 26, 'baseline_count': 4, 'delta': 22}; {'token': 'closing', 'current_count': 12, 'baseline_count': 2, 'delta': 10}; {'token': 'indexcomponent', 'current_count': 8, 'baseline_count': 0, 'delta': 8} (+17 more)
  - `grounding.origin_error_count` → 2

## [WARNING] `ontology_planning` / `new_surface_token_count`

- value: **53**  (from `<search recursive metrics JSON for key `new_surface_token_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → accordancestandard; closing_price; closing_price_available (+17 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; accordancestandard; canonical (+37 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'price', 'current_count': 26, 'baseline_count': 4, 'delta': 22}; {'token': 'closing', 'current_count': 12, 'baseline_count': 2, 'delta': 10}; {'token': 'indexcomponent', 'current_count': 8, 'baseline_count': 0, 'delta': 8} (+17 more)
  - `grounding.origin_error_count` → 2

## [WARNING] `ontology_planning` / `ungrounded_sort_count`

- value: **1**  (from `grounding.ungrounded_sort_count`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → accordancestandard; closing_price; closing_price_available (+17 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; accordancestandard; canonical (+37 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'price', 'current_count': 26, 'baseline_count': 4, 'delta': 22}; {'token': 'closing', 'current_count': 12, 'baseline_count': 2, 'delta': 10}; {'token': 'indexcomponent', 'current_count': 8, 'baseline_count': 0, 'delta': 8} (+17 more)
  - `grounding.origin_error_count` → 2

## [WARNING] `ontology_planning` / `ungrounded_symbol_count`

- value: **1**  (from `grounding.ungrounded_symbol_count`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → accordancestandard; closing_price; closing_price_available (+17 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; accordancestandard; canonical (+37 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'price', 'current_count': 26, 'baseline_count': 4, 'delta': 22}; {'token': 'closing', 'current_count': 12, 'baseline_count': 2, 'delta': 10}; {'token': 'indexcomponent', 'current_count': 8, 'baseline_count': 0, 'delta': 8} (+17 more)
  - `grounding.origin_error_count` → 2
