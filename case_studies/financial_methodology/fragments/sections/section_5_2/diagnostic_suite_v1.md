# Diagnostic report — section_5_2

- **gate**: `needs_review`
- fail: 0, warning: 36

## [WARNING] `a4v3_semantic_lint` / `temporal_rel_in_deontic_context_count`

- value: **2**  (from `a4v3_semantic_lint_v1.json::summary.temporal_rel_in_deontic_context_count`)
- meaning: A deontic/temporal requirement may have been modeled as an ad-hoc ordinary relation.
- repair: Inspect whether the relation should be represented by deontic scope/deadline or a first-class temporal construct.
- evidence:
  - `a4v3_semantic_lint_v1.json::findings` → example_condition_changed_since_launch_of_index; reflects_reality_as_before

## [WARNING] `merge_canonicalization` / `callable_symbol_count`

- value: **24**  (from `parameterization.callable_symbol_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 24
  - `<related section in metrics JSON>` → 24

## [WARNING] `merge_canonicalization` / `callable_symbol_with_args_count`

- value: **24**  (from `parameterization.callable_symbol_with_args_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 24
  - `<related section in metrics JSON>` → 24

## [WARNING] `merge_canonicalization` / `cross_reference_usage_count`

- value: **3**  (from `<search recursive metrics JSON for key `cross_reference_usage_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `evidence.ir_cross_references` → body of announcement_section_location mentions section/annex; body of section_of_website mentions section/annex; entity Guideline : Document

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

- value: **24**  (from `parameterization.factorization_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 24
  - `<related section in metrics JSON>` → 24

## [WARNING] `merge_canonicalization` / `focus_signature_unique_count`

- value: **1**  (from `variability.focus_signature_unique_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.

## [WARNING] `merge_canonicalization` / `quantifier_parameter_slot_count`

- value: **8**  (from `parameterization.quantifier_parameter_slot_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `assertion_complexity.top_complex_assertions` → identified_need_has_review_identified_change; methodology_change_need_example_condition_scope; methodology_reviews_are_regular_at_least_annually (+2 more)
  - `assertion_complexity.max_assertion_depth` → 8
  - `assertion_complexity.total_quantifier_count` → 8

## [WARNING] `merge_canonicalization` / `top_level_parameter_slot_count`

- value: **43**  (from `parameterization.top_level_parameter_slot_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 43
  - `<related section in metrics JSON>` → 43

## [WARNING] `merge_canonicalization` / `total_parameter_slot_mass`

- value: **51**  (from `parameterization.total_parameter_slot_mass`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 51
  - `<related section in metrics JSON>` → 51

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

- value: **22**  (from `identifier_glue.compound_identifier_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'no_longer_reflects_reality_condition_means_not_reflects_reality_; {'identifier': 'HttpsWwwSolactiveComDocumentsMethodologyPolicy', 'raw_piece_coun; {'identifier': 'methodology_subject_to_regular_review_at_least_annually', 'raw_p (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'example_condition_reflection_quality', 'raw_piece_count': 4, 'co; {'identifier': 'DocumentPart', 'raw_piece_count': 2, 'content_piece_count': 2, '; {'identifier': 'MethodologyReview', 'raw_piece_count': 2, 'content_piece_count': (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'no_longer_reflects_reality_condition_means_not_reflects_reality_
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `compound_identifier_count_raw`

- value: **21**  (from `identifier_glue.compound_identifier_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'no_longer_reflects_reality_condition_means_not_reflects_reality_; {'identifier': 'HttpsWwwSolactiveComDocumentsMethodologyPolicy', 'raw_piece_coun; {'identifier': 'methodology_subject_to_regular_review_at_least_annually', 'raw_p (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'example_condition_reflection_quality', 'raw_piece_count': 4, 'co; {'identifier': 'DocumentPart', 'raw_piece_count': 2, 'content_piece_count': 2, '; {'identifier': 'MethodologyReview', 'raw_piece_count': 2, 'content_piece_count': (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'no_longer_reflects_reality_condition_means_not_reflects_reality_
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `cross_reference_usage_count`

- value: **3**  (from `<search recursive metrics JSON for key `cross_reference_usage_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `evidence.ir_cross_references` → body of announcement_section_location mentions section/annex; body of section_of_website mentions section/annex; entity Guideline : Document

## [WARNING] `ontology_planning` / `dependency_link_count`

- value: **4**  (from `<search recursive metrics JSON for key `dependency_link_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 4
  - `<related section in metrics JSON>` → 4

## [WARNING] `ontology_planning` / `identifier_count`

- value: **59**  (from `identifier_glue.identifier_count`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'no_longer_reflects_reality_condition_means_not_reflects_reality_; {'identifier': 'HttpsWwwSolactiveComDocumentsMethodologyPolicy', 'raw_piece_coun; {'identifier': 'methodology_subject_to_regular_review_at_least_annually', 'raw_p (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'example_condition_reflection_quality', 'raw_piece_count': 4, 'co; {'identifier': 'DocumentPart', 'raw_piece_count': 2, 'content_piece_count': 2, '; {'identifier': 'MethodologyReview', 'raw_piece_count': 2, 'content_piece_count': (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'no_longer_reflects_reality_condition_means_not_reflects_reality_
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `identifier_glue_excess_mass_content`

- value: **59**  (from `identifier_glue.identifier_glue_excess_mass_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'no_longer_reflects_reality_condition_means_not_reflects_reality_; {'identifier': 'HttpsWwwSolactiveComDocumentsMethodologyPolicy', 'raw_piece_coun; {'identifier': 'methodology_subject_to_regular_review_at_least_annually', 'raw_p (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'example_condition_reflection_quality', 'raw_piece_count': 4, 'co; {'identifier': 'DocumentPart', 'raw_piece_count': 2, 'content_piece_count': 2, '; {'identifier': 'MethodologyReview', 'raw_piece_count': 2, 'content_piece_count': (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'no_longer_reflects_reality_condition_means_not_reflects_reality_
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `identifier_glue_excess_mass_raw`

- value: **54**  (from `identifier_glue.identifier_glue_excess_mass_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'no_longer_reflects_reality_condition_means_not_reflects_reality_; {'identifier': 'HttpsWwwSolactiveComDocumentsMethodologyPolicy', 'raw_piece_coun; {'identifier': 'methodology_subject_to_regular_review_at_least_annually', 'raw_p (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'example_condition_reflection_quality', 'raw_piece_count': 4, 'co; {'identifier': 'DocumentPart', 'raw_piece_count': 2, 'content_piece_count': 2, '; {'identifier': 'MethodologyReview', 'raw_piece_count': 2, 'content_piece_count': (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'no_longer_reflects_reality_condition_means_not_reflects_reality_
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `invented_helper_sort_count`

- value: **1**  (from `<search recursive metrics JSON for key `invented_helper_sort_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → accuracy; amendment_date; amendment_of_index (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; accuracy; amendment_date (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'condition', 'current_count': 24, 'baseline_count': 0, 'delta': 24}; {'token': 'example', 'current_count': 23, 'baseline_count': 0, 'delta': 23}; {'token': 'change', 'current_count': 21, 'baseline_count': 3, 'delta': 18} (+17 more)
  - `grounding.origin_error_count` → 20
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'no_longer_reflects_reality_condition_means_not_reflects_reality_; {'identifier': 'HttpsWwwSolactiveComDocumentsMethodologyPolicy', 'raw_piece_coun; {'identifier': 'methodology_subject_to_regular_review_at_least_annually', 'raw_p (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'example_condition_reflection_quality', 'raw_piece_count': 4, 'co; {'identifier': 'DocumentPart', 'raw_piece_count': 2, 'content_piece_count': 2, '; {'identifier': 'MethodologyReview', 'raw_piece_count': 2, 'content_piece_count': (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'no_longer_reflects_reality_condition_means_not_reflects_reality_
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)
  - `evidence.invented_helper_sorts` → ReflectionQuality

## [WARNING] `ontology_planning` / `invented_helper_symbol_count`

- value: **1**  (from `<search recursive metrics JSON for key `invented_helper_symbol_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → accuracy; amendment_date; amendment_of_index (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; accuracy; amendment_date (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'condition', 'current_count': 24, 'baseline_count': 0, 'delta': 24}; {'token': 'example', 'current_count': 23, 'baseline_count': 0, 'delta': 23}; {'token': 'change', 'current_count': 21, 'baseline_count': 3, 'delta': 18} (+17 more)
  - `grounding.origin_error_count` → 20
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'no_longer_reflects_reality_condition_means_not_reflects_reality_; {'identifier': 'HttpsWwwSolactiveComDocumentsMethodologyPolicy', 'raw_piece_coun; {'identifier': 'methodology_subject_to_regular_review_at_least_annually', 'raw_p (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'example_condition_reflection_quality', 'raw_piece_count': 4, 'co; {'identifier': 'DocumentPart', 'raw_piece_count': 2, 'content_piece_count': 2, '; {'identifier': 'MethodologyReview', 'raw_piece_count': 2, 'content_piece_count': (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'no_longer_reflects_reality_condition_means_not_reflects_reality_
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)
  - `evidence.invented_helper_sorts` → ReflectionQuality

## [WARNING] `ontology_planning` / `low_source_grounded_glued_identifier_count`

- value: **15**  (from `identifier_glue.low_source_grounded_glued_identifier_count`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'no_longer_reflects_reality_condition_means_not_reflects_reality_; {'identifier': 'HttpsWwwSolactiveComDocumentsMethodologyPolicy', 'raw_piece_coun; {'identifier': 'methodology_subject_to_regular_review_at_least_annually', 'raw_p (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'example_condition_reflection_quality', 'raw_piece_count': 4, 'co; {'identifier': 'DocumentPart', 'raw_piece_count': 2, 'content_piece_count': 2, '; {'identifier': 'MethodologyReview', 'raw_piece_count': 2, 'content_piece_count': (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'no_longer_reflects_reality_condition_means_not_reflects_reality_
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `max_identifier_piece_count_content`

- value: **8**  (from `identifier_glue.max_identifier_piece_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'no_longer_reflects_reality_condition_means_not_reflects_reality_; {'identifier': 'HttpsWwwSolactiveComDocumentsMethodologyPolicy', 'raw_piece_coun; {'identifier': 'methodology_subject_to_regular_review_at_least_annually', 'raw_p (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'example_condition_reflection_quality', 'raw_piece_count': 4, 'co; {'identifier': 'DocumentPart', 'raw_piece_count': 2, 'content_piece_count': 2, '; {'identifier': 'MethodologyReview', 'raw_piece_count': 2, 'content_piece_count': (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'no_longer_reflects_reality_condition_means_not_reflects_reality_
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `max_identifier_piece_count_raw`

- value: **11**  (from `identifier_glue.max_identifier_piece_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'no_longer_reflects_reality_condition_means_not_reflects_reality_; {'identifier': 'HttpsWwwSolactiveComDocumentsMethodologyPolicy', 'raw_piece_coun; {'identifier': 'methodology_subject_to_regular_review_at_least_annually', 'raw_p (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'example_condition_reflection_quality', 'raw_piece_count': 4, 'co; {'identifier': 'DocumentPart', 'raw_piece_count': 2, 'content_piece_count': 2, '; {'identifier': 'MethodologyReview', 'raw_piece_count': 2, 'content_piece_count': (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'no_longer_reflects_reality_condition_means_not_reflects_reality_
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `mean_identifier_piece_count_content`

- value: **2.6440677966101696**  (from `identifier_glue.mean_identifier_piece_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'no_longer_reflects_reality_condition_means_not_reflects_reality_; {'identifier': 'HttpsWwwSolactiveComDocumentsMethodologyPolicy', 'raw_piece_coun; {'identifier': 'methodology_subject_to_regular_review_at_least_annually', 'raw_p (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'example_condition_reflection_quality', 'raw_piece_count': 4, 'co; {'identifier': 'DocumentPart', 'raw_piece_count': 2, 'content_piece_count': 2, '; {'identifier': 'MethodologyReview', 'raw_piece_count': 2, 'content_piece_count': (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'no_longer_reflects_reality_condition_means_not_reflects_reality_
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `mean_identifier_piece_count_raw`

- value: **3.23728813559322**  (from `identifier_glue.mean_identifier_piece_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'no_longer_reflects_reality_condition_means_not_reflects_reality_; {'identifier': 'HttpsWwwSolactiveComDocumentsMethodologyPolicy', 'raw_piece_coun; {'identifier': 'methodology_subject_to_regular_review_at_least_annually', 'raw_p (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'example_condition_reflection_quality', 'raw_piece_count': 4, 'co; {'identifier': 'DocumentPart', 'raw_piece_count': 2, 'content_piece_count': 2, '; {'identifier': 'MethodologyReview', 'raw_piece_count': 2, 'content_piece_count': (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'no_longer_reflects_reality_condition_means_not_reflects_reality_
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `new_formula_content_token_count_vs_text_only`

- value: **68**  (from `grounding.new_formula_content_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → accuracy; amendment_date; amendment_of_index (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; accuracy; amendment_date (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'condition', 'current_count': 24, 'baseline_count': 0, 'delta': 24}; {'token': 'example', 'current_count': 23, 'baseline_count': 0, 'delta': 23}; {'token': 'change', 'current_count': 21, 'baseline_count': 3, 'delta': 18} (+17 more)
  - `grounding.origin_error_count` → 20

## [WARNING] `ontology_planning` / `new_formula_token_count_vs_text_only`

- value: **74**  (from `grounding.new_formula_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → accuracy; amendment_date; amendment_of_index (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; accuracy; amendment_date (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'condition', 'current_count': 24, 'baseline_count': 0, 'delta': 24}; {'token': 'example', 'current_count': 23, 'baseline_count': 0, 'delta': 23}; {'token': 'change', 'current_count': 21, 'baseline_count': 3, 'delta': 18} (+17 more)
  - `grounding.origin_error_count` → 20

## [WARNING] `ontology_planning` / `new_full_surface_content_token_count_vs_text_only`

- value: **87**  (from `grounding.new_full_surface_content_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → accuracy; amendment_date; amendment_of_index (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; accuracy; amendment_date (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'condition', 'current_count': 24, 'baseline_count': 0, 'delta': 24}; {'token': 'example', 'current_count': 23, 'baseline_count': 0, 'delta': 23}; {'token': 'change', 'current_count': 21, 'baseline_count': 3, 'delta': 18} (+17 more)
  - `grounding.origin_error_count` → 20

## [WARNING] `ontology_planning` / `new_full_surface_token_count_vs_text_only`

- value: **97**  (from `grounding.new_full_surface_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → accuracy; amendment_date; amendment_of_index (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; accuracy; amendment_date (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'condition', 'current_count': 24, 'baseline_count': 0, 'delta': 24}; {'token': 'example', 'current_count': 23, 'baseline_count': 0, 'delta': 23}; {'token': 'change', 'current_count': 21, 'baseline_count': 3, 'delta': 18} (+17 more)
  - `grounding.origin_error_count` → 20

## [WARNING] `ontology_planning` / `new_surface_content_token_count`

- value: **175**  (from `<search recursive metrics JSON for key `new_surface_content_token_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → accuracy; amendment_date; amendment_of_index (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; accuracy; amendment_date (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'condition', 'current_count': 24, 'baseline_count': 0, 'delta': 24}; {'token': 'example', 'current_count': 23, 'baseline_count': 0, 'delta': 23}; {'token': 'change', 'current_count': 21, 'baseline_count': 3, 'delta': 18} (+17 more)
  - `grounding.origin_error_count` → 20

## [WARNING] `ontology_planning` / `new_surface_token_count`

- value: **175**  (from `<search recursive metrics JSON for key `new_surface_token_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → accuracy; amendment_date; amendment_of_index (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; accuracy; amendment_date (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'condition', 'current_count': 24, 'baseline_count': 0, 'delta': 24}; {'token': 'example', 'current_count': 23, 'baseline_count': 0, 'delta': 23}; {'token': 'change', 'current_count': 21, 'baseline_count': 3, 'delta': 18} (+17 more)
  - `grounding.origin_error_count` → 20

## [WARNING] `ontology_planning` / `ungrounded_sort_count`

- value: **12**  (from `grounding.ungrounded_sort_count`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → accuracy; amendment_date; amendment_of_index (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; accuracy; amendment_date (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'condition', 'current_count': 24, 'baseline_count': 0, 'delta': 24}; {'token': 'example', 'current_count': 23, 'baseline_count': 0, 'delta': 23}; {'token': 'change', 'current_count': 21, 'baseline_count': 3, 'delta': 18} (+17 more)
  - `grounding.origin_error_count` → 20

## [WARNING] `ontology_planning` / `ungrounded_symbol_count`

- value: **8**  (from `grounding.ungrounded_symbol_count`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → accuracy; amendment_date; amendment_of_index (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; accuracy; amendment_date (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'condition', 'current_count': 24, 'baseline_count': 0, 'delta': 24}; {'token': 'example', 'current_count': 23, 'baseline_count': 0, 'delta': 23}; {'token': 'change', 'current_count': 21, 'baseline_count': 3, 'delta': 18} (+17 more)
  - `grounding.origin_error_count` → 20
