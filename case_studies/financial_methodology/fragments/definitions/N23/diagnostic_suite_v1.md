# Diagnostic report — N23

- **gate**: `needs_review`
- fail: 0, warning: 27

## [WARNING] `merge_canonicalization` / `callable_symbol_count`

- value: **3**  (from `parameterization.callable_symbol_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 3
  - `<related section in metrics JSON>` → 3

## [WARNING] `merge_canonicalization` / `callable_symbol_with_args_count`

- value: **3**  (from `parameterization.callable_symbol_with_args_count`)
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

- value: **3**  (from `parameterization.factorization_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 3
  - `<related section in metrics JSON>` → 3

## [WARNING] `merge_canonicalization` / `focus_signature_unique_count`

- value: **1**  (from `variability.focus_signature_unique_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.

## [WARNING] `merge_canonicalization` / `quantifier_parameter_slot_count`

- value: **1**  (from `parameterization.quantifier_parameter_slot_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `assertion_complexity.top_complex_assertions` → index_universe_definition
  - `assertion_complexity.max_assertion_depth` → 4
  - `assertion_complexity.total_quantifier_count` → 1

## [WARNING] `merge_canonicalization` / `top_level_parameter_slot_count`

- value: **6**  (from `parameterization.top_level_parameter_slot_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 6
  - `<related section in metrics JSON>` → 6

## [WARNING] `merge_canonicalization` / `total_parameter_slot_mass`

- value: **7**  (from `parameterization.total_parameter_slot_mass`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 7
  - `<related section in metrics JSON>` → 7

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
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'index_universe_is_sum_of_financial_instruments_fulfilling_requir; {'identifier': 'financial_instrument_in_index_universe', 'raw_piece_count': 5, '; {'identifier': 'fulfills_index_universe_requirements', 'raw_piece_count': 4, 'co (+7 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'index_universe_definition', 'raw_piece_count': 3, 'content_piece; {'identifier': 'fulfills_index_universe_requirements', 'raw_piece_count': 4, 'co; {'identifier': 'index_universe_is_sum_of_financial_instruments_fulfilling_requir (+6 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `compound_identifier_count_raw`

- value: **4**  (from `identifier_glue.compound_identifier_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'index_universe_is_sum_of_financial_instruments_fulfilling_requir; {'identifier': 'financial_instrument_in_index_universe', 'raw_piece_count': 5, '; {'identifier': 'fulfills_index_universe_requirements', 'raw_piece_count': 4, 'co (+7 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'index_universe_definition', 'raw_piece_count': 3, 'content_piece; {'identifier': 'fulfills_index_universe_requirements', 'raw_piece_count': 4, 'co; {'identifier': 'index_universe_is_sum_of_financial_instruments_fulfilling_requir (+6 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `identifier_count`

- value: **10**  (from `identifier_glue.identifier_count`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'index_universe_is_sum_of_financial_instruments_fulfilling_requir; {'identifier': 'financial_instrument_in_index_universe', 'raw_piece_count': 5, '; {'identifier': 'fulfills_index_universe_requirements', 'raw_piece_count': 4, 'co (+7 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'index_universe_definition', 'raw_piece_count': 3, 'content_piece; {'identifier': 'fulfills_index_universe_requirements', 'raw_piece_count': 4, 'co; {'identifier': 'index_universe_is_sum_of_financial_instruments_fulfilling_requir (+6 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `identifier_glue_excess_mass_content`

- value: **12**  (from `identifier_glue.identifier_glue_excess_mass_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'index_universe_is_sum_of_financial_instruments_fulfilling_requir; {'identifier': 'financial_instrument_in_index_universe', 'raw_piece_count': 5, '; {'identifier': 'fulfills_index_universe_requirements', 'raw_piece_count': 4, 'co (+7 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'index_universe_definition', 'raw_piece_count': 3, 'content_piece; {'identifier': 'fulfills_index_universe_requirements', 'raw_piece_count': 4, 'co; {'identifier': 'index_universe_is_sum_of_financial_instruments_fulfilling_requir (+6 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `identifier_glue_excess_mass_raw`

- value: **10**  (from `identifier_glue.identifier_glue_excess_mass_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'index_universe_is_sum_of_financial_instruments_fulfilling_requir; {'identifier': 'financial_instrument_in_index_universe', 'raw_piece_count': 5, '; {'identifier': 'fulfills_index_universe_requirements', 'raw_piece_count': 4, 'co (+7 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'index_universe_definition', 'raw_piece_count': 3, 'content_piece; {'identifier': 'fulfills_index_universe_requirements', 'raw_piece_count': 4, 'co; {'identifier': 'index_universe_is_sum_of_financial_instruments_fulfilling_requir (+6 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `low_source_grounded_glued_identifier_count`

- value: **1**  (from `identifier_glue.low_source_grounded_glued_identifier_count`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'index_universe_is_sum_of_financial_instruments_fulfilling_requir; {'identifier': 'financial_instrument_in_index_universe', 'raw_piece_count': 5, '; {'identifier': 'fulfills_index_universe_requirements', 'raw_piece_count': 4, 'co (+7 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'index_universe_definition', 'raw_piece_count': 3, 'content_piece; {'identifier': 'fulfills_index_universe_requirements', 'raw_piece_count': 4, 'co; {'identifier': 'index_universe_is_sum_of_financial_instruments_fulfilling_requir (+6 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `max_identifier_piece_count_content`

- value: **7**  (from `identifier_glue.max_identifier_piece_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'index_universe_is_sum_of_financial_instruments_fulfilling_requir; {'identifier': 'financial_instrument_in_index_universe', 'raw_piece_count': 5, '; {'identifier': 'fulfills_index_universe_requirements', 'raw_piece_count': 4, 'co (+7 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'index_universe_definition', 'raw_piece_count': 3, 'content_piece; {'identifier': 'fulfills_index_universe_requirements', 'raw_piece_count': 4, 'co; {'identifier': 'index_universe_is_sum_of_financial_instruments_fulfilling_requir (+6 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `max_identifier_piece_count_raw`

- value: **9**  (from `identifier_glue.max_identifier_piece_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'index_universe_is_sum_of_financial_instruments_fulfilling_requir; {'identifier': 'financial_instrument_in_index_universe', 'raw_piece_count': 5, '; {'identifier': 'fulfills_index_universe_requirements', 'raw_piece_count': 4, 'co (+7 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'index_universe_definition', 'raw_piece_count': 3, 'content_piece; {'identifier': 'fulfills_index_universe_requirements', 'raw_piece_count': 4, 'co; {'identifier': 'index_universe_is_sum_of_financial_instruments_fulfilling_requir (+6 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `mean_identifier_piece_count_content`

- value: **3**  (from `identifier_glue.mean_identifier_piece_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'index_universe_is_sum_of_financial_instruments_fulfilling_requir; {'identifier': 'financial_instrument_in_index_universe', 'raw_piece_count': 5, '; {'identifier': 'fulfills_index_universe_requirements', 'raw_piece_count': 4, 'co (+7 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'index_universe_definition', 'raw_piece_count': 3, 'content_piece; {'identifier': 'fulfills_index_universe_requirements', 'raw_piece_count': 4, 'co; {'identifier': 'index_universe_is_sum_of_financial_instruments_fulfilling_requir (+6 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `mean_identifier_piece_count_raw`

- value: **3.6**  (from `identifier_glue.mean_identifier_piece_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'index_universe_is_sum_of_financial_instruments_fulfilling_requir; {'identifier': 'financial_instrument_in_index_universe', 'raw_piece_count': 5, '; {'identifier': 'fulfills_index_universe_requirements', 'raw_piece_count': 4, 'co (+7 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'index_universe_definition', 'raw_piece_count': 3, 'content_piece; {'identifier': 'fulfills_index_universe_requirements', 'raw_piece_count': 4, 'co; {'identifier': 'index_universe_is_sum_of_financial_instruments_fulfilling_requir (+6 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `new_formula_content_token_count_vs_text_only`

- value: **10**  (from `grounding.new_formula_content_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → financial_instrument_in_index_universe; financialinstrument; fulfills_index_universe_requirements (+7 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; canonical; computation (+27 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'index', 'current_count': 8, 'baseline_count': 2, 'delta': 6}; {'token': 'universe', 'current_count': 8, 'baseline_count': 2, 'delta': 6}; {'token': 'indexuniverse', 'current_count': 4, 'baseline_count': 0, 'delta': 4} (+12 more)
  - `grounding.origin_error_count` → 0

## [WARNING] `ontology_planning` / `new_formula_token_count_vs_text_only`

- value: **11**  (from `grounding.new_formula_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → financial_instrument_in_index_universe; financialinstrument; fulfills_index_universe_requirements (+7 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; canonical; computation (+27 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'index', 'current_count': 8, 'baseline_count': 2, 'delta': 6}; {'token': 'universe', 'current_count': 8, 'baseline_count': 2, 'delta': 6}; {'token': 'indexuniverse', 'current_count': 4, 'baseline_count': 0, 'delta': 4} (+12 more)
  - `grounding.origin_error_count` → 0

## [WARNING] `ontology_planning` / `new_full_surface_content_token_count_vs_text_only`

- value: **30**  (from `grounding.new_full_surface_content_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → financial_instrument_in_index_universe; financialinstrument; fulfills_index_universe_requirements (+7 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; canonical; computation (+27 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'index', 'current_count': 8, 'baseline_count': 2, 'delta': 6}; {'token': 'universe', 'current_count': 8, 'baseline_count': 2, 'delta': 6}; {'token': 'indexuniverse', 'current_count': 4, 'baseline_count': 0, 'delta': 4} (+12 more)
  - `grounding.origin_error_count` → 0

## [WARNING] `ontology_planning` / `new_full_surface_token_count_vs_text_only`

- value: **35**  (from `grounding.new_full_surface_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → financial_instrument_in_index_universe; financialinstrument; fulfills_index_universe_requirements (+7 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; canonical; computation (+27 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'index', 'current_count': 8, 'baseline_count': 2, 'delta': 6}; {'token': 'universe', 'current_count': 8, 'baseline_count': 2, 'delta': 6}; {'token': 'indexuniverse', 'current_count': 4, 'baseline_count': 0, 'delta': 4} (+12 more)
  - `grounding.origin_error_count` → 0

## [WARNING] `ontology_planning` / `new_surface_content_token_count`

- value: **33**  (from `<search recursive metrics JSON for key `new_surface_content_token_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → financial_instrument_in_index_universe; financialinstrument; fulfills_index_universe_requirements (+7 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; canonical; computation (+27 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'index', 'current_count': 8, 'baseline_count': 2, 'delta': 6}; {'token': 'universe', 'current_count': 8, 'baseline_count': 2, 'delta': 6}; {'token': 'indexuniverse', 'current_count': 4, 'baseline_count': 0, 'delta': 4} (+12 more)
  - `grounding.origin_error_count` → 0

## [WARNING] `ontology_planning` / `new_surface_token_count`

- value: **33**  (from `<search recursive metrics JSON for key `new_surface_token_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → financial_instrument_in_index_universe; financialinstrument; fulfills_index_universe_requirements (+7 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; canonical; computation (+27 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'index', 'current_count': 8, 'baseline_count': 2, 'delta': 6}; {'token': 'universe', 'current_count': 8, 'baseline_count': 2, 'delta': 6}; {'token': 'indexuniverse', 'current_count': 4, 'baseline_count': 0, 'delta': 4} (+12 more)
  - `grounding.origin_error_count` → 0
