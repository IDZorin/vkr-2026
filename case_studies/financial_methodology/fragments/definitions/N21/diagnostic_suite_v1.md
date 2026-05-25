# Diagnostic report — N21

- **gate**: `needs_review`
- fail: 0, warning: 30

## [WARNING] `merge_canonicalization` / `callable_symbol_count`

- value: **7**  (from `parameterization.callable_symbol_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 7
  - `<related section in metrics JSON>` → 7

## [WARNING] `merge_canonicalization` / `callable_symbol_with_args_count`

- value: **7**  (from `parameterization.callable_symbol_with_args_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 7
  - `<related section in metrics JSON>` → 7

## [WARNING] `merge_canonicalization` / `cross_reference_dropout_count`

- value: **2**  (from `<search recursive metrics JSON for key `cross_reference_dropout_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `evidence.source_cross_references` → Section 1.2
  - `evidence.ir_cross_references` → (empty)

## [WARNING] `merge_canonicalization` / `draft_variant_count`

- value: **1**  (from `variants.draft_variant_count`)
- meaning: A merge/variant/gold comparison changed structure or semantics; report exact compared variants or merge rows.
- repair: Use overlay/bridge/conflict split or reject rewrite based on backtest.

## [WARNING] `merge_canonicalization` / `factorization_count`

- value: **7**  (from `parameterization.factorization_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 7
  - `<related section in metrics JSON>` → 7

## [WARNING] `merge_canonicalization` / `focus_signature_unique_count`

- value: **1**  (from `variability.focus_signature_unique_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.

## [WARNING] `merge_canonicalization` / `quantifier_parameter_slot_count`

- value: **3**  (from `parameterization.quantifier_parameter_slot_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `assertion_complexity.top_complex_assertions` → index_currency_definition
  - `assertion_complexity.max_assertion_depth` → 7
  - `assertion_complexity.total_quantifier_count` → 3

## [WARNING] `merge_canonicalization` / `top_level_parameter_slot_count`

- value: **14**  (from `parameterization.top_level_parameter_slot_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 14
  - `<related section in metrics JSON>` → 14

## [WARNING] `merge_canonicalization` / `total_parameter_slot_mass`

- value: **17**  (from `parameterization.total_parameter_slot_mass`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 17
  - `<related section in metrics JSON>` → 17

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

- value: **3**  (from `identifier_glue.compound_identifier_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'Section1_2IndexTable', 'raw_piece_count': 4, 'content_piece_coun; {'identifier': 'index_currency_definition', 'raw_piece_count': 3, 'content_piece; {'identifier': 'IndexCurrencySpecification', 'raw_piece_count': 3, 'content_piec (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DocumentPart', 'raw_piece_count': 2, 'content_piece_count': 2, '; {'identifier': 'specification_column', 'raw_piece_count': 2, 'content_piece_coun; {'identifier': 'specification_currency', 'raw_piece_count': 2, 'content_piece_co (+10 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `compound_identifier_count_raw`

- value: **1**  (from `identifier_glue.compound_identifier_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'Section1_2IndexTable', 'raw_piece_count': 4, 'content_piece_coun; {'identifier': 'index_currency_definition', 'raw_piece_count': 3, 'content_piece; {'identifier': 'IndexCurrencySpecification', 'raw_piece_count': 3, 'content_piec (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DocumentPart', 'raw_piece_count': 2, 'content_piece_count': 2, '; {'identifier': 'specification_column', 'raw_piece_count': 2, 'content_piece_coun; {'identifier': 'specification_currency', 'raw_piece_count': 2, 'content_piece_co (+10 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `cross_reference_dropout_count`

- value: **2**  (from `<search recursive metrics JSON for key `cross_reference_dropout_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `evidence.source_cross_references` → Section 1.2
  - `evidence.ir_cross_references` → (empty)

## [WARNING] `ontology_planning` / `identifier_count`

- value: **20**  (from `identifier_glue.identifier_count`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'Section1_2IndexTable', 'raw_piece_count': 4, 'content_piece_coun; {'identifier': 'index_currency_definition', 'raw_piece_count': 3, 'content_piece; {'identifier': 'IndexCurrencySpecification', 'raw_piece_count': 3, 'content_piec (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DocumentPart', 'raw_piece_count': 2, 'content_piece_count': 2, '; {'identifier': 'specification_column', 'raw_piece_count': 2, 'content_piece_coun; {'identifier': 'specification_currency', 'raw_piece_count': 2, 'content_piece_co (+10 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `identifier_glue_excess_mass_content`

- value: **3**  (from `identifier_glue.identifier_glue_excess_mass_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'Section1_2IndexTable', 'raw_piece_count': 4, 'content_piece_coun; {'identifier': 'index_currency_definition', 'raw_piece_count': 3, 'content_piece; {'identifier': 'IndexCurrencySpecification', 'raw_piece_count': 3, 'content_piec (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DocumentPart', 'raw_piece_count': 2, 'content_piece_count': 2, '; {'identifier': 'specification_column', 'raw_piece_count': 2, 'content_piece_coun; {'identifier': 'specification_currency', 'raw_piece_count': 2, 'content_piece_co (+10 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `identifier_glue_excess_mass_raw`

- value: **1**  (from `identifier_glue.identifier_glue_excess_mass_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'Section1_2IndexTable', 'raw_piece_count': 4, 'content_piece_coun; {'identifier': 'index_currency_definition', 'raw_piece_count': 3, 'content_piece; {'identifier': 'IndexCurrencySpecification', 'raw_piece_count': 3, 'content_piec (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DocumentPart', 'raw_piece_count': 2, 'content_piece_count': 2, '; {'identifier': 'specification_column', 'raw_piece_count': 2, 'content_piece_coun; {'identifier': 'specification_currency', 'raw_piece_count': 2, 'content_piece_co (+10 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `low_source_grounded_glued_identifier_count`

- value: **3**  (from `identifier_glue.low_source_grounded_glued_identifier_count`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'Section1_2IndexTable', 'raw_piece_count': 4, 'content_piece_coun; {'identifier': 'index_currency_definition', 'raw_piece_count': 3, 'content_piece; {'identifier': 'IndexCurrencySpecification', 'raw_piece_count': 3, 'content_piec (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DocumentPart', 'raw_piece_count': 2, 'content_piece_count': 2, '; {'identifier': 'specification_column', 'raw_piece_count': 2, 'content_piece_coun; {'identifier': 'specification_currency', 'raw_piece_count': 2, 'content_piece_co (+10 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `max_identifier_piece_count_content`

- value: **3**  (from `identifier_glue.max_identifier_piece_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'Section1_2IndexTable', 'raw_piece_count': 4, 'content_piece_coun; {'identifier': 'index_currency_definition', 'raw_piece_count': 3, 'content_piece; {'identifier': 'IndexCurrencySpecification', 'raw_piece_count': 3, 'content_piec (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DocumentPart', 'raw_piece_count': 2, 'content_piece_count': 2, '; {'identifier': 'specification_column', 'raw_piece_count': 2, 'content_piece_coun; {'identifier': 'specification_currency', 'raw_piece_count': 2, 'content_piece_co (+10 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `max_identifier_piece_count_raw`

- value: **4**  (from `identifier_glue.max_identifier_piece_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'Section1_2IndexTable', 'raw_piece_count': 4, 'content_piece_coun; {'identifier': 'index_currency_definition', 'raw_piece_count': 3, 'content_piece; {'identifier': 'IndexCurrencySpecification', 'raw_piece_count': 3, 'content_piec (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DocumentPart', 'raw_piece_count': 2, 'content_piece_count': 2, '; {'identifier': 'specification_column', 'raw_piece_count': 2, 'content_piece_coun; {'identifier': 'specification_currency', 'raw_piece_count': 2, 'content_piece_co (+10 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `mean_identifier_piece_count_content`

- value: **1.7**  (from `identifier_glue.mean_identifier_piece_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'Section1_2IndexTable', 'raw_piece_count': 4, 'content_piece_coun; {'identifier': 'index_currency_definition', 'raw_piece_count': 3, 'content_piece; {'identifier': 'IndexCurrencySpecification', 'raw_piece_count': 3, 'content_piec (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DocumentPart', 'raw_piece_count': 2, 'content_piece_count': 2, '; {'identifier': 'specification_column', 'raw_piece_count': 2, 'content_piece_coun; {'identifier': 'specification_currency', 'raw_piece_count': 2, 'content_piece_co (+10 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `mean_identifier_piece_count_raw`

- value: **2.05**  (from `identifier_glue.mean_identifier_piece_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'Section1_2IndexTable', 'raw_piece_count': 4, 'content_piece_coun; {'identifier': 'index_currency_definition', 'raw_piece_count': 3, 'content_piece; {'identifier': 'IndexCurrencySpecification', 'raw_piece_count': 3, 'content_piec (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DocumentPart', 'raw_piece_count': 2, 'content_piece_count': 2, '; {'identifier': 'specification_column', 'raw_piece_count': 2, 'content_piece_coun; {'identifier': 'specification_currency', 'raw_piece_count': 2, 'content_piece_co (+10 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `new_formula_content_token_count_vs_text_only`

- value: **16**  (from `grounding.new_formula_content_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → column_of_table; currency_column_in_section_1_2_table; currencycolumn (+13 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; canonical; column_of_table (+32 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'table', 'current_count': 12, 'baseline_count': 1, 'delta': 11}; {'token': 'index', 'current_count': 9, 'baseline_count': 1, 'delta': 8}; {'token': 'specification', 'current_count': 8, 'baseline_count': 0, 'delta': 8} (+11 more)
  - `grounding.origin_error_count` → 2

## [WARNING] `ontology_planning` / `new_formula_token_count_vs_text_only`

- value: **18**  (from `grounding.new_formula_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → column_of_table; currency_column_in_section_1_2_table; currencycolumn (+13 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; canonical; column_of_table (+32 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'table', 'current_count': 12, 'baseline_count': 1, 'delta': 11}; {'token': 'index', 'current_count': 9, 'baseline_count': 1, 'delta': 8}; {'token': 'specification', 'current_count': 8, 'baseline_count': 0, 'delta': 8} (+11 more)
  - `grounding.origin_error_count` → 2

## [WARNING] `ontology_planning` / `new_full_surface_content_token_count_vs_text_only`

- value: **35**  (from `grounding.new_full_surface_content_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → column_of_table; currency_column_in_section_1_2_table; currencycolumn (+13 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; canonical; column_of_table (+32 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'table', 'current_count': 12, 'baseline_count': 1, 'delta': 11}; {'token': 'index', 'current_count': 9, 'baseline_count': 1, 'delta': 8}; {'token': 'specification', 'current_count': 8, 'baseline_count': 0, 'delta': 8} (+11 more)
  - `grounding.origin_error_count` → 2

## [WARNING] `ontology_planning` / `new_full_surface_token_count_vs_text_only`

- value: **41**  (from `grounding.new_full_surface_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → column_of_table; currency_column_in_section_1_2_table; currencycolumn (+13 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; canonical; column_of_table (+32 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'table', 'current_count': 12, 'baseline_count': 1, 'delta': 11}; {'token': 'index', 'current_count': 9, 'baseline_count': 1, 'delta': 8}; {'token': 'specification', 'current_count': 8, 'baseline_count': 0, 'delta': 8} (+11 more)
  - `grounding.origin_error_count` → 2

## [WARNING] `ontology_planning` / `new_surface_content_token_count`

- value: **30**  (from `<search recursive metrics JSON for key `new_surface_content_token_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → column_of_table; currency_column_in_section_1_2_table; currencycolumn (+13 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; canonical; column_of_table (+32 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'table', 'current_count': 12, 'baseline_count': 1, 'delta': 11}; {'token': 'index', 'current_count': 9, 'baseline_count': 1, 'delta': 8}; {'token': 'specification', 'current_count': 8, 'baseline_count': 0, 'delta': 8} (+11 more)
  - `grounding.origin_error_count` → 2

## [WARNING] `ontology_planning` / `new_surface_token_count`

- value: **30**  (from `<search recursive metrics JSON for key `new_surface_token_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → column_of_table; currency_column_in_section_1_2_table; currencycolumn (+13 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; canonical; column_of_table (+32 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'table', 'current_count': 12, 'baseline_count': 1, 'delta': 11}; {'token': 'index', 'current_count': 9, 'baseline_count': 1, 'delta': 8}; {'token': 'specification', 'current_count': 8, 'baseline_count': 0, 'delta': 8} (+11 more)
  - `grounding.origin_error_count` → 2

## [WARNING] `ontology_planning` / `ungrounded_sort_count`

- value: **2**  (from `grounding.ungrounded_sort_count`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → column_of_table; currency_column_in_section_1_2_table; currencycolumn (+13 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; canonical; column_of_table (+32 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'table', 'current_count': 12, 'baseline_count': 1, 'delta': 11}; {'token': 'index', 'current_count': 9, 'baseline_count': 1, 'delta': 8}; {'token': 'specification', 'current_count': 8, 'baseline_count': 0, 'delta': 8} (+11 more)
  - `grounding.origin_error_count` → 2

## [ERROR_NO_VALUE] `merge_canonicalization` / `llm_bertscore`

- value: **None**  (from `None`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `render_back.render_back_text` → An index currency is defined by an index currency specification that links an index to a currency, the CurrencyColumn, and the Section 1.2 Index Table. The Section 1.2 Index Table is in Section 1.2, and the CurrencyColumn is a column of that table.
  - `render_back.render_nli_text_implies_ir` → 0.929487943649292
  - `render_back.render_nli_ir_implies_text` → 0.6444000601768494
  - `render_back.render_contradiction_score` → 0.18321286141872406

## [ERROR_NO_VALUE] `merge_canonicalization` / `llm_contradiction`

- value: **None**  (from `None`)
- meaning: Rendered IR does not preserve entailment/equivalence; report render text and entailment/contradiction values.
- repair: Repair IR until render-back and entailment preserve normalized meaning.
- evidence:
  - `render_back.render_back_text` → An index currency is defined by an index currency specification that links an index to a currency, the CurrencyColumn, and the Section 1.2 Index Table. The Section 1.2 Index Table is in Section 1.2, and the CurrencyColumn is a column of that table.
  - `render_back.render_nli_text_implies_ir` → 0.929487943649292
  - `render_back.render_nli_ir_implies_text` → 0.6444000601768494
  - `render_back.render_contradiction_score` → 0.18321286141872406

## [ERROR_NO_VALUE] `merge_canonicalization` / `llm_ir_to_text`

- value: **None**  (from `None`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.

## [ERROR_NO_VALUE] `merge_canonicalization` / `llm_text_to_ir`

- value: **None**  (from `None`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
