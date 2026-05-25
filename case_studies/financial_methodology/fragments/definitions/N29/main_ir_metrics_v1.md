# Translation Metrics v1 - N29

- generated_at: `2026-05-10T20:12:41.784103+02:00`
- artifact_path: `<PRIVATE_WORKSPACE>\case_studies\financial_methodology\definitions\N29\N29_manual_section_workspace_artifact_current_v1.json`
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
  "new_formula_token_count_vs_text_only": 6,
  "new_formula_content_token_count_vs_text_only": 6,
  "new_formula_token_count_vs_text_prelude_only": 6,
  "new_formula_content_token_count_vs_text_prelude_only": 6,
  "new_formula_token_count_vs_text_prelude_advisory": 6,
  "new_formula_content_token_count_vs_text_prelude_advisory": 6,
  "new_full_surface_token_count_vs_text_only": 29,
  "new_full_surface_content_token_count_vs_text_only": 25,
  "new_full_surface_token_count_vs_text_prelude_only": 27,
  "new_full_surface_content_token_count_vs_text_prelude_only": 24,
  "new_full_surface_token_count_vs_text_prelude_advisory": 27,
  "new_full_surface_content_token_count_vs_text_prelude_advisory": 24,
  "new_formula_content_tokens_vs_text_only": [
    "definedterm",
    "documentpart",
    "section1_3",
    "start_date_meaning_defined_in_section_1_3",
    "startdateterm",
    "term_shall_have_meaning_defined_in_section"
  ],
  "new_formula_content_tokens_vs_text_prelude_only": [
    "definedterm",
    "documentpart",
    "section1_3",
    "start_date_meaning_defined_in_section_1_3",
    "startdateterm",
    "term_shall_have_meaning_defined_in_section"
  ],
  "new_formula_content_tokens_vs_text_prelude_advisory": [
    "definedterm",
    "documentpart",
    "section1_3",
    "start_date_meaning_defined_in_section_1_3",
    "startdateterm",
    "term_shall_have_meaning_defined_in_section"
  ],
  "new_full_surface_content_tokens_vs_text_only": [
    "a4v3",
    "canonical",
    "computation",
    "current",
    "definedterm",
    "deterministic",
    "documentpart",
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
    "section-level",
    "section1_3",
    "start_date_meaning_defined_in_section_1_3",
    "startdateterm",
    "strengths",
    "term_shall_have_meaning_defined_in_section",
    "text",
    "workspace"
  ],
  "new_full_surface_content_tokens_vs_text_prelude_only": [
    "canonical",
    "computation",
    "current",
    "definedterm",
    "deterministic",
    "documentpart",
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
    "section-level",
    "section1_3",
    "start_date_meaning_defined_in_section_1_3",
    "startdateterm",
    "strengths",
    "term_shall_have_meaning_defined_in_section",
    "text",
    "workspace"
  ],
  "new_full_surface_content_tokens_vs_text_prelude_advisory": [
    "canonical",
    "computation",
    "current",
    "definedterm",
    "deterministic",
    "documentpart",
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
    "section-level",
    "section1_3",
    "start_date_meaning_defined_in_section_1_3",
    "startdateterm",
    "strengths",
    "term_shall_have_meaning_defined_in_section",
    "text",
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
  "source_content_token_count": 3,
  "source_content_token_mass": 6,
  "formula_content_token_count": 11,
  "formula_content_token_mass": 25,
  "full_surface_content_token_count": 33,
  "full_surface_content_token_mass": 52,
  "formula_content_token_recall": 1.0,
  "full_surface_content_token_recall": 1.0,
  "full_surface_content_token_jaccard": 0.09090909090909091,
  "formula_content_token_multiset_recall": 1.0,
  "formula_content_token_multiset_precision": 0.24,
  "formula_repeat_overuse_token_count": 10,
  "formula_repeat_overuse_mass": 19,
  "formula_repeat_underuse_token_count": 0,
  "formula_repeat_underuse_mass": 0,
  "formula_repeat_overuse_examples": [
    {
      "token": "definedterm",
      "current_count": 3,
      "baseline_count": 0,
      "delta": 3
    },
    {
      "token": "defined",
      "current_count": 3,
      "baseline_count": 1,
      "delta": 2
    },
    {
      "token": "meaning",
      "current_count": 3,
      "baseline_count": 1,
      "delta": 2
    },
    {
      "token": "section",
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
      "token": "section1",
      "current_count": 2,
      "baseline_count": 0,
      "delta": 2
    },
    {
      "token": "startdateterm",
      "current_count": 2,
      "baseline_count": 0,
      "delta": 2
    },
    {
      "token": "term",
      "current_count": 2,
      "baseline_count": 0,
      "delta": 2
    },
    {
      "token": "have",
      "current_count": 2,
      "baseline_count": 1,
      "delta": 1
    },
    {
      "token": "shall",
      "current_count": 2,
      "baseline_count": 1,
      "delta": 1
    }
  ],
  "full_surface_content_token_multiset_recall": 1.0,
  "full_surface_content_token_multiset_precision": 0.11538461538461539,
  "full_surface_repeat_overuse_token_count": 32,
  "full_surface_repeat_overuse_mass": 46,
  "full_surface_repeat_underuse_token_count": 0,
  "full_surface_repeat_underuse_mass": 0,
  "full_surface_repeat_overuse_examples": [
    {
      "token": "section",
      "current_count": 5,
      "baseline_count": 1,
      "delta": 4
    },
    {
      "token": "definedterm",
      "current_count": 3,
      "baseline_count": 0,
      "delta": 3
    },
    {
      "token": "defined",
      "current_count": 3,
      "baseline_count": 1,
      "delta": 2
    },
    {
      "token": "meaning",
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
      "token": "startdateterm",
      "current_count": 2,
      "baseline_count": 0,
      "delta": 2
    },
    {
      "token": "term",
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
      "token": "have",
      "current_count": 2,
      "baseline_count": 1,
      "delta": 1
    },
    {
      "token": "shall",
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
  "source_excerpt_content_token_count": 3,
  "source_excerpt_content_token_mass": 6,
  "normalized_content_token_count": 3,
  "normalized_content_token_mass": 6,
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
  "normalized_content_mass_per_clause": 6.0,
  "source_normalized_bertscore_precision": 1.0,
  "source_normalized_bertscore_recall": 1.0,
  "source_normalized_bertscore_f1": 1.0,
  "normalized_implies_source_entailment": 0.9641603827476501,
  "source_implies_normalized_entailment": 0.9641603827476501,
  "source_vs_normalized_contradiction_score": 0.02664381079375744
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
  "notes_to_formula_content_ratio": 2.090909090909091
}
```

## identifier_glue

```json
{
  "identifier_count": 5,
  "compound_identifier_count_raw": 1,
  "compound_identifier_count_content": 1,
  "compound_identifier_rate_raw": 0.2,
  "compound_identifier_rate_content": 0.2,
  "max_identifier_piece_count_raw": 7,
  "max_identifier_piece_count_content": 6,
  "mean_identifier_piece_count_raw": 3.2,
  "mean_identifier_piece_count_content": 2.6,
  "identifier_glue_excess_mass_raw": 4,
  "identifier_glue_excess_mass_content": 4,
  "identifier_glue_excess_rate_raw": 0.8,
  "identifier_glue_excess_rate_content": 0.8,
  "source_grounded_content_piece_ratio_mean": 0.3666666666666667,
  "advisory_grounded_content_piece_ratio_mean": 0.3666666666666667,
  "low_source_grounded_glued_identifier_count": 0,
  "low_source_grounded_glued_identifier_rate": 0.0,
  "entity_relation_target_fusion_count": 0,
  "entity_relation_target_fusion_rate": 0.0,
  "conditional_relation_name_packing_count": 0,
  "conditional_relation_name_packing_rate": 0.0,
  "top_glued_identifiers": [
    {
      "identifier": "term_shall_have_meaning_defined_in_section",
      "raw_piece_count": 7,
      "content_piece_count": 6,
      "raw_pieces": [
        "term",
        "shall",
        "have",
        "meaning",
        "defined",
        "in",
        "section"
      ],
      "content_pieces": [
        "term",
        "shall",
        "have",
        "meaning",
        "defined",
        "section"
      ],
      "glue_excess_raw": 4,
      "glue_excess_content": 4,
      "source_grounded_content_piece_count": 5,
      "advisory_grounded_content_piece_count": 5,
      "source_grounded_content_piece_ratio": 0.8333333333333334,
      "advisory_grounded_content_piece_ratio": 0.8333333333333334
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
      "identifier": "Section1_3",
      "raw_piece_count": 2,
      "content_piece_count": 1,
      "raw_pieces": [
        "section1",
        "3"
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
      "identifier": "DefinedTerm",
      "raw_piece_count": 2,
      "content_piece_count": 2,
      "raw_pieces": [
        "defined",
        "term"
      ],
      "content_pieces": [
        "defined",
        "term"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 0,
      "source_grounded_content_piece_count": 1,
      "advisory_grounded_content_piece_count": 1,
      "source_grounded_content_piece_ratio": 0.5,
      "advisory_grounded_content_piece_ratio": 0.5
    },
    {
      "identifier": "StartDateTerm",
      "raw_piece_count": 3,
      "content_piece_count": 2,
      "raw_pieces": [
        "start",
        "date",
        "term"
      ],
      "content_pieces": [
        "start",
        "term"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 0,
      "source_grounded_content_piece_count": 1,
      "advisory_grounded_content_piece_count": 1,
      "source_grounded_content_piece_ratio": 0.5,
      "advisory_grounded_content_piece_ratio": 0.5
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
      "identifier": "DefinedTerm",
      "raw_piece_count": 2,
      "content_piece_count": 2,
      "raw_pieces": [
        "defined",
        "term"
      ],
      "content_pieces": [
        "defined",
        "term"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 0,
      "source_grounded_content_piece_count": 1,
      "advisory_grounded_content_piece_count": 1,
      "source_grounded_content_piece_ratio": 0.5,
      "advisory_grounded_content_piece_ratio": 0.5
    },
    {
      "identifier": "StartDateTerm",
      "raw_piece_count": 3,
      "content_piece_count": 2,
      "raw_pieces": [
        "start",
        "date",
        "term"
      ],
      "content_pieces": [
        "start",
        "term"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 0,
      "source_grounded_content_piece_count": 1,
      "advisory_grounded_content_piece_count": 1,
      "source_grounded_content_piece_ratio": 0.5,
      "advisory_grounded_content_piece_ratio": 0.5
    },
    {
      "identifier": "term_shall_have_meaning_defined_in_section",
      "raw_piece_count": 7,
      "content_piece_count": 6,
      "raw_pieces": [
        "term",
        "shall",
        "have",
        "meaning",
        "defined",
        "in",
        "section"
      ],
      "content_pieces": [
        "term",
        "shall",
        "have",
        "meaning",
        "defined",
        "section"
      ],
      "glue_excess_raw": 4,
      "glue_excess_content": 4,
      "source_grounded_content_piece_count": 5,
      "advisory_grounded_content_piece_count": 5,
      "source_grounded_content_piece_ratio": 0.8333333333333334,
      "advisory_grounded_content_piece_ratio": 0.8333333333333334
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
  "top_level_parameter_slot_count": 2,
  "quantifier_parameter_slot_count": 0,
  "total_parameter_slot_mass": 2,
  "factorization_count": 1,
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
  "helper_factorization_count": 1,
  "single_assertion_logic_share": null,
  "underdecomposed_logic_flag": 0
}
```

## normalized_relative

```json
{
  "new_formula_content_token_rate_vs_reference_mass": 1.0,
  "new_full_surface_content_token_rate_vs_reference_mass": 4.0,
  "formula_repeat_overuse_rate": 3.1666666666666665,
  "full_surface_repeat_overuse_rate": 7.666666666666667,
  "parameter_slot_mass_per_clause": 2.0,
  "parameter_slot_mass_per_reference_token": 0.3333333333333333,
  "factorization_per_clause": 1.0,
  "factorization_per_reference_token": 0.16666666666666666,
  "notes_content_token_rate_vs_reference_mass": 3.8333333333333335
}
```

## tradeoff

```json
{
  "render_bertscore_f1_to_normalized_per_parameter_slot_mass": 0.39993903040885925,
  "render_bertscore_f1_to_source_per_parameter_slot_mass": 0.39993903040885925,
  "render_nli_ir_implies_text_per_parameter_slot_mass": 0.011529526673257351,
  "render_nli_text_implies_ir_per_parameter_slot_mass": 0.06702487915754318,
  "render_bertscore_f1_to_normalized_per_formula_repeat_overuse_mass": 0.04209884530619571,
  "render_nli_text_implies_ir_per_formula_repeat_overuse_mass": 0.007055250437636124,
  "render_nli_ir_implies_text_per_formula_repeat_overuse_mass": 0.0012136343866586685,
  "render_bertscore_f1_to_normalized_per_full_surface_repeat_overuse_mass": 0.017388653496037357,
  "render_nli_text_implies_ir_per_full_surface_repeat_overuse_mass": 0.0029141251807627473,
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
  "render_back_text": "defined term is a type. start date term is a distinguished entity. section1 3 is a distinguished entity. term shall have meaning defined in section holds between defined term and document part.",
  "render_bertscore_precision_to_normalized": 0.7669438123703003,
  "render_bertscore_recall_to_normalized": 0.8357677459716797,
  "render_bertscore_f1_to_normalized": 0.7998780608177185,
  "render_bertscore_precision_to_source": 0.7669438123703003,
  "render_bertscore_recall_to_source": 0.8357677459716797,
  "render_bertscore_f1_to_source": 0.7998780608177185,
  "render_nli_ir_implies_text": 0.023059053346514702,
  "render_nli_text_implies_ir": 0.13404975831508636,
  "render_nli_ir_implies_source": 0.023059053346514702,
  "render_nli_source_implies_ir": 0.13404975831508636,
  "render_nli_render_to_normalized": {
    "entailment": 0.023059053346514702,
    "neutral": 0.030392961576581,
    "contradiction": 0.9465479254722595
  },
  "render_nli_normalized_to_render": {
    "entailment": 0.13404975831508636,
    "neutral": 0.7531611323356628,
    "contradiction": 0.11278906464576721
  },
  "render_nli_render_to_source": {
    "entailment": 0.023059053346514702,
    "neutral": 0.030392961576581,
    "contradiction": 0.9465479254722595
  },
  "render_nli_source_to_render": {
    "entailment": 0.13404975831508636,
    "neutral": 0.7531611323356628,
    "contradiction": 0.11278906464576721
  },
  "render_contradiction_score": 0.9465479254722595
}
```

## silver_reference

```json
{
  "disabled_for_manual_reference": false,
  "silver_reference_found": false,
  "silver_reference_path": "<PRIVATE_WORKSPACE>\\IR\\outputs\\runs\\silver_baseline\\definitions_full6_multivariant_critic_v1_with_gold.md",
  "silver_reference_ir": "",
  "top_level_cosine": null,
  "logic_cosine": null,
  "arity_cosine": null,
  "silver_structure_similarity": null
}
```
