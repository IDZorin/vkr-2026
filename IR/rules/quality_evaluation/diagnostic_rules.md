# Diagnostic Rules: quality_evaluation

- metric_count: `243`
- check_count: `46`
- rule_count: `289`

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

## `annotation_node_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `annotation_node_count`>`
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

## `artifact_signature_entropy`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `variability.artifact_signature_entropy`
- evidence paths:
  - `variants`
  - `variability`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `assertion_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `assertion_complexity.assertion_count`
- evidence paths:
  - `assertion_complexity.top_complex_assertions`
  - `assertion_complexity.max_assertion_depth`
  - `assertion_complexity.total_quantifier_count`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `assertion_shape_error_count`

- type: `metric`
- bad value means: The artifact is structurally invalid; report parser/schema/combined validation errors.
- repair target: Fix A4V3 syntax, declarations, references, signatures, or combined theory conflicts.
- value paths:
  - `<search recursive metrics JSON for key `assertion_shape_error_count`>`
- evidence paths:
  - `validity.ast_error_count`
  - `validity.rendering_status`
  - `validity.combined_validation_ok`
  - `assertion_complexity.top_complex_assertions`
  - `assertion_complexity.max_assertion_depth`
  - `assertion_complexity.total_quantifier_count`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `ast_error_count`

- type: `metric`
- bad value means: The artifact is structurally invalid; report parser/schema/combined validation errors.
- repair target: Fix A4V3 syntax, declarations, references, signatures, or combined theory conflicts.
- value paths:
  - `validity.ast_error_count`
- evidence paths:
  - `validity.ast_error_count`
  - `validity.rendering_status`
  - `validity.combined_validation_ok`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `ast_valid`

- type: `metric`
- bad value means: The artifact is structurally invalid; report parser/schema/combined validation errors.
- repair target: Fix A4V3 syntax, declarations, references, signatures, or combined theory conflicts.
- value paths:
  - `validity.ast_valid`
- evidence paths:
  - `validity.ast_error_count`
  - `validity.rendering_status`
  - `validity.combined_validation_ok`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `avg_call_latency_s`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `avg_call_latency_s`>`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `avg_structure_similarity_to_other_successful_runs`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `avg_structure_similarity_to_other_successful_runs`>`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `biconditional_present_when_expected`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `biconditional_present_when_expected`>`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `callable_symbol_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `parameterization.callable_symbol_count`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `callable_symbol_with_args_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `parameterization.callable_symbol_with_args_count`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `candidate_reading_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `variants.candidate_reading_count`
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

## `clarification_loss_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `semantic_preservation.clarification_loss_count`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `clause_coverage_ratio`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `clause_coverage_ratio`>`
- evidence paths:
  - `coverage.normalized_clause_count`
  - `coverage.formula_bearing_item_count`
  - `coverage.missing_fragment_count`
  - `coverage.prose_leak_count`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `clause_overdecomposition_mass`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `normalized_alignment.clause_overdecomposition_mass`
- evidence paths:
  - `coverage.normalized_clause_count`
  - `coverage.formula_bearing_item_count`
  - `coverage.missing_fragment_count`
  - `coverage.prose_leak_count`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `clause_to_logic_block_ratio`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `normalized_alignment.clause_to_logic_block_ratio`
- evidence paths:
  - `coverage.normalized_clause_count`
  - `coverage.formula_bearing_item_count`
  - `coverage.missing_fragment_count`
  - `coverage.prose_leak_count`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `clause_underdecomposition_mass`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `normalized_alignment.clause_underdecomposition_mass`
- evidence paths:
  - `coverage.normalized_clause_count`
  - `coverage.formula_bearing_item_count`
  - `coverage.missing_fragment_count`
  - `coverage.prose_leak_count`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `combined_validation_ok`

- type: `metric`
- bad value means: The artifact is structurally invalid; report parser/schema/combined validation errors.
- repair target: Fix A4V3 syntax, declarations, references, signatures, or combined theory conflicts.
- value paths:
  - `validity.combined_validation_ok`
- evidence paths:
  - `validity.ast_error_count`
  - `validity.rendering_status`
  - `validity.combined_validation_ok`
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

## `consensus_margin`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `consensus_margin`>`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `consensus_sample_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `consensus_sample_count`>`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `content_token_jaccard`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `content_token_jaccard`>`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `content_token_multiset_precision`

- type: `metric`
- bad value means: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair target: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- value paths:
  - `<search recursive metrics JSON for key `content_token_multiset_precision`>`
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

## `content_token_multiset_recall`

- type: `metric`
- bad value means: Some source/normalized content is absent from the target representation; report the missing token/fragment list.
- repair target: Add the missing concepts as explicit formula structure, or document why they are intentionally excluded.
- value paths:
  - `<search recursive metrics JSON for key `content_token_multiset_recall`>`
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

## `content_token_precision`

- type: `metric`
- bad value means: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair target: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- value paths:
  - `<search recursive metrics JSON for key `content_token_precision`>`
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

## `content_token_recall`

- type: `metric`
- bad value means: Some source/normalized content is absent from the target representation; report the missing token/fragment list.
- repair target: Add the missing concepts as explicit formula structure, or document why they are intentionally excluded.
- value paths:
  - `<search recursive metrics JSON for key `content_token_recall`>`
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

## `core_term_centeredness_score`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `core_term_centeredness_score`>`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `cost_estimate_tokens_in`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `cost_estimate_tokens_in`>`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `cost_estimate_tokens_out`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `cost_estimate_tokens_out`>`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `counterfactual_loss_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `semantic_preservation.counterfactual_loss_count`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `covered_only_in_notes_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `coverage.covered_only_in_notes_count`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `critic_confidence`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `critic_confidence`>`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `critic_margin`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `critic_margin`>`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `critic_merge_recommended`

- type: `metric`
- bad value means: A merge/variant/gold comparison changed structure or semantics; report exact compared variants or merge rows.
- repair target: Use overlay/bridge/conflict split or reject rewrite based on backtest.
- value paths:
  - `variants.critic_merge_recommended`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
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

## `declaration_only_downgrade_flag`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `definition_quality.declaration_only_downgrade_flag`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `declaration_shape_error_count`

- type: `metric`
- bad value means: The artifact is structurally invalid; report parser/schema/combined validation errors.
- repair target: Fix A4V3 syntax, declarations, references, signatures, or combined theory conflicts.
- value paths:
  - `<search recursive metrics JSON for key `declaration_shape_error_count`>`
- evidence paths:
  - `validity.ast_error_count`
  - `validity.rendering_status`
  - `validity.combined_validation_ok`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `definition_body_present`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `definition_quality.definition_body_present`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `definitional_equation_present`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `definitional_equation_present`>`
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

## `draft_variant_count`

- type: `metric`
- bad value means: A merge/variant/gold comparison changed structure or semantics; report exact compared variants or merge rows.
- repair target: Use overlay/bridge/conflict split or reject rewrite based on backtest.
- value paths:
  - `variants.draft_variant_count`
- evidence paths:
  - `variants`
  - `variability`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `duplication_suspected`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `duplication_suspected`>`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
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

## `exception_visibility_violation_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `semantic_preservation.exception_visibility_violation_count`
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

## `expr_shape_error_count`

- type: `metric`
- bad value means: The artifact is structurally invalid; report parser/schema/combined validation errors.
- repair target: Fix A4V3 syntax, declarations, references, signatures, or combined theory conflicts.
- value paths:
  - `<search recursive metrics JSON for key `expr_shape_error_count`>`
- evidence paths:
  - `validity.ast_error_count`
  - `validity.rendering_status`
  - `validity.combined_validation_ok`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `factorization_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `parameterization.factorization_count`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `factorization_index`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `parameterization.factorization_index`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `factorization_per_clause`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `normalized_relative.factorization_per_clause`
- evidence paths:
  - `coverage.normalized_clause_count`
  - `coverage.formula_bearing_item_count`
  - `coverage.missing_fragment_count`
  - `coverage.prose_leak_count`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `factorization_per_reference_token`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `normalized_relative.factorization_per_reference_token`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `failed_llm_call_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `failed_llm_call_count`>`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `focus_signature_mode_share`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `variability.focus_signature_mode_share`
- evidence paths:
  - `variants`
  - `variability`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `focus_signature_mode_share_per_parameter_slot_mass`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `tradeoff.focus_signature_mode_share_per_parameter_slot_mass`
- evidence paths:
  - `variants`
  - `variability`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `focus_signature_unique_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `variability.focus_signature_unique_count`
- evidence paths:
  - `variants`
  - `variability`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `focus_symbol_arity`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `normalized_alignment.focus_symbol_arity`
  - `parameterization.focus_symbol_arity`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `focus_symbol_signature`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `parameterization.focus_symbol_signature`
- evidence paths:
  - `variants`
  - `variability`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `focus_term_explicitly_modeled`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `definition_quality.focus_term_explicitly_modeled`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `focus_term_in_formula_body`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `definition_quality.focus_term_in_formula_body`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `focus_term_in_top_level_decl`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `definition_quality.focus_term_in_top_level_decl`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `formula_bearing_item_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `coverage.formula_bearing_item_count`
- evidence paths:
  - `assertion_complexity.top_complex_assertions`
  - `assertion_complexity.max_assertion_depth`
  - `assertion_complexity.total_quantifier_count`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `formula_content_token_mass`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `lexical_coverage.formula_content_token_mass`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `formula_repeat_overuse_examples`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `lexical_coverage.formula_repeat_overuse_examples`
  - `lexical_coverage.formula_repeat_overuse_examples[0]`
  - `lexical_coverage.formula_repeat_overuse_examples[1]`
  - `lexical_coverage.formula_repeat_overuse_examples[2]`
  - `lexical_coverage.formula_repeat_overuse_examples[3]`
  - `lexical_coverage.formula_repeat_overuse_examples[4]`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `formula_repeat_overuse_mass`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `lexical_coverage.formula_repeat_overuse_mass`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `formula_repeat_overuse_rate`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `normalized_relative.formula_repeat_overuse_rate`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `formula_repeat_overuse_token_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `lexical_coverage.formula_repeat_overuse_token_count`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `formula_repeat_underuse_mass`

- type: `metric`
- bad value means: Some source/normalized content is absent from the target representation; report the missing token/fragment list.
- repair target: Add the missing concepts as explicit formula structure, or document why they are intentionally excluded.
- value paths:
  - `lexical_coverage.formula_repeat_underuse_mass`
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

## `formula_repeat_underuse_token_count`

- type: `metric`
- bad value means: Some source/normalized content is absent from the target representation; report the missing token/fragment list.
- repair target: Add the missing concepts as explicit formula structure, or document why they are intentionally excluded.
- value paths:
  - `lexical_coverage.formula_repeat_underuse_token_count`
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

## `formula_to_clause_compression_ratio`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `coverage.formula_to_clause_compression_ratio`
- evidence paths:
  - `coverage.normalized_clause_count`
  - `coverage.formula_bearing_item_count`
  - `coverage.missing_fragment_count`
  - `coverage.prose_leak_count`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `full_surface_content_token_mass`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `lexical_coverage.full_surface_content_token_mass`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `full_surface_repeat_overuse_examples`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `lexical_coverage.full_surface_repeat_overuse_examples`
  - `lexical_coverage.full_surface_repeat_overuse_examples[0]`
  - `lexical_coverage.full_surface_repeat_overuse_examples[1]`
  - `lexical_coverage.full_surface_repeat_overuse_examples[2]`
  - `lexical_coverage.full_surface_repeat_overuse_examples[3]`
  - `lexical_coverage.full_surface_repeat_overuse_examples[4]`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `full_surface_repeat_overuse_mass`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `lexical_coverage.full_surface_repeat_overuse_mass`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `full_surface_repeat_overuse_rate`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `normalized_relative.full_surface_repeat_overuse_rate`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `full_surface_repeat_overuse_token_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `lexical_coverage.full_surface_repeat_overuse_token_count`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `gold_clause_alignment`

- type: `metric`
- bad value means: A merge/variant/gold comparison changed structure or semantics; report exact compared variants or merge rows.
- repair target: Use overlay/bridge/conflict split or reject rewrite based on backtest.
- value paths:
  - `<search recursive metrics JSON for key `gold_clause_alignment`>`
- evidence paths:
  - `coverage.normalized_clause_count`
  - `coverage.formula_bearing_item_count`
  - `coverage.missing_fragment_count`
  - `coverage.prose_leak_count`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `gold_counterfactual_recall`

- type: `metric`
- bad value means: Some source/normalized content is absent from the target representation; report the missing token/fragment list.
- repair target: Add the missing concepts as explicit formula structure, or document why they are intentionally excluded.
- value paths:
  - `<search recursive metrics JSON for key `gold_counterfactual_recall`>`
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

## `gold_dependency_recall`

- type: `metric`
- bad value means: Some source/normalized content is absent from the target representation; report the missing token/fragment list.
- repair target: Add the missing concepts as explicit formula structure, or document why they are intentionally excluded.
- value paths:
  - `<search recursive metrics JSON for key `gold_dependency_recall`>`
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

## `gold_exception_recall`

- type: `metric`
- bad value means: Some source/normalized content is absent from the target representation; report the missing token/fragment list.
- repair target: Add the missing concepts as explicit formula structure, or document why they are intentionally excluded.
- value paths:
  - `<search recursive metrics JSON for key `gold_exception_recall`>`
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

## `gold_helper_overuse_delta`

- type: `metric`
- bad value means: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair target: Split long identifiers into anchored functions/relations/ontology links.
- value paths:
  - `<search recursive metrics JSON for key `gold_helper_overuse_delta`>`
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

## `gold_modulo_renaming_match`

- type: `metric`
- bad value means: A merge/variant/gold comparison changed structure or semantics; report exact compared variants or merge rows.
- repair target: Use overlay/bridge/conflict split or reject rewrite based on backtest.
- value paths:
  - `<search recursive metrics JSON for key `gold_modulo_renaming_match`>`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `gold_render_similarity`

- type: `metric`
- bad value means: Rendered IR does not preserve entailment/equivalence; report render text and entailment/contradiction values.
- repair target: Repair IR until render-back and entailment preserve normalized meaning.
- value paths:
  - `<search recursive metrics JSON for key `gold_render_similarity`>`
- evidence paths:
  - `render_back.render_back_text`
  - `render_back.render_nli_text_implies_ir`
  - `render_back.render_nli_ir_implies_text`
  - `render_back.render_contradiction_score`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `gold_scope_recall`

- type: `metric`
- bad value means: Some source/normalized content is absent from the target representation; report the missing token/fragment list.
- repair target: Add the missing concepts as explicit formula structure, or document why they are intentionally excluded.
- value paths:
  - `<search recursive metrics JSON for key `gold_scope_recall`>`
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

## `gold_structure_similarity`

- type: `metric`
- bad value means: A merge/variant/gold comparison changed structure or semantics; report exact compared variants or merge rows.
- repair target: Use overlay/bridge/conflict split or reject rewrite based on backtest.
- value paths:
  - `<search recursive metrics JSON for key `gold_structure_similarity`>`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `guard_loss_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `guard_loss_count`>`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `helper_explosion_count`

- type: `metric`
- bad value means: Semantics may be packed into names; report the exact identifier, pieces, grounding ratios, and source links.
- repair target: Split long identifiers into anchored functions/relations/ontology links.
- value paths:
  - `<search recursive metrics JSON for key `helper_explosion_count`>`
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

## `ir_to_source_token_gap_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `ir_to_source_token_gap_count`>`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `legacy_surface_token_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `legacy_surface_token_count`>`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `llm_call_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `llm_call_count`>`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `logic_block_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `normalized_alignment.logic_block_count`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `logic_block_to_clause_ratio`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `normalized_alignment.logic_block_to_clause_ratio`
- evidence paths:
  - `coverage.normalized_clause_count`
  - `coverage.formula_bearing_item_count`
  - `coverage.missing_fragment_count`
  - `coverage.prose_leak_count`
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

## `max_assertion_depth`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `assertion_complexity.max_assertion_depth`
- evidence paths:
  - `assertion_complexity.top_complex_assertions`
  - `assertion_complexity.max_assertion_depth`
  - `assertion_complexity.total_quantifier_count`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `max_assertion_node_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `assertion_complexity.max_assertion_node_count`
- evidence paths:
  - `assertion_complexity.top_complex_assertions`
  - `assertion_complexity.max_assertion_depth`
  - `assertion_complexity.total_quantifier_count`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `max_branching_point_count_per_assertion`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `assertion_complexity.max_branching_point_count_per_assertion`
- evidence paths:
  - `assertion_complexity.top_complex_assertions`
  - `assertion_complexity.max_assertion_depth`
  - `assertion_complexity.total_quantifier_count`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `max_call_latency_s`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `efficiency.max_call_latency_s`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `max_clause_collapse_size`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `max_clause_collapse_size`>`
- evidence paths:
  - `coverage.normalized_clause_count`
  - `coverage.formula_bearing_item_count`
  - `coverage.missing_fragment_count`
  - `coverage.prose_leak_count`
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

## `max_ite_count_per_assertion`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `assertion_complexity.max_ite_count_per_assertion`
- evidence paths:
  - `assertion_complexity.top_complex_assertions`
  - `assertion_complexity.max_assertion_depth`
  - `assertion_complexity.total_quantifier_count`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `mean_assertion_depth`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `assertion_complexity.mean_assertion_depth`
- evidence paths:
  - `assertion_complexity.top_complex_assertions`
  - `assertion_complexity.max_assertion_depth`
  - `assertion_complexity.total_quantifier_count`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `mean_assertion_node_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `assertion_complexity.mean_assertion_node_count`
- evidence paths:
  - `assertion_complexity.top_complex_assertions`
  - `assertion_complexity.max_assertion_depth`
  - `assertion_complexity.total_quantifier_count`
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

## `mean_significant_tokens_per_formula_item`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `mean_significant_tokens_per_formula_item`>`
- evidence paths:
  - `assertion_complexity.top_complex_assertions`
  - `assertion_complexity.max_assertion_depth`
  - `assertion_complexity.total_quantifier_count`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `missing_fragment_count`

- type: `metric`
- bad value means: Some source/normalized content is absent from the target representation; report the missing token/fragment list.
- repair target: Add the missing concepts as explicit formula structure, or document why they are intentionally excluded.
- value paths:
  - `coverage.missing_fragment_count`
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

## `multi_clause_merge_count`

- type: `metric`
- bad value means: A merge/variant/gold comparison changed structure or semantics; report exact compared variants or merge rows.
- repair target: Use overlay/bridge/conflict split or reject rewrite based on backtest.
- value paths:
  - `<search recursive metrics JSON for key `multi_clause_merge_count`>`
- evidence paths:
  - `coverage.normalized_clause_count`
  - `coverage.formula_bearing_item_count`
  - `coverage.missing_fragment_count`
  - `coverage.prose_leak_count`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `named_exclusion_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `named_exclusion_count`>`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `named_scope_predicate_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `named_scope_predicate_count`>`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `negation_loss_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `negation_loss_count`>`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
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

## `new_formula_content_token_rate_vs_reference_mass`

- type: `metric`
- bad value means: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair target: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- value paths:
  - `normalized_relative.new_formula_content_token_rate_vs_reference_mass`
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

## `new_full_surface_content_token_rate_vs_reference_mass`

- type: `metric`
- bad value means: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair target: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- value paths:
  - `normalized_relative.new_full_surface_content_token_rate_vs_reference_mass`
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

## `normalized_clause_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `assertion_complexity.normalized_clause_count`
  - `coverage.normalized_clause_count`
  - `normalized_alignment.normalized_clause_count`
  - `source_vs_normalized.normalized_clause_count`
- evidence paths:
  - `coverage.normalized_clause_count`
  - `coverage.formula_bearing_item_count`
  - `coverage.missing_fragment_count`
  - `coverage.prose_leak_count`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `normalized_content_mass_per_clause`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `source_vs_normalized.normalized_content_mass_per_clause`
- evidence paths:
  - `coverage.normalized_clause_count`
  - `coverage.formula_bearing_item_count`
  - `coverage.missing_fragment_count`
  - `coverage.prose_leak_count`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `normalized_content_token_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `source_vs_normalized.normalized_content_token_count`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `normalized_content_token_jaccard`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `source_vs_normalized.normalized_content_token_jaccard`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `normalized_content_token_mass`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `source_vs_normalized.normalized_content_token_mass`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `normalized_content_token_multiset_precision_to_source`

- type: `metric`
- bad value means: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair target: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- value paths:
  - `source_vs_normalized.normalized_content_token_multiset_precision_to_source`
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

## `normalized_content_token_multiset_recall_from_source`

- type: `metric`
- bad value means: Some source/normalized content is absent from the target representation; report the missing token/fragment list.
- repair target: Add the missing concepts as explicit formula structure, or document why they are intentionally excluded.
- value paths:
  - `source_vs_normalized.normalized_content_token_multiset_recall_from_source`
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

## `normalized_content_token_precision_to_source`

- type: `metric`
- bad value means: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair target: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- value paths:
  - `source_vs_normalized.normalized_content_token_precision_to_source`
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

## `normalized_content_token_recall_from_source`

- type: `metric`
- bad value means: Some source/normalized content is absent from the target representation; report the missing token/fragment list.
- repair target: Add the missing concepts as explicit formula structure, or document why they are intentionally excluded.
- value paths:
  - `source_vs_normalized.normalized_content_token_recall_from_source`
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

## `normalized_implies_source_entailment`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `source_vs_normalized.normalized_implies_source_entailment`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `normalized_length_ratio_vs_source_mass`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `source_vs_normalized.normalized_length_ratio_vs_source_mass`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `normalized_repeat_overuse_examples`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `source_vs_normalized.normalized_repeat_overuse_examples`
  - `source_vs_normalized.normalized_repeat_overuse_examples[0]`
  - `source_vs_normalized.normalized_repeat_overuse_examples[1]`
  - `source_vs_normalized.normalized_repeat_overuse_examples[2]`
  - `source_vs_normalized.normalized_repeat_overuse_examples[3]`
  - `source_vs_normalized.normalized_repeat_overuse_examples[4]`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `normalized_repeat_overuse_mass`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `source_vs_normalized.normalized_repeat_overuse_mass`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `normalized_repeat_overuse_token_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `source_vs_normalized.normalized_repeat_overuse_token_count`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `normalized_to_source_new_token_count`

- type: `metric`
- bad value means: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair target: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- value paths:
  - `source_vs_normalized.normalized_to_source_new_token_count`
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

## `notes_content_token_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `compression.notes_content_token_count`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `notes_content_token_rate_vs_reference_mass`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `normalized_relative.notes_content_token_rate_vs_reference_mass`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `notes_to_formula_content_ratio`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `compression.notes_to_formula_content_ratio`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `notes_token_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `compression.notes_token_count`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `opaque_support_symbol_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `opaque_support_symbol_count`>`
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

## `opaque_support_symbol_ratio`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `opaque_support_symbol_ratio`>`
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

## `overcompressed_single_assertion_flag`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `assertion_complexity.overcompressed_single_assertion_flag`
- evidence paths:
  - `assertion_complexity.top_complex_assertions`
  - `assertion_complexity.max_assertion_depth`
  - `assertion_complexity.total_quantifier_count`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `pairwise_structure_distance_mean`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `variability.pairwise_structure_distance_mean`
- evidence paths:
  - `variants`
  - `variability`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `pairwise_structure_similarity_mean`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `variability.pairwise_structure_similarity_mean`
- evidence paths:
  - `variants`
  - `variability`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `pairwise_structure_similarity_mean_per_parameter_slot_mass`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `tradeoff.pairwise_structure_similarity_mean_per_parameter_slot_mass`
- evidence paths:
  - `variants`
  - `variability`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `pairwise_token_jaccard_mean`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `variability.pairwise_token_jaccard_mean`
- evidence paths:
  - `variants`
  - `variability`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `parameter_slot_mass_per_clause`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `normalized_relative.parameter_slot_mass_per_clause`
- evidence paths:
  - `coverage.normalized_clause_count`
  - `coverage.formula_bearing_item_count`
  - `coverage.missing_fragment_count`
  - `coverage.prose_leak_count`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `parameter_slot_mass_per_reference_token`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `normalized_relative.parameter_slot_mass_per_reference_token`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `parameter_slots_per_factor`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `parameterization.parameter_slots_per_factor`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `parse_retry_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `parse_retry_count`>`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
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

## `probe_clarification_preserved`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `probe_clarification_preserved`>`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `probe_counterfactual_preserved`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `probe_counterfactual_preserved`>`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `probe_exception_preserved`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `probe_exception_preserved`>`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `probe_negation_preserved`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `probe_negation_preserved`>`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `probe_reference_preserved`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `probe_reference_preserved`>`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `probe_responsibility_preserved`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `probe_responsibility_preserved`>`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `probe_scope_preserved`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `probe_scope_preserved`>`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `probe_temporal_order_preserved`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `probe_temporal_order_preserved`>`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `probe_value_source_preserved`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `probe_value_source_preserved`>`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `procedural_note_leak_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `procedural_note_leak_count`>`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `prose_leak_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `coverage.prose_leak_count`
- evidence paths:
  - `coverage.normalized_clause_count`
  - `coverage.formula_bearing_item_count`
  - `coverage.missing_fragment_count`
  - `coverage.prose_leak_count`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `quantifier_loss_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `quantifier_loss_count`>`
- evidence paths:
  - `assertion_complexity.top_complex_assertions`
  - `assertion_complexity.max_assertion_depth`
  - `assertion_complexity.total_quantifier_count`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `quantifier_parameter_slot_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `parameterization.quantifier_parameter_slot_count`
- evidence paths:
  - `assertion_complexity.top_complex_assertions`
  - `assertion_complexity.max_assertion_depth`
  - `assertion_complexity.total_quantifier_count`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `reflexive_equality_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `definition_quality.reflexive_equality_count`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `render_back_available`

- type: `metric`
- bad value means: Rendered IR does not preserve entailment/equivalence; report render text and entailment/contradiction values.
- repair target: Repair IR until render-back and entailment preserve normalized meaning.
- value paths:
  - `<search recursive metrics JSON for key `render_back_available`>`
- evidence paths:
  - `render_back.render_back_text`
  - `render_back.render_nli_text_implies_ir`
  - `render_back.render_nli_ir_implies_text`
  - `render_back.render_contradiction_score`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `render_back_clause_count`

- type: `metric`
- bad value means: Rendered IR does not preserve entailment/equivalence; report render text and entailment/contradiction values.
- repair target: Repair IR until render-back and entailment preserve normalized meaning.
- value paths:
  - `<search recursive metrics JSON for key `render_back_clause_count`>`
- evidence paths:
  - `render_back.render_back_text`
  - `render_back.render_nli_text_implies_ir`
  - `render_back.render_nli_ir_implies_text`
  - `render_back.render_contradiction_score`
  - `coverage.normalized_clause_count`
  - `coverage.formula_bearing_item_count`
  - `coverage.missing_fragment_count`
  - `coverage.prose_leak_count`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `render_bertscore_f1_to_normalized`

- type: `metric`
- bad value means: Rendered IR does not preserve entailment/equivalence; report render text and entailment/contradiction values.
- repair target: Repair IR until render-back and entailment preserve normalized meaning.
- value paths:
  - `render_back.render_bertscore_f1_to_normalized`
- evidence paths:
  - `render_back.render_back_text`
  - `render_back.render_nli_text_implies_ir`
  - `render_back.render_nli_ir_implies_text`
  - `render_back.render_contradiction_score`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `render_bertscore_f1_to_normalized_per_formula_repeat_overuse_mass`

- type: `metric`
- bad value means: Rendered IR does not preserve entailment/equivalence; report render text and entailment/contradiction values.
- repair target: Repair IR until render-back and entailment preserve normalized meaning.
- value paths:
  - `tradeoff.render_bertscore_f1_to_normalized_per_formula_repeat_overuse_mass`
- evidence paths:
  - `render_back.render_back_text`
  - `render_back.render_nli_text_implies_ir`
  - `render_back.render_nli_ir_implies_text`
  - `render_back.render_contradiction_score`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `render_bertscore_f1_to_normalized_per_parameter_slot_mass`

- type: `metric`
- bad value means: Rendered IR does not preserve entailment/equivalence; report render text and entailment/contradiction values.
- repair target: Repair IR until render-back and entailment preserve normalized meaning.
- value paths:
  - `tradeoff.render_bertscore_f1_to_normalized_per_parameter_slot_mass`
- evidence paths:
  - `render_back.render_back_text`
  - `render_back.render_nli_text_implies_ir`
  - `render_back.render_nli_ir_implies_text`
  - `render_back.render_contradiction_score`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `render_bertscore_f1_to_source`

- type: `metric`
- bad value means: Rendered IR does not preserve entailment/equivalence; report render text and entailment/contradiction values.
- repair target: Repair IR until render-back and entailment preserve normalized meaning.
- value paths:
  - `render_back.render_bertscore_f1_to_source`
- evidence paths:
  - `render_back.render_back_text`
  - `render_back.render_nli_text_implies_ir`
  - `render_back.render_nli_ir_implies_text`
  - `render_back.render_contradiction_score`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `render_content_token_precision`

- type: `metric`
- bad value means: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair target: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- value paths:
  - `<search recursive metrics JSON for key `render_content_token_precision`>`
- evidence paths:
  - `grounding.new_formula_content_tokens_vs_text_only`
  - `grounding.new_full_surface_content_tokens_vs_text_only`
  - `lexical_coverage.formula_repeat_overuse_examples`
  - `grounding.origin_error_count`
  - `render_back.render_back_text`
  - `render_back.render_nli_text_implies_ir`
  - `render_back.render_nli_ir_implies_text`
  - `render_back.render_contradiction_score`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `render_content_token_recall`

- type: `metric`
- bad value means: Some source/normalized content is absent from the target representation; report the missing token/fragment list.
- repair target: Add the missing concepts as explicit formula structure, or document why they are intentionally excluded.
- value paths:
  - `<search recursive metrics JSON for key `render_content_token_recall`>`
- evidence paths:
  - `lexical_coverage.source_content_tokens_missing_from_formula`
  - `lexical_coverage.source_content_tokens_missing_from_full_surface`
  - `lexical_coverage.formula_repeat_underuse_mass`
  - `coverage.missing_fragment_count`
  - `render_back.render_back_text`
  - `render_back.render_nli_text_implies_ir`
  - `render_back.render_nli_ir_implies_text`
  - `render_back.render_contradiction_score`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `render_contradiction_score`

- type: `metric`
- bad value means: Rendered IR does not preserve entailment/equivalence; report render text and entailment/contradiction values.
- repair target: Repair IR until render-back and entailment preserve normalized meaning.
- value paths:
  - `render_back.render_contradiction_score`
- evidence paths:
  - `render_back.render_back_text`
  - `render_back.render_nli_text_implies_ir`
  - `render_back.render_nli_ir_implies_text`
  - `render_back.render_contradiction_score`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `render_nli_ir_implies_text`

- type: `metric`
- bad value means: Rendered IR does not preserve entailment/equivalence; report render text and entailment/contradiction values.
- repair target: Repair IR until render-back and entailment preserve normalized meaning.
- value paths:
  - `render_back.render_nli_ir_implies_text`
- evidence paths:
  - `render_back.render_back_text`
  - `render_back.render_nli_text_implies_ir`
  - `render_back.render_nli_ir_implies_text`
  - `render_back.render_contradiction_score`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `render_nli_ir_implies_text_per_parameter_slot_mass`

- type: `metric`
- bad value means: Rendered IR does not preserve entailment/equivalence; report render text and entailment/contradiction values.
- repair target: Repair IR until render-back and entailment preserve normalized meaning.
- value paths:
  - `tradeoff.render_nli_ir_implies_text_per_parameter_slot_mass`
- evidence paths:
  - `render_back.render_back_text`
  - `render_back.render_nli_text_implies_ir`
  - `render_back.render_nli_ir_implies_text`
  - `render_back.render_contradiction_score`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `render_nli_text_implies_ir`

- type: `metric`
- bad value means: Rendered IR does not preserve entailment/equivalence; report render text and entailment/contradiction values.
- repair target: Repair IR until render-back and entailment preserve normalized meaning.
- value paths:
  - `render_back.render_nli_text_implies_ir`
- evidence paths:
  - `render_back.render_back_text`
  - `render_back.render_nli_text_implies_ir`
  - `render_back.render_nli_ir_implies_text`
  - `render_back.render_contradiction_score`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `render_nli_text_implies_ir_per_formula_repeat_overuse_mass`

- type: `metric`
- bad value means: Rendered IR does not preserve entailment/equivalence; report render text and entailment/contradiction values.
- repair target: Repair IR until render-back and entailment preserve normalized meaning.
- value paths:
  - `tradeoff.render_nli_text_implies_ir_per_formula_repeat_overuse_mass`
- evidence paths:
  - `render_back.render_back_text`
  - `render_back.render_nli_text_implies_ir`
  - `render_back.render_nli_ir_implies_text`
  - `render_back.render_contradiction_score`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `render_nli_text_implies_ir_per_full_surface_repeat_overuse_mass`

- type: `metric`
- bad value means: Rendered IR does not preserve entailment/equivalence; report render text and entailment/contradiction values.
- repair target: Repair IR until render-back and entailment preserve normalized meaning.
- value paths:
  - `tradeoff.render_nli_text_implies_ir_per_full_surface_repeat_overuse_mass`
- evidence paths:
  - `render_back.render_back_text`
  - `render_back.render_nli_text_implies_ir`
  - `render_back.render_nli_ir_implies_text`
  - `render_back.render_contradiction_score`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `render_nli_text_implies_ir_per_parameter_slot_mass`

- type: `metric`
- bad value means: Rendered IR does not preserve entailment/equivalence; report render text and entailment/contradiction values.
- repair target: Repair IR until render-back and entailment preserve normalized meaning.
- value paths:
  - `tradeoff.render_nli_text_implies_ir_per_parameter_slot_mass`
- evidence paths:
  - `render_back.render_back_text`
  - `render_back.render_nli_text_implies_ir`
  - `render_back.render_nli_ir_implies_text`
  - `render_back.render_contradiction_score`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `render_similarity_threshold_pass`

- type: `metric`
- bad value means: Rendered IR does not preserve entailment/equivalence; report render text and entailment/contradiction values.
- repair target: Repair IR until render-back and entailment preserve normalized meaning.
- value paths:
  - `<search recursive metrics JSON for key `render_similarity_threshold_pass`>`
- evidence paths:
  - `render_back.render_back_text`
  - `render_back.render_nli_text_implies_ir`
  - `render_back.render_nli_ir_implies_text`
  - `render_back.render_contradiction_score`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `rendering_ok`

- type: `metric`
- bad value means: Rendered IR does not preserve entailment/equivalence; report render text and entailment/contradiction values.
- repair target: Repair IR until render-back and entailment preserve normalized meaning.
- value paths:
  - `validity.rendering_ok`
- evidence paths:
  - `render_back.render_back_text`
  - `render_back.render_nli_text_implies_ir`
  - `render_back.render_nli_ir_implies_text`
  - `render_back.render_contradiction_score`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `repair_calls_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `repair_calls_count`>`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `responsibility_loss_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `semantic_preservation.responsibility_loss_count`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `same_parameter_mass_different_structure_pair_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `variability.same_parameter_mass_different_structure_pair_count`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `same_parameter_mass_different_structure_pair_ratio`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `same_parameter_mass_different_structure_pair_ratio`>`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `schema_repair_round_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `schema_repair_round_count`>`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `scope_visibility_violation_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `semantic_preservation.scope_visibility_violation_count`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `semantic_coverage_retry_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `validity.semantic_coverage_retry_count`
- evidence paths:
  - `coverage.normalized_clause_count`
  - `coverage.formula_bearing_item_count`
  - `coverage.missing_fragment_count`
  - `coverage.prose_leak_count`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `single_assertion_logic_share`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `assertion_complexity.single_assertion_logic_share`
  - `normalized_alignment.single_assertion_logic_share`
- evidence paths:
  - `assertion_complexity.top_complex_assertions`
  - `assertion_complexity.max_assertion_depth`
  - `assertion_complexity.total_quantifier_count`
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

## `source_content_token_mass`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `lexical_coverage.source_content_token_mass`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `source_excerpt_content_token_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `source_vs_normalized.source_excerpt_content_token_count`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `source_excerpt_content_token_mass`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `source_vs_normalized.source_excerpt_content_token_mass`
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

## `source_implies_normalized_entailment`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `source_vs_normalized.source_implies_normalized_entailment`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `source_normalized_bertscore_f1`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `source_vs_normalized.source_normalized_bertscore_f1`
- evidence paths:
  - `render_back.render_back_text`
  - `render_back.render_nli_text_implies_ir`
  - `render_back.render_nli_ir_implies_text`
  - `render_back.render_contradiction_score`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `source_to_ir_token_gap_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `source_to_ir_token_gap_count`>`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `source_to_normalized_token_gap_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `source_vs_normalized.source_to_normalized_token_gap_count`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `source_vs_normalized_contradiction_score`

- type: `metric`
- bad value means: Rendered IR does not preserve entailment/equivalence; report render text and entailment/contradiction values.
- repair target: Repair IR until render-back and entailment preserve normalized meaning.
- value paths:
  - `source_vs_normalized.source_vs_normalized_contradiction_score`
- evidence paths:
  - `render_back.render_back_text`
  - `render_back.render_nli_text_implies_ir`
  - `render_back.render_nli_ir_implies_text`
  - `render_back.render_contradiction_score`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `successful_llm_call_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `successful_llm_call_count`>`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `support_only_clause_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `support_only_clause_count`>`
- evidence paths:
  - `coverage.normalized_clause_count`
  - `coverage.formula_bearing_item_count`
  - `coverage.missing_fragment_count`
  - `coverage.prose_leak_count`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `support_only_clause_ratio`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `support_only_clause_ratio`>`
- evidence paths:
  - `coverage.normalized_clause_count`
  - `coverage.formula_bearing_item_count`
  - `coverage.missing_fragment_count`
  - `coverage.prose_leak_count`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `temporal_link_loss_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `temporal_link_loss_count`>`
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

## `threshold`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `threshold`>`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `timeout_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `timeout_count`>`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `top_complex_assertions`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `assertion_complexity.top_complex_assertions`
  - `assertion_complexity.top_complex_assertions[0]`
  - `assertion_complexity.top_complex_assertions[1]`
  - `assertion_complexity.top_complex_assertions[2]`
  - `assertion_complexity.top_complex_assertions[3]`
  - `assertion_complexity.top_complex_assertions[4]`
- evidence paths:
  - `assertion_complexity.top_complex_assertions`
  - `assertion_complexity.max_assertion_depth`
  - `assertion_complexity.total_quantifier_count`
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

## `top_level_parameter_slot_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `parameterization.top_level_parameter_slot_count`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `total_assertion_node_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `assertion_complexity.total_assertion_node_count`
- evidence paths:
  - `assertion_complexity.top_complex_assertions`
  - `assertion_complexity.max_assertion_depth`
  - `assertion_complexity.total_quantifier_count`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `total_branching_point_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `assertion_complexity.total_branching_point_count`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `total_connective_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `assertion_complexity.total_connective_count`
- evidence paths:
  - `assertion_complexity.top_complex_assertions`
  - `assertion_complexity.max_assertion_depth`
  - `assertion_complexity.total_quantifier_count`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `total_ite_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `assertion_complexity.total_ite_count`
- evidence paths:
  - `assertion_complexity.top_complex_assertions`
  - `assertion_complexity.max_assertion_depth`
  - `assertion_complexity.total_quantifier_count`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `total_parameter_slot_mass`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `parameterization.total_parameter_slot_mass`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `total_quantifier_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `assertion_complexity.total_quantifier_count`
- evidence paths:
  - `assertion_complexity.top_complex_assertions`
  - `assertion_complexity.max_assertion_depth`
  - `assertion_complexity.total_quantifier_count`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `uncovered_clause_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `uncovered_clause_count`>`
- evidence paths:
  - `coverage.normalized_clause_count`
  - `coverage.formula_bearing_item_count`
  - `coverage.missing_fragment_count`
  - `coverage.prose_leak_count`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `underdecomposed_logic_flag`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `normalized_alignment.underdecomposed_logic_flag`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
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

## `unique_ir_variant_count`

- type: `metric`
- bad value means: A merge/variant/gold comparison changed structure or semantics; report exact compared variants or merge rows.
- repair target: Use overlay/bridge/conflict split or reject rewrite based on backtest.
- value paths:
  - `variants.unique_ir_variant_count`
- evidence paths:
  - `variants`
  - `variability`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `unique_variant_signature_count`

- type: `metric`
- bad value means: A merge/variant/gold comparison changed structure or semantics; report exact compared variants or merge rows.
- repair target: Use overlay/bridge/conflict split or reject rewrite based on backtest.
- value paths:
  - `variability.unique_variant_signature_count`
- evidence paths:
  - `variants`
  - `variability`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `usable_variant_count`

- type: `metric`
- bad value means: A merge/variant/gold comparison changed structure or semantics; report exact compared variants or merge rows.
- repair target: Use overlay/bridge/conflict split or reject rewrite based on backtest.
- value paths:
  - `variability.usable_variant_count`
- evidence paths:
  - `variants`
  - `variability`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `vacuous_constraint_flag`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `definition_quality.vacuous_constraint_flag`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `variant_diversity_score`

- type: `metric`
- bad value means: A merge/variant/gold comparison changed structure or semantics; report exact compared variants or merge rows.
- repair target: Use overlay/bridge/conflict split or reject rewrite based on backtest.
- value paths:
  - `<search recursive metrics JSON for key `variant_diversity_score`>`
- evidence paths:
  - `variants`
  - `variability`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `wall_clock_seconds`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `efficiency.wall_clock_seconds`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `accepted`

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

## `avoid_padding_or_repetition`

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

## `cover_every_normalized_block`

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

## `definition_role_alignment_failed`

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

## `draft_ir_parse_failed`

- type: `check`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<check output, lint report, checklist result, or generated diagnostic finding>`
- evidence paths:
  - `parse errors`
  - `validation errors`
  - `main_ir.a4v3`
- diagnostic output must include:
  - check name
  - severity
  - exact row/code that fired
  - source path and target path when available
  - symbol/token/line number when available

## `draft_ir_validation_failed`

- type: `check`
- bad value means: The artifact is structurally invalid; report parser/schema/combined validation errors.
- repair target: Fix A4V3 syntax, declarations, references, signatures, or combined theory conflicts.
- value paths:
  - `<check output, lint report, checklist result, or generated diagnostic finding>`
- evidence paths:
  - `parse errors`
  - `validation errors`
  - `main_ir.a4v3`
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

## `formula_item_count_below_normalized_clause_count`

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

## `invalid_surface_correction`

- type: `check`
- bad value means: The artifact is structurally invalid; report parser/schema/combined validation errors.
- repair target: Fix A4V3 syntax, declarations, references, signatures, or combined theory conflicts.
- value paths:
  - `<check output, lint report, checklist result, or generated diagnostic finding>`
- evidence paths:
  - `parse errors`
  - `validation errors`
  - `main_ir.a4v3`
- diagnostic output must include:
  - check name
  - severity
  - exact row/code that fired
  - source path and target path when available
  - symbol/token/line number when available

## `keep_clause_boundaries_honest`

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

## `keep_grounding_auditable`

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

## `keep_links_explicit`

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

## `keep_render_back_close_to_normalized_text`

- type: `check`
- bad value means: Rendered IR does not preserve entailment/equivalence; report render text and entailment/contradiction values.
- repair target: Repair IR until render-back and entailment preserve normalized meaning.
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

## `keep_unresolved_ambiguity_visible`

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

## `lexical_preservation_below_threshold`

- type: `check`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
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

## `make_edits_explicit`

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

## `missing_render_targets`

- type: `check`
- bad value means: Some source/normalized content is absent from the target representation; report the missing token/fragment list.
- repair target: Add the missing concepts as explicit formula structure, or document why they are intentionally excluded.
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

## `needs_review`

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

## `normalization_duplicate_content_repetition`

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

## `preserve_meaning`

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

## `preserve_negation_scope_and_exceptions`

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

## `render_alignment_below_threshold`

- type: `check`
- bad value means: Rendered IR does not preserve entailment/equivalence; report render text and entailment/contradiction values.
- repair target: Repair IR until render-back and entailment preserve normalized meaning.
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

## `silent_addition`

- type: `check`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
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

## `silent_deletion`

- type: `check`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
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

## `soft_review`

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

## `symbol_name_embeds_concept_without_explicit_link`

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

## `symbol_name_embeds_entity_without_explicit_link`

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

## `use_valid_ir_surface_forms`

- type: `check`
- bad value means: The artifact is structurally invalid; report parser/schema/combined validation errors.
- repair target: Fix A4V3 syntax, declarations, references, signatures, or combined theory conflicts.
- value paths:
  - `<check output, lint report, checklist result, or generated diagnostic finding>`
- evidence paths:
  - `parse errors`
  - `validation errors`
  - `main_ir.a4v3`
- diagnostic output must include:
  - check name
  - severity
  - exact row/code that fired
  - source path and target path when available
  - symbol/token/line number when available
