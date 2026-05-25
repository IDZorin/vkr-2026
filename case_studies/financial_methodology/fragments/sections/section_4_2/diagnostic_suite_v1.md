# Diagnostic report — section_4_2

- **gate**: `needs_review`
- fail: 0, warning: 39

## [WARNING] `a4v3_semantic_lint` / `shared_name_token_without_structural_carrier_count`

- value: **2**  (from `a4v3_semantic_lint_v1.json::summary.shared_name_token_without_structural_carrier_count`)
- meaning: A semantic link may be encoded only by repeated words inside predicate names, rather than by an explicit shared entity/sort/argument in formula structure.
- repair: Introduce a structural carrier for the repeated concept, e.g. a sort/entity and relation arguments, or document why the repeated token is intentionally only lexical.
- evidence:
  - `a4v3_semantic_lint_v1.json::findings` → after; {'check': 'shared_name_token_without_structural_carrier', 'severity': 'soft', 'c; {'check': 'shared_name_token_without_structural_carrier', 'severity': 'soft', 'c

## [WARNING] `a4v3_semantic_lint` / `temporal_rel_in_deontic_context_count`

- value: **1**  (from `a4v3_semantic_lint_v1.json::summary.temporal_rel_in_deontic_context_count`)
- meaning: A deontic/temporal requirement may have been modeled as an ad-hoc ordinary relation.
- repair: Inspect whether the relation should be represented by deontic scope/deadline or a first-class temporal construct.
- evidence:
  - `a4v3_semantic_lint_v1.json::findings` → after; {'check': 'shared_name_token_without_structural_carrier', 'severity': 'soft', 'c; {'check': 'shared_name_token_without_structural_carrier', 'severity': 'soft', 'c

## [WARNING] `merge_canonicalization` / `callable_symbol_count`

- value: **15**  (from `parameterization.callable_symbol_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 15
  - `<related section in metrics JSON>` → 15

## [WARNING] `merge_canonicalization` / `callable_symbol_with_args_count`

- value: **15**  (from `parameterization.callable_symbol_with_args_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 15
  - `<related section in metrics JSON>` → 15

## [WARNING] `merge_canonicalization` / `cross_reference_dropout_count`

- value: **2**  (from `<search recursive metrics JSON for key `cross_reference_dropout_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `evidence.source_cross_references` → Section 4.2; section “News”
  - `evidence.ir_cross_references` → body of news_section_location mentions section/annex; body of section_of_website mentions section/annex

## [WARNING] `merge_canonicalization` / `cross_reference_usage_count`

- value: **2**  (from `<search recursive metrics JSON for key `cross_reference_usage_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `evidence.ir_cross_references` → body of news_section_location mentions section/annex; body of section_of_website mentions section/annex

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

- value: **15**  (from `parameterization.factorization_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 15
  - `<related section in metrics JSON>` → 15

## [WARNING] `merge_canonicalization` / `focus_signature_unique_count`

- value: **1**  (from `variability.focus_signature_unique_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.

## [WARNING] `merge_canonicalization` / `quantifier_parameter_slot_count`

- value: **6**  (from `parameterization.quantifier_parameter_slot_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `assertion_complexity.top_complex_assertions` → termination_and_announcement_at_zero_or_below; other_reason_termination_in_accordance_with_solactive_policies
  - `assertion_complexity.max_assertion_depth` → 8
  - `assertion_complexity.total_quantifier_count` → 6

## [WARNING] `merge_canonicalization` / `top_level_parameter_slot_count`

- value: **29**  (from `parameterization.top_level_parameter_slot_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 29
  - `<related section in metrics JSON>` → 29

## [WARNING] `merge_canonicalization` / `total_parameter_slot_mass`

- value: **35**  (from `parameterization.total_parameter_slot_mass`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 35
  - `<related section in metrics JSON>` → 35

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
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'other_reason_termination_in_accordance_with_solactive_policies',; {'identifier': 'HttpsWwwSolactiveComNewsAnnouncements', 'raw_piece_count': 6, 'c; {'identifier': 'termination_and_announcement_at_zero_or_below', 'raw_piece_count (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'announcement_timing_described_by', 'raw_piece_count': 4, 'conten; {'identifier': 'termination_reason_qualified_by', 'raw_piece_count': 4, 'content; {'identifier': 'announces_termination', 'raw_piece_count': 2, 'content_piece_cou (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `compound_identifier_count_raw`

- value: **7**  (from `identifier_glue.compound_identifier_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'other_reason_termination_in_accordance_with_solactive_policies',; {'identifier': 'HttpsWwwSolactiveComNewsAnnouncements', 'raw_piece_count': 6, 'c; {'identifier': 'termination_and_announcement_at_zero_or_below', 'raw_piece_count (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'announcement_timing_described_by', 'raw_piece_count': 4, 'conten; {'identifier': 'termination_reason_qualified_by', 'raw_piece_count': 4, 'content; {'identifier': 'announces_termination', 'raw_piece_count': 2, 'content_piece_cou (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `cross_reference_dropout_count`

- value: **2**  (from `<search recursive metrics JSON for key `cross_reference_dropout_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `evidence.source_cross_references` → Section 4.2; section “News”
  - `evidence.ir_cross_references` → body of news_section_location mentions section/annex; body of section_of_website mentions section/annex

## [WARNING] `ontology_planning` / `cross_reference_usage_count`

- value: **2**  (from `<search recursive metrics JSON for key `cross_reference_usage_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `evidence.ir_cross_references` → body of news_section_location mentions section/annex; body of section_of_website mentions section/annex

## [WARNING] `ontology_planning` / `dependency_link_count`

- value: **2**  (from `<search recursive metrics JSON for key `dependency_link_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 2
  - `<related section in metrics JSON>` → 2

## [WARNING] `ontology_planning` / `identifier_count`

- value: **42**  (from `identifier_glue.identifier_count`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'other_reason_termination_in_accordance_with_solactive_policies',; {'identifier': 'HttpsWwwSolactiveComNewsAnnouncements', 'raw_piece_count': 6, 'c; {'identifier': 'termination_and_announcement_at_zero_or_below', 'raw_piece_count (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'announcement_timing_described_by', 'raw_piece_count': 4, 'conten; {'identifier': 'termination_reason_qualified_by', 'raw_piece_count': 4, 'content; {'identifier': 'announces_termination', 'raw_piece_count': 2, 'content_piece_cou (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `identifier_glue_excess_mass_content`

- value: **16**  (from `identifier_glue.identifier_glue_excess_mass_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'other_reason_termination_in_accordance_with_solactive_policies',; {'identifier': 'HttpsWwwSolactiveComNewsAnnouncements', 'raw_piece_count': 6, 'c; {'identifier': 'termination_and_announcement_at_zero_or_below', 'raw_piece_count (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'announcement_timing_described_by', 'raw_piece_count': 4, 'conten; {'identifier': 'termination_reason_qualified_by', 'raw_piece_count': 4, 'content; {'identifier': 'announces_termination', 'raw_piece_count': 2, 'content_piece_cou (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `identifier_glue_excess_mass_raw`

- value: **18**  (from `identifier_glue.identifier_glue_excess_mass_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'other_reason_termination_in_accordance_with_solactive_policies',; {'identifier': 'HttpsWwwSolactiveComNewsAnnouncements', 'raw_piece_count': 6, 'c; {'identifier': 'termination_and_announcement_at_zero_or_below', 'raw_piece_count (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'announcement_timing_described_by', 'raw_piece_count': 4, 'conten; {'identifier': 'termination_reason_qualified_by', 'raw_piece_count': 4, 'content; {'identifier': 'announces_termination', 'raw_piece_count': 2, 'content_piece_cou (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `invented_helper_sort_count`

- value: **1**  (from `<search recursive metrics JSON for key `invented_helper_sort_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → adjustedreturnindex; announced_on; announcement_by (+38 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; adjustedreturnindex; announced_on (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'index', 'current_count': 13, 'baseline_count': 3, 'delta': 10}; {'token': 'indextermination', 'current_count': 8, 'baseline_count': 0, 'delta': ; {'token': 'policy', 'current_count': 8, 'baseline_count': 0, 'delta': 8} (+17 more)
  - `grounding.origin_error_count` → 18
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'other_reason_termination_in_accordance_with_solactive_policies',; {'identifier': 'HttpsWwwSolactiveComNewsAnnouncements', 'raw_piece_count': 6, 'c; {'identifier': 'termination_and_announcement_at_zero_or_below', 'raw_piece_count (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'announcement_timing_described_by', 'raw_piece_count': 4, 'conten; {'identifier': 'termination_reason_qualified_by', 'raw_piece_count': 4, 'content; {'identifier': 'announces_termination', 'raw_piece_count': 2, 'content_piece_cou (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)
  - `evidence.invented_helper_sorts` → Policy

## [WARNING] `ontology_planning` / `invented_helper_symbol_count`

- value: **1**  (from `<search recursive metrics JSON for key `invented_helper_symbol_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → adjustedreturnindex; announced_on; announcement_by (+38 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; adjustedreturnindex; announced_on (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'index', 'current_count': 13, 'baseline_count': 3, 'delta': 10}; {'token': 'indextermination', 'current_count': 8, 'baseline_count': 0, 'delta': ; {'token': 'policy', 'current_count': 8, 'baseline_count': 0, 'delta': 8} (+17 more)
  - `grounding.origin_error_count` → 18
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'other_reason_termination_in_accordance_with_solactive_policies',; {'identifier': 'HttpsWwwSolactiveComNewsAnnouncements', 'raw_piece_count': 6, 'c; {'identifier': 'termination_and_announcement_at_zero_or_below', 'raw_piece_count (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'announcement_timing_described_by', 'raw_piece_count': 4, 'conten; {'identifier': 'termination_reason_qualified_by', 'raw_piece_count': 4, 'content; {'identifier': 'announces_termination', 'raw_piece_count': 2, 'content_piece_cou (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)
  - `evidence.invented_helper_sorts` → Policy

## [WARNING] `ontology_planning` / `low_source_grounded_glued_identifier_count`

- value: **6**  (from `identifier_glue.low_source_grounded_glued_identifier_count`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'other_reason_termination_in_accordance_with_solactive_policies',; {'identifier': 'HttpsWwwSolactiveComNewsAnnouncements', 'raw_piece_count': 6, 'c; {'identifier': 'termination_and_announcement_at_zero_or_below', 'raw_piece_count (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'announcement_timing_described_by', 'raw_piece_count': 4, 'conten; {'identifier': 'termination_reason_qualified_by', 'raw_piece_count': 4, 'content; {'identifier': 'announces_termination', 'raw_piece_count': 2, 'content_piece_cou (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `max_identifier_piece_count_content`

- value: **6**  (from `identifier_glue.max_identifier_piece_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'other_reason_termination_in_accordance_with_solactive_policies',; {'identifier': 'HttpsWwwSolactiveComNewsAnnouncements', 'raw_piece_count': 6, 'c; {'identifier': 'termination_and_announcement_at_zero_or_below', 'raw_piece_count (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'announcement_timing_described_by', 'raw_piece_count': 4, 'conten; {'identifier': 'termination_reason_qualified_by', 'raw_piece_count': 4, 'content; {'identifier': 'announces_termination', 'raw_piece_count': 2, 'content_piece_cou (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `max_identifier_piece_count_raw`

- value: **8**  (from `identifier_glue.max_identifier_piece_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'other_reason_termination_in_accordance_with_solactive_policies',; {'identifier': 'HttpsWwwSolactiveComNewsAnnouncements', 'raw_piece_count': 6, 'c; {'identifier': 'termination_and_announcement_at_zero_or_below', 'raw_piece_count (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'announcement_timing_described_by', 'raw_piece_count': 4, 'conten; {'identifier': 'termination_reason_qualified_by', 'raw_piece_count': 4, 'content; {'identifier': 'announces_termination', 'raw_piece_count': 2, 'content_piece_cou (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `mean_identifier_piece_count_content`

- value: **1.9047619047619047**  (from `identifier_glue.mean_identifier_piece_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'other_reason_termination_in_accordance_with_solactive_policies',; {'identifier': 'HttpsWwwSolactiveComNewsAnnouncements', 'raw_piece_count': 6, 'c; {'identifier': 'termination_and_announcement_at_zero_or_below', 'raw_piece_count (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'announcement_timing_described_by', 'raw_piece_count': 4, 'conten; {'identifier': 'termination_reason_qualified_by', 'raw_piece_count': 4, 'content; {'identifier': 'announces_termination', 'raw_piece_count': 2, 'content_piece_cou (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `mean_identifier_piece_count_raw`

- value: **2.4047619047619047**  (from `identifier_glue.mean_identifier_piece_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'other_reason_termination_in_accordance_with_solactive_policies',; {'identifier': 'HttpsWwwSolactiveComNewsAnnouncements', 'raw_piece_count': 6, 'c; {'identifier': 'termination_and_announcement_at_zero_or_below', 'raw_piece_count (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'announcement_timing_described_by', 'raw_piece_count': 4, 'conten; {'identifier': 'termination_reason_qualified_by', 'raw_piece_count': 4, 'content; {'identifier': 'announces_termination', 'raw_piece_count': 2, 'content_piece_cou (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `new_formula_content_token_count_vs_text_only`

- value: **41**  (from `grounding.new_formula_content_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → adjustedreturnindex; announced_on; announcement_by (+38 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; adjustedreturnindex; announced_on (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'index', 'current_count': 13, 'baseline_count': 3, 'delta': 10}; {'token': 'indextermination', 'current_count': 8, 'baseline_count': 0, 'delta': ; {'token': 'policy', 'current_count': 8, 'baseline_count': 0, 'delta': 8} (+17 more)
  - `grounding.origin_error_count` → 18

## [WARNING] `ontology_planning` / `new_formula_token_count_vs_text_only`

- value: **46**  (from `grounding.new_formula_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → adjustedreturnindex; announced_on; announcement_by (+38 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; adjustedreturnindex; announced_on (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'index', 'current_count': 13, 'baseline_count': 3, 'delta': 10}; {'token': 'indextermination', 'current_count': 8, 'baseline_count': 0, 'delta': ; {'token': 'policy', 'current_count': 8, 'baseline_count': 0, 'delta': 8} (+17 more)
  - `grounding.origin_error_count` → 18

## [WARNING] `ontology_planning` / `new_full_surface_content_token_count_vs_text_only`

- value: **60**  (from `grounding.new_full_surface_content_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → adjustedreturnindex; announced_on; announcement_by (+38 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; adjustedreturnindex; announced_on (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'index', 'current_count': 13, 'baseline_count': 3, 'delta': 10}; {'token': 'indextermination', 'current_count': 8, 'baseline_count': 0, 'delta': ; {'token': 'policy', 'current_count': 8, 'baseline_count': 0, 'delta': 8} (+17 more)
  - `grounding.origin_error_count` → 18

## [WARNING] `ontology_planning` / `new_full_surface_token_count_vs_text_only`

- value: **68**  (from `grounding.new_full_surface_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → adjustedreturnindex; announced_on; announcement_by (+38 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; adjustedreturnindex; announced_on (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'index', 'current_count': 13, 'baseline_count': 3, 'delta': 10}; {'token': 'indextermination', 'current_count': 8, 'baseline_count': 0, 'delta': ; {'token': 'policy', 'current_count': 8, 'baseline_count': 0, 'delta': 8} (+17 more)
  - `grounding.origin_error_count` → 18

## [WARNING] `ontology_planning` / `new_surface_content_token_count`

- value: **80**  (from `<search recursive metrics JSON for key `new_surface_content_token_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → adjustedreturnindex; announced_on; announcement_by (+38 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; adjustedreturnindex; announced_on (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'index', 'current_count': 13, 'baseline_count': 3, 'delta': 10}; {'token': 'indextermination', 'current_count': 8, 'baseline_count': 0, 'delta': ; {'token': 'policy', 'current_count': 8, 'baseline_count': 0, 'delta': 8} (+17 more)
  - `grounding.origin_error_count` → 18

## [WARNING] `ontology_planning` / `new_surface_token_count`

- value: **80**  (from `<search recursive metrics JSON for key `new_surface_token_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → adjustedreturnindex; announced_on; announcement_by (+38 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; adjustedreturnindex; announced_on (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'index', 'current_count': 13, 'baseline_count': 3, 'delta': 10}; {'token': 'indextermination', 'current_count': 8, 'baseline_count': 0, 'delta': ; {'token': 'policy', 'current_count': 8, 'baseline_count': 0, 'delta': 8} (+17 more)
  - `grounding.origin_error_count` → 18

## [WARNING] `ontology_planning` / `ungrounded_sort_count`

- value: **16**  (from `grounding.ungrounded_sort_count`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → adjustedreturnindex; announced_on; announcement_by (+38 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; adjustedreturnindex; announced_on (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'index', 'current_count': 13, 'baseline_count': 3, 'delta': 10}; {'token': 'indextermination', 'current_count': 8, 'baseline_count': 0, 'delta': ; {'token': 'policy', 'current_count': 8, 'baseline_count': 0, 'delta': 8} (+17 more)
  - `grounding.origin_error_count` → 18

## [WARNING] `ontology_planning` / `ungrounded_symbol_count`

- value: **2**  (from `grounding.ungrounded_symbol_count`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → adjustedreturnindex; announced_on; announcement_by (+38 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; adjustedreturnindex; announced_on (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'index', 'current_count': 13, 'baseline_count': 3, 'delta': 10}; {'token': 'indextermination', 'current_count': 8, 'baseline_count': 0, 'delta': ; {'token': 'policy', 'current_count': 8, 'baseline_count': 0, 'delta': 8} (+17 more)
  - `grounding.origin_error_count` → 18
