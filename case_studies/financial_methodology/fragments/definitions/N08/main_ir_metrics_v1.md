# Translation Metrics v1 - N08

- generated_at: `2026-05-20T03:37:40.915339+02:00`
- artifact_path: `case_studies\financial_methodology\definitions\N08\N08_manual_section_workspace_artifact_current_v1.json`
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
  "new_formula_token_count_vs_text_only": 15,
  "new_formula_content_token_count_vs_text_only": 13,
  "new_formula_token_count_vs_text_prelude_only": 13,
  "new_formula_content_token_count_vs_text_prelude_only": 11,
  "new_formula_token_count_vs_text_prelude_advisory": 13,
  "new_formula_content_token_count_vs_text_prelude_advisory": 11,
  "new_full_surface_token_count_vs_text_only": 39,
  "new_full_surface_content_token_count_vs_text_only": 33,
  "new_full_surface_token_count_vs_text_prelude_only": 35,
  "new_full_surface_content_token_count_vs_text_prelude_only": 30,
  "new_full_surface_token_count_vs_text_prelude_advisory": 35,
  "new_full_surface_content_token_count_vs_text_prelude_advisory": 30,
  "new_formula_content_tokens_vs_text_only": [
    "closing_price",
    "closingprice",
    "daily_value_traded",
    "daily_value_traded_product_definition",
    "dailyvaluetraded",
    "financialinstrument",
    "indexcomponent",
    "monetaryamount",
    "required",
    "respective_exchange",
    "tradingday",
    "volume_traded_on_exchange_during_trading_day",
    "volumenumberofshares"
  ],
  "new_formula_content_tokens_vs_text_prelude_only": [
    "closing_price",
    "closingprice",
    "daily_value_traded",
    "daily_value_traded_product_definition",
    "dailyvaluetraded",
    "indexcomponent",
    "monetaryamount",
    "required",
    "respective_exchange",
    "volume_traded_on_exchange_during_trading_day",
    "volumenumberofshares"
  ],
  "new_formula_content_tokens_vs_text_prelude_advisory": [
    "closing_price",
    "closingprice",
    "daily_value_traded",
    "daily_value_traded_product_definition",
    "dailyvaluetraded",
    "indexcomponent",
    "monetaryamount",
    "required",
    "respective_exchange",
    "volume_traded_on_exchange_during_trading_day",
    "volumenumberofshares"
  ],
  "new_full_surface_content_tokens_vs_text_only": [
    "a4v3",
    "canonical",
    "closing_price",
    "closingprice",
    "computation",
    "current",
    "daily_value_traded",
    "daily_value_traded_product_definition",
    "dailyvaluetraded",
    "deterministic",
    "draft",
    "financialinstrument",
    "indexcomponent",
    "main_ir",
    "manual",
    "metric",
    "monetaryamount",
    "parsed",
    "primitive_usage",
    "recomputation",
    "reconstructed",
    "rendering_notes",
    "required",
    "residual_risks",
    "respective_exchange",
    "section",
    "section-level",
    "strengths",
    "text",
    "tradingday",
    "volume_traded_on_exchange_during_trading_day",
    "volumenumberofshares",
    "workspace"
  ],
  "new_full_surface_content_tokens_vs_text_prelude_only": [
    "canonical",
    "closing_price",
    "closingprice",
    "computation",
    "current",
    "daily_value_traded",
    "daily_value_traded_product_definition",
    "dailyvaluetraded",
    "deterministic",
    "draft",
    "indexcomponent",
    "main_ir",
    "manual",
    "metric",
    "monetaryamount",
    "parsed",
    "primitive_usage",
    "recomputation",
    "reconstructed",
    "rendering_notes",
    "required",
    "residual_risks",
    "respective_exchange",
    "section",
    "section-level",
    "strengths",
    "text",
    "volume_traded_on_exchange_during_trading_day",
    "volumenumberofshares",
    "workspace"
  ],
  "new_full_surface_content_tokens_vs_text_prelude_advisory": [
    "canonical",
    "closing_price",
    "closingprice",
    "computation",
    "current",
    "daily_value_traded",
    "daily_value_traded_product_definition",
    "dailyvaluetraded",
    "deterministic",
    "draft",
    "indexcomponent",
    "main_ir",
    "manual",
    "metric",
    "monetaryamount",
    "parsed",
    "primitive_usage",
    "recomputation",
    "reconstructed",
    "rendering_notes",
    "required",
    "residual_risks",
    "respective_exchange",
    "section",
    "section-level",
    "strengths",
    "text",
    "volume_traded_on_exchange_during_trading_day",
    "volumenumberofshares",
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
  "source_content_token_count": 14,
  "source_content_token_mass": 26,
  "formula_content_token_count": 20,
  "formula_content_token_mass": 56,
  "full_surface_content_token_count": 43,
  "full_surface_content_token_mass": 83,
  "formula_content_token_recall": 0.6428571428571429,
  "full_surface_content_token_recall": 0.6428571428571429,
  "full_surface_content_token_jaccard": 0.1875,
  "formula_content_token_multiset_recall": 0.46153846153846156,
  "formula_content_token_multiset_precision": 0.21428571428571427,
  "formula_repeat_overuse_token_count": 18,
  "formula_repeat_overuse_mass": 44,
  "formula_repeat_underuse_token_count": 8,
  "formula_repeat_underuse_mass": 14,
  "formula_repeat_overuse_examples": [
    {
      "token": "exchange",
      "current_count": 7,
      "baseline_count": 1,
      "delta": 6
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
      "token": "traded",
      "current_count": 5,
      "baseline_count": 2,
      "delta": 3
    },
    {
      "token": "daily",
      "current_count": 3,
      "baseline_count": 1,
      "delta": 2
    },
    {
      "token": "value",
      "current_count": 3,
      "baseline_count": 1,
      "delta": 2
    },
    {
      "token": "closingprice",
      "current_count": 2,
      "baseline_count": 0,
      "delta": 2
    },
    {
      "token": "dailyvaluetraded",
      "current_count": 2,
      "baseline_count": 0,
      "delta": 2
    },
    {
      "token": "monetaryamount",
      "current_count": 2,
      "baseline_count": 0,
      "delta": 2
    },
    {
      "token": "respective",
      "current_count": 2,
      "baseline_count": 0,
      "delta": 2
    },
    {
      "token": "volumenumberofshares",
      "current_count": 2,
      "baseline_count": 0,
      "delta": 2
    },
    {
      "token": "closing",
      "current_count": 2,
      "baseline_count": 1,
      "delta": 1
    },
    {
      "token": "during",
      "current_count": 2,
      "baseline_count": 1,
      "delta": 1
    },
    {
      "token": "price",
      "current_count": 2,
      "baseline_count": 1,
      "delta": 1
    },
    {
      "token": "volume",
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
  "full_surface_content_token_multiset_recall": 0.46153846153846156,
  "full_surface_content_token_multiset_precision": 0.14457831325301204,
  "full_surface_repeat_overuse_token_count": 41,
  "full_surface_repeat_overuse_mass": 71,
  "full_surface_repeat_underuse_token_count": 8,
  "full_surface_repeat_underuse_mass": 14,
  "full_surface_repeat_overuse_examples": [
    {
      "token": "exchange",
      "current_count": 7,
      "baseline_count": 1,
      "delta": 6
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
      "token": "traded",
      "current_count": 5,
      "baseline_count": 2,
      "delta": 3
    },
    {
      "token": "daily",
      "current_count": 3,
      "baseline_count": 1,
      "delta": 2
    },
    {
      "token": "value",
      "current_count": 3,
      "baseline_count": 1,
      "delta": 2
    },
    {
      "token": "closingprice",
      "current_count": 2,
      "baseline_count": 0,
      "delta": 2
    },
    {
      "token": "dailyvaluetraded",
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
      "token": "monetaryamount",
      "current_count": 2,
      "baseline_count": 0,
      "delta": 2
    },
    {
      "token": "respective",
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
      "token": "volumenumberofshares",
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
      "token": "closing",
      "current_count": 2,
      "baseline_count": 1,
      "delta": 1
    },
    {
      "token": "during",
      "current_count": 2,
      "baseline_count": 1,
      "delta": 1
    },
    {
      "token": "price",
      "current_count": 2,
      "baseline_count": 1,
      "delta": 1
    },
    {
      "token": "volume",
      "current_count": 2,
      "baseline_count": 1,
      "delta": 1
    }
  ],
  "source_to_formula_token_gap_count": 5,
  "source_to_full_surface_token_gap_count": 5,
  "source_content_tokens_missing_from_formula": [
    "component",
    "index",
    "measured",
    "number",
    "shares"
  ],
  "source_content_tokens_missing_from_full_surface": [
    "component",
    "index",
    "measured",
    "number",
    "shares"
  ]
}
```

## source_vs_normalized

```json
{
  "source_excerpt_content_token_count": 14,
  "source_excerpt_content_token_mass": 26,
  "normalized_content_token_count": 14,
  "normalized_content_token_mass": 26,
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
  "normalized_content_mass_per_clause": 26.0,
  "source_normalized_bertscore_precision": 1.0,
  "source_normalized_bertscore_recall": 1.0,
  "source_normalized_bertscore_f1": 1.0,
  "normalized_implies_source_entailment": 0.8933804035186768,
  "source_implies_normalized_entailment": 0.8933804035186768,
  "source_vs_normalized_contradiction_score": 0.0849866271018982
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
  "notes_to_formula_content_ratio": 1.15
}
```

## identifier_glue

```json
{
  "identifier_count": 11,
  "compound_identifier_count_raw": 3,
  "compound_identifier_count_content": 4,
  "compound_identifier_rate_raw": 0.2727272727272727,
  "compound_identifier_rate_content": 0.36363636363636365,
  "max_identifier_piece_count_raw": 7,
  "max_identifier_piece_count_content": 6,
  "mean_identifier_piece_count_raw": 2.727272727272727,
  "mean_identifier_piece_count_content": 2.3636363636363638,
  "identifier_glue_excess_mass_raw": 7,
  "identifier_glue_excess_mass_content": 9,
  "identifier_glue_excess_rate_raw": 0.6363636363636364,
  "identifier_glue_excess_rate_content": 0.8181818181818182,
  "source_grounded_content_piece_ratio_mean": 0.9363636363636364,
  "advisory_grounded_content_piece_ratio_mean": 0.9363636363636364,
  "low_source_grounded_glued_identifier_count": 0,
  "low_source_grounded_glued_identifier_rate": 0.0,
  "entity_relation_target_fusion_count": 0,
  "entity_relation_target_fusion_rate": 0.0,
  "conditional_relation_name_packing_count": 0,
  "conditional_relation_name_packing_rate": 0.0,
  "top_glued_identifiers": [
    {
      "identifier": "volume_traded_on_exchange_during_trading_day",
      "raw_piece_count": 7,
      "content_piece_count": 6,
      "raw_pieces": [
        "volume",
        "traded",
        "on",
        "exchange",
        "during",
        "trading",
        "day"
      ],
      "content_pieces": [
        "volume",
        "traded",
        "exchange",
        "during",
        "trading",
        "day"
      ],
      "glue_excess_raw": 4,
      "glue_excess_content": 4,
      "source_grounded_content_piece_count": 6,
      "advisory_grounded_content_piece_count": 6,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    },
    {
      "identifier": "daily_value_traded_product_definition",
      "raw_piece_count": 5,
      "content_piece_count": 5,
      "raw_pieces": [
        "daily",
        "value",
        "traded",
        "product",
        "definition"
      ],
      "content_pieces": [
        "daily",
        "value",
        "traded",
        "product",
        "definition"
      ],
      "glue_excess_raw": 2,
      "glue_excess_content": 3,
      "source_grounded_content_piece_count": 4,
      "advisory_grounded_content_piece_count": 4,
      "source_grounded_content_piece_ratio": 0.8,
      "advisory_grounded_content_piece_ratio": 0.8
    },
    {
      "identifier": "VolumeNumberOfShares",
      "raw_piece_count": 4,
      "content_piece_count": 3,
      "raw_pieces": [
        "volume",
        "number",
        "of",
        "shares"
      ],
      "content_pieces": [
        "volume",
        "number",
        "shares"
      ],
      "glue_excess_raw": 1,
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
      "identifier": "respective_exchange",
      "raw_piece_count": 2,
      "content_piece_count": 2,
      "raw_pieces": [
        "respective",
        "exchange"
      ],
      "content_pieces": [
        "respective",
        "exchange"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 0,
      "source_grounded_content_piece_count": 1,
      "advisory_grounded_content_piece_count": 1,
      "source_grounded_content_piece_ratio": 0.5,
      "advisory_grounded_content_piece_ratio": 0.5
    },
    {
      "identifier": "ClosingPrice",
      "raw_piece_count": 2,
      "content_piece_count": 2,
      "raw_pieces": [
        "closing",
        "price"
      ],
      "content_pieces": [
        "closing",
        "price"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 0,
      "source_grounded_content_piece_count": 2,
      "advisory_grounded_content_piece_count": 2,
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
    }
  ],
  "lowest_source_grounded_identifiers": [
    {
      "identifier": "respective_exchange",
      "raw_piece_count": 2,
      "content_piece_count": 2,
      "raw_pieces": [
        "respective",
        "exchange"
      ],
      "content_pieces": [
        "respective",
        "exchange"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 0,
      "source_grounded_content_piece_count": 1,
      "advisory_grounded_content_piece_count": 1,
      "source_grounded_content_piece_ratio": 0.5,
      "advisory_grounded_content_piece_ratio": 0.5
    },
    {
      "identifier": "daily_value_traded_product_definition",
      "raw_piece_count": 5,
      "content_piece_count": 5,
      "raw_pieces": [
        "daily",
        "value",
        "traded",
        "product",
        "definition"
      ],
      "content_pieces": [
        "daily",
        "value",
        "traded",
        "product",
        "definition"
      ],
      "glue_excess_raw": 2,
      "glue_excess_content": 3,
      "source_grounded_content_piece_count": 4,
      "advisory_grounded_content_piece_count": 4,
      "source_grounded_content_piece_ratio": 0.8,
      "advisory_grounded_content_piece_ratio": 0.8
    },
    {
      "identifier": "volume_traded_on_exchange_during_trading_day",
      "raw_piece_count": 7,
      "content_piece_count": 6,
      "raw_pieces": [
        "volume",
        "traded",
        "on",
        "exchange",
        "during",
        "trading",
        "day"
      ],
      "content_pieces": [
        "volume",
        "traded",
        "exchange",
        "during",
        "trading",
        "day"
      ],
      "glue_excess_raw": 4,
      "glue_excess_content": 4,
      "source_grounded_content_piece_count": 6,
      "advisory_grounded_content_piece_count": 6,
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
      "identifier": "VolumeNumberOfShares",
      "raw_piece_count": 4,
      "content_piece_count": 3,
      "raw_pieces": [
        "volume",
        "number",
        "of",
        "shares"
      ],
      "content_pieces": [
        "volume",
        "number",
        "shares"
      ],
      "glue_excess_raw": 1,
      "glue_excess_content": 1,
      "source_grounded_content_piece_count": 3,
      "advisory_grounded_content_piece_count": 3,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    },
    {
      "identifier": "ClosingPrice",
      "raw_piece_count": 2,
      "content_piece_count": 2,
      "raw_pieces": [
        "closing",
        "price"
      ],
      "content_pieces": [
        "closing",
        "price"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 0,
      "source_grounded_content_piece_count": 2,
      "advisory_grounded_content_piece_count": 2,
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
    }
  ],
  "entity_relation_target_fusion_examples": [],
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
  "mean_assertion_depth": 7,
  "max_assertion_depth": 7,
  "total_ite_count": 0,
  "max_ite_count_per_assertion": 0,
  "total_quantifier_count": 2,
  "total_connective_count": 0,
  "total_branching_point_count": 0,
  "max_branching_point_count_per_assertion": 0,
  "mean_call_count_per_assertion": 4,
  "single_assertion_logic_share": 1.0,
  "overcompressed_single_assertion_flag": 0,
  "top_complex_assertions": [
    {
      "name": "daily_value_traded_product_definition",
      "assert_kind": "constraint",
      "node_count": 15,
      "depth": 7,
      "ite_count": 0,
      "quantifier_count": 2,
      "connective_count": 0,
      "branching_point_count": 0,
      "max_fanout": 3,
      "call_count": 4
    }
  ],
  "normalized_clause_count": 1,
  "node_count_per_normalized_clause": 15.0,
  "branching_point_count_per_normalized_clause": 0.0
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
  "new_formula_content_token_rate_vs_reference_mass": 0.4230769230769231,
  "new_full_surface_content_token_rate_vs_reference_mass": 1.1538461538461537,
  "formula_repeat_overuse_rate": 1.6923076923076923,
  "full_surface_repeat_overuse_rate": 2.730769230769231,
  "parameter_slot_mass_per_clause": 10.0,
  "parameter_slot_mass_per_reference_token": 0.38461538461538464,
  "factorization_per_clause": 4.0,
  "factorization_per_reference_token": 0.15384615384615385,
  "notes_content_token_rate_vs_reference_mass": 0.8846153846153846
}
```

## tradeoff

```json
{
  "render_bertscore_f1_to_normalized_per_parameter_slot_mass": 0.07881668210029602,
  "render_bertscore_f1_to_source_per_parameter_slot_mass": 0.07881668210029602,
  "render_nli_ir_implies_text_per_parameter_slot_mass": 0.08810922503471375,
  "render_nli_text_implies_ir_per_parameter_slot_mass": 0.08433000445365905,
  "render_bertscore_f1_to_normalized_per_formula_repeat_overuse_mass": 0.017912882295521824,
  "render_nli_text_implies_ir_per_formula_repeat_overuse_mass": 0.019165910103104332,
  "render_nli_ir_implies_text_per_formula_repeat_overuse_mass": 0.020024823871525852,
  "render_bertscore_f1_to_normalized_per_full_surface_repeat_overuse_mass": 0.011100941140886764,
  "render_nli_text_implies_ir_per_full_surface_repeat_overuse_mass": 0.011877465416008318,
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
  "render_back_text": "constraint daily value traded product definition states that for every c of type index component, for every d of type trading day, daily value traded for c and d equals mul. index component is a type. trading day is a type. exchange is a type. closing price is a type. daily value traded is a type. volume number of shares is a type. closing price maps index component and trading day to closing price. daily value traded maps index component and trading day to daily value traded. volume traded on exchange during trading day maps index component, exchange, and trading day to volume number of shares. respective exchange maps index component to exchange.",
  "render_bertscore_precision_to_normalized": 0.7847849130630493,
  "render_bertscore_recall_to_normalized": 0.7915780544281006,
  "render_bertscore_f1_to_normalized": 0.7881668210029602,
  "render_bertscore_precision_to_source": 0.7847849130630493,
  "render_bertscore_recall_to_source": 0.7915780544281006,
  "render_bertscore_f1_to_source": 0.7881668210029602,
  "render_nli_ir_implies_text": 0.8810922503471375,
  "render_nli_text_implies_ir": 0.8433000445365906,
  "render_nli_ir_implies_source": 0.8810922503471375,
  "render_nli_source_implies_ir": 0.8433000445365906,
  "render_nli_render_to_normalized": {
    "entailment": 0.8810922503471375,
    "neutral": 0.054573725908994675,
    "contradiction": 0.06433402746915817
  },
  "render_nli_normalized_to_render": {
    "entailment": 0.8433000445365906,
    "neutral": 0.0835597887635231,
    "contradiction": 0.07314027100801468
  },
  "render_nli_render_to_source": {
    "entailment": 0.8810922503471375,
    "neutral": 0.054573725908994675,
    "contradiction": 0.06433402746915817
  },
  "render_nli_source_to_render": {
    "entailment": 0.8433000445365906,
    "neutral": 0.0835597887635231,
    "contradiction": 0.07314027100801468
  },
  "render_contradiction_score": 0.07314027100801468
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
