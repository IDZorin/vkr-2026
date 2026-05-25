# Diagnostic report — section_1_2

- **gate**: `needs_review`
- fail: 0, warning: 35

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

- value: **2**  (from `<search recursive metrics JSON for key `cross_reference_usage_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `evidence.ir_cross_references` → entity EquityIndexMethodology : Document; entity Guideline : Document

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

- value: **3**  (from `parameterization.quantifier_parameter_slot_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `assertion_complexity.top_complex_assertions` → index_publications_available_at_announcements_website; bbg_ticker_at_most_one
  - `assertion_complexity.max_assertion_depth` → 6
  - `assertion_complexity.total_quantifier_count` → 3

## [WARNING] `merge_canonicalization` / `top_level_parameter_slot_count`

- value: **41**  (from `parameterization.top_level_parameter_slot_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 41
  - `<related section in metrics JSON>` → 41

## [WARNING] `merge_canonicalization` / `total_parameter_slot_mass`

- value: **44**  (from `parameterization.total_parameter_slot_mass`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 44
  - `<related section in metrics JSON>` → 44

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

- value: **31**  (from `identifier_glue.compound_identifier_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'HttpsWwwSolactiveComDocumentsEquityIndexMethodology', 'raw_piece; {'identifier': 'SolactiveTransatlanticCleanEnergyEURIndex5PercentARName', 'raw_p; {'identifier': 'SolactiveTransatlanticCleanEnergyEURIndex5PercentAR', 'raw_piece (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DE000SL0R4B4', 'raw_piece_count': 4, 'content_piece_count': 2, '; {'identifier': 'DE000SL0R4C2', 'raw_piece_count': 4, 'content_piece_count': 2, '; {'identifier': 'DE000SL0R4D0', 'raw_piece_count': 4, 'content_piece_count': 2, ' (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'published_under_following_identifiers', 'raw_piece_count': 4, 'c

## [WARNING] `ontology_planning` / `compound_identifier_count_raw`

- value: **33**  (from `identifier_glue.compound_identifier_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'HttpsWwwSolactiveComDocumentsEquityIndexMethodology', 'raw_piece; {'identifier': 'SolactiveTransatlanticCleanEnergyEURIndex5PercentARName', 'raw_p; {'identifier': 'SolactiveTransatlanticCleanEnergyEURIndex5PercentAR', 'raw_piece (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DE000SL0R4B4', 'raw_piece_count': 4, 'content_piece_count': 2, '; {'identifier': 'DE000SL0R4C2', 'raw_piece_count': 4, 'content_piece_count': 2, '; {'identifier': 'DE000SL0R4D0', 'raw_piece_count': 4, 'content_piece_count': 2, ' (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'published_under_following_identifiers', 'raw_piece_count': 4, 'c

## [WARNING] `ontology_planning` / `cross_reference_usage_count`

- value: **2**  (from `<search recursive metrics JSON for key `cross_reference_usage_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `evidence.ir_cross_references` → entity EquityIndexMethodology : Document; entity Guideline : Document

## [WARNING] `ontology_planning` / `dependency_link_count`

- value: **2**  (from `<search recursive metrics JSON for key `dependency_link_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 2
  - `<related section in metrics JSON>` → 2

## [WARNING] `ontology_planning` / `identifier_count`

- value: **82**  (from `identifier_glue.identifier_count`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'HttpsWwwSolactiveComDocumentsEquityIndexMethodology', 'raw_piece; {'identifier': 'SolactiveTransatlanticCleanEnergyEURIndex5PercentARName', 'raw_p; {'identifier': 'SolactiveTransatlanticCleanEnergyEURIndex5PercentAR', 'raw_piece (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DE000SL0R4B4', 'raw_piece_count': 4, 'content_piece_count': 2, '; {'identifier': 'DE000SL0R4C2', 'raw_piece_count': 4, 'content_piece_count': 2, '; {'identifier': 'DE000SL0R4D0', 'raw_piece_count': 4, 'content_piece_count': 2, ' (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'published_under_following_identifiers', 'raw_piece_count': 4, 'c

## [WARNING] `ontology_planning` / `identifier_glue_excess_mass_content`

- value: **80**  (from `identifier_glue.identifier_glue_excess_mass_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'HttpsWwwSolactiveComDocumentsEquityIndexMethodology', 'raw_piece; {'identifier': 'SolactiveTransatlanticCleanEnergyEURIndex5PercentARName', 'raw_p; {'identifier': 'SolactiveTransatlanticCleanEnergyEURIndex5PercentAR', 'raw_piece (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DE000SL0R4B4', 'raw_piece_count': 4, 'content_piece_count': 2, '; {'identifier': 'DE000SL0R4C2', 'raw_piece_count': 4, 'content_piece_count': 2, '; {'identifier': 'DE000SL0R4D0', 'raw_piece_count': 4, 'content_piece_count': 2, ' (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'published_under_following_identifiers', 'raw_piece_count': 4, 'c

## [WARNING] `ontology_planning` / `identifier_glue_excess_mass_raw`

- value: **77**  (from `identifier_glue.identifier_glue_excess_mass_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'HttpsWwwSolactiveComDocumentsEquityIndexMethodology', 'raw_piece; {'identifier': 'SolactiveTransatlanticCleanEnergyEURIndex5PercentARName', 'raw_p; {'identifier': 'SolactiveTransatlanticCleanEnergyEURIndex5PercentAR', 'raw_piece (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DE000SL0R4B4', 'raw_piece_count': 4, 'content_piece_count': 2, '; {'identifier': 'DE000SL0R4C2', 'raw_piece_count': 4, 'content_piece_count': 2, '; {'identifier': 'DE000SL0R4D0', 'raw_piece_count': 4, 'content_piece_count': 2, ' (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'published_under_following_identifiers', 'raw_piece_count': 4, 'c

## [WARNING] `ontology_planning` / `invented_helper_sort_count`

- value: **2**  (from `<search recursive metrics JSON for key `invented_helper_sort_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → adjustedreturnindex; affiliatedvendor; announcements_website (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; adjustedreturnindex; affiliatedvendor (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'index', 'current_count': 77, 'baseline_count': 18, 'delta': 59}; {'token': 'isin', 'current_count': 13, 'baseline_count': 1, 'delta': 12}; {'token': 'published', 'current_count': 13, 'baseline_count': 2, 'delta': 11} (+17 more)
  - `grounding.origin_error_count` → 38
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'HttpsWwwSolactiveComDocumentsEquityIndexMethodology', 'raw_piece; {'identifier': 'SolactiveTransatlanticCleanEnergyEURIndex5PercentARName', 'raw_p; {'identifier': 'SolactiveTransatlanticCleanEnergyEURIndex5PercentAR', 'raw_piece (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DE000SL0R4B4', 'raw_piece_count': 4, 'content_piece_count': 2, '; {'identifier': 'DE000SL0R4C2', 'raw_piece_count': 4, 'content_piece_count': 2, '; {'identifier': 'DE000SL0R4D0', 'raw_piece_count': 4, 'content_piece_count': 2, ' (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'published_under_following_identifiers', 'raw_piece_count': 4, 'c
  - `evidence.invented_helper_sorts` → ISIN; RIC

## [WARNING] `ontology_planning` / `invented_helper_symbol_count`

- value: **2**  (from `<search recursive metrics JSON for key `invented_helper_symbol_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → adjustedreturnindex; affiliatedvendor; announcements_website (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; adjustedreturnindex; affiliatedvendor (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'index', 'current_count': 77, 'baseline_count': 18, 'delta': 59}; {'token': 'isin', 'current_count': 13, 'baseline_count': 1, 'delta': 12}; {'token': 'published', 'current_count': 13, 'baseline_count': 2, 'delta': 11} (+17 more)
  - `grounding.origin_error_count` → 38
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'HttpsWwwSolactiveComDocumentsEquityIndexMethodology', 'raw_piece; {'identifier': 'SolactiveTransatlanticCleanEnergyEURIndex5PercentARName', 'raw_p; {'identifier': 'SolactiveTransatlanticCleanEnergyEURIndex5PercentAR', 'raw_piece (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DE000SL0R4B4', 'raw_piece_count': 4, 'content_piece_count': 2, '; {'identifier': 'DE000SL0R4C2', 'raw_piece_count': 4, 'content_piece_count': 2, '; {'identifier': 'DE000SL0R4D0', 'raw_piece_count': 4, 'content_piece_count': 2, ' (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'published_under_following_identifiers', 'raw_piece_count': 4, 'c
  - `evidence.invented_helper_sorts` → ISIN; RIC

## [WARNING] `ontology_planning` / `low_source_grounded_glued_identifier_count`

- value: **18**  (from `identifier_glue.low_source_grounded_glued_identifier_count`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'HttpsWwwSolactiveComDocumentsEquityIndexMethodology', 'raw_piece; {'identifier': 'SolactiveTransatlanticCleanEnergyEURIndex5PercentARName', 'raw_p; {'identifier': 'SolactiveTransatlanticCleanEnergyEURIndex5PercentAR', 'raw_piece (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DE000SL0R4B4', 'raw_piece_count': 4, 'content_piece_count': 2, '; {'identifier': 'DE000SL0R4C2', 'raw_piece_count': 4, 'content_piece_count': 2, '; {'identifier': 'DE000SL0R4D0', 'raw_piece_count': 4, 'content_piece_count': 2, ' (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'published_under_following_identifiers', 'raw_piece_count': 4, 'c

## [WARNING] `ontology_planning` / `max_identifier_piece_count_content`

- value: **8**  (from `identifier_glue.max_identifier_piece_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'HttpsWwwSolactiveComDocumentsEquityIndexMethodology', 'raw_piece; {'identifier': 'SolactiveTransatlanticCleanEnergyEURIndex5PercentARName', 'raw_p; {'identifier': 'SolactiveTransatlanticCleanEnergyEURIndex5PercentAR', 'raw_piece (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DE000SL0R4B4', 'raw_piece_count': 4, 'content_piece_count': 2, '; {'identifier': 'DE000SL0R4C2', 'raw_piece_count': 4, 'content_piece_count': 2, '; {'identifier': 'DE000SL0R4D0', 'raw_piece_count': 4, 'content_piece_count': 2, ' (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'published_under_following_identifiers', 'raw_piece_count': 4, 'c

## [WARNING] `ontology_planning` / `max_identifier_piece_count_raw`

- value: **8**  (from `identifier_glue.max_identifier_piece_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'HttpsWwwSolactiveComDocumentsEquityIndexMethodology', 'raw_piece; {'identifier': 'SolactiveTransatlanticCleanEnergyEURIndex5PercentARName', 'raw_p; {'identifier': 'SolactiveTransatlanticCleanEnergyEURIndex5PercentAR', 'raw_piece (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DE000SL0R4B4', 'raw_piece_count': 4, 'content_piece_count': 2, '; {'identifier': 'DE000SL0R4C2', 'raw_piece_count': 4, 'content_piece_count': 2, '; {'identifier': 'DE000SL0R4D0', 'raw_piece_count': 4, 'content_piece_count': 2, ' (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'published_under_following_identifiers', 'raw_piece_count': 4, 'c

## [WARNING] `ontology_planning` / `mean_identifier_piece_count_content`

- value: **2.658536585365854**  (from `identifier_glue.mean_identifier_piece_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'HttpsWwwSolactiveComDocumentsEquityIndexMethodology', 'raw_piece; {'identifier': 'SolactiveTransatlanticCleanEnergyEURIndex5PercentARName', 'raw_p; {'identifier': 'SolactiveTransatlanticCleanEnergyEURIndex5PercentAR', 'raw_piece (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DE000SL0R4B4', 'raw_piece_count': 4, 'content_piece_count': 2, '; {'identifier': 'DE000SL0R4C2', 'raw_piece_count': 4, 'content_piece_count': 2, '; {'identifier': 'DE000SL0R4D0', 'raw_piece_count': 4, 'content_piece_count': 2, ' (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'published_under_following_identifiers', 'raw_piece_count': 4, 'c

## [WARNING] `ontology_planning` / `mean_identifier_piece_count_raw`

- value: **3.182926829268293**  (from `identifier_glue.mean_identifier_piece_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'HttpsWwwSolactiveComDocumentsEquityIndexMethodology', 'raw_piece; {'identifier': 'SolactiveTransatlanticCleanEnergyEURIndex5PercentARName', 'raw_p; {'identifier': 'SolactiveTransatlanticCleanEnergyEURIndex5PercentAR', 'raw_piece (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DE000SL0R4B4', 'raw_piece_count': 4, 'content_piece_count': 2, '; {'identifier': 'DE000SL0R4C2', 'raw_piece_count': 4, 'content_piece_count': 2, '; {'identifier': 'DE000SL0R4D0', 'raw_piece_count': 4, 'content_piece_count': 2, ' (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'published_under_following_identifiers', 'raw_piece_count': 4, 'c

## [WARNING] `ontology_planning` / `new_formula_content_token_count_vs_text_only`

- value: **89**  (from `grounding.new_formula_content_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → adjustedreturnindex; affiliatedvendor; announcements_website (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; adjustedreturnindex; affiliatedvendor (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'index', 'current_count': 77, 'baseline_count': 18, 'delta': 59}; {'token': 'isin', 'current_count': 13, 'baseline_count': 1, 'delta': 12}; {'token': 'published', 'current_count': 13, 'baseline_count': 2, 'delta': 11} (+17 more)
  - `grounding.origin_error_count` → 38

## [WARNING] `ontology_planning` / `new_formula_token_count_vs_text_only`

- value: **96**  (from `grounding.new_formula_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → adjustedreturnindex; affiliatedvendor; announcements_website (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; adjustedreturnindex; affiliatedvendor (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'index', 'current_count': 77, 'baseline_count': 18, 'delta': 59}; {'token': 'isin', 'current_count': 13, 'baseline_count': 1, 'delta': 12}; {'token': 'published', 'current_count': 13, 'baseline_count': 2, 'delta': 11} (+17 more)
  - `grounding.origin_error_count` → 38

## [WARNING] `ontology_planning` / `new_full_surface_content_token_count_vs_text_only`

- value: **108**  (from `grounding.new_full_surface_content_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → adjustedreturnindex; affiliatedvendor; announcements_website (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; adjustedreturnindex; affiliatedvendor (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'index', 'current_count': 77, 'baseline_count': 18, 'delta': 59}; {'token': 'isin', 'current_count': 13, 'baseline_count': 1, 'delta': 12}; {'token': 'published', 'current_count': 13, 'baseline_count': 2, 'delta': 11} (+17 more)
  - `grounding.origin_error_count` → 38

## [WARNING] `ontology_planning` / `new_full_surface_token_count_vs_text_only`

- value: **119**  (from `grounding.new_full_surface_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → adjustedreturnindex; affiliatedvendor; announcements_website (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; adjustedreturnindex; affiliatedvendor (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'index', 'current_count': 77, 'baseline_count': 18, 'delta': 59}; {'token': 'isin', 'current_count': 13, 'baseline_count': 1, 'delta': 12}; {'token': 'published', 'current_count': 13, 'baseline_count': 2, 'delta': 11} (+17 more)
  - `grounding.origin_error_count` → 38

## [WARNING] `ontology_planning` / `new_surface_content_token_count`

- value: **244**  (from `<search recursive metrics JSON for key `new_surface_content_token_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → adjustedreturnindex; affiliatedvendor; announcements_website (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; adjustedreturnindex; affiliatedvendor (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'index', 'current_count': 77, 'baseline_count': 18, 'delta': 59}; {'token': 'isin', 'current_count': 13, 'baseline_count': 1, 'delta': 12}; {'token': 'published', 'current_count': 13, 'baseline_count': 2, 'delta': 11} (+17 more)
  - `grounding.origin_error_count` → 38

## [WARNING] `ontology_planning` / `new_surface_token_count`

- value: **244**  (from `<search recursive metrics JSON for key `new_surface_token_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → adjustedreturnindex; affiliatedvendor; announcements_website (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; adjustedreturnindex; affiliatedvendor (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'index', 'current_count': 77, 'baseline_count': 18, 'delta': 59}; {'token': 'isin', 'current_count': 13, 'baseline_count': 1, 'delta': 12}; {'token': 'published', 'current_count': 13, 'baseline_count': 2, 'delta': 11} (+17 more)
  - `grounding.origin_error_count` → 38

## [WARNING] `ontology_planning` / `ungrounded_sort_count`

- value: **17**  (from `grounding.ungrounded_sort_count`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → adjustedreturnindex; affiliatedvendor; announcements_website (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; adjustedreturnindex; affiliatedvendor (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'index', 'current_count': 77, 'baseline_count': 18, 'delta': 59}; {'token': 'isin', 'current_count': 13, 'baseline_count': 1, 'delta': 12}; {'token': 'published', 'current_count': 13, 'baseline_count': 2, 'delta': 11} (+17 more)
  - `grounding.origin_error_count` → 38

## [WARNING] `ontology_planning` / `ungrounded_symbol_count`

- value: **4**  (from `grounding.ungrounded_symbol_count`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → adjustedreturnindex; affiliatedvendor; announcements_website (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; adjustedreturnindex; affiliatedvendor (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'index', 'current_count': 77, 'baseline_count': 18, 'delta': 59}; {'token': 'isin', 'current_count': 13, 'baseline_count': 1, 'delta': 12}; {'token': 'published', 'current_count': 13, 'baseline_count': 2, 'delta': 11} (+17 more)
  - `grounding.origin_error_count` → 38
