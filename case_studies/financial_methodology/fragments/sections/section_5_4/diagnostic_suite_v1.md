# Diagnostic report — section_5_4

- **gate**: `needs_review`
- fail: 0, warning: 34

## [WARNING] `merge_canonicalization` / `callable_symbol_count`

- value: **46**  (from `parameterization.callable_symbol_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 46
  - `<related section in metrics JSON>` → 46

## [WARNING] `merge_canonicalization` / `callable_symbol_with_args_count`

- value: **46**  (from `parameterization.callable_symbol_with_args_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 46
  - `<related section in metrics JSON>` → 46

## [WARNING] `merge_canonicalization` / `cross_reference_dropout_count`

- value: **4**  (from `<search recursive metrics JSON for key `cross_reference_dropout_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `evidence.source_cross_references` → Section 5.2; Section 5.4
  - `evidence.ir_cross_references` → (empty)

## [WARNING] `merge_canonicalization` / `dependency_link_count`

- value: **9**  (from `<search recursive metrics JSON for key `dependency_link_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 9
  - `<related section in metrics JSON>` → 9

## [WARNING] `merge_canonicalization` / `draft_variant_count`

- value: **1**  (from `variants.draft_variant_count`)
- meaning: A merge/variant/gold comparison changed structure or semantics; report exact compared variants or merge rows.
- repair: Use overlay/bridge/conflict split or reject rewrite based on backtest.

## [WARNING] `merge_canonicalization` / `factorization_count`

- value: **46**  (from `parameterization.factorization_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 46
  - `<related section in metrics JSON>` → 46

## [WARNING] `merge_canonicalization` / `focus_signature_unique_count`

- value: **1**  (from `variability.focus_signature_unique_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.

## [WARNING] `merge_canonicalization` / `quantifier_parameter_slot_count`

- value: **19**  (from `parameterization.quantifier_parameter_slot_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `assertion_complexity.top_complex_assertions` → methodology_adaptation_where_necessary; cessation_usual_when_economic_reality_changes; cessation_usual_when_underlying_market_changes (+6 more)
  - `assertion_complexity.max_assertion_depth` → 8
  - `assertion_complexity.total_quantifier_count` → 19

## [WARNING] `merge_canonicalization` / `top_level_parameter_slot_count`

- value: **82**  (from `parameterization.top_level_parameter_slot_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 82
  - `<related section in metrics JSON>` → 82

## [WARNING] `merge_canonicalization` / `total_parameter_slot_mass`

- value: **101**  (from `parameterization.total_parameter_slot_mass`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 101
  - `<related section in metrics JSON>` → 101

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

- value: **35**  (from `identifier_glue.compound_identifier_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'cessation_usual_when_index_not_used_as_underlying_value', 'raw_p; {'identifier': 'cessation_usual_when_selection_criteria_not_applied_coherently',; {'identifier': 'HttpsWwwSolactiveComDocumentsTerminationPolicy', 'raw_piece_coun (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DocumentLocator', 'raw_piece_count': 2, 'content_piece_count': 2; {'identifier': 'DocumentPart', 'raw_piece_count': 2, 'content_piece_count': 2, '; {'identifier': 'VagueTerm', 'raw_piece_count': 2, 'content_piece_count': 2, 'raw (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'cessation_usual_when_rules_not_applied_coherently', 'raw_piece_c; {'identifier': 'cessation_usual_when_selection_criteria_not_applied_coherently',; {'identifier': 'cessation_usual_when_index_not_used_as_underlying_value', 'raw_p (+1 more)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'used_as_underlying_value_for_financial_instrument', 'raw_piece_c; {'identifier': 'used_as_underlying_value_for_investment_fund', 'raw_piece_count'; {'identifier': 'used_as_underlying_value_for_financial_contract', 'raw_piece_cou (+1 more)

## [WARNING] `ontology_planning` / `compound_identifier_count_raw`

- value: **29**  (from `identifier_glue.compound_identifier_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'cessation_usual_when_index_not_used_as_underlying_value', 'raw_p; {'identifier': 'cessation_usual_when_selection_criteria_not_applied_coherently',; {'identifier': 'HttpsWwwSolactiveComDocumentsTerminationPolicy', 'raw_piece_coun (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DocumentLocator', 'raw_piece_count': 2, 'content_piece_count': 2; {'identifier': 'DocumentPart', 'raw_piece_count': 2, 'content_piece_count': 2, '; {'identifier': 'VagueTerm', 'raw_piece_count': 2, 'content_piece_count': 2, 'raw (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'cessation_usual_when_rules_not_applied_coherently', 'raw_piece_c; {'identifier': 'cessation_usual_when_selection_criteria_not_applied_coherently',; {'identifier': 'cessation_usual_when_index_not_used_as_underlying_value', 'raw_p (+1 more)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'used_as_underlying_value_for_financial_instrument', 'raw_piece_c; {'identifier': 'used_as_underlying_value_for_investment_fund', 'raw_piece_count'; {'identifier': 'used_as_underlying_value_for_financial_contract', 'raw_piece_cou (+1 more)

## [WARNING] `ontology_planning` / `cross_reference_dropout_count`

- value: **4**  (from `<search recursive metrics JSON for key `cross_reference_dropout_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `evidence.source_cross_references` → Section 5.2; Section 5.4
  - `evidence.ir_cross_references` → (empty)

## [WARNING] `ontology_planning` / `dependency_link_count`

- value: **9**  (from `<search recursive metrics JSON for key `dependency_link_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 9
  - `<related section in metrics JSON>` → 9

## [WARNING] `ontology_planning` / `identifier_count`

- value: **107**  (from `identifier_glue.identifier_count`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'cessation_usual_when_index_not_used_as_underlying_value', 'raw_p; {'identifier': 'cessation_usual_when_selection_criteria_not_applied_coherently',; {'identifier': 'HttpsWwwSolactiveComDocumentsTerminationPolicy', 'raw_piece_coun (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DocumentLocator', 'raw_piece_count': 2, 'content_piece_count': 2; {'identifier': 'DocumentPart', 'raw_piece_count': 2, 'content_piece_count': 2, '; {'identifier': 'VagueTerm', 'raw_piece_count': 2, 'content_piece_count': 2, 'raw (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'cessation_usual_when_rules_not_applied_coherently', 'raw_piece_c; {'identifier': 'cessation_usual_when_selection_criteria_not_applied_coherently',; {'identifier': 'cessation_usual_when_index_not_used_as_underlying_value', 'raw_p (+1 more)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'used_as_underlying_value_for_financial_instrument', 'raw_piece_c; {'identifier': 'used_as_underlying_value_for_investment_fund', 'raw_piece_count'; {'identifier': 'used_as_underlying_value_for_financial_contract', 'raw_piece_cou (+1 more)

## [WARNING] `ontology_planning` / `identifier_glue_excess_mass_content`

- value: **85**  (from `identifier_glue.identifier_glue_excess_mass_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'cessation_usual_when_index_not_used_as_underlying_value', 'raw_p; {'identifier': 'cessation_usual_when_selection_criteria_not_applied_coherently',; {'identifier': 'HttpsWwwSolactiveComDocumentsTerminationPolicy', 'raw_piece_coun (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DocumentLocator', 'raw_piece_count': 2, 'content_piece_count': 2; {'identifier': 'DocumentPart', 'raw_piece_count': 2, 'content_piece_count': 2, '; {'identifier': 'VagueTerm', 'raw_piece_count': 2, 'content_piece_count': 2, 'raw (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'cessation_usual_when_rules_not_applied_coherently', 'raw_piece_c; {'identifier': 'cessation_usual_when_selection_criteria_not_applied_coherently',; {'identifier': 'cessation_usual_when_index_not_used_as_underlying_value', 'raw_p (+1 more)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'used_as_underlying_value_for_financial_instrument', 'raw_piece_c; {'identifier': 'used_as_underlying_value_for_investment_fund', 'raw_piece_count'; {'identifier': 'used_as_underlying_value_for_financial_contract', 'raw_piece_cou (+1 more)

## [WARNING] `ontology_planning` / `identifier_glue_excess_mass_raw`

- value: **80**  (from `identifier_glue.identifier_glue_excess_mass_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'cessation_usual_when_index_not_used_as_underlying_value', 'raw_p; {'identifier': 'cessation_usual_when_selection_criteria_not_applied_coherently',; {'identifier': 'HttpsWwwSolactiveComDocumentsTerminationPolicy', 'raw_piece_coun (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DocumentLocator', 'raw_piece_count': 2, 'content_piece_count': 2; {'identifier': 'DocumentPart', 'raw_piece_count': 2, 'content_piece_count': 2, '; {'identifier': 'VagueTerm', 'raw_piece_count': 2, 'content_piece_count': 2, 'raw (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'cessation_usual_when_rules_not_applied_coherently', 'raw_piece_c; {'identifier': 'cessation_usual_when_selection_criteria_not_applied_coherently',; {'identifier': 'cessation_usual_when_index_not_used_as_underlying_value', 'raw_p (+1 more)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'used_as_underlying_value_for_financial_instrument', 'raw_piece_c; {'identifier': 'used_as_underlying_value_for_investment_fund', 'raw_piece_count'; {'identifier': 'used_as_underlying_value_for_financial_contract', 'raw_piece_cou (+1 more)

## [WARNING] `ontology_planning` / `low_source_grounded_glued_identifier_count`

- value: **9**  (from `identifier_glue.low_source_grounded_glued_identifier_count`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'cessation_usual_when_index_not_used_as_underlying_value', 'raw_p; {'identifier': 'cessation_usual_when_selection_criteria_not_applied_coherently',; {'identifier': 'HttpsWwwSolactiveComDocumentsTerminationPolicy', 'raw_piece_coun (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DocumentLocator', 'raw_piece_count': 2, 'content_piece_count': 2; {'identifier': 'DocumentPart', 'raw_piece_count': 2, 'content_piece_count': 2, '; {'identifier': 'VagueTerm', 'raw_piece_count': 2, 'content_piece_count': 2, 'raw (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'cessation_usual_when_rules_not_applied_coherently', 'raw_piece_c; {'identifier': 'cessation_usual_when_selection_criteria_not_applied_coherently',; {'identifier': 'cessation_usual_when_index_not_used_as_underlying_value', 'raw_p (+1 more)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'used_as_underlying_value_for_financial_instrument', 'raw_piece_c; {'identifier': 'used_as_underlying_value_for_investment_fund', 'raw_piece_count'; {'identifier': 'used_as_underlying_value_for_financial_contract', 'raw_piece_cou (+1 more)

## [WARNING] `ontology_planning` / `max_identifier_piece_count_content`

- value: **7**  (from `identifier_glue.max_identifier_piece_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'cessation_usual_when_index_not_used_as_underlying_value', 'raw_p; {'identifier': 'cessation_usual_when_selection_criteria_not_applied_coherently',; {'identifier': 'HttpsWwwSolactiveComDocumentsTerminationPolicy', 'raw_piece_coun (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DocumentLocator', 'raw_piece_count': 2, 'content_piece_count': 2; {'identifier': 'DocumentPart', 'raw_piece_count': 2, 'content_piece_count': 2, '; {'identifier': 'VagueTerm', 'raw_piece_count': 2, 'content_piece_count': 2, 'raw (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'cessation_usual_when_rules_not_applied_coherently', 'raw_piece_c; {'identifier': 'cessation_usual_when_selection_criteria_not_applied_coherently',; {'identifier': 'cessation_usual_when_index_not_used_as_underlying_value', 'raw_p (+1 more)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'used_as_underlying_value_for_financial_instrument', 'raw_piece_c; {'identifier': 'used_as_underlying_value_for_investment_fund', 'raw_piece_count'; {'identifier': 'used_as_underlying_value_for_financial_contract', 'raw_piece_cou (+1 more)

## [WARNING] `ontology_planning` / `max_identifier_piece_count_raw`

- value: **9**  (from `identifier_glue.max_identifier_piece_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'cessation_usual_when_index_not_used_as_underlying_value', 'raw_p; {'identifier': 'cessation_usual_when_selection_criteria_not_applied_coherently',; {'identifier': 'HttpsWwwSolactiveComDocumentsTerminationPolicy', 'raw_piece_coun (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DocumentLocator', 'raw_piece_count': 2, 'content_piece_count': 2; {'identifier': 'DocumentPart', 'raw_piece_count': 2, 'content_piece_count': 2, '; {'identifier': 'VagueTerm', 'raw_piece_count': 2, 'content_piece_count': 2, 'raw (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'cessation_usual_when_rules_not_applied_coherently', 'raw_piece_c; {'identifier': 'cessation_usual_when_selection_criteria_not_applied_coherently',; {'identifier': 'cessation_usual_when_index_not_used_as_underlying_value', 'raw_p (+1 more)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'used_as_underlying_value_for_financial_instrument', 'raw_piece_c; {'identifier': 'used_as_underlying_value_for_investment_fund', 'raw_piece_count'; {'identifier': 'used_as_underlying_value_for_financial_contract', 'raw_piece_cou (+1 more)

## [WARNING] `ontology_planning` / `mean_identifier_piece_count_content`

- value: **2.3271028037383177**  (from `identifier_glue.mean_identifier_piece_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'cessation_usual_when_index_not_used_as_underlying_value', 'raw_p; {'identifier': 'cessation_usual_when_selection_criteria_not_applied_coherently',; {'identifier': 'HttpsWwwSolactiveComDocumentsTerminationPolicy', 'raw_piece_coun (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DocumentLocator', 'raw_piece_count': 2, 'content_piece_count': 2; {'identifier': 'DocumentPart', 'raw_piece_count': 2, 'content_piece_count': 2, '; {'identifier': 'VagueTerm', 'raw_piece_count': 2, 'content_piece_count': 2, 'raw (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'cessation_usual_when_rules_not_applied_coherently', 'raw_piece_c; {'identifier': 'cessation_usual_when_selection_criteria_not_applied_coherently',; {'identifier': 'cessation_usual_when_index_not_used_as_underlying_value', 'raw_p (+1 more)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'used_as_underlying_value_for_financial_instrument', 'raw_piece_c; {'identifier': 'used_as_underlying_value_for_investment_fund', 'raw_piece_count'; {'identifier': 'used_as_underlying_value_for_financial_contract', 'raw_piece_cou (+1 more)

## [WARNING] `ontology_planning` / `mean_identifier_piece_count_raw`

- value: **2.8598130841121496**  (from `identifier_glue.mean_identifier_piece_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'cessation_usual_when_index_not_used_as_underlying_value', 'raw_p; {'identifier': 'cessation_usual_when_selection_criteria_not_applied_coherently',; {'identifier': 'HttpsWwwSolactiveComDocumentsTerminationPolicy', 'raw_piece_coun (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DocumentLocator', 'raw_piece_count': 2, 'content_piece_count': 2; {'identifier': 'DocumentPart', 'raw_piece_count': 2, 'content_piece_count': 2, '; {'identifier': 'VagueTerm', 'raw_piece_count': 2, 'content_piece_count': 2, 'raw (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'cessation_usual_when_rules_not_applied_coherently', 'raw_piece_c; {'identifier': 'cessation_usual_when_selection_criteria_not_applied_coherently',; {'identifier': 'cessation_usual_when_index_not_used_as_underlying_value', 'raw_p (+1 more)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'used_as_underlying_value_for_financial_instrument', 'raw_piece_c; {'identifier': 'used_as_underlying_value_for_investment_fund', 'raw_piece_count'; {'identifier': 'used_as_underlying_value_for_financial_contract', 'raw_piece_cou (+1 more)

## [WARNING] `ontology_planning` / `new_formula_content_token_count_vs_text_only`

- value: **92**  (from `grounding.new_formula_content_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → adapts_index_methodology; alternativeindex; applied_coherently (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; adapts_index_methodology; alternativeindex (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'index', 'current_count': 53, 'baseline_count': 8, 'delta': 45}; {'token': 'procedure', 'current_count': 35, 'baseline_count': 1, 'delta': 34}; {'token': 'guidelines', 'current_count': 20, 'baseline_count': 1, 'delta': 19} (+17 more)
  - `grounding.origin_error_count` → 20

## [WARNING] `ontology_planning` / `new_formula_token_count_vs_text_only`

- value: **106**  (from `grounding.new_formula_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → adapts_index_methodology; alternativeindex; applied_coherently (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; adapts_index_methodology; alternativeindex (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'index', 'current_count': 53, 'baseline_count': 8, 'delta': 45}; {'token': 'procedure', 'current_count': 35, 'baseline_count': 1, 'delta': 34}; {'token': 'guidelines', 'current_count': 20, 'baseline_count': 1, 'delta': 19} (+17 more)
  - `grounding.origin_error_count` → 20

## [WARNING] `ontology_planning` / `new_full_surface_content_token_count_vs_text_only`

- value: **111**  (from `grounding.new_full_surface_content_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → adapts_index_methodology; alternativeindex; applied_coherently (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; adapts_index_methodology; alternativeindex (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'index', 'current_count': 53, 'baseline_count': 8, 'delta': 45}; {'token': 'procedure', 'current_count': 35, 'baseline_count': 1, 'delta': 34}; {'token': 'guidelines', 'current_count': 20, 'baseline_count': 1, 'delta': 19} (+17 more)
  - `grounding.origin_error_count` → 20

## [WARNING] `ontology_planning` / `new_full_surface_token_count_vs_text_only`

- value: **128**  (from `grounding.new_full_surface_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → adapts_index_methodology; alternativeindex; applied_coherently (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; adapts_index_methodology; alternativeindex (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'index', 'current_count': 53, 'baseline_count': 8, 'delta': 45}; {'token': 'procedure', 'current_count': 35, 'baseline_count': 1, 'delta': 34}; {'token': 'guidelines', 'current_count': 20, 'baseline_count': 1, 'delta': 19} (+17 more)
  - `grounding.origin_error_count` → 20

## [WARNING] `ontology_planning` / `new_surface_content_token_count`

- value: **263**  (from `<search recursive metrics JSON for key `new_surface_content_token_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → adapts_index_methodology; alternativeindex; applied_coherently (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; adapts_index_methodology; alternativeindex (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'index', 'current_count': 53, 'baseline_count': 8, 'delta': 45}; {'token': 'procedure', 'current_count': 35, 'baseline_count': 1, 'delta': 34}; {'token': 'guidelines', 'current_count': 20, 'baseline_count': 1, 'delta': 19} (+17 more)
  - `grounding.origin_error_count` → 20

## [WARNING] `ontology_planning` / `new_surface_token_count`

- value: **263**  (from `<search recursive metrics JSON for key `new_surface_token_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → adapts_index_methodology; alternativeindex; applied_coherently (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; adapts_index_methodology; alternativeindex (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'index', 'current_count': 53, 'baseline_count': 8, 'delta': 45}; {'token': 'procedure', 'current_count': 35, 'baseline_count': 1, 'delta': 34}; {'token': 'guidelines', 'current_count': 20, 'baseline_count': 1, 'delta': 19} (+17 more)
  - `grounding.origin_error_count` → 20

## [WARNING] `ontology_planning` / `ungrounded_ref_count`

- value: **1**  (from `grounding.ungrounded_ref_count`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → adapts_index_methodology; alternativeindex; applied_coherently (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; adapts_index_methodology; alternativeindex (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'index', 'current_count': 53, 'baseline_count': 8, 'delta': 45}; {'token': 'procedure', 'current_count': 35, 'baseline_count': 1, 'delta': 34}; {'token': 'guidelines', 'current_count': 20, 'baseline_count': 1, 'delta': 19} (+17 more)
  - `grounding.origin_error_count` → 20

## [WARNING] `ontology_planning` / `ungrounded_sort_count`

- value: **16**  (from `grounding.ungrounded_sort_count`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → adapts_index_methodology; alternativeindex; applied_coherently (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; adapts_index_methodology; alternativeindex (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'index', 'current_count': 53, 'baseline_count': 8, 'delta': 45}; {'token': 'procedure', 'current_count': 35, 'baseline_count': 1, 'delta': 34}; {'token': 'guidelines', 'current_count': 20, 'baseline_count': 1, 'delta': 19} (+17 more)
  - `grounding.origin_error_count` → 20

## [WARNING] `ontology_planning` / `ungrounded_symbol_count`

- value: **2**  (from `grounding.ungrounded_symbol_count`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → adapts_index_methodology; alternativeindex; applied_coherently (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; adapts_index_methodology; alternativeindex (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'index', 'current_count': 53, 'baseline_count': 8, 'delta': 45}; {'token': 'procedure', 'current_count': 35, 'baseline_count': 1, 'delta': 34}; {'token': 'guidelines', 'current_count': 20, 'baseline_count': 1, 'delta': 19} (+17 more)
  - `grounding.origin_error_count` → 20
