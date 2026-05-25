# Diagnostic report — section_5_3

- **gate**: `needs_review`
- fail: 0, warning: 33

## [WARNING] `merge_canonicalization` / `callable_symbol_count`

- value: **26**  (from `parameterization.callable_symbol_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 26
  - `<related section in metrics JSON>` → 26

## [WARNING] `merge_canonicalization` / `callable_symbol_with_args_count`

- value: **26**  (from `parameterization.callable_symbol_with_args_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 26
  - `<related section in metrics JSON>` → 26

## [WARNING] `merge_canonicalization` / `cross_reference_dropout_count`

- value: **1**  (from `<search recursive metrics JSON for key `cross_reference_dropout_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `evidence.source_cross_references` → Section 5.3
  - `evidence.ir_cross_references` → entity ThisDocument : Document

## [WARNING] `merge_canonicalization` / `cross_reference_usage_count`

- value: **1**  (from `<search recursive metrics JSON for key `cross_reference_usage_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `evidence.ir_cross_references` → entity ThisDocument : Document

## [WARNING] `merge_canonicalization` / `draft_variant_count`

- value: **1**  (from `variants.draft_variant_count`)
- meaning: A merge/variant/gold comparison changed structure or semantics; report exact compared variants or merge rows.
- repair: Use overlay/bridge/conflict split or reject rewrite based on backtest.

## [WARNING] `merge_canonicalization` / `factorization_count`

- value: **26**  (from `parameterization.factorization_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 26
  - `<related section in metrics JSON>` → 26

## [WARNING] `merge_canonicalization` / `focus_signature_unique_count`

- value: **1**  (from `variability.focus_signature_unique_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.

## [WARNING] `merge_canonicalization` / `quantifier_parameter_slot_count`

- value: **4**  (from `parameterization.quantifier_parameter_slot_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `assertion_complexity.top_complex_assertions` → deemed_modification_or_change_scope; information_withheld_means_information_not_provided
  - `assertion_complexity.max_assertion_depth` → 8
  - `assertion_complexity.total_quantifier_count` → 4

## [WARNING] `merge_canonicalization` / `top_level_parameter_slot_count`

- value: **50**  (from `parameterization.top_level_parameter_slot_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 50
  - `<related section in metrics JSON>` → 50

## [WARNING] `merge_canonicalization` / `total_parameter_slot_mass`

- value: **54**  (from `parameterization.total_parameter_slot_mass`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 54
  - `<related section in metrics JSON>` → 54

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

- value: **18**  (from `identifier_glue.compound_identifier_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'information_withheld_means_information_not_provided', 'raw_piece; {'identifier': 'information_withheld_on_modification_or_change', 'raw_piece_coun; {'identifier': 'provide_information_on_modification_or_change', 'raw_piece_count (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'potentially_requires_change_to_method', 'raw_piece_count': 5, 'c; {'identifier': 'change_to_calculation_method', 'raw_piece_count': 4, 'content_pi; {'identifier': 'deemed_modification_or_change_scope', 'raw_piece_count': 5, 'con (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'information_withheld_means_information_not_provided', 'raw_piece
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `compound_identifier_count_raw`

- value: **17**  (from `identifier_glue.compound_identifier_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'information_withheld_means_information_not_provided', 'raw_piece; {'identifier': 'information_withheld_on_modification_or_change', 'raw_piece_coun; {'identifier': 'provide_information_on_modification_or_change', 'raw_piece_count (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'potentially_requires_change_to_method', 'raw_piece_count': 5, 'c; {'identifier': 'change_to_calculation_method', 'raw_piece_count': 4, 'content_pi; {'identifier': 'deemed_modification_or_change_scope', 'raw_piece_count': 5, 'con (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'information_withheld_means_information_not_provided', 'raw_piece
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `cross_reference_dropout_count`

- value: **1**  (from `<search recursive metrics JSON for key `cross_reference_dropout_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `evidence.source_cross_references` → Section 5.3
  - `evidence.ir_cross_references` → entity ThisDocument : Document

## [WARNING] `ontology_planning` / `cross_reference_usage_count`

- value: **1**  (from `<search recursive metrics JSON for key `cross_reference_usage_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `evidence.ir_cross_references` → entity ThisDocument : Document

## [WARNING] `ontology_planning` / `identifier_count`

- value: **58**  (from `identifier_glue.identifier_count`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'information_withheld_means_information_not_provided', 'raw_piece; {'identifier': 'information_withheld_on_modification_or_change', 'raw_piece_coun; {'identifier': 'provide_information_on_modification_or_change', 'raw_piece_count (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'potentially_requires_change_to_method', 'raw_piece_count': 5, 'c; {'identifier': 'change_to_calculation_method', 'raw_piece_count': 4, 'content_pi; {'identifier': 'deemed_modification_or_change_scope', 'raw_piece_count': 5, 'con (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'information_withheld_means_information_not_provided', 'raw_piece
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `identifier_glue_excess_mass_content`

- value: **23**  (from `identifier_glue.identifier_glue_excess_mass_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'information_withheld_means_information_not_provided', 'raw_piece; {'identifier': 'information_withheld_on_modification_or_change', 'raw_piece_coun; {'identifier': 'provide_information_on_modification_or_change', 'raw_piece_count (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'potentially_requires_change_to_method', 'raw_piece_count': 5, 'c; {'identifier': 'change_to_calculation_method', 'raw_piece_count': 4, 'content_pi; {'identifier': 'deemed_modification_or_change_scope', 'raw_piece_count': 5, 'con (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'information_withheld_means_information_not_provided', 'raw_piece
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `identifier_glue_excess_mass_raw`

- value: **27**  (from `identifier_glue.identifier_glue_excess_mass_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'information_withheld_means_information_not_provided', 'raw_piece; {'identifier': 'information_withheld_on_modification_or_change', 'raw_piece_coun; {'identifier': 'provide_information_on_modification_or_change', 'raw_piece_count (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'potentially_requires_change_to_method', 'raw_piece_count': 5, 'c; {'identifier': 'change_to_calculation_method', 'raw_piece_count': 4, 'content_pi; {'identifier': 'deemed_modification_or_change_scope', 'raw_piece_count': 5, 'con (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'information_withheld_means_information_not_provided', 'raw_piece
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `low_source_grounded_glued_identifier_count`

- value: **16**  (from `identifier_glue.low_source_grounded_glued_identifier_count`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'information_withheld_means_information_not_provided', 'raw_piece; {'identifier': 'information_withheld_on_modification_or_change', 'raw_piece_coun; {'identifier': 'provide_information_on_modification_or_change', 'raw_piece_count (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'potentially_requires_change_to_method', 'raw_piece_count': 5, 'c; {'identifier': 'change_to_calculation_method', 'raw_piece_count': 4, 'content_pi; {'identifier': 'deemed_modification_or_change_scope', 'raw_piece_count': 5, 'con (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'information_withheld_means_information_not_provided', 'raw_piece
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `max_identifier_piece_count_content`

- value: **5**  (from `identifier_glue.max_identifier_piece_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'information_withheld_means_information_not_provided', 'raw_piece; {'identifier': 'information_withheld_on_modification_or_change', 'raw_piece_coun; {'identifier': 'provide_information_on_modification_or_change', 'raw_piece_count (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'potentially_requires_change_to_method', 'raw_piece_count': 5, 'c; {'identifier': 'change_to_calculation_method', 'raw_piece_count': 4, 'content_pi; {'identifier': 'deemed_modification_or_change_scope', 'raw_piece_count': 5, 'con (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'information_withheld_means_information_not_provided', 'raw_piece
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `max_identifier_piece_count_raw`

- value: **6**  (from `identifier_glue.max_identifier_piece_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'information_withheld_means_information_not_provided', 'raw_piece; {'identifier': 'information_withheld_on_modification_or_change', 'raw_piece_coun; {'identifier': 'provide_information_on_modification_or_change', 'raw_piece_count (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'potentially_requires_change_to_method', 'raw_piece_count': 5, 'c; {'identifier': 'change_to_calculation_method', 'raw_piece_count': 4, 'content_pi; {'identifier': 'deemed_modification_or_change_scope', 'raw_piece_count': 5, 'con (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'information_withheld_means_information_not_provided', 'raw_piece
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `mean_identifier_piece_count_content`

- value: **1.9655172413793103**  (from `identifier_glue.mean_identifier_piece_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'information_withheld_means_information_not_provided', 'raw_piece; {'identifier': 'information_withheld_on_modification_or_change', 'raw_piece_coun; {'identifier': 'provide_information_on_modification_or_change', 'raw_piece_count (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'potentially_requires_change_to_method', 'raw_piece_count': 5, 'c; {'identifier': 'change_to_calculation_method', 'raw_piece_count': 4, 'content_pi; {'identifier': 'deemed_modification_or_change_scope', 'raw_piece_count': 5, 'con (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'information_withheld_means_information_not_provided', 'raw_piece
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `mean_identifier_piece_count_raw`

- value: **2.6724137931034484**  (from `identifier_glue.mean_identifier_piece_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'information_withheld_means_information_not_provided', 'raw_piece; {'identifier': 'information_withheld_on_modification_or_change', 'raw_piece_coun; {'identifier': 'provide_information_on_modification_or_change', 'raw_piece_count (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'potentially_requires_change_to_method', 'raw_piece_count': 5, 'c; {'identifier': 'change_to_calculation_method', 'raw_piece_count': 4, 'content_pi; {'identifier': 'deemed_modification_or_change_scope', 'raw_piece_count': 5, 'con (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'information_withheld_means_information_not_provided', 'raw_piece
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `new_formula_content_token_count_vs_text_only`

- value: **65**  (from `grounding.new_formula_content_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → application_by; application_of_method; apply_described_method (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; application_by; application_of_method (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'change', 'current_count': 27, 'baseline_count': 0, 'delta': 27}; {'token': 'modificationorchange', 'current_count': 15, 'baseline_count': 0, 'del; {'token': 'describedmethod', 'current_count': 14, 'baseline_count': 0, 'delta':  (+17 more)
  - `grounding.origin_error_count` → 12

## [WARNING] `ontology_planning` / `new_formula_token_count_vs_text_only`

- value: **67**  (from `grounding.new_formula_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → application_by; application_of_method; apply_described_method (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; application_by; application_of_method (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'change', 'current_count': 27, 'baseline_count': 0, 'delta': 27}; {'token': 'modificationorchange', 'current_count': 15, 'baseline_count': 0, 'del; {'token': 'describedmethod', 'current_count': 14, 'baseline_count': 0, 'delta':  (+17 more)
  - `grounding.origin_error_count` → 12

## [WARNING] `ontology_planning` / `new_full_surface_content_token_count_vs_text_only`

- value: **84**  (from `grounding.new_full_surface_content_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → application_by; application_of_method; apply_described_method (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; application_by; application_of_method (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'change', 'current_count': 27, 'baseline_count': 0, 'delta': 27}; {'token': 'modificationorchange', 'current_count': 15, 'baseline_count': 0, 'del; {'token': 'describedmethod', 'current_count': 14, 'baseline_count': 0, 'delta':  (+17 more)
  - `grounding.origin_error_count` → 12

## [WARNING] `ontology_planning` / `new_full_surface_token_count_vs_text_only`

- value: **89**  (from `grounding.new_full_surface_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → application_by; application_of_method; apply_described_method (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; application_by; application_of_method (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'change', 'current_count': 27, 'baseline_count': 0, 'delta': 27}; {'token': 'modificationorchange', 'current_count': 15, 'baseline_count': 0, 'del; {'token': 'describedmethod', 'current_count': 14, 'baseline_count': 0, 'delta':  (+17 more)
  - `grounding.origin_error_count` → 12

## [WARNING] `ontology_planning` / `new_surface_content_token_count`

- value: **159**  (from `<search recursive metrics JSON for key `new_surface_content_token_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → application_by; application_of_method; apply_described_method (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; application_by; application_of_method (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'change', 'current_count': 27, 'baseline_count': 0, 'delta': 27}; {'token': 'modificationorchange', 'current_count': 15, 'baseline_count': 0, 'del; {'token': 'describedmethod', 'current_count': 14, 'baseline_count': 0, 'delta':  (+17 more)
  - `grounding.origin_error_count` → 12

## [WARNING] `ontology_planning` / `new_surface_token_count`

- value: **159**  (from `<search recursive metrics JSON for key `new_surface_token_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → application_by; application_of_method; apply_described_method (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; application_by; application_of_method (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'change', 'current_count': 27, 'baseline_count': 0, 'delta': 27}; {'token': 'modificationorchange', 'current_count': 15, 'baseline_count': 0, 'del; {'token': 'describedmethod', 'current_count': 14, 'baseline_count': 0, 'delta':  (+17 more)
  - `grounding.origin_error_count` → 12

## [WARNING] `ontology_planning` / `ungrounded_sort_count`

- value: **8**  (from `grounding.ungrounded_sort_count`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → application_by; application_of_method; apply_described_method (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; application_by; application_of_method (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'change', 'current_count': 27, 'baseline_count': 0, 'delta': 27}; {'token': 'modificationorchange', 'current_count': 15, 'baseline_count': 0, 'del; {'token': 'describedmethod', 'current_count': 14, 'baseline_count': 0, 'delta':  (+17 more)
  - `grounding.origin_error_count` → 12

## [WARNING] `ontology_planning` / `ungrounded_symbol_count`

- value: **4**  (from `grounding.ungrounded_symbol_count`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → application_by; application_of_method; apply_described_method (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; application_by; application_of_method (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'change', 'current_count': 27, 'baseline_count': 0, 'delta': 27}; {'token': 'modificationorchange', 'current_count': 15, 'baseline_count': 0, 'del; {'token': 'describedmethod', 'current_count': 14, 'baseline_count': 0, 'delta':  (+17 more)
  - `grounding.origin_error_count` → 12
