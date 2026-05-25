# Diagnostic report — section_4_5

- **gate**: `needs_review`
- fail: 0, warning: 35

## [WARNING] `merge_canonicalization` / `callable_symbol_count`

- value: **35**  (from `parameterization.callable_symbol_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 35
  - `<related section in metrics JSON>` → 35

## [WARNING] `merge_canonicalization` / `callable_symbol_with_args_count`

- value: **35**  (from `parameterization.callable_symbol_with_args_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 35
  - `<related section in metrics JSON>` → 35

## [WARNING] `merge_canonicalization` / `cross_reference_dropout_count`

- value: **1**  (from `<search recursive metrics JSON for key `cross_reference_dropout_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `evidence.source_cross_references` → Section 4.5
  - `evidence.ir_cross_references` → entity EquityIndexMethodology : Document

## [WARNING] `merge_canonicalization` / `cross_reference_usage_count`

- value: **1**  (from `<search recursive metrics JSON for key `cross_reference_usage_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `evidence.ir_cross_references` → entity EquityIndexMethodology : Document

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

- value: **35**  (from `parameterization.factorization_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 35
  - `<related section in metrics JSON>` → 35

## [WARNING] `merge_canonicalization` / `focus_signature_unique_count`

- value: **1**  (from `variability.focus_signature_unique_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.

## [WARNING] `merge_canonicalization` / `quantifier_parameter_slot_count`

- value: **13**  (from `parameterization.quantifier_parameter_slot_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `assertion_complexity.top_complex_assertions` → corporate_action_deviation_conditions; considered_corporate_actions_result_in_index_adjustment; equity_index_methodology_material_for_covered_corporate_actions (+3 more)
  - `assertion_complexity.max_assertion_depth` → 9
  - `assertion_complexity.total_quantifier_count` → 13

## [WARNING] `merge_canonicalization` / `top_level_parameter_slot_count`

- value: **70**  (from `parameterization.top_level_parameter_slot_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 70
  - `<related section in metrics JSON>` → 70

## [WARNING] `merge_canonicalization` / `total_parameter_slot_mass`

- value: **83**  (from `parameterization.total_parameter_slot_mass`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 83
  - `<related section in metrics JSON>` → 83

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

- value: **28**  (from `identifier_glue.compound_identifier_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'equity_index_methodology_material_for_covered_corporate_actions'; {'identifier': 'considered_corporate_actions_result_in_index_adjustment', 'raw_p; {'identifier': 'methodology_specifies_relevant_adjustment_to_index_variable', 'r (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'ListedCorporateActionKind', 'raw_piece_count': 4, 'content_piece; {'identifier': 'SpinOffs', 'raw_piece_count': 2, 'content_piece_count': 2, 'raw_; {'identifier': 'VagueTerm', 'raw_piece_count': 2, 'content_piece_count': 2, 'raw (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'non_conclusive_means_not_conclusive', 'raw_piece_count': 5, 'con
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `compound_identifier_count_raw`

- value: **27**  (from `identifier_glue.compound_identifier_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'equity_index_methodology_material_for_covered_corporate_actions'; {'identifier': 'considered_corporate_actions_result_in_index_adjustment', 'raw_p; {'identifier': 'methodology_specifies_relevant_adjustment_to_index_variable', 'r (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'ListedCorporateActionKind', 'raw_piece_count': 4, 'content_piece; {'identifier': 'SpinOffs', 'raw_piece_count': 2, 'content_piece_count': 2, 'raw_; {'identifier': 'VagueTerm', 'raw_piece_count': 2, 'content_piece_count': 2, 'raw (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'non_conclusive_means_not_conclusive', 'raw_piece_count': 5, 'con
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `cross_reference_dropout_count`

- value: **1**  (from `<search recursive metrics JSON for key `cross_reference_dropout_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `evidence.source_cross_references` → Section 4.5
  - `evidence.ir_cross_references` → entity EquityIndexMethodology : Document

## [WARNING] `ontology_planning` / `cross_reference_usage_count`

- value: **1**  (from `<search recursive metrics JSON for key `cross_reference_usage_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `evidence.ir_cross_references` → entity EquityIndexMethodology : Document

## [WARNING] `ontology_planning` / `dependency_link_count`

- value: **4**  (from `<search recursive metrics JSON for key `dependency_link_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 4
  - `<related section in metrics JSON>` → 4

## [WARNING] `ontology_planning` / `identifier_count`

- value: **100**  (from `identifier_glue.identifier_count`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'equity_index_methodology_material_for_covered_corporate_actions'; {'identifier': 'considered_corporate_actions_result_in_index_adjustment', 'raw_p; {'identifier': 'methodology_specifies_relevant_adjustment_to_index_variable', 'r (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'ListedCorporateActionKind', 'raw_piece_count': 4, 'content_piece; {'identifier': 'SpinOffs', 'raw_piece_count': 2, 'content_piece_count': 2, 'raw_; {'identifier': 'VagueTerm', 'raw_piece_count': 2, 'content_piece_count': 2, 'raw (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'non_conclusive_means_not_conclusive', 'raw_piece_count': 5, 'con
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `identifier_glue_excess_mass_content`

- value: **52**  (from `identifier_glue.identifier_glue_excess_mass_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'equity_index_methodology_material_for_covered_corporate_actions'; {'identifier': 'considered_corporate_actions_result_in_index_adjustment', 'raw_p; {'identifier': 'methodology_specifies_relevant_adjustment_to_index_variable', 'r (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'ListedCorporateActionKind', 'raw_piece_count': 4, 'content_piece; {'identifier': 'SpinOffs', 'raw_piece_count': 2, 'content_piece_count': 2, 'raw_; {'identifier': 'VagueTerm', 'raw_piece_count': 2, 'content_piece_count': 2, 'raw (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'non_conclusive_means_not_conclusive', 'raw_piece_count': 5, 'con
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `identifier_glue_excess_mass_raw`

- value: **55**  (from `identifier_glue.identifier_glue_excess_mass_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'equity_index_methodology_material_for_covered_corporate_actions'; {'identifier': 'considered_corporate_actions_result_in_index_adjustment', 'raw_p; {'identifier': 'methodology_specifies_relevant_adjustment_to_index_variable', 'r (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'ListedCorporateActionKind', 'raw_piece_count': 4, 'content_piece; {'identifier': 'SpinOffs', 'raw_piece_count': 2, 'content_piece_count': 2, 'raw_; {'identifier': 'VagueTerm', 'raw_piece_count': 2, 'content_piece_count': 2, 'raw (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'non_conclusive_means_not_conclusive', 'raw_piece_count': 5, 'con
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `low_source_grounded_glued_identifier_count`

- value: **16**  (from `identifier_glue.low_source_grounded_glued_identifier_count`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'equity_index_methodology_material_for_covered_corporate_actions'; {'identifier': 'considered_corporate_actions_result_in_index_adjustment', 'raw_p; {'identifier': 'methodology_specifies_relevant_adjustment_to_index_variable', 'r (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'ListedCorporateActionKind', 'raw_piece_count': 4, 'content_piece; {'identifier': 'SpinOffs', 'raw_piece_count': 2, 'content_piece_count': 2, 'raw_; {'identifier': 'VagueTerm', 'raw_piece_count': 2, 'content_piece_count': 2, 'raw (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'non_conclusive_means_not_conclusive', 'raw_piece_count': 5, 'con
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `max_identifier_piece_count_content`

- value: **7**  (from `identifier_glue.max_identifier_piece_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'equity_index_methodology_material_for_covered_corporate_actions'; {'identifier': 'considered_corporate_actions_result_in_index_adjustment', 'raw_p; {'identifier': 'methodology_specifies_relevant_adjustment_to_index_variable', 'r (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'ListedCorporateActionKind', 'raw_piece_count': 4, 'content_piece; {'identifier': 'SpinOffs', 'raw_piece_count': 2, 'content_piece_count': 2, 'raw_; {'identifier': 'VagueTerm', 'raw_piece_count': 2, 'content_piece_count': 2, 'raw (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'non_conclusive_means_not_conclusive', 'raw_piece_count': 5, 'con
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `max_identifier_piece_count_raw`

- value: **8**  (from `identifier_glue.max_identifier_piece_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'equity_index_methodology_material_for_covered_corporate_actions'; {'identifier': 'considered_corporate_actions_result_in_index_adjustment', 'raw_p; {'identifier': 'methodology_specifies_relevant_adjustment_to_index_variable', 'r (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'ListedCorporateActionKind', 'raw_piece_count': 4, 'content_piece; {'identifier': 'SpinOffs', 'raw_piece_count': 2, 'content_piece_count': 2, 'raw_; {'identifier': 'VagueTerm', 'raw_piece_count': 2, 'content_piece_count': 2, 'raw (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'non_conclusive_means_not_conclusive', 'raw_piece_count': 5, 'con
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `mean_identifier_piece_count_content`

- value: **2.1**  (from `identifier_glue.mean_identifier_piece_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'equity_index_methodology_material_for_covered_corporate_actions'; {'identifier': 'considered_corporate_actions_result_in_index_adjustment', 'raw_p; {'identifier': 'methodology_specifies_relevant_adjustment_to_index_variable', 'r (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'ListedCorporateActionKind', 'raw_piece_count': 4, 'content_piece; {'identifier': 'SpinOffs', 'raw_piece_count': 2, 'content_piece_count': 2, 'raw_; {'identifier': 'VagueTerm', 'raw_piece_count': 2, 'content_piece_count': 2, 'raw (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'non_conclusive_means_not_conclusive', 'raw_piece_count': 5, 'con
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `mean_identifier_piece_count_raw`

- value: **2.81**  (from `identifier_glue.mean_identifier_piece_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'equity_index_methodology_material_for_covered_corporate_actions'; {'identifier': 'considered_corporate_actions_result_in_index_adjustment', 'raw_p; {'identifier': 'methodology_specifies_relevant_adjustment_to_index_variable', 'r (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'ListedCorporateActionKind', 'raw_piece_count': 4, 'content_piece; {'identifier': 'SpinOffs', 'raw_piece_count': 2, 'content_piece_count': 2, 'raw_; {'identifier': 'VagueTerm', 'raw_piece_count': 2, 'content_piece_count': 2, 'raw (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'non_conclusive_means_not_conclusive', 'raw_piece_count': 5, 'con
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `new_formula_content_token_count_vs_text_only`

- value: **95**  (from `grounding.new_formula_content_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → account_for; account_for_corporate_action_in_index_calculation; adjustment_between_regular_rebalance_days (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; account_for; account_for_corporate_action_in_index_calculation (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'index', 'current_count': 51, 'baseline_count': 11, 'delta': 40}; {'token': 'methodology', 'current_count': 34, 'baseline_count': 3, 'delta': 31}; {'token': 'equityindexmethodology', 'current_count': 29, 'baseline_count': 0, 'd (+17 more)
  - `grounding.origin_error_count` → 20

## [WARNING] `ontology_planning` / `new_formula_token_count_vs_text_only`

- value: **104**  (from `grounding.new_formula_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → account_for; account_for_corporate_action_in_index_calculation; adjustment_between_regular_rebalance_days (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; account_for; account_for_corporate_action_in_index_calculation (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'index', 'current_count': 51, 'baseline_count': 11, 'delta': 40}; {'token': 'methodology', 'current_count': 34, 'baseline_count': 3, 'delta': 31}; {'token': 'equityindexmethodology', 'current_count': 29, 'baseline_count': 0, 'd (+17 more)
  - `grounding.origin_error_count` → 20

## [WARNING] `ontology_planning` / `new_full_surface_content_token_count_vs_text_only`

- value: **114**  (from `grounding.new_full_surface_content_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → account_for; account_for_corporate_action_in_index_calculation; adjustment_between_regular_rebalance_days (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; account_for; account_for_corporate_action_in_index_calculation (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'index', 'current_count': 51, 'baseline_count': 11, 'delta': 40}; {'token': 'methodology', 'current_count': 34, 'baseline_count': 3, 'delta': 31}; {'token': 'equityindexmethodology', 'current_count': 29, 'baseline_count': 0, 'd (+17 more)
  - `grounding.origin_error_count` → 20

## [WARNING] `ontology_planning` / `new_full_surface_token_count_vs_text_only`

- value: **125**  (from `grounding.new_full_surface_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → account_for; account_for_corporate_action_in_index_calculation; adjustment_between_regular_rebalance_days (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; account_for; account_for_corporate_action_in_index_calculation (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'index', 'current_count': 51, 'baseline_count': 11, 'delta': 40}; {'token': 'methodology', 'current_count': 34, 'baseline_count': 3, 'delta': 31}; {'token': 'equityindexmethodology', 'current_count': 29, 'baseline_count': 0, 'd (+17 more)
  - `grounding.origin_error_count` → 20

## [WARNING] `ontology_planning` / `new_surface_content_token_count`

- value: **267**  (from `<search recursive metrics JSON for key `new_surface_content_token_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → account_for; account_for_corporate_action_in_index_calculation; adjustment_between_regular_rebalance_days (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; account_for; account_for_corporate_action_in_index_calculation (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'index', 'current_count': 51, 'baseline_count': 11, 'delta': 40}; {'token': 'methodology', 'current_count': 34, 'baseline_count': 3, 'delta': 31}; {'token': 'equityindexmethodology', 'current_count': 29, 'baseline_count': 0, 'd (+17 more)
  - `grounding.origin_error_count` → 20

## [WARNING] `ontology_planning` / `new_surface_token_count`

- value: **267**  (from `<search recursive metrics JSON for key `new_surface_token_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → account_for; account_for_corporate_action_in_index_calculation; adjustment_between_regular_rebalance_days (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; account_for; account_for_corporate_action_in_index_calculation (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'index', 'current_count': 51, 'baseline_count': 11, 'delta': 40}; {'token': 'methodology', 'current_count': 34, 'baseline_count': 3, 'delta': 31}; {'token': 'equityindexmethodology', 'current_count': 29, 'baseline_count': 0, 'd (+17 more)
  - `grounding.origin_error_count` → 20

## [WARNING] `ontology_planning` / `ungrounded_sort_count`

- value: **14**  (from `grounding.ungrounded_sort_count`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → account_for; account_for_corporate_action_in_index_calculation; adjustment_between_regular_rebalance_days (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; account_for; account_for_corporate_action_in_index_calculation (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'index', 'current_count': 51, 'baseline_count': 11, 'delta': 40}; {'token': 'methodology', 'current_count': 34, 'baseline_count': 3, 'delta': 31}; {'token': 'equityindexmethodology', 'current_count': 29, 'baseline_count': 0, 'd (+17 more)
  - `grounding.origin_error_count` → 20

## [WARNING] `ontology_planning` / `ungrounded_symbol_count`

- value: **6**  (from `grounding.ungrounded_symbol_count`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → account_for; account_for_corporate_action_in_index_calculation; adjustment_between_regular_rebalance_days (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; account_for; account_for_corporate_action_in_index_calculation (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'index', 'current_count': 51, 'baseline_count': 11, 'delta': 40}; {'token': 'methodology', 'current_count': 34, 'baseline_count': 3, 'delta': 31}; {'token': 'equityindexmethodology', 'current_count': 29, 'baseline_count': 0, 'd (+17 more)
  - `grounding.origin_error_count` → 20
