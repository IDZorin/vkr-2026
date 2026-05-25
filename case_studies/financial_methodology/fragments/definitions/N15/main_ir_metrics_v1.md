# Translation Metrics v1 - N15

- generated_at: `2026-05-14T15:43:19.036791+02:00`
- artifact_path: `<PRIVATE_WORKSPACE>\case_studies\financial_methodology\definitions\N15\N15_manual_section_workspace_artifact_current_v1.json`
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
  "new_formula_token_count_vs_text_only": 11,
  "new_formula_content_token_count_vs_text_only": 10,
  "new_formula_token_count_vs_text_prelude_only": 10,
  "new_formula_content_token_count_vs_text_prelude_only": 9,
  "new_formula_token_count_vs_text_prelude_advisory": 10,
  "new_formula_content_token_count_vs_text_prelude_advisory": 9,
  "new_full_surface_token_count_vs_text_only": 34,
  "new_full_surface_content_token_count_vs_text_only": 29,
  "new_full_surface_token_count_vs_text_prelude_only": 31,
  "new_full_surface_content_token_count_vs_text_prelude_only": 27,
  "new_full_surface_token_count_vs_text_prelude_advisory": 31,
  "new_full_surface_content_token_count_vs_text_prelude_advisory": 27,
  "new_formula_content_tokens_vs_text_only": [
    "documentpart",
    "financialinstrument",
    "gbs_index_component",
    "gbs_index_component_definition",
    "gbs_index_specified_in_section",
    "gbs_index_specified_in_section_2_1",
    "gbsindex",
    "gbsindexspecifiedinsection2_1",
    "section2_1",
    "security_reflected_in_gbs_index"
  ],
  "new_formula_content_tokens_vs_text_prelude_only": [
    "documentpart",
    "gbs_index_component",
    "gbs_index_component_definition",
    "gbs_index_specified_in_section",
    "gbs_index_specified_in_section_2_1",
    "gbsindex",
    "gbsindexspecifiedinsection2_1",
    "section2_1",
    "security_reflected_in_gbs_index"
  ],
  "new_formula_content_tokens_vs_text_prelude_advisory": [
    "documentpart",
    "gbs_index_component",
    "gbs_index_component_definition",
    "gbs_index_specified_in_section",
    "gbs_index_specified_in_section_2_1",
    "gbsindex",
    "gbsindexspecifiedinsection2_1",
    "section2_1",
    "security_reflected_in_gbs_index"
  ],
  "new_full_surface_content_tokens_vs_text_only": [
    "a4v3",
    "canonical",
    "computation",
    "current",
    "deterministic",
    "documentpart",
    "draft",
    "financialinstrument",
    "gbs_index_component",
    "gbs_index_component_definition",
    "gbs_index_specified_in_section",
    "gbs_index_specified_in_section_2_1",
    "gbsindex",
    "gbsindexspecifiedinsection2_1",
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
    "section2_1",
    "security_reflected_in_gbs_index",
    "strengths",
    "text",
    "workspace"
  ],
  "new_full_surface_content_tokens_vs_text_prelude_only": [
    "canonical",
    "computation",
    "current",
    "deterministic",
    "documentpart",
    "draft",
    "gbs_index_component",
    "gbs_index_component_definition",
    "gbs_index_specified_in_section",
    "gbs_index_specified_in_section_2_1",
    "gbsindex",
    "gbsindexspecifiedinsection2_1",
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
    "section2_1",
    "security_reflected_in_gbs_index",
    "strengths",
    "text",
    "workspace"
  ],
  "new_full_surface_content_tokens_vs_text_prelude_advisory": [
    "canonical",
    "computation",
    "current",
    "deterministic",
    "documentpart",
    "draft",
    "gbs_index_component",
    "gbs_index_component_definition",
    "gbs_index_specified_in_section",
    "gbs_index_specified_in_section_2_1",
    "gbsindex",
    "gbsindexspecifiedinsection2_1",
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
    "section2_1",
    "security_reflected_in_gbs_index",
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
  "source_content_token_count": 6,
  "source_content_token_mass": 7,
  "formula_content_token_count": 12,
  "formula_content_token_mass": 40,
  "full_surface_content_token_count": 34,
  "full_surface_content_token_mass": 67,
  "formula_content_token_recall": 1.0,
  "full_surface_content_token_recall": 1.0,
  "full_surface_content_token_jaccard": 0.17647058823529413,
  "formula_content_token_multiset_recall": 1.0,
  "formula_content_token_multiset_precision": 0.175,
  "formula_repeat_overuse_token_count": 12,
  "formula_repeat_overuse_mass": 33,
  "formula_repeat_underuse_token_count": 0,
  "formula_repeat_underuse_mass": 0,
  "formula_repeat_overuse_examples": [
    {
      "token": "index",
      "current_count": 8,
      "baseline_count": 2,
      "delta": 6
    },
    {
      "token": "security",
      "current_count": 6,
      "baseline_count": 1,
      "delta": 5
    },
    {
      "token": "gbsindex",
      "current_count": 5,
      "baseline_count": 0,
      "delta": 5
    },
    {
      "token": "gbsindexspecifiedinsection2",
      "current_count": 4,
      "baseline_count": 0,
      "delta": 4
    },
    {
      "token": "component",
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
      "token": "specified",
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
      "token": "section2",
      "current_count": 2,
      "baseline_count": 0,
      "delta": 2
    },
    {
      "token": "reflected",
      "current_count": 2,
      "baseline_count": 1,
      "delta": 1
    },
    {
      "token": "definition",
      "current_count": 1,
      "baseline_count": 0,
      "delta": 1
    },
    {
      "token": "financialinstrument",
      "current_count": 1,
      "baseline_count": 0,
      "delta": 1
    }
  ],
  "full_surface_content_token_multiset_recall": 1.0,
  "full_surface_content_token_multiset_precision": 0.1044776119402985,
  "full_surface_repeat_overuse_token_count": 34,
  "full_surface_repeat_overuse_mass": 60,
  "full_surface_repeat_underuse_token_count": 0,
  "full_surface_repeat_underuse_mass": 0,
  "full_surface_repeat_overuse_examples": [
    {
      "token": "index",
      "current_count": 8,
      "baseline_count": 2,
      "delta": 6
    },
    {
      "token": "security",
      "current_count": 6,
      "baseline_count": 1,
      "delta": 5
    },
    {
      "token": "gbsindex",
      "current_count": 5,
      "baseline_count": 0,
      "delta": 5
    },
    {
      "token": "section",
      "current_count": 5,
      "baseline_count": 1,
      "delta": 4
    },
    {
      "token": "gbsindexspecifiedinsection2",
      "current_count": 4,
      "baseline_count": 0,
      "delta": 4
    },
    {
      "token": "component",
      "current_count": 3,
      "baseline_count": 1,
      "delta": 2
    },
    {
      "token": "specified",
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
      "token": "section2",
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
      "token": "reflected",
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
  "source_excerpt_content_token_count": 6,
  "source_excerpt_content_token_mass": 7,
  "normalized_content_token_count": 6,
  "normalized_content_token_mass": 7,
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
  "normalized_content_mass_per_clause": 7.0,
  "source_normalized_bertscore_precision": 1.0,
  "source_normalized_bertscore_recall": 1.0,
  "source_normalized_bertscore_f1": 1.0,
  "normalized_implies_source_entailment": 0.9841516017913818,
  "source_implies_normalized_entailment": 0.9841516017913818,
  "source_vs_normalized_contradiction_score": 0.007596246432512999
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
  "notes_to_formula_content_ratio": 1.9166666666666667
}
```

## identifier_glue

```json
{
  "identifier_count": 10,
  "compound_identifier_count_raw": 4,
  "compound_identifier_count_content": 5,
  "compound_identifier_rate_raw": 0.4,
  "compound_identifier_rate_content": 0.5,
  "max_identifier_piece_count_raw": 6,
  "max_identifier_piece_count_content": 4,
  "mean_identifier_piece_count_raw": 3.1,
  "mean_identifier_piece_count_content": 2.5,
  "identifier_glue_excess_mass_raw": 8,
  "identifier_glue_excess_mass_content": 9,
  "identifier_glue_excess_rate_raw": 0.8,
  "identifier_glue_excess_rate_content": 0.9,
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
      "identifier": "GbsIndexSpecifiedInSection2_1",
      "raw_piece_count": 6,
      "content_piece_count": 4,
      "raw_pieces": [
        "gbs",
        "index",
        "specified",
        "in",
        "section2",
        "1"
      ],
      "content_pieces": [
        "gbs",
        "index",
        "specified",
        "section2"
      ],
      "glue_excess_raw": 3,
      "glue_excess_content": 2,
      "source_grounded_content_piece_count": 3,
      "advisory_grounded_content_piece_count": 3,
      "source_grounded_content_piece_ratio": 0.75,
      "advisory_grounded_content_piece_ratio": 0.75
    },
    {
      "identifier": "gbs_index_specified_in_section",
      "raw_piece_count": 5,
      "content_piece_count": 4,
      "raw_pieces": [
        "gbs",
        "index",
        "specified",
        "in",
        "section"
      ],
      "content_pieces": [
        "gbs",
        "index",
        "specified",
        "section"
      ],
      "glue_excess_raw": 2,
      "glue_excess_content": 2,
      "source_grounded_content_piece_count": 4,
      "advisory_grounded_content_piece_count": 4,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    },
    {
      "identifier": "security_reflected_in_gbs_index",
      "raw_piece_count": 5,
      "content_piece_count": 4,
      "raw_pieces": [
        "security",
        "reflected",
        "in",
        "gbs",
        "index"
      ],
      "content_pieces": [
        "security",
        "reflected",
        "gbs",
        "index"
      ],
      "glue_excess_raw": 2,
      "glue_excess_content": 2,
      "source_grounded_content_piece_count": 4,
      "advisory_grounded_content_piece_count": 4,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    },
    {
      "identifier": "gbs_index_component_definition",
      "raw_piece_count": 4,
      "content_piece_count": 4,
      "raw_pieces": [
        "gbs",
        "index",
        "component",
        "definition"
      ],
      "content_pieces": [
        "gbs",
        "index",
        "component",
        "definition"
      ],
      "glue_excess_raw": 1,
      "glue_excess_content": 2,
      "source_grounded_content_piece_count": 3,
      "advisory_grounded_content_piece_count": 3,
      "source_grounded_content_piece_ratio": 0.75,
      "advisory_grounded_content_piece_ratio": 0.75
    },
    {
      "identifier": "gbs_index_component",
      "raw_piece_count": 3,
      "content_piece_count": 3,
      "raw_pieces": [
        "gbs",
        "index",
        "component"
      ],
      "content_pieces": [
        "gbs",
        "index",
        "component"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 1,
      "source_grounded_content_piece_count": 3,
      "advisory_grounded_content_piece_count": 3,
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
      "identifier": "Section2_1",
      "raw_piece_count": 2,
      "content_piece_count": 1,
      "raw_pieces": [
        "section2",
        "1"
      ],
      "content_pieces": [
        "section2"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 0,
      "source_grounded_content_piece_count": 0,
      "advisory_grounded_content_piece_count": 0,
      "source_grounded_content_piece_ratio": 0.0,
      "advisory_grounded_content_piece_ratio": 0.0
    },
    {
      "identifier": "GbsIndex",
      "raw_piece_count": 2,
      "content_piece_count": 2,
      "raw_pieces": [
        "gbs",
        "index"
      ],
      "content_pieces": [
        "gbs",
        "index"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 0,
      "source_grounded_content_piece_count": 2,
      "advisory_grounded_content_piece_count": 2,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    },
    {
      "identifier": "Security",
      "raw_piece_count": 1,
      "content_piece_count": 1,
      "raw_pieces": [
        "security"
      ],
      "content_pieces": [
        "security"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 0,
      "source_grounded_content_piece_count": 1,
      "advisory_grounded_content_piece_count": 1,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    },
    {
      "identifier": "s",
      "raw_piece_count": 1,
      "content_piece_count": 0,
      "raw_pieces": [
        "s"
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
      "identifier": "gbs_index_component_definition",
      "raw_piece_count": 4,
      "content_piece_count": 4,
      "raw_pieces": [
        "gbs",
        "index",
        "component",
        "definition"
      ],
      "content_pieces": [
        "gbs",
        "index",
        "component",
        "definition"
      ],
      "glue_excess_raw": 1,
      "glue_excess_content": 2,
      "source_grounded_content_piece_count": 3,
      "advisory_grounded_content_piece_count": 3,
      "source_grounded_content_piece_ratio": 0.75,
      "advisory_grounded_content_piece_ratio": 0.75
    },
    {
      "identifier": "GbsIndexSpecifiedInSection2_1",
      "raw_piece_count": 6,
      "content_piece_count": 4,
      "raw_pieces": [
        "gbs",
        "index",
        "specified",
        "in",
        "section2",
        "1"
      ],
      "content_pieces": [
        "gbs",
        "index",
        "specified",
        "section2"
      ],
      "glue_excess_raw": 3,
      "glue_excess_content": 2,
      "source_grounded_content_piece_count": 3,
      "advisory_grounded_content_piece_count": 3,
      "source_grounded_content_piece_ratio": 0.75,
      "advisory_grounded_content_piece_ratio": 0.75
    },
    {
      "identifier": "gbs_index_specified_in_section",
      "raw_piece_count": 5,
      "content_piece_count": 4,
      "raw_pieces": [
        "gbs",
        "index",
        "specified",
        "in",
        "section"
      ],
      "content_pieces": [
        "gbs",
        "index",
        "specified",
        "section"
      ],
      "glue_excess_raw": 2,
      "glue_excess_content": 2,
      "source_grounded_content_piece_count": 4,
      "advisory_grounded_content_piece_count": 4,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    },
    {
      "identifier": "security_reflected_in_gbs_index",
      "raw_piece_count": 5,
      "content_piece_count": 4,
      "raw_pieces": [
        "security",
        "reflected",
        "in",
        "gbs",
        "index"
      ],
      "content_pieces": [
        "security",
        "reflected",
        "gbs",
        "index"
      ],
      "glue_excess_raw": 2,
      "glue_excess_content": 2,
      "source_grounded_content_piece_count": 4,
      "advisory_grounded_content_piece_count": 4,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    },
    {
      "identifier": "gbs_index_component",
      "raw_piece_count": 3,
      "content_piece_count": 3,
      "raw_pieces": [
        "gbs",
        "index",
        "component"
      ],
      "content_pieces": [
        "gbs",
        "index",
        "component"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 1,
      "source_grounded_content_piece_count": 3,
      "advisory_grounded_content_piece_count": 3,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    },
    {
      "identifier": "GbsIndex",
      "raw_piece_count": 2,
      "content_piece_count": 2,
      "raw_pieces": [
        "gbs",
        "index"
      ],
      "content_pieces": [
        "gbs",
        "index"
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
  "callable_symbol_count": 3,
  "callable_symbol_with_args_count": 3,
  "top_level_parameter_slot_count": 6,
  "quantifier_parameter_slot_count": 1,
  "total_parameter_slot_mass": 7,
  "factorization_count": 3,
  "parameter_slots_per_factor": 2.0,
  "factorization_index": 0.5,
  "focus_symbol_signature": "missing",
  "focus_symbol_arity": null
}
```

## assertion_complexity

```json
{
  "assertion_count": 1,
  "mean_assertion_node_count": 8,
  "max_assertion_node_count": 8,
  "total_assertion_node_count": 8,
  "mean_assertion_depth": 4,
  "max_assertion_depth": 4,
  "total_ite_count": 0,
  "max_ite_count_per_assertion": 0,
  "total_quantifier_count": 1,
  "total_connective_count": 1,
  "total_branching_point_count": 1,
  "max_branching_point_count_per_assertion": 1,
  "mean_call_count_per_assertion": 2,
  "single_assertion_logic_share": 1.0,
  "overcompressed_single_assertion_flag": 0,
  "top_complex_assertions": [
    {
      "name": "gbs_index_component_definition",
      "assert_kind": "constraint",
      "node_count": 8,
      "depth": 4,
      "ite_count": 0,
      "quantifier_count": 1,
      "connective_count": 1,
      "branching_point_count": 1,
      "max_fanout": 2,
      "call_count": 2
    }
  ],
  "normalized_clause_count": 1,
  "node_count_per_normalized_clause": 8.0,
  "branching_point_count_per_normalized_clause": 1.0
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
  "helper_factorization_count": 3,
  "single_assertion_logic_share": 1.0,
  "underdecomposed_logic_flag": 0
}
```

## normalized_relative

```json
{
  "new_formula_content_token_rate_vs_reference_mass": 1.2857142857142858,
  "new_full_surface_content_token_rate_vs_reference_mass": 3.857142857142857,
  "formula_repeat_overuse_rate": 4.714285714285714,
  "full_surface_repeat_overuse_rate": 8.571428571428571,
  "parameter_slot_mass_per_clause": 7.0,
  "parameter_slot_mass_per_reference_token": 1.0,
  "factorization_per_clause": 3.0,
  "factorization_per_reference_token": 0.42857142857142855,
  "notes_content_token_rate_vs_reference_mass": 3.2857142857142856
}
```

## tradeoff

```json
{
  "render_bertscore_f1_to_normalized_per_parameter_slot_mass": 0.11516182763235909,
  "render_bertscore_f1_to_source_per_parameter_slot_mass": 0.11516182763235909,
  "render_nli_ir_implies_text_per_parameter_slot_mass": 0.1172878657068525,
  "render_nli_text_implies_ir_per_parameter_slot_mass": 0.0969497902052743,
  "render_bertscore_f1_to_normalized_per_formula_repeat_overuse_mass": 0.024428266467470112,
  "render_nli_text_implies_ir_per_formula_repeat_overuse_mass": 0.020565107013240005,
  "render_nli_ir_implies_text_per_formula_repeat_overuse_mass": 0.0248792442408475,
  "render_bertscore_f1_to_normalized_per_full_surface_repeat_overuse_mass": 0.013435546557108562,
  "render_nli_text_implies_ir_per_full_surface_repeat_overuse_mass": 0.011310808857282003,
  "pairwise_structure_similarity_mean_per_parameter_slot_mass": null,
  "focus_signature_mode_share_per_parameter_slot_mass": 0.14285714285714285
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
  "parameter_slot_mass_mean": 7.0,
  "parameter_slot_mass_stddev": 0.0,
  "factorization_count_mean": 3.0,
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
  "render_back_text": "constraint gbs index component definition states that for every s of type security, gbs index component for s and gbs index specified in section2 1 if and only if security reflected in gbs index for s and gbs index specified in section2 1. gbs index is a type. security is a type. gbs index specified in section2 1 is a distinguished entity. section2 1 is a distinguished entity. gbs index component holds between security and gbs index. security reflected in gbs index holds between security and gbs index. gbs index specified in section holds between gbs index and document part.",
  "render_bertscore_precision_to_normalized": 0.7832966446876526,
  "render_bertscore_recall_to_normalized": 0.8303403854370117,
  "render_bertscore_f1_to_normalized": 0.8061327934265137,
  "render_bertscore_precision_to_source": 0.7832966446876526,
  "render_bertscore_recall_to_source": 0.8303403854370117,
  "render_bertscore_f1_to_source": 0.8061327934265137,
  "render_nli_ir_implies_text": 0.8210150599479675,
  "render_nli_text_implies_ir": 0.6786485314369202,
  "render_nli_ir_implies_source": 0.8210150599479675,
  "render_nli_source_implies_ir": 0.6786485314369202,
  "render_nli_render_to_normalized": {
    "entailment": 0.8210150599479675,
    "neutral": 0.09346572309732437,
    "contradiction": 0.0855192020535469
  },
  "render_nli_normalized_to_render": {
    "entailment": 0.6786485314369202,
    "neutral": 0.23600471019744873,
    "contradiction": 0.08534683287143707
  },
  "render_nli_render_to_source": {
    "entailment": 0.8210150599479675,
    "neutral": 0.09346572309732437,
    "contradiction": 0.0855192020535469
  },
  "render_nli_source_to_render": {
    "entailment": 0.6786485314369202,
    "neutral": 0.23600471019744873,
    "contradiction": 0.08534683287143707
  },
  "render_contradiction_score": 0.0855192020535469
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
