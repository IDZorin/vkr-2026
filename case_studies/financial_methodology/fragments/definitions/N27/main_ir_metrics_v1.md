# Translation Metrics v1 - N27

- generated_at: `2026-05-20T03:00:00.617741+02:00`
- artifact_path: `case_studies\financial_methodology\definitions\N27\N27_manual_section_workspace_artifact_current_v1.json`
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
  "ungrounded_symbol_count": 1,
  "ungrounded_sort_count": 1,
  "ungrounded_ref_count": 0,
  "ungrounded_callee_count": 0,
  "prelude_redeclaration_count": 0,
  "origin_error_count": 3,
  "new_formula_token_count_vs_text_only": 13,
  "new_formula_content_token_count_vs_text_only": 11,
  "new_formula_token_count_vs_text_prelude_only": 11,
  "new_formula_content_token_count_vs_text_prelude_only": 9,
  "new_formula_token_count_vs_text_prelude_advisory": 11,
  "new_formula_content_token_count_vs_text_prelude_advisory": 9,
  "new_full_surface_token_count_vs_text_only": 37,
  "new_full_surface_content_token_count_vs_text_only": 31,
  "new_full_surface_token_count_vs_text_prelude_only": 33,
  "new_full_surface_content_token_count_vs_text_prelude_only": 28,
  "new_full_surface_token_count_vs_text_prelude_advisory": 33,
  "new_full_surface_content_token_count_vs_text_prelude_advisory": 28,
  "new_formula_content_tokens_vs_text_only": [
    "business_day_count_before",
    "businessdaycount",
    "change_of_rebalance_day_disregarded_for_selection_day",
    "rebalance_day_change_disregarded_for_selection_day",
    "rebalanceday",
    "required",
    "selection_day_definition",
    "selection_day_for_rebalance_day",
    "selectionday",
    "twenty_business_days_count",
    "twentybusinessdays"
  ],
  "new_formula_content_tokens_vs_text_prelude_only": [
    "business_day_count_before",
    "businessdaycount",
    "change_of_rebalance_day_disregarded_for_selection_day",
    "rebalance_day_change_disregarded_for_selection_day",
    "required",
    "selection_day_definition",
    "selection_day_for_rebalance_day",
    "twenty_business_days_count",
    "twentybusinessdays"
  ],
  "new_formula_content_tokens_vs_text_prelude_advisory": [
    "business_day_count_before",
    "businessdaycount",
    "change_of_rebalance_day_disregarded_for_selection_day",
    "rebalance_day_change_disregarded_for_selection_day",
    "required",
    "selection_day_definition",
    "selection_day_for_rebalance_day",
    "twenty_business_days_count",
    "twentybusinessdays"
  ],
  "new_full_surface_content_tokens_vs_text_only": [
    "a4v3",
    "business_day_count_before",
    "businessdaycount",
    "canonical",
    "change_of_rebalance_day_disregarded_for_selection_day",
    "computation",
    "current",
    "deterministic",
    "draft",
    "main_ir",
    "manual",
    "metric",
    "parsed",
    "primitive_usage",
    "rebalance_day_change_disregarded_for_selection_day",
    "rebalanceday",
    "recomputation",
    "reconstructed",
    "rendering_notes",
    "required",
    "residual_risks",
    "section",
    "section-level",
    "selection_day_definition",
    "selection_day_for_rebalance_day",
    "selectionday",
    "strengths",
    "text",
    "twenty_business_days_count",
    "twentybusinessdays",
    "workspace"
  ],
  "new_full_surface_content_tokens_vs_text_prelude_only": [
    "business_day_count_before",
    "businessdaycount",
    "canonical",
    "change_of_rebalance_day_disregarded_for_selection_day",
    "computation",
    "current",
    "deterministic",
    "draft",
    "main_ir",
    "manual",
    "metric",
    "parsed",
    "primitive_usage",
    "rebalance_day_change_disregarded_for_selection_day",
    "recomputation",
    "reconstructed",
    "rendering_notes",
    "required",
    "residual_risks",
    "section",
    "section-level",
    "selection_day_definition",
    "selection_day_for_rebalance_day",
    "strengths",
    "text",
    "twenty_business_days_count",
    "twentybusinessdays",
    "workspace"
  ],
  "new_full_surface_content_tokens_vs_text_prelude_advisory": [
    "business_day_count_before",
    "businessdaycount",
    "canonical",
    "change_of_rebalance_day_disregarded_for_selection_day",
    "computation",
    "current",
    "deterministic",
    "draft",
    "main_ir",
    "manual",
    "metric",
    "parsed",
    "primitive_usage",
    "rebalance_day_change_disregarded_for_selection_day",
    "recomputation",
    "reconstructed",
    "rendering_notes",
    "required",
    "residual_risks",
    "section",
    "section-level",
    "selection_day_definition",
    "selection_day_for_rebalance_day",
    "strengths",
    "text",
    "twenty_business_days_count",
    "twentybusinessdays",
    "workspace"
  ]
}
```

## coverage

```json
{
  "normalized_clause_count": 1,
  "formula_bearing_item_count": 2,
  "formula_to_clause_compression_ratio": 0.5,
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
  "source_content_token_mass": 8,
  "formula_content_token_count": 14,
  "formula_content_token_mass": 44,
  "full_surface_content_token_count": 37,
  "full_surface_content_token_mass": 71,
  "formula_content_token_recall": 0.8333333333333334,
  "full_surface_content_token_recall": 0.8333333333333334,
  "full_surface_content_token_jaccard": 0.13157894736842105,
  "formula_content_token_multiset_recall": 0.875,
  "formula_content_token_multiset_precision": 0.1590909090909091,
  "formula_repeat_overuse_token_count": 13,
  "formula_repeat_overuse_mass": 37,
  "formula_repeat_underuse_token_count": 1,
  "formula_repeat_underuse_mass": 1,
  "formula_repeat_overuse_examples": [
    {
      "token": "selection",
      "current_count": 7,
      "baseline_count": 1,
      "delta": 6
    },
    {
      "token": "rebalanceday",
      "current_count": 5,
      "baseline_count": 0,
      "delta": 5
    },
    {
      "token": "selectionday",
      "current_count": 5,
      "baseline_count": 0,
      "delta": 5
    },
    {
      "token": "rebalance",
      "current_count": 6,
      "baseline_count": 2,
      "delta": 4
    },
    {
      "token": "businessdaycount",
      "current_count": 3,
      "baseline_count": 0,
      "delta": 3
    },
    {
      "token": "disregarded",
      "current_count": 3,
      "baseline_count": 0,
      "delta": 3
    },
    {
      "token": "twentybusinessdays",
      "current_count": 3,
      "baseline_count": 0,
      "delta": 3
    },
    {
      "token": "business",
      "current_count": 3,
      "baseline_count": 1,
      "delta": 2
    },
    {
      "token": "change",
      "current_count": 3,
      "baseline_count": 1,
      "delta": 2
    },
    {
      "token": "before",
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
      "token": "required",
      "current_count": 1,
      "baseline_count": 0,
      "delta": 1
    },
    {
      "token": "twenty",
      "current_count": 1,
      "baseline_count": 0,
      "delta": 1
    }
  ],
  "full_surface_content_token_multiset_recall": 0.875,
  "full_surface_content_token_multiset_precision": 0.09859154929577464,
  "full_surface_repeat_overuse_token_count": 36,
  "full_surface_repeat_overuse_mass": 64,
  "full_surface_repeat_underuse_token_count": 1,
  "full_surface_repeat_underuse_mass": 1,
  "full_surface_repeat_overuse_examples": [
    {
      "token": "selection",
      "current_count": 7,
      "baseline_count": 1,
      "delta": 6
    },
    {
      "token": "rebalanceday",
      "current_count": 5,
      "baseline_count": 0,
      "delta": 5
    },
    {
      "token": "selectionday",
      "current_count": 5,
      "baseline_count": 0,
      "delta": 5
    },
    {
      "token": "rebalance",
      "current_count": 6,
      "baseline_count": 2,
      "delta": 4
    },
    {
      "token": "businessdaycount",
      "current_count": 3,
      "baseline_count": 0,
      "delta": 3
    },
    {
      "token": "disregarded",
      "current_count": 3,
      "baseline_count": 0,
      "delta": 3
    },
    {
      "token": "twentybusinessdays",
      "current_count": 3,
      "baseline_count": 0,
      "delta": 3
    },
    {
      "token": "business",
      "current_count": 3,
      "baseline_count": 1,
      "delta": 2
    },
    {
      "token": "change",
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
      "token": "before",
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
    }
  ],
  "source_to_formula_token_gap_count": 1,
  "source_to_full_surface_token_gap_count": 1,
  "source_content_tokens_missing_from_formula": [
    "disregarding"
  ],
  "source_content_tokens_missing_from_full_surface": [
    "disregarding"
  ]
}
```

## source_vs_normalized

```json
{
  "source_excerpt_content_token_count": 6,
  "source_excerpt_content_token_mass": 8,
  "normalized_content_token_count": 6,
  "normalized_content_token_mass": 8,
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
  "normalized_content_mass_per_clause": 8.0,
  "source_normalized_bertscore_precision": 1.0,
  "source_normalized_bertscore_recall": 1.0,
  "source_normalized_bertscore_f1": 1.0,
  "normalized_implies_source_entailment": 0.9904200434684753,
  "source_implies_normalized_entailment": 0.9904200434684753,
  "source_vs_normalized_contradiction_score": 0.00344782299362123
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
  "identifier_count": 12,
  "compound_identifier_count_raw": 4,
  "compound_identifier_count_content": 6,
  "compound_identifier_rate_raw": 0.3333333333333333,
  "compound_identifier_rate_content": 0.5,
  "max_identifier_piece_count_raw": 8,
  "max_identifier_piece_count_content": 6,
  "mean_identifier_piece_count_raw": 3.3333333333333335,
  "mean_identifier_piece_count_content": 2.6666666666666665,
  "identifier_glue_excess_mass_raw": 12,
  "identifier_glue_excess_mass_content": 13,
  "identifier_glue_excess_rate_raw": 1.0,
  "identifier_glue_excess_rate_content": 1.0833333333333333,
  "source_grounded_content_piece_ratio_mean": 0.9166666666666666,
  "advisory_grounded_content_piece_ratio_mean": 0.9166666666666666,
  "low_source_grounded_glued_identifier_count": 2,
  "low_source_grounded_glued_identifier_rate": 0.16666666666666666,
  "entity_relation_target_fusion_count": 0,
  "entity_relation_target_fusion_rate": 0.0,
  "conditional_relation_name_packing_count": 0,
  "conditional_relation_name_packing_rate": 0.0,
  "top_glued_identifiers": [
    {
      "identifier": "change_of_rebalance_day_disregarded_for_selection_day",
      "raw_piece_count": 8,
      "content_piece_count": 6,
      "raw_pieces": [
        "change",
        "of",
        "rebalance",
        "day",
        "disregarded",
        "for",
        "selection",
        "day"
      ],
      "content_pieces": [
        "change",
        "rebalance",
        "day",
        "disregarded",
        "selection",
        "day"
      ],
      "glue_excess_raw": 5,
      "glue_excess_content": 4,
      "source_grounded_content_piece_count": 5,
      "advisory_grounded_content_piece_count": 5,
      "source_grounded_content_piece_ratio": 0.8333333333333334,
      "advisory_grounded_content_piece_ratio": 0.8333333333333334
    },
    {
      "identifier": "rebalance_day_change_disregarded_for_selection_day",
      "raw_piece_count": 7,
      "content_piece_count": 6,
      "raw_pieces": [
        "rebalance",
        "day",
        "change",
        "disregarded",
        "for",
        "selection",
        "day"
      ],
      "content_pieces": [
        "rebalance",
        "day",
        "change",
        "disregarded",
        "selection",
        "day"
      ],
      "glue_excess_raw": 4,
      "glue_excess_content": 4,
      "source_grounded_content_piece_count": 5,
      "advisory_grounded_content_piece_count": 5,
      "source_grounded_content_piece_ratio": 0.8333333333333334,
      "advisory_grounded_content_piece_ratio": 0.8333333333333334
    },
    {
      "identifier": "selection_day_for_rebalance_day",
      "raw_piece_count": 5,
      "content_piece_count": 4,
      "raw_pieces": [
        "selection",
        "day",
        "for",
        "rebalance",
        "day"
      ],
      "content_pieces": [
        "selection",
        "day",
        "rebalance",
        "day"
      ],
      "glue_excess_raw": 2,
      "glue_excess_content": 2,
      "source_grounded_content_piece_count": 4,
      "advisory_grounded_content_piece_count": 4,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    },
    {
      "identifier": "business_day_count_before",
      "raw_piece_count": 4,
      "content_piece_count": 3,
      "raw_pieces": [
        "business",
        "day",
        "count",
        "before"
      ],
      "content_pieces": [
        "business",
        "day",
        "before"
      ],
      "glue_excess_raw": 1,
      "glue_excess_content": 1,
      "source_grounded_content_piece_count": 3,
      "advisory_grounded_content_piece_count": 3,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    },
    {
      "identifier": "selection_day_definition",
      "raw_piece_count": 3,
      "content_piece_count": 3,
      "raw_pieces": [
        "selection",
        "day",
        "definition"
      ],
      "content_pieces": [
        "selection",
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
      "identifier": "TwentyBusinessDays",
      "raw_piece_count": 3,
      "content_piece_count": 3,
      "raw_pieces": [
        "twenty",
        "business",
        "days"
      ],
      "content_pieces": [
        "twenty",
        "business",
        "days"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 1,
      "source_grounded_content_piece_count": 2,
      "advisory_grounded_content_piece_count": 2,
      "source_grounded_content_piece_ratio": 0.6666666666666666,
      "advisory_grounded_content_piece_ratio": 0.6666666666666666
    },
    {
      "identifier": "BusinessDayCount",
      "raw_piece_count": 3,
      "content_piece_count": 2,
      "raw_pieces": [
        "business",
        "day",
        "count"
      ],
      "content_pieces": [
        "business",
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
      "identifier": "RebalanceDay",
      "raw_piece_count": 2,
      "content_piece_count": 2,
      "raw_pieces": [
        "rebalance",
        "day"
      ],
      "content_pieces": [
        "rebalance",
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
      "identifier": "SelectionDay",
      "raw_piece_count": 2,
      "content_piece_count": 2,
      "raw_pieces": [
        "selection",
        "day"
      ],
      "content_pieces": [
        "selection",
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
      "identifier": "rd",
      "raw_piece_count": 1,
      "content_piece_count": 0,
      "raw_pieces": [
        "rd"
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
      "identifier": "sd",
      "raw_piece_count": 1,
      "content_piece_count": 0,
      "raw_pieces": [
        "sd"
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
      "identifier": "selection_day_definition",
      "raw_piece_count": 3,
      "content_piece_count": 3,
      "raw_pieces": [
        "selection",
        "day",
        "definition"
      ],
      "content_pieces": [
        "selection",
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
      "identifier": "TwentyBusinessDays",
      "raw_piece_count": 3,
      "content_piece_count": 3,
      "raw_pieces": [
        "twenty",
        "business",
        "days"
      ],
      "content_pieces": [
        "twenty",
        "business",
        "days"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 1,
      "source_grounded_content_piece_count": 2,
      "advisory_grounded_content_piece_count": 2,
      "source_grounded_content_piece_ratio": 0.6666666666666666,
      "advisory_grounded_content_piece_ratio": 0.6666666666666666
    },
    {
      "identifier": "change_of_rebalance_day_disregarded_for_selection_day",
      "raw_piece_count": 8,
      "content_piece_count": 6,
      "raw_pieces": [
        "change",
        "of",
        "rebalance",
        "day",
        "disregarded",
        "for",
        "selection",
        "day"
      ],
      "content_pieces": [
        "change",
        "rebalance",
        "day",
        "disregarded",
        "selection",
        "day"
      ],
      "glue_excess_raw": 5,
      "glue_excess_content": 4,
      "source_grounded_content_piece_count": 5,
      "advisory_grounded_content_piece_count": 5,
      "source_grounded_content_piece_ratio": 0.8333333333333334,
      "advisory_grounded_content_piece_ratio": 0.8333333333333334
    },
    {
      "identifier": "rebalance_day_change_disregarded_for_selection_day",
      "raw_piece_count": 7,
      "content_piece_count": 6,
      "raw_pieces": [
        "rebalance",
        "day",
        "change",
        "disregarded",
        "for",
        "selection",
        "day"
      ],
      "content_pieces": [
        "rebalance",
        "day",
        "change",
        "disregarded",
        "selection",
        "day"
      ],
      "glue_excess_raw": 4,
      "glue_excess_content": 4,
      "source_grounded_content_piece_count": 5,
      "advisory_grounded_content_piece_count": 5,
      "source_grounded_content_piece_ratio": 0.8333333333333334,
      "advisory_grounded_content_piece_ratio": 0.8333333333333334
    },
    {
      "identifier": "selection_day_for_rebalance_day",
      "raw_piece_count": 5,
      "content_piece_count": 4,
      "raw_pieces": [
        "selection",
        "day",
        "for",
        "rebalance",
        "day"
      ],
      "content_pieces": [
        "selection",
        "day",
        "rebalance",
        "day"
      ],
      "glue_excess_raw": 2,
      "glue_excess_content": 2,
      "source_grounded_content_piece_count": 4,
      "advisory_grounded_content_piece_count": 4,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    },
    {
      "identifier": "business_day_count_before",
      "raw_piece_count": 4,
      "content_piece_count": 3,
      "raw_pieces": [
        "business",
        "day",
        "count",
        "before"
      ],
      "content_pieces": [
        "business",
        "day",
        "before"
      ],
      "glue_excess_raw": 1,
      "glue_excess_content": 1,
      "source_grounded_content_piece_count": 3,
      "advisory_grounded_content_piece_count": 3,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    },
    {
      "identifier": "BusinessDayCount",
      "raw_piece_count": 3,
      "content_piece_count": 2,
      "raw_pieces": [
        "business",
        "day",
        "count"
      ],
      "content_pieces": [
        "business",
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
      "identifier": "RebalanceDay",
      "raw_piece_count": 2,
      "content_piece_count": 2,
      "raw_pieces": [
        "rebalance",
        "day"
      ],
      "content_pieces": [
        "rebalance",
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
      "identifier": "SelectionDay",
      "raw_piece_count": 2,
      "content_piece_count": 2,
      "raw_pieces": [
        "selection",
        "day"
      ],
      "content_pieces": [
        "selection",
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
  "callable_symbol_count": 3,
  "callable_symbol_with_args_count": 3,
  "top_level_parameter_slot_count": 6,
  "quantifier_parameter_slot_count": 4,
  "total_parameter_slot_mass": 10,
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
  "assertion_count": 2,
  "mean_assertion_node_count": 10,
  "max_assertion_node_count": 11,
  "total_assertion_node_count": 20,
  "mean_assertion_depth": 5.5,
  "max_assertion_depth": 6,
  "total_ite_count": 0,
  "max_ite_count_per_assertion": 0,
  "total_quantifier_count": 4,
  "total_connective_count": 2,
  "total_branching_point_count": 2,
  "max_branching_point_count_per_assertion": 1,
  "mean_call_count_per_assertion": 2,
  "single_assertion_logic_share": 0.55,
  "overcompressed_single_assertion_flag": 0,
  "top_complex_assertions": [
    {
      "name": "selection_day_definition",
      "assert_kind": "constraint",
      "node_count": 11,
      "depth": 6,
      "ite_count": 0,
      "quantifier_count": 2,
      "connective_count": 1,
      "branching_point_count": 1,
      "max_fanout": 2,
      "call_count": 2
    },
    {
      "name": "rebalance_day_change_disregarded_for_selection_day",
      "assert_kind": "constraint",
      "node_count": 9,
      "depth": 5,
      "ite_count": 0,
      "quantifier_count": 2,
      "connective_count": 1,
      "branching_point_count": 1,
      "max_fanout": 2,
      "call_count": 2
    }
  ],
  "normalized_clause_count": 1,
  "node_count_per_normalized_clause": 20.0,
  "branching_point_count_per_normalized_clause": 2.0
}
```

## normalized_alignment

```json
{
  "normalized_clause_count": 1,
  "logic_block_count": 2,
  "clause_to_logic_block_ratio": 0.5,
  "logic_block_to_clause_ratio": 2.0,
  "clause_underdecomposition_mass": 0,
  "clause_overdecomposition_mass": 1,
  "focus_symbol_arity": null,
  "helper_factorization_count": 3,
  "single_assertion_logic_share": 0.55,
  "underdecomposed_logic_flag": 0
}
```

## normalized_relative

```json
{
  "new_formula_content_token_rate_vs_reference_mass": 1.125,
  "new_full_surface_content_token_rate_vs_reference_mass": 3.5,
  "formula_repeat_overuse_rate": 4.625,
  "full_surface_repeat_overuse_rate": 8.0,
  "parameter_slot_mass_per_clause": 10.0,
  "parameter_slot_mass_per_reference_token": 1.25,
  "factorization_per_clause": 3.0,
  "factorization_per_reference_token": 0.375,
  "notes_content_token_rate_vs_reference_mass": 2.875
}
```

## tradeoff

```json
{
  "render_bertscore_f1_to_normalized_per_parameter_slot_mass": 0.07689914107322693,
  "render_bertscore_f1_to_source_per_parameter_slot_mass": 0.07689914107322693,
  "render_nli_ir_implies_text_per_parameter_slot_mass": 0.07563576698303223,
  "render_nli_text_implies_ir_per_parameter_slot_mass": 0.07434474825859069,
  "render_bertscore_f1_to_normalized_per_formula_repeat_overuse_mass": 0.020783551641412684,
  "render_nli_text_implies_ir_per_formula_repeat_overuse_mass": 0.020093175205024513,
  "render_nli_ir_implies_text_per_formula_repeat_overuse_mass": 0.020442099184603303,
  "render_bertscore_f1_to_normalized_per_full_surface_repeat_overuse_mass": 0.012015490792691708,
  "render_nli_text_implies_ir_per_full_surface_repeat_overuse_mass": 0.011616366915404797,
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
  "render_back_text": "constraint selection day definition states that for every sd of type selection day, for every rd of type rebalance day, selection day for rebalance day for sd and rd if and only if business day count before for sd and rd equals twenty business days. constraint rebalance day change disregarded for selection day states that for every sd of type selection day, for every rd of type rebalance day, if selection day for rebalance day for sd and rd, then change of rebalance day disregarded for selection day for sd and rd. selection day is a type. rebalance day is a type. business day count is a type. twenty business days is a distinguished entity. business day count before maps day and day to business day count. selection day for rebalance day holds between selection day and rebalance day. change of rebalance day disregarded for selection day holds between selection day and rebalance day.",
  "render_bertscore_precision_to_normalized": 0.7323887348175049,
  "render_bertscore_recall_to_normalized": 0.8094452619552612,
  "render_bertscore_f1_to_normalized": 0.7689914107322693,
  "render_bertscore_precision_to_source": 0.7323887348175049,
  "render_bertscore_recall_to_source": 0.8094452619552612,
  "render_bertscore_f1_to_source": 0.7689914107322693,
  "render_nli_ir_implies_text": 0.7563576698303223,
  "render_nli_text_implies_ir": 0.743447482585907,
  "render_nli_ir_implies_source": 0.7563576698303223,
  "render_nli_source_implies_ir": 0.743447482585907,
  "render_nli_render_to_normalized": {
    "entailment": 0.7563576698303223,
    "neutral": 0.0964130237698555,
    "contradiction": 0.14722925424575806
  },
  "render_nli_normalized_to_render": {
    "entailment": 0.743447482585907,
    "neutral": 0.19847139716148376,
    "contradiction": 0.05808116868138313
  },
  "render_nli_render_to_source": {
    "entailment": 0.7563576698303223,
    "neutral": 0.0964130237698555,
    "contradiction": 0.14722925424575806
  },
  "render_nli_source_to_render": {
    "entailment": 0.743447482585907,
    "neutral": 0.19847139716148376,
    "contradiction": 0.05808116868138313
  },
  "render_contradiction_score": 0.14722925424575806
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
