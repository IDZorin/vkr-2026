# Diagnostic report — N09

- **gate**: `needs_review`
- fail: 0, warning: 26

## [WARNING] `merge_canonicalization` / `callable_symbol_count`

- value: **2**  (from `parameterization.callable_symbol_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 2
  - `<related section in metrics JSON>` → 2

## [WARNING] `merge_canonicalization` / `callable_symbol_with_args_count`

- value: **2**  (from `parameterization.callable_symbol_with_args_count`)
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

- value: **2**  (from `parameterization.factorization_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 2
  - `<related section in metrics JSON>` → 2

## [WARNING] `merge_canonicalization` / `focus_signature_unique_count`

- value: **1**  (from `variability.focus_signature_unique_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.

## [WARNING] `merge_canonicalization` / `quantifier_parameter_slot_count`

- value: **1**  (from `parameterization.quantifier_parameter_slot_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `assertion_complexity.top_complex_assertions` → eligible_rebalance_day_definition
  - `assertion_complexity.max_assertion_depth` → 5
  - `assertion_complexity.total_quantifier_count` → 1

## [WARNING] `merge_canonicalization` / `top_level_parameter_slot_count`

- value: **3**  (from `parameterization.top_level_parameter_slot_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 3
  - `<related section in metrics JSON>` → 3

## [WARNING] `merge_canonicalization` / `total_parameter_slot_mass`

- value: **4**  (from `parameterization.total_parameter_slot_mass`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 4
  - `<related section in metrics JSON>` → 4

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

- value: **6**  (from `identifier_glue.compound_identifier_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'eligible_rebalance_day_definition', 'raw_piece_count': 4, 'conte; {'identifier': 'NewYorkStockExchange', 'raw_piece_count': 4, 'content_piece_coun; {'identifier': 'trading_day_at_exchange', 'raw_piece_count': 4, 'content_piece_c (+7 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'eligible_rebalance_day_definition', 'raw_piece_count': 4, 'conte; {'identifier': 'NewYorkStockExchange', 'raw_piece_count': 4, 'content_piece_coun; {'identifier': 'EligibleRebalanceDay', 'raw_piece_count': 3, 'content_piece_coun (+3 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `compound_identifier_count_raw`

- value: **3**  (from `identifier_glue.compound_identifier_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'eligible_rebalance_day_definition', 'raw_piece_count': 4, 'conte; {'identifier': 'NewYorkStockExchange', 'raw_piece_count': 4, 'content_piece_coun; {'identifier': 'trading_day_at_exchange', 'raw_piece_count': 4, 'content_piece_c (+7 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'eligible_rebalance_day_definition', 'raw_piece_count': 4, 'conte; {'identifier': 'NewYorkStockExchange', 'raw_piece_count': 4, 'content_piece_coun; {'identifier': 'EligibleRebalanceDay', 'raw_piece_count': 3, 'content_piece_coun (+3 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `identifier_count`

- value: **10**  (from `identifier_glue.identifier_count`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'eligible_rebalance_day_definition', 'raw_piece_count': 4, 'conte; {'identifier': 'NewYorkStockExchange', 'raw_piece_count': 4, 'content_piece_coun; {'identifier': 'trading_day_at_exchange', 'raw_piece_count': 4, 'content_piece_c (+7 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'eligible_rebalance_day_definition', 'raw_piece_count': 4, 'conte; {'identifier': 'NewYorkStockExchange', 'raw_piece_count': 4, 'content_piece_coun; {'identifier': 'EligibleRebalanceDay', 'raw_piece_count': 3, 'content_piece_coun (+3 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `identifier_glue_excess_mass_content`

- value: **8**  (from `identifier_glue.identifier_glue_excess_mass_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'eligible_rebalance_day_definition', 'raw_piece_count': 4, 'conte; {'identifier': 'NewYorkStockExchange', 'raw_piece_count': 4, 'content_piece_coun; {'identifier': 'trading_day_at_exchange', 'raw_piece_count': 4, 'content_piece_c (+7 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'eligible_rebalance_day_definition', 'raw_piece_count': 4, 'conte; {'identifier': 'NewYorkStockExchange', 'raw_piece_count': 4, 'content_piece_coun; {'identifier': 'EligibleRebalanceDay', 'raw_piece_count': 3, 'content_piece_coun (+3 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `identifier_glue_excess_mass_raw`

- value: **3**  (from `identifier_glue.identifier_glue_excess_mass_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'eligible_rebalance_day_definition', 'raw_piece_count': 4, 'conte; {'identifier': 'NewYorkStockExchange', 'raw_piece_count': 4, 'content_piece_coun; {'identifier': 'trading_day_at_exchange', 'raw_piece_count': 4, 'content_piece_c (+7 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'eligible_rebalance_day_definition', 'raw_piece_count': 4, 'conte; {'identifier': 'NewYorkStockExchange', 'raw_piece_count': 4, 'content_piece_coun; {'identifier': 'EligibleRebalanceDay', 'raw_piece_count': 3, 'content_piece_coun (+3 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `max_identifier_piece_count_content`

- value: **4**  (from `identifier_glue.max_identifier_piece_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'eligible_rebalance_day_definition', 'raw_piece_count': 4, 'conte; {'identifier': 'NewYorkStockExchange', 'raw_piece_count': 4, 'content_piece_coun; {'identifier': 'trading_day_at_exchange', 'raw_piece_count': 4, 'content_piece_c (+7 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'eligible_rebalance_day_definition', 'raw_piece_count': 4, 'conte; {'identifier': 'NewYorkStockExchange', 'raw_piece_count': 4, 'content_piece_coun; {'identifier': 'EligibleRebalanceDay', 'raw_piece_count': 3, 'content_piece_coun (+3 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `max_identifier_piece_count_raw`

- value: **4**  (from `identifier_glue.max_identifier_piece_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'eligible_rebalance_day_definition', 'raw_piece_count': 4, 'conte; {'identifier': 'NewYorkStockExchange', 'raw_piece_count': 4, 'content_piece_coun; {'identifier': 'trading_day_at_exchange', 'raw_piece_count': 4, 'content_piece_c (+7 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'eligible_rebalance_day_definition', 'raw_piece_count': 4, 'conte; {'identifier': 'NewYorkStockExchange', 'raw_piece_count': 4, 'content_piece_coun; {'identifier': 'EligibleRebalanceDay', 'raw_piece_count': 3, 'content_piece_coun (+3 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `mean_identifier_piece_count_content`

- value: **2.3**  (from `identifier_glue.mean_identifier_piece_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'eligible_rebalance_day_definition', 'raw_piece_count': 4, 'conte; {'identifier': 'NewYorkStockExchange', 'raw_piece_count': 4, 'content_piece_coun; {'identifier': 'trading_day_at_exchange', 'raw_piece_count': 4, 'content_piece_c (+7 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'eligible_rebalance_day_definition', 'raw_piece_count': 4, 'conte; {'identifier': 'NewYorkStockExchange', 'raw_piece_count': 4, 'content_piece_coun; {'identifier': 'EligibleRebalanceDay', 'raw_piece_count': 3, 'content_piece_coun (+3 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `mean_identifier_piece_count_raw`

- value: **2.5**  (from `identifier_glue.mean_identifier_piece_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'eligible_rebalance_day_definition', 'raw_piece_count': 4, 'conte; {'identifier': 'NewYorkStockExchange', 'raw_piece_count': 4, 'content_piece_coun; {'identifier': 'trading_day_at_exchange', 'raw_piece_count': 4, 'content_piece_c (+7 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'eligible_rebalance_day_definition', 'raw_piece_count': 4, 'conte; {'identifier': 'NewYorkStockExchange', 'raw_piece_count': 4, 'content_piece_coun; {'identifier': 'EligibleRebalanceDay', 'raw_piece_count': 3, 'content_piece_coun (+3 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `new_formula_content_token_count_vs_text_only`

- value: **8**  (from `grounding.new_formula_content_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → eligible_rebalance_day; eligible_rebalance_day_definition; eligiblerebalanceday (+5 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; canonical; computation (+25 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'exchange', 'current_count': 11, 'baseline_count': 4, 'delta': 7}; {'token': 'trading', 'current_count': 5, 'baseline_count': 1, 'delta': 4}; {'token': 'eligiblerebalanceday', 'current_count': 3, 'baseline_count': 0, 'delt (+7 more)
  - `grounding.origin_error_count` → 0

## [WARNING] `ontology_planning` / `new_formula_token_count_vs_text_only`

- value: **9**  (from `grounding.new_formula_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → eligible_rebalance_day; eligible_rebalance_day_definition; eligiblerebalanceday (+5 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; canonical; computation (+25 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'exchange', 'current_count': 11, 'baseline_count': 4, 'delta': 7}; {'token': 'trading', 'current_count': 5, 'baseline_count': 1, 'delta': 4}; {'token': 'eligiblerebalanceday', 'current_count': 3, 'baseline_count': 0, 'delt (+7 more)
  - `grounding.origin_error_count` → 0

## [WARNING] `ontology_planning` / `new_full_surface_content_token_count_vs_text_only`

- value: **28**  (from `grounding.new_full_surface_content_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → eligible_rebalance_day; eligible_rebalance_day_definition; eligiblerebalanceday (+5 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; canonical; computation (+25 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'exchange', 'current_count': 11, 'baseline_count': 4, 'delta': 7}; {'token': 'trading', 'current_count': 5, 'baseline_count': 1, 'delta': 4}; {'token': 'eligiblerebalanceday', 'current_count': 3, 'baseline_count': 0, 'delt (+7 more)
  - `grounding.origin_error_count` → 0

## [WARNING] `ontology_planning` / `new_full_surface_token_count_vs_text_only`

- value: **33**  (from `grounding.new_full_surface_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → eligible_rebalance_day; eligible_rebalance_day_definition; eligiblerebalanceday (+5 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; canonical; computation (+25 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'exchange', 'current_count': 11, 'baseline_count': 4, 'delta': 7}; {'token': 'trading', 'current_count': 5, 'baseline_count': 1, 'delta': 4}; {'token': 'eligiblerebalanceday', 'current_count': 3, 'baseline_count': 0, 'delt (+7 more)
  - `grounding.origin_error_count` → 0

## [WARNING] `ontology_planning` / `new_surface_content_token_count`

- value: **25**  (from `<search recursive metrics JSON for key `new_surface_content_token_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → eligible_rebalance_day; eligible_rebalance_day_definition; eligiblerebalanceday (+5 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; canonical; computation (+25 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'exchange', 'current_count': 11, 'baseline_count': 4, 'delta': 7}; {'token': 'trading', 'current_count': 5, 'baseline_count': 1, 'delta': 4}; {'token': 'eligiblerebalanceday', 'current_count': 3, 'baseline_count': 0, 'delt (+7 more)
  - `grounding.origin_error_count` → 0

## [WARNING] `ontology_planning` / `new_surface_token_count`

- value: **25**  (from `<search recursive metrics JSON for key `new_surface_token_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → eligible_rebalance_day; eligible_rebalance_day_definition; eligiblerebalanceday (+5 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; canonical; computation (+25 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'exchange', 'current_count': 11, 'baseline_count': 4, 'delta': 7}; {'token': 'trading', 'current_count': 5, 'baseline_count': 1, 'delta': 4}; {'token': 'eligiblerebalanceday', 'current_count': 3, 'baseline_count': 0, 'delt (+7 more)
  - `grounding.origin_error_count` → 0
