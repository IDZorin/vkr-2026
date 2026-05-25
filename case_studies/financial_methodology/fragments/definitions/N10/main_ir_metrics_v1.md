# Translation Metrics v1 - N10

- generated_at: `2026-05-20T02:56:28.570585+02:00`
- artifact_path: `case_studies\financial_methodology\definitions\N10\N10_manual_section_workspace_artifact_current_v1.json`
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
  "new_formula_token_count_vs_text_only": 12,
  "new_formula_content_token_count_vs_text_only": 10,
  "new_formula_token_count_vs_text_prelude_only": 11,
  "new_formula_content_token_count_vs_text_prelude_only": 9,
  "new_formula_token_count_vs_text_prelude_advisory": 11,
  "new_formula_content_token_count_vs_text_prelude_advisory": 9,
  "new_full_surface_token_count_vs_text_only": 35,
  "new_full_surface_content_token_count_vs_text_only": 29,
  "new_full_surface_token_count_vs_text_prelude_only": 32,
  "new_full_surface_content_token_count_vs_text_prelude_only": 27,
  "new_full_surface_token_count_vs_text_prelude_advisory": 32,
  "new_full_surface_content_token_count_vs_text_prelude_advisory": 27,
  "new_formula_content_tokens_vs_text_only": [
    "exchange_definition",
    "financialinstrument",
    "indexcomponent",
    "listing_component",
    "listing_determined_in_accordance_with_rules",
    "listing_exchange",
    "required",
    "respective_exchange_for_index_component",
    "section2rules",
    "theindex"
  ],
  "new_formula_content_tokens_vs_text_prelude_only": [
    "exchange_definition",
    "indexcomponent",
    "listing_component",
    "listing_determined_in_accordance_with_rules",
    "listing_exchange",
    "required",
    "respective_exchange_for_index_component",
    "section2rules",
    "theindex"
  ],
  "new_formula_content_tokens_vs_text_prelude_advisory": [
    "exchange_definition",
    "indexcomponent",
    "listing_component",
    "listing_determined_in_accordance_with_rules",
    "listing_exchange",
    "required",
    "respective_exchange_for_index_component",
    "section2rules",
    "theindex"
  ],
  "new_full_surface_content_tokens_vs_text_only": [
    "a4v3",
    "canonical",
    "computation",
    "current",
    "deterministic",
    "draft",
    "exchange_definition",
    "financialinstrument",
    "indexcomponent",
    "listing_component",
    "listing_determined_in_accordance_with_rules",
    "listing_exchange",
    "main_ir",
    "manual",
    "metric",
    "parsed",
    "primitive_usage",
    "recomputation",
    "reconstructed",
    "rendering_notes",
    "required",
    "residual_risks",
    "respective_exchange_for_index_component",
    "section-level",
    "section2rules",
    "strengths",
    "text",
    "theindex",
    "workspace"
  ],
  "new_full_surface_content_tokens_vs_text_prelude_only": [
    "canonical",
    "computation",
    "current",
    "deterministic",
    "draft",
    "exchange_definition",
    "indexcomponent",
    "listing_component",
    "listing_determined_in_accordance_with_rules",
    "listing_exchange",
    "main_ir",
    "manual",
    "metric",
    "parsed",
    "primitive_usage",
    "recomputation",
    "reconstructed",
    "rendering_notes",
    "required",
    "residual_risks",
    "respective_exchange_for_index_component",
    "section-level",
    "section2rules",
    "strengths",
    "text",
    "theindex",
    "workspace"
  ],
  "new_full_surface_content_tokens_vs_text_prelude_advisory": [
    "canonical",
    "computation",
    "current",
    "deterministic",
    "draft",
    "exchange_definition",
    "indexcomponent",
    "listing_component",
    "listing_determined_in_accordance_with_rules",
    "listing_exchange",
    "main_ir",
    "manual",
    "metric",
    "parsed",
    "primitive_usage",
    "recomputation",
    "reconstructed",
    "rendering_notes",
    "required",
    "residual_risks",
    "respective_exchange_for_index_component",
    "section-level",
    "section2rules",
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
  "source_content_token_count": 9,
  "source_content_token_mass": 14,
  "formula_content_token_count": 14,
  "formula_content_token_mass": 50,
  "full_surface_content_token_count": 37,
  "full_surface_content_token_mass": 77,
  "formula_content_token_recall": 0.8888888888888888,
  "full_surface_content_token_recall": 1.0,
  "full_surface_content_token_jaccard": 0.24324324324324326,
  "formula_content_token_multiset_recall": 0.8571428571428571,
  "formula_content_token_multiset_precision": 0.24,
  "formula_repeat_overuse_token_count": 14,
  "formula_repeat_overuse_mass": 38,
  "formula_repeat_underuse_token_count": 2,
  "formula_repeat_underuse_mass": 2,
  "formula_repeat_overuse_examples": [
    {
      "token": "listing",
      "current_count": 11,
      "baseline_count": 1,
      "delta": 10
    },
    {
      "token": "exchange",
      "current_count": 8,
      "baseline_count": 2,
      "delta": 6
    },
    {
      "token": "rules",
      "current_count": 5,
      "baseline_count": 1,
      "delta": 4
    },
    {
      "token": "indexcomponent",
      "current_count": 4,
      "baseline_count": 0,
      "delta": 4
    },
    {
      "token": "index",
      "current_count": 5,
      "baseline_count": 3,
      "delta": 2
    },
    {
      "token": "component",
      "current_count": 4,
      "baseline_count": 2,
      "delta": 2
    },
    {
      "token": "section2rules",
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
      "token": "accordance",
      "current_count": 2,
      "baseline_count": 1,
      "delta": 1
    },
    {
      "token": "determined",
      "current_count": 2,
      "baseline_count": 1,
      "delta": 1
    },
    {
      "token": "respective",
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
    },
    {
      "token": "required",
      "current_count": 1,
      "baseline_count": 0,
      "delta": 1
    }
  ],
  "full_surface_content_token_multiset_recall": 0.9285714285714286,
  "full_surface_content_token_multiset_precision": 0.16883116883116883,
  "full_surface_repeat_overuse_token_count": 37,
  "full_surface_repeat_overuse_mass": 64,
  "full_surface_repeat_underuse_token_count": 1,
  "full_surface_repeat_underuse_mass": 1,
  "full_surface_repeat_overuse_examples": [
    {
      "token": "listing",
      "current_count": 11,
      "baseline_count": 1,
      "delta": 10
    },
    {
      "token": "exchange",
      "current_count": 8,
      "baseline_count": 2,
      "delta": 6
    },
    {
      "token": "rules",
      "current_count": 5,
      "baseline_count": 1,
      "delta": 4
    },
    {
      "token": "indexcomponent",
      "current_count": 4,
      "baseline_count": 0,
      "delta": 4
    },
    {
      "token": "index",
      "current_count": 5,
      "baseline_count": 3,
      "delta": 2
    },
    {
      "token": "component",
      "current_count": 4,
      "baseline_count": 2,
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
      "token": "section2rules",
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
      "token": "accordance",
      "current_count": 2,
      "baseline_count": 1,
      "delta": 1
    },
    {
      "token": "determined",
      "current_count": 2,
      "baseline_count": 1,
      "delta": 1
    },
    {
      "token": "respective",
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
  "source_to_formula_token_gap_count": 1,
  "source_to_full_surface_token_gap_count": 0,
  "source_content_tokens_missing_from_formula": [
    "section"
  ],
  "source_content_tokens_missing_from_full_surface": []
}
```

## source_vs_normalized

```json
{
  "source_excerpt_content_token_count": 9,
  "source_excerpt_content_token_mass": 14,
  "normalized_content_token_count": 9,
  "normalized_content_token_mass": 14,
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
  "normalized_content_mass_per_clause": 14.0,
  "source_normalized_bertscore_precision": 1.0,
  "source_normalized_bertscore_recall": 1.0,
  "source_normalized_bertscore_f1": 1.0,
  "normalized_implies_source_entailment": 0.9814209342002869,
  "source_implies_normalized_entailment": 0.9814209342002869,
  "source_vs_normalized_contradiction_score": 0.010503755882382393
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
  "notes_to_formula_content_ratio": 1.6428571428571428
}
```

## identifier_glue

```json
{
  "identifier_count": 14,
  "compound_identifier_count_raw": 2,
  "compound_identifier_count_content": 2,
  "compound_identifier_rate_raw": 0.14285714285714285,
  "compound_identifier_rate_content": 0.14285714285714285,
  "max_identifier_piece_count_raw": 6,
  "max_identifier_piece_count_content": 4,
  "mean_identifier_piece_count_raw": 2.0714285714285716,
  "mean_identifier_piece_count_content": 1.6428571428571428,
  "identifier_glue_excess_mass_raw": 5,
  "identifier_glue_excess_mass_content": 4,
  "identifier_glue_excess_rate_raw": 0.35714285714285715,
  "identifier_glue_excess_rate_content": 0.2857142857142857,
  "source_grounded_content_piece_ratio_mean": 0.9285714285714286,
  "advisory_grounded_content_piece_ratio_mean": 0.9285714285714286,
  "low_source_grounded_glued_identifier_count": 0,
  "low_source_grounded_glued_identifier_rate": 0.0,
  "entity_relation_target_fusion_count": 1,
  "entity_relation_target_fusion_rate": 0.07142857142857142,
  "conditional_relation_name_packing_count": 0,
  "conditional_relation_name_packing_rate": 0.0,
  "top_glued_identifiers": [
    {
      "identifier": "listing_determined_in_accordance_with_rules",
      "raw_piece_count": 6,
      "content_piece_count": 4,
      "raw_pieces": [
        "listing",
        "determined",
        "in",
        "accordance",
        "with",
        "rules"
      ],
      "content_pieces": [
        "listing",
        "determined",
        "accordance",
        "rules"
      ],
      "glue_excess_raw": 3,
      "glue_excess_content": 2,
      "source_grounded_content_piece_count": 4,
      "advisory_grounded_content_piece_count": 4,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    },
    {
      "identifier": "respective_exchange_for_index_component",
      "raw_piece_count": 5,
      "content_piece_count": 4,
      "raw_pieces": [
        "respective",
        "exchange",
        "for",
        "index",
        "component"
      ],
      "content_pieces": [
        "respective",
        "exchange",
        "index",
        "component"
      ],
      "glue_excess_raw": 2,
      "glue_excess_content": 2,
      "source_grounded_content_piece_count": 4,
      "advisory_grounded_content_piece_count": 4,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    },
    {
      "identifier": "exchange_definition",
      "raw_piece_count": 2,
      "content_piece_count": 2,
      "raw_pieces": [
        "exchange",
        "definition"
      ],
      "content_pieces": [
        "exchange",
        "definition"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 0,
      "source_grounded_content_piece_count": 1,
      "advisory_grounded_content_piece_count": 1,
      "source_grounded_content_piece_ratio": 0.5,
      "advisory_grounded_content_piece_ratio": 0.5
    },
    {
      "identifier": "Section2Rules",
      "raw_piece_count": 2,
      "content_piece_count": 2,
      "raw_pieces": [
        "section2",
        "rules"
      ],
      "content_pieces": [
        "section2",
        "rules"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 0,
      "source_grounded_content_piece_count": 1,
      "advisory_grounded_content_piece_count": 1,
      "source_grounded_content_piece_ratio": 0.5,
      "advisory_grounded_content_piece_ratio": 0.5
    },
    {
      "identifier": "IndexComponent",
      "raw_piece_count": 2,
      "content_piece_count": 2,
      "raw_pieces": [
        "index",
        "component"
      ],
      "content_pieces": [
        "index",
        "component"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 0,
      "source_grounded_content_piece_count": 2,
      "advisory_grounded_content_piece_count": 2,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    },
    {
      "identifier": "listing_component",
      "raw_piece_count": 2,
      "content_piece_count": 2,
      "raw_pieces": [
        "listing",
        "component"
      ],
      "content_pieces": [
        "listing",
        "component"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 0,
      "source_grounded_content_piece_count": 2,
      "advisory_grounded_content_piece_count": 2,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    },
    {
      "identifier": "listing_exchange",
      "raw_piece_count": 2,
      "content_piece_count": 2,
      "raw_pieces": [
        "listing",
        "exchange"
      ],
      "content_pieces": [
        "listing",
        "exchange"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 0,
      "source_grounded_content_piece_count": 2,
      "advisory_grounded_content_piece_count": 2,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    },
    {
      "identifier": "Exchange",
      "raw_piece_count": 1,
      "content_piece_count": 1,
      "raw_pieces": [
        "exchange"
      ],
      "content_pieces": [
        "exchange"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 0,
      "source_grounded_content_piece_count": 1,
      "advisory_grounded_content_piece_count": 1,
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
      "identifier": "Listing",
      "raw_piece_count": 1,
      "content_piece_count": 1,
      "raw_pieces": [
        "listing"
      ],
      "content_pieces": [
        "listing"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 0,
      "source_grounded_content_piece_count": 1,
      "advisory_grounded_content_piece_count": 1,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    },
    {
      "identifier": "Rules",
      "raw_piece_count": 1,
      "content_piece_count": 1,
      "raw_pieces": [
        "rules"
      ],
      "content_pieces": [
        "rules"
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
    },
    {
      "identifier": "c",
      "raw_piece_count": 1,
      "content_piece_count": 0,
      "raw_pieces": [
        "c"
      ],
      "content_pieces": [],
      "glue_excess_raw": 0,
      "glue_excess_content": 0,
      "source_grounded_content_piece_count": 0,
      "advisory_grounded_content_piece_count": 0,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    },
    {
      "identifier": "l",
      "raw_piece_count": 1,
      "content_piece_count": 0,
      "raw_pieces": [
        "l"
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
      "identifier": "exchange_definition",
      "raw_piece_count": 2,
      "content_piece_count": 2,
      "raw_pieces": [
        "exchange",
        "definition"
      ],
      "content_pieces": [
        "exchange",
        "definition"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 0,
      "source_grounded_content_piece_count": 1,
      "advisory_grounded_content_piece_count": 1,
      "source_grounded_content_piece_ratio": 0.5,
      "advisory_grounded_content_piece_ratio": 0.5
    },
    {
      "identifier": "Section2Rules",
      "raw_piece_count": 2,
      "content_piece_count": 2,
      "raw_pieces": [
        "section2",
        "rules"
      ],
      "content_pieces": [
        "section2",
        "rules"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 0,
      "source_grounded_content_piece_count": 1,
      "advisory_grounded_content_piece_count": 1,
      "source_grounded_content_piece_ratio": 0.5,
      "advisory_grounded_content_piece_ratio": 0.5
    },
    {
      "identifier": "listing_determined_in_accordance_with_rules",
      "raw_piece_count": 6,
      "content_piece_count": 4,
      "raw_pieces": [
        "listing",
        "determined",
        "in",
        "accordance",
        "with",
        "rules"
      ],
      "content_pieces": [
        "listing",
        "determined",
        "accordance",
        "rules"
      ],
      "glue_excess_raw": 3,
      "glue_excess_content": 2,
      "source_grounded_content_piece_count": 4,
      "advisory_grounded_content_piece_count": 4,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    },
    {
      "identifier": "respective_exchange_for_index_component",
      "raw_piece_count": 5,
      "content_piece_count": 4,
      "raw_pieces": [
        "respective",
        "exchange",
        "for",
        "index",
        "component"
      ],
      "content_pieces": [
        "respective",
        "exchange",
        "index",
        "component"
      ],
      "glue_excess_raw": 2,
      "glue_excess_content": 2,
      "source_grounded_content_piece_count": 4,
      "advisory_grounded_content_piece_count": 4,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    },
    {
      "identifier": "IndexComponent",
      "raw_piece_count": 2,
      "content_piece_count": 2,
      "raw_pieces": [
        "index",
        "component"
      ],
      "content_pieces": [
        "index",
        "component"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 0,
      "source_grounded_content_piece_count": 2,
      "advisory_grounded_content_piece_count": 2,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    },
    {
      "identifier": "listing_component",
      "raw_piece_count": 2,
      "content_piece_count": 2,
      "raw_pieces": [
        "listing",
        "component"
      ],
      "content_pieces": [
        "listing",
        "component"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 0,
      "source_grounded_content_piece_count": 2,
      "advisory_grounded_content_piece_count": 2,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    },
    {
      "identifier": "listing_exchange",
      "raw_piece_count": 2,
      "content_piece_count": 2,
      "raw_pieces": [
        "listing",
        "exchange"
      ],
      "content_pieces": [
        "listing",
        "exchange"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 0,
      "source_grounded_content_piece_count": 2,
      "advisory_grounded_content_piece_count": 2,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    }
  ],
  "entity_relation_target_fusion_examples": [
    {
      "identifier": "listing_determined_in_accordance_with_rules",
      "raw_piece_count": 6,
      "content_piece_count": 4,
      "raw_pieces": [
        "listing",
        "determined",
        "in",
        "accordance",
        "with",
        "rules"
      ],
      "content_pieces": [
        "listing",
        "determined",
        "accordance",
        "rules"
      ],
      "glue_excess_raw": 3,
      "glue_excess_content": 2,
      "source_grounded_content_piece_count": 4,
      "advisory_grounded_content_piece_count": 4,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    }
  ],
  "conditional_relation_name_packing_examples": []
}
```

## parameterization

```json
{
  "callable_symbol_count": 4,
  "callable_symbol_with_args_count": 4,
  "top_level_parameter_slot_count": 8,
  "quantifier_parameter_slot_count": 2,
  "total_parameter_slot_mass": 10,
  "factorization_count": 4,
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
  "mean_assertion_node_count": 15,
  "max_assertion_node_count": 15,
  "total_assertion_node_count": 15,
  "mean_assertion_depth": 6,
  "max_assertion_depth": 6,
  "total_ite_count": 0,
  "max_ite_count_per_assertion": 0,
  "total_quantifier_count": 2,
  "total_connective_count": 1,
  "total_branching_point_count": 2,
  "max_branching_point_count_per_assertion": 2,
  "mean_call_count_per_assertion": 4,
  "single_assertion_logic_share": 1.0,
  "overcompressed_single_assertion_flag": 0,
  "top_complex_assertions": [
    {
      "name": "exchange_definition",
      "assert_kind": "constraint",
      "node_count": 15,
      "depth": 6,
      "ite_count": 0,
      "quantifier_count": 2,
      "connective_count": 1,
      "branching_point_count": 2,
      "max_fanout": 3,
      "call_count": 4
    }
  ],
  "normalized_clause_count": 1,
  "node_count_per_normalized_clause": 15.0,
  "branching_point_count_per_normalized_clause": 2.0
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
  "helper_factorization_count": 4,
  "single_assertion_logic_share": 1.0,
  "underdecomposed_logic_flag": 0
}
```

## normalized_relative

```json
{
  "new_formula_content_token_rate_vs_reference_mass": 0.6428571428571429,
  "new_full_surface_content_token_rate_vs_reference_mass": 1.9285714285714286,
  "formula_repeat_overuse_rate": 2.7142857142857144,
  "full_surface_repeat_overuse_rate": 4.571428571428571,
  "parameter_slot_mass_per_clause": 10.0,
  "parameter_slot_mass_per_reference_token": 0.7142857142857143,
  "factorization_per_clause": 4.0,
  "factorization_per_reference_token": 0.2857142857142857,
  "notes_content_token_rate_vs_reference_mass": 1.6428571428571428
}
```

## tradeoff

```json
{
  "render_bertscore_f1_to_normalized_per_parameter_slot_mass": 0.07712895274162293,
  "render_bertscore_f1_to_source_per_parameter_slot_mass": 0.07712895274162293,
  "render_nli_ir_implies_text_per_parameter_slot_mass": 0.09176459312438964,
  "render_nli_text_implies_ir_per_parameter_slot_mass": 0.08263476490974427,
  "render_bertscore_f1_to_normalized_per_formula_repeat_overuse_mass": 0.020297092826742875,
  "render_nli_text_implies_ir_per_formula_repeat_overuse_mass": 0.021745990765722173,
  "render_nli_ir_implies_text_per_formula_repeat_overuse_mass": 0.024148577137997274,
  "render_bertscore_f1_to_normalized_per_full_surface_repeat_overuse_mass": 0.012051398865878582,
  "render_nli_text_implies_ir_per_full_surface_repeat_overuse_mass": 0.012911682017147541,
  "pairwise_structure_similarity_mean_per_parameter_slot_mass": null,
  "focus_signature_mode_share_per_parameter_slot_mass": 0.1
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
  "parameter_slot_mass_mean": 10.0,
  "parameter_slot_mass_stddev": 0.0,
  "factorization_count_mean": 4.0,
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
  "render_back_text": "constraint exchange definition states that for every c of type index component, there exists l of type listing, (listing component for l and c, listing determined in accordance with rules for l and section2 rules, and respective exchange for index component for the index and c equals listing exchange for l). index is a type. index component is a type. exchange is a type. listing is a type. rules is a type. the index is a distinguished entity. section2 rules is a distinguished entity. respective exchange for index component maps index and index component to exchange. listing component holds between listing and index component. listing exchange holds between listing and exchange. listing determined in accordance with rules holds between listing and rules.",
  "render_bertscore_precision_to_normalized": 0.7467491626739502,
  "render_bertscore_recall_to_normalized": 0.797497570514679,
  "render_bertscore_f1_to_normalized": 0.7712895274162292,
  "render_bertscore_precision_to_source": 0.7467491626739502,
  "render_bertscore_recall_to_source": 0.797497570514679,
  "render_bertscore_f1_to_source": 0.7712895274162292,
  "render_nli_ir_implies_text": 0.9176459312438965,
  "render_nli_text_implies_ir": 0.8263476490974426,
  "render_nli_ir_implies_source": 0.9176459312438965,
  "render_nli_source_implies_ir": 0.8263476490974426,
  "render_nli_render_to_normalized": {
    "entailment": 0.9176459312438965,
    "neutral": 0.039332516491413116,
    "contradiction": 0.0430215448141098
  },
  "render_nli_normalized_to_render": {
    "entailment": 0.8263476490974426,
    "neutral": 0.13779519498348236,
    "contradiction": 0.035857148468494415
  },
  "render_nli_render_to_source": {
    "entailment": 0.9176459312438965,
    "neutral": 0.039332516491413116,
    "contradiction": 0.0430215448141098
  },
  "render_nli_source_to_render": {
    "entailment": 0.8263476490974426,
    "neutral": 0.13779519498348236,
    "contradiction": 0.035857148468494415
  },
  "render_contradiction_score": 0.0430215448141098
}
```

## silver_reference

```json
{
  "disabled_for_manual_reference": false,
  "silver_reference_found": true,
  "silver_reference_path": "D:\\OneDrive\\Documents\\Study\\MIPT\\VKR\\research_experiments\\2026-02_pipeline\\IR\\outputs\\runs\\silver_baseline\\definitions_full6_multivariant_critic_v1_with_gold.md",
  "silver_reference_ir": "abstract ExchangeFor : Security -> Exchange",
  "top_level_cosine": null,
  "logic_cosine": null,
  "arity_cosine": null,
  "silver_structure_similarity": null
}
```
