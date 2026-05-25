# Diagnostic report — appendix_8_1

- **gate**: `needs_review`
- fail: 0, warning: 30

## [WARNING] `merge_canonicalization` / `callable_symbol_count`

- value: **5**  (from `parameterization.callable_symbol_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 5
  - `<related section in metrics JSON>` → 5

## [WARNING] `merge_canonicalization` / `callable_symbol_with_args_count`

- value: **5**  (from `parameterization.callable_symbol_with_args_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 5
  - `<related section in metrics JSON>` → 5

## [WARNING] `merge_canonicalization` / `cross_reference_dropout_count`

- value: **2**  (from `<search recursive metrics JSON for key `cross_reference_dropout_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `evidence.source_cross_references` → Appendix 8
  - `evidence.ir_cross_references` → (empty)

## [WARNING] `merge_canonicalization` / `draft_variant_count`

- value: **1**  (from `variants.draft_variant_count`)
- meaning: A merge/variant/gold comparison changed structure or semantics; report exact compared variants or merge rows.
- repair: Use overlay/bridge/conflict split or reject rewrite based on backtest.

## [WARNING] `merge_canonicalization` / `factorization_count`

- value: **5**  (from `parameterization.factorization_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 5
  - `<related section in metrics JSON>` → 5

## [WARNING] `merge_canonicalization` / `focus_signature_unique_count`

- value: **1**  (from `variability.focus_signature_unique_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.

## [WARNING] `merge_canonicalization` / `top_level_parameter_slot_count`

- value: **7**  (from `parameterization.top_level_parameter_slot_count`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `<same JSON key as metric name when present>` → 7
  - `<related section in metrics JSON>` → 7

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

- value: **222**  (from `identifier_glue.compound_identifier_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'RbicsNameAltEnergyMotorHomesAndCampersRvsMakers', 'raw_piece_cou; {'identifier': 'RbicsNameMiddleEastAndAfricaMixedAltWholesalePower', 'raw_piece_; {'identifier': 'RbicsNameAltEnergyAutonomousHeavyDutyTruckMakers', 'raw_piece_co (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'rbics_classifies_subindustry', 'raw_piece_count': 3, 'content_pi; {'identifier': 'RbicsSubindustry', 'raw_piece_count': 2, 'content_piece_count': ; {'identifier': 'RbicsSubindustry101025153010', 'raw_piece_count': 2, 'content_pi (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'RbicsNameCarbonCaptureServicesAndTechnologies', 'raw_piece_count

## [WARNING] `ontology_planning` / `compound_identifier_count_raw`

- value: **109**  (from `identifier_glue.compound_identifier_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'RbicsNameAltEnergyMotorHomesAndCampersRvsMakers', 'raw_piece_cou; {'identifier': 'RbicsNameMiddleEastAndAfricaMixedAltWholesalePower', 'raw_piece_; {'identifier': 'RbicsNameAltEnergyAutonomousHeavyDutyTruckMakers', 'raw_piece_co (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'rbics_classifies_subindustry', 'raw_piece_count': 3, 'content_pi; {'identifier': 'RbicsSubindustry', 'raw_piece_count': 2, 'content_piece_count': ; {'identifier': 'RbicsSubindustry101025153010', 'raw_piece_count': 2, 'content_pi (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'RbicsNameCarbonCaptureServicesAndTechnologies', 'raw_piece_count

## [WARNING] `ontology_planning` / `cross_reference_dropout_count`

- value: **2**  (from `<search recursive metrics JSON for key `cross_reference_dropout_count`>`)
- meaning: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair: Inspect relevant artifacts and apply module-specific repair rules.
- evidence:
  - `evidence.source_cross_references` → Appendix 8
  - `evidence.ir_cross_references` → (empty)

## [WARNING] `ontology_planning` / `identifier_count`

- value: **334**  (from `identifier_glue.identifier_count`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'RbicsNameAltEnergyMotorHomesAndCampersRvsMakers', 'raw_piece_cou; {'identifier': 'RbicsNameMiddleEastAndAfricaMixedAltWholesalePower', 'raw_piece_; {'identifier': 'RbicsNameAltEnergyAutonomousHeavyDutyTruckMakers', 'raw_piece_co (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'rbics_classifies_subindustry', 'raw_piece_count': 3, 'content_pi; {'identifier': 'RbicsSubindustry', 'raw_piece_count': 2, 'content_piece_count': ; {'identifier': 'RbicsSubindustry101025153010', 'raw_piece_count': 2, 'content_pi (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'RbicsNameCarbonCaptureServicesAndTechnologies', 'raw_piece_count

## [WARNING] `ontology_planning` / `identifier_glue_excess_mass_content`

- value: **617**  (from `identifier_glue.identifier_glue_excess_mass_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'RbicsNameAltEnergyMotorHomesAndCampersRvsMakers', 'raw_piece_cou; {'identifier': 'RbicsNameMiddleEastAndAfricaMixedAltWholesalePower', 'raw_piece_; {'identifier': 'RbicsNameAltEnergyAutonomousHeavyDutyTruckMakers', 'raw_piece_co (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'rbics_classifies_subindustry', 'raw_piece_count': 3, 'content_pi; {'identifier': 'RbicsSubindustry', 'raw_piece_count': 2, 'content_piece_count': ; {'identifier': 'RbicsSubindustry101025153010', 'raw_piece_count': 2, 'content_pi (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'RbicsNameCarbonCaptureServicesAndTechnologies', 'raw_piece_count

## [WARNING] `ontology_planning` / `identifier_glue_excess_mass_raw`

- value: **414**  (from `identifier_glue.identifier_glue_excess_mass_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'RbicsNameAltEnergyMotorHomesAndCampersRvsMakers', 'raw_piece_cou; {'identifier': 'RbicsNameMiddleEastAndAfricaMixedAltWholesalePower', 'raw_piece_; {'identifier': 'RbicsNameAltEnergyAutonomousHeavyDutyTruckMakers', 'raw_piece_co (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'rbics_classifies_subindustry', 'raw_piece_count': 3, 'content_pi; {'identifier': 'RbicsSubindustry', 'raw_piece_count': 2, 'content_piece_count': ; {'identifier': 'RbicsSubindustry101025153010', 'raw_piece_count': 2, 'content_pi (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'RbicsNameCarbonCaptureServicesAndTechnologies', 'raw_piece_count

## [WARNING] `ontology_planning` / `low_source_grounded_glued_identifier_count`

- value: **116**  (from `identifier_glue.low_source_grounded_glued_identifier_count`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'RbicsNameAltEnergyMotorHomesAndCampersRvsMakers', 'raw_piece_cou; {'identifier': 'RbicsNameMiddleEastAndAfricaMixedAltWholesalePower', 'raw_piece_; {'identifier': 'RbicsNameAltEnergyAutonomousHeavyDutyTruckMakers', 'raw_piece_co (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'rbics_classifies_subindustry', 'raw_piece_count': 3, 'content_pi; {'identifier': 'RbicsSubindustry', 'raw_piece_count': 2, 'content_piece_count': ; {'identifier': 'RbicsSubindustry101025153010', 'raw_piece_count': 2, 'content_pi (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'RbicsNameCarbonCaptureServicesAndTechnologies', 'raw_piece_count

## [WARNING] `ontology_planning` / `max_identifier_piece_count_content`

- value: **9**  (from `identifier_glue.max_identifier_piece_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'RbicsNameAltEnergyMotorHomesAndCampersRvsMakers', 'raw_piece_cou; {'identifier': 'RbicsNameMiddleEastAndAfricaMixedAltWholesalePower', 'raw_piece_; {'identifier': 'RbicsNameAltEnergyAutonomousHeavyDutyTruckMakers', 'raw_piece_co (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'rbics_classifies_subindustry', 'raw_piece_count': 3, 'content_pi; {'identifier': 'RbicsSubindustry', 'raw_piece_count': 2, 'content_piece_count': ; {'identifier': 'RbicsSubindustry101025153010', 'raw_piece_count': 2, 'content_pi (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'RbicsNameCarbonCaptureServicesAndTechnologies', 'raw_piece_count

## [WARNING] `ontology_planning` / `max_identifier_piece_count_raw`

- value: **10**  (from `identifier_glue.max_identifier_piece_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'RbicsNameAltEnergyMotorHomesAndCampersRvsMakers', 'raw_piece_cou; {'identifier': 'RbicsNameMiddleEastAndAfricaMixedAltWholesalePower', 'raw_piece_; {'identifier': 'RbicsNameAltEnergyAutonomousHeavyDutyTruckMakers', 'raw_piece_co (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'rbics_classifies_subindustry', 'raw_piece_count': 3, 'content_pi; {'identifier': 'RbicsSubindustry', 'raw_piece_count': 2, 'content_piece_count': ; {'identifier': 'RbicsSubindustry101025153010', 'raw_piece_count': 2, 'content_pi (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'RbicsNameCarbonCaptureServicesAndTechnologies', 'raw_piece_count

## [WARNING] `ontology_planning` / `mean_identifier_piece_count_content`

- value: **3.838323353293413**  (from `identifier_glue.mean_identifier_piece_count_content`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'RbicsNameAltEnergyMotorHomesAndCampersRvsMakers', 'raw_piece_cou; {'identifier': 'RbicsNameMiddleEastAndAfricaMixedAltWholesalePower', 'raw_piece_; {'identifier': 'RbicsNameAltEnergyAutonomousHeavyDutyTruckMakers', 'raw_piece_co (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'rbics_classifies_subindustry', 'raw_piece_count': 3, 'content_pi; {'identifier': 'RbicsSubindustry', 'raw_piece_count': 2, 'content_piece_count': ; {'identifier': 'RbicsSubindustry101025153010', 'raw_piece_count': 2, 'content_pi (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'RbicsNameCarbonCaptureServicesAndTechnologies', 'raw_piece_count

## [WARNING] `ontology_planning` / `mean_identifier_piece_count_raw`

- value: **3.895209580838323**  (from `identifier_glue.mean_identifier_piece_count_raw`)
- meaning: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair: Split long identifiers into anchored functions/relations/ontology links.
- evidence:
  - `identifier_glue.top_glued_identifiers` → {'identifier': 'RbicsNameAltEnergyMotorHomesAndCampersRvsMakers', 'raw_piece_cou; {'identifier': 'RbicsNameMiddleEastAndAfricaMixedAltWholesalePower', 'raw_piece_; {'identifier': 'RbicsNameAltEnergyAutonomousHeavyDutyTruckMakers', 'raw_piece_co (+17 more)
  - `identifier_glue.lowest_source_grounded_identifiers` → {'identifier': 'rbics_classifies_subindustry', 'raw_piece_count': 3, 'content_pi; {'identifier': 'RbicsSubindustry', 'raw_piece_count': 2, 'content_piece_count': ; {'identifier': 'RbicsSubindustry101025153010', 'raw_piece_count': 2, 'content_pi (+17 more)
  - `identifier_glue.conditional_relation_name_packing_examples` → (empty)
  - `identifier_glue.entity_relation_target_fusion_examples` → {'identifier': 'RbicsNameCarbonCaptureServicesAndTechnologies', 'raw_piece_count

## [WARNING] `ontology_planning` / `new_formula_content_token_count_vs_text_only`

- value: **445**  (from `grounding.new_formula_content_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → appendix8; appendix_includes_rbics_subindustry; rbics_classification_level (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; appendix8; appendix_includes_rbics_subindustry (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'rbicssubindustry', 'current_count': 114, 'baseline_count': 0, 'delta'; {'token': 'appendix', 'current_count': 112, 'baseline_count': 2, 'delta': 110}; {'token': 'rbicsnumbercode', 'current_count': 110, 'baseline_count': 0, 'delta': (+17 more)
  - `grounding.origin_error_count` → 113

## [WARNING] `ontology_planning` / `new_formula_token_count_vs_text_only`

- value: **445**  (from `grounding.new_formula_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → appendix8; appendix_includes_rbics_subindustry; rbics_classification_level (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; appendix8; appendix_includes_rbics_subindustry (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'rbicssubindustry', 'current_count': 114, 'baseline_count': 0, 'delta'; {'token': 'appendix', 'current_count': 112, 'baseline_count': 2, 'delta': 110}; {'token': 'rbicsnumbercode', 'current_count': 110, 'baseline_count': 0, 'delta': (+17 more)
  - `grounding.origin_error_count` → 113

## [WARNING] `ontology_planning` / `new_full_surface_content_token_count_vs_text_only`

- value: **465**  (from `grounding.new_full_surface_content_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → appendix8; appendix_includes_rbics_subindustry; rbics_classification_level (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; appendix8; appendix_includes_rbics_subindustry (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'rbicssubindustry', 'current_count': 114, 'baseline_count': 0, 'delta'; {'token': 'appendix', 'current_count': 112, 'baseline_count': 2, 'delta': 110}; {'token': 'rbicsnumbercode', 'current_count': 110, 'baseline_count': 0, 'delta': (+17 more)
  - `grounding.origin_error_count` → 113

## [WARNING] `ontology_planning` / `new_full_surface_token_count_vs_text_only`

- value: **469**  (from `grounding.new_full_surface_token_count_vs_text_only`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → appendix8; appendix_includes_rbics_subindustry; rbics_classification_level (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; appendix8; appendix_includes_rbics_subindustry (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'rbicssubindustry', 'current_count': 114, 'baseline_count': 0, 'delta'; {'token': 'appendix', 'current_count': 112, 'baseline_count': 2, 'delta': 110}; {'token': 'rbicsnumbercode', 'current_count': 110, 'baseline_count': 0, 'delta': (+17 more)
  - `grounding.origin_error_count` → 113

## [WARNING] `ontology_planning` / `new_surface_content_token_count`

- value: **1831**  (from `<search recursive metrics JSON for key `new_surface_content_token_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → appendix8; appendix_includes_rbics_subindustry; rbics_classification_level (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; appendix8; appendix_includes_rbics_subindustry (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'rbicssubindustry', 'current_count': 114, 'baseline_count': 0, 'delta'; {'token': 'appendix', 'current_count': 112, 'baseline_count': 2, 'delta': 110}; {'token': 'rbicsnumbercode', 'current_count': 110, 'baseline_count': 0, 'delta': (+17 more)
  - `grounding.origin_error_count` → 113

## [WARNING] `ontology_planning` / `new_surface_token_count`

- value: **1831**  (from `<search recursive metrics JSON for key `new_surface_token_count`>`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → appendix8; appendix_includes_rbics_subindustry; rbics_classification_level (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; appendix8; appendix_includes_rbics_subindustry (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'rbicssubindustry', 'current_count': 114, 'baseline_count': 0, 'delta'; {'token': 'appendix', 'current_count': 112, 'baseline_count': 2, 'delta': 110}; {'token': 'rbicsnumbercode', 'current_count': 110, 'baseline_count': 0, 'delta': (+17 more)
  - `grounding.origin_error_count` → 113

## [WARNING] `ontology_planning` / `ungrounded_sort_count`

- value: **1**  (from `grounding.ungrounded_sort_count`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → appendix8; appendix_includes_rbics_subindustry; rbics_classification_level (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; appendix8; appendix_includes_rbics_subindustry (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'rbicssubindustry', 'current_count': 114, 'baseline_count': 0, 'delta'; {'token': 'appendix', 'current_count': 112, 'baseline_count': 2, 'delta': 110}; {'token': 'rbicsnumbercode', 'current_count': 110, 'baseline_count': 0, 'delta': (+17 more)
  - `grounding.origin_error_count` → 113

## [WARNING] `ontology_planning` / `ungrounded_symbol_count`

- value: **2**  (from `grounding.ungrounded_symbol_count`)
- meaning: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- evidence:
  - `grounding.new_formula_content_tokens_vs_text_only` → appendix8; appendix_includes_rbics_subindustry; rbics_classification_level (+47 more)
  - `grounding.new_full_surface_content_tokens_vs_text_only` → a4v3; appendix8; appendix_includes_rbics_subindustry (+47 more)
  - `lexical_coverage.formula_repeat_overuse_examples` → {'token': 'rbicssubindustry', 'current_count': 114, 'baseline_count': 0, 'delta'; {'token': 'appendix', 'current_count': 112, 'baseline_count': 2, 'delta': 110}; {'token': 'rbicsnumbercode', 'current_count': 110, 'baseline_count': 0, 'delta': (+17 more)
  - `grounding.origin_error_count` → 113
