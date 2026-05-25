# Diagnostic report — section_2_1

- **gate**: `needs_review`
- fail: 0, warning: 36

## [WARNING] `a4v3_semantic_lint` / `unused_sort_entity_declaration_count`

- value: **1**  (from `a4v3_semantic_lint_v1.json::summary.unused_sort_entity_count`)
- meaning: The IR may contain support ontology that no current formula uses.
- repair: Inspect whether the declaration is intentionally supporting context; otherwise delete it.
- evidence:
  - `a4v3_semantic_lint_v1.json::findings` → AvoidFrequentChangesBetweenTwoShareClasses

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

## [WARNING] `merge_canonicalization` / `cross_reference_usage_count`

- value: **1**  (from `<search recursive metrics JSON for key `cross_reference_usage_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `evidence.ir_cross_references` → entity SolactiveGBSBenchmarkSeriesPdf : Document

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

- value: **27**  (from `parameterization.quantifier_parameter_slot_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `assertion_complexity.top_complex_assertions` → eligible_for_index_universe_requirements; declared_lookback_windows; current_company_buffer_rule (+7 more)
  - `assertion_complexity.max_assertion_depth` → 10
  - `assertion_complexity.total_quantifier_count` → 27

## [WARNING] `merge_canonicalization` / `top_level_parameter_slot_count`

- value: **47**  (from `parameterization.top_level_parameter_slot_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 47
  - `<related section in metrics JSON>` → 47

## [WARNING] `merge_canonicalization` / `total_parameter_slot_mass`

- value: **74**  (from `parameterization.total_parameter_slot_mass`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 74
  - `<related section in metrics JSON>` → 74

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

- value: **47**  (from `identifier_glue.compound_identifier_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'HttpsWwwSolactiveComDownloadsGuidelineSolactiveGBSBenchmarkSerie; {'identifier': 'minimum_average_daily_value_traded_over_declared_lookback_window; {'identifier': 'highest_minimum_average_daily_value_traded_share_class_company', (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'declared_lookback_windows', 'raw_piece_count': 3, 'content_piece; {'identifier': 'index_universe_bridge', 'raw_piece_count': 3, 'content_piece_cou; {'identifier': 'MonetaryAmountScale', 'raw_piece_count': 3, 'content_piece_count (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'months_prior_including_selection_day', 'raw_piece_count': 5, 'co; {'identifier': 'eligible_by_not_current_company_buffer_rule', 'raw_piece_count':; {'identifier': 'NotCurrentCompanyBufferRule', 'raw_piece_count': 5, 'content_pie
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'months_prior_including_selection_day', 'raw_piece_count': 5, 'co; {'identifier': 'company_currently_included_in_index', 'raw_piece_count': 5, 'con; {'identifier': 'share_class_currently_included_in_index', 'raw_piece_count': 6,  (+1 more)

## [WARNING] `ontology_planning` / `compound_identifier_count_raw`

- value: **39**  (from `identifier_glue.compound_identifier_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'HttpsWwwSolactiveComDownloadsGuidelineSolactiveGBSBenchmarkSerie; {'identifier': 'minimum_average_daily_value_traded_over_declared_lookback_window; {'identifier': 'highest_minimum_average_daily_value_traded_share_class_company', (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'declared_lookback_windows', 'raw_piece_count': 3, 'content_piece; {'identifier': 'index_universe_bridge', 'raw_piece_count': 3, 'content_piece_cou; {'identifier': 'MonetaryAmountScale', 'raw_piece_count': 3, 'content_piece_count (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'months_prior_including_selection_day', 'raw_piece_count': 5, 'co; {'identifier': 'eligible_by_not_current_company_buffer_rule', 'raw_piece_count':; {'identifier': 'NotCurrentCompanyBufferRule', 'raw_piece_count': 5, 'content_pie
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'months_prior_including_selection_day', 'raw_piece_count': 5, 'co; {'identifier': 'company_currently_included_in_index', 'raw_piece_count': 5, 'con; {'identifier': 'share_class_currently_included_in_index', 'raw_piece_count': 6,  (+1 more)

## [WARNING] `ontology_planning` / `cross_reference_usage_count`

- value: **1**  (from `<search recursive metrics JSON for key `cross_reference_usage_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `evidence.ir_cross_references` → entity SolactiveGBSBenchmarkSeriesPdf : Document

## [WARNING] `ontology_planning` / `dependency_link_count`

- value: **2**  (from `<search recursive metrics JSON for key `dependency_link_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 2
  - `<related section in metrics JSON>` → 2

## [WARNING] `ontology_planning` / `identifier_count`

- value: **81**  (from `identifier_glue.identifier_count`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'HttpsWwwSolactiveComDownloadsGuidelineSolactiveGBSBenchmarkSerie; {'identifier': 'minimum_average_daily_value_traded_over_declared_lookback_window; {'identifier': 'highest_minimum_average_daily_value_traded_share_class_company', (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'declared_lookback_windows', 'raw_piece_count': 3, 'content_piece; {'identifier': 'index_universe_bridge', 'raw_piece_count': 3, 'content_piece_cou; {'identifier': 'MonetaryAmountScale', 'raw_piece_count': 3, 'content_piece_count (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'months_prior_including_selection_day', 'raw_piece_count': 5, 'co; {'identifier': 'eligible_by_not_current_company_buffer_rule', 'raw_piece_count':; {'identifier': 'NotCurrentCompanyBufferRule', 'raw_piece_count': 5, 'content_pie
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'months_prior_including_selection_day', 'raw_piece_count': 5, 'co; {'identifier': 'company_currently_included_in_index', 'raw_piece_count': 5, 'con; {'identifier': 'share_class_currently_included_in_index', 'raw_piece_count': 6,  (+1 more)

## [WARNING] `ontology_planning` / `identifier_glue_excess_mass_content`

- value: **139**  (from `identifier_glue.identifier_glue_excess_mass_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'HttpsWwwSolactiveComDownloadsGuidelineSolactiveGBSBenchmarkSerie; {'identifier': 'minimum_average_daily_value_traded_over_declared_lookback_window; {'identifier': 'highest_minimum_average_daily_value_traded_share_class_company', (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'declared_lookback_windows', 'raw_piece_count': 3, 'content_piece; {'identifier': 'index_universe_bridge', 'raw_piece_count': 3, 'content_piece_cou; {'identifier': 'MonetaryAmountScale', 'raw_piece_count': 3, 'content_piece_count (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'months_prior_including_selection_day', 'raw_piece_count': 5, 'co; {'identifier': 'eligible_by_not_current_company_buffer_rule', 'raw_piece_count':; {'identifier': 'NotCurrentCompanyBufferRule', 'raw_piece_count': 5, 'content_pie
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'months_prior_including_selection_day', 'raw_piece_count': 5, 'co; {'identifier': 'company_currently_included_in_index', 'raw_piece_count': 5, 'con; {'identifier': 'share_class_currently_included_in_index', 'raw_piece_count': 6,  (+1 more)

## [WARNING] `ontology_planning` / `identifier_glue_excess_mass_raw`

- value: **111**  (from `identifier_glue.identifier_glue_excess_mass_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'HttpsWwwSolactiveComDownloadsGuidelineSolactiveGBSBenchmarkSerie; {'identifier': 'minimum_average_daily_value_traded_over_declared_lookback_window; {'identifier': 'highest_minimum_average_daily_value_traded_share_class_company', (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'declared_lookback_windows', 'raw_piece_count': 3, 'content_piece; {'identifier': 'index_universe_bridge', 'raw_piece_count': 3, 'content_piece_cou; {'identifier': 'MonetaryAmountScale', 'raw_piece_count': 3, 'content_piece_count (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'months_prior_including_selection_day', 'raw_piece_count': 5, 'co; {'identifier': 'eligible_by_not_current_company_buffer_rule', 'raw_piece_count':; {'identifier': 'NotCurrentCompanyBufferRule', 'raw_piece_count': 5, 'content_pie
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'months_prior_including_selection_day', 'raw_piece_count': 5, 'co; {'identifier': 'company_currently_included_in_index', 'raw_piece_count': 5, 'con; {'identifier': 'share_class_currently_included_in_index', 'raw_piece_count': 6,  (+1 more)

## [WARNING] `ontology_planning` / `invented_helper_sort_count`

- value: **1**  (from `<search recursive metrics JSON for key `invented_helper_sort_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → appendix_rbics_subindustry_classification; appendix_rbics_subindustry_classification_definition; average_daily_value_traded (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; appendix_rbics_subindustry_classification; appendix_rbics_subindustry_classification_definition (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'selectionday', 'current_count': 32, 'baseline_count': 0, 'delta': 32}; {'token': 'company', 'current_count': 33, 'baseline_count': 5, 'delta': 28}; {'token': 'value', 'current_count': 32, 'baseline_count': 4, 'delta': 28} (+17 more)
  - `grounding.origin_error_count` → 23
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'HttpsWwwSolactiveComDownloadsGuidelineSolactiveGBSBenchmarkSerie; {'identifier': 'minimum_average_daily_value_traded_over_declared_lookback_window; {'identifier': 'highest_minimum_average_daily_value_traded_share_class_company', (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'declared_lookback_windows', 'raw_piece_count': 3, 'content_piece; {'identifier': 'index_universe_bridge', 'raw_piece_count': 3, 'content_piece_cou; {'identifier': 'MonetaryAmountScale', 'raw_piece_count': 3, 'content_piece_count (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'months_prior_including_selection_day', 'raw_piece_count': 5, 'co; {'identifier': 'eligible_by_not_current_company_buffer_rule', 'raw_piece_count':; {'identifier': 'NotCurrentCompanyBufferRule', 'raw_piece_count': 5, 'content_pie
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'months_prior_including_selection_day', 'raw_piece_count': 5, 'co; {'identifier': 'company_currently_included_in_index', 'raw_piece_count': 5, 'con; {'identifier': 'share_class_currently_included_in_index', 'raw_piece_count': 6,  (+1 more)
  - `evidence.invented_helper_sorts` → ISIN

## [WARNING] `ontology_planning` / `invented_helper_symbol_count`

- value: **1**  (from `<search recursive metrics JSON for key `invented_helper_symbol_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → appendix_rbics_subindustry_classification; appendix_rbics_subindustry_classification_definition; average_daily_value_traded (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; appendix_rbics_subindustry_classification; appendix_rbics_subindustry_classification_definition (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'selectionday', 'current_count': 32, 'baseline_count': 0, 'delta': 32}; {'token': 'company', 'current_count': 33, 'baseline_count': 5, 'delta': 28}; {'token': 'value', 'current_count': 32, 'baseline_count': 4, 'delta': 28} (+17 more)
  - `grounding.origin_error_count` → 23
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'HttpsWwwSolactiveComDownloadsGuidelineSolactiveGBSBenchmarkSerie; {'identifier': 'minimum_average_daily_value_traded_over_declared_lookback_window; {'identifier': 'highest_minimum_average_daily_value_traded_share_class_company', (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'declared_lookback_windows', 'raw_piece_count': 3, 'content_piece; {'identifier': 'index_universe_bridge', 'raw_piece_count': 3, 'content_piece_cou; {'identifier': 'MonetaryAmountScale', 'raw_piece_count': 3, 'content_piece_count (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'months_prior_including_selection_day', 'raw_piece_count': 5, 'co; {'identifier': 'eligible_by_not_current_company_buffer_rule', 'raw_piece_count':; {'identifier': 'NotCurrentCompanyBufferRule', 'raw_piece_count': 5, 'content_pie
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'months_prior_including_selection_day', 'raw_piece_count': 5, 'co; {'identifier': 'company_currently_included_in_index', 'raw_piece_count': 5, 'con; {'identifier': 'share_class_currently_included_in_index', 'raw_piece_count': 6,  (+1 more)
  - `evidence.invented_helper_sorts` → ISIN

## [WARNING] `ontology_planning` / `low_source_grounded_glued_identifier_count`

- value: **27**  (from `identifier_glue.low_source_grounded_glued_identifier_count`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'HttpsWwwSolactiveComDownloadsGuidelineSolactiveGBSBenchmarkSerie; {'identifier': 'minimum_average_daily_value_traded_over_declared_lookback_window; {'identifier': 'highest_minimum_average_daily_value_traded_share_class_company', (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'declared_lookback_windows', 'raw_piece_count': 3, 'content_piece; {'identifier': 'index_universe_bridge', 'raw_piece_count': 3, 'content_piece_cou; {'identifier': 'MonetaryAmountScale', 'raw_piece_count': 3, 'content_piece_count (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'months_prior_including_selection_day', 'raw_piece_count': 5, 'co; {'identifier': 'eligible_by_not_current_company_buffer_rule', 'raw_piece_count':; {'identifier': 'NotCurrentCompanyBufferRule', 'raw_piece_count': 5, 'content_pie
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'months_prior_including_selection_day', 'raw_piece_count': 5, 'co; {'identifier': 'company_currently_included_in_index', 'raw_piece_count': 5, 'con; {'identifier': 'share_class_currently_included_in_index', 'raw_piece_count': 6,  (+1 more)

## [WARNING] `ontology_planning` / `max_identifier_piece_count_content`

- value: **10**  (from `identifier_glue.max_identifier_piece_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'HttpsWwwSolactiveComDownloadsGuidelineSolactiveGBSBenchmarkSerie; {'identifier': 'minimum_average_daily_value_traded_over_declared_lookback_window; {'identifier': 'highest_minimum_average_daily_value_traded_share_class_company', (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'declared_lookback_windows', 'raw_piece_count': 3, 'content_piece; {'identifier': 'index_universe_bridge', 'raw_piece_count': 3, 'content_piece_cou; {'identifier': 'MonetaryAmountScale', 'raw_piece_count': 3, 'content_piece_count (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'months_prior_including_selection_day', 'raw_piece_count': 5, 'co; {'identifier': 'eligible_by_not_current_company_buffer_rule', 'raw_piece_count':; {'identifier': 'NotCurrentCompanyBufferRule', 'raw_piece_count': 5, 'content_pie
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'months_prior_including_selection_day', 'raw_piece_count': 5, 'co; {'identifier': 'company_currently_included_in_index', 'raw_piece_count': 5, 'con; {'identifier': 'share_class_currently_included_in_index', 'raw_piece_count': 6,  (+1 more)

## [WARNING] `ontology_planning` / `max_identifier_piece_count_raw`

- value: **10**  (from `identifier_glue.max_identifier_piece_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'HttpsWwwSolactiveComDownloadsGuidelineSolactiveGBSBenchmarkSerie; {'identifier': 'minimum_average_daily_value_traded_over_declared_lookback_window; {'identifier': 'highest_minimum_average_daily_value_traded_share_class_company', (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'declared_lookback_windows', 'raw_piece_count': 3, 'content_piece; {'identifier': 'index_universe_bridge', 'raw_piece_count': 3, 'content_piece_cou; {'identifier': 'MonetaryAmountScale', 'raw_piece_count': 3, 'content_piece_count (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'months_prior_including_selection_day', 'raw_piece_count': 5, 'co; {'identifier': 'eligible_by_not_current_company_buffer_rule', 'raw_piece_count':; {'identifier': 'NotCurrentCompanyBufferRule', 'raw_piece_count': 5, 'content_pie
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'months_prior_including_selection_day', 'raw_piece_count': 5, 'co; {'identifier': 'company_currently_included_in_index', 'raw_piece_count': 5, 'con; {'identifier': 'share_class_currently_included_in_index', 'raw_piece_count': 6,  (+1 more)

## [WARNING] `ontology_planning` / `mean_identifier_piece_count_content`

- value: **3.45679012345679**  (from `identifier_glue.mean_identifier_piece_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'HttpsWwwSolactiveComDownloadsGuidelineSolactiveGBSBenchmarkSerie; {'identifier': 'minimum_average_daily_value_traded_over_declared_lookback_window; {'identifier': 'highest_minimum_average_daily_value_traded_share_class_company', (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'declared_lookback_windows', 'raw_piece_count': 3, 'content_piece; {'identifier': 'index_universe_bridge', 'raw_piece_count': 3, 'content_piece_cou; {'identifier': 'MonetaryAmountScale', 'raw_piece_count': 3, 'content_piece_count (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'months_prior_including_selection_day', 'raw_piece_count': 5, 'co; {'identifier': 'eligible_by_not_current_company_buffer_rule', 'raw_piece_count':; {'identifier': 'NotCurrentCompanyBufferRule', 'raw_piece_count': 5, 'content_pie
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'months_prior_including_selection_day', 'raw_piece_count': 5, 'co; {'identifier': 'company_currently_included_in_index', 'raw_piece_count': 5, 'con; {'identifier': 'share_class_currently_included_in_index', 'raw_piece_count': 6,  (+1 more)

## [WARNING] `ontology_planning` / `mean_identifier_piece_count_raw`

- value: **3.765432098765432**  (from `identifier_glue.mean_identifier_piece_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'HttpsWwwSolactiveComDownloadsGuidelineSolactiveGBSBenchmarkSerie; {'identifier': 'minimum_average_daily_value_traded_over_declared_lookback_window; {'identifier': 'highest_minimum_average_daily_value_traded_share_class_company', (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'declared_lookback_windows', 'raw_piece_count': 3, 'content_piece; {'identifier': 'index_universe_bridge', 'raw_piece_count': 3, 'content_piece_cou; {'identifier': 'MonetaryAmountScale', 'raw_piece_count': 3, 'content_piece_count (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'months_prior_including_selection_day', 'raw_piece_count': 5, 'co; {'identifier': 'eligible_by_not_current_company_buffer_rule', 'raw_piece_count':; {'identifier': 'NotCurrentCompanyBufferRule', 'raw_piece_count': 5, 'content_pie
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'months_prior_including_selection_day', 'raw_piece_count': 5, 'co; {'identifier': 'company_currently_included_in_index', 'raw_piece_count': 5, 'con; {'identifier': 'share_class_currently_included_in_index', 'raw_piece_count': 6,  (+1 more)

## [WARNING] `ontology_planning` / `new_formula_content_token_count_vs_text_only`

- value: **96**  (from `grounding.new_formula_content_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → appendix_rbics_subindustry_classification; appendix_rbics_subindustry_classification_definition; average_daily_value_traded (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; appendix_rbics_subindustry_classification; appendix_rbics_subindustry_classification_definition (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'selectionday', 'current_count': 32, 'baseline_count': 0, 'delta': 32}; {'token': 'company', 'current_count': 33, 'baseline_count': 5, 'delta': 28}; {'token': 'value', 'current_count': 32, 'baseline_count': 4, 'delta': 28} (+17 more)
  - `grounding.origin_error_count` → 23

## [WARNING] `ontology_planning` / `new_formula_token_count_vs_text_only`

- value: **102**  (from `grounding.new_formula_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → appendix_rbics_subindustry_classification; appendix_rbics_subindustry_classification_definition; average_daily_value_traded (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; appendix_rbics_subindustry_classification; appendix_rbics_subindustry_classification_definition (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'selectionday', 'current_count': 32, 'baseline_count': 0, 'delta': 32}; {'token': 'company', 'current_count': 33, 'baseline_count': 5, 'delta': 28}; {'token': 'value', 'current_count': 32, 'baseline_count': 4, 'delta': 28} (+17 more)
  - `grounding.origin_error_count` → 23

## [WARNING] `ontology_planning` / `new_full_surface_content_token_count_vs_text_only`

- value: **116**  (from `grounding.new_full_surface_content_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → appendix_rbics_subindustry_classification; appendix_rbics_subindustry_classification_definition; average_daily_value_traded (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; appendix_rbics_subindustry_classification; appendix_rbics_subindustry_classification_definition (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'selectionday', 'current_count': 32, 'baseline_count': 0, 'delta': 32}; {'token': 'company', 'current_count': 33, 'baseline_count': 5, 'delta': 28}; {'token': 'value', 'current_count': 32, 'baseline_count': 4, 'delta': 28} (+17 more)
  - `grounding.origin_error_count` → 23

## [WARNING] `ontology_planning` / `new_full_surface_token_count_vs_text_only`

- value: **125**  (from `grounding.new_full_surface_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → appendix_rbics_subindustry_classification; appendix_rbics_subindustry_classification_definition; average_daily_value_traded (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; appendix_rbics_subindustry_classification; appendix_rbics_subindustry_classification_definition (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'selectionday', 'current_count': 32, 'baseline_count': 0, 'delta': 32}; {'token': 'company', 'current_count': 33, 'baseline_count': 5, 'delta': 28}; {'token': 'value', 'current_count': 32, 'baseline_count': 4, 'delta': 28} (+17 more)
  - `grounding.origin_error_count` → 23

## [WARNING] `ontology_planning` / `new_surface_content_token_count`

- value: **361**  (from `<search recursive metrics JSON for key `new_surface_content_token_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → appendix_rbics_subindustry_classification; appendix_rbics_subindustry_classification_definition; average_daily_value_traded (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; appendix_rbics_subindustry_classification; appendix_rbics_subindustry_classification_definition (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'selectionday', 'current_count': 32, 'baseline_count': 0, 'delta': 32}; {'token': 'company', 'current_count': 33, 'baseline_count': 5, 'delta': 28}; {'token': 'value', 'current_count': 32, 'baseline_count': 4, 'delta': 28} (+17 more)
  - `grounding.origin_error_count` → 23

## [WARNING] `ontology_planning` / `new_surface_token_count`

- value: **361**  (from `<search recursive metrics JSON for key `new_surface_token_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → appendix_rbics_subindustry_classification; appendix_rbics_subindustry_classification_definition; average_daily_value_traded (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; appendix_rbics_subindustry_classification; appendix_rbics_subindustry_classification_definition (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'selectionday', 'current_count': 32, 'baseline_count': 0, 'delta': 32}; {'token': 'company', 'current_count': 33, 'baseline_count': 5, 'delta': 28}; {'token': 'value', 'current_count': 32, 'baseline_count': 4, 'delta': 28} (+17 more)
  - `grounding.origin_error_count` → 23

## [WARNING] `ontology_planning` / `ungrounded_sort_count`

- value: **13**  (from `grounding.ungrounded_sort_count`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → appendix_rbics_subindustry_classification; appendix_rbics_subindustry_classification_definition; average_daily_value_traded (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; appendix_rbics_subindustry_classification; appendix_rbics_subindustry_classification_definition (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'selectionday', 'current_count': 32, 'baseline_count': 0, 'delta': 32}; {'token': 'company', 'current_count': 33, 'baseline_count': 5, 'delta': 28}; {'token': 'value', 'current_count': 32, 'baseline_count': 4, 'delta': 28} (+17 more)
  - `grounding.origin_error_count` → 23

## [WARNING] `ontology_planning` / `ungrounded_symbol_count`

- value: **3**  (from `grounding.ungrounded_symbol_count`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → appendix_rbics_subindustry_classification; appendix_rbics_subindustry_classification_definition; average_daily_value_traded (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; appendix_rbics_subindustry_classification; appendix_rbics_subindustry_classification_definition (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'selectionday', 'current_count': 32, 'baseline_count': 0, 'delta': 32}; {'token': 'company', 'current_count': 33, 'baseline_count': 5, 'delta': 28}; {'token': 'value', 'current_count': 32, 'baseline_count': 4, 'delta': 28} (+17 more)
  - `grounding.origin_error_count` → 23
