# Diagnostic report — N12

- **gate**: `needs_review`
- fail: 0, warning: 33

## [WARNING] `merge_canonicalization` / `callable_symbol_count`

- value: **10**  (from `parameterization.callable_symbol_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 10
  - `<related section in metrics JSON>` → 10

## [WARNING] `merge_canonicalization` / `callable_symbol_with_args_count`

- value: **10**  (from `parameterization.callable_symbol_with_args_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 10
  - `<related section in metrics JSON>` → 10

## [WARNING] `merge_canonicalization` / `dependency_link_count`

- value: **1**  (from `<search recursive metrics JSON for key `dependency_link_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 1
  - `<related section in metrics JSON>` → 1

## [WARNING] `merge_canonicalization` / `draft_variant_count`

- value: **1**  (from `variants.draft_variant_count`)
- meaning: A merge/variant/gold comparison changed structure or semantics; report exact compared variants or merge rows.
- repair: Use overlay/bridge/conflict split or reject rewrite based on backtest.

## [WARNING] `merge_canonicalization` / `factorization_count`

- value: **10**  (from `parameterization.factorization_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 10
  - `<related section in metrics JSON>` → 10

## [WARNING] `merge_canonicalization` / `focus_signature_unique_count`

- value: **1**  (from `variability.focus_signature_unique_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.

## [WARNING] `merge_canonicalization` / `quantifier_parameter_slot_count`

- value: **3**  (from `parameterization.quantifier_parameter_slot_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `assertion_complexity.top_complex_assertions` → free_float_definition
  - `assertion_complexity.max_assertion_depth` → 9
  - `assertion_complexity.total_quantifier_count` → 3

## [WARNING] `merge_canonicalization` / `top_level_parameter_slot_count`

- value: **18**  (from `parameterization.top_level_parameter_slot_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 18
  - `<related section in metrics JSON>` → 18

## [WARNING] `merge_canonicalization` / `total_parameter_slot_mass`

- value: **21**  (from `parameterization.total_parameter_slot_mass`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 21
  - `<related section in metrics JSON>` → 21

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

- value: **9**  (from `identifier_glue.compound_identifier_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'locked_in_by_long_term_holders', 'raw_piece_count': 6, 'content_; {'identifier': 'available_for_trading_by_market_participants', 'raw_piece_count'; {'identifier': 'issued_share_on_selection_day', 'raw_piece_count': 5, 'content_p (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DataVendor', 'raw_piece_count': 2, 'content_piece_count': 2, 'ra; {'identifier': 'free_float_definition', 'raw_piece_count': 3, 'content_piece_cou; {'identifier': 'free_float_denominator', 'raw_piece_count': 3, 'content_piece_co (+10 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `compound_identifier_count_raw`

- value: **6**  (from `identifier_glue.compound_identifier_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'locked_in_by_long_term_holders', 'raw_piece_count': 6, 'content_; {'identifier': 'available_for_trading_by_market_participants', 'raw_piece_count'; {'identifier': 'issued_share_on_selection_day', 'raw_piece_count': 5, 'content_p (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DataVendor', 'raw_piece_count': 2, 'content_piece_count': 2, 'ra; {'identifier': 'free_float_definition', 'raw_piece_count': 3, 'content_piece_cou; {'identifier': 'free_float_denominator', 'raw_piece_count': 3, 'content_piece_co (+10 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `dependency_link_count`

- value: **1**  (from `<search recursive metrics JSON for key `dependency_link_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 1
  - `<related section in metrics JSON>` → 1

## [WARNING] `ontology_planning` / `identifier_count`

- value: **20**  (from `identifier_glue.identifier_count`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'locked_in_by_long_term_holders', 'raw_piece_count': 6, 'content_; {'identifier': 'available_for_trading_by_market_participants', 'raw_piece_count'; {'identifier': 'issued_share_on_selection_day', 'raw_piece_count': 5, 'content_p (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DataVendor', 'raw_piece_count': 2, 'content_piece_count': 2, 'ra; {'identifier': 'free_float_definition', 'raw_piece_count': 3, 'content_piece_cou; {'identifier': 'free_float_denominator', 'raw_piece_count': 3, 'content_piece_co (+10 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `identifier_glue_excess_mass_content`

- value: **13**  (from `identifier_glue.identifier_glue_excess_mass_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'locked_in_by_long_term_holders', 'raw_piece_count': 6, 'content_; {'identifier': 'available_for_trading_by_market_participants', 'raw_piece_count'; {'identifier': 'issued_share_on_selection_day', 'raw_piece_count': 5, 'content_p (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DataVendor', 'raw_piece_count': 2, 'content_piece_count': 2, 'ra; {'identifier': 'free_float_definition', 'raw_piece_count': 3, 'content_piece_cou; {'identifier': 'free_float_denominator', 'raw_piece_count': 3, 'content_piece_co (+10 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `identifier_glue_excess_mass_raw`

- value: **11**  (from `identifier_glue.identifier_glue_excess_mass_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'locked_in_by_long_term_holders', 'raw_piece_count': 6, 'content_; {'identifier': 'available_for_trading_by_market_participants', 'raw_piece_count'; {'identifier': 'issued_share_on_selection_day', 'raw_piece_count': 5, 'content_p (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DataVendor', 'raw_piece_count': 2, 'content_piece_count': 2, 'ra; {'identifier': 'free_float_definition', 'raw_piece_count': 3, 'content_piece_cou; {'identifier': 'free_float_denominator', 'raw_piece_count': 3, 'content_piece_co (+10 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `invented_helper_sort_count`

- value: **1**  (from `<search recursive metrics JSON for key `invented_helper_sort_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → available_for_trading_by_market_participants; datavendor; financialinstrument (+18 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; available_for_trading_by_market_participants; canonical (+38 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'share', 'current_count': 19, 'baseline_count': 2, 'delta': 17}; {'token': 'float', 'current_count': 14, 'baseline_count': 1, 'delta': 13}; {'token': 'free', 'current_count': 14, 'baseline_count': 1, 'delta': 13} (+17 more)
  - `grounding.origin_error_count` → 3
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'locked_in_by_long_term_holders', 'raw_piece_count': 6, 'content_; {'identifier': 'available_for_trading_by_market_participants', 'raw_piece_count'; {'identifier': 'issued_share_on_selection_day', 'raw_piece_count': 5, 'content_p (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DataVendor', 'raw_piece_count': 2, 'content_piece_count': 2, 'ra; {'identifier': 'free_float_definition', 'raw_piece_count': 3, 'content_piece_cou; {'identifier': 'free_float_denominator', 'raw_piece_count': 3, 'content_piece_co (+10 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)
  - `evidence.invented_helper_sorts` → Security

## [WARNING] `ontology_planning` / `invented_helper_symbol_count`

- value: **1**  (from `<search recursive metrics JSON for key `invented_helper_symbol_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → available_for_trading_by_market_participants; datavendor; financialinstrument (+18 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; available_for_trading_by_market_participants; canonical (+38 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'share', 'current_count': 19, 'baseline_count': 2, 'delta': 17}; {'token': 'float', 'current_count': 14, 'baseline_count': 1, 'delta': 13}; {'token': 'free', 'current_count': 14, 'baseline_count': 1, 'delta': 13} (+17 more)
  - `grounding.origin_error_count` → 3
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'locked_in_by_long_term_holders', 'raw_piece_count': 6, 'content_; {'identifier': 'available_for_trading_by_market_participants', 'raw_piece_count'; {'identifier': 'issued_share_on_selection_day', 'raw_piece_count': 5, 'content_p (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DataVendor', 'raw_piece_count': 2, 'content_piece_count': 2, 'ra; {'identifier': 'free_float_definition', 'raw_piece_count': 3, 'content_piece_cou; {'identifier': 'free_float_denominator', 'raw_piece_count': 3, 'content_piece_co (+10 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)
  - `evidence.invented_helper_sorts` → Security

## [WARNING] `ontology_planning` / `low_source_grounded_glued_identifier_count`

- value: **4**  (from `identifier_glue.low_source_grounded_glued_identifier_count`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'locked_in_by_long_term_holders', 'raw_piece_count': 6, 'content_; {'identifier': 'available_for_trading_by_market_participants', 'raw_piece_count'; {'identifier': 'issued_share_on_selection_day', 'raw_piece_count': 5, 'content_p (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DataVendor', 'raw_piece_count': 2, 'content_piece_count': 2, 'ra; {'identifier': 'free_float_definition', 'raw_piece_count': 3, 'content_piece_cou; {'identifier': 'free_float_denominator', 'raw_piece_count': 3, 'content_piece_co (+10 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `max_identifier_piece_count_content`

- value: **4**  (from `identifier_glue.max_identifier_piece_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'locked_in_by_long_term_holders', 'raw_piece_count': 6, 'content_; {'identifier': 'available_for_trading_by_market_participants', 'raw_piece_count'; {'identifier': 'issued_share_on_selection_day', 'raw_piece_count': 5, 'content_p (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DataVendor', 'raw_piece_count': 2, 'content_piece_count': 2, 'ra; {'identifier': 'free_float_definition', 'raw_piece_count': 3, 'content_piece_cou; {'identifier': 'free_float_denominator', 'raw_piece_count': 3, 'content_piece_co (+10 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `max_identifier_piece_count_raw`

- value: **6**  (from `identifier_glue.max_identifier_piece_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'locked_in_by_long_term_holders', 'raw_piece_count': 6, 'content_; {'identifier': 'available_for_trading_by_market_participants', 'raw_piece_count'; {'identifier': 'issued_share_on_selection_day', 'raw_piece_count': 5, 'content_p (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DataVendor', 'raw_piece_count': 2, 'content_piece_count': 2, 'ra; {'identifier': 'free_float_definition', 'raw_piece_count': 3, 'content_piece_cou; {'identifier': 'free_float_denominator', 'raw_piece_count': 3, 'content_piece_co (+10 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `mean_identifier_piece_count_content`

- value: **2.2**  (from `identifier_glue.mean_identifier_piece_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'locked_in_by_long_term_holders', 'raw_piece_count': 6, 'content_; {'identifier': 'available_for_trading_by_market_participants', 'raw_piece_count'; {'identifier': 'issued_share_on_selection_day', 'raw_piece_count': 5, 'content_p (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DataVendor', 'raw_piece_count': 2, 'content_piece_count': 2, 'ra; {'identifier': 'free_float_definition', 'raw_piece_count': 3, 'content_piece_cou; {'identifier': 'free_float_denominator', 'raw_piece_count': 3, 'content_piece_co (+10 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `mean_identifier_piece_count_raw`

- value: **2.7**  (from `identifier_glue.mean_identifier_piece_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'locked_in_by_long_term_holders', 'raw_piece_count': 6, 'content_; {'identifier': 'available_for_trading_by_market_participants', 'raw_piece_count'; {'identifier': 'issued_share_on_selection_day', 'raw_piece_count': 5, 'content_p (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DataVendor', 'raw_piece_count': 2, 'content_piece_count': 2, 'ra; {'identifier': 'free_float_definition', 'raw_piece_count': 3, 'content_piece_cou; {'identifier': 'free_float_denominator', 'raw_piece_count': 3, 'content_piece_co (+10 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `new_formula_content_token_count_vs_text_only`

- value: **21**  (from `grounding.new_formula_content_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → available_for_trading_by_market_participants; datavendor; financialinstrument (+18 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; available_for_trading_by_market_participants; canonical (+38 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'share', 'current_count': 19, 'baseline_count': 2, 'delta': 17}; {'token': 'float', 'current_count': 14, 'baseline_count': 1, 'delta': 13}; {'token': 'free', 'current_count': 14, 'baseline_count': 1, 'delta': 13} (+17 more)
  - `grounding.origin_error_count` → 3

## [WARNING] `ontology_planning` / `new_formula_token_count_vs_text_only`

- value: **24**  (from `grounding.new_formula_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → available_for_trading_by_market_participants; datavendor; financialinstrument (+18 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; available_for_trading_by_market_participants; canonical (+38 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'share', 'current_count': 19, 'baseline_count': 2, 'delta': 17}; {'token': 'float', 'current_count': 14, 'baseline_count': 1, 'delta': 13}; {'token': 'free', 'current_count': 14, 'baseline_count': 1, 'delta': 13} (+17 more)
  - `grounding.origin_error_count` → 3

## [WARNING] `ontology_planning` / `new_full_surface_content_token_count_vs_text_only`

- value: **41**  (from `grounding.new_full_surface_content_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → available_for_trading_by_market_participants; datavendor; financialinstrument (+18 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; available_for_trading_by_market_participants; canonical (+38 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'share', 'current_count': 19, 'baseline_count': 2, 'delta': 17}; {'token': 'float', 'current_count': 14, 'baseline_count': 1, 'delta': 13}; {'token': 'free', 'current_count': 14, 'baseline_count': 1, 'delta': 13} (+17 more)
  - `grounding.origin_error_count` → 3

## [WARNING] `ontology_planning` / `new_full_surface_token_count_vs_text_only`

- value: **46**  (from `grounding.new_full_surface_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → available_for_trading_by_market_participants; datavendor; financialinstrument (+18 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; available_for_trading_by_market_participants; canonical (+38 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'share', 'current_count': 19, 'baseline_count': 2, 'delta': 17}; {'token': 'float', 'current_count': 14, 'baseline_count': 1, 'delta': 13}; {'token': 'free', 'current_count': 14, 'baseline_count': 1, 'delta': 13} (+17 more)
  - `grounding.origin_error_count` → 3

## [WARNING] `ontology_planning` / `new_surface_content_token_count`

- value: **48**  (from `<search recursive metrics JSON for key `new_surface_content_token_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → available_for_trading_by_market_participants; datavendor; financialinstrument (+18 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; available_for_trading_by_market_participants; canonical (+38 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'share', 'current_count': 19, 'baseline_count': 2, 'delta': 17}; {'token': 'float', 'current_count': 14, 'baseline_count': 1, 'delta': 13}; {'token': 'free', 'current_count': 14, 'baseline_count': 1, 'delta': 13} (+17 more)
  - `grounding.origin_error_count` → 3

## [WARNING] `ontology_planning` / `new_surface_token_count`

- value: **48**  (from `<search recursive metrics JSON for key `new_surface_token_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → available_for_trading_by_market_participants; datavendor; financialinstrument (+18 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; available_for_trading_by_market_participants; canonical (+38 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'share', 'current_count': 19, 'baseline_count': 2, 'delta': 17}; {'token': 'float', 'current_count': 14, 'baseline_count': 1, 'delta': 13}; {'token': 'free', 'current_count': 14, 'baseline_count': 1, 'delta': 13} (+17 more)
  - `grounding.origin_error_count` → 3

## [WARNING] `ontology_planning` / `ungrounded_sort_count`

- value: **1**  (from `grounding.ungrounded_sort_count`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → available_for_trading_by_market_participants; datavendor; financialinstrument (+18 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; available_for_trading_by_market_participants; canonical (+38 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'share', 'current_count': 19, 'baseline_count': 2, 'delta': 17}; {'token': 'float', 'current_count': 14, 'baseline_count': 1, 'delta': 13}; {'token': 'free', 'current_count': 14, 'baseline_count': 1, 'delta': 13} (+17 more)
  - `grounding.origin_error_count` → 3

## [WARNING] `ontology_planning` / `ungrounded_symbol_count`

- value: **2**  (from `grounding.ungrounded_symbol_count`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → available_for_trading_by_market_participants; datavendor; financialinstrument (+18 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; available_for_trading_by_market_participants; canonical (+38 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'share', 'current_count': 19, 'baseline_count': 2, 'delta': 17}; {'token': 'float', 'current_count': 14, 'baseline_count': 1, 'delta': 13}; {'token': 'free', 'current_count': 14, 'baseline_count': 1, 'delta': 13} (+17 more)
  - `grounding.origin_error_count` → 3
