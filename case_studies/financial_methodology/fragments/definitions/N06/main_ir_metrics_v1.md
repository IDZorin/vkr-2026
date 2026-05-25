# Translation Metrics v1 - N06

- generated_at: `2026-05-12T14:18:49.697964+02:00`
- artifact_path: `D:\OneDrive\Documents\Study\MIPT\VKR\research_experiments\2026-02_pipeline\case_studies\financial_methodology\definitions\N06\N06_manual_section_workspace_artifact_current_v1.json`
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
  "ungrounded_sort_count": 2,
  "ungrounded_ref_count": 0,
  "ungrounded_callee_count": 0,
  "prelude_redeclaration_count": 0,
  "origin_error_count": 2,
  "new_formula_token_count_vs_text_only": 8,
  "new_formula_content_token_count_vs_text_only": 8,
  "new_formula_token_count_vs_text_prelude_only": 8,
  "new_formula_content_token_count_vs_text_prelude_only": 8,
  "new_formula_token_count_vs_text_prelude_advisory": 8,
  "new_formula_content_token_count_vs_text_prelude_advisory": 8,
  "new_full_surface_token_count_vs_text_only": 31,
  "new_full_surface_content_token_count_vs_text_only": 27,
  "new_full_surface_token_count_vs_text_prelude_only": 29,
  "new_full_surface_content_token_count_vs_text_prelude_only": 26,
  "new_full_surface_token_count_vs_text_prelude_advisory": 29,
  "new_full_surface_content_token_count_vs_text_prelude_advisory": 26,
  "new_formula_content_tokens_vs_text_only": [
    "calculation_time_of_closing_level_of_index",
    "calculationtime",
    "close_of_business_definition",
    "closeofbusiness",
    "documentpart",
    "outlined_in_section",
    "section1_4",
    "theindex"
  ],
  "new_formula_content_tokens_vs_text_prelude_only": [
    "calculation_time_of_closing_level_of_index",
    "calculationtime",
    "close_of_business_definition",
    "closeofbusiness",
    "documentpart",
    "outlined_in_section",
    "section1_4",
    "theindex"
  ],
  "new_formula_content_tokens_vs_text_prelude_advisory": [
    "calculation_time_of_closing_level_of_index",
    "calculationtime",
    "close_of_business_definition",
    "closeofbusiness",
    "documentpart",
    "outlined_in_section",
    "section1_4",
    "theindex"
  ],
  "new_full_surface_content_tokens_vs_text_only": [
    "a4v3",
    "calculation_time_of_closing_level_of_index",
    "calculationtime",
    "canonical",
    "close_of_business_definition",
    "closeofbusiness",
    "computation",
    "current",
    "deterministic",
    "documentpart",
    "draft",
    "main_ir",
    "manual",
    "metric",
    "outlined_in_section",
    "parsed",
    "primitive_usage",
    "recomputation",
    "reconstructed",
    "rendering_notes",
    "residual_risks",
    "section-level",
    "section1_4",
    "strengths",
    "text",
    "theindex",
    "workspace"
  ],
  "new_full_surface_content_tokens_vs_text_prelude_only": [
    "calculation_time_of_closing_level_of_index",
    "calculationtime",
    "canonical",
    "close_of_business_definition",
    "closeofbusiness",
    "computation",
    "current",
    "deterministic",
    "documentpart",
    "draft",
    "main_ir",
    "manual",
    "metric",
    "outlined_in_section",
    "parsed",
    "primitive_usage",
    "recomputation",
    "reconstructed",
    "rendering_notes",
    "residual_risks",
    "section-level",
    "section1_4",
    "strengths",
    "text",
    "theindex",
    "workspace"
  ],
  "new_full_surface_content_tokens_vs_text_prelude_advisory": [
    "calculation_time_of_closing_level_of_index",
    "calculationtime",
    "canonical",
    "close_of_business_definition",
    "closeofbusiness",
    "computation",
    "current",
    "deterministic",
    "documentpart",
    "draft",
    "main_ir",
    "manual",
    "metric",
    "outlined_in_section",
    "parsed",
    "primitive_usage",
    "recomputation",
    "reconstructed",
    "rendering_notes",
    "residual_risks",
    "section-level",
    "section1_4",
    "strengths",
    "text",
    "theindex",
    "workspace"
  ]
}
```

## coverage

```json
{
  "normalized_clause_count": 1,
  "formula_bearing_item_count": 0,
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
  "source_content_token_count": 8,
  "source_content_token_mass": 9,
  "formula_content_token_count": 15,
  "formula_content_token_mass": 33,
  "full_surface_content_token_count": 36,
  "full_surface_content_token_mass": 60,
  "formula_content_token_recall": 1.0,
  "full_surface_content_token_recall": 1.0,
  "full_surface_content_token_jaccard": 0.2222222222222222,
  "formula_content_token_multiset_recall": 1.0,
  "formula_content_token_multiset_precision": 0.2727272727272727,
  "formula_repeat_overuse_token_count": 13,
  "formula_repeat_overuse_mass": 24,
  "formula_repeat_underuse_token_count": 0,
  "formula_repeat_underuse_mass": 0,
  "formula_repeat_overuse_examples": [
    {
      "token": "index",
      "current_count": 5,
      "baseline_count": 1,
      "delta": 4
    },
    {
      "token": "calculationtime",
      "current_count": 4,
      "baseline_count": 0,
      "delta": 4
    },
    {
      "token": "closeofbusiness",
      "current_count": 3,
      "baseline_count": 0,
      "delta": 3
    },
    {
      "token": "documentpart",
      "current_count": 2,
      "baseline_count": 0,
      "delta": 2
    },
    {
      "token": "section1",
      "current_count": 2,
      "baseline_count": 0,
      "delta": 2
    },
    {
      "token": "theindex",
      "current_count": 2,
      "baseline_count": 0,
      "delta": 2
    },
    {
      "token": "calculation",
      "current_count": 2,
      "baseline_count": 1,
      "delta": 1
    },
    {
      "token": "closing",
      "current_count": 2,
      "baseline_count": 1,
      "delta": 1
    },
    {
      "token": "level",
      "current_count": 2,
      "baseline_count": 1,
      "delta": 1
    },
    {
      "token": "outlined",
      "current_count": 2,
      "baseline_count": 1,
      "delta": 1
    },
    {
      "token": "section",
      "current_count": 2,
      "baseline_count": 1,
      "delta": 1
    },
    {
      "token": "time",
      "current_count": 2,
      "baseline_count": 1,
      "delta": 1
    },
    {
      "token": "definition",
      "current_count": 1,
      "baseline_count": 0,
      "delta": 1
    }
  ],
  "full_surface_content_token_multiset_recall": 1.0,
  "full_surface_content_token_multiset_precision": 0.15,
  "full_surface_repeat_overuse_token_count": 34,
  "full_surface_repeat_overuse_mass": 51,
  "full_surface_repeat_underuse_token_count": 0,
  "full_surface_repeat_underuse_mass": 0,
  "full_surface_repeat_overuse_examples": [
    {
      "token": "index",
      "current_count": 5,
      "baseline_count": 1,
      "delta": 4
    },
    {
      "token": "calculationtime",
      "current_count": 4,
      "baseline_count": 0,
      "delta": 4
    },
    {
      "token": "section",
      "current_count": 4,
      "baseline_count": 1,
      "delta": 3
    },
    {
      "token": "closeofbusiness",
      "current_count": 3,
      "baseline_count": 0,
      "delta": 3
    },
    {
      "token": "level",
      "current_count": 3,
      "baseline_count": 1,
      "delta": 2
    },
    {
      "token": "documentpart",
      "current_count": 2,
      "baseline_count": 0,
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
      "token": "section1",
      "current_count": 2,
      "baseline_count": 0,
      "delta": 2
    },
    {
      "token": "theindex",
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
      "token": "calculation",
      "current_count": 2,
      "baseline_count": 1,
      "delta": 1
    },
    {
      "token": "closing",
      "current_count": 2,
      "baseline_count": 1,
      "delta": 1
    },
    {
      "token": "outlined",
      "current_count": 2,
      "baseline_count": 1,
      "delta": 1
    },
    {
      "token": "time",
      "current_count": 2,
      "baseline_count": 1,
      "delta": 1
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
    }
  ],
  "source_to_formula_token_gap_count": 0,
  "source_to_full_surface_token_gap_count": 0,
  "source_content_tokens_missing_from_formula": [],
  "source_content_tokens_missing_from_full_surface": []
}
```

## source_vs_normalized

```json
{
  "source_excerpt_content_token_count": 8,
  "source_excerpt_content_token_mass": 9,
  "normalized_content_token_count": 8,
  "normalized_content_token_mass": 9,
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
  "normalized_content_mass_per_clause": 9.0,
  "source_normalized_bertscore_precision": 1.0,
  "source_normalized_bertscore_recall": 1.0,
  "source_normalized_bertscore_f1": 1.0,
  "normalized_implies_source_entailment": 0.9837480783462524,
  "source_implies_normalized_entailment": 0.9837480783462524,
  "source_vs_normalized_contradiction_score": 0.008347575552761555
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
  "declaration_only_downgrade_flag": 1,
  "definition_body_present": 0,
  "vacuous_constraint_flag": 0,
  "reflexive_equality_count": 0
}
```

## compression

```json
{
  "notes_token_count": 29,
  "notes_content_token_count": 23,
  "notes_to_formula_content_ratio": 1.5333333333333334
}
```

## identifier_glue

```json
{
  "identifier_count": 8,
  "compound_identifier_count_raw": 1,
  "compound_identifier_count_content": 1,
  "compound_identifier_rate_raw": 0.125,
  "compound_identifier_rate_content": 0.125,
  "max_identifier_piece_count_raw": 7,
  "max_identifier_piece_count_content": 5,
  "mean_identifier_piece_count_raw": 2.75,
  "mean_identifier_piece_count_content": 2,
  "identifier_glue_excess_mass_raw": 4,
  "identifier_glue_excess_mass_content": 3,
  "identifier_glue_excess_rate_raw": 0.5,
  "identifier_glue_excess_rate_content": 0.375,
  "source_grounded_content_piece_ratio_mean": 0.75,
  "advisory_grounded_content_piece_ratio_mean": 0.75,
  "low_source_grounded_glued_identifier_count": 0,
  "low_source_grounded_glued_identifier_rate": 0.0,
  "entity_relation_target_fusion_count": 0,
  "entity_relation_target_fusion_rate": 0.0,
  "conditional_relation_name_packing_count": 0,
  "conditional_relation_name_packing_rate": 0.0,
  "top_glued_identifiers": [
    {
      "identifier": "calculation_time_of_closing_level_of_index",
      "raw_piece_count": 7,
      "content_piece_count": 5,
      "raw_pieces": [
        "calculation",
        "time",
        "of",
        "closing",
        "level",
        "of",
        "index"
      ],
      "content_pieces": [
        "calculation",
        "time",
        "closing",
        "level",
        "index"
      ],
      "glue_excess_raw": 4,
      "glue_excess_content": 3,
      "source_grounded_content_piece_count": 5,
      "advisory_grounded_content_piece_count": 5,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    },
    {
      "identifier": "DocumentPart",
      "raw_piece_count": 2,
      "content_piece_count": 2,
      "raw_pieces": [
        "document",
        "part"
      ],
      "content_pieces": [
        "document",
        "part"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 0,
      "source_grounded_content_piece_count": 0,
      "advisory_grounded_content_piece_count": 0,
      "source_grounded_content_piece_ratio": 0.0,
      "advisory_grounded_content_piece_ratio": 0.0
    },
    {
      "identifier": "Section1_4",
      "raw_piece_count": 2,
      "content_piece_count": 1,
      "raw_pieces": [
        "section1",
        "4"
      ],
      "content_pieces": [
        "section1"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 0,
      "source_grounded_content_piece_count": 0,
      "advisory_grounded_content_piece_count": 0,
      "source_grounded_content_piece_ratio": 0.0,
      "advisory_grounded_content_piece_ratio": 0.0
    },
    {
      "identifier": "CalculationTime",
      "raw_piece_count": 2,
      "content_piece_count": 2,
      "raw_pieces": [
        "calculation",
        "time"
      ],
      "content_pieces": [
        "calculation",
        "time"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 0,
      "source_grounded_content_piece_count": 2,
      "advisory_grounded_content_piece_count": 2,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    },
    {
      "identifier": "CloseOfBusiness",
      "raw_piece_count": 3,
      "content_piece_count": 2,
      "raw_pieces": [
        "close",
        "of",
        "business"
      ],
      "content_pieces": [
        "close",
        "business"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 0,
      "source_grounded_content_piece_count": 2,
      "advisory_grounded_content_piece_count": 2,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    },
    {
      "identifier": "outlined_in_section",
      "raw_piece_count": 3,
      "content_piece_count": 2,
      "raw_pieces": [
        "outlined",
        "in",
        "section"
      ],
      "content_pieces": [
        "outlined",
        "section"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 0,
      "source_grounded_content_piece_count": 2,
      "advisory_grounded_content_piece_count": 2,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    },
    {
      "identifier": "Index",
      "raw_piece_count": 1,
      "content_piece_count": 1,
      "raw_pieces": [
        "index"
      ],
      "content_pieces": [
        "index"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 0,
      "source_grounded_content_piece_count": 1,
      "advisory_grounded_content_piece_count": 1,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    },
    {
      "identifier": "TheIndex",
      "raw_piece_count": 2,
      "content_piece_count": 1,
      "raw_pieces": [
        "the",
        "index"
      ],
      "content_pieces": [
        "index"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 0,
      "source_grounded_content_piece_count": 1,
      "advisory_grounded_content_piece_count": 1,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    }
  ],
  "lowest_source_grounded_identifiers": [
    {
      "identifier": "DocumentPart",
      "raw_piece_count": 2,
      "content_piece_count": 2,
      "raw_pieces": [
        "document",
        "part"
      ],
      "content_pieces": [
        "document",
        "part"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 0,
      "source_grounded_content_piece_count": 0,
      "advisory_grounded_content_piece_count": 0,
      "source_grounded_content_piece_ratio": 0.0,
      "advisory_grounded_content_piece_ratio": 0.0
    },
    {
      "identifier": "calculation_time_of_closing_level_of_index",
      "raw_piece_count": 7,
      "content_piece_count": 5,
      "raw_pieces": [
        "calculation",
        "time",
        "of",
        "closing",
        "level",
        "of",
        "index"
      ],
      "content_pieces": [
        "calculation",
        "time",
        "closing",
        "level",
        "index"
      ],
      "glue_excess_raw": 4,
      "glue_excess_content": 3,
      "source_grounded_content_piece_count": 5,
      "advisory_grounded_content_piece_count": 5,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    },
    {
      "identifier": "CalculationTime",
      "raw_piece_count": 2,
      "content_piece_count": 2,
      "raw_pieces": [
        "calculation",
        "time"
      ],
      "content_pieces": [
        "calculation",
        "time"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 0,
      "source_grounded_content_piece_count": 2,
      "advisory_grounded_content_piece_count": 2,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    },
    {
      "identifier": "CloseOfBusiness",
      "raw_piece_count": 3,
      "content_piece_count": 2,
      "raw_pieces": [
        "close",
        "of",
        "business"
      ],
      "content_pieces": [
        "close",
        "business"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 0,
      "source_grounded_content_piece_count": 2,
      "advisory_grounded_content_piece_count": 2,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    },
    {
      "identifier": "outlined_in_section",
      "raw_piece_count": 3,
      "content_piece_count": 2,
      "raw_pieces": [
        "outlined",
        "in",
        "section"
      ],
      "content_pieces": [
        "outlined",
        "section"
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
  "callable_symbol_count": 2,
  "callable_symbol_with_args_count": 2,
  "top_level_parameter_slot_count": 4,
  "quantifier_parameter_slot_count": 0,
  "total_parameter_slot_mass": 4,
  "factorization_count": 2,
  "parameter_slots_per_factor": 2.0,
  "factorization_index": 0.5,
  "focus_symbol_signature": "missing",
  "focus_symbol_arity": null
}
```

## assertion_complexity

```json
{
  "assertion_count": 0,
  "mean_assertion_node_count": 0.0,
  "max_assertion_node_count": 0,
  "total_assertion_node_count": 0,
  "mean_assertion_depth": 0.0,
  "max_assertion_depth": 0,
  "total_ite_count": 0,
  "max_ite_count_per_assertion": 0,
  "total_quantifier_count": 0,
  "total_connective_count": 0,
  "total_branching_point_count": 0,
  "max_branching_point_count_per_assertion": 0,
  "mean_call_count_per_assertion": 0.0,
  "single_assertion_logic_share": null,
  "overcompressed_single_assertion_flag": 0,
  "top_complex_assertions": [],
  "normalized_clause_count": 1,
  "node_count_per_normalized_clause": 0.0,
  "branching_point_count_per_normalized_clause": 0.0
}
```

## normalized_alignment

```json
{
  "normalized_clause_count": 1,
  "logic_block_count": 0,
  "clause_to_logic_block_ratio": 1.0,
  "logic_block_to_clause_ratio": 0.0,
  "clause_underdecomposition_mass": 1,
  "clause_overdecomposition_mass": 0,
  "focus_symbol_arity": null,
  "helper_factorization_count": 2,
  "single_assertion_logic_share": null,
  "underdecomposed_logic_flag": 0
}
```

## normalized_relative

```json
{
  "new_formula_content_token_rate_vs_reference_mass": 0.8888888888888888,
  "new_full_surface_content_token_rate_vs_reference_mass": 2.888888888888889,
  "formula_repeat_overuse_rate": 2.6666666666666665,
  "full_surface_repeat_overuse_rate": 5.666666666666667,
  "parameter_slot_mass_per_clause": 4.0,
  "parameter_slot_mass_per_reference_token": 0.4444444444444444,
  "factorization_per_clause": 2.0,
  "factorization_per_reference_token": 0.2222222222222222,
  "notes_content_token_rate_vs_reference_mass": 2.5555555555555554
}
```

## tradeoff

```json
{
  "render_bertscore_f1_to_normalized_per_parameter_slot_mass": 0.19993270933628082,
  "render_bertscore_f1_to_source_per_parameter_slot_mass": 0.19993270933628082,
  "render_nli_ir_implies_text_per_parameter_slot_mass": 0.07273012399673462,
  "render_nli_text_implies_ir_per_parameter_slot_mass": 0.10722202062606812,
  "render_bertscore_f1_to_normalized_per_formula_repeat_overuse_mass": 0.03332211822271347,
  "render_nli_text_implies_ir_per_formula_repeat_overuse_mass": 0.017870336771011353,
  "render_nli_ir_implies_text_per_formula_repeat_overuse_mass": 0.012121687332789103,
  "render_bertscore_f1_to_normalized_per_full_surface_repeat_overuse_mass": 0.015680996810688692,
  "render_nli_text_implies_ir_per_full_surface_repeat_overuse_mass": 0.008409570245181812,
  "pairwise_structure_similarity_mean_per_parameter_slot_mass": null,
  "focus_signature_mode_share_per_parameter_slot_mass": 0.25
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
  "parameter_slot_mass_mean": 4.0,
  "parameter_slot_mass_stddev": 0.0,
  "factorization_count_mean": 2.0,
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
  "render_back_text": "index is a type. calculation time is a type. the index is a distinguished entity. close of business is a distinguished entity. section1 4 is a distinguished entity. calculation time of closing level of index holds between calculation time and index. outlined in section holds between calculation time and document part.",
  "render_bertscore_precision_to_normalized": 0.7720903754234314,
  "render_bertscore_recall_to_normalized": 0.8294238448143005,
  "render_bertscore_f1_to_normalized": 0.7997308373451233,
  "render_bertscore_precision_to_source": 0.7720903754234314,
  "render_bertscore_recall_to_source": 0.8294238448143005,
  "render_bertscore_f1_to_source": 0.7997308373451233,
  "render_nli_ir_implies_text": 0.2909204959869385,
  "render_nli_text_implies_ir": 0.42888808250427246,
  "render_nli_ir_implies_source": 0.2909204959869385,
  "render_nli_source_implies_ir": 0.42888808250427246,
  "render_nli_render_to_normalized": {
    "entailment": 0.2909204959869385,
    "neutral": 0.09210403263568878,
    "contradiction": 0.6169754266738892
  },
  "render_nli_normalized_to_render": {
    "entailment": 0.42888808250427246,
    "neutral": 0.5305228233337402,
    "contradiction": 0.0405891127884388
  },
  "render_nli_render_to_source": {
    "entailment": 0.2909204959869385,
    "neutral": 0.09210403263568878,
    "contradiction": 0.6169754266738892
  },
  "render_nli_source_to_render": {
    "entailment": 0.42888808250427246,
    "neutral": 0.5305228233337402,
    "contradiction": 0.0405891127884388
  },
  "render_contradiction_score": 0.6169754266738892
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
