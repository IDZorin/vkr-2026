# Diagnostic report — section_2_3

- **gate**: `needs_review`
- fail: 0, warning: 31

## [WARNING] `merge_canonicalization` / `callable_symbol_count`

- value: **7**  (from `parameterization.callable_symbol_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 7
  - `<related section in metrics JSON>` → 7

## [WARNING] `merge_canonicalization` / `callable_symbol_with_args_count`

- value: **7**  (from `parameterization.callable_symbol_with_args_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 7
  - `<related section in metrics JSON>` → 7

## [WARNING] `merge_canonicalization` / `draft_variant_count`

- value: **1**  (from `variants.draft_variant_count`)
- meaning: A merge/variant/gold comparison changed structure or semantics; report exact compared variants or merge rows.
- repair: Use overlay/bridge/conflict split or reject rewrite based on backtest.

## [WARNING] `merge_canonicalization` / `factorization_count`

- value: **7**  (from `parameterization.factorization_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 7
  - `<related section in metrics JSON>` → 7

## [WARNING] `merge_canonicalization` / `focus_signature_unique_count`

- value: **1**  (from `variability.focus_signature_unique_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.

## [WARNING] `merge_canonicalization` / `quantifier_parameter_slot_count`

- value: **4**  (from `parameterization.quantifier_parameter_slot_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `assertion_complexity.top_complex_assertions` → region_represents_exactly_50_percent; single_index_component_weight_capped
  - `assertion_complexity.max_assertion_depth` → 6
  - `assertion_complexity.total_quantifier_count` → 4

## [WARNING] `merge_canonicalization` / `top_level_parameter_slot_count`

- value: **12**  (from `parameterization.top_level_parameter_slot_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 12
  - `<related section in metrics JSON>` → 12

## [WARNING] `merge_canonicalization` / `total_parameter_slot_mass`

- value: **16**  (from `parameterization.total_parameter_slot_mass`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 16
  - `<related section in metrics JSON>` → 16

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
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'weight_has_float_market_capizatlization_basis', 'raw_piece_count; {'identifier': 'single_index_component_weight_capped', 'raw_piece_count': 5, 'co; {'identifier': 'region_represents_exactly_50_percent', 'raw_piece_count': 5, 'co (+14 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'region_represents_exactly_50_percent', 'raw_piece_count': 5, 'co; {'identifier': 'IndexComponent', 'raw_piece_count': 2, 'content_piece_count': 2,; {'identifier': 'weight_has_float_market_capizatlization_basis', 'raw_piece_count (+6 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `compound_identifier_count_raw`

- value: **3**  (from `identifier_glue.compound_identifier_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'weight_has_float_market_capizatlization_basis', 'raw_piece_count; {'identifier': 'single_index_component_weight_capped', 'raw_piece_count': 5, 'co; {'identifier': 'region_represents_exactly_50_percent', 'raw_piece_count': 5, 'co (+14 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'region_represents_exactly_50_percent', 'raw_piece_count': 5, 'co; {'identifier': 'IndexComponent', 'raw_piece_count': 2, 'content_piece_count': 2,; {'identifier': 'weight_has_float_market_capizatlization_basis', 'raw_piece_count (+6 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `identifier_count`

- value: **17**  (from `identifier_glue.identifier_count`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'weight_has_float_market_capizatlization_basis', 'raw_piece_count; {'identifier': 'single_index_component_weight_capped', 'raw_piece_count': 5, 'co; {'identifier': 'region_represents_exactly_50_percent', 'raw_piece_count': 5, 'co (+14 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'region_represents_exactly_50_percent', 'raw_piece_count': 5, 'co; {'identifier': 'IndexComponent', 'raw_piece_count': 2, 'content_piece_count': 2,; {'identifier': 'weight_has_float_market_capizatlization_basis', 'raw_piece_count (+6 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `identifier_glue_excess_mass_content`

- value: **11**  (from `identifier_glue.identifier_glue_excess_mass_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'weight_has_float_market_capizatlization_basis', 'raw_piece_count; {'identifier': 'single_index_component_weight_capped', 'raw_piece_count': 5, 'co; {'identifier': 'region_represents_exactly_50_percent', 'raw_piece_count': 5, 'co (+14 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'region_represents_exactly_50_percent', 'raw_piece_count': 5, 'co; {'identifier': 'IndexComponent', 'raw_piece_count': 2, 'content_piece_count': 2,; {'identifier': 'weight_has_float_market_capizatlization_basis', 'raw_piece_count (+6 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `identifier_glue_excess_mass_raw`

- value: **7**  (from `identifier_glue.identifier_glue_excess_mass_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'weight_has_float_market_capizatlization_basis', 'raw_piece_count; {'identifier': 'single_index_component_weight_capped', 'raw_piece_count': 5, 'co; {'identifier': 'region_represents_exactly_50_percent', 'raw_piece_count': 5, 'co (+14 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'region_represents_exactly_50_percent', 'raw_piece_count': 5, 'co; {'identifier': 'IndexComponent', 'raw_piece_count': 2, 'content_piece_count': 2,; {'identifier': 'weight_has_float_market_capizatlization_basis', 'raw_piece_count (+6 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `low_source_grounded_glued_identifier_count`

- value: **4**  (from `identifier_glue.low_source_grounded_glued_identifier_count`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'weight_has_float_market_capizatlization_basis', 'raw_piece_count; {'identifier': 'single_index_component_weight_capped', 'raw_piece_count': 5, 'co; {'identifier': 'region_represents_exactly_50_percent', 'raw_piece_count': 5, 'co (+14 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'region_represents_exactly_50_percent', 'raw_piece_count': 5, 'co; {'identifier': 'IndexComponent', 'raw_piece_count': 2, 'content_piece_count': 2,; {'identifier': 'weight_has_float_market_capizatlization_basis', 'raw_piece_count (+6 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `max_identifier_piece_count_content`

- value: **6**  (from `identifier_glue.max_identifier_piece_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'weight_has_float_market_capizatlization_basis', 'raw_piece_count; {'identifier': 'single_index_component_weight_capped', 'raw_piece_count': 5, 'co; {'identifier': 'region_represents_exactly_50_percent', 'raw_piece_count': 5, 'co (+14 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'region_represents_exactly_50_percent', 'raw_piece_count': 5, 'co; {'identifier': 'IndexComponent', 'raw_piece_count': 2, 'content_piece_count': 2,; {'identifier': 'weight_has_float_market_capizatlization_basis', 'raw_piece_count (+6 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `max_identifier_piece_count_raw`

- value: **6**  (from `identifier_glue.max_identifier_piece_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'weight_has_float_market_capizatlization_basis', 'raw_piece_count; {'identifier': 'single_index_component_weight_capped', 'raw_piece_count': 5, 'co; {'identifier': 'region_represents_exactly_50_percent', 'raw_piece_count': 5, 'co (+14 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'region_represents_exactly_50_percent', 'raw_piece_count': 5, 'co; {'identifier': 'IndexComponent', 'raw_piece_count': 2, 'content_piece_count': 2,; {'identifier': 'weight_has_float_market_capizatlization_basis', 'raw_piece_count (+6 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `mean_identifier_piece_count_content`

- value: **1.9411764705882353**  (from `identifier_glue.mean_identifier_piece_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'weight_has_float_market_capizatlization_basis', 'raw_piece_count; {'identifier': 'single_index_component_weight_capped', 'raw_piece_count': 5, 'co; {'identifier': 'region_represents_exactly_50_percent', 'raw_piece_count': 5, 'co (+14 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'region_represents_exactly_50_percent', 'raw_piece_count': 5, 'co; {'identifier': 'IndexComponent', 'raw_piece_count': 2, 'content_piece_count': 2,; {'identifier': 'weight_has_float_market_capizatlization_basis', 'raw_piece_count (+6 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `mean_identifier_piece_count_raw`

- value: **2.2941176470588234**  (from `identifier_glue.mean_identifier_piece_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'weight_has_float_market_capizatlization_basis', 'raw_piece_count; {'identifier': 'single_index_component_weight_capped', 'raw_piece_count': 5, 'co; {'identifier': 'region_represents_exactly_50_percent', 'raw_piece_count': 5, 'co (+14 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'region_represents_exactly_50_percent', 'raw_piece_count': 5, 'co; {'identifier': 'IndexComponent', 'raw_piece_count': 2, 'content_piece_count': 2,; {'identifier': 'weight_has_float_market_capizatlization_basis', 'raw_piece_count (+6 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `new_formula_content_token_count_vs_text_only`

- value: **16**  (from `grounding.new_formula_content_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → float_market_capizatlization; floatmarketcapizatlization; indexcomponent (+13 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; canonical; computation (+33 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'weight', 'current_count': 15, 'baseline_count': 2, 'delta': 13}; {'token': 'indexcomponent', 'current_count': 9, 'baseline_count': 0, 'delta': 9}; {'token': 'selectionday', 'current_count': 9, 'baseline_count': 0, 'delta': 9} (+15 more)
  - `grounding.origin_error_count` → 6

## [WARNING] `ontology_planning` / `new_formula_token_count_vs_text_only`

- value: **20**  (from `grounding.new_formula_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → float_market_capizatlization; floatmarketcapizatlization; indexcomponent (+13 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; canonical; computation (+33 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'weight', 'current_count': 15, 'baseline_count': 2, 'delta': 13}; {'token': 'indexcomponent', 'current_count': 9, 'baseline_count': 0, 'delta': 9}; {'token': 'selectionday', 'current_count': 9, 'baseline_count': 0, 'delta': 9} (+15 more)
  - `grounding.origin_error_count` → 6

## [WARNING] `ontology_planning` / `new_full_surface_content_token_count_vs_text_only`

- value: **36**  (from `grounding.new_full_surface_content_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → float_market_capizatlization; floatmarketcapizatlization; indexcomponent (+13 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; canonical; computation (+33 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'weight', 'current_count': 15, 'baseline_count': 2, 'delta': 13}; {'token': 'indexcomponent', 'current_count': 9, 'baseline_count': 0, 'delta': 9}; {'token': 'selectionday', 'current_count': 9, 'baseline_count': 0, 'delta': 9} (+15 more)
  - `grounding.origin_error_count` → 6

## [WARNING] `ontology_planning` / `new_full_surface_token_count_vs_text_only`

- value: **44**  (from `grounding.new_full_surface_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → float_market_capizatlization; floatmarketcapizatlization; indexcomponent (+13 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; canonical; computation (+33 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'weight', 'current_count': 15, 'baseline_count': 2, 'delta': 13}; {'token': 'indexcomponent', 'current_count': 9, 'baseline_count': 0, 'delta': 9}; {'token': 'selectionday', 'current_count': 9, 'baseline_count': 0, 'delta': 9} (+15 more)
  - `grounding.origin_error_count` → 6

## [WARNING] `ontology_planning` / `new_surface_content_token_count`

- value: **50**  (from `<search recursive metrics JSON for key `new_surface_content_token_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → float_market_capizatlization; floatmarketcapizatlization; indexcomponent (+13 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; canonical; computation (+33 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'weight', 'current_count': 15, 'baseline_count': 2, 'delta': 13}; {'token': 'indexcomponent', 'current_count': 9, 'baseline_count': 0, 'delta': 9}; {'token': 'selectionday', 'current_count': 9, 'baseline_count': 0, 'delta': 9} (+15 more)
  - `grounding.origin_error_count` → 6

## [WARNING] `ontology_planning` / `new_surface_token_count`

- value: **50**  (from `<search recursive metrics JSON for key `new_surface_token_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → float_market_capizatlization; floatmarketcapizatlization; indexcomponent (+13 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; canonical; computation (+33 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'weight', 'current_count': 15, 'baseline_count': 2, 'delta': 13}; {'token': 'indexcomponent', 'current_count': 9, 'baseline_count': 0, 'delta': 9}; {'token': 'selectionday', 'current_count': 9, 'baseline_count': 0, 'delta': 9} (+15 more)
  - `grounding.origin_error_count` → 6

## [WARNING] `ontology_planning` / `ungrounded_callee_count`

- value: **1**  (from `grounding.ungrounded_callee_count`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → float_market_capizatlization; floatmarketcapizatlization; indexcomponent (+13 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; canonical; computation (+33 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'weight', 'current_count': 15, 'baseline_count': 2, 'delta': 13}; {'token': 'indexcomponent', 'current_count': 9, 'baseline_count': 0, 'delta': 9}; {'token': 'selectionday', 'current_count': 9, 'baseline_count': 0, 'delta': 9} (+15 more)
  - `grounding.origin_error_count` → 6

## [WARNING] `ontology_planning` / `ungrounded_ref_count`

- value: **1**  (from `grounding.ungrounded_ref_count`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → float_market_capizatlization; floatmarketcapizatlization; indexcomponent (+13 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; canonical; computation (+33 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'weight', 'current_count': 15, 'baseline_count': 2, 'delta': 13}; {'token': 'indexcomponent', 'current_count': 9, 'baseline_count': 0, 'delta': 9}; {'token': 'selectionday', 'current_count': 9, 'baseline_count': 0, 'delta': 9} (+15 more)
  - `grounding.origin_error_count` → 6

## [WARNING] `ontology_planning` / `ungrounded_sort_count`

- value: **3**  (from `grounding.ungrounded_sort_count`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → float_market_capizatlization; floatmarketcapizatlization; indexcomponent (+13 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; canonical; computation (+33 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'weight', 'current_count': 15, 'baseline_count': 2, 'delta': 13}; {'token': 'indexcomponent', 'current_count': 9, 'baseline_count': 0, 'delta': 9}; {'token': 'selectionday', 'current_count': 9, 'baseline_count': 0, 'delta': 9} (+15 more)
  - `grounding.origin_error_count` → 6

## [WARNING] `ontology_planning` / `ungrounded_symbol_count`

- value: **2**  (from `grounding.ungrounded_symbol_count`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → float_market_capizatlization; floatmarketcapizatlization; indexcomponent (+13 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; canonical; computation (+33 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'weight', 'current_count': 15, 'baseline_count': 2, 'delta': 13}; {'token': 'indexcomponent', 'current_count': 9, 'baseline_count': 0, 'delta': 9}; {'token': 'selectionday', 'current_count': 9, 'baseline_count': 0, 'delta': 9} (+15 more)
  - `grounding.origin_error_count` → 6
