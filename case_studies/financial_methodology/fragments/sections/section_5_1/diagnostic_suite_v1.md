# Diagnostic report — section_5_1

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

## [WARNING] `merge_canonicalization` / `cross_reference_dropout_count`

- value: **2**  (from `<search recursive metrics JSON for key `cross_reference_dropout_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `evidence.source_cross_references` → Section 5.1
  - `evidence.ir_cross_references` → (empty)

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

- value: **2**  (from `parameterization.quantifier_parameter_slot_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `assertion_complexity.top_complex_assertions` → index_determination_discretion_scope
  - `assertion_complexity.max_assertion_depth` → 5
  - `assertion_complexity.total_quantifier_count` → 2

## [WARNING] `merge_canonicalization` / `top_level_parameter_slot_count`

- value: **10**  (from `parameterization.top_level_parameter_slot_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 10
  - `<related section in metrics JSON>` → 10

## [WARNING] `merge_canonicalization` / `total_parameter_slot_mass`

- value: **12**  (from `parameterization.total_parameter_slot_mass`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 12
  - `<related section in metrics JSON>` → 12

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
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'other_relevant_decision_in_relation_to_index', 'raw_piece_count'; {'identifier': 'StrictRulesForDiscretionAndExpertJudgement', 'raw_piece_count': ; {'identifier': 'discretion_in_relation_to_matter', 'raw_piece_count': 5, 'conten (+15 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'discretion_in_relation_to_matter', 'raw_piece_count': 5, 'conten; {'identifier': 'ExerciseBasis', 'raw_piece_count': 2, 'content_piece_count': 2, ; {'identifier': 'StrictRule', 'raw_piece_count': 2, 'content_piece_count': 2, 'ra (+9 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `compound_identifier_count_raw`

- value: **6**  (from `identifier_glue.compound_identifier_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'other_relevant_decision_in_relation_to_index', 'raw_piece_count'; {'identifier': 'StrictRulesForDiscretionAndExpertJudgement', 'raw_piece_count': ; {'identifier': 'discretion_in_relation_to_matter', 'raw_piece_count': 5, 'conten (+15 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'discretion_in_relation_to_matter', 'raw_piece_count': 5, 'conten; {'identifier': 'ExerciseBasis', 'raw_piece_count': 2, 'content_piece_count': 2, ; {'identifier': 'StrictRule', 'raw_piece_count': 2, 'content_piece_count': 2, 'ra (+9 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `cross_reference_dropout_count`

- value: **2**  (from `<search recursive metrics JSON for key `cross_reference_dropout_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `evidence.source_cross_references` → Section 5.1
  - `evidence.ir_cross_references` → (empty)

## [WARNING] `ontology_planning` / `identifier_count`

- value: **18**  (from `identifier_glue.identifier_count`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'other_relevant_decision_in_relation_to_index', 'raw_piece_count'; {'identifier': 'StrictRulesForDiscretionAndExpertJudgement', 'raw_piece_count': ; {'identifier': 'discretion_in_relation_to_matter', 'raw_piece_count': 5, 'conten (+15 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'discretion_in_relation_to_matter', 'raw_piece_count': 5, 'conten; {'identifier': 'ExerciseBasis', 'raw_piece_count': 2, 'content_piece_count': 2, ; {'identifier': 'StrictRule', 'raw_piece_count': 2, 'content_piece_count': 2, 'ra (+9 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `identifier_glue_excess_mass_content`

- value: **13**  (from `identifier_glue.identifier_glue_excess_mass_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'other_relevant_decision_in_relation_to_index', 'raw_piece_count'; {'identifier': 'StrictRulesForDiscretionAndExpertJudgement', 'raw_piece_count': ; {'identifier': 'discretion_in_relation_to_matter', 'raw_piece_count': 5, 'conten (+15 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'discretion_in_relation_to_matter', 'raw_piece_count': 5, 'conten; {'identifier': 'ExerciseBasis', 'raw_piece_count': 2, 'content_piece_count': 2, ; {'identifier': 'StrictRule', 'raw_piece_count': 2, 'content_piece_count': 2, 'ra (+9 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `identifier_glue_excess_mass_raw`

- value: **14**  (from `identifier_glue.identifier_glue_excess_mass_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'other_relevant_decision_in_relation_to_index', 'raw_piece_count'; {'identifier': 'StrictRulesForDiscretionAndExpertJudgement', 'raw_piece_count': ; {'identifier': 'discretion_in_relation_to_matter', 'raw_piece_count': 5, 'conten (+15 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'discretion_in_relation_to_matter', 'raw_piece_count': 5, 'conten; {'identifier': 'ExerciseBasis', 'raw_piece_count': 2, 'content_piece_count': 2, ; {'identifier': 'StrictRule', 'raw_piece_count': 2, 'content_piece_count': 2, 'ra (+9 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `low_source_grounded_glued_identifier_count`

- value: **6**  (from `identifier_glue.low_source_grounded_glued_identifier_count`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'other_relevant_decision_in_relation_to_index', 'raw_piece_count'; {'identifier': 'StrictRulesForDiscretionAndExpertJudgement', 'raw_piece_count': ; {'identifier': 'discretion_in_relation_to_matter', 'raw_piece_count': 5, 'conten (+15 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'discretion_in_relation_to_matter', 'raw_piece_count': 5, 'conten; {'identifier': 'ExerciseBasis', 'raw_piece_count': 2, 'content_piece_count': 2, ; {'identifier': 'StrictRule', 'raw_piece_count': 2, 'content_piece_count': 2, 'ra (+9 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `max_identifier_piece_count_content`

- value: **5**  (from `identifier_glue.max_identifier_piece_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'other_relevant_decision_in_relation_to_index', 'raw_piece_count'; {'identifier': 'StrictRulesForDiscretionAndExpertJudgement', 'raw_piece_count': ; {'identifier': 'discretion_in_relation_to_matter', 'raw_piece_count': 5, 'conten (+15 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'discretion_in_relation_to_matter', 'raw_piece_count': 5, 'conten; {'identifier': 'ExerciseBasis', 'raw_piece_count': 2, 'content_piece_count': 2, ; {'identifier': 'StrictRule', 'raw_piece_count': 2, 'content_piece_count': 2, 'ra (+9 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `max_identifier_piece_count_raw`

- value: **7**  (from `identifier_glue.max_identifier_piece_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'other_relevant_decision_in_relation_to_index', 'raw_piece_count'; {'identifier': 'StrictRulesForDiscretionAndExpertJudgement', 'raw_piece_count': ; {'identifier': 'discretion_in_relation_to_matter', 'raw_piece_count': 5, 'conten (+15 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'discretion_in_relation_to_matter', 'raw_piece_count': 5, 'conten; {'identifier': 'ExerciseBasis', 'raw_piece_count': 2, 'content_piece_count': 2, ; {'identifier': 'StrictRule', 'raw_piece_count': 2, 'content_piece_count': 2, 'ra (+9 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `mean_identifier_piece_count_content`

- value: **2.2777777777777777**  (from `identifier_glue.mean_identifier_piece_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'other_relevant_decision_in_relation_to_index', 'raw_piece_count'; {'identifier': 'StrictRulesForDiscretionAndExpertJudgement', 'raw_piece_count': ; {'identifier': 'discretion_in_relation_to_matter', 'raw_piece_count': 5, 'conten (+15 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'discretion_in_relation_to_matter', 'raw_piece_count': 5, 'conten; {'identifier': 'ExerciseBasis', 'raw_piece_count': 2, 'content_piece_count': 2, ; {'identifier': 'StrictRule', 'raw_piece_count': 2, 'content_piece_count': 2, 'ra (+9 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `mean_identifier_piece_count_raw`

- value: **3.0555555555555554**  (from `identifier_glue.mean_identifier_piece_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'other_relevant_decision_in_relation_to_index', 'raw_piece_count'; {'identifier': 'StrictRulesForDiscretionAndExpertJudgement', 'raw_piece_count': ; {'identifier': 'discretion_in_relation_to_matter', 'raw_piece_count': 5, 'conten (+15 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'discretion_in_relation_to_matter', 'raw_piece_count': 5, 'conten; {'identifier': 'ExerciseBasis', 'raw_piece_count': 2, 'content_piece_count': 2, ; {'identifier': 'StrictRule', 'raw_piece_count': 2, 'content_piece_count': 2, 'ra (+9 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `new_formula_content_token_count_vs_text_only`

- value: **24**  (from `grounding.new_formula_content_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → applicable_example_matters; determinationofindex; determinationofindexuniverse (+21 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; applicable_example_matters; canonical (+40 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'rules', 'current_count': 7, 'baseline_count': 1, 'delta': 6}; {'token': 'indexdeterminationdiscretion', 'current_count': 6, 'baseline_count': ; {'token': 'index', 'current_count': 9, 'baseline_count': 4, 'delta': 5} (+17 more)
  - `grounding.origin_error_count` → 4

## [WARNING] `ontology_planning` / `new_formula_token_count_vs_text_only`

- value: **26**  (from `grounding.new_formula_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → applicable_example_matters; determinationofindex; determinationofindexuniverse (+21 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; applicable_example_matters; canonical (+40 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'rules', 'current_count': 7, 'baseline_count': 1, 'delta': 6}; {'token': 'indexdeterminationdiscretion', 'current_count': 6, 'baseline_count': ; {'token': 'index', 'current_count': 9, 'baseline_count': 4, 'delta': 5} (+17 more)
  - `grounding.origin_error_count` → 4

## [WARNING] `ontology_planning` / `new_full_surface_content_token_count_vs_text_only`

- value: **43**  (from `grounding.new_full_surface_content_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → applicable_example_matters; determinationofindex; determinationofindexuniverse (+21 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; applicable_example_matters; canonical (+40 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'rules', 'current_count': 7, 'baseline_count': 1, 'delta': 6}; {'token': 'indexdeterminationdiscretion', 'current_count': 6, 'baseline_count': ; {'token': 'index', 'current_count': 9, 'baseline_count': 4, 'delta': 5} (+17 more)
  - `grounding.origin_error_count` → 4

## [WARNING] `ontology_planning` / `new_full_surface_token_count_vs_text_only`

- value: **48**  (from `grounding.new_full_surface_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → applicable_example_matters; determinationofindex; determinationofindexuniverse (+21 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; applicable_example_matters; canonical (+40 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'rules', 'current_count': 7, 'baseline_count': 1, 'delta': 6}; {'token': 'indexdeterminationdiscretion', 'current_count': 6, 'baseline_count': ; {'token': 'index', 'current_count': 9, 'baseline_count': 4, 'delta': 5} (+17 more)
  - `grounding.origin_error_count` → 4

## [WARNING] `ontology_planning` / `new_surface_content_token_count`

- value: **58**  (from `<search recursive metrics JSON for key `new_surface_content_token_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → applicable_example_matters; determinationofindex; determinationofindexuniverse (+21 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; applicable_example_matters; canonical (+40 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'rules', 'current_count': 7, 'baseline_count': 1, 'delta': 6}; {'token': 'indexdeterminationdiscretion', 'current_count': 6, 'baseline_count': ; {'token': 'index', 'current_count': 9, 'baseline_count': 4, 'delta': 5} (+17 more)
  - `grounding.origin_error_count` → 4

## [WARNING] `ontology_planning` / `new_surface_token_count`

- value: **58**  (from `<search recursive metrics JSON for key `new_surface_token_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → applicable_example_matters; determinationofindex; determinationofindexuniverse (+21 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; applicable_example_matters; canonical (+40 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'rules', 'current_count': 7, 'baseline_count': 1, 'delta': 6}; {'token': 'indexdeterminationdiscretion', 'current_count': 6, 'baseline_count': ; {'token': 'index', 'current_count': 9, 'baseline_count': 4, 'delta': 5} (+17 more)
  - `grounding.origin_error_count` → 4

## [WARNING] `ontology_planning` / `ungrounded_sort_count`

- value: **2**  (from `grounding.ungrounded_sort_count`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → applicable_example_matters; determinationofindex; determinationofindexuniverse (+21 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; applicable_example_matters; canonical (+40 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'rules', 'current_count': 7, 'baseline_count': 1, 'delta': 6}; {'token': 'indexdeterminationdiscretion', 'current_count': 6, 'baseline_count': ; {'token': 'index', 'current_count': 9, 'baseline_count': 4, 'delta': 5} (+17 more)
  - `grounding.origin_error_count` → 4

## [WARNING] `ontology_planning` / `ungrounded_symbol_count`

- value: **2**  (from `grounding.ungrounded_symbol_count`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → applicable_example_matters; determinationofindex; determinationofindexuniverse (+21 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; applicable_example_matters; canonical (+40 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'rules', 'current_count': 7, 'baseline_count': 1, 'delta': 6}; {'token': 'indexdeterminationdiscretion', 'current_count': 6, 'baseline_count': ; {'token': 'index', 'current_count': 9, 'baseline_count': 4, 'delta': 5} (+17 more)
  - `grounding.origin_error_count` → 4
