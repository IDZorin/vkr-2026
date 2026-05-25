# Translation Metrics v1 - N05

- generated_at: `2026-05-12T14:18:47.370787+02:00`
- artifact_path: `D:\OneDrive\Documents\Study\MIPT\VKR\research_experiments\2026-02_pipeline\case_studies\financial_methodology\definitions\N05\N05_manual_section_workspace_artifact_current_v1.json`
- catalog_version: `translation_metrics_catalog_v1`

## validity

```json
{
  "ast_valid": 1,
  "ast_error_count": 0,
  "rendering_ok": 1,
  "combined_validation_ok": 1,
  "invalid_submit_count": 0,
  "repair_orchestrator_count": 0,
  "semantic_coverage_retry_count": 0,
  "status": "ok",
  "ast_conformance": "canonical_ast_v1",
  "rendering_status": "rendered_from_ast"
}
```

## grounding

```json
{
  "ungrounded_symbol_count": 0,
  "ungrounded_sort_count": 0,
  "ungrounded_ref_count": 0,
  "ungrounded_callee_count": 0,
  "prelude_redeclaration_count": 0,
  "origin_error_count": 0,
  "new_formula_token_count_vs_text_only": 7,
  "new_formula_content_token_count_vs_text_only": 6,
  "new_formula_token_count_vs_text_prelude_only": 3,
  "new_formula_content_token_count_vs_text_prelude_only": 2,
  "new_formula_token_count_vs_text_prelude_advisory": 3,
  "new_formula_content_token_count_vs_text_prelude_advisory": 2,
  "new_full_surface_token_count_vs_text_only": 30,
  "new_full_surface_content_token_count_vs_text_only": 26,
  "new_full_surface_token_count_vs_text_prelude_only": 24,
  "new_full_surface_content_token_count_vs_text_prelude_only": 21,
  "new_full_surface_token_count_vs_text_prelude_advisory": 24,
  "new_full_surface_content_token_count_vs_text_prelude_advisory": 21,
  "new_formula_content_tokens_vs_text_only": [
    "calculation_day",
    "calculation_day_definition",
    "thursday",
    "tuesday",
    "wednesday",
    "weekdayof"
  ],
  "new_formula_content_tokens_vs_text_prelude_only": [
    "calculation_day",
    "calculation_day_definition"
  ],
  "new_formula_content_tokens_vs_text_prelude_advisory": [
    "calculation_day",
    "calculation_day_definition"
  ],
  "new_full_surface_content_tokens_vs_text_only": [
    "a4v3",
    "calculation_day",
    "calculation_day_definition",
    "canonical",
    "computation",
    "current",
    "deterministic",
    "draft",
    "main_ir",
    "manual",
    "metric",
    "parsed",
    "primitive_usage",
    "recomputation",
    "reconstructed",
    "rendering_notes",
    "residual_risks",
    "section",
    "section-level",
    "strengths",
    "text",
    "thursday",
    "tuesday",
    "wednesday",
    "weekdayof",
    "workspace"
  ],
  "new_full_surface_content_tokens_vs_text_prelude_only": [
    "calculation_day",
    "calculation_day_definition",
    "canonical",
    "computation",
    "current",
    "deterministic",
    "draft",
    "main_ir",
    "manual",
    "metric",
    "parsed",
    "primitive_usage",
    "recomputation",
    "reconstructed",
    "rendering_notes",
    "residual_risks",
    "section",
    "section-level",
    "strengths",
    "text",
    "workspace"
  ],
  "new_full_surface_content_tokens_vs_text_prelude_advisory": [
    "calculation_day",
    "calculation_day_definition",
    "canonical",
    "computation",
    "current",
    "deterministic",
    "draft",
    "main_ir",
    "manual",
    "metric",
    "parsed",
    "primitive_usage",
    "recomputation",
    "reconstructed",
    "rendering_notes",
    "residual_risks",
    "section",
    "section-level",
    "strengths",
    "text",
    "workspace"
  ]
}
```

## coverage

```json
{
  "normalized_clause_count": 1,
  "formula_bearing_item_count": 1,
  "formula_to_clause_compression_ratio": 1.0,
  "coverage_fragment_count": 0,
  "covered_formally_count": 0,
  "covered_only_in_notes_count": 0,
  "missing_fragment_count": 0,
  "coverage_fragment_formal_ratio": 1.0,
  "coverage_fragment_any_ratio": 1.0,
  "prose_leak_count": 0
}
```

## lexical_coverage

```json
{
  "reference_text_basis": "normalized_clauses_or_source_excerpt_fallback",
  "source_content_token_count": 4,
  "source_content_token_mass": 4,
  "formula_content_token_count": 8,
  "formula_content_token_mass": 14,
  "full_surface_content_token_count": 31,
  "full_surface_content_token_mass": 41,
  "formula_content_token_recall": 0.75,
  "full_surface_content_token_recall": 0.75,
  "full_surface_content_token_jaccard": 0.09375,
  "formula_content_token_multiset_recall": 0.75,
  "formula_content_token_multiset_precision": 0.21428571428571427,
  "formula_repeat_overuse_token_count": 6,
  "formula_repeat_overuse_mass": 11,
  "formula_repeat_underuse_token_count": 1,
  "formula_repeat_underuse_mass": 1,
  "formula_repeat_overuse_examples": [
    {
      "token": "weekdayof",
      "current_count": 5,
      "baseline_count": 0,
      "delta": 5
    },
    {
      "token": "calculation",
      "current_count": 3,
      "baseline_count": 1,
      "delta": 2
    },
    {
      "token": "definition",
      "current_count": 1,
      "baseline_count": 0,
      "delta": 1
    },
    {
      "token": "thursday",
      "current_count": 1,
      "baseline_count": 0,
      "delta": 1
    },
    {
      "token": "tuesday",
      "current_count": 1,
      "baseline_count": 0,
      "delta": 1
    },
    {
      "token": "wednesday",
      "current_count": 1,
      "baseline_count": 0,
      "delta": 1
    }
  ],
  "full_surface_content_token_multiset_recall": 0.75,
  "full_surface_content_token_multiset_precision": 0.07317073170731707,
  "full_surface_repeat_overuse_token_count": 29,
  "full_surface_repeat_overuse_mass": 38,
  "full_surface_repeat_underuse_token_count": 1,
  "full_surface_repeat_underuse_mass": 1,
  "full_surface_repeat_overuse_examples": [
    {
      "token": "weekdayof",
      "current_count": 5,
      "baseline_count": 0,
      "delta": 5
    },
    {
      "token": "calculation",
      "current_count": 3,
      "baseline_count": 1,
      "delta": 2
    },
    {
      "token": "manual",
      "current_count": 2,
      "baseline_count": 0,
      "delta": 2
    },
    {
      "token": "metric",
      "current_count": 2,
      "baseline_count": 0,
      "delta": 2
    },
    {
      "token": "section",
      "current_count": 2,
      "baseline_count": 0,
      "delta": 2
    },
    {
      "token": "workspace",
      "current_count": 2,
      "baseline_count": 0,
      "delta": 2
    },
    {
      "token": "a4v3",
      "current_count": 1,
      "baseline_count": 0,
      "delta": 1
    },
    {
      "token": "canonical",
      "current_count": 1,
      "baseline_count": 0,
      "delta": 1
    },
    {
      "token": "computation",
      "current_count": 1,
      "baseline_count": 0,
      "delta": 1
    },
    {
      "token": "current",
      "current_count": 1,
      "baseline_count": 0,
      "delta": 1
    },
    {
      "token": "definition",
      "current_count": 1,
      "baseline_count": 0,
      "delta": 1
    },
    {
      "token": "deterministic",
      "current_count": 1,
      "baseline_count": 0,
      "delta": 1
    },
    {
      "token": "draft",
      "current_count": 1,
      "baseline_count": 0,
      "delta": 1
    },
    {
      "token": "level",
      "current_count": 1,
      "baseline_count": 0,
      "delta": 1
    },
    {
      "token": "main",
      "current_count": 1,
      "baseline_count": 0,
      "delta": 1
    },
    {
      "token": "notes",
      "current_count": 1,
      "baseline_count": 0,
      "delta": 1
    },
    {
      "token": "parsed",
      "current_count": 1,
      "baseline_count": 0,
      "delta": 1
    },
    {
      "token": "primitive",
      "current_count": 1,
      "baseline_count": 0,
      "delta": 1
    },
    {
      "token": "recomputation",
      "current_count": 1,
      "baseline_count": 0,
      "delta": 1
    },
    {
      "token": "reconstructed",
      "current_count": 1,
      "baseline_count": 0,
      "delta": 1
    }
  ],
  "source_to_formula_token_gap_count": 1,
  "source_to_full_surface_token_gap_count": 1,
  "source_content_tokens_missing_from_formula": [
    "weekday"
  ],
  "source_content_tokens_missing_from_full_surface": [
    "weekday"
  ]
}
```

## source_vs_normalized

```json
{
  "source_excerpt_content_token_count": 4,
  "source_excerpt_content_token_mass": 4,
  "normalized_content_token_count": 4,
  "normalized_content_token_mass": 4,
  "normalized_clause_count": 1,
  "normalized_content_token_recall_from_source": 1.0,
  "normalized_content_token_precision_to_source": 1.0,
  "normalized_content_token_jaccard": 1.0,
  "normalized_content_token_multiset_recall_from_source": 1.0,
  "normalized_content_token_multiset_precision_to_source": 1.0,
  "source_to_normalized_token_gap_count": 0,
  "normalized_to_source_new_token_count": 0,
  "normalized_repeat_overuse_token_count": 0,
  "normalized_repeat_overuse_mass": 0,
  "normalized_repeat_underuse_token_count": 0,
  "normalized_repeat_underuse_mass": 0,
  "normalized_repeat_overuse_examples": [],
  "normalized_length_ratio_vs_source_mass": 1.0,
  "normalized_content_mass_per_clause": 4.0,
  "source_normalized_bertscore_precision": 1.0,
  "source_normalized_bertscore_recall": 1.0,
  "source_normalized_bertscore_f1": 1.0,
  "normalized_implies_source_entailment": 0.9891141653060913,
  "source_implies_normalized_entailment": 0.9891141653060913,
  "source_vs_normalized_contradiction_score": 0.00419963151216507
}
```

## semantic_preservation

```json
{
  "explicit_link_violation_count": 0,
  "scope_visibility_violation_count": 0,
  "exception_visibility_violation_count": 0,
  "counterfactual_loss_count": 0,
  "clarification_loss_count": 0,
  "responsibility_loss_count": 0
}
```

## definition_quality

```json
{
  "focus_term_explicitly_modeled": 0,
  "focus_term_in_top_level_decl": 0,
  "focus_term_in_formula_body": 0,
  "declaration_only_downgrade_flag": 0,
  "definition_body_present": 1,
  "vacuous_constraint_flag": 0,
  "reflexive_equality_count": 0
}
```

## compression

```json
{
  "notes_token_count": 29,
  "notes_content_token_count": 23,
  "notes_to_formula_content_ratio": 2.875
}
```

## identifier_glue

```json
{
  "identifier_count": 10,
  "compound_identifier_count_raw": 0,
  "compound_identifier_count_content": 1,
  "compound_identifier_rate_raw": 0.0,
  "compound_identifier_rate_content": 0.1,
  "max_identifier_piece_count_raw": 3,
  "max_identifier_piece_count_content": 3,
  "mean_identifier_piece_count_raw": 1.4,
  "mean_identifier_piece_count_content": 1.2,
  "identifier_glue_excess_mass_raw": 0,
  "identifier_glue_excess_mass_content": 1,
  "identifier_glue_excess_rate_raw": 0.0,
  "identifier_glue_excess_rate_content": 0.1,
  "source_grounded_content_piece_ratio_mean": 0.9666666666666667,
  "advisory_grounded_content_piece_ratio_mean": 0.9666666666666667,
  "low_source_grounded_glued_identifier_count": 1,
  "low_source_grounded_glued_identifier_rate": 0.1,
  "entity_relation_target_fusion_count": 0,
  "entity_relation_target_fusion_rate": 0.0,
  "conditional_relation_name_packing_count": 0,
  "conditional_relation_name_packing_rate": 0.0,
  "top_glued_identifiers": [
    {
      "identifier": "calculation_day_definition",
      "raw_piece_count": 3,
      "content_piece_count": 3,
      "raw_pieces": [
        "calculation",
        "day",
        "definition"
      ],
      "content_pieces": [
        "calculation",
        "day",
        "definition"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 1,
      "source_grounded_content_piece_count": 2,
      "advisory_grounded_content_piece_count": 2,
      "source_grounded_content_piece_ratio": 0.6666666666666666,
      "advisory_grounded_content_piece_ratio": 0.6666666666666666
    },
    {
      "identifier": "calculation_day",
      "raw_piece_count": 2,
      "content_piece_count": 2,
      "raw_pieces": [
        "calculation",
        "day"
      ],
      "content_pieces": [
        "calculation",
        "day"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 0,
      "source_grounded_content_piece_count": 2,
      "advisory_grounded_content_piece_count": 2,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    },
    {
      "identifier": "Day",
      "raw_piece_count": 1,
      "content_piece_count": 1,
      "raw_pieces": [
        "day"
      ],
      "content_pieces": [
        "day"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 0,
      "source_grounded_content_piece_count": 1,
      "advisory_grounded_content_piece_count": 1,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    },
    {
      "identifier": "Friday",
      "raw_piece_count": 1,
      "content_piece_count": 1,
      "raw_pieces": [
        "friday"
      ],
      "content_pieces": [
        "friday"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 0,
      "source_grounded_content_piece_count": 1,
      "advisory_grounded_content_piece_count": 1,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    },
    {
      "identifier": "Monday",
      "raw_piece_count": 1,
      "content_piece_count": 1,
      "raw_pieces": [
        "monday"
      ],
      "content_pieces": [
        "monday"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 0,
      "source_grounded_content_piece_count": 1,
      "advisory_grounded_content_piece_count": 1,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    },
    {
      "identifier": "Thursday",
      "raw_piece_count": 1,
      "content_piece_count": 1,
      "raw_pieces": [
        "thursday"
      ],
      "content_pieces": [
        "thursday"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 0,
      "source_grounded_content_piece_count": 1,
      "advisory_grounded_content_piece_count": 1,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    },
    {
      "identifier": "Tuesday",
      "raw_piece_count": 1,
      "content_piece_count": 1,
      "raw_pieces": [
        "tuesday"
      ],
      "content_pieces": [
        "tuesday"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 0,
      "source_grounded_content_piece_count": 1,
      "advisory_grounded_content_piece_count": 1,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    },
    {
      "identifier": "Wednesday",
      "raw_piece_count": 1,
      "content_piece_count": 1,
      "raw_pieces": [
        "wednesday"
      ],
      "content_pieces": [
        "wednesday"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 0,
      "source_grounded_content_piece_count": 1,
      "advisory_grounded_content_piece_count": 1,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    },
    {
      "identifier": "WeekdayOf",
      "raw_piece_count": 2,
      "content_piece_count": 1,
      "raw_pieces": [
        "weekday",
        "of"
      ],
      "content_pieces": [
        "weekday"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 0,
      "source_grounded_content_piece_count": 1,
      "advisory_grounded_content_piece_count": 1,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    },
    {
      "identifier": "d",
      "raw_piece_count": 1,
      "content_piece_count": 0,
      "raw_pieces": [
        "d"
      ],
      "content_pieces": [],
      "glue_excess_raw": 0,
      "glue_excess_content": 0,
      "source_grounded_content_piece_count": 0,
      "advisory_grounded_content_piece_count": 0,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    }
  ],
  "lowest_source_grounded_identifiers": [
    {
      "identifier": "calculation_day_definition",
      "raw_piece_count": 3,
      "content_piece_count": 3,
      "raw_pieces": [
        "calculation",
        "day",
        "definition"
      ],
      "content_pieces": [
        "calculation",
        "day",
        "definition"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 1,
      "source_grounded_content_piece_count": 2,
      "advisory_grounded_content_piece_count": 2,
      "source_grounded_content_piece_ratio": 0.6666666666666666,
      "advisory_grounded_content_piece_ratio": 0.6666666666666666
    },
    {
      "identifier": "calculation_day",
      "raw_piece_count": 2,
      "content_piece_count": 2,
      "raw_pieces": [
        "calculation",
        "day"
      ],
      "content_pieces": [
        "calculation",
        "day"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 0,
      "source_grounded_content_piece_count": 2,
      "advisory_grounded_content_piece_count": 2,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    }
  ],
  "entity_relation_target_fusion_examples": [],
  "conditional_relation_name_packing_examples": []
}
```

## parameterization

```json
{
  "callable_symbol_count": 1,
  "callable_symbol_with_args_count": 1,
  "top_level_parameter_slot_count": 1,
  "quantifier_parameter_slot_count": 1,
  "total_parameter_slot_mass": 2,
  "factorization_count": 1,
  "parameter_slots_per_factor": 1.0,
  "factorization_index": 1.0,
  "focus_symbol_signature": "missing",
  "focus_symbol_arity": null
}
```

## assertion_complexity

```json
{
  "assertion_count": 1,
  "mean_assertion_node_count": 25,
  "max_assertion_node_count": 25,
  "total_assertion_node_count": 25,
  "mean_assertion_depth": 6,
  "max_assertion_depth": 6,
  "total_ite_count": 0,
  "max_ite_count_per_assertion": 0,
  "total_quantifier_count": 1,
  "total_connective_count": 2,
  "total_branching_point_count": 5,
  "max_branching_point_count_per_assertion": 5,
  "mean_call_count_per_assertion": 6,
  "single_assertion_logic_share": 1.0,
  "overcompressed_single_assertion_flag": 0,
  "top_complex_assertions": [
    {
      "name": "calculation_day_definition",
      "assert_kind": "constraint",
      "node_count": 25,
      "depth": 6,
      "ite_count": 0,
      "quantifier_count": 1,
      "connective_count": 2,
      "branching_point_count": 5,
      "max_fanout": 5,
      "call_count": 6
    }
  ],
  "normalized_clause_count": 1,
  "node_count_per_normalized_clause": 25.0,
  "branching_point_count_per_normalized_clause": 5.0
}
```

## normalized_alignment

```json
{
  "normalized_clause_count": 1,
  "logic_block_count": 1,
  "clause_to_logic_block_ratio": 1.0,
  "logic_block_to_clause_ratio": 1.0,
  "clause_underdecomposition_mass": 0,
  "clause_overdecomposition_mass": 0,
  "focus_symbol_arity": null,
  "helper_factorization_count": 1,
  "single_assertion_logic_share": 1.0,
  "underdecomposed_logic_flag": 0
}
```

## normalized_relative

```json
{
  "new_formula_content_token_rate_vs_reference_mass": 0.5,
  "new_full_surface_content_token_rate_vs_reference_mass": 5.25,
  "formula_repeat_overuse_rate": 2.75,
  "full_surface_repeat_overuse_rate": 9.5,
  "parameter_slot_mass_per_clause": 2.0,
  "parameter_slot_mass_per_reference_token": 0.5,
  "factorization_per_clause": 1.0,
  "factorization_per_reference_token": 0.25,
  "notes_content_token_rate_vs_reference_mass": 5.75
}
```

## tradeoff

```json
{
  "render_bertscore_f1_to_normalized_per_parameter_slot_mass": 0.3730396032333374,
  "render_bertscore_f1_to_source_per_parameter_slot_mass": 0.3730396032333374,
  "render_nli_ir_implies_text_per_parameter_slot_mass": 0.2817618250846863,
  "render_nli_text_implies_ir_per_parameter_slot_mass": 0.4273165762424469,
  "render_bertscore_f1_to_normalized_per_formula_repeat_overuse_mass": 0.06782538240606134,
  "render_nli_text_implies_ir_per_formula_repeat_overuse_mass": 0.07769392295317216,
  "render_nli_ir_implies_text_per_formula_repeat_overuse_mass": 0.051229422742670234,
  "render_bertscore_f1_to_normalized_per_full_surface_repeat_overuse_mass": 0.01963366332807039,
  "render_nli_text_implies_ir_per_full_surface_repeat_overuse_mass": 0.02249034611802352,
  "pairwise_structure_similarity_mean_per_parameter_slot_mass": null,
  "focus_signature_mode_share_per_parameter_slot_mass": 0.5
}
```

## variants

```json
{
  "candidate_reading_count": 0,
  "draft_variant_count": 1,
  "unique_ir_variant_count": 1,
  "critic_selected_reading_id": "MANUAL",
  "critic_selected_reading_label": "Manual section workspace current IR",
  "critic_confidence_label": "",
  "critic_confidence_score": null,
  "critic_merge_recommended": false
}
```

## variability

```json
{
  "usable_variant_count": 1,
  "unique_variant_signature_count": 1,
  "focus_signature_unique_count": 1,
  "focus_signatures": {
    "missing": 1
  },
  "artifact_signature_entropy": 0.0,
  "focus_signature_entropy": 0.0,
  "focus_signature_mode_share": 1.0,
  "pairwise_structure_similarity_mean": null,
  "pairwise_structure_distance_mean": null,
  "pairwise_token_jaccard_mean": null,
  "parameter_slot_mass_mean": 2.0,
  "parameter_slot_mass_stddev": 0.0,
  "factorization_count_mean": 1.0,
  "factorization_count_stddev": 0.0,
  "same_parameter_mass_different_structure_pair_count": 0,
  "selected_ir_is_mode": true
}
```

## efficiency

```json
{
  "observable_llm_call_lower_bound": 0,
  "qa_json_attempt_count": 0,
  "critic_json_attempt_count": 0,
  "advisor_assistant_turn_count_lower_bound": 0,
  "selected_drafter_assistant_turn_count_lower_bound": 0,
  "wall_clock_seconds": null,
  "max_call_latency_s": null
}
```

## render_back

```json
{
  "render_back_mode": "deterministic_proxy",
  "render_back_metric_status": "proxy_only_until_llm_verbalizer_runs",
  "render_back_text": "constraint calculation day definition states that for every d of type day, calculation day for d if and only if (weekday of for d equals monday, weekday of for d equals tuesday, weekday of for d equals wednesday, weekday of for d equals thursday, or weekday of for d equals friday). calculation day holds between day.",
  "render_bertscore_precision_to_normalized": 0.7045909762382507,
  "render_bertscore_recall_to_normalized": 0.7927590012550354,
  "render_bertscore_f1_to_normalized": 0.7460792064666748,
  "render_bertscore_precision_to_source": 0.7045909762382507,
  "render_bertscore_recall_to_source": 0.7927590012550354,
  "render_bertscore_f1_to_source": 0.7460792064666748,
  "render_nli_ir_implies_text": 0.5635236501693726,
  "render_nli_text_implies_ir": 0.8546331524848938,
  "render_nli_ir_implies_source": 0.5635236501693726,
  "render_nli_source_implies_ir": 0.8546331524848938,
  "render_nli_render_to_normalized": {
    "entailment": 0.5635236501693726,
    "neutral": 0.11101686209440231,
    "contradiction": 0.32545948028564453
  },
  "render_nli_normalized_to_render": {
    "entailment": 0.8546331524848938,
    "neutral": 0.09162487089633942,
    "contradiction": 0.053742021322250366
  },
  "render_nli_render_to_source": {
    "entailment": 0.5635236501693726,
    "neutral": 0.11101686209440231,
    "contradiction": 0.32545948028564453
  },
  "render_nli_source_to_render": {
    "entailment": 0.8546331524848938,
    "neutral": 0.09162487089633942,
    "contradiction": 0.053742021322250366
  },
  "render_contradiction_score": 0.32545948028564453
}
```

## silver_reference

```json
{
  "disabled_for_manual_reference": false,
  "silver_reference_found": false,
  "silver_reference_path": "D:\\OneDrive\\Documents\\Study\\MIPT\\VKR\\research_experiments\\2026-02_pipeline\\IR\\outputs\\runs\\silver_baseline\\definitions_full6_multivariant_critic_v1_with_gold.md",
  "silver_reference_ir": "",
  "top_level_cosine": null,
  "logic_cosine": null,
  "arity_cosine": null,
  "silver_structure_similarity": null
}
```
