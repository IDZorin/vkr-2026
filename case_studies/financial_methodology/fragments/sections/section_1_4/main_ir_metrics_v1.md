# Translation Metrics v1 - section_1_4

- generated_at: `2026-05-14T20:15:43.550530+02:00`
- artifact_path: `<PRIVATE_WORKSPACE>\case_studies\financial_methodology\sections\section_1_4\section_1_4_manual_section_workspace_artifact_current_v1.json`
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
  "ungrounded_symbol_count": 7,
  "ungrounded_sort_count": 8,
  "ungrounded_ref_count": 0,
  "ungrounded_callee_count": 0,
  "prelude_redeclaration_count": 0,
  "origin_error_count": 18,
  "new_formula_token_count_vs_text_only": 84,
  "new_formula_content_token_count_vs_text_only": 76,
  "new_formula_token_count_vs_text_prelude_only": 82,
  "new_formula_content_token_count_vs_text_prelude_only": 74,
  "new_formula_token_count_vs_text_prelude_advisory": 82,
  "new_formula_content_token_count_vs_text_prelude_advisory": 74,
  "new_full_surface_token_count_vs_text_only": 105,
  "new_full_surface_content_token_count_vs_text_only": 95,
  "new_full_surface_token_count_vs_text_prelude_only": 102,
  "new_full_surface_content_token_count_vs_text_prelude_only": 92,
  "new_full_surface_token_count_vs_text_prelude_advisory": 102,
  "new_full_surface_content_token_count_vs_text_prelude_advisory": 92,
  "new_formula_content_tokens_vs_text_only": [
    "calculation_mode",
    "calculation_time_from_to",
    "calculationday",
    "calculationmode",
    "calculationtime",
    "closing_calculation_price",
    "closing_level",
    "closing_level_based_on_closing_prices",
    "closing_level_calculated_each_calculation_day",
    "closing_level_calculated_on",
    "closing_price",
    "closing_price_converted_with_available_wm_fixing",
    "closing_price_converted_with_last_available_wm_fixing",
    "closing_price_kept_when_listed_in_index_currency",
    "closingprice",
    "converted_from_using",
    "current_ice_spot_foreign_exchange_rate",
    "current_ice_spot_foreign_exchange_rate_source",
    "current_trading_price",
    "current_trading_price_available",
    "current_trading_price_used_when_available",
    "fallback_price_candidates_are_temporally_comparable",
    "financialinstrument",
    "fixing_time",
    "foreign_exchange_rate_provider",
    "foreignexchangerate",
    "ice_alias",
    "index_component",
    "index_currency",
    "indexcomponent",
    "indexlevel",
    "intercontinentalexchange",
    "intraday_calculation_price",
    "intraday_calculation_time",
    "intraday_calculation_window",
    "intraday_level",
    "intraday_level_calculated_on",
    "intraday_level_uses_exchange_trading_prices",
    "intraday_price_converted_when_not_listed_in_index_currency",
    "intraday_price_kept_when_listed_in_index_currency",
    "intraday_source_price",
    "intradaycalculation",
    "last_available_trading_price",
    "last_available_wm_fixing_4pm_london",
    "last_available_wm_fixing_4pm_london_quoted_by_reuters",
    "later_of",
    "later_of_returns_a_candidate",
    "later_of_selects_temporally_later_candidate",
    "listed_currency",
    "listed_on_exchanges"
  ],
  "new_formula_content_tokens_vs_text_prelude_only": [
    "calculation_mode",
    "calculation_time_from_to",
    "calculationday",
    "calculationmode",
    "calculationtime",
    "closing_calculation_price",
    "closing_level",
    "closing_level_based_on_closing_prices",
    "closing_level_calculated_each_calculation_day",
    "closing_level_calculated_on",
    "closing_price",
    "closing_price_converted_with_available_wm_fixing",
    "closing_price_converted_with_last_available_wm_fixing",
    "closing_price_kept_when_listed_in_index_currency",
    "closingprice",
    "converted_from_using",
    "current_ice_spot_foreign_exchange_rate",
    "current_ice_spot_foreign_exchange_rate_source",
    "current_trading_price",
    "current_trading_price_available",
    "current_trading_price_used_when_available",
    "fallback_price_candidates_are_temporally_comparable",
    "fixing_time",
    "foreign_exchange_rate_provider",
    "foreignexchangerate",
    "ice_alias",
    "index_component",
    "index_currency",
    "indexcomponent",
    "indexlevel",
    "intercontinentalexchange",
    "intraday_calculation_price",
    "intraday_calculation_time",
    "intraday_calculation_window",
    "intraday_level",
    "intraday_level_calculated_on",
    "intraday_level_uses_exchange_trading_prices",
    "intraday_price_converted_when_not_listed_in_index_currency",
    "intraday_price_kept_when_listed_in_index_currency",
    "intraday_source_price",
    "intradaycalculation",
    "last_available_trading_price",
    "last_available_wm_fixing_4pm_london",
    "last_available_wm_fixing_4pm_london_quoted_by_reuters",
    "later_of",
    "later_of_returns_a_candidate",
    "later_of_selects_temporally_later_candidate",
    "listed_currency",
    "listed_on_exchanges",
    "londontime"
  ],
  "new_formula_content_tokens_vs_text_prelude_advisory": [
    "calculation_mode",
    "calculation_time_from_to",
    "calculationday",
    "calculationmode",
    "calculationtime",
    "closing_calculation_price",
    "closing_level",
    "closing_level_based_on_closing_prices",
    "closing_level_calculated_each_calculation_day",
    "closing_level_calculated_on",
    "closing_price",
    "closing_price_converted_with_available_wm_fixing",
    "closing_price_converted_with_last_available_wm_fixing",
    "closing_price_kept_when_listed_in_index_currency",
    "closingprice",
    "converted_from_using",
    "current_ice_spot_foreign_exchange_rate",
    "current_ice_spot_foreign_exchange_rate_source",
    "current_trading_price",
    "current_trading_price_available",
    "current_trading_price_used_when_available",
    "fallback_price_candidates_are_temporally_comparable",
    "fixing_time",
    "foreign_exchange_rate_provider",
    "foreignexchangerate",
    "ice_alias",
    "index_component",
    "index_currency",
    "indexcomponent",
    "indexlevel",
    "intercontinentalexchange",
    "intraday_calculation_price",
    "intraday_calculation_time",
    "intraday_calculation_window",
    "intraday_level",
    "intraday_level_calculated_on",
    "intraday_level_uses_exchange_trading_prices",
    "intraday_price_converted_when_not_listed_in_index_currency",
    "intraday_price_kept_when_listed_in_index_currency",
    "intraday_source_price",
    "intradaycalculation",
    "last_available_trading_price",
    "last_available_wm_fixing_4pm_london",
    "last_available_wm_fixing_4pm_london_quoted_by_reuters",
    "later_of",
    "later_of_returns_a_candidate",
    "later_of_selects_temporally_later_candidate",
    "listed_currency",
    "listed_on_exchanges",
    "londontime"
  ],
  "new_full_surface_content_tokens_vs_text_only": [
    "a4v3",
    "calculation_mode",
    "calculation_time_from_to",
    "calculationday",
    "calculationmode",
    "calculationtime",
    "canonical",
    "closing_calculation_price",
    "closing_level",
    "closing_level_based_on_closing_prices",
    "closing_level_calculated_each_calculation_day",
    "closing_level_calculated_on",
    "closing_price",
    "closing_price_converted_with_available_wm_fixing",
    "closing_price_converted_with_last_available_wm_fixing",
    "closing_price_kept_when_listed_in_index_currency",
    "closingprice",
    "computation",
    "converted_from_using",
    "current_ice_spot_foreign_exchange_rate",
    "current_ice_spot_foreign_exchange_rate_source",
    "current_trading_price",
    "current_trading_price_available",
    "current_trading_price_used_when_available",
    "deterministic",
    "draft",
    "fallback_price_candidates_are_temporally_comparable",
    "financialinstrument",
    "fixing_time",
    "foreign_exchange_rate_provider",
    "foreignexchangerate",
    "ice_alias",
    "index_component",
    "index_currency",
    "indexcomponent",
    "indexlevel",
    "intercontinentalexchange",
    "intraday_calculation_price",
    "intraday_calculation_time",
    "intraday_calculation_window",
    "intraday_level",
    "intraday_level_calculated_on",
    "intraday_level_uses_exchange_trading_prices",
    "intraday_price_converted_when_not_listed_in_index_currency",
    "intraday_price_kept_when_listed_in_index_currency",
    "intraday_source_price",
    "intradaycalculation",
    "last_available_trading_price",
    "last_available_wm_fixing_4pm_london",
    "last_available_wm_fixing_4pm_london_quoted_by_reuters"
  ],
  "new_full_surface_content_tokens_vs_text_prelude_only": [
    "calculation_mode",
    "calculation_time_from_to",
    "calculationday",
    "calculationmode",
    "calculationtime",
    "canonical",
    "closing_calculation_price",
    "closing_level",
    "closing_level_based_on_closing_prices",
    "closing_level_calculated_each_calculation_day",
    "closing_level_calculated_on",
    "closing_price",
    "closing_price_converted_with_available_wm_fixing",
    "closing_price_converted_with_last_available_wm_fixing",
    "closing_price_kept_when_listed_in_index_currency",
    "closingprice",
    "computation",
    "converted_from_using",
    "current_ice_spot_foreign_exchange_rate",
    "current_ice_spot_foreign_exchange_rate_source",
    "current_trading_price",
    "current_trading_price_available",
    "current_trading_price_used_when_available",
    "deterministic",
    "draft",
    "fallback_price_candidates_are_temporally_comparable",
    "fixing_time",
    "foreign_exchange_rate_provider",
    "foreignexchangerate",
    "ice_alias",
    "index_component",
    "index_currency",
    "indexcomponent",
    "indexlevel",
    "intercontinentalexchange",
    "intraday_calculation_price",
    "intraday_calculation_time",
    "intraday_calculation_window",
    "intraday_level",
    "intraday_level_calculated_on",
    "intraday_level_uses_exchange_trading_prices",
    "intraday_price_converted_when_not_listed_in_index_currency",
    "intraday_price_kept_when_listed_in_index_currency",
    "intraday_source_price",
    "intradaycalculation",
    "last_available_trading_price",
    "last_available_wm_fixing_4pm_london",
    "last_available_wm_fixing_4pm_london_quoted_by_reuters",
    "later_of",
    "later_of_returns_a_candidate"
  ],
  "new_full_surface_content_tokens_vs_text_prelude_advisory": [
    "calculation_mode",
    "calculation_time_from_to",
    "calculationday",
    "calculationmode",
    "calculationtime",
    "canonical",
    "closing_calculation_price",
    "closing_level",
    "closing_level_based_on_closing_prices",
    "closing_level_calculated_each_calculation_day",
    "closing_level_calculated_on",
    "closing_price",
    "closing_price_converted_with_available_wm_fixing",
    "closing_price_converted_with_last_available_wm_fixing",
    "closing_price_kept_when_listed_in_index_currency",
    "closingprice",
    "computation",
    "converted_from_using",
    "current_ice_spot_foreign_exchange_rate",
    "current_ice_spot_foreign_exchange_rate_source",
    "current_trading_price",
    "current_trading_price_available",
    "current_trading_price_used_when_available",
    "deterministic",
    "draft",
    "fallback_price_candidates_are_temporally_comparable",
    "fixing_time",
    "foreign_exchange_rate_provider",
    "foreignexchangerate",
    "ice_alias",
    "index_component",
    "index_currency",
    "indexcomponent",
    "indexlevel",
    "intercontinentalexchange",
    "intraday_calculation_price",
    "intraday_calculation_time",
    "intraday_calculation_window",
    "intraday_level",
    "intraday_level_calculated_on",
    "intraday_level_uses_exchange_trading_prices",
    "intraday_price_converted_when_not_listed_in_index_currency",
    "intraday_price_kept_when_listed_in_index_currency",
    "intraday_source_price",
    "intradaycalculation",
    "last_available_trading_price",
    "last_available_wm_fixing_4pm_london",
    "last_available_wm_fixing_4pm_london_quoted_by_reuters",
    "later_of",
    "later_of_returns_a_candidate"
  ]
}
```

## coverage

```json
{
  "normalized_clause_count": 3,
  "formula_bearing_item_count": 12,
  "formula_to_clause_compression_ratio": 0.25,
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
  "source_content_token_count": 31,
  "source_content_token_mass": 88,
  "formula_content_token_count": 75,
  "formula_content_token_mass": 681,
  "full_surface_content_token_count": 96,
  "full_surface_content_token_mass": 708,
  "formula_content_token_recall": 0.8064516129032258,
  "full_surface_content_token_recall": 0.8064516129032258,
  "full_surface_content_token_jaccard": 0.24509803921568626,
  "formula_content_token_multiset_recall": 0.8295454545454546,
  "formula_content_token_multiset_precision": 0.10719530102790015,
  "formula_repeat_overuse_token_count": 74,
  "formula_repeat_overuse_mass": 608,
  "formula_repeat_underuse_token_count": 10,
  "formula_repeat_underuse_mass": 15,
  "formula_repeat_overuse_examples": [
    {
      "token": "price",
      "current_count": 71,
      "baseline_count": 3,
      "delta": 68
    },
    {
      "token": "currency",
      "current_count": 51,
      "baseline_count": 2,
      "delta": 49
    },
    {
      "token": "calculationday",
      "current_count": 37,
      "baseline_count": 0,
      "delta": 37
    },
    {
      "token": "intraday",
      "current_count": 27,
      "baseline_count": 1,
      "delta": 26
    },
    {
      "token": "index",
      "current_count": 34,
      "baseline_count": 10,
      "delta": 24
    },
    {
      "token": "closing",
      "current_count": 30,
      "baseline_count": 6,
      "delta": 24
    },
    {
      "token": "fixing",
      "current_count": 26,
      "baseline_count": 3,
      "delta": 23
    },
    {
      "token": "indexcomponent",
      "current_count": 23,
      "baseline_count": 0,
      "delta": 23
    },
    {
      "token": "calculationtime",
      "current_count": 20,
      "baseline_count": 0,
      "delta": 20
    },
    {
      "token": "theindex",
      "current_count": 19,
      "baseline_count": 0,
      "delta": 19
    },
    {
      "token": "level",
      "current_count": 21,
      "baseline_count": 4,
      "delta": 17
    },
    {
      "token": "listed",
      "current_count": 21,
      "baseline_count": 4,
      "delta": 17
    },
    {
      "token": "required",
      "current_count": 17,
      "baseline_count": 0,
      "delta": 17
    },
    {
      "token": "available",
      "current_count": 18,
      "baseline_count": 2,
      "delta": 16
    },
    {
      "token": "exchange",
      "current_count": 15,
      "baseline_count": 2,
      "delta": 13
    },
    {
      "token": "trading",
      "current_count": 16,
      "baseline_count": 5,
      "delta": 11
    },
    {
      "token": "london",
      "current_count": 13,
      "baseline_count": 3,
      "delta": 10
    },
    {
      "token": "time",
      "current_count": 13,
      "baseline_count": 3,
      "delta": 10
    },
    {
      "token": "component",
      "current_count": 11,
      "baseline_count": 1,
      "delta": 10
    },
    {
      "token": "current",
      "current_count": 11,
      "baseline_count": 2,
      "delta": 9
    }
  ],
  "full_surface_content_token_multiset_recall": 0.8295454545454546,
  "full_surface_content_token_multiset_precision": 0.10310734463276836,
  "full_surface_repeat_overuse_token_count": 95,
  "full_surface_repeat_overuse_mass": 635,
  "full_surface_repeat_underuse_token_count": 10,
  "full_surface_repeat_underuse_mass": 15,
  "full_surface_repeat_overuse_examples": [
    {
      "token": "price",
      "current_count": 71,
      "baseline_count": 3,
      "delta": 68
    },
    {
      "token": "currency",
      "current_count": 51,
      "baseline_count": 2,
      "delta": 49
    },
    {
      "token": "calculationday",
      "current_count": 37,
      "baseline_count": 0,
      "delta": 37
    },
    {
      "token": "intraday",
      "current_count": 27,
      "baseline_count": 1,
      "delta": 26
    },
    {
      "token": "index",
      "current_count": 34,
      "baseline_count": 10,
      "delta": 24
    },
    {
      "token": "closing",
      "current_count": 30,
      "baseline_count": 6,
      "delta": 24
    },
    {
      "token": "fixing",
      "current_count": 26,
      "baseline_count": 3,
      "delta": 23
    },
    {
      "token": "indexcomponent",
      "current_count": 23,
      "baseline_count": 0,
      "delta": 23
    },
    {
      "token": "calculationtime",
      "current_count": 20,
      "baseline_count": 0,
      "delta": 20
    },
    {
      "token": "theindex",
      "current_count": 19,
      "baseline_count": 0,
      "delta": 19
    },
    {
      "token": "level",
      "current_count": 22,
      "baseline_count": 4,
      "delta": 18
    },
    {
      "token": "listed",
      "current_count": 21,
      "baseline_count": 4,
      "delta": 17
    },
    {
      "token": "required",
      "current_count": 17,
      "baseline_count": 0,
      "delta": 17
    },
    {
      "token": "available",
      "current_count": 18,
      "baseline_count": 2,
      "delta": 16
    },
    {
      "token": "exchange",
      "current_count": 15,
      "baseline_count": 2,
      "delta": 13
    },
    {
      "token": "trading",
      "current_count": 16,
      "baseline_count": 5,
      "delta": 11
    },
    {
      "token": "london",
      "current_count": 13,
      "baseline_count": 3,
      "delta": 10
    },
    {
      "token": "time",
      "current_count": 13,
      "baseline_count": 3,
      "delta": 10
    },
    {
      "token": "current",
      "current_count": 12,
      "baseline_count": 2,
      "delta": 10
    },
    {
      "token": "component",
      "current_count": 11,
      "baseline_count": 1,
      "delta": 10
    }
  ],
  "source_to_formula_token_gap_count": 6,
  "source_to_full_surface_token_gap_count": 6,
  "source_content_tokens_missing_from_formula": [
    "addition",
    "components",
    "intercontinental",
    "relevant",
    "respective",
    "should"
  ],
  "source_content_tokens_missing_from_full_surface": [
    "addition",
    "components",
    "intercontinental",
    "relevant",
    "respective",
    "should"
  ]
}
```

## source_vs_normalized

```json
{
  "source_excerpt_content_token_count": 31,
  "source_excerpt_content_token_mass": 88,
  "normalized_content_token_count": 31,
  "normalized_content_token_mass": 88,
  "normalized_clause_count": 3,
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
  "normalized_content_mass_per_clause": 29.333333333333332,
  "source_normalized_bertscore_precision": 1.0,
  "source_normalized_bertscore_recall": 1.0,
  "source_normalized_bertscore_f1": 1.0,
  "normalized_implies_source_entailment": 0.8523855209350586,
  "source_implies_normalized_entailment": 0.2663731276988983,
  "source_vs_normalized_contradiction_score": 0.09996511042118073
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
  "notes_to_formula_content_ratio": 0.30666666666666664
}
```

## identifier_glue

```json
{
  "identifier_count": 76,
  "compound_identifier_count_raw": 27,
  "compound_identifier_count_content": 32,
  "compound_identifier_rate_raw": 0.35526315789473684,
  "compound_identifier_rate_content": 0.42105263157894735,
  "max_identifier_piece_count_raw": 9,
  "max_identifier_piece_count_content": 7,
  "mean_identifier_piece_count_raw": 3.210526315789474,
  "mean_identifier_piece_count_content": 2.6578947368421053,
  "identifier_glue_excess_mass_raw": 65,
  "identifier_glue_excess_mass_content": 73,
  "identifier_glue_excess_rate_raw": 0.8552631578947368,
  "identifier_glue_excess_rate_content": 0.9605263157894737,
  "source_grounded_content_piece_ratio_mean": 0.8035401002506266,
  "advisory_grounded_content_piece_ratio_mean": 0.8035401002506266,
  "low_source_grounded_glued_identifier_count": 9,
  "low_source_grounded_glued_identifier_rate": 0.11842105263157894,
  "entity_relation_target_fusion_count": 1,
  "entity_relation_target_fusion_rate": 0.013157894736842105,
  "conditional_relation_name_packing_count": 1,
  "conditional_relation_name_packing_rate": 0.013157894736842105,
  "top_glued_identifiers": [
    {
      "identifier": "intraday_price_converted_when_not_listed_in_index_currency",
      "raw_piece_count": 9,
      "content_piece_count": 7,
      "raw_pieces": [
        "intraday",
        "price",
        "converted",
        "when",
        "not",
        "listed",
        "in",
        "index",
        "currency"
      ],
      "content_pieces": [
        "intraday",
        "price",
        "converted",
        "when",
        "listed",
        "index",
        "currency"
      ],
      "glue_excess_raw": 6,
      "glue_excess_content": 5,
      "source_grounded_content_piece_count": 6,
      "advisory_grounded_content_piece_count": 6,
      "source_grounded_content_piece_ratio": 0.8571428571428571,
      "advisory_grounded_content_piece_ratio": 0.8571428571428571
    },
    {
      "identifier": "closing_price_kept_when_listed_in_index_currency",
      "raw_piece_count": 8,
      "content_piece_count": 7,
      "raw_pieces": [
        "closing",
        "price",
        "kept",
        "when",
        "listed",
        "in",
        "index",
        "currency"
      ],
      "content_pieces": [
        "closing",
        "price",
        "kept",
        "when",
        "listed",
        "index",
        "currency"
      ],
      "glue_excess_raw": 5,
      "glue_excess_content": 5,
      "source_grounded_content_piece_count": 5,
      "advisory_grounded_content_piece_count": 5,
      "source_grounded_content_piece_ratio": 0.7142857142857143,
      "advisory_grounded_content_piece_ratio": 0.7142857142857143
    },
    {
      "identifier": "intraday_price_kept_when_listed_in_index_currency",
      "raw_piece_count": 8,
      "content_piece_count": 7,
      "raw_pieces": [
        "intraday",
        "price",
        "kept",
        "when",
        "listed",
        "in",
        "index",
        "currency"
      ],
      "content_pieces": [
        "intraday",
        "price",
        "kept",
        "when",
        "listed",
        "index",
        "currency"
      ],
      "glue_excess_raw": 5,
      "glue_excess_content": 5,
      "source_grounded_content_piece_count": 5,
      "advisory_grounded_content_piece_count": 5,
      "source_grounded_content_piece_ratio": 0.7142857142857143,
      "advisory_grounded_content_piece_ratio": 0.7142857142857143
    },
    {
      "identifier": "closing_price_converted_with_last_available_wm_fixing",
      "raw_piece_count": 8,
      "content_piece_count": 6,
      "raw_pieces": [
        "closing",
        "price",
        "converted",
        "with",
        "last",
        "available",
        "wm",
        "fixing"
      ],
      "content_pieces": [
        "closing",
        "price",
        "converted",
        "last",
        "available",
        "fixing"
      ],
      "glue_excess_raw": 5,
      "glue_excess_content": 4,
      "source_grounded_content_piece_count": 6,
      "advisory_grounded_content_piece_count": 6,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    },
    {
      "identifier": "intraday_level_uses_exchange_trading_prices",
      "raw_piece_count": 6,
      "content_piece_count": 6,
      "raw_pieces": [
        "intraday",
        "level",
        "uses",
        "exchange",
        "trading",
        "prices"
      ],
      "content_pieces": [
        "intraday",
        "level",
        "uses",
        "exchange",
        "trading",
        "prices"
      ],
      "glue_excess_raw": 3,
      "glue_excess_content": 4,
      "source_grounded_content_piece_count": 4,
      "advisory_grounded_content_piece_count": 4,
      "source_grounded_content_piece_ratio": 0.6666666666666666,
      "advisory_grounded_content_piece_ratio": 0.6666666666666666
    },
    {
      "identifier": "current_trading_price_used_when_available",
      "raw_piece_count": 6,
      "content_piece_count": 6,
      "raw_pieces": [
        "current",
        "trading",
        "price",
        "used",
        "when",
        "available"
      ],
      "content_pieces": [
        "current",
        "trading",
        "price",
        "used",
        "when",
        "available"
      ],
      "glue_excess_raw": 3,
      "glue_excess_content": 4,
      "source_grounded_content_piece_count": 5,
      "advisory_grounded_content_piece_count": 5,
      "source_grounded_content_piece_ratio": 0.8333333333333334,
      "advisory_grounded_content_piece_ratio": 0.8333333333333334
    },
    {
      "identifier": "current_ice_spot_foreign_exchange_rate",
      "raw_piece_count": 6,
      "content_piece_count": 6,
      "raw_pieces": [
        "current",
        "ice",
        "spot",
        "foreign",
        "exchange",
        "rate"
      ],
      "content_pieces": [
        "current",
        "ice",
        "spot",
        "foreign",
        "exchange",
        "rate"
      ],
      "glue_excess_raw": 3,
      "glue_excess_content": 4,
      "source_grounded_content_piece_count": 6,
      "advisory_grounded_content_piece_count": 6,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    },
    {
      "identifier": "closing_price_converted_with_available_wm_fixing",
      "raw_piece_count": 7,
      "content_piece_count": 5,
      "raw_pieces": [
        "closing",
        "price",
        "converted",
        "with",
        "available",
        "wm",
        "fixing"
      ],
      "content_pieces": [
        "closing",
        "price",
        "converted",
        "available",
        "fixing"
      ],
      "glue_excess_raw": 4,
      "glue_excess_content": 3,
      "source_grounded_content_piece_count": 5,
      "advisory_grounded_content_piece_count": 5,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    },
    {
      "identifier": "fallback_price_candidates_are_temporally_comparable",
      "raw_piece_count": 6,
      "content_piece_count": 5,
      "raw_pieces": [
        "fallback",
        "price",
        "candidates",
        "are",
        "temporally",
        "comparable"
      ],
      "content_pieces": [
        "fallback",
        "price",
        "candidates",
        "temporally",
        "comparable"
      ],
      "glue_excess_raw": 3,
      "glue_excess_content": 3,
      "source_grounded_content_piece_count": 1,
      "advisory_grounded_content_piece_count": 1,
      "source_grounded_content_piece_ratio": 0.2,
      "advisory_grounded_content_piece_ratio": 0.2
    },
    {
      "identifier": "later_of_selects_temporally_later_candidate",
      "raw_piece_count": 6,
      "content_piece_count": 5,
      "raw_pieces": [
        "later",
        "of",
        "selects",
        "temporally",
        "later",
        "candidate"
      ],
      "content_pieces": [
        "later",
        "selects",
        "temporally",
        "later",
        "candidate"
      ],
      "glue_excess_raw": 3,
      "glue_excess_content": 3,
      "source_grounded_content_piece_count": 2,
      "advisory_grounded_content_piece_count": 2,
      "source_grounded_content_piece_ratio": 0.4,
      "advisory_grounded_content_piece_ratio": 0.4
    },
    {
      "identifier": "closing_level_based_on_closing_prices",
      "raw_piece_count": 6,
      "content_piece_count": 5,
      "raw_pieces": [
        "closing",
        "level",
        "based",
        "on",
        "closing",
        "prices"
      ],
      "content_pieces": [
        "closing",
        "level",
        "based",
        "closing",
        "prices"
      ],
      "glue_excess_raw": 3,
      "glue_excess_content": 3,
      "source_grounded_content_piece_count": 4,
      "advisory_grounded_content_piece_count": 4,
      "source_grounded_content_piece_ratio": 0.8,
      "advisory_grounded_content_piece_ratio": 0.8
    },
    {
      "identifier": "last_available_wm_fixing_4pm_london",
      "raw_piece_count": 6,
      "content_piece_count": 5,
      "raw_pieces": [
        "last",
        "available",
        "wm",
        "fixing",
        "4pm",
        "london"
      ],
      "content_pieces": [
        "last",
        "available",
        "fixing",
        "4pm",
        "london"
      ],
      "glue_excess_raw": 3,
      "glue_excess_content": 3,
      "source_grounded_content_piece_count": 4,
      "advisory_grounded_content_piece_count": 4,
      "source_grounded_content_piece_ratio": 0.8,
      "advisory_grounded_content_piece_ratio": 0.8
    },
    {
      "identifier": "no_current_trading_price_fallback",
      "raw_piece_count": 5,
      "content_piece_count": 4,
      "raw_pieces": [
        "no",
        "current",
        "trading",
        "price",
        "fallback"
      ],
      "content_pieces": [
        "current",
        "trading",
        "price",
        "fallback"
      ],
      "glue_excess_raw": 2,
      "glue_excess_content": 2,
      "source_grounded_content_piece_count": 3,
      "advisory_grounded_content_piece_count": 3,
      "source_grounded_content_piece_ratio": 0.75,
      "advisory_grounded_content_piece_ratio": 0.75
    },
    {
      "identifier": "wm_fixing_4pm_london_available",
      "raw_piece_count": 5,
      "content_piece_count": 4,
      "raw_pieces": [
        "wm",
        "fixing",
        "4pm",
        "london",
        "available"
      ],
      "content_pieces": [
        "fixing",
        "4pm",
        "london",
        "available"
      ],
      "glue_excess_raw": 2,
      "glue_excess_content": 2,
      "source_grounded_content_piece_count": 3,
      "advisory_grounded_content_piece_count": 3,
      "source_grounded_content_piece_ratio": 0.75,
      "advisory_grounded_content_piece_ratio": 0.75
    },
    {
      "identifier": "foreign_exchange_rate_provider",
      "raw_piece_count": 4,
      "content_piece_count": 4,
      "raw_pieces": [
        "foreign",
        "exchange",
        "rate",
        "provider"
      ],
      "content_pieces": [
        "foreign",
        "exchange",
        "rate",
        "provider"
      ],
      "glue_excess_raw": 1,
      "glue_excess_content": 2,
      "source_grounded_content_piece_count": 3,
      "advisory_grounded_content_piece_count": 3,
      "source_grounded_content_piece_ratio": 0.75,
      "advisory_grounded_content_piece_ratio": 0.75
    },
    {
      "identifier": "current_trading_price_available",
      "raw_piece_count": 4,
      "content_piece_count": 4,
      "raw_pieces": [
        "current",
        "trading",
        "price",
        "available"
      ],
      "content_pieces": [
        "current",
        "trading",
        "price",
        "available"
      ],
      "glue_excess_raw": 1,
      "glue_excess_content": 2,
      "source_grounded_content_piece_count": 4,
      "advisory_grounded_content_piece_count": 4,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    },
    {
      "identifier": "last_available_trading_price",
      "raw_piece_count": 4,
      "content_piece_count": 4,
      "raw_pieces": [
        "last",
        "available",
        "trading",
        "price"
      ],
      "content_pieces": [
        "last",
        "available",
        "trading",
        "price"
      ],
      "glue_excess_raw": 1,
      "glue_excess_content": 2,
      "source_grounded_content_piece_count": 4,
      "advisory_grounded_content_piece_count": 4,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    },
    {
      "identifier": "most_recent_closing_price",
      "raw_piece_count": 4,
      "content_piece_count": 4,
      "raw_pieces": [
        "most",
        "recent",
        "closing",
        "price"
      ],
      "content_pieces": [
        "most",
        "recent",
        "closing",
        "price"
      ],
      "glue_excess_raw": 1,
      "glue_excess_content": 2,
      "source_grounded_content_piece_count": 4,
      "advisory_grounded_content_piece_count": 4,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    },
    {
      "identifier": "SpotForeignExchangeRate",
      "raw_piece_count": 4,
      "content_piece_count": 4,
      "raw_pieces": [
        "spot",
        "foreign",
        "exchange",
        "rate"
      ],
      "content_pieces": [
        "spot",
        "foreign",
        "exchange",
        "rate"
      ],
      "glue_excess_raw": 1,
      "glue_excess_content": 2,
      "source_grounded_content_piece_count": 4,
      "advisory_grounded_content_piece_count": 4,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    },
    {
      "identifier": "later_of_returns_a_candidate",
      "raw_piece_count": 5,
      "content_piece_count": 3,
      "raw_pieces": [
        "later",
        "of",
        "returns",
        "a",
        "candidate"
      ],
      "content_pieces": [
        "later",
        "returns",
        "candidate"
      ],
      "glue_excess_raw": 2,
      "glue_excess_content": 1,
      "source_grounded_content_piece_count": 1,
      "advisory_grounded_content_piece_count": 1,
      "source_grounded_content_piece_ratio": 0.3333333333333333,
      "advisory_grounded_content_piece_ratio": 0.3333333333333333
    }
  ],
  "lowest_source_grounded_identifiers": [
    {
      "identifier": "CalculationMode",
      "raw_piece_count": 2,
      "content_piece_count": 2,
      "raw_pieces": [
        "calculation",
        "mode"
      ],
      "content_pieces": [
        "calculation",
        "mode"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 0,
      "source_grounded_content_piece_count": 0,
      "advisory_grounded_content_piece_count": 0,
      "source_grounded_content_piece_ratio": 0.0,
      "advisory_grounded_content_piece_ratio": 0.0
    },
    {
      "identifier": "Time04_00PMLondon",
      "raw_piece_count": 3,
      "content_piece_count": 2,
      "raw_pieces": [
        "time04",
        "00",
        "pmlondon"
      ],
      "content_pieces": [
        "time04",
        "pmlondon"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 0,
      "source_grounded_content_piece_count": 0,
      "advisory_grounded_content_piece_count": 0,
      "source_grounded_content_piece_ratio": 0.0,
      "advisory_grounded_content_piece_ratio": 0.0
    },
    {
      "identifier": "Time10_50PMCET",
      "raw_piece_count": 3,
      "content_piece_count": 2,
      "raw_pieces": [
        "time10",
        "50",
        "pmcet"
      ],
      "content_pieces": [
        "time10",
        "pmcet"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 0,
      "source_grounded_content_piece_count": 0,
      "advisory_grounded_content_piece_count": 0,
      "source_grounded_content_piece_ratio": 0.0,
      "advisory_grounded_content_piece_ratio": 0.0
    },
    {
      "identifier": "Time1_00AMCET",
      "raw_piece_count": 3,
      "content_piece_count": 2,
      "raw_pieces": [
        "time1",
        "00",
        "amcet"
      ],
      "content_pieces": [
        "time1",
        "amcet"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 0,
      "source_grounded_content_piece_count": 0,
      "advisory_grounded_content_piece_count": 0,
      "source_grounded_content_piece_ratio": 0.0,
      "advisory_grounded_content_piece_ratio": 0.0
    },
    {
      "identifier": "fallback_price_candidates_are_temporally_comparable",
      "raw_piece_count": 6,
      "content_piece_count": 5,
      "raw_pieces": [
        "fallback",
        "price",
        "candidates",
        "are",
        "temporally",
        "comparable"
      ],
      "content_pieces": [
        "fallback",
        "price",
        "candidates",
        "temporally",
        "comparable"
      ],
      "glue_excess_raw": 3,
      "glue_excess_content": 3,
      "source_grounded_content_piece_count": 1,
      "advisory_grounded_content_piece_count": 1,
      "source_grounded_content_piece_ratio": 0.2,
      "advisory_grounded_content_piece_ratio": 0.2
    },
    {
      "identifier": "later_of_returns_a_candidate",
      "raw_piece_count": 5,
      "content_piece_count": 3,
      "raw_pieces": [
        "later",
        "of",
        "returns",
        "a",
        "candidate"
      ],
      "content_pieces": [
        "later",
        "returns",
        "candidate"
      ],
      "glue_excess_raw": 2,
      "glue_excess_content": 1,
      "source_grounded_content_piece_count": 1,
      "advisory_grounded_content_piece_count": 1,
      "source_grounded_content_piece_ratio": 0.3333333333333333,
      "advisory_grounded_content_piece_ratio": 0.3333333333333333
    },
    {
      "identifier": "price_selection_order",
      "raw_piece_count": 3,
      "content_piece_count": 3,
      "raw_pieces": [
        "price",
        "selection",
        "order"
      ],
      "content_pieces": [
        "price",
        "selection",
        "order"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 1,
      "source_grounded_content_piece_count": 1,
      "advisory_grounded_content_piece_count": 1,
      "source_grounded_content_piece_ratio": 0.3333333333333333,
      "advisory_grounded_content_piece_ratio": 0.3333333333333333
    },
    {
      "identifier": "later_of_selects_temporally_later_candidate",
      "raw_piece_count": 6,
      "content_piece_count": 5,
      "raw_pieces": [
        "later",
        "of",
        "selects",
        "temporally",
        "later",
        "candidate"
      ],
      "content_pieces": [
        "later",
        "selects",
        "temporally",
        "later",
        "candidate"
      ],
      "glue_excess_raw": 3,
      "glue_excess_content": 3,
      "source_grounded_content_piece_count": 2,
      "advisory_grounded_content_piece_count": 2,
      "source_grounded_content_piece_ratio": 0.4,
      "advisory_grounded_content_piece_ratio": 0.4
    },
    {
      "identifier": "calculation_time_from_to",
      "raw_piece_count": 4,
      "content_piece_count": 2,
      "raw_pieces": [
        "calculation",
        "time",
        "from",
        "to"
      ],
      "content_pieces": [
        "calculation",
        "time"
      ],
      "glue_excess_raw": 1,
      "glue_excess_content": 0,
      "source_grounded_content_piece_count": 1,
      "advisory_grounded_content_piece_count": 1,
      "source_grounded_content_piece_ratio": 0.5,
      "advisory_grounded_content_piece_ratio": 0.5
    },
    {
      "identifier": "CalculationDay",
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
      "source_grounded_content_piece_count": 1,
      "advisory_grounded_content_piece_count": 1,
      "source_grounded_content_piece_ratio": 0.5,
      "advisory_grounded_content_piece_ratio": 0.5
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
      "source_grounded_content_piece_count": 1,
      "advisory_grounded_content_piece_count": 1,
      "source_grounded_content_piece_ratio": 0.5,
      "advisory_grounded_content_piece_ratio": 0.5
    },
    {
      "identifier": "IntradayCalculation",
      "raw_piece_count": 2,
      "content_piece_count": 2,
      "raw_pieces": [
        "intraday",
        "calculation"
      ],
      "content_pieces": [
        "intraday",
        "calculation"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 0,
      "source_grounded_content_piece_count": 1,
      "advisory_grounded_content_piece_count": 1,
      "source_grounded_content_piece_ratio": 0.5,
      "advisory_grounded_content_piece_ratio": 0.5
    },
    {
      "identifier": "TimeZone",
      "raw_piece_count": 2,
      "content_piece_count": 2,
      "raw_pieces": [
        "time",
        "zone"
      ],
      "content_pieces": [
        "time",
        "zone"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 0,
      "source_grounded_content_piece_count": 1,
      "advisory_grounded_content_piece_count": 1,
      "source_grounded_content_piece_ratio": 0.5,
      "advisory_grounded_content_piece_ratio": 0.5
    },
    {
      "identifier": "intraday_level_uses_exchange_trading_prices",
      "raw_piece_count": 6,
      "content_piece_count": 6,
      "raw_pieces": [
        "intraday",
        "level",
        "uses",
        "exchange",
        "trading",
        "prices"
      ],
      "content_pieces": [
        "intraday",
        "level",
        "uses",
        "exchange",
        "trading",
        "prices"
      ],
      "glue_excess_raw": 3,
      "glue_excess_content": 4,
      "source_grounded_content_piece_count": 4,
      "advisory_grounded_content_piece_count": 4,
      "source_grounded_content_piece_ratio": 0.6666666666666666,
      "advisory_grounded_content_piece_ratio": 0.6666666666666666
    },
    {
      "identifier": "closing_calculation_price",
      "raw_piece_count": 3,
      "content_piece_count": 3,
      "raw_pieces": [
        "closing",
        "calculation",
        "price"
      ],
      "content_pieces": [
        "closing",
        "calculation",
        "price"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 1,
      "source_grounded_content_piece_count": 2,
      "advisory_grounded_content_piece_count": 2,
      "source_grounded_content_piece_ratio": 0.6666666666666666,
      "advisory_grounded_content_piece_ratio": 0.6666666666666666
    },
    {
      "identifier": "intraday_calculation_price",
      "raw_piece_count": 3,
      "content_piece_count": 3,
      "raw_pieces": [
        "intraday",
        "calculation",
        "price"
      ],
      "content_pieces": [
        "intraday",
        "calculation",
        "price"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 1,
      "source_grounded_content_piece_count": 2,
      "advisory_grounded_content_piece_count": 2,
      "source_grounded_content_piece_ratio": 0.6666666666666666,
      "advisory_grounded_content_piece_ratio": 0.6666666666666666
    },
    {
      "identifier": "intraday_calculation_time",
      "raw_piece_count": 3,
      "content_piece_count": 3,
      "raw_pieces": [
        "intraday",
        "calculation",
        "time"
      ],
      "content_pieces": [
        "intraday",
        "calculation",
        "time"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 1,
      "source_grounded_content_piece_count": 2,
      "advisory_grounded_content_piece_count": 2,
      "source_grounded_content_piece_ratio": 0.6666666666666666,
      "advisory_grounded_content_piece_ratio": 0.6666666666666666
    },
    {
      "identifier": "wm_fixing_4pm_london",
      "raw_piece_count": 4,
      "content_piece_count": 3,
      "raw_pieces": [
        "wm",
        "fixing",
        "4pm",
        "london"
      ],
      "content_pieces": [
        "fixing",
        "4pm",
        "london"
      ],
      "glue_excess_raw": 1,
      "glue_excess_content": 1,
      "source_grounded_content_piece_count": 2,
      "advisory_grounded_content_piece_count": 2,
      "source_grounded_content_piece_ratio": 0.6666666666666666,
      "advisory_grounded_content_piece_ratio": 0.6666666666666666
    },
    {
      "identifier": "closing_price_kept_when_listed_in_index_currency",
      "raw_piece_count": 8,
      "content_piece_count": 7,
      "raw_pieces": [
        "closing",
        "price",
        "kept",
        "when",
        "listed",
        "in",
        "index",
        "currency"
      ],
      "content_pieces": [
        "closing",
        "price",
        "kept",
        "when",
        "listed",
        "index",
        "currency"
      ],
      "glue_excess_raw": 5,
      "glue_excess_content": 5,
      "source_grounded_content_piece_count": 5,
      "advisory_grounded_content_piece_count": 5,
      "source_grounded_content_piece_ratio": 0.7142857142857143,
      "advisory_grounded_content_piece_ratio": 0.7142857142857143
    },
    {
      "identifier": "intraday_price_kept_when_listed_in_index_currency",
      "raw_piece_count": 8,
      "content_piece_count": 7,
      "raw_pieces": [
        "intraday",
        "price",
        "kept",
        "when",
        "listed",
        "in",
        "index",
        "currency"
      ],
      "content_pieces": [
        "intraday",
        "price",
        "kept",
        "when",
        "listed",
        "index",
        "currency"
      ],
      "glue_excess_raw": 5,
      "glue_excess_content": 5,
      "source_grounded_content_piece_count": 5,
      "advisory_grounded_content_piece_count": 5,
      "source_grounded_content_piece_ratio": 0.7142857142857143,
      "advisory_grounded_content_piece_ratio": 0.7142857142857143
    }
  ],
  "entity_relation_target_fusion_examples": [
    {
      "identifier": "current_trading_price_used_when_available",
      "raw_piece_count": 6,
      "content_piece_count": 6,
      "raw_pieces": [
        "current",
        "trading",
        "price",
        "used",
        "when",
        "available"
      ],
      "content_pieces": [
        "current",
        "trading",
        "price",
        "used",
        "when",
        "available"
      ],
      "glue_excess_raw": 3,
      "glue_excess_content": 4,
      "source_grounded_content_piece_count": 5,
      "advisory_grounded_content_piece_count": 5,
      "source_grounded_content_piece_ratio": 0.8333333333333334,
      "advisory_grounded_content_piece_ratio": 0.8333333333333334
    }
  ],
  "conditional_relation_name_packing_examples": [
    {
      "identifier": "intraday_price_converted_when_not_listed_in_index_currency",
      "raw_piece_count": 9,
      "content_piece_count": 7,
      "raw_pieces": [
        "intraday",
        "price",
        "converted",
        "when",
        "not",
        "listed",
        "in",
        "index",
        "currency"
      ],
      "content_pieces": [
        "intraday",
        "price",
        "converted",
        "when",
        "listed",
        "index",
        "currency"
      ],
      "glue_excess_raw": 6,
      "glue_excess_content": 5,
      "source_grounded_content_piece_count": 6,
      "advisory_grounded_content_piece_count": 6,
      "source_grounded_content_piece_ratio": 0.8571428571428571,
      "advisory_grounded_content_piece_ratio": 0.8571428571428571
    }
  ]
}
```

## parameterization

```json
{
  "callable_symbol_count": 33,
  "callable_symbol_with_args_count": 33,
  "top_level_parameter_slot_count": 83,
  "quantifier_parameter_slot_count": 32,
  "total_parameter_slot_mass": 115,
  "factorization_count": 33,
  "parameter_slots_per_factor": 2.515151515151515,
  "factorization_index": 0.39759036144578314,
  "focus_symbol_signature": "missing",
  "focus_symbol_arity": null
}
```

## assertion_complexity

```json
{
  "assertion_count": 12,
  "mean_assertion_node_count": 30,
  "max_assertion_node_count": 52,
  "total_assertion_node_count": 360,
  "mean_assertion_depth": 7.916666666666667,
  "max_assertion_depth": 9,
  "total_ite_count": 0,
  "max_ite_count_per_assertion": 0,
  "total_quantifier_count": 32,
  "total_connective_count": 33,
  "total_branching_point_count": 36,
  "max_branching_point_count_per_assertion": 4,
  "mean_call_count_per_assertion": 8.416666666666666,
  "single_assertion_logic_share": 0.14444444444444443,
  "overcompressed_single_assertion_flag": 0,
  "top_complex_assertions": [
    {
      "name": "closing_price_converted_with_last_available_wm_fixing",
      "assert_kind": "constraint",
      "node_count": 52,
      "depth": 8,
      "ite_count": 0,
      "quantifier_count": 2,
      "connective_count": 5,
      "branching_point_count": 4,
      "max_fanout": 3,
      "call_count": 18
    },
    {
      "name": "closing_price_converted_with_available_wm_fixing",
      "assert_kind": "constraint",
      "node_count": 51,
      "depth": 8,
      "ite_count": 0,
      "quantifier_count": 2,
      "connective_count": 4,
      "branching_point_count": 4,
      "max_fanout": 3,
      "call_count": 18
    },
    {
      "name": "intraday_price_converted_when_not_listed_in_index_currency",
      "assert_kind": "constraint",
      "node_count": 35,
      "depth": 9,
      "ite_count": 0,
      "quantifier_count": 3,
      "connective_count": 3,
      "branching_point_count": 3,
      "max_fanout": 4,
      "call_count": 10
    },
    {
      "name": "intraday_level_uses_exchange_trading_prices",
      "assert_kind": "constraint",
      "node_count": 33,
      "depth": 9,
      "ite_count": 0,
      "quantifier_count": 4,
      "connective_count": 3,
      "branching_point_count": 4,
      "max_fanout": 3,
      "call_count": 8
    },
    {
      "name": "fallback_price_candidates_are_temporally_comparable",
      "assert_kind": "constraint",
      "node_count": 30,
      "depth": 9,
      "ite_count": 0,
      "quantifier_count": 3,
      "connective_count": 3,
      "branching_point_count": 3,
      "max_fanout": 3,
      "call_count": 10
    },
    {
      "name": "no_current_trading_price_fallback",
      "assert_kind": "constraint",
      "node_count": 30,
      "depth": 9,
      "ite_count": 0,
      "quantifier_count": 3,
      "connective_count": 3,
      "branching_point_count": 3,
      "max_fanout": 3,
      "call_count": 8
    },
    {
      "name": "intraday_price_kept_when_listed_in_index_currency",
      "assert_kind": "constraint",
      "node_count": 26,
      "depth": 8,
      "ite_count": 0,
      "quantifier_count": 3,
      "connective_count": 2,
      "branching_point_count": 3,
      "max_fanout": 3,
      "call_count": 6
    },
    {
      "name": "closing_level_based_on_closing_prices",
      "assert_kind": "constraint",
      "node_count": 25,
      "depth": 8,
      "ite_count": 0,
      "quantifier_count": 3,
      "connective_count": 2,
      "branching_point_count": 3,
      "max_fanout": 3,
      "call_count": 7
    },
    {
      "name": "current_trading_price_used_when_available",
      "assert_kind": "constraint",
      "node_count": 24,
      "depth": 7,
      "ite_count": 0,
      "quantifier_count": 3,
      "connective_count": 2,
      "branching_point_count": 3,
      "max_fanout": 3,
      "call_count": 5
    },
    {
      "name": "later_of_selects_temporally_later_candidate",
      "assert_kind": "constraint",
      "node_count": 21,
      "depth": 7,
      "ite_count": 0,
      "quantifier_count": 2,
      "connective_count": 3,
      "branching_point_count": 3,
      "max_fanout": 2,
      "call_count": 4
    }
  ],
  "normalized_clause_count": 3,
  "node_count_per_normalized_clause": 120.0,
  "branching_point_count_per_normalized_clause": 12.0
}
```

## normalized_alignment

```json
{
  "normalized_clause_count": 3,
  "logic_block_count": 12,
  "clause_to_logic_block_ratio": 0.25,
  "logic_block_to_clause_ratio": 4.0,
  "clause_underdecomposition_mass": 0,
  "clause_overdecomposition_mass": 9,
  "focus_symbol_arity": null,
  "helper_factorization_count": 33,
  "single_assertion_logic_share": 0.14444444444444443,
  "underdecomposed_logic_flag": 0
}
```

## normalized_relative

```json
{
  "new_formula_content_token_rate_vs_reference_mass": 0.8409090909090909,
  "new_full_surface_content_token_rate_vs_reference_mass": 1.0454545454545454,
  "formula_repeat_overuse_rate": 6.909090909090909,
  "full_surface_repeat_overuse_rate": 7.215909090909091,
  "parameter_slot_mass_per_clause": 38.333333333333336,
  "parameter_slot_mass_per_reference_token": 1.3068181818181819,
  "factorization_per_clause": 11.0,
  "factorization_per_reference_token": 0.375,
  "notes_content_token_rate_vs_reference_mass": 0.26136363636363635
}
```

## tradeoff

```json
{
  "render_bertscore_f1_to_normalized_per_parameter_slot_mass": 0.006537910648014234,
  "render_bertscore_f1_to_source_per_parameter_slot_mass": 0.006537910648014234,
  "render_nli_ir_implies_text_per_parameter_slot_mass": 0.0005520188290139903,
  "render_nli_text_implies_ir_per_parameter_slot_mass": 0.0016016472940859588,
  "render_bertscore_f1_to_normalized_per_formula_repeat_overuse_mass": 0.0012366113890158502,
  "render_nli_text_implies_ir_per_formula_repeat_overuse_mass": 0.00030294315595375866,
  "render_nli_ir_implies_text_per_formula_repeat_overuse_mass": 0.0001044114561457383,
  "render_bertscore_f1_to_normalized_per_full_surface_repeat_overuse_mass": 0.0011840310622387984,
  "render_nli_text_implies_ir_per_full_surface_repeat_overuse_mass": 0.00029006210837777204,
  "pairwise_structure_similarity_mean_per_parameter_slot_mass": null,
  "focus_signature_mode_share_per_parameter_slot_mass": 0.008695652173913044
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
  "parameter_slot_mass_mean": 115.0,
  "parameter_slot_mass_stddev": 0.0,
  "factorization_count_mean": 33.0,
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
  "render_back_text": "constraint intraday level uses exchange trading prices states that for every d of type calculation day, for every t of type calculation time, for every c of type index component, if (intraday calculation time for d and t and index component for d and c), then there exists e of type exchange, (listed on exchanges for d, c, and e, price on exchange for intraday source price for c, d, and t and e, and price used for level for intraday level for the index, d, and t, c, and intraday calculation price for c, d, and t). constraint current trading price used when available states that for every d of type calculation day, for every t of type calculation time, for every c of type index component, if (intraday calculation time for d and t, index component for d and c, and current trading price available for c, d, and t), then intraday source price for c, d, and t equals current trading price for c, d, and t. constraint no current trading price fallback states that for every d of type calculation day, for every t of type calculation time, for every c of type index component, if (intraday calculation time for d and t, index component for d and c, and not (current trading price available for c, d, and t)), then intraday source price for c, d, and t equals later of for most recent closing price for c, d, and t and last available trading price for c and preceding trading day for d. constraint fallback price candidates are temporally comparable states that for every d of type calculation day, for every t of type calculation time, for every c of type index component, if (intraday calculation time for d and t and index component for d and c), then (price selection order for most recent closing price for c, d, and t and last available trading price for c and preceding trading day for d or price selection order for last available trading price for c and preceding trading day for d and most recent closing price for c, d, and t). constraint later of returns a candidate states that for every p1 of type price, for every p2 of type price, (later of for p1 and p2 equals p1 or later of for p1 and p2 equals p2). constraint later of selects temporally later candidate states that for every p1 of type price, for every p2 of type price, (if price selection order for p1 and p2, then later of for p1 and p2 equals p1 and if price selection order for p2 and p1, then later of for p1 and p2 equals p2). constraint intraday price kept when listed in index currency states that for every d of type calculation day, for every t of type calculation time, for every c of type index component, if (intraday calculation time for d and t, index component for d and c, and listed currency for d and c equals index currency for the index), then intraday calculation price for c, d, and t equals intraday source price for c, d, and t. constraint intraday price converted when not listed in index currency states that for every d of type calculation day, for every t of type calculation time, for every c of type index component, if (intraday calculation time for d and t, index component for d and c, and not (listed currency for d and c equals index currency for the index)), then converted from using for intraday calculation price for c, d, and t, intraday source price for c, d, and t, and current ice spot foreign exchange rate for listed currency for d and c, index currency for the index, d, and t. constraint closing level based on closing prices states that for every d of type calculation day, for every c of type index component, if index component for d and c, then there exists e of type exchange, (listed on exchanges for d, c, and e, price on exchange for closing price for c and d and e, and price used for level for closing level for the index and d, c, and closing calculation price for c and d). constraint closing price kept when listed in index currency states that for every d of type calculation day, for every c of type index component, if (index component for d and c and listed currency for d and c equals index currency for the index), then closing calculation price for c and d equals closing price for c and d. constraint closing price converted with available wm fixing states that for every d of type calculation day, for every c of type index component, if (index component for d and c, not (listed currency for d and c equals index currency for the index), and wm fixing 4pm london available for listed currency for d and c, index currency for the index, and d), then (wm fixing for closing level for listed currency for d and c, index currency for the index, and d equals wm fixing 4pm london for listed currency for d and c, index currency for the index, and d and converted from using for closing calculation price for c and d, closing price for c and d, and wm fixing for closing level for listed currency for d and c, index currency for the index, and d). constraint closing price converted with last available wm fixing states that for every d of type calculation day, for every c of type index component, if (index component for d and c, not (listed currency for d and c equals index currency for the index), and not (wm fixing 4pm london available for listed currency for d and c, index currency for the index, and d)), then (wm fixing for closing level for listed currency for d and c, index currency for the index, and d equals last available wm fixing 4pm london for listed currency for d and c, index currency for the index, and d and converted from using for closing calculation price for c and d, closing price for c and d, and wm fixing for closing level for listed currency for d and c, index currency for the index, and d). index is a type. index component is a type. calculation day is a type. trading day is a type. exchange is a type. calculation time is a type. calculation mode is a type. time of day is a type. time zone is a type. index level is a type. price is a type. trading price is a type. closing price is a type. foreign exchange rate is a type. spot foreign exchange rate is a type. wmfixing is a type. the index is a distinguished entity. time1 00 amcet is a distinguished entity. time10 50 pmcet is a distinguished entity. time04 00 pmlondon is a distinguished entity. intraday calculation is a distinguished entity. cet is a distinguished entity. london time is a distinguished entity. intercontinental exchange is a distinguished entity. ice is a distinguished entity. reuters is a distinguished entity. index currency maps index to currency. intraday level maps index, calculation day, and calculation time to index level. closing level maps index and calculation day to index level. intraday source price maps index component, calculation day, and calculation time to price. intraday calculation price maps index component, calculation day, and calculation time to price. current trading price maps index component, calculation day, and calculation time to trading price. most recent closing price maps index component, calculation day, and calculation time to closing price. preceding trading day maps calculation day to trading day. last available trading price maps index component and trading day to trading price. later of maps price and price to price. closing price maps index component and calculation day to closing price. closing calculation price maps index component and calculation day to price. listed currency maps calculation day and index component to currency. current ice spot foreign exchange rate maps currency, currency, calculation day, and calculation time to spot foreign exchange rate. wm fixing 4pm london maps currency, currency, and calculation day to wmfixing. last available wm fixing 4pm london maps currency, currency, and calculation day to wmfixing. wm fixing for closing level maps currency, currency, and calculation day to wmfixing. index component holds between calculation day and index component. intraday calculation time holds between calculation day and calculation time. calculation mode holds between calculation time and calculation mode. calculation time from to holds between calculation time, time of day, time of day, and time zone. listed on exchanges holds between calculation day, index component, and exchange. price on exchange holds between price and exchange. intraday level calculated on holds between index level, calculation day, and calculation time. closing level calculated on holds between index level and calculation day. price used for level holds between index level, index component, and price. current trading price available holds between index component, calculation day, and calculation time. price selection order holds between price and price. converted from using holds between price, price, and foreign exchange rate. foreign exchange rate provider holds between foreign exchange rate and organization. wm fixing 4pm london available holds between currency, currency, and calculation day. wm fixing quoted by holds between wmfixing and organization. fixing time holds between wmfixing, time of day, and time zone.",
  "render_bertscore_precision_to_normalized": 0.7456996440887451,
  "render_bertscore_recall_to_normalized": 0.7581225633621216,
  "render_bertscore_f1_to_normalized": 0.751859724521637,
  "render_bertscore_precision_to_source": 0.7456996440887451,
  "render_bertscore_recall_to_source": 0.7581225633621216,
  "render_bertscore_f1_to_source": 0.751859724521637,
  "render_nli_ir_implies_text": 0.06348216533660889,
  "render_nli_text_implies_ir": 0.18418943881988525,
  "render_nli_ir_implies_source": 0.05739765986800194,
  "render_nli_source_implies_ir": 0.1320609599351883,
  "render_nli_render_to_normalized": {
    "entailment": 0.06348216533660889,
    "neutral": 0.32006335258483887,
    "contradiction": 0.6164544820785522
  },
  "render_nli_normalized_to_render": {
    "entailment": 0.18418943881988525,
    "neutral": 0.5922081470489502,
    "contradiction": 0.22360242903232574
  },
  "render_nli_render_to_source": {
    "entailment": 0.05739765986800194,
    "neutral": 0.5578505992889404,
    "contradiction": 0.38475173711776733
  },
  "render_nli_source_to_render": {
    "entailment": 0.1320609599351883,
    "neutral": 0.8019876480102539,
    "contradiction": 0.06595135480165482
  },
  "render_contradiction_score": 0.6164544820785522
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
