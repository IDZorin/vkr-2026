# Diagnostic report — section_5_5

- **gate**: `needs_review`
- fail: 0, warning: 36

## [WARNING] `merge_canonicalization` / `callable_symbol_count`

- value: **11**  (from `parameterization.callable_symbol_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 11
  - `<related section in metrics JSON>` → 11

## [WARNING] `merge_canonicalization` / `callable_symbol_with_args_count`

- value: **11**  (from `parameterization.callable_symbol_with_args_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 11
  - `<related section in metrics JSON>` → 11

## [WARNING] `merge_canonicalization` / `cross_reference_dropout_count`

- value: **1**  (from `<search recursive metrics JSON for key `cross_reference_dropout_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `evidence.source_cross_references` → Section 5.5
  - `evidence.ir_cross_references` → entity Guideline : Document

## [WARNING] `merge_canonicalization` / `cross_reference_usage_count`

- value: **1**  (from `<search recursive metrics JSON for key `cross_reference_usage_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `evidence.ir_cross_references` → entity Guideline : Document

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

- value: **11**  (from `parameterization.factorization_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 11
  - `<related section in metrics JSON>` → 11

## [WARNING] `merge_canonicalization` / `focus_signature_unique_count`

- value: **1**  (from `variability.focus_signature_unique_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.

## [WARNING] `merge_canonicalization` / `quantifier_parameter_slot_count`

- value: **8**  (from `parameterization.quantifier_parameter_slot_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `assertion_complexity.top_complex_assertions` → oversight_committee_staff_from_solactive_or_subsidiary; oversight_committee_responsible_for_index_rule_amendment_decisions; index_rule_amendment_scope (+1 more)
  - `assertion_complexity.max_assertion_depth` → 7
  - `assertion_complexity.total_quantifier_count` → 8

## [WARNING] `merge_canonicalization` / `top_level_parameter_slot_count`

- value: **22**  (from `parameterization.top_level_parameter_slot_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 22
  - `<related section in metrics JSON>` → 22

## [WARNING] `merge_canonicalization` / `total_parameter_slot_mass`

- value: **30**  (from `parameterization.total_parameter_slot_mass`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 30
  - `<related section in metrics JSON>` → 30

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

- value: **8**  (from `identifier_glue.compound_identifier_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'oversight_committee_responsible_for_index_rule_amendment_decisio; {'identifier': 'index_rule_amendments_may_result_in_guideline_amendment', 'raw_p; {'identifier': 'HttpsWwwSolactiveComDocumentsMethodologyPolicy', 'raw_piece_coun (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'WebResource', 'raw_piece_count': 2, 'content_piece_count': 2, 'r; {'identifier': 'amendment_of_document', 'raw_piece_count': 3, 'content_piece_cou; {'identifier': 'amendment_of_rule', 'raw_piece_count': 3, 'content_piece_count': (+15 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'oversight_committee_responsible_for_index_rule_amendment_decisio

## [WARNING] `ontology_planning` / `compound_identifier_count_raw`

- value: **7**  (from `identifier_glue.compound_identifier_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'oversight_committee_responsible_for_index_rule_amendment_decisio; {'identifier': 'index_rule_amendments_may_result_in_guideline_amendment', 'raw_p; {'identifier': 'HttpsWwwSolactiveComDocumentsMethodologyPolicy', 'raw_piece_coun (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'WebResource', 'raw_piece_count': 2, 'content_piece_count': 2, 'r; {'identifier': 'amendment_of_document', 'raw_piece_count': 3, 'content_piece_cou; {'identifier': 'amendment_of_rule', 'raw_piece_count': 3, 'content_piece_count': (+15 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'oversight_committee_responsible_for_index_rule_amendment_decisio

## [WARNING] `ontology_planning` / `cross_reference_dropout_count`

- value: **1**  (from `<search recursive metrics JSON for key `cross_reference_dropout_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `evidence.source_cross_references` → Section 5.5
  - `evidence.ir_cross_references` → entity Guideline : Document

## [WARNING] `ontology_planning` / `cross_reference_usage_count`

- value: **1**  (from `<search recursive metrics JSON for key `cross_reference_usage_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `evidence.ir_cross_references` → entity Guideline : Document

## [WARNING] `ontology_planning` / `dependency_link_count`

- value: **2**  (from `<search recursive metrics JSON for key `dependency_link_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 2
  - `<related section in metrics JSON>` → 2

## [WARNING] `ontology_planning` / `identifier_count`

- value: **43**  (from `identifier_glue.identifier_count`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'oversight_committee_responsible_for_index_rule_amendment_decisio; {'identifier': 'index_rule_amendments_may_result_in_guideline_amendment', 'raw_p; {'identifier': 'HttpsWwwSolactiveComDocumentsMethodologyPolicy', 'raw_piece_coun (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'WebResource', 'raw_piece_count': 2, 'content_piece_count': 2, 'r; {'identifier': 'amendment_of_document', 'raw_piece_count': 3, 'content_piece_cou; {'identifier': 'amendment_of_rule', 'raw_piece_count': 3, 'content_piece_count': (+15 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'oversight_committee_responsible_for_index_rule_amendment_decisio

## [WARNING] `ontology_planning` / `identifier_glue_excess_mass_content`

- value: **23**  (from `identifier_glue.identifier_glue_excess_mass_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'oversight_committee_responsible_for_index_rule_amendment_decisio; {'identifier': 'index_rule_amendments_may_result_in_guideline_amendment', 'raw_p; {'identifier': 'HttpsWwwSolactiveComDocumentsMethodologyPolicy', 'raw_piece_coun (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'WebResource', 'raw_piece_count': 2, 'content_piece_count': 2, 'r; {'identifier': 'amendment_of_document', 'raw_piece_count': 3, 'content_piece_cou; {'identifier': 'amendment_of_rule', 'raw_piece_count': 3, 'content_piece_count': (+15 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'oversight_committee_responsible_for_index_rule_amendment_decisio

## [WARNING] `ontology_planning` / `identifier_glue_excess_mass_raw`

- value: **21**  (from `identifier_glue.identifier_glue_excess_mass_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'oversight_committee_responsible_for_index_rule_amendment_decisio; {'identifier': 'index_rule_amendments_may_result_in_guideline_amendment', 'raw_p; {'identifier': 'HttpsWwwSolactiveComDocumentsMethodologyPolicy', 'raw_piece_coun (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'WebResource', 'raw_piece_count': 2, 'content_piece_count': 2, 'r; {'identifier': 'amendment_of_document', 'raw_piece_count': 3, 'content_piece_cou; {'identifier': 'amendment_of_rule', 'raw_piece_count': 3, 'content_piece_count': (+15 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'oversight_committee_responsible_for_index_rule_amendment_decisio

## [WARNING] `ontology_planning` / `invented_helper_sort_count`

- value: **1**  (from `<search recursive metrics JSON for key `invented_helper_sort_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → amendment_of_document; amendment_of_rule; approval_by (+34 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; amendment_of_document; amendment_of_rule (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'amendment', 'current_count': 16, 'baseline_count': 2, 'delta': 14}; {'token': 'rule', 'current_count': 11, 'baseline_count': 0, 'delta': 11}; {'token': 'staff', 'current_count': 10, 'baseline_count': 1, 'delta': 9} (+17 more)
  - `grounding.origin_error_count` → 8
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'oversight_committee_responsible_for_index_rule_amendment_decisio; {'identifier': 'index_rule_amendments_may_result_in_guideline_amendment', 'raw_p; {'identifier': 'HttpsWwwSolactiveComDocumentsMethodologyPolicy', 'raw_piece_coun (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'WebResource', 'raw_piece_count': 2, 'content_piece_count': 2, 'r; {'identifier': 'amendment_of_document', 'raw_piece_count': 3, 'content_piece_cou; {'identifier': 'amendment_of_rule', 'raw_piece_count': 3, 'content_piece_count': (+15 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'oversight_committee_responsible_for_index_rule_amendment_decisio
  - `evidence.invented_helper_sorts` → Subsidiary

## [WARNING] `ontology_planning` / `invented_helper_symbol_count`

- value: **1**  (from `<search recursive metrics JSON for key `invented_helper_symbol_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → amendment_of_document; amendment_of_rule; approval_by (+34 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; amendment_of_document; amendment_of_rule (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'amendment', 'current_count': 16, 'baseline_count': 2, 'delta': 14}; {'token': 'rule', 'current_count': 11, 'baseline_count': 0, 'delta': 11}; {'token': 'staff', 'current_count': 10, 'baseline_count': 1, 'delta': 9} (+17 more)
  - `grounding.origin_error_count` → 8
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'oversight_committee_responsible_for_index_rule_amendment_decisio; {'identifier': 'index_rule_amendments_may_result_in_guideline_amendment', 'raw_p; {'identifier': 'HttpsWwwSolactiveComDocumentsMethodologyPolicy', 'raw_piece_coun (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'WebResource', 'raw_piece_count': 2, 'content_piece_count': 2, 'r; {'identifier': 'amendment_of_document', 'raw_piece_count': 3, 'content_piece_cou; {'identifier': 'amendment_of_rule', 'raw_piece_count': 3, 'content_piece_count': (+15 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'oversight_committee_responsible_for_index_rule_amendment_decisio
  - `evidence.invented_helper_sorts` → Subsidiary

## [WARNING] `ontology_planning` / `low_source_grounded_glued_identifier_count`

- value: **3**  (from `identifier_glue.low_source_grounded_glued_identifier_count`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'oversight_committee_responsible_for_index_rule_amendment_decisio; {'identifier': 'index_rule_amendments_may_result_in_guideline_amendment', 'raw_p; {'identifier': 'HttpsWwwSolactiveComDocumentsMethodologyPolicy', 'raw_piece_coun (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'WebResource', 'raw_piece_count': 2, 'content_piece_count': 2, 'r; {'identifier': 'amendment_of_document', 'raw_piece_count': 3, 'content_piece_cou; {'identifier': 'amendment_of_rule', 'raw_piece_count': 3, 'content_piece_count': (+15 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'oversight_committee_responsible_for_index_rule_amendment_decisio

## [WARNING] `ontology_planning` / `max_identifier_piece_count_content`

- value: **7**  (from `identifier_glue.max_identifier_piece_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'oversight_committee_responsible_for_index_rule_amendment_decisio; {'identifier': 'index_rule_amendments_may_result_in_guideline_amendment', 'raw_p; {'identifier': 'HttpsWwwSolactiveComDocumentsMethodologyPolicy', 'raw_piece_coun (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'WebResource', 'raw_piece_count': 2, 'content_piece_count': 2, 'r; {'identifier': 'amendment_of_document', 'raw_piece_count': 3, 'content_piece_cou; {'identifier': 'amendment_of_rule', 'raw_piece_count': 3, 'content_piece_count': (+15 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'oversight_committee_responsible_for_index_rule_amendment_decisio

## [WARNING] `ontology_planning` / `max_identifier_piece_count_raw`

- value: **8**  (from `identifier_glue.max_identifier_piece_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'oversight_committee_responsible_for_index_rule_amendment_decisio; {'identifier': 'index_rule_amendments_may_result_in_guideline_amendment', 'raw_p; {'identifier': 'HttpsWwwSolactiveComDocumentsMethodologyPolicy', 'raw_piece_coun (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'WebResource', 'raw_piece_count': 2, 'content_piece_count': 2, 'r; {'identifier': 'amendment_of_document', 'raw_piece_count': 3, 'content_piece_cou; {'identifier': 'amendment_of_rule', 'raw_piece_count': 3, 'content_piece_count': (+15 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'oversight_committee_responsible_for_index_rule_amendment_decisio

## [WARNING] `ontology_planning` / `mean_identifier_piece_count_content`

- value: **1.8372093023255813**  (from `identifier_glue.mean_identifier_piece_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'oversight_committee_responsible_for_index_rule_amendment_decisio; {'identifier': 'index_rule_amendments_may_result_in_guideline_amendment', 'raw_p; {'identifier': 'HttpsWwwSolactiveComDocumentsMethodologyPolicy', 'raw_piece_coun (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'WebResource', 'raw_piece_count': 2, 'content_piece_count': 2, 'r; {'identifier': 'amendment_of_document', 'raw_piece_count': 3, 'content_piece_cou; {'identifier': 'amendment_of_rule', 'raw_piece_count': 3, 'content_piece_count': (+15 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'oversight_committee_responsible_for_index_rule_amendment_decisio

## [WARNING] `ontology_planning` / `mean_identifier_piece_count_raw`

- value: **2.3488372093023258**  (from `identifier_glue.mean_identifier_piece_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'oversight_committee_responsible_for_index_rule_amendment_decisio; {'identifier': 'index_rule_amendments_may_result_in_guideline_amendment', 'raw_p; {'identifier': 'HttpsWwwSolactiveComDocumentsMethodologyPolicy', 'raw_piece_coun (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'WebResource', 'raw_piece_count': 2, 'content_piece_count': 2, 'r; {'identifier': 'amendment_of_document', 'raw_piece_count': 3, 'content_piece_cou; {'identifier': 'amendment_of_rule', 'raw_piece_count': 3, 'content_piece_count': (+15 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'oversight_committee_responsible_for_index_rule_amendment_decisio

## [WARNING] `ontology_planning` / `new_formula_content_token_count_vs_text_only`

- value: **37**  (from `grounding.new_formula_content_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → amendment_of_document; amendment_of_rule; approval_by (+34 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; amendment_of_document; amendment_of_rule (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'amendment', 'current_count': 16, 'baseline_count': 2, 'delta': 14}; {'token': 'rule', 'current_count': 11, 'baseline_count': 0, 'delta': 11}; {'token': 'staff', 'current_count': 10, 'baseline_count': 1, 'delta': 9} (+17 more)
  - `grounding.origin_error_count` → 8

## [WARNING] `ontology_planning` / `new_formula_token_count_vs_text_only`

- value: **42**  (from `grounding.new_formula_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → amendment_of_document; amendment_of_rule; approval_by (+34 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; amendment_of_document; amendment_of_rule (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'amendment', 'current_count': 16, 'baseline_count': 2, 'delta': 14}; {'token': 'rule', 'current_count': 11, 'baseline_count': 0, 'delta': 11}; {'token': 'staff', 'current_count': 10, 'baseline_count': 1, 'delta': 9} (+17 more)
  - `grounding.origin_error_count` → 8

## [WARNING] `ontology_planning` / `new_full_surface_content_token_count_vs_text_only`

- value: **56**  (from `grounding.new_full_surface_content_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → amendment_of_document; amendment_of_rule; approval_by (+34 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; amendment_of_document; amendment_of_rule (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'amendment', 'current_count': 16, 'baseline_count': 2, 'delta': 14}; {'token': 'rule', 'current_count': 11, 'baseline_count': 0, 'delta': 11}; {'token': 'staff', 'current_count': 10, 'baseline_count': 1, 'delta': 9} (+17 more)
  - `grounding.origin_error_count` → 8

## [WARNING] `ontology_planning` / `new_full_surface_token_count_vs_text_only`

- value: **63**  (from `grounding.new_full_surface_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → amendment_of_document; amendment_of_rule; approval_by (+34 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; amendment_of_document; amendment_of_rule (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'amendment', 'current_count': 16, 'baseline_count': 2, 'delta': 14}; {'token': 'rule', 'current_count': 11, 'baseline_count': 0, 'delta': 11}; {'token': 'staff', 'current_count': 10, 'baseline_count': 1, 'delta': 9} (+17 more)
  - `grounding.origin_error_count` → 8

## [WARNING] `ontology_planning` / `new_surface_content_token_count`

- value: **97**  (from `<search recursive metrics JSON for key `new_surface_content_token_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → amendment_of_document; amendment_of_rule; approval_by (+34 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; amendment_of_document; amendment_of_rule (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'amendment', 'current_count': 16, 'baseline_count': 2, 'delta': 14}; {'token': 'rule', 'current_count': 11, 'baseline_count': 0, 'delta': 11}; {'token': 'staff', 'current_count': 10, 'baseline_count': 1, 'delta': 9} (+17 more)
  - `grounding.origin_error_count` → 8

## [WARNING] `ontology_planning` / `new_surface_token_count`

- value: **97**  (from `<search recursive metrics JSON for key `new_surface_token_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → amendment_of_document; amendment_of_rule; approval_by (+34 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; amendment_of_document; amendment_of_rule (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'amendment', 'current_count': 16, 'baseline_count': 2, 'delta': 14}; {'token': 'rule', 'current_count': 11, 'baseline_count': 0, 'delta': 11}; {'token': 'staff', 'current_count': 10, 'baseline_count': 1, 'delta': 9} (+17 more)
  - `grounding.origin_error_count` → 8

## [WARNING] `ontology_planning` / `ungrounded_sort_count`

- value: **8**  (from `grounding.ungrounded_sort_count`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → amendment_of_document; amendment_of_rule; approval_by (+34 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; amendment_of_document; amendment_of_rule (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'amendment', 'current_count': 16, 'baseline_count': 2, 'delta': 14}; {'token': 'rule', 'current_count': 11, 'baseline_count': 0, 'delta': 11}; {'token': 'staff', 'current_count': 10, 'baseline_count': 1, 'delta': 9} (+17 more)
  - `grounding.origin_error_count` → 8
