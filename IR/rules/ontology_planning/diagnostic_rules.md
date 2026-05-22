# Diagnostic Rules: ontology_planning

- metric_count: `44`
- check_count: `20`
- rule_count: `64`

## `advisory_grounded_content_piece_ratio_mean`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `identifier_glue.advisory_grounded_content_piece_ratio_mean`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `advisory_only_symbol_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `advisory_only_symbol_count`>`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `arg_arity_stability`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `arg_arity_stability`>`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `carrier_choice_stability`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `carrier_choice_stability`>`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `compound_identifier_count_content`

- type: `metric`
- bad value means: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair target: Split long identifiers into anchored functions/relations/ontology links.
- value paths:
  - `identifier_glue.compound_identifier_count_content`
- evidence paths:
  - `identifier_glue.top_glued_identifiers`
  - `identifier_glue.lowest_source_grounded_identifiers`
  - `identifier_glue.conditional_relation_name_packing_examples`
  - `identifier_glue.entity_relation_target_fusion_examples`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `compound_identifier_count_raw`

- type: `metric`
- bad value means: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair target: Split long identifiers into anchored functions/relations/ontology links.
- value paths:
  - `identifier_glue.compound_identifier_count_raw`
- evidence paths:
  - `identifier_glue.top_glued_identifiers`
  - `identifier_glue.lowest_source_grounded_identifiers`
  - `identifier_glue.conditional_relation_name_packing_examples`
  - `identifier_glue.entity_relation_target_fusion_examples`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `compound_identifier_rate_content`

- type: `metric`
- bad value means: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair target: Split long identifiers into anchored functions/relations/ontology links.
- value paths:
  - `identifier_glue.compound_identifier_rate_content`
- evidence paths:
  - `identifier_glue.top_glued_identifiers`
  - `identifier_glue.lowest_source_grounded_identifiers`
  - `identifier_glue.conditional_relation_name_packing_examples`
  - `identifier_glue.entity_relation_target_fusion_examples`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `compound_identifier_rate_raw`

- type: `metric`
- bad value means: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair target: Split long identifiers into anchored functions/relations/ontology links.
- value paths:
  - `identifier_glue.compound_identifier_rate_raw`
- evidence paths:
  - `identifier_glue.top_glued_identifiers`
  - `identifier_glue.lowest_source_grounded_identifiers`
  - `identifier_glue.conditional_relation_name_packing_examples`
  - `identifier_glue.entity_relation_target_fusion_examples`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `cross_reference_dropout_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `cross_reference_dropout_count`>`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `cross_reference_usage_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `cross_reference_usage_count`>`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `dependency_link_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `dependency_link_count`>`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `dependency_link_recall`

- type: `metric`
- bad value means: Some source/normalized content is absent from the target representation; report the missing token/fragment list.
- repair target: Add the missing concepts as explicit formula structure, or document why they are intentionally excluded.
- value paths:
  - `<search recursive metrics JSON for key `dependency_link_recall`>`
- evidence paths:
  - `lexical_coverage.source_content_tokens_missing_from_formula`
  - `lexical_coverage.source_content_tokens_missing_from_full_surface`
  - `lexical_coverage.formula_repeat_underuse_mass`
  - `coverage.missing_fragment_count`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `embedded_concept_without_formula_link_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `embedded_concept_without_formula_link_count`>`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `explicit_link_violation_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `semantic_preservation.explicit_link_violation_count`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `identifier_count`

- type: `metric`
- bad value means: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair target: Split long identifiers into anchored functions/relations/ontology links.
- value paths:
  - `identifier_glue.identifier_count`
- evidence paths:
  - `identifier_glue.top_glued_identifiers`
  - `identifier_glue.lowest_source_grounded_identifiers`
  - `identifier_glue.conditional_relation_name_packing_examples`
  - `identifier_glue.entity_relation_target_fusion_examples`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `identifier_glue_excess_mass_content`

- type: `metric`
- bad value means: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair target: Split long identifiers into anchored functions/relations/ontology links.
- value paths:
  - `identifier_glue.identifier_glue_excess_mass_content`
- evidence paths:
  - `identifier_glue.top_glued_identifiers`
  - `identifier_glue.lowest_source_grounded_identifiers`
  - `identifier_glue.conditional_relation_name_packing_examples`
  - `identifier_glue.entity_relation_target_fusion_examples`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `identifier_glue_excess_mass_raw`

- type: `metric`
- bad value means: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair target: Split long identifiers into anchored functions/relations/ontology links.
- value paths:
  - `identifier_glue.identifier_glue_excess_mass_raw`
- evidence paths:
  - `identifier_glue.top_glued_identifiers`
  - `identifier_glue.lowest_source_grounded_identifiers`
  - `identifier_glue.conditional_relation_name_packing_examples`
  - `identifier_glue.entity_relation_target_fusion_examples`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `identifier_glue_excess_rate_content`

- type: `metric`
- bad value means: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair target: Split long identifiers into anchored functions/relations/ontology links.
- value paths:
  - `identifier_glue.identifier_glue_excess_rate_content`
- evidence paths:
  - `identifier_glue.top_glued_identifiers`
  - `identifier_glue.lowest_source_grounded_identifiers`
  - `identifier_glue.conditional_relation_name_packing_examples`
  - `identifier_glue.entity_relation_target_fusion_examples`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `identifier_glue_excess_rate_raw`

- type: `metric`
- bad value means: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair target: Split long identifiers into anchored functions/relations/ontology links.
- value paths:
  - `identifier_glue.identifier_glue_excess_rate_raw`
- evidence paths:
  - `identifier_glue.top_glued_identifiers`
  - `identifier_glue.lowest_source_grounded_identifiers`
  - `identifier_glue.conditional_relation_name_packing_examples`
  - `identifier_glue.entity_relation_target_fusion_examples`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `invented_helper_sort_count`

- type: `metric`
- bad value means: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair target: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- value paths:
  - `<search recursive metrics JSON for key `invented_helper_sort_count`>`
- evidence paths:
  - `grounding.new_formula_content_tokens_vs_text_only`
  - `grounding.new_full_surface_content_tokens_vs_text_only`
  - `lexical_coverage.formula_repeat_overuse_examples`
  - `grounding.origin_error_count`
  - `identifier_glue.top_glued_identifiers`
  - `identifier_glue.lowest_source_grounded_identifiers`
  - `identifier_glue.conditional_relation_name_packing_examples`
  - `identifier_glue.entity_relation_target_fusion_examples`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `invented_helper_symbol_count`

- type: `metric`
- bad value means: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair target: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- value paths:
  - `<search recursive metrics JSON for key `invented_helper_symbol_count`>`
- evidence paths:
  - `grounding.new_formula_content_tokens_vs_text_only`
  - `grounding.new_full_surface_content_tokens_vs_text_only`
  - `lexical_coverage.formula_repeat_overuse_examples`
  - `grounding.origin_error_count`
  - `identifier_glue.top_glued_identifiers`
  - `identifier_glue.lowest_source_grounded_identifiers`
  - `identifier_glue.conditional_relation_name_packing_examples`
  - `identifier_glue.entity_relation_target_fusion_examples`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `low_source_grounded_glued_identifier_count`

- type: `metric`
- bad value means: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair target: Split long identifiers into anchored functions/relations/ontology links.
- value paths:
  - `identifier_glue.low_source_grounded_glued_identifier_count`
- evidence paths:
  - `identifier_glue.top_glued_identifiers`
  - `identifier_glue.lowest_source_grounded_identifiers`
  - `identifier_glue.conditional_relation_name_packing_examples`
  - `identifier_glue.entity_relation_target_fusion_examples`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `low_source_grounded_glued_identifier_rate`

- type: `metric`
- bad value means: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair target: Split long identifiers into anchored functions/relations/ontology links.
- value paths:
  - `identifier_glue.low_source_grounded_glued_identifier_rate`
- evidence paths:
  - `identifier_glue.top_glued_identifiers`
  - `identifier_glue.lowest_source_grounded_identifiers`
  - `identifier_glue.conditional_relation_name_packing_examples`
  - `identifier_glue.entity_relation_target_fusion_examples`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `lowest_source_grounded_identifiers`

- type: `metric`
- bad value means: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair target: Split long identifiers into anchored functions/relations/ontology links.
- value paths:
  - `identifier_glue.lowest_source_grounded_identifiers`
  - `identifier_glue.lowest_source_grounded_identifiers[0]`
  - `identifier_glue.lowest_source_grounded_identifiers[1]`
  - `identifier_glue.lowest_source_grounded_identifiers[2]`
  - `identifier_glue.lowest_source_grounded_identifiers[3]`
  - `identifier_glue.lowest_source_grounded_identifiers[4]`
- evidence paths:
  - `identifier_glue.top_glued_identifiers`
  - `identifier_glue.lowest_source_grounded_identifiers`
  - `identifier_glue.conditional_relation_name_packing_examples`
  - `identifier_glue.entity_relation_target_fusion_examples`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `max_identifier_piece_count_content`

- type: `metric`
- bad value means: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair target: Split long identifiers into anchored functions/relations/ontology links.
- value paths:
  - `identifier_glue.max_identifier_piece_count_content`
- evidence paths:
  - `identifier_glue.top_glued_identifiers`
  - `identifier_glue.lowest_source_grounded_identifiers`
  - `identifier_glue.conditional_relation_name_packing_examples`
  - `identifier_glue.entity_relation_target_fusion_examples`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `max_identifier_piece_count_raw`

- type: `metric`
- bad value means: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair target: Split long identifiers into anchored functions/relations/ontology links.
- value paths:
  - `identifier_glue.max_identifier_piece_count_raw`
- evidence paths:
  - `identifier_glue.top_glued_identifiers`
  - `identifier_glue.lowest_source_grounded_identifiers`
  - `identifier_glue.conditional_relation_name_packing_examples`
  - `identifier_glue.entity_relation_target_fusion_examples`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `mean_identifier_piece_count_content`

- type: `metric`
- bad value means: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair target: Split long identifiers into anchored functions/relations/ontology links.
- value paths:
  - `identifier_glue.mean_identifier_piece_count_content`
- evidence paths:
  - `identifier_glue.top_glued_identifiers`
  - `identifier_glue.lowest_source_grounded_identifiers`
  - `identifier_glue.conditional_relation_name_packing_examples`
  - `identifier_glue.entity_relation_target_fusion_examples`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `mean_identifier_piece_count_raw`

- type: `metric`
- bad value means: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair target: Split long identifiers into anchored functions/relations/ontology links.
- value paths:
  - `identifier_glue.mean_identifier_piece_count_raw`
- evidence paths:
  - `identifier_glue.top_glued_identifiers`
  - `identifier_glue.lowest_source_grounded_identifiers`
  - `identifier_glue.conditional_relation_name_packing_examples`
  - `identifier_glue.entity_relation_target_fusion_examples`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `new_formula_content_token_count_vs_text_only`

- type: `metric`
- bad value means: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair target: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- value paths:
  - `grounding.new_formula_content_token_count_vs_text_only`
- evidence paths:
  - `grounding.new_formula_content_tokens_vs_text_only`
  - `grounding.new_full_surface_content_tokens_vs_text_only`
  - `lexical_coverage.formula_repeat_overuse_examples`
  - `grounding.origin_error_count`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `new_formula_token_count_vs_text_only`

- type: `metric`
- bad value means: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair target: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- value paths:
  - `grounding.new_formula_token_count_vs_text_only`
- evidence paths:
  - `grounding.new_formula_content_tokens_vs_text_only`
  - `grounding.new_full_surface_content_tokens_vs_text_only`
  - `lexical_coverage.formula_repeat_overuse_examples`
  - `grounding.origin_error_count`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `new_full_surface_content_token_count_vs_text_only`

- type: `metric`
- bad value means: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair target: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- value paths:
  - `grounding.new_full_surface_content_token_count_vs_text_only`
- evidence paths:
  - `grounding.new_formula_content_tokens_vs_text_only`
  - `grounding.new_full_surface_content_tokens_vs_text_only`
  - `lexical_coverage.formula_repeat_overuse_examples`
  - `grounding.origin_error_count`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `new_full_surface_token_count_vs_text_only`

- type: `metric`
- bad value means: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair target: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- value paths:
  - `grounding.new_full_surface_token_count_vs_text_only`
- evidence paths:
  - `grounding.new_formula_content_tokens_vs_text_only`
  - `grounding.new_full_surface_content_tokens_vs_text_only`
  - `lexical_coverage.formula_repeat_overuse_examples`
  - `grounding.origin_error_count`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `new_surface_content_token_count`

- type: `metric`
- bad value means: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair target: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- value paths:
  - `<search recursive metrics JSON for key `new_surface_content_token_count`>`
- evidence paths:
  - `grounding.new_formula_content_tokens_vs_text_only`
  - `grounding.new_full_surface_content_tokens_vs_text_only`
  - `lexical_coverage.formula_repeat_overuse_examples`
  - `grounding.origin_error_count`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `new_surface_token_count`

- type: `metric`
- bad value means: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair target: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- value paths:
  - `<search recursive metrics JSON for key `new_surface_token_count`>`
- evidence paths:
  - `grounding.new_formula_content_tokens_vs_text_only`
  - `grounding.new_full_surface_content_tokens_vs_text_only`
  - `lexical_coverage.formula_repeat_overuse_examples`
  - `grounding.origin_error_count`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `prelude_redeclaration_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `grounding.prelude_redeclaration_count`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `prelude_symbol_ratio`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `prelude_symbol_ratio`>`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `sort_choice_stability`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `sort_choice_stability`>`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `source_grounded_content_piece_ratio_mean`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `identifier_glue.source_grounded_content_piece_ratio_mean`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `text_licensed_symbol_ratio`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `text_licensed_symbol_ratio`>`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `top_glued_identifiers`

- type: `metric`
- bad value means: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair target: Split long identifiers into anchored functions/relations/ontology links.
- value paths:
  - `identifier_glue.top_glued_identifiers`
  - `identifier_glue.top_glued_identifiers[0]`
  - `identifier_glue.top_glued_identifiers[1]`
  - `identifier_glue.top_glued_identifiers[2]`
  - `identifier_glue.top_glued_identifiers[3]`
  - `identifier_glue.top_glued_identifiers[4]`
- evidence paths:
  - `identifier_glue.top_glued_identifiers`
  - `identifier_glue.lowest_source_grounded_identifiers`
  - `identifier_glue.conditional_relation_name_packing_examples`
  - `identifier_glue.entity_relation_target_fusion_examples`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `ungrounded_callee_count`

- type: `metric`
- bad value means: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair target: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- value paths:
  - `grounding.ungrounded_callee_count`
- evidence paths:
  - `grounding.new_formula_content_tokens_vs_text_only`
  - `grounding.new_full_surface_content_tokens_vs_text_only`
  - `lexical_coverage.formula_repeat_overuse_examples`
  - `grounding.origin_error_count`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `ungrounded_ref_count`

- type: `metric`
- bad value means: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair target: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- value paths:
  - `grounding.ungrounded_ref_count`
- evidence paths:
  - `grounding.new_formula_content_tokens_vs_text_only`
  - `grounding.new_full_surface_content_tokens_vs_text_only`
  - `lexical_coverage.formula_repeat_overuse_examples`
  - `grounding.origin_error_count`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `ungrounded_sort_count`

- type: `metric`
- bad value means: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair target: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- value paths:
  - `grounding.ungrounded_sort_count`
- evidence paths:
  - `grounding.new_formula_content_tokens_vs_text_only`
  - `grounding.new_full_surface_content_tokens_vs_text_only`
  - `lexical_coverage.formula_repeat_overuse_examples`
  - `grounding.origin_error_count`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `ungrounded_symbol_count`

- type: `metric`
- bad value means: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair target: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- value paths:
  - `grounding.ungrounded_symbol_count`
- evidence paths:
  - `grounding.new_formula_content_tokens_vs_text_only`
  - `grounding.new_full_surface_content_tokens_vs_text_only`
  - `lexical_coverage.formula_repeat_overuse_examples`
  - `grounding.origin_error_count`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `identifier_structural_anchor_gap`

- type: `check`
- bad value means: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair target: Split long identifiers into anchored functions/relations/ontology links.
- value paths:
  - `<check output, lint report, checklist result, or generated diagnostic finding>`
- evidence paths:
  - `symbol`
  - `kind`
  - `signature`
  - `identifier pieces`
  - `line_no`
  - `matched_source_phrases`
- diagnostic output must include:
  - check name
  - severity
  - exact row/code that fired
  - source path and target path when available
  - symbol/token/line number when available

## `same_symbol_different_codomains`

- type: `check`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<check output, lint report, checklist result, or generated diagnostic finding>`
- evidence paths:
  - `<check-specific rows in checklist/lint/judge output>`
- diagnostic output must include:
  - check name
  - severity
  - exact row/code that fired
  - source path and target path when available
  - symbol/token/line number when available

## `ontology_level_mixing`

- type: `check`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<check output, lint report, checklist result, or generated diagnostic finding>`
- evidence paths:
  - `<check-specific rows in checklist/lint/judge output>`
- diagnostic output must include:
  - check name
  - severity
  - exact row/code that fired
  - source path and target path when available
  - symbol/token/line number when available

## `enum_value_mapping_candidates`

- type: `check`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<check output, lint report, checklist result, or generated diagnostic finding>`
- evidence paths:
  - `<check-specific rows in checklist/lint/judge output>`
- diagnostic output must include:
  - check name
  - severity
  - exact row/code that fired
  - source path and target path when available
  - symbol/token/line number when available

## `codomain_split_value_families`

- type: `check`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<check output, lint report, checklist result, or generated diagnostic finding>`
- evidence paths:
  - `<check-specific rows in checklist/lint/judge output>`
- diagnostic output must include:
  - check name
  - severity
  - exact row/code that fired
  - source path and target path when available
  - symbol/token/line number when available

## `overlay_consistency_drift`

- type: `check`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<check output, lint report, checklist result, or generated diagnostic finding>`
- evidence paths:
  - `overlay row`
  - `local symbol rows`
  - `backtest metrics`
- diagnostic output must include:
  - check name
  - severity
  - exact row/code that fired
  - source path and target path when available
  - symbol/token/line number when available

## `semantic_load_in_name`

- type: `check`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<check output, lint report, checklist result, or generated diagnostic finding>`
- evidence paths:
  - `symbol`
  - `kind`
  - `signature`
  - `identifier pieces`
  - `line_no`
  - `matched_source_phrases`
- diagnostic output must include:
  - check name
  - severity
  - exact row/code that fired
  - source path and target path when available
  - symbol/token/line number when available

## `opaque_helper_predicates`

- type: `check`
- bad value means: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair target: Split long identifiers into anchored functions/relations/ontology links.
- value paths:
  - `<check output, lint report, checklist result, or generated diagnostic finding>`
- evidence paths:
  - `symbol`
  - `kind`
  - `signature`
  - `identifier pieces`
  - `line_no`
  - `matched_source_phrases`
- diagnostic output must include:
  - check name
  - severity
  - exact row/code that fired
  - source path and target path when available
  - symbol/token/line number when available

## `numeric_window_fusion_forbidden`

- type: `check`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<check output, lint report, checklist result, or generated diagnostic finding>`
- evidence paths:
  - `<check-specific rows in checklist/lint/judge output>`
- diagnostic output must include:
  - check name
  - severity
  - exact row/code that fired
  - source path and target path when available
  - symbol/token/line number when available

## `identifier_source_lexical_crosslink_gap`

- type: `check`
- bad value means: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair target: Split long identifiers into anchored functions/relations/ontology links.
- value paths:
  - `<check output, lint report, checklist result, or generated diagnostic finding>`
- evidence paths:
  - `missing token list`
  - `new token list`
  - `source.md`
  - `normalized.md`
- diagnostic output must include:
  - check name
  - severity
  - exact row/code that fired
  - source path and target path when available
  - symbol/token/line number when available

## `identifier_source_lexical_crosslink_candidates`

- type: `check`
- bad value means: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair target: Split long identifiers into anchored functions/relations/ontology links.
- value paths:
  - `<check output, lint report, checklist result, or generated diagnostic finding>`
- evidence paths:
  - `missing token list`
  - `new token list`
  - `source.md`
  - `normalized.md`
- diagnostic output must include:
  - check name
  - severity
  - exact row/code that fired
  - source path and target path when available
  - symbol/token/line number when available

## `source_phrase_identifier_crosslink_gap`

- type: `check`
- bad value means: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair target: Split long identifiers into anchored functions/relations/ontology links.
- value paths:
  - `<check output, lint report, checklist result, or generated diagnostic finding>`
- evidence paths:
  - `symbol`
  - `kind`
  - `signature`
  - `identifier pieces`
  - `line_no`
  - `matched_source_phrases`
- diagnostic output must include:
  - check name
  - severity
  - exact row/code that fired
  - source path and target path when available
  - symbol/token/line number when available

## `source_phrase_identifier_crosslink_candidates`

- type: `check`
- bad value means: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair target: Split long identifiers into anchored functions/relations/ontology links.
- value paths:
  - `<check output, lint report, checklist result, or generated diagnostic finding>`
- evidence paths:
  - `symbol`
  - `kind`
  - `signature`
  - `identifier pieces`
  - `line_no`
  - `matched_source_phrases`
- diagnostic output must include:
  - check name
  - severity
  - exact row/code that fired
  - source path and target path when available
  - symbol/token/line number when available

## `composite_identifier_crosslink_gap`

- type: `check`
- bad value means: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair target: Split long identifiers into anchored functions/relations/ontology links.
- value paths:
  - `<check output, lint report, checklist result, or generated diagnostic finding>`
- evidence paths:
  - `symbol`
  - `kind`
  - `signature`
  - `identifier pieces`
  - `line_no`
  - `matched_source_phrases`
- diagnostic output must include:
  - check name
  - severity
  - exact row/code that fired
  - source path and target path when available
  - symbol/token/line number when available

## `composite_identifier_crosslink_candidates`

- type: `check`
- bad value means: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair target: Split long identifiers into anchored functions/relations/ontology links.
- value paths:
  - `<check output, lint report, checklist result, or generated diagnostic finding>`
- evidence paths:
  - `symbol`
  - `kind`
  - `signature`
  - `identifier pieces`
  - `line_no`
  - `matched_source_phrases`
- diagnostic output must include:
  - check name
  - severity
  - exact row/code that fired
  - source path and target path when available
  - symbol/token/line number when available

## `shared_base_phrase_family_candidates`

- type: `check`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<check output, lint report, checklist result, or generated diagnostic finding>`
- evidence paths:
  - `<check-specific rows in checklist/lint/judge output>`
- diagnostic output must include:
  - check name
  - severity
  - exact row/code that fired
  - source path and target path when available
  - symbol/token/line number when available

## `canonical_subterm_reuse_gap`

- type: `check`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<check output, lint report, checklist result, or generated diagnostic finding>`
- evidence paths:
  - `<check-specific rows in checklist/lint/judge output>`
- diagnostic output must include:
  - check name
  - severity
  - exact row/code that fired
  - source path and target path when available
  - symbol/token/line number when available

## `canonical_subterm_reuse_candidates`

- type: `check`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<check output, lint report, checklist result, or generated diagnostic finding>`
- evidence paths:
  - `<check-specific rows in checklist/lint/judge output>`
- diagnostic output must include:
  - check name
  - severity
  - exact row/code that fired
  - source path and target path when available
  - symbol/token/line number when available

## `decomposition_policy_gap`

- type: `check`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<check output, lint report, checklist result, or generated diagnostic finding>`
- evidence paths:
  - `symbol`
  - `kind`
  - `signature`
  - `identifier pieces`
  - `line_no`
  - `matched_source_phrases`
- diagnostic output must include:
  - check name
  - severity
  - exact row/code that fired
  - source path and target path when available
  - symbol/token/line number when available

## `decomposition_policy_candidates`

- type: `check`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<check output, lint report, checklist result, or generated diagnostic finding>`
- evidence paths:
  - `symbol`
  - `kind`
  - `signature`
  - `identifier pieces`
  - `line_no`
  - `matched_source_phrases`
- diagnostic output must include:
  - check name
  - severity
  - exact row/code that fired
  - source path and target path when available
  - symbol/token/line number when available
