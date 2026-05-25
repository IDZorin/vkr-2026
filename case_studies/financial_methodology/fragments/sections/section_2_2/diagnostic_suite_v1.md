# Diagnostic report — section_2_2

- **gate**: `needs_review`
- fail: 0, warning: 29

## [WARNING] `merge_canonicalization` / `callable_symbol_count`

- value: **12**  (from `parameterization.callable_symbol_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 12
  - `<related section in metrics JSON>` → 12

## [WARNING] `merge_canonicalization` / `callable_symbol_with_args_count`

- value: **12**  (from `parameterization.callable_symbol_with_args_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 12
  - `<related section in metrics JSON>` → 12

## [WARNING] `merge_canonicalization` / `dependency_link_count`

- value: **5**  (from `<search recursive metrics JSON for key `dependency_link_count`>`)
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

- value: **12**  (from `parameterization.factorization_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 12
  - `<related section in metrics JSON>` → 12

## [WARNING] `merge_canonicalization` / `focus_signature_unique_count`

- value: **1**  (from `variability.focus_signature_unique_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.

## [WARNING] `merge_canonicalization` / `quantifier_parameter_slot_count`

- value: **22**  (from `parameterization.quantifier_parameter_slot_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `assertion_complexity.top_complex_assertions` → descending_order_by_free_float_market_capizatlization; americas_country_assignment_classification; europe_country_assignment_classification (+7 more)
  - `assertion_complexity.max_assertion_depth` → 9
  - `assertion_complexity.total_quantifier_count` → 22

## [WARNING] `merge_canonicalization` / `top_level_parameter_slot_count`

- value: **23**  (from `parameterization.top_level_parameter_slot_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 23
  - `<related section in metrics JSON>` → 23

## [WARNING] `merge_canonicalization` / `total_parameter_slot_mass`

- value: **45**  (from `parameterization.total_parameter_slot_mass`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 45
  - `<related section in metrics JSON>` → 45

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

- value: **16**  (from `identifier_glue.compound_identifier_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'less_than_20_per_region_less_than_40_index_components', 'raw_pie; {'identifier': 'ordinary_rebalance_selection_determined_by_index_component_requi; {'identifier': 'initial_composition_determined_by_index_component_requirements', (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'SelectionOfIndexComponents', 'raw_piece_count': 4, 'content_piec; {'identifier': 'index_components_selected_for_index_inclusion', 'raw_piece_count; {'identifier': 'index_component', 'raw_piece_count': 2, 'content_piece_count': 2 (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'initial_composition_determined_by_index_component_requirements',; {'identifier': 'ordinary_rebalance_selection_determined_by_index_component_requi

## [WARNING] `ontology_planning` / `compound_identifier_count_raw`

- value: **13**  (from `identifier_glue.compound_identifier_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'less_than_20_per_region_less_than_40_index_components', 'raw_pie; {'identifier': 'ordinary_rebalance_selection_determined_by_index_component_requi; {'identifier': 'initial_composition_determined_by_index_component_requirements', (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'SelectionOfIndexComponents', 'raw_piece_count': 4, 'content_piec; {'identifier': 'index_components_selected_for_index_inclusion', 'raw_piece_count; {'identifier': 'index_component', 'raw_piece_count': 2, 'content_piece_count': 2 (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'initial_composition_determined_by_index_component_requirements',; {'identifier': 'ordinary_rebalance_selection_determined_by_index_component_requi

## [WARNING] `ontology_planning` / `dependency_link_count`

- value: **5**  (from `<search recursive metrics JSON for key `dependency_link_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 5
  - `<related section in metrics JSON>` → 5

## [WARNING] `ontology_planning` / `identifier_count`

- value: **37**  (from `identifier_glue.identifier_count`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'less_than_20_per_region_less_than_40_index_components', 'raw_pie; {'identifier': 'ordinary_rebalance_selection_determined_by_index_component_requi; {'identifier': 'initial_composition_determined_by_index_component_requirements', (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'SelectionOfIndexComponents', 'raw_piece_count': 4, 'content_piec; {'identifier': 'index_components_selected_for_index_inclusion', 'raw_piece_count; {'identifier': 'index_component', 'raw_piece_count': 2, 'content_piece_count': 2 (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'initial_composition_determined_by_index_component_requirements',; {'identifier': 'ordinary_rebalance_selection_determined_by_index_component_requi

## [WARNING] `ontology_planning` / `identifier_glue_excess_mass_content`

- value: **40**  (from `identifier_glue.identifier_glue_excess_mass_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'less_than_20_per_region_less_than_40_index_components', 'raw_pie; {'identifier': 'ordinary_rebalance_selection_determined_by_index_component_requi; {'identifier': 'initial_composition_determined_by_index_component_requirements', (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'SelectionOfIndexComponents', 'raw_piece_count': 4, 'content_piec; {'identifier': 'index_components_selected_for_index_inclusion', 'raw_piece_count; {'identifier': 'index_component', 'raw_piece_count': 2, 'content_piece_count': 2 (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'initial_composition_determined_by_index_component_requirements',; {'identifier': 'ordinary_rebalance_selection_determined_by_index_component_requi

## [WARNING] `ontology_planning` / `identifier_glue_excess_mass_raw`

- value: **39**  (from `identifier_glue.identifier_glue_excess_mass_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'less_than_20_per_region_less_than_40_index_components', 'raw_pie; {'identifier': 'ordinary_rebalance_selection_determined_by_index_component_requi; {'identifier': 'initial_composition_determined_by_index_component_requirements', (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'SelectionOfIndexComponents', 'raw_piece_count': 4, 'content_piec; {'identifier': 'index_components_selected_for_index_inclusion', 'raw_piece_count; {'identifier': 'index_component', 'raw_piece_count': 2, 'content_piece_count': 2 (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'initial_composition_determined_by_index_component_requirements',; {'identifier': 'ordinary_rebalance_selection_determined_by_index_component_requi

## [WARNING] `ontology_planning` / `low_source_grounded_glued_identifier_count`

- value: **5**  (from `identifier_glue.low_source_grounded_glued_identifier_count`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'less_than_20_per_region_less_than_40_index_components', 'raw_pie; {'identifier': 'ordinary_rebalance_selection_determined_by_index_component_requi; {'identifier': 'initial_composition_determined_by_index_component_requirements', (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'SelectionOfIndexComponents', 'raw_piece_count': 4, 'content_piec; {'identifier': 'index_components_selected_for_index_inclusion', 'raw_piece_count; {'identifier': 'index_component', 'raw_piece_count': 2, 'content_piece_count': 2 (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'initial_composition_determined_by_index_component_requirements',; {'identifier': 'ordinary_rebalance_selection_determined_by_index_component_requi

## [WARNING] `ontology_planning` / `max_identifier_piece_count_content`

- value: **8**  (from `identifier_glue.max_identifier_piece_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'less_than_20_per_region_less_than_40_index_components', 'raw_pie; {'identifier': 'ordinary_rebalance_selection_determined_by_index_component_requi; {'identifier': 'initial_composition_determined_by_index_component_requirements', (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'SelectionOfIndexComponents', 'raw_piece_count': 4, 'content_piec; {'identifier': 'index_components_selected_for_index_inclusion', 'raw_piece_count; {'identifier': 'index_component', 'raw_piece_count': 2, 'content_piece_count': 2 (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'initial_composition_determined_by_index_component_requirements',; {'identifier': 'ordinary_rebalance_selection_determined_by_index_component_requi

## [WARNING] `ontology_planning` / `max_identifier_piece_count_raw`

- value: **10**  (from `identifier_glue.max_identifier_piece_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'less_than_20_per_region_less_than_40_index_components', 'raw_pie; {'identifier': 'ordinary_rebalance_selection_determined_by_index_component_requi; {'identifier': 'initial_composition_determined_by_index_component_requirements', (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'SelectionOfIndexComponents', 'raw_piece_count': 4, 'content_piec; {'identifier': 'index_components_selected_for_index_inclusion', 'raw_piece_count; {'identifier': 'index_component', 'raw_piece_count': 2, 'content_piece_count': 2 (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'initial_composition_determined_by_index_component_requirements',; {'identifier': 'ordinary_rebalance_selection_determined_by_index_component_requi

## [WARNING] `ontology_planning` / `mean_identifier_piece_count_content`

- value: **2.6216216216216215**  (from `identifier_glue.mean_identifier_piece_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'less_than_20_per_region_less_than_40_index_components', 'raw_pie; {'identifier': 'ordinary_rebalance_selection_determined_by_index_component_requi; {'identifier': 'initial_composition_determined_by_index_component_requirements', (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'SelectionOfIndexComponents', 'raw_piece_count': 4, 'content_piec; {'identifier': 'index_components_selected_for_index_inclusion', 'raw_piece_count; {'identifier': 'index_component', 'raw_piece_count': 2, 'content_piece_count': 2 (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'initial_composition_determined_by_index_component_requirements',; {'identifier': 'ordinary_rebalance_selection_determined_by_index_component_requi

## [WARNING] `ontology_planning` / `mean_identifier_piece_count_raw`

- value: **3.1621621621621623**  (from `identifier_glue.mean_identifier_piece_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'less_than_20_per_region_less_than_40_index_components', 'raw_pie; {'identifier': 'ordinary_rebalance_selection_determined_by_index_component_requi; {'identifier': 'initial_composition_determined_by_index_component_requirements', (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'SelectionOfIndexComponents', 'raw_piece_count': 4, 'content_piec; {'identifier': 'index_components_selected_for_index_inclusion', 'raw_piece_count; {'identifier': 'index_component', 'raw_piece_count': 2, 'content_piece_count': 2 (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'initial_composition_determined_by_index_component_requirements',; {'identifier': 'ordinary_rebalance_selection_determined_by_index_component_requi

## [WARNING] `ontology_planning` / `new_formula_content_token_count_vs_text_only`

- value: **35**  (from `grounding.new_formula_content_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → americas_country_assignment_classification; countryassignment; descending_order_by_free_float_market_capizatlization (+32 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; americas_country_assignment_classification; canonical (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'selectionday', 'current_count': 23, 'baseline_count': 0, 'delta': 23}; {'token': 'security', 'current_count': 24, 'baseline_count': 2, 'delta': 22}; {'token': 'region', 'current_count': 18, 'baseline_count': 2, 'delta': 16} (+17 more)
  - `grounding.origin_error_count` → 0

## [WARNING] `ontology_planning` / `new_formula_token_count_vs_text_only`

- value: **40**  (from `grounding.new_formula_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → americas_country_assignment_classification; countryassignment; descending_order_by_free_float_market_capizatlization (+32 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; americas_country_assignment_classification; canonical (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'selectionday', 'current_count': 23, 'baseline_count': 0, 'delta': 23}; {'token': 'security', 'current_count': 24, 'baseline_count': 2, 'delta': 22}; {'token': 'region', 'current_count': 18, 'baseline_count': 2, 'delta': 16} (+17 more)
  - `grounding.origin_error_count` → 0

## [WARNING] `ontology_planning` / `new_full_surface_content_token_count_vs_text_only`

- value: **55**  (from `grounding.new_full_surface_content_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → americas_country_assignment_classification; countryassignment; descending_order_by_free_float_market_capizatlization (+32 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; americas_country_assignment_classification; canonical (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'selectionday', 'current_count': 23, 'baseline_count': 0, 'delta': 23}; {'token': 'security', 'current_count': 24, 'baseline_count': 2, 'delta': 22}; {'token': 'region', 'current_count': 18, 'baseline_count': 2, 'delta': 16} (+17 more)
  - `grounding.origin_error_count` → 0

## [WARNING] `ontology_planning` / `new_full_surface_token_count_vs_text_only`

- value: **63**  (from `grounding.new_full_surface_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → americas_country_assignment_classification; countryassignment; descending_order_by_free_float_market_capizatlization (+32 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; americas_country_assignment_classification; canonical (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'selectionday', 'current_count': 23, 'baseline_count': 0, 'delta': 23}; {'token': 'security', 'current_count': 24, 'baseline_count': 2, 'delta': 22}; {'token': 'region', 'current_count': 18, 'baseline_count': 2, 'delta': 16} (+17 more)
  - `grounding.origin_error_count` → 0

## [WARNING] `ontology_planning` / `new_surface_content_token_count`

- value: **117**  (from `<search recursive metrics JSON for key `new_surface_content_token_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → americas_country_assignment_classification; countryassignment; descending_order_by_free_float_market_capizatlization (+32 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; americas_country_assignment_classification; canonical (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'selectionday', 'current_count': 23, 'baseline_count': 0, 'delta': 23}; {'token': 'security', 'current_count': 24, 'baseline_count': 2, 'delta': 22}; {'token': 'region', 'current_count': 18, 'baseline_count': 2, 'delta': 16} (+17 more)
  - `grounding.origin_error_count` → 0

## [WARNING] `ontology_planning` / `new_surface_token_count`

- value: **117**  (from `<search recursive metrics JSON for key `new_surface_token_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → americas_country_assignment_classification; countryassignment; descending_order_by_free_float_market_capizatlization (+32 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; americas_country_assignment_classification; canonical (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'selectionday', 'current_count': 23, 'baseline_count': 0, 'delta': 23}; {'token': 'security', 'current_count': 24, 'baseline_count': 2, 'delta': 22}; {'token': 'region', 'current_count': 18, 'baseline_count': 2, 'delta': 16} (+17 more)
  - `grounding.origin_error_count` → 0
