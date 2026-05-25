# Diagnostic report — N30

- **gate**: `needs_review`
- fail: 0, warning: 34

## [WARNING] `a4v3_semantic_lint` / `shared_name_token_without_structural_carrier_count`

- value: **5**  (from `a4v3_semantic_lint_v1.json::summary.shared_name_token_without_structural_carrier_count`)
- meaning: A semantic link may be encoded only by repeated words inside predicate names, rather than by an explicit shared entity/sort/argument in formula structure.
- repair: Introduce a structural carrier for the repeated concept, e.g. a sort/entity and relation arguments, or document why the repeated token is intentionally only lexical.
- evidence:
  - `a4v3_semantic_lint_v1.json::findings` → {'check': 'shared_name_token_without_structural_carrier', 'severity': 'soft', 'c; {'check': 'shared_name_token_without_structural_carrier', 'severity': 'soft', 'c; {'check': 'shared_name_token_without_structural_carrier', 'severity': 'soft', 'c (+2 more)

## [WARNING] `merge_canonicalization` / `callable_symbol_count`

- value: **32**  (from `parameterization.callable_symbol_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 32
  - `<related section in metrics JSON>` → 32

## [WARNING] `merge_canonicalization` / `callable_symbol_with_args_count`

- value: **32**  (from `parameterization.callable_symbol_with_args_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 32
  - `<related section in metrics JSON>` → 32

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

- value: **32**  (from `parameterization.factorization_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 32
  - `<related section in metrics JSON>` → 32

## [WARNING] `merge_canonicalization` / `focus_signature_unique_count`

- value: **1**  (from `variability.focus_signature_unique_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.

## [WARNING] `merge_canonicalization` / `quantifier_parameter_slot_count`

- value: **34**  (from `parameterization.quantifier_parameter_slot_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `assertion_complexity.top_complex_assertions` → following_calculation_day_component_scope; trading_day_context_definition; early_cessation_exclusion (+7 more)
  - `assertion_complexity.max_assertion_depth` → 9
  - `assertion_complexity.total_quantifier_count` → 34

## [WARNING] `merge_canonicalization` / `top_level_parameter_slot_count`

- value: **54**  (from `parameterization.top_level_parameter_slot_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 54
  - `<related section in metrics JSON>` → 54

## [WARNING] `merge_canonicalization` / `total_parameter_slot_mass`

- value: **88**  (from `parameterization.total_parameter_slot_mass`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 88
  - `<related section in metrics JSON>` → 88

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

- value: **40**  (from `identifier_glue.compound_identifier_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'would_have_been_open_for_trading_without_market_disruption', 'ra; {'identifier': 'context_captures_new_index_component_close_of_trading', 'raw_pie; {'identifier': 'security_to_be_included_in_index_as_new_index_component', 'raw_p (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'early_cessation_exclusion', 'raw_piece_count': 3, 'content_piece; {'identifier': 'cessation_possibility_day', 'raw_piece_count': 3, 'content_piece; {'identifier': 'cessation_possibility_exchange', 'raw_piece_count': 3, 'content_ (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'calculation_day_immediately_following_rebalance_day', 'raw_piece; {'identifier': 'context_component_included_at_following_calculation_day', 'raw_p; {'identifier': 'context_excluded_by_prior_to_close_cessation', 'raw_piece_count' (+2 more)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'calculation_day_immediately_following_rebalance_day', 'raw_piece; {'identifier': 'context_component_included_at_rebalance_day', 'raw_piece_count':; {'identifier': 'context_component_included_at_following_calculation_day', 'raw_p (+8 more)

## [WARNING] `ontology_planning` / `compound_identifier_count_raw`

- value: **26**  (from `identifier_glue.compound_identifier_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'would_have_been_open_for_trading_without_market_disruption', 'ra; {'identifier': 'context_captures_new_index_component_close_of_trading', 'raw_pie; {'identifier': 'security_to_be_included_in_index_as_new_index_component', 'raw_p (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'early_cessation_exclusion', 'raw_piece_count': 3, 'content_piece; {'identifier': 'cessation_possibility_day', 'raw_piece_count': 3, 'content_piece; {'identifier': 'cessation_possibility_exchange', 'raw_piece_count': 3, 'content_ (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'calculation_day_immediately_following_rebalance_day', 'raw_piece; {'identifier': 'context_component_included_at_following_calculation_day', 'raw_p; {'identifier': 'context_excluded_by_prior_to_close_cessation', 'raw_piece_count' (+2 more)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'calculation_day_immediately_following_rebalance_day', 'raw_piece; {'identifier': 'context_component_included_at_rebalance_day', 'raw_piece_count':; {'identifier': 'context_component_included_at_following_calculation_day', 'raw_p (+8 more)

## [WARNING] `ontology_planning` / `dependency_link_count`

- value: **2**  (from `<search recursive metrics JSON for key `dependency_link_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 2
  - `<related section in metrics JSON>` → 2

## [WARNING] `ontology_planning` / `identifier_count`

- value: **71**  (from `identifier_glue.identifier_count`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'would_have_been_open_for_trading_without_market_disruption', 'ra; {'identifier': 'context_captures_new_index_component_close_of_trading', 'raw_pie; {'identifier': 'security_to_be_included_in_index_as_new_index_component', 'raw_p (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'early_cessation_exclusion', 'raw_piece_count': 3, 'content_piece; {'identifier': 'cessation_possibility_day', 'raw_piece_count': 3, 'content_piece; {'identifier': 'cessation_possibility_exchange', 'raw_piece_count': 3, 'content_ (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'calculation_day_immediately_following_rebalance_day', 'raw_piece; {'identifier': 'context_component_included_at_following_calculation_day', 'raw_p; {'identifier': 'context_excluded_by_prior_to_close_cessation', 'raw_piece_count' (+2 more)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'calculation_day_immediately_following_rebalance_day', 'raw_piece; {'identifier': 'context_component_included_at_rebalance_day', 'raw_piece_count':; {'identifier': 'context_component_included_at_following_calculation_day', 'raw_p (+8 more)

## [WARNING] `ontology_planning` / `identifier_glue_excess_mass_content`

- value: **86**  (from `identifier_glue.identifier_glue_excess_mass_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'would_have_been_open_for_trading_without_market_disruption', 'ra; {'identifier': 'context_captures_new_index_component_close_of_trading', 'raw_pie; {'identifier': 'security_to_be_included_in_index_as_new_index_component', 'raw_p (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'early_cessation_exclusion', 'raw_piece_count': 3, 'content_piece; {'identifier': 'cessation_possibility_day', 'raw_piece_count': 3, 'content_piece; {'identifier': 'cessation_possibility_exchange', 'raw_piece_count': 3, 'content_ (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'calculation_day_immediately_following_rebalance_day', 'raw_piece; {'identifier': 'context_component_included_at_following_calculation_day', 'raw_p; {'identifier': 'context_excluded_by_prior_to_close_cessation', 'raw_piece_count' (+2 more)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'calculation_day_immediately_following_rebalance_day', 'raw_piece; {'identifier': 'context_component_included_at_rebalance_day', 'raw_piece_count':; {'identifier': 'context_component_included_at_following_calculation_day', 'raw_p (+8 more)

## [WARNING] `ontology_planning` / `identifier_glue_excess_mass_raw`

- value: **70**  (from `identifier_glue.identifier_glue_excess_mass_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'would_have_been_open_for_trading_without_market_disruption', 'ra; {'identifier': 'context_captures_new_index_component_close_of_trading', 'raw_pie; {'identifier': 'security_to_be_included_in_index_as_new_index_component', 'raw_p (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'early_cessation_exclusion', 'raw_piece_count': 3, 'content_piece; {'identifier': 'cessation_possibility_day', 'raw_piece_count': 3, 'content_piece; {'identifier': 'cessation_possibility_exchange', 'raw_piece_count': 3, 'content_ (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'calculation_day_immediately_following_rebalance_day', 'raw_piece; {'identifier': 'context_component_included_at_following_calculation_day', 'raw_p; {'identifier': 'context_excluded_by_prior_to_close_cessation', 'raw_piece_count' (+2 more)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'calculation_day_immediately_following_rebalance_day', 'raw_piece; {'identifier': 'context_component_included_at_rebalance_day', 'raw_piece_count':; {'identifier': 'context_component_included_at_following_calculation_day', 'raw_p (+8 more)

## [WARNING] `ontology_planning` / `invented_helper_sort_count`

- value: **1**  (from `<search recursive metrics JSON for key `invented_helper_sort_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → calculation_day_immediately_following_rebalance_day; calculationday; cessation_possibility_day (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; calculation_day_immediately_following_rebalance_day; calculationday (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'context', 'current_count': 49, 'baseline_count': 0, 'delta': 49}; {'token': 'exchange', 'current_count': 33, 'baseline_count': 4, 'delta': 29}; {'token': 'tradingdaycontext', 'current_count': 25, 'baseline_count': 0, 'delta' (+17 more)
  - `grounding.origin_error_count` → 20
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'would_have_been_open_for_trading_without_market_disruption', 'ra; {'identifier': 'context_captures_new_index_component_close_of_trading', 'raw_pie; {'identifier': 'security_to_be_included_in_index_as_new_index_component', 'raw_p (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'early_cessation_exclusion', 'raw_piece_count': 3, 'content_piece; {'identifier': 'cessation_possibility_day', 'raw_piece_count': 3, 'content_piece; {'identifier': 'cessation_possibility_exchange', 'raw_piece_count': 3, 'content_ (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'calculation_day_immediately_following_rebalance_day', 'raw_piece; {'identifier': 'context_component_included_at_following_calculation_day', 'raw_p; {'identifier': 'context_excluded_by_prior_to_close_cessation', 'raw_piece_count' (+2 more)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'calculation_day_immediately_following_rebalance_day', 'raw_piece; {'identifier': 'context_component_included_at_rebalance_day', 'raw_piece_count':; {'identifier': 'context_component_included_at_following_calculation_day', 'raw_p (+8 more)
  - `evidence.invented_helper_sorts` → Security

## [WARNING] `ontology_planning` / `invented_helper_symbol_count`

- value: **1**  (from `<search recursive metrics JSON for key `invented_helper_symbol_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → calculation_day_immediately_following_rebalance_day; calculationday; cessation_possibility_day (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; calculation_day_immediately_following_rebalance_day; calculationday (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'context', 'current_count': 49, 'baseline_count': 0, 'delta': 49}; {'token': 'exchange', 'current_count': 33, 'baseline_count': 4, 'delta': 29}; {'token': 'tradingdaycontext', 'current_count': 25, 'baseline_count': 0, 'delta' (+17 more)
  - `grounding.origin_error_count` → 20
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'would_have_been_open_for_trading_without_market_disruption', 'ra; {'identifier': 'context_captures_new_index_component_close_of_trading', 'raw_pie; {'identifier': 'security_to_be_included_in_index_as_new_index_component', 'raw_p (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'early_cessation_exclusion', 'raw_piece_count': 3, 'content_piece; {'identifier': 'cessation_possibility_day', 'raw_piece_count': 3, 'content_piece; {'identifier': 'cessation_possibility_exchange', 'raw_piece_count': 3, 'content_ (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'calculation_day_immediately_following_rebalance_day', 'raw_piece; {'identifier': 'context_component_included_at_following_calculation_day', 'raw_p; {'identifier': 'context_excluded_by_prior_to_close_cessation', 'raw_piece_count' (+2 more)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'calculation_day_immediately_following_rebalance_day', 'raw_piece; {'identifier': 'context_component_included_at_rebalance_day', 'raw_piece_count':; {'identifier': 'context_component_included_at_following_calculation_day', 'raw_p (+8 more)
  - `evidence.invented_helper_sorts` → Security

## [WARNING] `ontology_planning` / `low_source_grounded_glued_identifier_count`

- value: **19**  (from `identifier_glue.low_source_grounded_glued_identifier_count`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'would_have_been_open_for_trading_without_market_disruption', 'ra; {'identifier': 'context_captures_new_index_component_close_of_trading', 'raw_pie; {'identifier': 'security_to_be_included_in_index_as_new_index_component', 'raw_p (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'early_cessation_exclusion', 'raw_piece_count': 3, 'content_piece; {'identifier': 'cessation_possibility_day', 'raw_piece_count': 3, 'content_piece; {'identifier': 'cessation_possibility_exchange', 'raw_piece_count': 3, 'content_ (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'calculation_day_immediately_following_rebalance_day', 'raw_piece; {'identifier': 'context_component_included_at_following_calculation_day', 'raw_p; {'identifier': 'context_excluded_by_prior_to_close_cessation', 'raw_piece_count' (+2 more)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'calculation_day_immediately_following_rebalance_day', 'raw_piece; {'identifier': 'context_component_included_at_rebalance_day', 'raw_piece_count':; {'identifier': 'context_component_included_at_following_calculation_day', 'raw_p (+8 more)

## [WARNING] `ontology_planning` / `max_identifier_piece_count_content`

- value: **8**  (from `identifier_glue.max_identifier_piece_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'would_have_been_open_for_trading_without_market_disruption', 'ra; {'identifier': 'context_captures_new_index_component_close_of_trading', 'raw_pie; {'identifier': 'security_to_be_included_in_index_as_new_index_component', 'raw_p (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'early_cessation_exclusion', 'raw_piece_count': 3, 'content_piece; {'identifier': 'cessation_possibility_day', 'raw_piece_count': 3, 'content_piece; {'identifier': 'cessation_possibility_exchange', 'raw_piece_count': 3, 'content_ (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'calculation_day_immediately_following_rebalance_day', 'raw_piece; {'identifier': 'context_component_included_at_following_calculation_day', 'raw_p; {'identifier': 'context_excluded_by_prior_to_close_cessation', 'raw_piece_count' (+2 more)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'calculation_day_immediately_following_rebalance_day', 'raw_piece; {'identifier': 'context_component_included_at_rebalance_day', 'raw_piece_count':; {'identifier': 'context_component_included_at_following_calculation_day', 'raw_p (+8 more)

## [WARNING] `ontology_planning` / `max_identifier_piece_count_raw`

- value: **10**  (from `identifier_glue.max_identifier_piece_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'would_have_been_open_for_trading_without_market_disruption', 'ra; {'identifier': 'context_captures_new_index_component_close_of_trading', 'raw_pie; {'identifier': 'security_to_be_included_in_index_as_new_index_component', 'raw_p (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'early_cessation_exclusion', 'raw_piece_count': 3, 'content_piece; {'identifier': 'cessation_possibility_day', 'raw_piece_count': 3, 'content_piece; {'identifier': 'cessation_possibility_exchange', 'raw_piece_count': 3, 'content_ (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'calculation_day_immediately_following_rebalance_day', 'raw_piece; {'identifier': 'context_component_included_at_following_calculation_day', 'raw_p; {'identifier': 'context_excluded_by_prior_to_close_cessation', 'raw_piece_count' (+2 more)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'calculation_day_immediately_following_rebalance_day', 'raw_piece; {'identifier': 'context_component_included_at_rebalance_day', 'raw_piece_count':; {'identifier': 'context_component_included_at_following_calculation_day', 'raw_p (+8 more)

## [WARNING] `ontology_planning` / `mean_identifier_piece_count_content`

- value: **2.8732394366197185**  (from `identifier_glue.mean_identifier_piece_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'would_have_been_open_for_trading_without_market_disruption', 'ra; {'identifier': 'context_captures_new_index_component_close_of_trading', 'raw_pie; {'identifier': 'security_to_be_included_in_index_as_new_index_component', 'raw_p (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'early_cessation_exclusion', 'raw_piece_count': 3, 'content_piece; {'identifier': 'cessation_possibility_day', 'raw_piece_count': 3, 'content_piece; {'identifier': 'cessation_possibility_exchange', 'raw_piece_count': 3, 'content_ (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'calculation_day_immediately_following_rebalance_day', 'raw_piece; {'identifier': 'context_component_included_at_following_calculation_day', 'raw_p; {'identifier': 'context_excluded_by_prior_to_close_cessation', 'raw_piece_count' (+2 more)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'calculation_day_immediately_following_rebalance_day', 'raw_piece; {'identifier': 'context_component_included_at_rebalance_day', 'raw_piece_count':; {'identifier': 'context_component_included_at_following_calculation_day', 'raw_p (+8 more)

## [WARNING] `ontology_planning` / `mean_identifier_piece_count_raw`

- value: **3.3661971830985915**  (from `identifier_glue.mean_identifier_piece_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'would_have_been_open_for_trading_without_market_disruption', 'ra; {'identifier': 'context_captures_new_index_component_close_of_trading', 'raw_pie; {'identifier': 'security_to_be_included_in_index_as_new_index_component', 'raw_p (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'early_cessation_exclusion', 'raw_piece_count': 3, 'content_piece; {'identifier': 'cessation_possibility_day', 'raw_piece_count': 3, 'content_piece; {'identifier': 'cessation_possibility_exchange', 'raw_piece_count': 3, 'content_ (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → {'identifier': 'calculation_day_immediately_following_rebalance_day', 'raw_piece; {'identifier': 'context_component_included_at_following_calculation_day', 'raw_p; {'identifier': 'context_excluded_by_prior_to_close_cessation', 'raw_piece_count' (+2 more)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'calculation_day_immediately_following_rebalance_day', 'raw_piece; {'identifier': 'context_component_included_at_rebalance_day', 'raw_piece_count':; {'identifier': 'context_component_included_at_following_calculation_day', 'raw_p (+8 more)

## [WARNING] `ontology_planning` / `new_formula_content_token_count_vs_text_only`

- value: **60**  (from `grounding.new_formula_content_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → calculation_day_immediately_following_rebalance_day; calculationday; cessation_possibility_day (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; calculation_day_immediately_following_rebalance_day; calculationday (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'context', 'current_count': 49, 'baseline_count': 0, 'delta': 49}; {'token': 'exchange', 'current_count': 33, 'baseline_count': 4, 'delta': 29}; {'token': 'tradingdaycontext', 'current_count': 25, 'baseline_count': 0, 'delta' (+17 more)
  - `grounding.origin_error_count` → 20

## [WARNING] `ontology_planning` / `new_formula_token_count_vs_text_only`

- value: **70**  (from `grounding.new_formula_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → calculation_day_immediately_following_rebalance_day; calculationday; cessation_possibility_day (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; calculation_day_immediately_following_rebalance_day; calculationday (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'context', 'current_count': 49, 'baseline_count': 0, 'delta': 49}; {'token': 'exchange', 'current_count': 33, 'baseline_count': 4, 'delta': 29}; {'token': 'tradingdaycontext', 'current_count': 25, 'baseline_count': 0, 'delta' (+17 more)
  - `grounding.origin_error_count` → 20

## [WARNING] `ontology_planning` / `new_full_surface_content_token_count_vs_text_only`

- value: **80**  (from `grounding.new_full_surface_content_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → calculation_day_immediately_following_rebalance_day; calculationday; cessation_possibility_day (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; calculation_day_immediately_following_rebalance_day; calculationday (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'context', 'current_count': 49, 'baseline_count': 0, 'delta': 49}; {'token': 'exchange', 'current_count': 33, 'baseline_count': 4, 'delta': 29}; {'token': 'tradingdaycontext', 'current_count': 25, 'baseline_count': 0, 'delta' (+17 more)
  - `grounding.origin_error_count` → 20

## [WARNING] `ontology_planning` / `new_full_surface_token_count_vs_text_only`

- value: **93**  (from `grounding.new_full_surface_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → calculation_day_immediately_following_rebalance_day; calculationday; cessation_possibility_day (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; calculation_day_immediately_following_rebalance_day; calculationday (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'context', 'current_count': 49, 'baseline_count': 0, 'delta': 49}; {'token': 'exchange', 'current_count': 33, 'baseline_count': 4, 'delta': 29}; {'token': 'tradingdaycontext', 'current_count': 25, 'baseline_count': 0, 'delta' (+17 more)
  - `grounding.origin_error_count` → 20

## [WARNING] `ontology_planning` / `new_surface_content_token_count`

- value: **198**  (from `<search recursive metrics JSON for key `new_surface_content_token_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → calculation_day_immediately_following_rebalance_day; calculationday; cessation_possibility_day (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; calculation_day_immediately_following_rebalance_day; calculationday (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'context', 'current_count': 49, 'baseline_count': 0, 'delta': 49}; {'token': 'exchange', 'current_count': 33, 'baseline_count': 4, 'delta': 29}; {'token': 'tradingdaycontext', 'current_count': 25, 'baseline_count': 0, 'delta' (+17 more)
  - `grounding.origin_error_count` → 20

## [WARNING] `ontology_planning` / `new_surface_token_count`

- value: **198**  (from `<search recursive metrics JSON for key `new_surface_token_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → calculation_day_immediately_following_rebalance_day; calculationday; cessation_possibility_day (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; calculation_day_immediately_following_rebalance_day; calculationday (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'context', 'current_count': 49, 'baseline_count': 0, 'delta': 49}; {'token': 'exchange', 'current_count': 33, 'baseline_count': 4, 'delta': 29}; {'token': 'tradingdaycontext', 'current_count': 25, 'baseline_count': 0, 'delta' (+17 more)
  - `grounding.origin_error_count` → 20

## [WARNING] `ontology_planning` / `ungrounded_sort_count`

- value: **3**  (from `grounding.ungrounded_sort_count`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → calculation_day_immediately_following_rebalance_day; calculationday; cessation_possibility_day (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; calculation_day_immediately_following_rebalance_day; calculationday (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'context', 'current_count': 49, 'baseline_count': 0, 'delta': 49}; {'token': 'exchange', 'current_count': 33, 'baseline_count': 4, 'delta': 29}; {'token': 'tradingdaycontext', 'current_count': 25, 'baseline_count': 0, 'delta' (+17 more)
  - `grounding.origin_error_count` → 20

## [WARNING] `ontology_planning` / `ungrounded_symbol_count`

- value: **17**  (from `grounding.ungrounded_symbol_count`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → calculation_day_immediately_following_rebalance_day; calculationday; cessation_possibility_day (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; calculation_day_immediately_following_rebalance_day; calculationday (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'context', 'current_count': 49, 'baseline_count': 0, 'delta': 49}; {'token': 'exchange', 'current_count': 33, 'baseline_count': 4, 'delta': 29}; {'token': 'tradingdaycontext', 'current_count': 25, 'baseline_count': 0, 'delta' (+17 more)
  - `grounding.origin_error_count` → 20

## [ERROR_NO_VALUE] `merge_canonicalization` / `llm_bertscore`

- value: **None**  (from `None`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `render_back.render_back_text` → A trading day context is valid when it identifies a rebalance day, a day, and an index component, and the context exchange is the component’s relevant exchange, and either the component was included in The Index on that rebalance day or, if the day immediately follows that rebalance day, the component was included in The Index on that calculation day.  

A valid trading day context is a trading day when the context identifies a day, an index component, and an exchange, the exchange is the component’s relevant exchange, and the exchange was open for trading on that day, or a market disruption occurred on that day and the exchange would have been open for trading without the disruption, and there was no trading cessation possibility for that exchange and day prior to the scheduled exchange closing time, and no scheduled shortened period for that exchange and day.  

A context captures new index component close of trading when it identifies a rebalance day and an index component that is to be included in The Index as a new index component, and the close of trading is for that component’s relevant exchange on that rebalance day.  

The Index Administrator is ultimately responsible for any determination that decides whether a valid trading day context is a trading day.
  - `render_back.render_nli_text_implies_ir` → 0.9133610129356384
  - `render_back.render_nli_ir_implies_text` → 0.6745283007621765
  - `render_back.render_contradiction_score` → 0.09063196182250977

## [ERROR_NO_VALUE] `merge_canonicalization` / `llm_contradiction`

- value: **None**  (from `None`)
- meaning: Rendered IR does not preserve entailment/equivalence; report render text and entailment/contradiction values.
- repair: Repair IR until render-back and entailment preserve normalized meaning.
- evidence:
  - `render_back.render_back_text` → A trading day context is valid when it identifies a rebalance day, a day, and an index component, and the context exchange is the component’s relevant exchange, and either the component was included in The Index on that rebalance day or, if the day immediately follows that rebalance day, the component was included in The Index on that calculation day.  

A valid trading day context is a trading day when the context identifies a day, an index component, and an exchange, the exchange is the component’s relevant exchange, and the exchange was open for trading on that day, or a market disruption occurred on that day and the exchange would have been open for trading without the disruption, and there was no trading cessation possibility for that exchange and day prior to the scheduled exchange closing time, and no scheduled shortened period for that exchange and day.  

A context captures new index component close of trading when it identifies a rebalance day and an index component that is to be included in The Index as a new index component, and the close of trading is for that component’s relevant exchange on that rebalance day.  

The Index Administrator is ultimately responsible for any determination that decides whether a valid trading day context is a trading day.
  - `render_back.render_nli_text_implies_ir` → 0.9133610129356384
  - `render_back.render_nli_ir_implies_text` → 0.6745283007621765
  - `render_back.render_contradiction_score` → 0.09063196182250977

## [ERROR_NO_VALUE] `merge_canonicalization` / `llm_ir_to_text`

- value: **None**  (from `None`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.

## [ERROR_NO_VALUE] `merge_canonicalization` / `llm_text_to_ir`

- value: **None**  (from `None`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
