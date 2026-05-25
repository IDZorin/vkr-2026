# Diagnostic report — N31

- **gate**: `needs_review`
- fail: 0, warning: 31

## [WARNING] `merge_canonicalization` / `callable_symbol_count`

- value: **9**  (from `parameterization.callable_symbol_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 9
  - `<related section in metrics JSON>` → 9

## [WARNING] `merge_canonicalization` / `callable_symbol_with_args_count`

- value: **9**  (from `parameterization.callable_symbol_with_args_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 9
  - `<related section in metrics JSON>` → 9

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

- value: **9**  (from `parameterization.factorization_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 9
  - `<related section in metrics JSON>` → 9

## [WARNING] `merge_canonicalization` / `focus_signature_unique_count`

- value: **1**  (from `variability.focus_signature_unique_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.

## [WARNING] `merge_canonicalization` / `quantifier_parameter_slot_count`

- value: **14**  (from `parameterization.quantifier_parameter_slot_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `assertion_complexity.top_complex_assertions` → most_recent_published_trade_temporal_ordering; most_recent_published_trade_scope; most_recent_published_trade_uniqueness (+1 more)
  - `assertion_complexity.max_assertion_depth` → 9
  - `assertion_complexity.total_quantifier_count` → 14

## [WARNING] `merge_canonicalization` / `top_level_parameter_slot_count`

- value: **15**  (from `parameterization.top_level_parameter_slot_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 15
  - `<related section in metrics JSON>` → 15

## [WARNING] `merge_canonicalization` / `total_parameter_slot_mass`

- value: **29**  (from `parameterization.total_parameter_slot_mass`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 29
  - `<related section in metrics JSON>` → 29

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

- value: **5**  (from `identifier_glue.compound_identifier_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'most_recent_published_trade_temporal_ordering', 'raw_piece_count; {'identifier': 'most_recent_published_trade_uniqueness', 'raw_piece_count': 5, '; {'identifier': 'most_recent_published_trade_for', 'raw_piece_count': 5, 'content (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'TradeTime', 'raw_piece_count': 2, 'content_piece_count': 2, 'raw; {'identifier': 'most_recent_published_trade_temporal_ordering', 'raw_piece_count; {'identifier': 'published_trade', 'raw_piece_count': 2, 'content_piece_count': 2 (+12 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `compound_identifier_count_raw`

- value: **4**  (from `identifier_glue.compound_identifier_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'most_recent_published_trade_temporal_ordering', 'raw_piece_count; {'identifier': 'most_recent_published_trade_uniqueness', 'raw_piece_count': 5, '; {'identifier': 'most_recent_published_trade_for', 'raw_piece_count': 5, 'content (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'TradeTime', 'raw_piece_count': 2, 'content_piece_count': 2, 'raw; {'identifier': 'most_recent_published_trade_temporal_ordering', 'raw_piece_count; {'identifier': 'published_trade', 'raw_piece_count': 2, 'content_piece_count': 2 (+12 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `dependency_link_count`

- value: **3**  (from `<search recursive metrics JSON for key `dependency_link_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 3
  - `<related section in metrics JSON>` → 3

## [WARNING] `ontology_planning` / `identifier_count`

- value: **24**  (from `identifier_glue.identifier_count`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'most_recent_published_trade_temporal_ordering', 'raw_piece_count; {'identifier': 'most_recent_published_trade_uniqueness', 'raw_piece_count': 5, '; {'identifier': 'most_recent_published_trade_for', 'raw_piece_count': 5, 'content (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'TradeTime', 'raw_piece_count': 2, 'content_piece_count': 2, 'raw; {'identifier': 'most_recent_published_trade_temporal_ordering', 'raw_piece_count; {'identifier': 'published_trade', 'raw_piece_count': 2, 'content_piece_count': 2 (+12 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `identifier_glue_excess_mass_content`

- value: **12**  (from `identifier_glue.identifier_glue_excess_mass_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'most_recent_published_trade_temporal_ordering', 'raw_piece_count; {'identifier': 'most_recent_published_trade_uniqueness', 'raw_piece_count': 5, '; {'identifier': 'most_recent_published_trade_for', 'raw_piece_count': 5, 'content (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'TradeTime', 'raw_piece_count': 2, 'content_piece_count': 2, 'raw; {'identifier': 'most_recent_published_trade_temporal_ordering', 'raw_piece_count; {'identifier': 'published_trade', 'raw_piece_count': 2, 'content_piece_count': 2 (+12 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `identifier_glue_excess_mass_raw`

- value: **9**  (from `identifier_glue.identifier_glue_excess_mass_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'most_recent_published_trade_temporal_ordering', 'raw_piece_count; {'identifier': 'most_recent_published_trade_uniqueness', 'raw_piece_count': 5, '; {'identifier': 'most_recent_published_trade_for', 'raw_piece_count': 5, 'content (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'TradeTime', 'raw_piece_count': 2, 'content_piece_count': 2, 'raw; {'identifier': 'most_recent_published_trade_temporal_ordering', 'raw_piece_count; {'identifier': 'published_trade', 'raw_piece_count': 2, 'content_piece_count': 2 (+12 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `low_source_grounded_glued_identifier_count`

- value: **3**  (from `identifier_glue.low_source_grounded_glued_identifier_count`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'most_recent_published_trade_temporal_ordering', 'raw_piece_count; {'identifier': 'most_recent_published_trade_uniqueness', 'raw_piece_count': 5, '; {'identifier': 'most_recent_published_trade_for', 'raw_piece_count': 5, 'content (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'TradeTime', 'raw_piece_count': 2, 'content_piece_count': 2, 'raw; {'identifier': 'most_recent_published_trade_temporal_ordering', 'raw_piece_count; {'identifier': 'published_trade', 'raw_piece_count': 2, 'content_piece_count': 2 (+12 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `max_identifier_piece_count_content`

- value: **6**  (from `identifier_glue.max_identifier_piece_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'most_recent_published_trade_temporal_ordering', 'raw_piece_count; {'identifier': 'most_recent_published_trade_uniqueness', 'raw_piece_count': 5, '; {'identifier': 'most_recent_published_trade_for', 'raw_piece_count': 5, 'content (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'TradeTime', 'raw_piece_count': 2, 'content_piece_count': 2, 'raw; {'identifier': 'most_recent_published_trade_temporal_ordering', 'raw_piece_count; {'identifier': 'published_trade', 'raw_piece_count': 2, 'content_piece_count': 2 (+12 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `max_identifier_piece_count_raw`

- value: **6**  (from `identifier_glue.max_identifier_piece_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'most_recent_published_trade_temporal_ordering', 'raw_piece_count; {'identifier': 'most_recent_published_trade_uniqueness', 'raw_piece_count': 5, '; {'identifier': 'most_recent_published_trade_for', 'raw_piece_count': 5, 'content (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'TradeTime', 'raw_piece_count': 2, 'content_piece_count': 2, 'raw; {'identifier': 'most_recent_published_trade_temporal_ordering', 'raw_piece_count; {'identifier': 'published_trade', 'raw_piece_count': 2, 'content_piece_count': 2 (+12 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `mean_identifier_piece_count_content`

- value: **1.9166666666666667**  (from `identifier_glue.mean_identifier_piece_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'most_recent_published_trade_temporal_ordering', 'raw_piece_count; {'identifier': 'most_recent_published_trade_uniqueness', 'raw_piece_count': 5, '; {'identifier': 'most_recent_published_trade_for', 'raw_piece_count': 5, 'content (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'TradeTime', 'raw_piece_count': 2, 'content_piece_count': 2, 'raw; {'identifier': 'most_recent_published_trade_temporal_ordering', 'raw_piece_count; {'identifier': 'published_trade', 'raw_piece_count': 2, 'content_piece_count': 2 (+12 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `mean_identifier_piece_count_raw`

- value: **2.2083333333333335**  (from `identifier_glue.mean_identifier_piece_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'most_recent_published_trade_temporal_ordering', 'raw_piece_count; {'identifier': 'most_recent_published_trade_uniqueness', 'raw_piece_count': 5, '; {'identifier': 'most_recent_published_trade_for', 'raw_piece_count': 5, 'content (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'TradeTime', 'raw_piece_count': 2, 'content_piece_count': 2, 'raw; {'identifier': 'most_recent_published_trade_temporal_ordering', 'raw_piece_count; {'identifier': 'published_trade', 'raw_piece_count': 2, 'content_piece_count': 2 (+12 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `new_formula_content_token_count_vs_text_only`

- value: **22**  (from `grounding.new_formula_content_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → financialinstrument; indexcomponent; most_recent_published_trade_for (+19 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; canonical; computation (+39 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'trade', 'current_count': 40, 'baseline_count': 0, 'delta': 40}; {'token': 'published', 'current_count': 12, 'baseline_count': 1, 'delta': 11}; {'token': 'indexcomponent', 'current_count': 9, 'baseline_count': 0, 'delta': 9} (+17 more)
  - `grounding.origin_error_count` → 2

## [WARNING] `ontology_planning` / `new_formula_token_count_vs_text_only`

- value: **27**  (from `grounding.new_formula_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → financialinstrument; indexcomponent; most_recent_published_trade_for (+19 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; canonical; computation (+39 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'trade', 'current_count': 40, 'baseline_count': 0, 'delta': 40}; {'token': 'published', 'current_count': 12, 'baseline_count': 1, 'delta': 11}; {'token': 'indexcomponent', 'current_count': 9, 'baseline_count': 0, 'delta': 9} (+17 more)
  - `grounding.origin_error_count` → 2

## [WARNING] `ontology_planning` / `new_full_surface_content_token_count_vs_text_only`

- value: **42**  (from `grounding.new_full_surface_content_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → financialinstrument; indexcomponent; most_recent_published_trade_for (+19 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; canonical; computation (+39 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'trade', 'current_count': 40, 'baseline_count': 0, 'delta': 40}; {'token': 'published', 'current_count': 12, 'baseline_count': 1, 'delta': 11}; {'token': 'indexcomponent', 'current_count': 9, 'baseline_count': 0, 'delta': 9} (+17 more)
  - `grounding.origin_error_count` → 2

## [WARNING] `ontology_planning` / `new_full_surface_token_count_vs_text_only`

- value: **51**  (from `grounding.new_full_surface_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → financialinstrument; indexcomponent; most_recent_published_trade_for (+19 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; canonical; computation (+39 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'trade', 'current_count': 40, 'baseline_count': 0, 'delta': 40}; {'token': 'published', 'current_count': 12, 'baseline_count': 1, 'delta': 11}; {'token': 'indexcomponent', 'current_count': 9, 'baseline_count': 0, 'delta': 9} (+17 more)
  - `grounding.origin_error_count` → 2

## [WARNING] `ontology_planning` / `new_surface_content_token_count`

- value: **50**  (from `<search recursive metrics JSON for key `new_surface_content_token_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → financialinstrument; indexcomponent; most_recent_published_trade_for (+19 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; canonical; computation (+39 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'trade', 'current_count': 40, 'baseline_count': 0, 'delta': 40}; {'token': 'published', 'current_count': 12, 'baseline_count': 1, 'delta': 11}; {'token': 'indexcomponent', 'current_count': 9, 'baseline_count': 0, 'delta': 9} (+17 more)
  - `grounding.origin_error_count` → 2

## [WARNING] `ontology_planning` / `new_surface_token_count`

- value: **50**  (from `<search recursive metrics JSON for key `new_surface_token_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → financialinstrument; indexcomponent; most_recent_published_trade_for (+19 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; canonical; computation (+39 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'trade', 'current_count': 40, 'baseline_count': 0, 'delta': 40}; {'token': 'published', 'current_count': 12, 'baseline_count': 1, 'delta': 11}; {'token': 'indexcomponent', 'current_count': 9, 'baseline_count': 0, 'delta': 9} (+17 more)
  - `grounding.origin_error_count` → 2

## [WARNING] `ontology_planning` / `ungrounded_sort_count`

- value: **1**  (from `grounding.ungrounded_sort_count`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → financialinstrument; indexcomponent; most_recent_published_trade_for (+19 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; canonical; computation (+39 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'trade', 'current_count': 40, 'baseline_count': 0, 'delta': 40}; {'token': 'published', 'current_count': 12, 'baseline_count': 1, 'delta': 11}; {'token': 'indexcomponent', 'current_count': 9, 'baseline_count': 0, 'delta': 9} (+17 more)
  - `grounding.origin_error_count` → 2

## [WARNING] `ontology_planning` / `ungrounded_symbol_count`

- value: **1**  (from `grounding.ungrounded_symbol_count`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → financialinstrument; indexcomponent; most_recent_published_trade_for (+19 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; canonical; computation (+39 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'trade', 'current_count': 40, 'baseline_count': 0, 'delta': 40}; {'token': 'published', 'current_count': 12, 'baseline_count': 1, 'delta': 11}; {'token': 'indexcomponent', 'current_count': 9, 'baseline_count': 0, 'delta': 9} (+17 more)
  - `grounding.origin_error_count` → 2
