# Diagnostic report — section_1_5

- **gate**: `needs_review`
- fail: 0, warning: 28

## [WARNING] `merge_canonicalization` / `callable_symbol_count`

- value: **6**  (from `parameterization.callable_symbol_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 6
  - `<related section in metrics JSON>` → 6

## [WARNING] `merge_canonicalization` / `callable_symbol_with_args_count`

- value: **6**  (from `parameterization.callable_symbol_with_args_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 6
  - `<related section in metrics JSON>` → 6

## [WARNING] `merge_canonicalization` / `draft_variant_count`

- value: **1**  (from `variants.draft_variant_count`)
- meaning: A merge/variant/gold comparison changed structure or semantics; report exact compared variants or merge rows.
- repair: Use overlay/bridge/conflict split or reject rewrite based on backtest.

## [WARNING] `merge_canonicalization` / `factorization_count`

- value: **6**  (from `parameterization.factorization_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 6
  - `<related section in metrics JSON>` → 6

## [WARNING] `merge_canonicalization` / `focus_signature_unique_count`

- value: **1**  (from `variability.focus_signature_unique_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.

## [WARNING] `merge_canonicalization` / `top_level_parameter_slot_count`

- value: **12**  (from `parameterization.top_level_parameter_slot_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 12
  - `<related section in metrics JSON>` → 12

## [WARNING] `merge_canonicalization` / `total_parameter_slot_mass`

- value: **12**  (from `parameterization.total_parameter_slot_mass`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 12
  - `<related section in metrics JSON>` → 12

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

- value: **10**  (from `identifier_glue.compound_identifier_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'license_class_uses_index_as_underlying_value', 'raw_piece_count'; {'identifier': 'LicensesToUseIndexAsUnderlyingValue', 'raw_piece_count': 7, 'con; {'identifier': 'IndexUnderlyingValueLicenseIssuance', 'raw_piece_count': 5, 'con (+15 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'issuance_of_license_class', 'raw_piece_count': 4, 'content_piece; {'identifier': 'issuance_to_recipient_category', 'raw_piece_count': 4, 'content_; {'identifier': 'license_instance_of_class', 'raw_piece_count': 4, 'content_piece (+10 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `compound_identifier_count_raw`

- value: **8**  (from `identifier_glue.compound_identifier_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'license_class_uses_index_as_underlying_value', 'raw_piece_count'; {'identifier': 'LicensesToUseIndexAsUnderlyingValue', 'raw_piece_count': 7, 'con; {'identifier': 'IndexUnderlyingValueLicenseIssuance', 'raw_piece_count': 5, 'con (+15 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'issuance_of_license_class', 'raw_piece_count': 4, 'content_piece; {'identifier': 'issuance_to_recipient_category', 'raw_piece_count': 4, 'content_; {'identifier': 'license_instance_of_class', 'raw_piece_count': 4, 'content_piece (+10 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `identifier_count`

- value: **18**  (from `identifier_glue.identifier_count`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'license_class_uses_index_as_underlying_value', 'raw_piece_count'; {'identifier': 'LicensesToUseIndexAsUnderlyingValue', 'raw_piece_count': 7, 'con; {'identifier': 'IndexUnderlyingValueLicenseIssuance', 'raw_piece_count': 5, 'con (+15 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'issuance_of_license_class', 'raw_piece_count': 4, 'content_piece; {'identifier': 'issuance_to_recipient_category', 'raw_piece_count': 4, 'content_; {'identifier': 'license_instance_of_class', 'raw_piece_count': 4, 'content_piece (+10 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `identifier_glue_excess_mass_content`

- value: **19**  (from `identifier_glue.identifier_glue_excess_mass_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'license_class_uses_index_as_underlying_value', 'raw_piece_count'; {'identifier': 'LicensesToUseIndexAsUnderlyingValue', 'raw_piece_count': 7, 'con; {'identifier': 'IndexUnderlyingValueLicenseIssuance', 'raw_piece_count': 5, 'con (+15 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'issuance_of_license_class', 'raw_piece_count': 4, 'content_piece; {'identifier': 'issuance_to_recipient_category', 'raw_piece_count': 4, 'content_; {'identifier': 'license_instance_of_class', 'raw_piece_count': 4, 'content_piece (+10 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `identifier_glue_excess_mass_raw`

- value: **15**  (from `identifier_glue.identifier_glue_excess_mass_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'license_class_uses_index_as_underlying_value', 'raw_piece_count'; {'identifier': 'LicensesToUseIndexAsUnderlyingValue', 'raw_piece_count': 7, 'con; {'identifier': 'IndexUnderlyingValueLicenseIssuance', 'raw_piece_count': 5, 'con (+15 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'issuance_of_license_class', 'raw_piece_count': 4, 'content_piece; {'identifier': 'issuance_to_recipient_category', 'raw_piece_count': 4, 'content_; {'identifier': 'license_instance_of_class', 'raw_piece_count': 4, 'content_piece (+10 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `low_source_grounded_glued_identifier_count`

- value: **8**  (from `identifier_glue.low_source_grounded_glued_identifier_count`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'license_class_uses_index_as_underlying_value', 'raw_piece_count'; {'identifier': 'LicensesToUseIndexAsUnderlyingValue', 'raw_piece_count': 7, 'con; {'identifier': 'IndexUnderlyingValueLicenseIssuance', 'raw_piece_count': 5, 'con (+15 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'issuance_of_license_class', 'raw_piece_count': 4, 'content_piece; {'identifier': 'issuance_to_recipient_category', 'raw_piece_count': 4, 'content_; {'identifier': 'license_instance_of_class', 'raw_piece_count': 4, 'content_piece (+10 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `max_identifier_piece_count_content`

- value: **6**  (from `identifier_glue.max_identifier_piece_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'license_class_uses_index_as_underlying_value', 'raw_piece_count'; {'identifier': 'LicensesToUseIndexAsUnderlyingValue', 'raw_piece_count': 7, 'con; {'identifier': 'IndexUnderlyingValueLicenseIssuance', 'raw_piece_count': 5, 'con (+15 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'issuance_of_license_class', 'raw_piece_count': 4, 'content_piece; {'identifier': 'issuance_to_recipient_category', 'raw_piece_count': 4, 'content_; {'identifier': 'license_instance_of_class', 'raw_piece_count': 4, 'content_piece (+10 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `max_identifier_piece_count_raw`

- value: **7**  (from `identifier_glue.max_identifier_piece_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'license_class_uses_index_as_underlying_value', 'raw_piece_count'; {'identifier': 'LicensesToUseIndexAsUnderlyingValue', 'raw_piece_count': 7, 'con; {'identifier': 'IndexUnderlyingValueLicenseIssuance', 'raw_piece_count': 5, 'con (+15 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'issuance_of_license_class', 'raw_piece_count': 4, 'content_piece; {'identifier': 'issuance_to_recipient_category', 'raw_piece_count': 4, 'content_; {'identifier': 'license_instance_of_class', 'raw_piece_count': 4, 'content_piece (+10 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `mean_identifier_piece_count_content`

- value: **2.7777777777777777**  (from `identifier_glue.mean_identifier_piece_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'license_class_uses_index_as_underlying_value', 'raw_piece_count'; {'identifier': 'LicensesToUseIndexAsUnderlyingValue', 'raw_piece_count': 7, 'con; {'identifier': 'IndexUnderlyingValueLicenseIssuance', 'raw_piece_count': 5, 'con (+15 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'issuance_of_license_class', 'raw_piece_count': 4, 'content_piece; {'identifier': 'issuance_to_recipient_category', 'raw_piece_count': 4, 'content_; {'identifier': 'license_instance_of_class', 'raw_piece_count': 4, 'content_piece (+10 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `mean_identifier_piece_count_raw`

- value: **3.2222222222222223**  (from `identifier_glue.mean_identifier_piece_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'license_class_uses_index_as_underlying_value', 'raw_piece_count'; {'identifier': 'LicensesToUseIndexAsUnderlyingValue', 'raw_piece_count': 7, 'con; {'identifier': 'IndexUnderlyingValueLicenseIssuance', 'raw_piece_count': 5, 'con (+15 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'issuance_of_license_class', 'raw_piece_count': 4, 'content_piece; {'identifier': 'issuance_to_recipient_category', 'raw_piece_count': 4, 'content_; {'identifier': 'license_instance_of_class', 'raw_piece_count': 4, 'content_piece (+10 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → (empty)

## [WARNING] `ontology_planning` / `new_formula_content_token_count_vs_text_only`

- value: **28**  (from `grounding.new_formula_content_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → bankrecipient; financialcontractuse; financialinstrumentuse (+25 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; bankrecipient; canonical (+45 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'license', 'current_count': 17, 'baseline_count': 0, 'delta': 17}; {'token': 'class', 'current_count': 12, 'baseline_count': 0, 'delta': 12}; {'token': 'category', 'current_count': 9, 'baseline_count': 0, 'delta': 9} (+17 more)
  - `grounding.origin_error_count` → 12

## [WARNING] `ontology_planning` / `new_formula_token_count_vs_text_only`

- value: **29**  (from `grounding.new_formula_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → bankrecipient; financialcontractuse; financialinstrumentuse (+25 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; bankrecipient; canonical (+45 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'license', 'current_count': 17, 'baseline_count': 0, 'delta': 17}; {'token': 'class', 'current_count': 12, 'baseline_count': 0, 'delta': 12}; {'token': 'category', 'current_count': 9, 'baseline_count': 0, 'delta': 9} (+17 more)
  - `grounding.origin_error_count` → 12

## [WARNING] `ontology_planning` / `new_full_surface_content_token_count_vs_text_only`

- value: **48**  (from `grounding.new_full_surface_content_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → bankrecipient; financialcontractuse; financialinstrumentuse (+25 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; bankrecipient; canonical (+45 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'license', 'current_count': 17, 'baseline_count': 0, 'delta': 17}; {'token': 'class', 'current_count': 12, 'baseline_count': 0, 'delta': 12}; {'token': 'category', 'current_count': 9, 'baseline_count': 0, 'delta': 9} (+17 more)
  - `grounding.origin_error_count` → 12

## [WARNING] `ontology_planning` / `new_full_surface_token_count_vs_text_only`

- value: **52**  (from `grounding.new_full_surface_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → bankrecipient; financialcontractuse; financialinstrumentuse (+25 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; bankrecipient; canonical (+45 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'license', 'current_count': 17, 'baseline_count': 0, 'delta': 17}; {'token': 'class', 'current_count': 12, 'baseline_count': 0, 'delta': 12}; {'token': 'category', 'current_count': 9, 'baseline_count': 0, 'delta': 9} (+17 more)
  - `grounding.origin_error_count` → 12

## [WARNING] `ontology_planning` / `new_surface_content_token_count`

- value: **67**  (from `<search recursive metrics JSON for key `new_surface_content_token_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → bankrecipient; financialcontractuse; financialinstrumentuse (+25 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; bankrecipient; canonical (+45 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'license', 'current_count': 17, 'baseline_count': 0, 'delta': 17}; {'token': 'class', 'current_count': 12, 'baseline_count': 0, 'delta': 12}; {'token': 'category', 'current_count': 9, 'baseline_count': 0, 'delta': 9} (+17 more)
  - `grounding.origin_error_count` → 12

## [WARNING] `ontology_planning` / `new_surface_token_count`

- value: **67**  (from `<search recursive metrics JSON for key `new_surface_token_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → bankrecipient; financialcontractuse; financialinstrumentuse (+25 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; bankrecipient; canonical (+45 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'license', 'current_count': 17, 'baseline_count': 0, 'delta': 17}; {'token': 'class', 'current_count': 12, 'baseline_count': 0, 'delta': 12}; {'token': 'category', 'current_count': 9, 'baseline_count': 0, 'delta': 9} (+17 more)
  - `grounding.origin_error_count` → 12

## [WARNING] `ontology_planning` / `ungrounded_sort_count`

- value: **5**  (from `grounding.ungrounded_sort_count`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → bankrecipient; financialcontractuse; financialinstrumentuse (+25 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; bankrecipient; canonical (+45 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'license', 'current_count': 17, 'baseline_count': 0, 'delta': 17}; {'token': 'class', 'current_count': 12, 'baseline_count': 0, 'delta': 12}; {'token': 'category', 'current_count': 9, 'baseline_count': 0, 'delta': 9} (+17 more)
  - `grounding.origin_error_count` → 12

## [WARNING] `ontology_planning` / `ungrounded_symbol_count`

- value: **6**  (from `grounding.ungrounded_symbol_count`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → bankrecipient; financialcontractuse; financialinstrumentuse (+25 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; bankrecipient; canonical (+45 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'license', 'current_count': 17, 'baseline_count': 0, 'delta': 17}; {'token': 'class', 'current_count': 12, 'baseline_count': 0, 'delta': 12}; {'token': 'category', 'current_count': 9, 'baseline_count': 0, 'delta': 9} (+17 more)
  - `grounding.origin_error_count` → 12
