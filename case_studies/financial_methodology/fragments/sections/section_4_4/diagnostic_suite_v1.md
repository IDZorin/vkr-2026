# Diagnostic report — section_4_4

- **gate**: `needs_review`
- fail: 0, warning: 37

## [WARNING] `a4v3_semantic_lint` / `shared_name_token_without_structural_carrier_count`

- value: **2**  (from `a4v3_semantic_lint_v1.json::summary.shared_name_token_without_structural_carrier_count`)
- meaning: A semantic link may be encoded only by repeated words inside predicate names, rather than by an explicit shared entity/sort/argument in formula structure.
- repair: Introduce a structural carrier for the repeated concept, e.g. a sort/entity and relation arguments, or document why the repeated token is intentionally only lexical.
- evidence:
  - `a4v3_semantic_lint_v1.json::findings` → {'check': 'shared_name_token_without_structural_carrier', 'severity': 'soft', 'c; {'check': 'shared_name_token_without_structural_carrier', 'severity': 'soft', 'c

## [WARNING] `merge_canonicalization` / `callable_symbol_count`

- value: **28**  (from `parameterization.callable_symbol_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 28
  - `<related section in metrics JSON>` → 28

## [WARNING] `merge_canonicalization` / `callable_symbol_with_args_count`

- value: **28**  (from `parameterization.callable_symbol_with_args_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 28
  - `<related section in metrics JSON>` → 28

## [WARNING] `merge_canonicalization` / `cross_reference_dropout_count`

- value: **3**  (from `<search recursive metrics JSON for key `cross_reference_dropout_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `evidence.source_cross_references` → Section 4.4; Section “Announcements”
  - `evidence.ir_cross_references` → body of announcements_section_on_solactive_website mentions section/annex; body of section_of_website mentions section/annex; entity ThisGuideline : Document

## [WARNING] `merge_canonicalization` / `cross_reference_usage_count`

- value: **3**  (from `<search recursive metrics JSON for key `cross_reference_usage_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `evidence.ir_cross_references` → body of announcements_section_on_solactive_website mentions section/annex; body of section_of_website mentions section/annex; entity ThisGuideline : Document

## [WARNING] `merge_canonicalization` / `dependency_link_count`

- value: **5**  (from `<search recursive metrics JSON for key `dependency_link_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 5
  - `<related section in metrics JSON>` → 5

## [WARNING] `merge_canonicalization` / `draft_variant_count`

- value: **1**  (from `variants.draft_variant_count`)
- meaning: A merge/variant/gold comparison changed structure or semantics; report exact compared variants or merge rows.
- repair: Use overlay/bridge/conflict split or reject rewrite based on backtest.

## [WARNING] `merge_canonicalization` / `factorization_count`

- value: **28**  (from `parameterization.factorization_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 28
  - `<related section in metrics JSON>` → 28

## [WARNING] `merge_canonicalization` / `focus_signature_unique_count`

- value: **1**  (from `variability.focus_signature_unique_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.

## [WARNING] `merge_canonicalization` / `quantifier_parameter_slot_count`

- value: **17**  (from `parameterization.quantifier_parameter_slot_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `assertion_complexity.top_complex_assertions` → corporate_action_creates_required_index_adjustment; notice_period_at_least_two_trading_days; index_adjustment_notice_publication (+3 more)
  - `assertion_complexity.max_assertion_depth` → 9
  - `assertion_complexity.total_quantifier_count` → 17

## [WARNING] `merge_canonicalization` / `top_level_parameter_slot_count`

- value: **55**  (from `parameterization.top_level_parameter_slot_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 55
  - `<related section in metrics JSON>` → 55

## [WARNING] `merge_canonicalization` / `total_parameter_slot_mass`

- value: **72**  (from `parameterization.total_parameter_slot_mass`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 72
  - `<related section in metrics JSON>` → 72

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

- value: **28**  (from `identifier_glue.compound_identifier_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'index_adjustment_implemented_on_notice_effective_day', 'raw_piec; {'identifier': 'notice_period_at_least_two_trading_days', 'raw_piece_count': 7, ; {'identifier': 'corporate_action_creates_required_index_adjustment', 'raw_piece_ (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DocumentPart', 'raw_piece_count': 2, 'content_piece_count': 2, '; {'identifier': 'VagueTerm', 'raw_piece_count': 2, 'content_piece_count': 2, 'raw; {'identifier': 'WebResource', 'raw_piece_count': 2, 'content_piece_count': 2, 'r (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `compound_identifier_count_raw`

- value: **22**  (from `identifier_glue.compound_identifier_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'index_adjustment_implemented_on_notice_effective_day', 'raw_piec; {'identifier': 'notice_period_at_least_two_trading_days', 'raw_piece_count': 7, ; {'identifier': 'corporate_action_creates_required_index_adjustment', 'raw_piece_ (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DocumentPart', 'raw_piece_count': 2, 'content_piece_count': 2, '; {'identifier': 'VagueTerm', 'raw_piece_count': 2, 'content_piece_count': 2, 'raw; {'identifier': 'WebResource', 'raw_piece_count': 2, 'content_piece_count': 2, 'r (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `cross_reference_dropout_count`

- value: **3**  (from `<search recursive metrics JSON for key `cross_reference_dropout_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `evidence.source_cross_references` → Section 4.4; Section “Announcements”
  - `evidence.ir_cross_references` → body of announcements_section_on_solactive_website mentions section/annex; body of section_of_website mentions section/annex; entity ThisGuideline : Document

## [WARNING] `ontology_planning` / `cross_reference_usage_count`

- value: **3**  (from `<search recursive metrics JSON for key `cross_reference_usage_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `evidence.ir_cross_references` → body of announcements_section_on_solactive_website mentions section/annex; body of section_of_website mentions section/annex; entity ThisGuideline : Document

## [WARNING] `ontology_planning` / `dependency_link_count`

- value: **5**  (from `<search recursive metrics JSON for key `dependency_link_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 5
  - `<related section in metrics JSON>` → 5

## [WARNING] `ontology_planning` / `identifier_count`

- value: **81**  (from `identifier_glue.identifier_count`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'index_adjustment_implemented_on_notice_effective_day', 'raw_piec; {'identifier': 'notice_period_at_least_two_trading_days', 'raw_piece_count': 7, ; {'identifier': 'corporate_action_creates_required_index_adjustment', 'raw_piece_ (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DocumentPart', 'raw_piece_count': 2, 'content_piece_count': 2, '; {'identifier': 'VagueTerm', 'raw_piece_count': 2, 'content_piece_count': 2, 'raw; {'identifier': 'WebResource', 'raw_piece_count': 2, 'content_piece_count': 2, 'r (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `identifier_glue_excess_mass_content`

- value: **46**  (from `identifier_glue.identifier_glue_excess_mass_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'index_adjustment_implemented_on_notice_effective_day', 'raw_piec; {'identifier': 'notice_period_at_least_two_trading_days', 'raw_piece_count': 7, ; {'identifier': 'corporate_action_creates_required_index_adjustment', 'raw_piece_ (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DocumentPart', 'raw_piece_count': 2, 'content_piece_count': 2, '; {'identifier': 'VagueTerm', 'raw_piece_count': 2, 'content_piece_count': 2, 'raw; {'identifier': 'WebResource', 'raw_piece_count': 2, 'content_piece_count': 2, 'r (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `identifier_glue_excess_mass_raw`

- value: **41**  (from `identifier_glue.identifier_glue_excess_mass_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'index_adjustment_implemented_on_notice_effective_day', 'raw_piec; {'identifier': 'notice_period_at_least_two_trading_days', 'raw_piece_count': 7, ; {'identifier': 'corporate_action_creates_required_index_adjustment', 'raw_piece_ (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DocumentPart', 'raw_piece_count': 2, 'content_piece_count': 2, '; {'identifier': 'VagueTerm', 'raw_piece_count': 2, 'content_piece_count': 2, 'raw; {'identifier': 'WebResource', 'raw_piece_count': 2, 'content_piece_count': 2, 'r (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `low_source_grounded_glued_identifier_count`

- value: **12**  (from `identifier_glue.low_source_grounded_glued_identifier_count`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'index_adjustment_implemented_on_notice_effective_day', 'raw_piec; {'identifier': 'notice_period_at_least_two_trading_days', 'raw_piece_count': 7, ; {'identifier': 'corporate_action_creates_required_index_adjustment', 'raw_piece_ (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DocumentPart', 'raw_piece_count': 2, 'content_piece_count': 2, '; {'identifier': 'VagueTerm', 'raw_piece_count': 2, 'content_piece_count': 2, 'raw; {'identifier': 'WebResource', 'raw_piece_count': 2, 'content_piece_count': 2, 'r (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `max_identifier_piece_count_content`

- value: **6**  (from `identifier_glue.max_identifier_piece_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'index_adjustment_implemented_on_notice_effective_day', 'raw_piec; {'identifier': 'notice_period_at_least_two_trading_days', 'raw_piece_count': 7, ; {'identifier': 'corporate_action_creates_required_index_adjustment', 'raw_piece_ (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DocumentPart', 'raw_piece_count': 2, 'content_piece_count': 2, '; {'identifier': 'VagueTerm', 'raw_piece_count': 2, 'content_piece_count': 2, 'raw; {'identifier': 'WebResource', 'raw_piece_count': 2, 'content_piece_count': 2, 'r (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `max_identifier_piece_count_raw`

- value: **7**  (from `identifier_glue.max_identifier_piece_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'index_adjustment_implemented_on_notice_effective_day', 'raw_piec; {'identifier': 'notice_period_at_least_two_trading_days', 'raw_piece_count': 7, ; {'identifier': 'corporate_action_creates_required_index_adjustment', 'raw_piece_ (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DocumentPart', 'raw_piece_count': 2, 'content_piece_count': 2, '; {'identifier': 'VagueTerm', 'raw_piece_count': 2, 'content_piece_count': 2, 'raw; {'identifier': 'WebResource', 'raw_piece_count': 2, 'content_piece_count': 2, 'r (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `mean_identifier_piece_count_content`

- value: **2.1604938271604937**  (from `identifier_glue.mean_identifier_piece_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'index_adjustment_implemented_on_notice_effective_day', 'raw_piec; {'identifier': 'notice_period_at_least_two_trading_days', 'raw_piece_count': 7, ; {'identifier': 'corporate_action_creates_required_index_adjustment', 'raw_piece_ (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DocumentPart', 'raw_piece_count': 2, 'content_piece_count': 2, '; {'identifier': 'VagueTerm', 'raw_piece_count': 2, 'content_piece_count': 2, 'raw; {'identifier': 'WebResource', 'raw_piece_count': 2, 'content_piece_count': 2, 'r (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `mean_identifier_piece_count_raw`

- value: **2.8271604938271606**  (from `identifier_glue.mean_identifier_piece_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'index_adjustment_implemented_on_notice_effective_day', 'raw_piec; {'identifier': 'notice_period_at_least_two_trading_days', 'raw_piece_count': 7, ; {'identifier': 'corporate_action_creates_required_index_adjustment', 'raw_piece_ (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'DocumentPart', 'raw_piece_count': 2, 'content_piece_count': 2, '; {'identifier': 'VagueTerm', 'raw_piece_count': 2, 'content_piece_count': 2, 'raw; {'identifier': 'WebResource', 'raw_piece_count': 2, 'content_piece_count': 2, 'r (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `new_formula_content_token_count_vs_text_only`

- value: **80**  (from `grounding.new_formula_content_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → adjustment_between_interval; adjustment_effect_described_by; adjustment_effect_scope_described_by (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; adjustment_between_interval; adjustment_effect_described_by (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'adjustment', 'current_count': 39, 'baseline_count': 4, 'delta': 35}; {'token': 'notice', 'current_count': 28, 'baseline_count': 2, 'delta': 26}; {'token': 'interval', 'current_count': 16, 'baseline_count': 0, 'delta': 16} (+17 more)
  - `grounding.origin_error_count` → 41

## [WARNING] `ontology_planning` / `new_formula_token_count_vs_text_only`

- value: **88**  (from `grounding.new_formula_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → adjustment_between_interval; adjustment_effect_described_by; adjustment_effect_scope_described_by (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; adjustment_between_interval; adjustment_effect_described_by (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'adjustment', 'current_count': 39, 'baseline_count': 4, 'delta': 35}; {'token': 'notice', 'current_count': 28, 'baseline_count': 2, 'delta': 26}; {'token': 'interval', 'current_count': 16, 'baseline_count': 0, 'delta': 16} (+17 more)
  - `grounding.origin_error_count` → 41

## [WARNING] `ontology_planning` / `new_full_surface_content_token_count_vs_text_only`

- value: **99**  (from `grounding.new_full_surface_content_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → adjustment_between_interval; adjustment_effect_described_by; adjustment_effect_scope_described_by (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; adjustment_between_interval; adjustment_effect_described_by (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'adjustment', 'current_count': 39, 'baseline_count': 4, 'delta': 35}; {'token': 'notice', 'current_count': 28, 'baseline_count': 2, 'delta': 26}; {'token': 'interval', 'current_count': 16, 'baseline_count': 0, 'delta': 16} (+17 more)
  - `grounding.origin_error_count` → 41

## [WARNING] `ontology_planning` / `new_full_surface_token_count_vs_text_only`

- value: **111**  (from `grounding.new_full_surface_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → adjustment_between_interval; adjustment_effect_described_by; adjustment_effect_scope_described_by (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; adjustment_between_interval; adjustment_effect_described_by (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'adjustment', 'current_count': 39, 'baseline_count': 4, 'delta': 35}; {'token': 'notice', 'current_count': 28, 'baseline_count': 2, 'delta': 26}; {'token': 'interval', 'current_count': 16, 'baseline_count': 0, 'delta': 16} (+17 more)
  - `grounding.origin_error_count` → 41

## [WARNING] `ontology_planning` / `new_surface_content_token_count`

- value: **198**  (from `<search recursive metrics JSON for key `new_surface_content_token_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → adjustment_between_interval; adjustment_effect_described_by; adjustment_effect_scope_described_by (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; adjustment_between_interval; adjustment_effect_described_by (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'adjustment', 'current_count': 39, 'baseline_count': 4, 'delta': 35}; {'token': 'notice', 'current_count': 28, 'baseline_count': 2, 'delta': 26}; {'token': 'interval', 'current_count': 16, 'baseline_count': 0, 'delta': 16} (+17 more)
  - `grounding.origin_error_count` → 41

## [WARNING] `ontology_planning` / `new_surface_token_count`

- value: **198**  (from `<search recursive metrics JSON for key `new_surface_token_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → adjustment_between_interval; adjustment_effect_described_by; adjustment_effect_scope_described_by (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; adjustment_between_interval; adjustment_effect_described_by (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'adjustment', 'current_count': 39, 'baseline_count': 4, 'delta': 35}; {'token': 'notice', 'current_count': 28, 'baseline_count': 2, 'delta': 26}; {'token': 'interval', 'current_count': 16, 'baseline_count': 0, 'delta': 16} (+17 more)
  - `grounding.origin_error_count` → 41

## [WARNING] `ontology_planning` / `ungrounded_callee_count`

- value: **1**  (from `grounding.ungrounded_callee_count`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → adjustment_between_interval; adjustment_effect_described_by; adjustment_effect_scope_described_by (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; adjustment_between_interval; adjustment_effect_described_by (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'adjustment', 'current_count': 39, 'baseline_count': 4, 'delta': 35}; {'token': 'notice', 'current_count': 28, 'baseline_count': 2, 'delta': 26}; {'token': 'interval', 'current_count': 16, 'baseline_count': 0, 'delta': 16} (+17 more)
  - `grounding.origin_error_count` → 41

## [WARNING] `ontology_planning` / `ungrounded_sort_count`

- value: **27**  (from `grounding.ungrounded_sort_count`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → adjustment_between_interval; adjustment_effect_described_by; adjustment_effect_scope_described_by (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; adjustment_between_interval; adjustment_effect_described_by (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'adjustment', 'current_count': 39, 'baseline_count': 4, 'delta': 35}; {'token': 'notice', 'current_count': 28, 'baseline_count': 2, 'delta': 26}; {'token': 'interval', 'current_count': 16, 'baseline_count': 0, 'delta': 16} (+17 more)
  - `grounding.origin_error_count` → 41

## [WARNING] `ontology_planning` / `ungrounded_symbol_count`

- value: **13**  (from `grounding.ungrounded_symbol_count`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → adjustment_between_interval; adjustment_effect_described_by; adjustment_effect_scope_described_by (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; adjustment_between_interval; adjustment_effect_described_by (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'adjustment', 'current_count': 39, 'baseline_count': 4, 'delta': 35}; {'token': 'notice', 'current_count': 28, 'baseline_count': 2, 'delta': 26}; {'token': 'interval', 'current_count': 16, 'baseline_count': 0, 'delta': 16} (+17 more)
  - `grounding.origin_error_count` → 41

## [ERROR_NO_VALUE] `merge_canonicalization` / `llm_bertscore`

- value: **None**  (from `None`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `render_back.render_back_text` → Adjustments to the Index may be necessary in certain circumstances between regular rebalance days. Any such adjustment is made in compliance with the Solactive Equity Index Methodology and is announced by Solactive in the Announcements section of the Solactive Website.  

A corporate action specified in Section 4.4 that relates to an Index Component gives rise to a required Index Adjustment for the Index, affecting that component and falling within a Rebalance Interval. The effect of a required adjustment may relate to the component relation, component number, or component weighting, and the weighting effect is described with respect to certain Index Components.  

The relevant notice states the effective day for the adjustment. The adjustment is implemented on that effective day. The notice is published by Solactive on the Solactive Website in the Announcements section and provides a notice period of at least two Trading Days for the affected component.
  - `render_back.render_nli_text_implies_ir` → 0.9465484619140625
  - `render_back.render_nli_ir_implies_text` → 0.8422635197639465
  - `render_back.render_contradiction_score` → 0.039833635091781616

## [ERROR_NO_VALUE] `merge_canonicalization` / `llm_contradiction`

- value: **None**  (from `None`)
- meaning: Rendered IR does not preserve entailment/equivalence; report render text and entailment/contradiction values.
- repair: Repair IR until render-back and entailment preserve normalized meaning.
- evidence:
  - `render_back.render_back_text` → Adjustments to the Index may be necessary in certain circumstances between regular rebalance days. Any such adjustment is made in compliance with the Solactive Equity Index Methodology and is announced by Solactive in the Announcements section of the Solactive Website.  

A corporate action specified in Section 4.4 that relates to an Index Component gives rise to a required Index Adjustment for the Index, affecting that component and falling within a Rebalance Interval. The effect of a required adjustment may relate to the component relation, component number, or component weighting, and the weighting effect is described with respect to certain Index Components.  

The relevant notice states the effective day for the adjustment. The adjustment is implemented on that effective day. The notice is published by Solactive on the Solactive Website in the Announcements section and provides a notice period of at least two Trading Days for the affected component.
  - `render_back.render_nli_text_implies_ir` → 0.9465484619140625
  - `render_back.render_nli_ir_implies_text` → 0.8422635197639465
  - `render_back.render_contradiction_score` → 0.039833635091781616

## [ERROR_NO_VALUE] `merge_canonicalization` / `llm_ir_to_text`

- value: **None**  (from `None`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.

## [ERROR_NO_VALUE] `merge_canonicalization` / `llm_text_to_ir`

- value: **None**  (from `None`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
