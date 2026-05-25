# Diagnostic report — section_3_1

- **gate**: `needs_review`
- fail: 0, warning: 33

## [WARNING] `merge_canonicalization` / `callable_symbol_count`

- value: **33**  (from `parameterization.callable_symbol_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 33
  - `<related section in metrics JSON>` → 33

## [WARNING] `merge_canonicalization` / `callable_symbol_with_args_count`

- value: **33**  (from `parameterization.callable_symbol_with_args_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 33
  - `<related section in metrics JSON>` → 33

## [WARNING] `merge_canonicalization` / `cross_reference_usage_count`

- value: **3**  (from `<search recursive metrics JSON for key `cross_reference_usage_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `evidence.ir_cross_references` → body of announcement_section_location mentions section/annex; body of section_of_website mentions section/annex; entity ThisGuideline : Document

## [WARNING] `merge_canonicalization` / `dependency_link_count`

- value: **3**  (from `<search recursive metrics JSON for key `dependency_link_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 3
  - `<related section in metrics JSON>` → 3

## [WARNING] `merge_canonicalization` / `draft_variant_count`

- value: **1**  (from `variants.draft_variant_count`)
- meaning: A merge/variant/gold comparison changed structure or semantics; report exact compared variants or merge rows.
- repair: Use overlay/bridge/conflict split or reject rewrite based on backtest.

## [WARNING] `merge_canonicalization` / `factorization_count`

- value: **33**  (from `parameterization.factorization_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 33
  - `<related section in metrics JSON>` → 33

## [WARNING] `merge_canonicalization` / `focus_signature_unique_count`

- value: **1**  (from `variability.focus_signature_unique_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.

## [WARNING] `merge_canonicalization` / `quantifier_parameter_slot_count`

- value: **14**  (from `parameterization.quantifier_parameter_slot_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `assertion_complexity.top_complex_assertions` → ordinary_rebalance_implements_fixing_day_shares; ordinary_rebalance_adjusts_index_after_close_of_business; new_selection_determined_in_accordance_with_sections (+2 more)
  - `assertion_complexity.max_assertion_depth` → 10
  - `assertion_complexity.total_quantifier_count` → 14

## [WARNING] `merge_canonicalization` / `top_level_parameter_slot_count`

- value: **63**  (from `parameterization.top_level_parameter_slot_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 63
  - `<related section in metrics JSON>` → 63

## [WARNING] `merge_canonicalization` / `total_parameter_slot_mass`

- value: **77**  (from `parameterization.total_parameter_slot_mass`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 77
  - `<related section in metrics JSON>` → 77

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

- value: **32**  (from `identifier_glue.compound_identifier_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'HttpsWwwSolactiveComDocumentsEquityIndexMethodology', 'raw_piece; {'identifier': 'ordinary_rebalance_adjusts_index_after_close_of_business', 'raw_; {'identifier': 'solactive_publishes_index_component_changes_with_notice', 'raw_p (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DocumentPart', 'raw_piece_count': 2, 'content_piece_count': 2, '; {'identifier': 'OrdinaryRebalance', 'raw_piece_count': 2, 'content_piece_count':; {'identifier': 'VagueTerm', 'raw_piece_count': 2, 'content_piece_count': 2, 'raw (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'SufficientNoticeBeforeRebalanceDay', 'raw_piece_count': 5, 'cont
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'new_selection_determined_in_accordance_with_sections', 'raw_piec

## [WARNING] `ontology_planning` / `compound_identifier_count_raw`

- value: **27**  (from `identifier_glue.compound_identifier_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'HttpsWwwSolactiveComDocumentsEquityIndexMethodology', 'raw_piece; {'identifier': 'ordinary_rebalance_adjusts_index_after_close_of_business', 'raw_; {'identifier': 'solactive_publishes_index_component_changes_with_notice', 'raw_p (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DocumentPart', 'raw_piece_count': 2, 'content_piece_count': 2, '; {'identifier': 'OrdinaryRebalance', 'raw_piece_count': 2, 'content_piece_count':; {'identifier': 'VagueTerm', 'raw_piece_count': 2, 'content_piece_count': 2, 'raw (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'SufficientNoticeBeforeRebalanceDay', 'raw_piece_count': 5, 'cont
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'new_selection_determined_in_accordance_with_sections', 'raw_piec

## [WARNING] `ontology_planning` / `cross_reference_usage_count`

- value: **3**  (from `<search recursive metrics JSON for key `cross_reference_usage_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `evidence.ir_cross_references` → body of announcement_section_location mentions section/annex; body of section_of_website mentions section/annex; entity ThisGuideline : Document

## [WARNING] `ontology_planning` / `dependency_link_count`

- value: **3**  (from `<search recursive metrics JSON for key `dependency_link_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 3
  - `<related section in metrics JSON>` → 3

## [WARNING] `ontology_planning` / `identifier_count`

- value: **81**  (from `identifier_glue.identifier_count`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'HttpsWwwSolactiveComDocumentsEquityIndexMethodology', 'raw_piece; {'identifier': 'ordinary_rebalance_adjusts_index_after_close_of_business', 'raw_; {'identifier': 'solactive_publishes_index_component_changes_with_notice', 'raw_p (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DocumentPart', 'raw_piece_count': 2, 'content_piece_count': 2, '; {'identifier': 'OrdinaryRebalance', 'raw_piece_count': 2, 'content_piece_count':; {'identifier': 'VagueTerm', 'raw_piece_count': 2, 'content_piece_count': 2, 'raw (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'SufficientNoticeBeforeRebalanceDay', 'raw_piece_count': 5, 'cont
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'new_selection_determined_in_accordance_with_sections', 'raw_piec

## [WARNING] `ontology_planning` / `identifier_glue_excess_mass_content`

- value: **61**  (from `identifier_glue.identifier_glue_excess_mass_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'HttpsWwwSolactiveComDocumentsEquityIndexMethodology', 'raw_piece; {'identifier': 'ordinary_rebalance_adjusts_index_after_close_of_business', 'raw_; {'identifier': 'solactive_publishes_index_component_changes_with_notice', 'raw_p (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DocumentPart', 'raw_piece_count': 2, 'content_piece_count': 2, '; {'identifier': 'OrdinaryRebalance', 'raw_piece_count': 2, 'content_piece_count':; {'identifier': 'VagueTerm', 'raw_piece_count': 2, 'content_piece_count': 2, 'raw (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'SufficientNoticeBeforeRebalanceDay', 'raw_piece_count': 5, 'cont
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'new_selection_determined_in_accordance_with_sections', 'raw_piec

## [WARNING] `ontology_planning` / `identifier_glue_excess_mass_raw`

- value: **54**  (from `identifier_glue.identifier_glue_excess_mass_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'HttpsWwwSolactiveComDocumentsEquityIndexMethodology', 'raw_piece; {'identifier': 'ordinary_rebalance_adjusts_index_after_close_of_business', 'raw_; {'identifier': 'solactive_publishes_index_component_changes_with_notice', 'raw_p (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DocumentPart', 'raw_piece_count': 2, 'content_piece_count': 2, '; {'identifier': 'OrdinaryRebalance', 'raw_piece_count': 2, 'content_piece_count':; {'identifier': 'VagueTerm', 'raw_piece_count': 2, 'content_piece_count': 2, 'raw (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'SufficientNoticeBeforeRebalanceDay', 'raw_piece_count': 5, 'cont
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'new_selection_determined_in_accordance_with_sections', 'raw_piec

## [WARNING] `ontology_planning` / `low_source_grounded_glued_identifier_count`

- value: **23**  (from `identifier_glue.low_source_grounded_glued_identifier_count`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'HttpsWwwSolactiveComDocumentsEquityIndexMethodology', 'raw_piece; {'identifier': 'ordinary_rebalance_adjusts_index_after_close_of_business', 'raw_; {'identifier': 'solactive_publishes_index_component_changes_with_notice', 'raw_p (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DocumentPart', 'raw_piece_count': 2, 'content_piece_count': 2, '; {'identifier': 'OrdinaryRebalance', 'raw_piece_count': 2, 'content_piece_count':; {'identifier': 'VagueTerm', 'raw_piece_count': 2, 'content_piece_count': 2, 'raw (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'SufficientNoticeBeforeRebalanceDay', 'raw_piece_count': 5, 'cont
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'new_selection_determined_in_accordance_with_sections', 'raw_piec

## [WARNING] `ontology_planning` / `max_identifier_piece_count_content`

- value: **8**  (from `identifier_glue.max_identifier_piece_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'HttpsWwwSolactiveComDocumentsEquityIndexMethodology', 'raw_piece; {'identifier': 'ordinary_rebalance_adjusts_index_after_close_of_business', 'raw_; {'identifier': 'solactive_publishes_index_component_changes_with_notice', 'raw_p (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DocumentPart', 'raw_piece_count': 2, 'content_piece_count': 2, '; {'identifier': 'OrdinaryRebalance', 'raw_piece_count': 2, 'content_piece_count':; {'identifier': 'VagueTerm', 'raw_piece_count': 2, 'content_piece_count': 2, 'raw (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'SufficientNoticeBeforeRebalanceDay', 'raw_piece_count': 5, 'cont
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'new_selection_determined_in_accordance_with_sections', 'raw_piec

## [WARNING] `ontology_planning` / `max_identifier_piece_count_raw`

- value: **8**  (from `identifier_glue.max_identifier_piece_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'HttpsWwwSolactiveComDocumentsEquityIndexMethodology', 'raw_piece; {'identifier': 'ordinary_rebalance_adjusts_index_after_close_of_business', 'raw_; {'identifier': 'solactive_publishes_index_component_changes_with_notice', 'raw_p (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DocumentPart', 'raw_piece_count': 2, 'content_piece_count': 2, '; {'identifier': 'OrdinaryRebalance', 'raw_piece_count': 2, 'content_piece_count':; {'identifier': 'VagueTerm', 'raw_piece_count': 2, 'content_piece_count': 2, 'raw (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'SufficientNoticeBeforeRebalanceDay', 'raw_piece_count': 5, 'cont
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'new_selection_determined_in_accordance_with_sections', 'raw_piec

## [WARNING] `ontology_planning` / `mean_identifier_piece_count_content`

- value: **2.382716049382716**  (from `identifier_glue.mean_identifier_piece_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'HttpsWwwSolactiveComDocumentsEquityIndexMethodology', 'raw_piece; {'identifier': 'ordinary_rebalance_adjusts_index_after_close_of_business', 'raw_; {'identifier': 'solactive_publishes_index_component_changes_with_notice', 'raw_p (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DocumentPart', 'raw_piece_count': 2, 'content_piece_count': 2, '; {'identifier': 'OrdinaryRebalance', 'raw_piece_count': 2, 'content_piece_count':; {'identifier': 'VagueTerm', 'raw_piece_count': 2, 'content_piece_count': 2, 'raw (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'SufficientNoticeBeforeRebalanceDay', 'raw_piece_count': 5, 'cont
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'new_selection_determined_in_accordance_with_sections', 'raw_piec

## [WARNING] `ontology_planning` / `mean_identifier_piece_count_raw`

- value: **3.0246913580246915**  (from `identifier_glue.mean_identifier_piece_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'HttpsWwwSolactiveComDocumentsEquityIndexMethodology', 'raw_piece; {'identifier': 'ordinary_rebalance_adjusts_index_after_close_of_business', 'raw_; {'identifier': 'solactive_publishes_index_component_changes_with_notice', 'raw_p (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DocumentPart', 'raw_piece_count': 2, 'content_piece_count': 2, '; {'identifier': 'OrdinaryRebalance', 'raw_piece_count': 2, 'content_piece_count':; {'identifier': 'VagueTerm', 'raw_piece_count': 2, 'content_piece_count': 2, 'raw (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'SufficientNoticeBeforeRebalanceDay', 'raw_piece_count': 5, 'cont
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'new_selection_determined_in_accordance_with_sections', 'raw_piec

## [WARNING] `ontology_planning` / `new_formula_content_token_count_vs_text_only`

- value: **77**  (from `grounding.new_formula_content_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → adjusted_index; announcement_section_location; announcementsection (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; adjusted_index; announcement_section_location (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'selection', 'current_count': 25, 'baseline_count': 3, 'delta': 22}; {'token': 'notice', 'current_count': 21, 'baseline_count': 1, 'delta': 20}; {'token': 'index', 'current_count': 22, 'baseline_count': 6, 'delta': 16} (+17 more)
  - `grounding.origin_error_count` → 22

## [WARNING] `ontology_planning` / `new_formula_token_count_vs_text_only`

- value: **86**  (from `grounding.new_formula_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → adjusted_index; announcement_section_location; announcementsection (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; adjusted_index; announcement_section_location (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'selection', 'current_count': 25, 'baseline_count': 3, 'delta': 22}; {'token': 'notice', 'current_count': 21, 'baseline_count': 1, 'delta': 20}; {'token': 'index', 'current_count': 22, 'baseline_count': 6, 'delta': 16} (+17 more)
  - `grounding.origin_error_count` → 22

## [WARNING] `ontology_planning` / `new_full_surface_content_token_count_vs_text_only`

- value: **96**  (from `grounding.new_full_surface_content_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → adjusted_index; announcement_section_location; announcementsection (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; adjusted_index; announcement_section_location (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'selection', 'current_count': 25, 'baseline_count': 3, 'delta': 22}; {'token': 'notice', 'current_count': 21, 'baseline_count': 1, 'delta': 20}; {'token': 'index', 'current_count': 22, 'baseline_count': 6, 'delta': 16} (+17 more)
  - `grounding.origin_error_count` → 22

## [WARNING] `ontology_planning` / `new_full_surface_token_count_vs_text_only`

- value: **108**  (from `grounding.new_full_surface_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → adjusted_index; announcement_section_location; announcementsection (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; adjusted_index; announcement_section_location (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'selection', 'current_count': 25, 'baseline_count': 3, 'delta': 22}; {'token': 'notice', 'current_count': 21, 'baseline_count': 1, 'delta': 20}; {'token': 'index', 'current_count': 22, 'baseline_count': 6, 'delta': 16} (+17 more)
  - `grounding.origin_error_count` → 22

## [WARNING] `ontology_planning` / `new_surface_content_token_count`

- value: **193**  (from `<search recursive metrics JSON for key `new_surface_content_token_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → adjusted_index; announcement_section_location; announcementsection (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; adjusted_index; announcement_section_location (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'selection', 'current_count': 25, 'baseline_count': 3, 'delta': 22}; {'token': 'notice', 'current_count': 21, 'baseline_count': 1, 'delta': 20}; {'token': 'index', 'current_count': 22, 'baseline_count': 6, 'delta': 16} (+17 more)
  - `grounding.origin_error_count` → 22

## [WARNING] `ontology_planning` / `new_surface_token_count`

- value: **193**  (from `<search recursive metrics JSON for key `new_surface_token_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → adjusted_index; announcement_section_location; announcementsection (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; adjusted_index; announcement_section_location (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'selection', 'current_count': 25, 'baseline_count': 3, 'delta': 22}; {'token': 'notice', 'current_count': 21, 'baseline_count': 1, 'delta': 20}; {'token': 'index', 'current_count': 22, 'baseline_count': 6, 'delta': 16} (+17 more)
  - `grounding.origin_error_count` → 22

## [WARNING] `ontology_planning` / `ungrounded_sort_count`

- value: **17**  (from `grounding.ungrounded_sort_count`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → adjusted_index; announcement_section_location; announcementsection (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; adjusted_index; announcement_section_location (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'selection', 'current_count': 25, 'baseline_count': 3, 'delta': 22}; {'token': 'notice', 'current_count': 21, 'baseline_count': 1, 'delta': 20}; {'token': 'index', 'current_count': 22, 'baseline_count': 6, 'delta': 16} (+17 more)
  - `grounding.origin_error_count` → 22

## [WARNING] `ontology_planning` / `ungrounded_symbol_count`

- value: **4**  (from `grounding.ungrounded_symbol_count`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → adjusted_index; announcement_section_location; announcementsection (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; adjusted_index; announcement_section_location (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'selection', 'current_count': 25, 'baseline_count': 3, 'delta': 22}; {'token': 'notice', 'current_count': 21, 'baseline_count': 1, 'delta': 20}; {'token': 'index', 'current_count': 22, 'baseline_count': 6, 'delta': 16} (+17 more)
  - `grounding.origin_error_count` → 22
