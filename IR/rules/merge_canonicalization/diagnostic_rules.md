# Diagnostic Rules: merge_canonicalization

- metric_count: `63`
- check_count: `15`
- rule_count: `78`

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

## `llm_bertscore`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `llm_bertscore`>`
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

## `llm_contradiction`

- type: `metric`
- bad value means: Rendered IR does not preserve entailment/equivalence; report render text and entailment/contradiction values.
- repair target: Repair IR until render-back and entailment preserve normalized meaning.
- value paths:
  - `<search recursive metrics JSON for key `llm_contradiction`>`
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

## `llm_ir_to_text`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `llm_ir_to_text`>`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `llm_text_to_ir`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `llm_text_to_ir`>`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
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

## `relation_type`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `relation_type`>`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
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

## `semantic_verdict`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `semantic_verdict`>`
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

## `bridge_family`

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

## `bridge_supertype`

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

## `conflict_split`

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

## `exact_merge_overlay`

- type: `check`
- bad value means: A merge/variant/gold comparison changed structure or semantics; report exact compared variants or merge rows.
- repair target: Use overlay/bridge/conflict split or reject rewrite based on backtest.
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

## `keep_separate_with_link`

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

## `role_link`

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

