# Diagnostic report — section_4_6

- **gate**: `needs_review`
- fail: 0, warning: 37

## [WARNING] `merge_canonicalization` / `callable_symbol_count`

- value: **30**  (from `parameterization.callable_symbol_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 30
  - `<related section in metrics JSON>` → 30

## [WARNING] `merge_canonicalization` / `callable_symbol_with_args_count`

- value: **30**  (from `parameterization.callable_symbol_with_args_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 30
  - `<related section in metrics JSON>` → 30

## [WARNING] `merge_canonicalization` / `cross_reference_dropout_count`

- value: **1**  (from `<search recursive metrics JSON for key `cross_reference_dropout_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `evidence.source_cross_references` → Section 4.6
  - `evidence.ir_cross_references` → entity ThisGuideline : Document

## [WARNING] `merge_canonicalization` / `cross_reference_usage_count`

- value: **1**  (from `<search recursive metrics JSON for key `cross_reference_usage_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `evidence.ir_cross_references` → entity ThisGuideline : Document

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

- value: **30**  (from `parameterization.factorization_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 30
  - `<related section in metrics JSON>` → 30

## [WARNING] `merge_canonicalization` / `focus_signature_unique_count`

- value: **1**  (from `variability.focus_signature_unique_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.

## [WARNING] `merge_canonicalization` / `quantifier_parameter_slot_count`

- value: **4**  (from `parameterization.quantifier_parameter_slot_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `assertion_complexity.top_complex_assertions` → identified_errors_correction_endeavor; efforts_to_accurately_calculate_and_maintain_indices
  - `assertion_complexity.max_assertion_depth` → 7
  - `assertion_complexity.total_quantifier_count` → 4

## [WARNING] `merge_canonicalization` / `top_level_parameter_slot_count`

- value: **56**  (from `parameterization.top_level_parameter_slot_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 56
  - `<related section in metrics JSON>` → 56

## [WARNING] `merge_canonicalization` / `total_parameter_slot_mass`

- value: **60**  (from `parameterization.total_parameter_slot_mass`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 60
  - `<related section in metrics JSON>` → 60

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

- value: **26**  (from `identifier_glue.compound_identifier_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'efforts_to_accurately_calculate_and_maintain_indices', 'raw_piec; {'identifier': 'error_possibility_in_determination_process', 'raw_piece_count': ; {'identifier': 'PeriodAndMeasureUnderlyingDependency', 'raw_piece_count': 5, 'co (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'description_occurrence_term', 'raw_piece_count': 3, 'content_pie; {'identifier': 'description_of_error_possibility', 'raw_piece_count': 4, 'conten; {'identifier': 'description_polarity_term', 'raw_piece_count': 3, 'content_piece (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'DeterminationProcessErrorPossibility', 'raw_piece_count': 4, 'co; {'identifier': 'DeterminationProcessErrorDescription', 'raw_piece_count': 4, 'co; {'identifier': 'error_possibility_in_determination_process', 'raw_piece_count': 

## [WARNING] `ontology_planning` / `compound_identifier_count_raw`

- value: **17**  (from `identifier_glue.compound_identifier_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'efforts_to_accurately_calculate_and_maintain_indices', 'raw_piec; {'identifier': 'error_possibility_in_determination_process', 'raw_piece_count': ; {'identifier': 'PeriodAndMeasureUnderlyingDependency', 'raw_piece_count': 5, 'co (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'description_occurrence_term', 'raw_piece_count': 3, 'content_pie; {'identifier': 'description_of_error_possibility', 'raw_piece_count': 4, 'conten; {'identifier': 'description_polarity_term', 'raw_piece_count': 3, 'content_piece (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'DeterminationProcessErrorPossibility', 'raw_piece_count': 4, 'co; {'identifier': 'DeterminationProcessErrorDescription', 'raw_piece_count': 4, 'co; {'identifier': 'error_possibility_in_determination_process', 'raw_piece_count': 

## [WARNING] `ontology_planning` / `cross_reference_dropout_count`

- value: **1**  (from `<search recursive metrics JSON for key `cross_reference_dropout_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `evidence.source_cross_references` → Section 4.6
  - `evidence.ir_cross_references` → entity ThisGuideline : Document

## [WARNING] `ontology_planning` / `cross_reference_usage_count`

- value: **1**  (from `<search recursive metrics JSON for key `cross_reference_usage_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `evidence.ir_cross_references` → entity ThisGuideline : Document

## [WARNING] `ontology_planning` / `dependency_link_count`

- value: **2**  (from `<search recursive metrics JSON for key `dependency_link_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 2
  - `<related section in metrics JSON>` → 2

## [WARNING] `ontology_planning` / `identifier_count`

- value: **74**  (from `identifier_glue.identifier_count`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'efforts_to_accurately_calculate_and_maintain_indices', 'raw_piec; {'identifier': 'error_possibility_in_determination_process', 'raw_piece_count': ; {'identifier': 'PeriodAndMeasureUnderlyingDependency', 'raw_piece_count': 5, 'co (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'description_occurrence_term', 'raw_piece_count': 3, 'content_pie; {'identifier': 'description_of_error_possibility', 'raw_piece_count': 4, 'conten; {'identifier': 'description_polarity_term', 'raw_piece_count': 3, 'content_piece (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'DeterminationProcessErrorPossibility', 'raw_piece_count': 4, 'co; {'identifier': 'DeterminationProcessErrorDescription', 'raw_piece_count': 4, 'co; {'identifier': 'error_possibility_in_determination_process', 'raw_piece_count': 

## [WARNING] `ontology_planning` / `identifier_glue_excess_mass_content`

- value: **36**  (from `identifier_glue.identifier_glue_excess_mass_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'efforts_to_accurately_calculate_and_maintain_indices', 'raw_piec; {'identifier': 'error_possibility_in_determination_process', 'raw_piece_count': ; {'identifier': 'PeriodAndMeasureUnderlyingDependency', 'raw_piece_count': 5, 'co (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'description_occurrence_term', 'raw_piece_count': 3, 'content_pie; {'identifier': 'description_of_error_possibility', 'raw_piece_count': 4, 'conten; {'identifier': 'description_polarity_term', 'raw_piece_count': 3, 'content_piece (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'DeterminationProcessErrorPossibility', 'raw_piece_count': 4, 'co; {'identifier': 'DeterminationProcessErrorDescription', 'raw_piece_count': 4, 'co; {'identifier': 'error_possibility_in_determination_process', 'raw_piece_count': 

## [WARNING] `ontology_planning` / `identifier_glue_excess_mass_raw`

- value: **26**  (from `identifier_glue.identifier_glue_excess_mass_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'efforts_to_accurately_calculate_and_maintain_indices', 'raw_piec; {'identifier': 'error_possibility_in_determination_process', 'raw_piece_count': ; {'identifier': 'PeriodAndMeasureUnderlyingDependency', 'raw_piece_count': 5, 'co (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'description_occurrence_term', 'raw_piece_count': 3, 'content_pie; {'identifier': 'description_of_error_possibility', 'raw_piece_count': 4, 'conten; {'identifier': 'description_polarity_term', 'raw_piece_count': 3, 'content_piece (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'DeterminationProcessErrorPossibility', 'raw_piece_count': 4, 'co; {'identifier': 'DeterminationProcessErrorDescription', 'raw_piece_count': 4, 'co; {'identifier': 'error_possibility_in_determination_process', 'raw_piece_count': 

## [WARNING] `ontology_planning` / `invented_helper_sort_count`

- value: **2**  (from `<search recursive metrics JSON for key `invented_helper_sort_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → accuratecalculation; accuratemaintenance; available_on (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; accuratecalculation; accuratemaintenance (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'error', 'current_count': 17, 'baseline_count': 0, 'delta': 17}; {'token': 'description', 'current_count': 14, 'baseline_count': 0, 'delta': 14}; {'token': 'understanding', 'current_count': 13, 'baseline_count': 1, 'delta': 12 (+17 more)
  - `grounding.origin_error_count` → 35
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'efforts_to_accurately_calculate_and_maintain_indices', 'raw_piec; {'identifier': 'error_possibility_in_determination_process', 'raw_piece_count': ; {'identifier': 'PeriodAndMeasureUnderlyingDependency', 'raw_piece_count': 5, 'co (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'description_occurrence_term', 'raw_piece_count': 3, 'content_pie; {'identifier': 'description_of_error_possibility', 'raw_piece_count': 4, 'conten; {'identifier': 'description_polarity_term', 'raw_piece_count': 3, 'content_piece (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'DeterminationProcessErrorPossibility', 'raw_piece_count': 4, 'co; {'identifier': 'DeterminationProcessErrorDescription', 'raw_piece_count': 4, 'co; {'identifier': 'error_possibility_in_determination_process', 'raw_piece_count': 
  - `evidence.invented_helper_sorts` → Index; Description

## [WARNING] `ontology_planning` / `invented_helper_symbol_count`

- value: **2**  (from `<search recursive metrics JSON for key `invented_helper_symbol_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → accuratecalculation; accuratemaintenance; available_on (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; accuratecalculation; accuratemaintenance (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'error', 'current_count': 17, 'baseline_count': 0, 'delta': 17}; {'token': 'description', 'current_count': 14, 'baseline_count': 0, 'delta': 14}; {'token': 'understanding', 'current_count': 13, 'baseline_count': 1, 'delta': 12 (+17 more)
  - `grounding.origin_error_count` → 35
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'efforts_to_accurately_calculate_and_maintain_indices', 'raw_piec; {'identifier': 'error_possibility_in_determination_process', 'raw_piece_count': ; {'identifier': 'PeriodAndMeasureUnderlyingDependency', 'raw_piece_count': 5, 'co (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'description_occurrence_term', 'raw_piece_count': 3, 'content_pie; {'identifier': 'description_of_error_possibility', 'raw_piece_count': 4, 'conten; {'identifier': 'description_polarity_term', 'raw_piece_count': 3, 'content_piece (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'DeterminationProcessErrorPossibility', 'raw_piece_count': 4, 'co; {'identifier': 'DeterminationProcessErrorDescription', 'raw_piece_count': 4, 'co; {'identifier': 'error_possibility_in_determination_process', 'raw_piece_count': 
  - `evidence.invented_helper_sorts` → Index; Description

## [WARNING] `ontology_planning` / `low_source_grounded_glued_identifier_count`

- value: **16**  (from `identifier_glue.low_source_grounded_glued_identifier_count`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'efforts_to_accurately_calculate_and_maintain_indices', 'raw_piec; {'identifier': 'error_possibility_in_determination_process', 'raw_piece_count': ; {'identifier': 'PeriodAndMeasureUnderlyingDependency', 'raw_piece_count': 5, 'co (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'description_occurrence_term', 'raw_piece_count': 3, 'content_pie; {'identifier': 'description_of_error_possibility', 'raw_piece_count': 4, 'conten; {'identifier': 'description_polarity_term', 'raw_piece_count': 3, 'content_piece (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'DeterminationProcessErrorPossibility', 'raw_piece_count': 4, 'co; {'identifier': 'DeterminationProcessErrorDescription', 'raw_piece_count': 4, 'co; {'identifier': 'error_possibility_in_determination_process', 'raw_piece_count': 

## [WARNING] `ontology_planning` / `max_identifier_piece_count_content`

- value: **5**  (from `identifier_glue.max_identifier_piece_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'efforts_to_accurately_calculate_and_maintain_indices', 'raw_piec; {'identifier': 'error_possibility_in_determination_process', 'raw_piece_count': ; {'identifier': 'PeriodAndMeasureUnderlyingDependency', 'raw_piece_count': 5, 'co (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'description_occurrence_term', 'raw_piece_count': 3, 'content_pie; {'identifier': 'description_of_error_possibility', 'raw_piece_count': 4, 'conten; {'identifier': 'description_polarity_term', 'raw_piece_count': 3, 'content_piece (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'DeterminationProcessErrorPossibility', 'raw_piece_count': 4, 'co; {'identifier': 'DeterminationProcessErrorDescription', 'raw_piece_count': 4, 'co; {'identifier': 'error_possibility_in_determination_process', 'raw_piece_count': 

## [WARNING] `ontology_planning` / `max_identifier_piece_count_raw`

- value: **7**  (from `identifier_glue.max_identifier_piece_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'efforts_to_accurately_calculate_and_maintain_indices', 'raw_piec; {'identifier': 'error_possibility_in_determination_process', 'raw_piece_count': ; {'identifier': 'PeriodAndMeasureUnderlyingDependency', 'raw_piece_count': 5, 'co (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'description_occurrence_term', 'raw_piece_count': 3, 'content_pie; {'identifier': 'description_of_error_possibility', 'raw_piece_count': 4, 'conten; {'identifier': 'description_polarity_term', 'raw_piece_count': 3, 'content_piece (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'DeterminationProcessErrorPossibility', 'raw_piece_count': 4, 'co; {'identifier': 'DeterminationProcessErrorDescription', 'raw_piece_count': 4, 'co; {'identifier': 'error_possibility_in_determination_process', 'raw_piece_count': 

## [WARNING] `ontology_planning` / `mean_identifier_piece_count_content`

- value: **2.1216216216216215**  (from `identifier_glue.mean_identifier_piece_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'efforts_to_accurately_calculate_and_maintain_indices', 'raw_piec; {'identifier': 'error_possibility_in_determination_process', 'raw_piece_count': ; {'identifier': 'PeriodAndMeasureUnderlyingDependency', 'raw_piece_count': 5, 'co (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'description_occurrence_term', 'raw_piece_count': 3, 'content_pie; {'identifier': 'description_of_error_possibility', 'raw_piece_count': 4, 'conten; {'identifier': 'description_polarity_term', 'raw_piece_count': 3, 'content_piece (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'DeterminationProcessErrorPossibility', 'raw_piece_count': 4, 'co; {'identifier': 'DeterminationProcessErrorDescription', 'raw_piece_count': 4, 'co; {'identifier': 'error_possibility_in_determination_process', 'raw_piece_count': 

## [WARNING] `ontology_planning` / `mean_identifier_piece_count_raw`

- value: **2.527027027027027**  (from `identifier_glue.mean_identifier_piece_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'efforts_to_accurately_calculate_and_maintain_indices', 'raw_piec; {'identifier': 'error_possibility_in_determination_process', 'raw_piece_count': ; {'identifier': 'PeriodAndMeasureUnderlyingDependency', 'raw_piece_count': 5, 'co (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'description_occurrence_term', 'raw_piece_count': 3, 'content_pie; {'identifier': 'description_of_error_possibility', 'raw_piece_count': 4, 'conten; {'identifier': 'description_polarity_term', 'raw_piece_count': 3, 'content_piece (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'DeterminationProcessErrorPossibility', 'raw_piece_count': 4, 'co; {'identifier': 'DeterminationProcessErrorDescription', 'raw_piece_count': 4, 'co; {'identifier': 'error_possibility_in_determination_process', 'raw_piece_count': 

## [WARNING] `ontology_planning` / `new_formula_content_token_count_vs_text_only`

- value: **70**  (from `grounding.new_formula_content_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → accuratecalculation; accuratemaintenance; available_on (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; accuratecalculation; accuratemaintenance (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'error', 'current_count': 17, 'baseline_count': 0, 'delta': 17}; {'token': 'description', 'current_count': 14, 'baseline_count': 0, 'delta': 14}; {'token': 'understanding', 'current_count': 13, 'baseline_count': 1, 'delta': 12 (+17 more)
  - `grounding.origin_error_count` → 35

## [WARNING] `ontology_planning` / `new_formula_token_count_vs_text_only`

- value: **75**  (from `grounding.new_formula_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → accuratecalculation; accuratemaintenance; available_on (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; accuratecalculation; accuratemaintenance (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'error', 'current_count': 17, 'baseline_count': 0, 'delta': 17}; {'token': 'description', 'current_count': 14, 'baseline_count': 0, 'delta': 14}; {'token': 'understanding', 'current_count': 13, 'baseline_count': 1, 'delta': 12 (+17 more)
  - `grounding.origin_error_count` → 35

## [WARNING] `ontology_planning` / `new_full_surface_content_token_count_vs_text_only`

- value: **89**  (from `grounding.new_full_surface_content_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → accuratecalculation; accuratemaintenance; available_on (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; accuratecalculation; accuratemaintenance (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'error', 'current_count': 17, 'baseline_count': 0, 'delta': 17}; {'token': 'description', 'current_count': 14, 'baseline_count': 0, 'delta': 14}; {'token': 'understanding', 'current_count': 13, 'baseline_count': 1, 'delta': 12 (+17 more)
  - `grounding.origin_error_count` → 35

## [WARNING] `ontology_planning` / `new_full_surface_token_count_vs_text_only`

- value: **96**  (from `grounding.new_full_surface_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → accuratecalculation; accuratemaintenance; available_on (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; accuratecalculation; accuratemaintenance (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'error', 'current_count': 17, 'baseline_count': 0, 'delta': 17}; {'token': 'description', 'current_count': 14, 'baseline_count': 0, 'delta': 14}; {'token': 'understanding', 'current_count': 13, 'baseline_count': 1, 'delta': 12 (+17 more)
  - `grounding.origin_error_count` → 35

## [WARNING] `ontology_planning` / `new_surface_content_token_count`

- value: **172**  (from `<search recursive metrics JSON for key `new_surface_content_token_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → accuratecalculation; accuratemaintenance; available_on (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; accuratecalculation; accuratemaintenance (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'error', 'current_count': 17, 'baseline_count': 0, 'delta': 17}; {'token': 'description', 'current_count': 14, 'baseline_count': 0, 'delta': 14}; {'token': 'understanding', 'current_count': 13, 'baseline_count': 1, 'delta': 12 (+17 more)
  - `grounding.origin_error_count` → 35

## [WARNING] `ontology_planning` / `new_surface_token_count`

- value: **172**  (from `<search recursive metrics JSON for key `new_surface_token_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → accuratecalculation; accuratemaintenance; available_on (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; accuratecalculation; accuratemaintenance (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'error', 'current_count': 17, 'baseline_count': 0, 'delta': 17}; {'token': 'description', 'current_count': 14, 'baseline_count': 0, 'delta': 14}; {'token': 'understanding', 'current_count': 13, 'baseline_count': 1, 'delta': 12 (+17 more)
  - `grounding.origin_error_count` → 35

## [WARNING] `ontology_planning` / `ungrounded_sort_count`

- value: **24**  (from `grounding.ungrounded_sort_count`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → accuratecalculation; accuratemaintenance; available_on (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; accuratecalculation; accuratemaintenance (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'error', 'current_count': 17, 'baseline_count': 0, 'delta': 17}; {'token': 'description', 'current_count': 14, 'baseline_count': 0, 'delta': 14}; {'token': 'understanding', 'current_count': 13, 'baseline_count': 1, 'delta': 12 (+17 more)
  - `grounding.origin_error_count` → 35

## [WARNING] `ontology_planning` / `ungrounded_symbol_count`

- value: **9**  (from `grounding.ungrounded_symbol_count`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → accuratecalculation; accuratemaintenance; available_on (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; accuratecalculation; accuratemaintenance (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'error', 'current_count': 17, 'baseline_count': 0, 'delta': 17}; {'token': 'description', 'current_count': 14, 'baseline_count': 0, 'delta': 14}; {'token': 'understanding', 'current_count': 13, 'baseline_count': 1, 'delta': 12 (+17 more)
  - `grounding.origin_error_count` → 35
