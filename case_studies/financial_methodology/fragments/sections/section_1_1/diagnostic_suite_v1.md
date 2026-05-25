# Diagnostic report — section_1_1

- **gate**: `needs_review`
- fail: 0, warning: 34

## [WARNING] `merge_canonicalization` / `callable_symbol_count`

- value: **8**  (from `parameterization.callable_symbol_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 8
  - `<related section in metrics JSON>` → 8

## [WARNING] `merge_canonicalization` / `callable_symbol_with_args_count`

- value: **8**  (from `parameterization.callable_symbol_with_args_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 8
  - `<related section in metrics JSON>` → 8

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

- value: **8**  (from `parameterization.factorization_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 8
  - `<related section in metrics JSON>` → 8

## [WARNING] `merge_canonicalization` / `focus_signature_unique_count`

- value: **1**  (from `variability.focus_signature_unique_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.

## [WARNING] `merge_canonicalization` / `quantifier_parameter_slot_count`

- value: **2**  (from `parameterization.quantifier_parameter_slot_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `assertion_complexity.top_complex_assertions` → no_rebalancing_fee_means_rebalancing_fee_not_charged; clean_energy_strategy_represents_clean_energy_securities
  - `assertion_complexity.max_assertion_depth` → 5
  - `assertion_complexity.total_quantifier_count` → 2

## [WARNING] `merge_canonicalization` / `top_level_parameter_slot_count`

- value: **12**  (from `parameterization.top_level_parameter_slot_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 12
  - `<related section in metrics JSON>` → 12

## [WARNING] `merge_canonicalization` / `total_parameter_slot_mass`

- value: **14**  (from `parameterization.total_parameter_slot_mass`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 14
  - `<related section in metrics JSON>` → 14

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

- value: **7**  (from `identifier_glue.compound_identifier_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'clean_energy_strategy_represents_clean_energy_securities', 'raw_; {'identifier': 'no_rebalancing_fee_means_rebalancing_fee_not_charged', 'raw_piec; {'identifier': 'CleanEnergyBusinessOperationsStrategy', 'raw_piece_count': 5, 'c (+16 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'security_has_business_operations_in', 'raw_piece_count': 5, 'con; {'identifier': 'IndexStrategy', 'raw_piece_count': 2, 'content_piece_count': 2, ; {'identifier': 'no_rebalancing_fee_means_rebalancing_fee_not_charged', 'raw_piec (+11 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'no_rebalancing_fee_means_rebalancing_fee_not_charged', 'raw_piec
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `compound_identifier_count_raw`

- value: **5**  (from `identifier_glue.compound_identifier_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'clean_energy_strategy_represents_clean_energy_securities', 'raw_; {'identifier': 'no_rebalancing_fee_means_rebalancing_fee_not_charged', 'raw_piec; {'identifier': 'CleanEnergyBusinessOperationsStrategy', 'raw_piece_count': 5, 'c (+16 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'security_has_business_operations_in', 'raw_piece_count': 5, 'con; {'identifier': 'IndexStrategy', 'raw_piece_count': 2, 'content_piece_count': 2, ; {'identifier': 'no_rebalancing_fee_means_rebalancing_fee_not_charged', 'raw_piec (+11 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'no_rebalancing_fee_means_rebalancing_fee_not_charged', 'raw_piec
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `dependency_link_count`

- value: **2**  (from `<search recursive metrics JSON for key `dependency_link_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 2
  - `<related section in metrics JSON>` → 2

## [WARNING] `ontology_planning` / `identifier_count`

- value: **19**  (from `identifier_glue.identifier_count`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'clean_energy_strategy_represents_clean_energy_securities', 'raw_; {'identifier': 'no_rebalancing_fee_means_rebalancing_fee_not_charged', 'raw_piec; {'identifier': 'CleanEnergyBusinessOperationsStrategy', 'raw_piece_count': 5, 'c (+16 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'security_has_business_operations_in', 'raw_piece_count': 5, 'con; {'identifier': 'IndexStrategy', 'raw_piece_count': 2, 'content_piece_count': 2, ; {'identifier': 'no_rebalancing_fee_means_rebalancing_fee_not_charged', 'raw_piec (+11 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'no_rebalancing_fee_means_rebalancing_fee_not_charged', 'raw_piec
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `identifier_glue_excess_mass_content`

- value: **17**  (from `identifier_glue.identifier_glue_excess_mass_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'clean_energy_strategy_represents_clean_energy_securities', 'raw_; {'identifier': 'no_rebalancing_fee_means_rebalancing_fee_not_charged', 'raw_piec; {'identifier': 'CleanEnergyBusinessOperationsStrategy', 'raw_piece_count': 5, 'c (+16 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'security_has_business_operations_in', 'raw_piece_count': 5, 'con; {'identifier': 'IndexStrategy', 'raw_piece_count': 2, 'content_piece_count': 2, ; {'identifier': 'no_rebalancing_fee_means_rebalancing_fee_not_charged', 'raw_piec (+11 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'no_rebalancing_fee_means_rebalancing_fee_not_charged', 'raw_piec
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `identifier_glue_excess_mass_raw`

- value: **14**  (from `identifier_glue.identifier_glue_excess_mass_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'clean_energy_strategy_represents_clean_energy_securities', 'raw_; {'identifier': 'no_rebalancing_fee_means_rebalancing_fee_not_charged', 'raw_piec; {'identifier': 'CleanEnergyBusinessOperationsStrategy', 'raw_piece_count': 5, 'c (+16 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'security_has_business_operations_in', 'raw_piece_count': 5, 'con; {'identifier': 'IndexStrategy', 'raw_piece_count': 2, 'content_piece_count': 2, ; {'identifier': 'no_rebalancing_fee_means_rebalancing_fee_not_charged', 'raw_piec (+11 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'no_rebalancing_fee_means_rebalancing_fee_not_charged', 'raw_piec
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `invented_helper_sort_count`

- value: **1**  (from `<search recursive metrics JSON for key `invented_helper_sort_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → asset_class; assetclass; businessfield (+23 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; asset_class; assetclass (+43 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'security', 'current_count': 8, 'baseline_count': 0, 'delta': 8}; {'token': 'theindex', 'current_count': 8, 'baseline_count': 0, 'delta': 8}; {'token': 'rebalancing', 'current_count': 9, 'baseline_count': 2, 'delta': 7} (+17 more)
  - `grounding.origin_error_count` → 5
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'clean_energy_strategy_represents_clean_energy_securities', 'raw_; {'identifier': 'no_rebalancing_fee_means_rebalancing_fee_not_charged', 'raw_piec; {'identifier': 'CleanEnergyBusinessOperationsStrategy', 'raw_piece_count': 5, 'c (+16 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'security_has_business_operations_in', 'raw_piece_count': 5, 'con; {'identifier': 'IndexStrategy', 'raw_piece_count': 2, 'content_piece_count': 2, ; {'identifier': 'no_rebalancing_fee_means_rebalancing_fee_not_charged', 'raw_piec (+11 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'no_rebalancing_fee_means_rebalancing_fee_not_charged', 'raw_piec
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)
  - `evidence.invented_helper_sorts` → Security

## [WARNING] `ontology_planning` / `invented_helper_symbol_count`

- value: **1**  (from `<search recursive metrics JSON for key `invented_helper_symbol_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → asset_class; assetclass; businessfield (+23 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; asset_class; assetclass (+43 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'security', 'current_count': 8, 'baseline_count': 0, 'delta': 8}; {'token': 'theindex', 'current_count': 8, 'baseline_count': 0, 'delta': 8}; {'token': 'rebalancing', 'current_count': 9, 'baseline_count': 2, 'delta': 7} (+17 more)
  - `grounding.origin_error_count` → 5
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'clean_energy_strategy_represents_clean_energy_securities', 'raw_; {'identifier': 'no_rebalancing_fee_means_rebalancing_fee_not_charged', 'raw_piec; {'identifier': 'CleanEnergyBusinessOperationsStrategy', 'raw_piece_count': 5, 'c (+16 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'security_has_business_operations_in', 'raw_piece_count': 5, 'con; {'identifier': 'IndexStrategy', 'raw_piece_count': 2, 'content_piece_count': 2, ; {'identifier': 'no_rebalancing_fee_means_rebalancing_fee_not_charged', 'raw_piec (+11 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'no_rebalancing_fee_means_rebalancing_fee_not_charged', 'raw_piec
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)
  - `evidence.invented_helper_sorts` → Security

## [WARNING] `ontology_planning` / `low_source_grounded_glued_identifier_count`

- value: **5**  (from `identifier_glue.low_source_grounded_glued_identifier_count`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'clean_energy_strategy_represents_clean_energy_securities', 'raw_; {'identifier': 'no_rebalancing_fee_means_rebalancing_fee_not_charged', 'raw_piec; {'identifier': 'CleanEnergyBusinessOperationsStrategy', 'raw_piece_count': 5, 'c (+16 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'security_has_business_operations_in', 'raw_piece_count': 5, 'con; {'identifier': 'IndexStrategy', 'raw_piece_count': 2, 'content_piece_count': 2, ; {'identifier': 'no_rebalancing_fee_means_rebalancing_fee_not_charged', 'raw_piec (+11 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'no_rebalancing_fee_means_rebalancing_fee_not_charged', 'raw_piec
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `max_identifier_piece_count_content`

- value: **7**  (from `identifier_glue.max_identifier_piece_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'clean_energy_strategy_represents_clean_energy_securities', 'raw_; {'identifier': 'no_rebalancing_fee_means_rebalancing_fee_not_charged', 'raw_piec; {'identifier': 'CleanEnergyBusinessOperationsStrategy', 'raw_piece_count': 5, 'c (+16 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'security_has_business_operations_in', 'raw_piece_count': 5, 'con; {'identifier': 'IndexStrategy', 'raw_piece_count': 2, 'content_piece_count': 2, ; {'identifier': 'no_rebalancing_fee_means_rebalancing_fee_not_charged', 'raw_piec (+11 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'no_rebalancing_fee_means_rebalancing_fee_not_charged', 'raw_piec
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `max_identifier_piece_count_raw`

- value: **8**  (from `identifier_glue.max_identifier_piece_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'clean_energy_strategy_represents_clean_energy_securities', 'raw_; {'identifier': 'no_rebalancing_fee_means_rebalancing_fee_not_charged', 'raw_piec; {'identifier': 'CleanEnergyBusinessOperationsStrategy', 'raw_piece_count': 5, 'c (+16 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'security_has_business_operations_in', 'raw_piece_count': 5, 'con; {'identifier': 'IndexStrategy', 'raw_piece_count': 2, 'content_piece_count': 2, ; {'identifier': 'no_rebalancing_fee_means_rebalancing_fee_not_charged', 'raw_piec (+11 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'no_rebalancing_fee_means_rebalancing_fee_not_charged', 'raw_piec
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `mean_identifier_piece_count_content`

- value: **2.526315789473684**  (from `identifier_glue.mean_identifier_piece_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'clean_energy_strategy_represents_clean_energy_securities', 'raw_; {'identifier': 'no_rebalancing_fee_means_rebalancing_fee_not_charged', 'raw_piec; {'identifier': 'CleanEnergyBusinessOperationsStrategy', 'raw_piece_count': 5, 'c (+16 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'security_has_business_operations_in', 'raw_piece_count': 5, 'con; {'identifier': 'IndexStrategy', 'raw_piece_count': 2, 'content_piece_count': 2, ; {'identifier': 'no_rebalancing_fee_means_rebalancing_fee_not_charged', 'raw_piec (+11 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'no_rebalancing_fee_means_rebalancing_fee_not_charged', 'raw_piec
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `mean_identifier_piece_count_raw`

- value: **2.9473684210526314**  (from `identifier_glue.mean_identifier_piece_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'clean_energy_strategy_represents_clean_energy_securities', 'raw_; {'identifier': 'no_rebalancing_fee_means_rebalancing_fee_not_charged', 'raw_piec; {'identifier': 'CleanEnergyBusinessOperationsStrategy', 'raw_piece_count': 5, 'c (+16 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'security_has_business_operations_in', 'raw_piece_count': 5, 'con; {'identifier': 'IndexStrategy', 'raw_piece_count': 2, 'content_piece_count': 2, ; {'identifier': 'no_rebalancing_fee_means_rebalancing_fee_not_charged', 'raw_piec (+11 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'no_rebalancing_fee_means_rebalancing_fee_not_charged', 'raw_piec
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `new_formula_content_token_count_vs_text_only`

- value: **26**  (from `grounding.new_formula_content_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → asset_class; assetclass; businessfield (+23 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; asset_class; assetclass (+43 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'security', 'current_count': 8, 'baseline_count': 0, 'delta': 8}; {'token': 'theindex', 'current_count': 8, 'baseline_count': 0, 'delta': 8}; {'token': 'rebalancing', 'current_count': 9, 'baseline_count': 2, 'delta': 7} (+17 more)
  - `grounding.origin_error_count` → 5

## [WARNING] `ontology_planning` / `new_formula_token_count_vs_text_only`

- value: **28**  (from `grounding.new_formula_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → asset_class; assetclass; businessfield (+23 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; asset_class; assetclass (+43 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'security', 'current_count': 8, 'baseline_count': 0, 'delta': 8}; {'token': 'theindex', 'current_count': 8, 'baseline_count': 0, 'delta': 8}; {'token': 'rebalancing', 'current_count': 9, 'baseline_count': 2, 'delta': 7} (+17 more)
  - `grounding.origin_error_count` → 5

## [WARNING] `ontology_planning` / `new_full_surface_content_token_count_vs_text_only`

- value: **46**  (from `grounding.new_full_surface_content_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → asset_class; assetclass; businessfield (+23 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; asset_class; assetclass (+43 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'security', 'current_count': 8, 'baseline_count': 0, 'delta': 8}; {'token': 'theindex', 'current_count': 8, 'baseline_count': 0, 'delta': 8}; {'token': 'rebalancing', 'current_count': 9, 'baseline_count': 2, 'delta': 7} (+17 more)
  - `grounding.origin_error_count` → 5

## [WARNING] `ontology_planning` / `new_full_surface_token_count_vs_text_only`

- value: **52**  (from `grounding.new_full_surface_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → asset_class; assetclass; businessfield (+23 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; asset_class; assetclass (+43 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'security', 'current_count': 8, 'baseline_count': 0, 'delta': 8}; {'token': 'theindex', 'current_count': 8, 'baseline_count': 0, 'delta': 8}; {'token': 'rebalancing', 'current_count': 9, 'baseline_count': 2, 'delta': 7} (+17 more)
  - `grounding.origin_error_count` → 5

## [WARNING] `ontology_planning` / `new_surface_content_token_count`

- value: **59**  (from `<search recursive metrics JSON for key `new_surface_content_token_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → asset_class; assetclass; businessfield (+23 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; asset_class; assetclass (+43 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'security', 'current_count': 8, 'baseline_count': 0, 'delta': 8}; {'token': 'theindex', 'current_count': 8, 'baseline_count': 0, 'delta': 8}; {'token': 'rebalancing', 'current_count': 9, 'baseline_count': 2, 'delta': 7} (+17 more)
  - `grounding.origin_error_count` → 5

## [WARNING] `ontology_planning` / `new_surface_token_count`

- value: **59**  (from `<search recursive metrics JSON for key `new_surface_token_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → asset_class; assetclass; businessfield (+23 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; asset_class; assetclass (+43 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'security', 'current_count': 8, 'baseline_count': 0, 'delta': 8}; {'token': 'theindex', 'current_count': 8, 'baseline_count': 0, 'delta': 8}; {'token': 'rebalancing', 'current_count': 9, 'baseline_count': 2, 'delta': 7} (+17 more)
  - `grounding.origin_error_count` → 5

## [WARNING] `ontology_planning` / `ungrounded_ref_count`

- value: **1**  (from `grounding.ungrounded_ref_count`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → asset_class; assetclass; businessfield (+23 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; asset_class; assetclass (+43 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'security', 'current_count': 8, 'baseline_count': 0, 'delta': 8}; {'token': 'theindex', 'current_count': 8, 'baseline_count': 0, 'delta': 8}; {'token': 'rebalancing', 'current_count': 9, 'baseline_count': 2, 'delta': 7} (+17 more)
  - `grounding.origin_error_count` → 5

## [WARNING] `ontology_planning` / `ungrounded_sort_count`

- value: **1**  (from `grounding.ungrounded_sort_count`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → asset_class; assetclass; businessfield (+23 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; asset_class; assetclass (+43 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'security', 'current_count': 8, 'baseline_count': 0, 'delta': 8}; {'token': 'theindex', 'current_count': 8, 'baseline_count': 0, 'delta': 8}; {'token': 'rebalancing', 'current_count': 9, 'baseline_count': 2, 'delta': 7} (+17 more)
  - `grounding.origin_error_count` → 5

## [WARNING] `ontology_planning` / `ungrounded_symbol_count`

- value: **3**  (from `grounding.ungrounded_symbol_count`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → asset_class; assetclass; businessfield (+23 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; asset_class; assetclass (+43 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'security', 'current_count': 8, 'baseline_count': 0, 'delta': 8}; {'token': 'theindex', 'current_count': 8, 'baseline_count': 0, 'delta': 8}; {'token': 'rebalancing', 'current_count': 9, 'baseline_count': 2, 'delta': 7} (+17 more)
  - `grounding.origin_error_count` → 5
