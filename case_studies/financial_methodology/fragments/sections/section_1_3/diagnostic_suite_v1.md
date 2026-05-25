# Diagnostic report — section_1_3

- **gate**: `needs_review`
- fail: 0, warning: 34

## [WARNING] `merge_canonicalization` / `callable_symbol_count`

- value: **10**  (from `parameterization.callable_symbol_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 10
  - `<related section in metrics JSON>` → 10

## [WARNING] `merge_canonicalization` / `callable_symbol_with_args_count`

- value: **10**  (from `parameterization.callable_symbol_with_args_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 10
  - `<related section in metrics JSON>` → 10

## [WARNING] `merge_canonicalization` / `cross_reference_usage_count`

- value: **6**  (from `<search recursive metrics JSON for key `cross_reference_usage_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `evidence.ir_cross_references` → body of historical_values_from_live_date_recorded_in_accordance_with_article_8_o; body of initial_level_default_on_start_date mentions section/annex; body of levels_published_prior_to_live_date_back_tested mentions section/annex (+3 more)

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

- value: **10**  (from `parameterization.factorization_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 10
  - `<related section in metrics JSON>` → 10

## [WARNING] `merge_canonicalization` / `focus_signature_unique_count`

- value: **1**  (from `variability.focus_signature_unique_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.

## [WARNING] `merge_canonicalization` / `quantifier_parameter_slot_count`

- value: **7**  (from `parameterization.quantifier_parameter_slot_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `assertion_complexity.top_complex_assertions` → historical_values_from_live_date_recorded_in_accordance_with_article_8_of_bmr; levels_published_prior_to_live_date_back_tested; initial_level_default_on_start_date
  - `assertion_complexity.max_assertion_depth` → 8
  - `assertion_complexity.total_quantifier_count` → 7

## [WARNING] `merge_canonicalization` / `top_level_parameter_slot_count`

- value: **17**  (from `parameterization.top_level_parameter_slot_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 17
  - `<related section in metrics JSON>` → 17

## [WARNING] `merge_canonicalization` / `total_parameter_slot_mass`

- value: **24**  (from `parameterization.total_parameter_slot_mass`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 24
  - `<related section in metrics JSON>` → 24

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

- value: **11**  (from `identifier_glue.compound_identifier_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'historical_values_from_live_date_recorded_in_accordance_with_art; {'identifier': 'levels_published_prior_to_live_date_back_tested', 'raw_piece_cou; {'identifier': 'SolactiveTransatlanticCleanEnergyEURIndex5PercentAR', 'raw_piece (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'back_tested', 'raw_piece_count': 2, 'content_piece_count': 2, 'r; {'identifier': 'DocumentPart', 'raw_piece_count': 2, 'content_piece_count': 2, '; {'identifier': 'IndexLevel', 'raw_piece_count': 2, 'content_piece_count': 2, 'ra (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'levels_published_prior_to_live_date_back_tested', 'raw_piece_cou
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `compound_identifier_count_raw`

- value: **13**  (from `identifier_glue.compound_identifier_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'historical_values_from_live_date_recorded_in_accordance_with_art; {'identifier': 'levels_published_prior_to_live_date_back_tested', 'raw_piece_cou; {'identifier': 'SolactiveTransatlanticCleanEnergyEURIndex5PercentAR', 'raw_piece (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'back_tested', 'raw_piece_count': 2, 'content_piece_count': 2, 'r; {'identifier': 'DocumentPart', 'raw_piece_count': 2, 'content_piece_count': 2, '; {'identifier': 'IndexLevel', 'raw_piece_count': 2, 'content_piece_count': 2, 'ra (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'levels_published_prior_to_live_date_back_tested', 'raw_piece_cou
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `cross_reference_usage_count`

- value: **6**  (from `<search recursive metrics JSON for key `cross_reference_usage_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `evidence.ir_cross_references` → body of historical_values_from_live_date_recorded_in_accordance_with_article_8_o; body of initial_level_default_on_start_date mentions section/annex; body of levels_published_prior_to_live_date_back_tested mentions section/annex (+3 more)

## [WARNING] `ontology_planning` / `dependency_link_count`

- value: **3**  (from `<search recursive metrics JSON for key `dependency_link_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 3
  - `<related section in metrics JSON>` → 3

## [WARNING] `ontology_planning` / `identifier_count`

- value: **34**  (from `identifier_glue.identifier_count`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'historical_values_from_live_date_recorded_in_accordance_with_art; {'identifier': 'levels_published_prior_to_live_date_back_tested', 'raw_piece_cou; {'identifier': 'SolactiveTransatlanticCleanEnergyEURIndex5PercentAR', 'raw_piece (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'back_tested', 'raw_piece_count': 2, 'content_piece_count': 2, 'r; {'identifier': 'DocumentPart', 'raw_piece_count': 2, 'content_piece_count': 2, '; {'identifier': 'IndexLevel', 'raw_piece_count': 2, 'content_piece_count': 2, 'ra (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'levels_published_prior_to_live_date_back_tested', 'raw_piece_cou
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `identifier_glue_excess_mass_content`

- value: **31**  (from `identifier_glue.identifier_glue_excess_mass_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'historical_values_from_live_date_recorded_in_accordance_with_art; {'identifier': 'levels_published_prior_to_live_date_back_tested', 'raw_piece_cou; {'identifier': 'SolactiveTransatlanticCleanEnergyEURIndex5PercentAR', 'raw_piece (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'back_tested', 'raw_piece_count': 2, 'content_piece_count': 2, 'r; {'identifier': 'DocumentPart', 'raw_piece_count': 2, 'content_piece_count': 2, '; {'identifier': 'IndexLevel', 'raw_piece_count': 2, 'content_piece_count': 2, 'ra (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'levels_published_prior_to_live_date_back_tested', 'raw_piece_cou
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `identifier_glue_excess_mass_raw`

- value: **39**  (from `identifier_glue.identifier_glue_excess_mass_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'historical_values_from_live_date_recorded_in_accordance_with_art; {'identifier': 'levels_published_prior_to_live_date_back_tested', 'raw_piece_cou; {'identifier': 'SolactiveTransatlanticCleanEnergyEURIndex5PercentAR', 'raw_piece (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'back_tested', 'raw_piece_count': 2, 'content_piece_count': 2, 'r; {'identifier': 'DocumentPart', 'raw_piece_count': 2, 'content_piece_count': 2, '; {'identifier': 'IndexLevel', 'raw_piece_count': 2, 'content_piece_count': 2, 'ra (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'levels_published_prior_to_live_date_back_tested', 'raw_piece_cou
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `low_source_grounded_glued_identifier_count`

- value: **7**  (from `identifier_glue.low_source_grounded_glued_identifier_count`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'historical_values_from_live_date_recorded_in_accordance_with_art; {'identifier': 'levels_published_prior_to_live_date_back_tested', 'raw_piece_cou; {'identifier': 'SolactiveTransatlanticCleanEnergyEURIndex5PercentAR', 'raw_piece (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'back_tested', 'raw_piece_count': 2, 'content_piece_count': 2, 'r; {'identifier': 'DocumentPart', 'raw_piece_count': 2, 'content_piece_count': 2, '; {'identifier': 'IndexLevel', 'raw_piece_count': 2, 'content_piece_count': 2, 'ra (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'levels_published_prior_to_live_date_back_tested', 'raw_piece_cou
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `max_identifier_piece_count_content`

- value: **7**  (from `identifier_glue.max_identifier_piece_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'historical_values_from_live_date_recorded_in_accordance_with_art; {'identifier': 'levels_published_prior_to_live_date_back_tested', 'raw_piece_cou; {'identifier': 'SolactiveTransatlanticCleanEnergyEURIndex5PercentAR', 'raw_piece (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'back_tested', 'raw_piece_count': 2, 'content_piece_count': 2, 'r; {'identifier': 'DocumentPart', 'raw_piece_count': 2, 'content_piece_count': 2, '; {'identifier': 'IndexLevel', 'raw_piece_count': 2, 'content_piece_count': 2, 'ra (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'levels_published_prior_to_live_date_back_tested', 'raw_piece_cou
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `max_identifier_piece_count_raw`

- value: **13**  (from `identifier_glue.max_identifier_piece_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'historical_values_from_live_date_recorded_in_accordance_with_art; {'identifier': 'levels_published_prior_to_live_date_back_tested', 'raw_piece_cou; {'identifier': 'SolactiveTransatlanticCleanEnergyEURIndex5PercentAR', 'raw_piece (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'back_tested', 'raw_piece_count': 2, 'content_piece_count': 2, 'r; {'identifier': 'DocumentPart', 'raw_piece_count': 2, 'content_piece_count': 2, '; {'identifier': 'IndexLevel', 'raw_piece_count': 2, 'content_piece_count': 2, 'ra (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'levels_published_prior_to_live_date_back_tested', 'raw_piece_cou
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `mean_identifier_piece_count_content`

- value: **2.4411764705882355**  (from `identifier_glue.mean_identifier_piece_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'historical_values_from_live_date_recorded_in_accordance_with_art; {'identifier': 'levels_published_prior_to_live_date_back_tested', 'raw_piece_cou; {'identifier': 'SolactiveTransatlanticCleanEnergyEURIndex5PercentAR', 'raw_piece (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'back_tested', 'raw_piece_count': 2, 'content_piece_count': 2, 'r; {'identifier': 'DocumentPart', 'raw_piece_count': 2, 'content_piece_count': 2, '; {'identifier': 'IndexLevel', 'raw_piece_count': 2, 'content_piece_count': 2, 'ra (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'levels_published_prior_to_live_date_back_tested', 'raw_piece_cou
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `mean_identifier_piece_count_raw`

- value: **3.2941176470588234**  (from `identifier_glue.mean_identifier_piece_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'historical_values_from_live_date_recorded_in_accordance_with_art; {'identifier': 'levels_published_prior_to_live_date_back_tested', 'raw_piece_cou; {'identifier': 'SolactiveTransatlanticCleanEnergyEURIndex5PercentAR', 'raw_piece (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'back_tested', 'raw_piece_count': 2, 'content_piece_count': 2, 'r; {'identifier': 'DocumentPart', 'raw_piece_count': 2, 'content_piece_count': 2, '; {'identifier': 'IndexLevel', 'raw_piece_count': 2, 'content_piece_count': 2, 'ra (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'levels_published_prior_to_live_date_back_tested', 'raw_piece_cou
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `new_formula_content_token_count_vs_text_only`

- value: **33**  (from `grounding.new_formula_content_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → article8ofbmr; article_8_of_bmr; article_number (+30 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; article8ofbmr; article_8_of_bmr (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'section', 'current_count': 10, 'baseline_count': 0, 'delta': 10}; {'token': 'indexlevel', 'current_count': 8, 'baseline_count': 0, 'delta': 8}; {'token': 'period', 'current_count': 7, 'baseline_count': 1, 'delta': 6} (+17 more)
  - `grounding.origin_error_count` → 13

## [WARNING] `ontology_planning` / `new_formula_token_count_vs_text_only`

- value: **38**  (from `grounding.new_formula_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → article8ofbmr; article_8_of_bmr; article_number (+30 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; article8ofbmr; article_8_of_bmr (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'section', 'current_count': 10, 'baseline_count': 0, 'delta': 10}; {'token': 'indexlevel', 'current_count': 8, 'baseline_count': 0, 'delta': 8}; {'token': 'period', 'current_count': 7, 'baseline_count': 1, 'delta': 6} (+17 more)
  - `grounding.origin_error_count` → 13

## [WARNING] `ontology_planning` / `new_full_surface_content_token_count_vs_text_only`

- value: **53**  (from `grounding.new_full_surface_content_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → article8ofbmr; article_8_of_bmr; article_number (+30 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; article8ofbmr; article_8_of_bmr (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'section', 'current_count': 10, 'baseline_count': 0, 'delta': 10}; {'token': 'indexlevel', 'current_count': 8, 'baseline_count': 0, 'delta': 8}; {'token': 'period', 'current_count': 7, 'baseline_count': 1, 'delta': 6} (+17 more)
  - `grounding.origin_error_count` → 13

## [WARNING] `ontology_planning` / `new_full_surface_token_count_vs_text_only`

- value: **60**  (from `grounding.new_full_surface_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → article8ofbmr; article_8_of_bmr; article_number (+30 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; article8ofbmr; article_8_of_bmr (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'section', 'current_count': 10, 'baseline_count': 0, 'delta': 10}; {'token': 'indexlevel', 'current_count': 8, 'baseline_count': 0, 'delta': 8}; {'token': 'period', 'current_count': 7, 'baseline_count': 1, 'delta': 6} (+17 more)
  - `grounding.origin_error_count` → 13

## [WARNING] `ontology_planning` / `new_surface_content_token_count`

- value: **91**  (from `<search recursive metrics JSON for key `new_surface_content_token_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → article8ofbmr; article_8_of_bmr; article_number (+30 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; article8ofbmr; article_8_of_bmr (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'section', 'current_count': 10, 'baseline_count': 0, 'delta': 10}; {'token': 'indexlevel', 'current_count': 8, 'baseline_count': 0, 'delta': 8}; {'token': 'period', 'current_count': 7, 'baseline_count': 1, 'delta': 6} (+17 more)
  - `grounding.origin_error_count` → 13

## [WARNING] `ontology_planning` / `new_surface_token_count`

- value: **91**  (from `<search recursive metrics JSON for key `new_surface_token_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → article8ofbmr; article_8_of_bmr; article_number (+30 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; article8ofbmr; article_8_of_bmr (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'section', 'current_count': 10, 'baseline_count': 0, 'delta': 10}; {'token': 'indexlevel', 'current_count': 8, 'baseline_count': 0, 'delta': 8}; {'token': 'period', 'current_count': 7, 'baseline_count': 1, 'delta': 6} (+17 more)
  - `grounding.origin_error_count` → 13

## [WARNING] `ontology_planning` / `ungrounded_callee_count`

- value: **1**  (from `grounding.ungrounded_callee_count`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → article8ofbmr; article_8_of_bmr; article_number (+30 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; article8ofbmr; article_8_of_bmr (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'section', 'current_count': 10, 'baseline_count': 0, 'delta': 10}; {'token': 'indexlevel', 'current_count': 8, 'baseline_count': 0, 'delta': 8}; {'token': 'period', 'current_count': 7, 'baseline_count': 1, 'delta': 6} (+17 more)
  - `grounding.origin_error_count` → 13

## [WARNING] `ontology_planning` / `ungrounded_sort_count`

- value: **5**  (from `grounding.ungrounded_sort_count`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → article8ofbmr; article_8_of_bmr; article_number (+30 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; article8ofbmr; article_8_of_bmr (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'section', 'current_count': 10, 'baseline_count': 0, 'delta': 10}; {'token': 'indexlevel', 'current_count': 8, 'baseline_count': 0, 'delta': 8}; {'token': 'period', 'current_count': 7, 'baseline_count': 1, 'delta': 6} (+17 more)
  - `grounding.origin_error_count` → 13

## [WARNING] `ontology_planning` / `ungrounded_symbol_count`

- value: **3**  (from `grounding.ungrounded_symbol_count`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → article8ofbmr; article_8_of_bmr; article_number (+30 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; article8ofbmr; article_8_of_bmr (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'section', 'current_count': 10, 'baseline_count': 0, 'delta': 10}; {'token': 'indexlevel', 'current_count': 8, 'baseline_count': 0, 'delta': 8}; {'token': 'period', 'current_count': 7, 'baseline_count': 1, 'delta': 6} (+17 more)
  - `grounding.origin_error_count` → 13
