# Translation Metrics v1 - N01

- generated_at: `2026-05-20T02:53:46.501028+02:00`
- artifact_path: `case_studies\financial_methodology\definitions\N01\N01_manual_section_workspace_artifact_current_v1.json`
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
  "ungrounded_symbol_count": 2,
  "ungrounded_sort_count": 1,
  "ungrounded_ref_count": 1,
  "ungrounded_callee_count": 1,
  "prelude_redeclaration_count": 0,
  "origin_error_count": 4,
  "new_formula_token_count_vs_text_only": 21,
  "new_formula_content_token_count_vs_text_only": 17,
  "new_formula_token_count_vs_text_prelude_only": 18,
  "new_formula_content_token_count_vs_text_prelude_only": 15,
  "new_formula_token_count_vs_text_prelude_advisory": 18,
  "new_formula_content_token_count_vs_text_prelude_advisory": 15,
  "new_full_surface_token_count_vs_text_only": 45,
  "new_full_surface_content_token_count_vs_text_only": 37,
  "new_full_surface_token_count_vs_text_prelude_only": 40,
  "new_full_surface_content_token_count_vs_text_prelude_only": 34,
  "new_full_surface_token_count_vs_text_prelude_advisory": 40,
  "new_full_surface_content_token_count_vs_text_prelude_advisory": 34,
  "new_formula_content_tokens_vs_text_only": [
    "average_daily_value_traded",
    "average_daily_value_traded_divided_by_trading_day_count_definition",
    "averagedailyvaluetraded",
    "daily_value_traded",
    "daily_value_traded_sum_over_period",
    "daily_value_traded_sum_over_period_definition",
    "dailyvaluetraded",
    "financialinstrument",
    "indexcomponent",
    "real",
    "required",
    "specifiedperiod",
    "trading_day_count_in_period",
    "trading_day_count_in_period_definition",
    "trading_day_falls_in_period",
    "tradingday",
    "tradingdaycount"
  ],
  "new_formula_content_tokens_vs_text_prelude_only": [
    "average_daily_value_traded",
    "average_daily_value_traded_divided_by_trading_day_count_definition",
    "averagedailyvaluetraded",
    "daily_value_traded",
    "daily_value_traded_sum_over_period",
    "daily_value_traded_sum_over_period_definition",
    "dailyvaluetraded",
    "indexcomponent",
    "real",
    "required",
    "specifiedperiod",
    "trading_day_count_in_period",
    "trading_day_count_in_period_definition",
    "trading_day_falls_in_period",
    "tradingdaycount"
  ],
  "new_formula_content_tokens_vs_text_prelude_advisory": [
    "average_daily_value_traded",
    "average_daily_value_traded_divided_by_trading_day_count_definition",
    "averagedailyvaluetraded",
    "daily_value_traded",
    "daily_value_traded_sum_over_period",
    "daily_value_traded_sum_over_period_definition",
    "dailyvaluetraded",
    "indexcomponent",
    "real",
    "required",
    "specifiedperiod",
    "trading_day_count_in_period",
    "trading_day_count_in_period_definition",
    "trading_day_falls_in_period",
    "tradingdaycount"
  ],
  "new_full_surface_content_tokens_vs_text_only": [
    "a4v3",
    "average_daily_value_traded",
    "average_daily_value_traded_divided_by_trading_day_count_definition",
    "averagedailyvaluetraded",
    "canonical",
    "computation",
    "current",
    "daily_value_traded",
    "daily_value_traded_sum_over_period",
    "daily_value_traded_sum_over_period_definition",
    "dailyvaluetraded",
    "deterministic",
    "draft",
    "financialinstrument",
    "indexcomponent",
    "main_ir",
    "manual",
    "metric",
    "parsed",
    "primitive_usage",
    "real",
    "recomputation",
    "reconstructed",
    "rendering_notes",
    "required",
    "residual_risks",
    "section",
    "section-level",
    "specifiedperiod",
    "strengths",
    "text",
    "trading_day_count_in_period",
    "trading_day_count_in_period_definition",
    "trading_day_falls_in_period",
    "tradingday",
    "tradingdaycount",
    "workspace"
  ],
  "new_full_surface_content_tokens_vs_text_prelude_only": [
    "average_daily_value_traded",
    "average_daily_value_traded_divided_by_trading_day_count_definition",
    "averagedailyvaluetraded",
    "canonical",
    "computation",
    "current",
    "daily_value_traded",
    "daily_value_traded_sum_over_period",
    "daily_value_traded_sum_over_period_definition",
    "dailyvaluetraded",
    "deterministic",
    "draft",
    "indexcomponent",
    "main_ir",
    "manual",
    "metric",
    "parsed",
    "primitive_usage",
    "real",
    "recomputation",
    "reconstructed",
    "rendering_notes",
    "required",
    "residual_risks",
    "section",
    "section-level",
    "specifiedperiod",
    "strengths",
    "text",
    "trading_day_count_in_period",
    "trading_day_count_in_period_definition",
    "trading_day_falls_in_period",
    "tradingdaycount",
    "workspace"
  ],
  "new_full_surface_content_tokens_vs_text_prelude_advisory": [
    "average_daily_value_traded",
    "average_daily_value_traded_divided_by_trading_day_count_definition",
    "averagedailyvaluetraded",
    "canonical",
    "computation",
    "current",
    "daily_value_traded",
    "daily_value_traded_sum_over_period",
    "daily_value_traded_sum_over_period_definition",
    "dailyvaluetraded",
    "deterministic",
    "draft",
    "indexcomponent",
    "main_ir",
    "manual",
    "metric",
    "parsed",
    "primitive_usage",
    "real",
    "recomputation",
    "reconstructed",
    "rendering_notes",
    "required",
    "residual_risks",
    "section",
    "section-level",
    "specifiedperiod",
    "strengths",
    "text",
    "trading_day_count_in_period",
    "trading_day_count_in_period_definition",
    "trading_day_falls_in_period",
    "tradingdaycount",
    "workspace"
  ]
}
```

## coverage

```json
{
  "normalized_clause_count": 1,
  "formula_bearing_item_count": 3,
  "formula_to_clause_compression_ratio": 0.3333333333333333,
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
  "source_content_token_count": 10,
  "source_content_token_mass": 21,
  "formula_content_token_count": 19,
  "formula_content_token_mass": 94,
  "full_surface_content_token_count": 42,
  "full_surface_content_token_mass": 121,
  "formula_content_token_recall": 0.6,
  "full_surface_content_token_recall": 0.6,
  "full_surface_content_token_jaccard": 0.13043478260869565,
  "formula_content_token_multiset_recall": 0.5714285714285714,
  "formula_content_token_multiset_precision": 0.1276595744680851,
  "formula_repeat_overuse_token_count": 18,
  "formula_repeat_overuse_mass": 82,
  "formula_repeat_underuse_token_count": 8,
  "formula_repeat_underuse_mass": 9,
  "formula_repeat_overuse_examples": [
    {
      "token": "period",
      "current_count": 12,
      "baseline_count": 2,
      "delta": 10
    },
    {
      "token": "specifiedperiod",
      "current_count": 8,
      "baseline_count": 0,
      "delta": 8
    },
    {
      "token": "daily",
      "current_count": 9,
      "baseline_count": 2,
      "delta": 7
    },
    {
      "token": "traded",
      "current_count": 9,
      "baseline_count": 2,
      "delta": 7
    },
    {
      "token": "value",
      "current_count": 9,
      "baseline_count": 2,
      "delta": 7
    },
    {
      "token": "trading",
      "current_count": 8,
      "baseline_count": 1,
      "delta": 7
    },
    {
      "token": "indexcomponent",
      "current_count": 6,
      "baseline_count": 0,
      "delta": 6
    },
    {
      "token": "tradingday",
      "current_count": 5,
      "baseline_count": 0,
      "delta": 5
    },
    {
      "token": "required",
      "current_count": 4,
      "baseline_count": 0,
      "delta": 4
    },
    {
      "token": "over",
      "current_count": 4,
      "baseline_count": 1,
      "delta": 3
    },
    {
      "token": "dailyvaluetraded",
      "current_count": 3,
      "baseline_count": 0,
      "delta": 3
    },
    {
      "token": "definition",
      "current_count": 3,
      "baseline_count": 0,
      "delta": 3
    },
    {
      "token": "falls",
      "current_count": 3,
      "baseline_count": 0,
      "delta": 3
    },
    {
      "token": "average",
      "current_count": 3,
      "baseline_count": 1,
      "delta": 2
    },
    {
      "token": "averagedailyvaluetraded",
      "current_count": 2,
      "baseline_count": 0,
      "delta": 2
    },
    {
      "token": "real",
      "current_count": 2,
      "baseline_count": 0,
      "delta": 2
    },
    {
      "token": "tradingdaycount",
      "current_count": 2,
      "baseline_count": 0,
      "delta": 2
    },
    {
      "token": "financialinstrument",
      "current_count": 1,
      "baseline_count": 0,
      "delta": 1
    }
  ],
  "full_surface_content_token_multiset_recall": 0.5714285714285714,
  "full_surface_content_token_multiset_precision": 0.09917355371900827,
  "full_surface_repeat_overuse_token_count": 41,
  "full_surface_repeat_overuse_mass": 109,
  "full_surface_repeat_underuse_token_count": 8,
  "full_surface_repeat_underuse_mass": 9,
  "full_surface_repeat_overuse_examples": [
    {
      "token": "period",
      "current_count": 12,
      "baseline_count": 2,
      "delta": 10
    },
    {
      "token": "specifiedperiod",
      "current_count": 8,
      "baseline_count": 0,
      "delta": 8
    },
    {
      "token": "daily",
      "current_count": 9,
      "baseline_count": 2,
      "delta": 7
    },
    {
      "token": "traded",
      "current_count": 9,
      "baseline_count": 2,
      "delta": 7
    },
    {
      "token": "value",
      "current_count": 9,
      "baseline_count": 2,
      "delta": 7
    },
    {
      "token": "trading",
      "current_count": 8,
      "baseline_count": 1,
      "delta": 7
    },
    {
      "token": "indexcomponent",
      "current_count": 6,
      "baseline_count": 0,
      "delta": 6
    },
    {
      "token": "tradingday",
      "current_count": 5,
      "baseline_count": 0,
      "delta": 5
    },
    {
      "token": "required",
      "current_count": 4,
      "baseline_count": 0,
      "delta": 4
    },
    {
      "token": "over",
      "current_count": 4,
      "baseline_count": 1,
      "delta": 3
    },
    {
      "token": "dailyvaluetraded",
      "current_count": 3,
      "baseline_count": 0,
      "delta": 3
    },
    {
      "token": "definition",
      "current_count": 3,
      "baseline_count": 0,
      "delta": 3
    },
    {
      "token": "falls",
      "current_count": 3,
      "baseline_count": 0,
      "delta": 3
    },
    {
      "token": "average",
      "current_count": 3,
      "baseline_count": 1,
      "delta": 2
    },
    {
      "token": "averagedailyvaluetraded",
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
      "token": "real",
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
      "token": "tradingdaycount",
      "current_count": 2,
      "baseline_count": 0,
      "delta": 2
    }
  ],
  "source_to_formula_token_gap_count": 4,
  "source_to_full_surface_token_gap_count": 4,
  "source_content_tokens_missing_from_formula": [
    "component",
    "index",
    "number",
    "specified"
  ],
  "source_content_tokens_missing_from_full_surface": [
    "component",
    "index",
    "number",
    "specified"
  ]
}
```

## source_vs_normalized

```json
{
  "source_excerpt_content_token_count": 10,
  "source_excerpt_content_token_mass": 21,
  "normalized_content_token_count": 10,
  "normalized_content_token_mass": 21,
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
  "normalized_content_mass_per_clause": 21.0,
  "source_normalized_bertscore_precision": 1.0,
  "source_normalized_bertscore_recall": 1.0,
  "source_normalized_bertscore_f1": 1.0,
  "normalized_implies_source_entailment": 0.9537801742553711,
  "source_implies_normalized_entailment": 0.9537801742553711,
  "source_vs_normalized_contradiction_score": 0.03286505118012428
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
  "notes_to_formula_content_ratio": 1.2105263157894737
}
```

## identifier_glue

```json
{
  "identifier_count": 16,
  "compound_identifier_count_raw": 7,
  "compound_identifier_count_content": 8,
  "compound_identifier_rate_raw": 0.4375,
  "compound_identifier_rate_content": 0.5,
  "max_identifier_piece_count_raw": 10,
  "max_identifier_piece_count_content": 8,
  "mean_identifier_piece_count_raw": 3.6875,
  "mean_identifier_piece_count_content": 3,
  "identifier_glue_excess_mass_raw": 22,
  "identifier_glue_excess_mass_content": 23,
  "identifier_glue_excess_rate_raw": 1.375,
  "identifier_glue_excess_rate_content": 1.4375,
  "source_grounded_content_piece_ratio_mean": 0.9520089285714286,
  "advisory_grounded_content_piece_ratio_mean": 0.9520089285714286,
  "low_source_grounded_glued_identifier_count": 0,
  "low_source_grounded_glued_identifier_rate": 0.0,
  "entity_relation_target_fusion_count": 0,
  "entity_relation_target_fusion_rate": 0.0,
  "conditional_relation_name_packing_count": 0,
  "conditional_relation_name_packing_rate": 0.0,
  "top_glued_identifiers": [
    {
      "identifier": "average_daily_value_traded_divided_by_trading_day_count_definition",
      "raw_piece_count": 10,
      "content_piece_count": 8,
      "raw_pieces": [
        "average",
        "daily",
        "value",
        "traded",
        "divided",
        "by",
        "trading",
        "day",
        "count",
        "definition"
      ],
      "content_pieces": [
        "average",
        "daily",
        "value",
        "traded",
        "divided",
        "trading",
        "day",
        "definition"
      ],
      "glue_excess_raw": 7,
      "glue_excess_content": 6,
      "source_grounded_content_piece_count": 7,
      "advisory_grounded_content_piece_count": 7,
      "source_grounded_content_piece_ratio": 0.875,
      "advisory_grounded_content_piece_ratio": 0.875
    },
    {
      "identifier": "daily_value_traded_sum_over_period_definition",
      "raw_piece_count": 7,
      "content_piece_count": 7,
      "raw_pieces": [
        "daily",
        "value",
        "traded",
        "sum",
        "over",
        "period",
        "definition"
      ],
      "content_pieces": [
        "daily",
        "value",
        "traded",
        "sum",
        "over",
        "period",
        "definition"
      ],
      "glue_excess_raw": 4,
      "glue_excess_content": 5,
      "source_grounded_content_piece_count": 6,
      "advisory_grounded_content_piece_count": 6,
      "source_grounded_content_piece_ratio": 0.8571428571428571,
      "advisory_grounded_content_piece_ratio": 0.8571428571428571
    },
    {
      "identifier": "daily_value_traded_sum_over_period",
      "raw_piece_count": 6,
      "content_piece_count": 6,
      "raw_pieces": [
        "daily",
        "value",
        "traded",
        "sum",
        "over",
        "period"
      ],
      "content_pieces": [
        "daily",
        "value",
        "traded",
        "sum",
        "over",
        "period"
      ],
      "glue_excess_raw": 3,
      "glue_excess_content": 4,
      "source_grounded_content_piece_count": 6,
      "advisory_grounded_content_piece_count": 6,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    },
    {
      "identifier": "trading_day_count_in_period_definition",
      "raw_piece_count": 6,
      "content_piece_count": 4,
      "raw_pieces": [
        "trading",
        "day",
        "count",
        "in",
        "period",
        "definition"
      ],
      "content_pieces": [
        "trading",
        "day",
        "period",
        "definition"
      ],
      "glue_excess_raw": 3,
      "glue_excess_content": 2,
      "source_grounded_content_piece_count": 3,
      "advisory_grounded_content_piece_count": 3,
      "source_grounded_content_piece_ratio": 0.75,
      "advisory_grounded_content_piece_ratio": 0.75
    },
    {
      "identifier": "trading_day_falls_in_period",
      "raw_piece_count": 5,
      "content_piece_count": 4,
      "raw_pieces": [
        "trading",
        "day",
        "falls",
        "in",
        "period"
      ],
      "content_pieces": [
        "trading",
        "day",
        "falls",
        "period"
      ],
      "glue_excess_raw": 2,
      "glue_excess_content": 2,
      "source_grounded_content_piece_count": 3,
      "advisory_grounded_content_piece_count": 3,
      "source_grounded_content_piece_ratio": 0.75,
      "advisory_grounded_content_piece_ratio": 0.75
    },
    {
      "identifier": "AverageDailyValueTraded",
      "raw_piece_count": 4,
      "content_piece_count": 4,
      "raw_pieces": [
        "average",
        "daily",
        "value",
        "traded"
      ],
      "content_pieces": [
        "average",
        "daily",
        "value",
        "traded"
      ],
      "glue_excess_raw": 1,
      "glue_excess_content": 2,
      "source_grounded_content_piece_count": 4,
      "advisory_grounded_content_piece_count": 4,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    },
    {
      "identifier": "trading_day_count_in_period",
      "raw_piece_count": 5,
      "content_piece_count": 3,
      "raw_pieces": [
        "trading",
        "day",
        "count",
        "in",
        "period"
      ],
      "content_pieces": [
        "trading",
        "day",
        "period"
      ],
      "glue_excess_raw": 2,
      "glue_excess_content": 1,
      "source_grounded_content_piece_count": 3,
      "advisory_grounded_content_piece_count": 3,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    },
    {
      "identifier": "DailyValueTraded",
      "raw_piece_count": 3,
      "content_piece_count": 3,
      "raw_pieces": [
        "daily",
        "value",
        "traded"
      ],
      "content_pieces": [
        "daily",
        "value",
        "traded"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 1,
      "source_grounded_content_piece_count": 3,
      "advisory_grounded_content_piece_count": 3,
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
      "identifier": "SpecifiedPeriod",
      "raw_piece_count": 2,
      "content_piece_count": 2,
      "raw_pieces": [
        "specified",
        "period"
      ],
      "content_pieces": [
        "specified",
        "period"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 0,
      "source_grounded_content_piece_count": 2,
      "advisory_grounded_content_piece_count": 2,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    },
    {
      "identifier": "TradingDay",
      "raw_piece_count": 2,
      "content_piece_count": 2,
      "raw_pieces": [
        "trading",
        "day"
      ],
      "content_pieces": [
        "trading",
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
      "identifier": "TradingDayCount",
      "raw_piece_count": 3,
      "content_piece_count": 2,
      "raw_pieces": [
        "trading",
        "day",
        "count"
      ],
      "content_pieces": [
        "trading",
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
      "identifier": "sum",
      "raw_piece_count": 1,
      "content_piece_count": 1,
      "raw_pieces": [
        "sum"
      ],
      "content_pieces": [
        "sum"
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
    },
    {
      "identifier": "p",
      "raw_piece_count": 1,
      "content_piece_count": 0,
      "raw_pieces": [
        "p"
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
      "identifier": "trading_day_count_in_period_definition",
      "raw_piece_count": 6,
      "content_piece_count": 4,
      "raw_pieces": [
        "trading",
        "day",
        "count",
        "in",
        "period",
        "definition"
      ],
      "content_pieces": [
        "trading",
        "day",
        "period",
        "definition"
      ],
      "glue_excess_raw": 3,
      "glue_excess_content": 2,
      "source_grounded_content_piece_count": 3,
      "advisory_grounded_content_piece_count": 3,
      "source_grounded_content_piece_ratio": 0.75,
      "advisory_grounded_content_piece_ratio": 0.75
    },
    {
      "identifier": "trading_day_falls_in_period",
      "raw_piece_count": 5,
      "content_piece_count": 4,
      "raw_pieces": [
        "trading",
        "day",
        "falls",
        "in",
        "period"
      ],
      "content_pieces": [
        "trading",
        "day",
        "falls",
        "period"
      ],
      "glue_excess_raw": 2,
      "glue_excess_content": 2,
      "source_grounded_content_piece_count": 3,
      "advisory_grounded_content_piece_count": 3,
      "source_grounded_content_piece_ratio": 0.75,
      "advisory_grounded_content_piece_ratio": 0.75
    },
    {
      "identifier": "daily_value_traded_sum_over_period_definition",
      "raw_piece_count": 7,
      "content_piece_count": 7,
      "raw_pieces": [
        "daily",
        "value",
        "traded",
        "sum",
        "over",
        "period",
        "definition"
      ],
      "content_pieces": [
        "daily",
        "value",
        "traded",
        "sum",
        "over",
        "period",
        "definition"
      ],
      "glue_excess_raw": 4,
      "glue_excess_content": 5,
      "source_grounded_content_piece_count": 6,
      "advisory_grounded_content_piece_count": 6,
      "source_grounded_content_piece_ratio": 0.8571428571428571,
      "advisory_grounded_content_piece_ratio": 0.8571428571428571
    },
    {
      "identifier": "average_daily_value_traded_divided_by_trading_day_count_definition",
      "raw_piece_count": 10,
      "content_piece_count": 8,
      "raw_pieces": [
        "average",
        "daily",
        "value",
        "traded",
        "divided",
        "by",
        "trading",
        "day",
        "count",
        "definition"
      ],
      "content_pieces": [
        "average",
        "daily",
        "value",
        "traded",
        "divided",
        "trading",
        "day",
        "definition"
      ],
      "glue_excess_raw": 7,
      "glue_excess_content": 6,
      "source_grounded_content_piece_count": 7,
      "advisory_grounded_content_piece_count": 7,
      "source_grounded_content_piece_ratio": 0.875,
      "advisory_grounded_content_piece_ratio": 0.875
    },
    {
      "identifier": "daily_value_traded_sum_over_period",
      "raw_piece_count": 6,
      "content_piece_count": 6,
      "raw_pieces": [
        "daily",
        "value",
        "traded",
        "sum",
        "over",
        "period"
      ],
      "content_pieces": [
        "daily",
        "value",
        "traded",
        "sum",
        "over",
        "period"
      ],
      "glue_excess_raw": 3,
      "glue_excess_content": 4,
      "source_grounded_content_piece_count": 6,
      "advisory_grounded_content_piece_count": 6,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    },
    {
      "identifier": "AverageDailyValueTraded",
      "raw_piece_count": 4,
      "content_piece_count": 4,
      "raw_pieces": [
        "average",
        "daily",
        "value",
        "traded"
      ],
      "content_pieces": [
        "average",
        "daily",
        "value",
        "traded"
      ],
      "glue_excess_raw": 1,
      "glue_excess_content": 2,
      "source_grounded_content_piece_count": 4,
      "advisory_grounded_content_piece_count": 4,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    },
    {
      "identifier": "DailyValueTraded",
      "raw_piece_count": 3,
      "content_piece_count": 3,
      "raw_pieces": [
        "daily",
        "value",
        "traded"
      ],
      "content_pieces": [
        "daily",
        "value",
        "traded"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 1,
      "source_grounded_content_piece_count": 3,
      "advisory_grounded_content_piece_count": 3,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    },
    {
      "identifier": "trading_day_count_in_period",
      "raw_piece_count": 5,
      "content_piece_count": 3,
      "raw_pieces": [
        "trading",
        "day",
        "count",
        "in",
        "period"
      ],
      "content_pieces": [
        "trading",
        "day",
        "period"
      ],
      "glue_excess_raw": 2,
      "glue_excess_content": 1,
      "source_grounded_content_piece_count": 3,
      "advisory_grounded_content_piece_count": 3,
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
      "identifier": "SpecifiedPeriod",
      "raw_piece_count": 2,
      "content_piece_count": 2,
      "raw_pieces": [
        "specified",
        "period"
      ],
      "content_pieces": [
        "specified",
        "period"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 0,
      "source_grounded_content_piece_count": 2,
      "advisory_grounded_content_piece_count": 2,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    },
    {
      "identifier": "TradingDay",
      "raw_piece_count": 2,
      "content_piece_count": 2,
      "raw_pieces": [
        "trading",
        "day"
      ],
      "content_pieces": [
        "trading",
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
      "identifier": "TradingDayCount",
      "raw_piece_count": 3,
      "content_piece_count": 2,
      "raw_pieces": [
        "trading",
        "day",
        "count"
      ],
      "content_pieces": [
        "trading",
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
  "callable_symbol_count": 5,
  "callable_symbol_with_args_count": 5,
  "top_level_parameter_slot_count": 9,
  "quantifier_parameter_slot_count": 5,
  "total_parameter_slot_mass": 14,
  "factorization_count": 5,
  "parameter_slots_per_factor": 1.8,
  "factorization_index": 0.5555555555555556,
  "focus_symbol_signature": "missing",
  "focus_symbol_arity": null
}
```

## assertion_complexity

```json
{
  "assertion_count": 3,
  "mean_assertion_node_count": 9.333333333333334,
  "max_assertion_node_count": 12,
  "total_assertion_node_count": 28,
  "mean_assertion_depth": 5.333333333333333,
  "max_assertion_depth": 6,
  "total_ite_count": 0,
  "max_ite_count_per_assertion": 0,
  "total_quantifier_count": 5,
  "total_connective_count": 0,
  "total_branching_point_count": 0,
  "max_branching_point_count_per_assertion": 0,
  "mean_call_count_per_assertion": 2.3333333333333335,
  "single_assertion_logic_share": 0.42857142857142855,
  "overcompressed_single_assertion_flag": 0,
  "top_complex_assertions": [
    {
      "name": "average_daily_value_traded_divided_by_trading_day_count_definition",
      "assert_kind": "constraint",
      "node_count": 12,
      "depth": 6,
      "ite_count": 0,
      "quantifier_count": 2,
      "connective_count": 0,
      "branching_point_count": 0,
      "max_fanout": 2,
      "call_count": 3
    },
    {
      "name": "daily_value_traded_sum_over_period_definition",
      "assert_kind": "constraint",
      "node_count": 11,
      "depth": 6,
      "ite_count": 0,
      "quantifier_count": 2,
      "connective_count": 0,
      "branching_point_count": 0,
      "max_fanout": 2,
      "call_count": 3
    },
    {
      "name": "trading_day_count_in_period_definition",
      "assert_kind": "constraint",
      "node_count": 5,
      "depth": 4,
      "ite_count": 0,
      "quantifier_count": 1,
      "connective_count": 0,
      "branching_point_count": 0,
      "max_fanout": 2,
      "call_count": 1
    }
  ],
  "normalized_clause_count": 1,
  "node_count_per_normalized_clause": 28.0,
  "branching_point_count_per_normalized_clause": 0.0
}
```

## normalized_alignment

```json
{
  "normalized_clause_count": 1,
  "logic_block_count": 3,
  "clause_to_logic_block_ratio": 0.3333333333333333,
  "logic_block_to_clause_ratio": 3.0,
  "clause_underdecomposition_mass": 0,
  "clause_overdecomposition_mass": 2,
  "focus_symbol_arity": null,
  "helper_factorization_count": 5,
  "single_assertion_logic_share": 0.42857142857142855,
  "underdecomposed_logic_flag": 0
}
```

## normalized_relative

```json
{
  "new_formula_content_token_rate_vs_reference_mass": 0.7142857142857143,
  "new_full_surface_content_token_rate_vs_reference_mass": 1.619047619047619,
  "formula_repeat_overuse_rate": 3.9047619047619047,
  "full_surface_repeat_overuse_rate": 5.190476190476191,
  "parameter_slot_mass_per_clause": 14.0,
  "parameter_slot_mass_per_reference_token": 0.6666666666666666,
  "factorization_per_clause": 5.0,
  "factorization_per_reference_token": 0.23809523809523808,
  "notes_content_token_rate_vs_reference_mass": 1.0952380952380953
}
```

## tradeoff

```json
{
  "render_bertscore_f1_to_normalized_per_parameter_slot_mass": 0.05415281653404236,
  "render_bertscore_f1_to_source_per_parameter_slot_mass": 0.05415281653404236,
  "render_nli_ir_implies_text_per_parameter_slot_mass": 0.06325708542551313,
  "render_nli_text_implies_ir_per_parameter_slot_mass": 0.06442977700914655,
  "render_bertscore_f1_to_normalized_per_formula_repeat_overuse_mass": 0.009245602822885281,
  "render_nli_text_implies_ir_per_formula_repeat_overuse_mass": 0.011000205830829899,
  "render_nli_ir_implies_text_per_formula_repeat_overuse_mass": 0.010799990194599802,
  "render_bertscore_f1_to_normalized_per_full_surface_repeat_overuse_mass": 0.006955407628225624,
  "render_nli_text_implies_ir_per_full_surface_repeat_overuse_mass": 0.00827538420300965,
  "pairwise_structure_similarity_mean_per_parameter_slot_mass": null,
  "focus_signature_mode_share_per_parameter_slot_mass": 0.07142857142857142
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
  "parameter_slot_mass_mean": 14.0,
  "parameter_slot_mass_stddev": 0.0,
  "factorization_count_mean": 5.0,
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
  "render_back_text": "constraint daily value traded sum over period definition states that for every c of type index component, for every p of type specified period, daily value traded sum over period for c and p equals sum for set comp and daily value traded for c and d. constraint trading day count in period definition states that for every p of type specified period, trading day count in period for p equals the number of d of type trading day such that trading day falls in period for d and p. constraint average daily value traded divided by trading day count definition states that for every c of type index component, for every p of type specified period, average daily value traded for c and p equals div. index component is a type. trading day is a type. specified period is a type. daily value traded is a type. average daily value traded is a type. trading day count is a type. daily value traded maps index component and trading day to daily value traded. average daily value traded maps index component and specified period to average daily value traded. daily value traded sum over period maps index component and specified period to daily value traded. trading day count in period maps specified period to trading day count. trading day falls in period holds between trading day and specified period.",
  "render_bertscore_precision_to_normalized": 0.7154443264007568,
  "render_bertscore_recall_to_normalized": 0.8062538504600525,
  "render_bertscore_f1_to_normalized": 0.758139431476593,
  "render_bertscore_precision_to_source": 0.7154443264007568,
  "render_bertscore_recall_to_source": 0.8062538504600525,
  "render_bertscore_f1_to_source": 0.758139431476593,
  "render_nli_ir_implies_text": 0.8855991959571838,
  "render_nli_text_implies_ir": 0.9020168781280518,
  "render_nli_ir_implies_source": 0.8855991959571838,
  "render_nli_source_implies_ir": 0.9020168781280518,
  "render_nli_render_to_normalized": {
    "entailment": 0.8855991959571838,
    "neutral": 0.08039264380931854,
    "contradiction": 0.034008171409368515
  },
  "render_nli_normalized_to_render": {
    "entailment": 0.9020168781280518,
    "neutral": 0.060353007167577744,
    "contradiction": 0.0376301035284996
  },
  "render_nli_render_to_source": {
    "entailment": 0.8855991959571838,
    "neutral": 0.08039264380931854,
    "contradiction": 0.034008171409368515
  },
  "render_nli_source_to_render": {
    "entailment": 0.9020168781280518,
    "neutral": 0.060353007167577744,
    "contradiction": 0.0376301035284996
  },
  "render_contradiction_score": 0.0376301035284996
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
