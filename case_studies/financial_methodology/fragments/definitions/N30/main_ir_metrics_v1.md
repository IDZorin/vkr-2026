# Translation Metrics v1 - N30

- generated_at: `2026-05-12T22:32:05.798677+02:00`
- artifact_path: `D:\OneDrive\Documents\Study\MIPT\VKR\research_experiments\2026-02_pipeline\case_studies\financial_methodology\definitions\N30\N30_manual_section_workspace_artifact_current_v1.json`
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
  "ungrounded_symbol_count": 17,
  "ungrounded_sort_count": 3,
  "ungrounded_ref_count": 0,
  "ungrounded_callee_count": 0,
  "prelude_redeclaration_count": 0,
  "origin_error_count": 20,
  "new_formula_token_count_vs_text_only": 70,
  "new_formula_content_token_count_vs_text_only": 60,
  "new_formula_token_count_vs_text_prelude_only": 68,
  "new_formula_content_token_count_vs_text_prelude_only": 58,
  "new_formula_token_count_vs_text_prelude_advisory": 68,
  "new_formula_content_token_count_vs_text_prelude_advisory": 58,
  "new_full_surface_token_count_vs_text_only": 93,
  "new_full_surface_content_token_count_vs_text_only": 80,
  "new_full_surface_token_count_vs_text_prelude_only": 90,
  "new_full_surface_content_token_count_vs_text_prelude_only": 77,
  "new_full_surface_token_count_vs_text_prelude_advisory": 90,
  "new_full_surface_content_token_count_vs_text_prelude_advisory": 77,
  "new_formula_content_tokens_vs_text_only": [
    "calculation_day_immediately_following_rebalance_day",
    "calculationday",
    "cessation_possibility_day",
    "cessation_possibility_exchange",
    "close_of_trading_exchange",
    "close_of_trading_rebalance_day",
    "closeoftrading",
    "context_captures_new_index_component_close_of_trading",
    "context_component",
    "context_component_included_at_following_calculation_day",
    "context_component_included_at_rebalance_day",
    "context_day",
    "context_exchange",
    "context_excluded_by_prior_to_close_cessation",
    "context_excluded_by_scheduled_shortened_period",
    "context_rebalance_day",
    "context_satisfies_market_disruption_counterfactual",
    "context_satisfies_open_for_trading_condition",
    "determination_decides_whether_context_is_trading_day",
    "early_cessation_exclusion",
    "exchange_open_for_trading",
    "exchangeclosingtime",
    "financialinstrument",
    "following_calculation_day_component_scope",
    "inclusion_component",
    "inclusion_day",
    "inclusion_index",
    "index_administrator_responsibility_for_trading_day_determination",
    "indexadministrator",
    "indexadministratorforthisindex",
    "indexcomponent",
    "indexcomponentinclusion",
    "market_disruption_counterfactual_condition",
    "market_disruption_occurred",
    "new_index_components_close_of_trading_clarification",
    "open_for_trading_condition",
    "organization",
    "prior_to",
    "rebalance_day_component_scope",
    "rebalanceday",
    "relevant_exchange",
    "required",
    "scheduled_exchange_closing_time",
    "scheduled_shortened_period_exclusion",
    "scheduledshortenedperiod",
    "security",
    "security_to_be_included_in_index_as_new_index_component",
    "shortened_period_day",
    "shortened_period_exchange",
    "theindex"
  ],
  "new_formula_content_tokens_vs_text_prelude_only": [
    "calculation_day_immediately_following_rebalance_day",
    "calculationday",
    "cessation_possibility_day",
    "cessation_possibility_exchange",
    "close_of_trading_exchange",
    "close_of_trading_rebalance_day",
    "closeoftrading",
    "context_captures_new_index_component_close_of_trading",
    "context_component",
    "context_component_included_at_following_calculation_day",
    "context_component_included_at_rebalance_day",
    "context_day",
    "context_exchange",
    "context_excluded_by_prior_to_close_cessation",
    "context_excluded_by_scheduled_shortened_period",
    "context_rebalance_day",
    "context_satisfies_market_disruption_counterfactual",
    "context_satisfies_open_for_trading_condition",
    "determination_decides_whether_context_is_trading_day",
    "early_cessation_exclusion",
    "exchange_open_for_trading",
    "exchangeclosingtime",
    "following_calculation_day_component_scope",
    "inclusion_component",
    "inclusion_day",
    "inclusion_index",
    "index_administrator_responsibility_for_trading_day_determination",
    "indexadministrator",
    "indexadministratorforthisindex",
    "indexcomponent",
    "indexcomponentinclusion",
    "market_disruption_counterfactual_condition",
    "market_disruption_occurred",
    "new_index_components_close_of_trading_clarification",
    "open_for_trading_condition",
    "organization",
    "prior_to",
    "rebalance_day_component_scope",
    "relevant_exchange",
    "required",
    "scheduled_exchange_closing_time",
    "scheduled_shortened_period_exclusion",
    "scheduledshortenedperiod",
    "security",
    "security_to_be_included_in_index_as_new_index_component",
    "shortened_period_day",
    "shortened_period_exchange",
    "theindex",
    "theindexadministrator",
    "trading_day"
  ],
  "new_formula_content_tokens_vs_text_prelude_advisory": [
    "calculation_day_immediately_following_rebalance_day",
    "calculationday",
    "cessation_possibility_day",
    "cessation_possibility_exchange",
    "close_of_trading_exchange",
    "close_of_trading_rebalance_day",
    "closeoftrading",
    "context_captures_new_index_component_close_of_trading",
    "context_component",
    "context_component_included_at_following_calculation_day",
    "context_component_included_at_rebalance_day",
    "context_day",
    "context_exchange",
    "context_excluded_by_prior_to_close_cessation",
    "context_excluded_by_scheduled_shortened_period",
    "context_rebalance_day",
    "context_satisfies_market_disruption_counterfactual",
    "context_satisfies_open_for_trading_condition",
    "determination_decides_whether_context_is_trading_day",
    "early_cessation_exclusion",
    "exchange_open_for_trading",
    "exchangeclosingtime",
    "following_calculation_day_component_scope",
    "inclusion_component",
    "inclusion_day",
    "inclusion_index",
    "index_administrator_responsibility_for_trading_day_determination",
    "indexadministrator",
    "indexadministratorforthisindex",
    "indexcomponent",
    "indexcomponentinclusion",
    "market_disruption_counterfactual_condition",
    "market_disruption_occurred",
    "new_index_components_close_of_trading_clarification",
    "open_for_trading_condition",
    "organization",
    "prior_to",
    "rebalance_day_component_scope",
    "relevant_exchange",
    "required",
    "scheduled_exchange_closing_time",
    "scheduled_shortened_period_exclusion",
    "scheduledshortenedperiod",
    "security",
    "security_to_be_included_in_index_as_new_index_component",
    "shortened_period_day",
    "shortened_period_exchange",
    "theindex",
    "theindexadministrator",
    "trading_day"
  ],
  "new_full_surface_content_tokens_vs_text_only": [
    "a4v3",
    "calculation_day_immediately_following_rebalance_day",
    "calculationday",
    "canonical",
    "cessation_possibility_day",
    "cessation_possibility_exchange",
    "close_of_trading_exchange",
    "close_of_trading_rebalance_day",
    "closeoftrading",
    "computation",
    "context_captures_new_index_component_close_of_trading",
    "context_component",
    "context_component_included_at_following_calculation_day",
    "context_component_included_at_rebalance_day",
    "context_day",
    "context_exchange",
    "context_excluded_by_prior_to_close_cessation",
    "context_excluded_by_scheduled_shortened_period",
    "context_rebalance_day",
    "context_satisfies_market_disruption_counterfactual",
    "context_satisfies_open_for_trading_condition",
    "current",
    "determination_decides_whether_context_is_trading_day",
    "deterministic",
    "draft",
    "early_cessation_exclusion",
    "exchange_open_for_trading",
    "exchangeclosingtime",
    "financialinstrument",
    "following_calculation_day_component_scope",
    "inclusion_component",
    "inclusion_day",
    "inclusion_index",
    "index_administrator_responsibility_for_trading_day_determination",
    "indexadministrator",
    "indexadministratorforthisindex",
    "indexcomponent",
    "indexcomponentinclusion",
    "main_ir",
    "manual",
    "market_disruption_counterfactual_condition",
    "market_disruption_occurred",
    "metric",
    "new_index_components_close_of_trading_clarification",
    "open_for_trading_condition",
    "organization",
    "parsed",
    "primitive_usage",
    "prior_to",
    "rebalance_day_component_scope"
  ],
  "new_full_surface_content_tokens_vs_text_prelude_only": [
    "calculation_day_immediately_following_rebalance_day",
    "calculationday",
    "canonical",
    "cessation_possibility_day",
    "cessation_possibility_exchange",
    "close_of_trading_exchange",
    "close_of_trading_rebalance_day",
    "closeoftrading",
    "computation",
    "context_captures_new_index_component_close_of_trading",
    "context_component",
    "context_component_included_at_following_calculation_day",
    "context_component_included_at_rebalance_day",
    "context_day",
    "context_exchange",
    "context_excluded_by_prior_to_close_cessation",
    "context_excluded_by_scheduled_shortened_period",
    "context_rebalance_day",
    "context_satisfies_market_disruption_counterfactual",
    "context_satisfies_open_for_trading_condition",
    "current",
    "determination_decides_whether_context_is_trading_day",
    "deterministic",
    "draft",
    "early_cessation_exclusion",
    "exchange_open_for_trading",
    "exchangeclosingtime",
    "following_calculation_day_component_scope",
    "inclusion_component",
    "inclusion_day",
    "inclusion_index",
    "index_administrator_responsibility_for_trading_day_determination",
    "indexadministrator",
    "indexadministratorforthisindex",
    "indexcomponent",
    "indexcomponentinclusion",
    "main_ir",
    "manual",
    "market_disruption_counterfactual_condition",
    "market_disruption_occurred",
    "metric",
    "new_index_components_close_of_trading_clarification",
    "open_for_trading_condition",
    "organization",
    "parsed",
    "primitive_usage",
    "prior_to",
    "rebalance_day_component_scope",
    "recomputation",
    "reconstructed"
  ],
  "new_full_surface_content_tokens_vs_text_prelude_advisory": [
    "calculation_day_immediately_following_rebalance_day",
    "calculationday",
    "canonical",
    "cessation_possibility_day",
    "cessation_possibility_exchange",
    "close_of_trading_exchange",
    "close_of_trading_rebalance_day",
    "closeoftrading",
    "computation",
    "context_captures_new_index_component_close_of_trading",
    "context_component",
    "context_component_included_at_following_calculation_day",
    "context_component_included_at_rebalance_day",
    "context_day",
    "context_exchange",
    "context_excluded_by_prior_to_close_cessation",
    "context_excluded_by_scheduled_shortened_period",
    "context_rebalance_day",
    "context_satisfies_market_disruption_counterfactual",
    "context_satisfies_open_for_trading_condition",
    "current",
    "determination_decides_whether_context_is_trading_day",
    "deterministic",
    "draft",
    "early_cessation_exclusion",
    "exchange_open_for_trading",
    "exchangeclosingtime",
    "following_calculation_day_component_scope",
    "inclusion_component",
    "inclusion_day",
    "inclusion_index",
    "index_administrator_responsibility_for_trading_day_determination",
    "indexadministrator",
    "indexadministratorforthisindex",
    "indexcomponent",
    "indexcomponentinclusion",
    "main_ir",
    "manual",
    "market_disruption_counterfactual_condition",
    "market_disruption_occurred",
    "metric",
    "new_index_components_close_of_trading_clarification",
    "open_for_trading_condition",
    "organization",
    "parsed",
    "primitive_usage",
    "prior_to",
    "rebalance_day_component_scope",
    "recomputation",
    "reconstructed"
  ]
}
```

## coverage

```json
{
  "normalized_clause_count": 1,
  "formula_bearing_item_count": 10,
  "formula_to_clause_compression_ratio": 0.1,
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
  "source_content_token_count": 33,
  "source_content_token_mass": 64,
  "formula_content_token_count": 65,
  "formula_content_token_mass": 422,
  "full_surface_content_token_count": 88,
  "full_surface_content_token_mass": 449,
  "formula_content_token_recall": 0.7878787878787878,
  "full_surface_content_token_recall": 0.7878787878787878,
  "full_surface_content_token_jaccard": 0.2736842105263158,
  "formula_content_token_multiset_recall": 0.8125,
  "formula_content_token_multiset_precision": 0.12322274881516587,
  "formula_repeat_overuse_token_count": 62,
  "formula_repeat_overuse_mass": 370,
  "formula_repeat_underuse_token_count": 10,
  "formula_repeat_underuse_mass": 12,
  "formula_repeat_overuse_examples": [
    {
      "token": "context",
      "current_count": 49,
      "baseline_count": 0,
      "delta": 49
    },
    {
      "token": "exchange",
      "current_count": 33,
      "baseline_count": 4,
      "delta": 29
    },
    {
      "token": "tradingdaycontext",
      "current_count": 25,
      "baseline_count": 0,
      "delta": 25
    },
    {
      "token": "trading",
      "current_count": 28,
      "baseline_count": 6,
      "delta": 22
    },
    {
      "token": "component",
      "current_count": 20,
      "baseline_count": 2,
      "delta": 18
    },
    {
      "token": "close",
      "current_count": 13,
      "baseline_count": 1,
      "delta": 12
    },
    {
      "token": "rebalance",
      "current_count": 13,
      "baseline_count": 3,
      "delta": 10
    },
    {
      "token": "inclusion",
      "current_count": 9,
      "baseline_count": 0,
      "delta": 9
    },
    {
      "token": "index",
      "current_count": 15,
      "baseline_count": 7,
      "delta": 8
    },
    {
      "token": "period",
      "current_count": 9,
      "baseline_count": 1,
      "delta": 8
    },
    {
      "token": "cessation",
      "current_count": 8,
      "baseline_count": 0,
      "delta": 8
    },
    {
      "token": "indexcomponent",
      "current_count": 8,
      "baseline_count": 0,
      "delta": 8
    },
    {
      "token": "rebalanceday",
      "current_count": 8,
      "baseline_count": 0,
      "delta": 8
    },
    {
      "token": "disruption",
      "current_count": 8,
      "baseline_count": 1,
      "delta": 7
    },
    {
      "token": "market",
      "current_count": 8,
      "baseline_count": 1,
      "delta": 7
    },
    {
      "token": "shortened",
      "current_count": 8,
      "baseline_count": 1,
      "delta": 7
    },
    {
      "token": "open",
      "current_count": 8,
      "baseline_count": 2,
      "delta": 6
    },
    {
      "token": "excluded",
      "current_count": 6,
      "baseline_count": 0,
      "delta": 6
    },
    {
      "token": "indexcomponentinclusion",
      "current_count": 6,
      "baseline_count": 0,
      "delta": 6
    },
    {
      "token": "satisfies",
      "current_count": 6,
      "baseline_count": 0,
      "delta": 6
    }
  ],
  "full_surface_content_token_multiset_recall": 0.8125,
  "full_surface_content_token_multiset_precision": 0.11581291759465479,
  "full_surface_repeat_overuse_token_count": 85,
  "full_surface_repeat_overuse_mass": 397,
  "full_surface_repeat_underuse_token_count": 10,
  "full_surface_repeat_underuse_mass": 12,
  "full_surface_repeat_overuse_examples": [
    {
      "token": "context",
      "current_count": 49,
      "baseline_count": 0,
      "delta": 49
    },
    {
      "token": "exchange",
      "current_count": 33,
      "baseline_count": 4,
      "delta": 29
    },
    {
      "token": "tradingdaycontext",
      "current_count": 25,
      "baseline_count": 0,
      "delta": 25
    },
    {
      "token": "trading",
      "current_count": 28,
      "baseline_count": 6,
      "delta": 22
    },
    {
      "token": "component",
      "current_count": 20,
      "baseline_count": 2,
      "delta": 18
    },
    {
      "token": "close",
      "current_count": 13,
      "baseline_count": 1,
      "delta": 12
    },
    {
      "token": "rebalance",
      "current_count": 13,
      "baseline_count": 3,
      "delta": 10
    },
    {
      "token": "inclusion",
      "current_count": 9,
      "baseline_count": 0,
      "delta": 9
    },
    {
      "token": "index",
      "current_count": 15,
      "baseline_count": 7,
      "delta": 8
    },
    {
      "token": "period",
      "current_count": 9,
      "baseline_count": 1,
      "delta": 8
    },
    {
      "token": "cessation",
      "current_count": 8,
      "baseline_count": 0,
      "delta": 8
    },
    {
      "token": "indexcomponent",
      "current_count": 8,
      "baseline_count": 0,
      "delta": 8
    },
    {
      "token": "rebalanceday",
      "current_count": 8,
      "baseline_count": 0,
      "delta": 8
    },
    {
      "token": "disruption",
      "current_count": 8,
      "baseline_count": 1,
      "delta": 7
    },
    {
      "token": "market",
      "current_count": 8,
      "baseline_count": 1,
      "delta": 7
    },
    {
      "token": "shortened",
      "current_count": 8,
      "baseline_count": 1,
      "delta": 7
    },
    {
      "token": "open",
      "current_count": 8,
      "baseline_count": 2,
      "delta": 6
    },
    {
      "token": "excluded",
      "current_count": 6,
      "baseline_count": 0,
      "delta": 6
    },
    {
      "token": "indexcomponentinclusion",
      "current_count": 6,
      "baseline_count": 0,
      "delta": 6
    },
    {
      "token": "satisfies",
      "current_count": 6,
      "baseline_count": 0,
      "delta": 6
    }
  ],
  "source_to_formula_token_gap_count": 7,
  "source_to_full_surface_token_gap_count": 7,
  "source_content_tokens_missing_from_formula": [
    "capture",
    "ceased",
    "certain",
    "excluding",
    "intended",
    "provision",
    "securities"
  ],
  "source_content_tokens_missing_from_full_surface": [
    "capture",
    "ceased",
    "certain",
    "excluding",
    "intended",
    "provision",
    "securities"
  ]
}
```

## source_vs_normalized

```json
{
  "source_excerpt_content_token_count": 33,
  "source_excerpt_content_token_mass": 64,
  "normalized_content_token_count": 33,
  "normalized_content_token_mass": 64,
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
  "normalized_content_mass_per_clause": 64.0,
  "source_normalized_bertscore_precision": 1.0,
  "source_normalized_bertscore_recall": 1.0,
  "source_normalized_bertscore_f1": 1.0,
  "normalized_implies_source_entailment": 0.9485527873039246,
  "source_implies_normalized_entailment": 0.9485527873039246,
  "source_vs_normalized_contradiction_score": 0.029369482770562172
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
  "notes_to_formula_content_ratio": 0.35384615384615387
}
```

## identifier_glue

```json
{
  "identifier_count": 71,
  "compound_identifier_count_raw": 26,
  "compound_identifier_count_content": 40,
  "compound_identifier_rate_raw": 0.36619718309859156,
  "compound_identifier_rate_content": 0.5633802816901409,
  "max_identifier_piece_count_raw": 10,
  "max_identifier_piece_count_content": 8,
  "mean_identifier_piece_count_raw": 3.3661971830985915,
  "mean_identifier_piece_count_content": 2.8732394366197185,
  "identifier_glue_excess_mass_raw": 70,
  "identifier_glue_excess_mass_content": 86,
  "identifier_glue_excess_rate_raw": 0.9859154929577465,
  "identifier_glue_excess_rate_content": 1.2112676056338028,
  "source_grounded_content_piece_ratio_mean": 0.7475016767270288,
  "advisory_grounded_content_piece_ratio_mean": 0.7475016767270288,
  "low_source_grounded_glued_identifier_count": 19,
  "low_source_grounded_glued_identifier_rate": 0.2676056338028169,
  "entity_relation_target_fusion_count": 11,
  "entity_relation_target_fusion_rate": 0.15492957746478872,
  "conditional_relation_name_packing_count": 5,
  "conditional_relation_name_packing_rate": 0.07042253521126761,
  "top_glued_identifiers": [
    {
      "identifier": "would_have_been_open_for_trading_without_market_disruption",
      "raw_piece_count": 9,
      "content_piece_count": 8,
      "raw_pieces": [
        "would",
        "have",
        "been",
        "open",
        "for",
        "trading",
        "without",
        "market",
        "disruption"
      ],
      "content_pieces": [
        "would",
        "have",
        "been",
        "open",
        "trading",
        "without",
        "market",
        "disruption"
      ],
      "glue_excess_raw": 6,
      "glue_excess_content": 6,
      "source_grounded_content_piece_count": 7,
      "advisory_grounded_content_piece_count": 7,
      "source_grounded_content_piece_ratio": 0.875,
      "advisory_grounded_content_piece_ratio": 0.875
    },
    {
      "identifier": "context_captures_new_index_component_close_of_trading",
      "raw_piece_count": 8,
      "content_piece_count": 7,
      "raw_pieces": [
        "context",
        "captures",
        "new",
        "index",
        "component",
        "close",
        "of",
        "trading"
      ],
      "content_pieces": [
        "context",
        "captures",
        "new",
        "index",
        "component",
        "close",
        "trading"
      ],
      "glue_excess_raw": 5,
      "glue_excess_content": 5,
      "source_grounded_content_piece_count": 5,
      "advisory_grounded_content_piece_count": 5,
      "source_grounded_content_piece_ratio": 0.7142857142857143,
      "advisory_grounded_content_piece_ratio": 0.7142857142857143
    },
    {
      "identifier": "security_to_be_included_in_index_as_new_index_component",
      "raw_piece_count": 10,
      "content_piece_count": 6,
      "raw_pieces": [
        "security",
        "to",
        "be",
        "included",
        "in",
        "index",
        "as",
        "new",
        "index",
        "component"
      ],
      "content_pieces": [
        "security",
        "included",
        "index",
        "new",
        "index",
        "component"
      ],
      "glue_excess_raw": 7,
      "glue_excess_content": 4,
      "source_grounded_content_piece_count": 5,
      "advisory_grounded_content_piece_count": 5,
      "source_grounded_content_piece_ratio": 0.8333333333333334,
      "advisory_grounded_content_piece_ratio": 0.8333333333333334
    },
    {
      "identifier": "determination_decides_whether_context_is_trading_day",
      "raw_piece_count": 7,
      "content_piece_count": 6,
      "raw_pieces": [
        "determination",
        "decides",
        "whether",
        "context",
        "is",
        "trading",
        "day"
      ],
      "content_pieces": [
        "determination",
        "decides",
        "whether",
        "context",
        "trading",
        "day"
      ],
      "glue_excess_raw": 4,
      "glue_excess_content": 4,
      "source_grounded_content_piece_count": 3,
      "advisory_grounded_content_piece_count": 3,
      "source_grounded_content_piece_ratio": 0.5,
      "advisory_grounded_content_piece_ratio": 0.5
    },
    {
      "identifier": "index_administrator_responsibility_for_trading_day_determination",
      "raw_piece_count": 7,
      "content_piece_count": 6,
      "raw_pieces": [
        "index",
        "administrator",
        "responsibility",
        "for",
        "trading",
        "day",
        "determination"
      ],
      "content_pieces": [
        "index",
        "administrator",
        "responsibility",
        "trading",
        "day",
        "determination"
      ],
      "glue_excess_raw": 4,
      "glue_excess_content": 4,
      "source_grounded_content_piece_count": 4,
      "advisory_grounded_content_piece_count": 4,
      "source_grounded_content_piece_ratio": 0.6666666666666666,
      "advisory_grounded_content_piece_ratio": 0.6666666666666666
    },
    {
      "identifier": "context_component_included_at_following_calculation_day",
      "raw_piece_count": 7,
      "content_piece_count": 6,
      "raw_pieces": [
        "context",
        "component",
        "included",
        "at",
        "following",
        "calculation",
        "day"
      ],
      "content_pieces": [
        "context",
        "component",
        "included",
        "following",
        "calculation",
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
      "identifier": "new_index_components_close_of_trading_clarification",
      "raw_piece_count": 7,
      "content_piece_count": 6,
      "raw_pieces": [
        "new",
        "index",
        "components",
        "close",
        "of",
        "trading",
        "clarification"
      ],
      "content_pieces": [
        "new",
        "index",
        "components",
        "close",
        "trading",
        "clarification"
      ],
      "glue_excess_raw": 4,
      "glue_excess_content": 4,
      "source_grounded_content_piece_count": 6,
      "advisory_grounded_content_piece_count": 6,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    },
    {
      "identifier": "calculation_day_immediately_following_rebalance_day",
      "raw_piece_count": 6,
      "content_piece_count": 6,
      "raw_pieces": [
        "calculation",
        "day",
        "immediately",
        "following",
        "rebalance",
        "day"
      ],
      "content_pieces": [
        "calculation",
        "day",
        "immediately",
        "following",
        "rebalance",
        "day"
      ],
      "glue_excess_raw": 3,
      "glue_excess_content": 4,
      "source_grounded_content_piece_count": 6,
      "advisory_grounded_content_piece_count": 6,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    },
    {
      "identifier": "context_excluded_by_prior_to_close_cessation",
      "raw_piece_count": 7,
      "content_piece_count": 5,
      "raw_pieces": [
        "context",
        "excluded",
        "by",
        "prior",
        "to",
        "close",
        "cessation"
      ],
      "content_pieces": [
        "context",
        "excluded",
        "prior",
        "close",
        "cessation"
      ],
      "glue_excess_raw": 4,
      "glue_excess_content": 3,
      "source_grounded_content_piece_count": 2,
      "advisory_grounded_content_piece_count": 2,
      "source_grounded_content_piece_ratio": 0.4,
      "advisory_grounded_content_piece_ratio": 0.4
    },
    {
      "identifier": "context_satisfies_open_for_trading_condition",
      "raw_piece_count": 6,
      "content_piece_count": 5,
      "raw_pieces": [
        "context",
        "satisfies",
        "open",
        "for",
        "trading",
        "condition"
      ],
      "content_pieces": [
        "context",
        "satisfies",
        "open",
        "trading",
        "condition"
      ],
      "glue_excess_raw": 3,
      "glue_excess_content": 3,
      "source_grounded_content_piece_count": 2,
      "advisory_grounded_content_piece_count": 2,
      "source_grounded_content_piece_ratio": 0.4,
      "advisory_grounded_content_piece_ratio": 0.4
    },
    {
      "identifier": "context_excluded_by_scheduled_shortened_period",
      "raw_piece_count": 6,
      "content_piece_count": 5,
      "raw_pieces": [
        "context",
        "excluded",
        "by",
        "scheduled",
        "shortened",
        "period"
      ],
      "content_pieces": [
        "context",
        "excluded",
        "scheduled",
        "shortened",
        "period"
      ],
      "glue_excess_raw": 3,
      "glue_excess_content": 3,
      "source_grounded_content_piece_count": 3,
      "advisory_grounded_content_piece_count": 3,
      "source_grounded_content_piece_ratio": 0.6,
      "advisory_grounded_content_piece_ratio": 0.6
    },
    {
      "identifier": "context_component_included_at_rebalance_day",
      "raw_piece_count": 6,
      "content_piece_count": 5,
      "raw_pieces": [
        "context",
        "component",
        "included",
        "at",
        "rebalance",
        "day"
      ],
      "content_pieces": [
        "context",
        "component",
        "included",
        "rebalance",
        "day"
      ],
      "glue_excess_raw": 3,
      "glue_excess_content": 3,
      "source_grounded_content_piece_count": 4,
      "advisory_grounded_content_piece_count": 4,
      "source_grounded_content_piece_ratio": 0.8,
      "advisory_grounded_content_piece_ratio": 0.8
    },
    {
      "identifier": "ultimately_responsible_for_trading_day_determination",
      "raw_piece_count": 6,
      "content_piece_count": 5,
      "raw_pieces": [
        "ultimately",
        "responsible",
        "for",
        "trading",
        "day",
        "determination"
      ],
      "content_pieces": [
        "ultimately",
        "responsible",
        "trading",
        "day",
        "determination"
      ],
      "glue_excess_raw": 3,
      "glue_excess_content": 3,
      "source_grounded_content_piece_count": 4,
      "advisory_grounded_content_piece_count": 4,
      "source_grounded_content_piece_ratio": 0.8,
      "advisory_grounded_content_piece_ratio": 0.8
    },
    {
      "identifier": "context_satisfies_market_disruption_counterfactual",
      "raw_piece_count": 5,
      "content_piece_count": 5,
      "raw_pieces": [
        "context",
        "satisfies",
        "market",
        "disruption",
        "counterfactual"
      ],
      "content_pieces": [
        "context",
        "satisfies",
        "market",
        "disruption",
        "counterfactual"
      ],
      "glue_excess_raw": 2,
      "glue_excess_content": 3,
      "source_grounded_content_piece_count": 2,
      "advisory_grounded_content_piece_count": 2,
      "source_grounded_content_piece_ratio": 0.4,
      "advisory_grounded_content_piece_ratio": 0.4
    },
    {
      "identifier": "close_of_trading_rebalance_day",
      "raw_piece_count": 5,
      "content_piece_count": 4,
      "raw_pieces": [
        "close",
        "of",
        "trading",
        "rebalance",
        "day"
      ],
      "content_pieces": [
        "close",
        "trading",
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
      "identifier": "following_calculation_day_component_scope",
      "raw_piece_count": 5,
      "content_piece_count": 4,
      "raw_pieces": [
        "following",
        "calculation",
        "day",
        "component",
        "scope"
      ],
      "content_pieces": [
        "following",
        "calculation",
        "day",
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
      "identifier": "market_disruption_counterfactual_condition",
      "raw_piece_count": 4,
      "content_piece_count": 4,
      "raw_pieces": [
        "market",
        "disruption",
        "counterfactual",
        "condition"
      ],
      "content_pieces": [
        "market",
        "disruption",
        "counterfactual",
        "condition"
      ],
      "glue_excess_raw": 1,
      "glue_excess_content": 2,
      "source_grounded_content_piece_count": 2,
      "advisory_grounded_content_piece_count": 2,
      "source_grounded_content_piece_ratio": 0.5,
      "advisory_grounded_content_piece_ratio": 0.5
    },
    {
      "identifier": "trading_day_context_definition",
      "raw_piece_count": 4,
      "content_piece_count": 4,
      "raw_pieces": [
        "trading",
        "day",
        "context",
        "definition"
      ],
      "content_pieces": [
        "trading",
        "day",
        "context",
        "definition"
      ],
      "glue_excess_raw": 1,
      "glue_excess_content": 2,
      "source_grounded_content_piece_count": 2,
      "advisory_grounded_content_piece_count": 2,
      "source_grounded_content_piece_ratio": 0.5,
      "advisory_grounded_content_piece_ratio": 0.5
    },
    {
      "identifier": "valid_trading_day_context",
      "raw_piece_count": 4,
      "content_piece_count": 4,
      "raw_pieces": [
        "valid",
        "trading",
        "day",
        "context"
      ],
      "content_pieces": [
        "valid",
        "trading",
        "day",
        "context"
      ],
      "glue_excess_raw": 1,
      "glue_excess_content": 2,
      "source_grounded_content_piece_count": 2,
      "advisory_grounded_content_piece_count": 2,
      "source_grounded_content_piece_ratio": 0.5,
      "advisory_grounded_content_piece_ratio": 0.5
    },
    {
      "identifier": "scheduled_shortened_period_exclusion",
      "raw_piece_count": 4,
      "content_piece_count": 4,
      "raw_pieces": [
        "scheduled",
        "shortened",
        "period",
        "exclusion"
      ],
      "content_pieces": [
        "scheduled",
        "shortened",
        "period",
        "exclusion"
      ],
      "glue_excess_raw": 1,
      "glue_excess_content": 2,
      "source_grounded_content_piece_count": 3,
      "advisory_grounded_content_piece_count": 3,
      "source_grounded_content_piece_ratio": 0.75,
      "advisory_grounded_content_piece_ratio": 0.75
    }
  ],
  "lowest_source_grounded_identifiers": [
    {
      "identifier": "early_cessation_exclusion",
      "raw_piece_count": 3,
      "content_piece_count": 3,
      "raw_pieces": [
        "early",
        "cessation",
        "exclusion"
      ],
      "content_pieces": [
        "early",
        "cessation",
        "exclusion"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 1,
      "source_grounded_content_piece_count": 0,
      "advisory_grounded_content_piece_count": 0,
      "source_grounded_content_piece_ratio": 0.0,
      "advisory_grounded_content_piece_ratio": 0.0
    },
    {
      "identifier": "cessation_possibility_day",
      "raw_piece_count": 3,
      "content_piece_count": 3,
      "raw_pieces": [
        "cessation",
        "possibility",
        "day"
      ],
      "content_pieces": [
        "cessation",
        "possibility",
        "day"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 1,
      "source_grounded_content_piece_count": 1,
      "advisory_grounded_content_piece_count": 1,
      "source_grounded_content_piece_ratio": 0.3333333333333333,
      "advisory_grounded_content_piece_ratio": 0.3333333333333333
    },
    {
      "identifier": "cessation_possibility_exchange",
      "raw_piece_count": 3,
      "content_piece_count": 3,
      "raw_pieces": [
        "cessation",
        "possibility",
        "exchange"
      ],
      "content_pieces": [
        "cessation",
        "possibility",
        "exchange"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 1,
      "source_grounded_content_piece_count": 1,
      "advisory_grounded_content_piece_count": 1,
      "source_grounded_content_piece_ratio": 0.3333333333333333,
      "advisory_grounded_content_piece_ratio": 0.3333333333333333
    },
    {
      "identifier": "TradingCessationPossibility",
      "raw_piece_count": 3,
      "content_piece_count": 3,
      "raw_pieces": [
        "trading",
        "cessation",
        "possibility"
      ],
      "content_pieces": [
        "trading",
        "cessation",
        "possibility"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 1,
      "source_grounded_content_piece_count": 1,
      "advisory_grounded_content_piece_count": 1,
      "source_grounded_content_piece_ratio": 0.3333333333333333,
      "advisory_grounded_content_piece_ratio": 0.3333333333333333
    },
    {
      "identifier": "context_excluded_by_prior_to_close_cessation",
      "raw_piece_count": 7,
      "content_piece_count": 5,
      "raw_pieces": [
        "context",
        "excluded",
        "by",
        "prior",
        "to",
        "close",
        "cessation"
      ],
      "content_pieces": [
        "context",
        "excluded",
        "prior",
        "close",
        "cessation"
      ],
      "glue_excess_raw": 4,
      "glue_excess_content": 3,
      "source_grounded_content_piece_count": 2,
      "advisory_grounded_content_piece_count": 2,
      "source_grounded_content_piece_ratio": 0.4,
      "advisory_grounded_content_piece_ratio": 0.4
    },
    {
      "identifier": "context_satisfies_market_disruption_counterfactual",
      "raw_piece_count": 5,
      "content_piece_count": 5,
      "raw_pieces": [
        "context",
        "satisfies",
        "market",
        "disruption",
        "counterfactual"
      ],
      "content_pieces": [
        "context",
        "satisfies",
        "market",
        "disruption",
        "counterfactual"
      ],
      "glue_excess_raw": 2,
      "glue_excess_content": 3,
      "source_grounded_content_piece_count": 2,
      "advisory_grounded_content_piece_count": 2,
      "source_grounded_content_piece_ratio": 0.4,
      "advisory_grounded_content_piece_ratio": 0.4
    },
    {
      "identifier": "context_satisfies_open_for_trading_condition",
      "raw_piece_count": 6,
      "content_piece_count": 5,
      "raw_pieces": [
        "context",
        "satisfies",
        "open",
        "for",
        "trading",
        "condition"
      ],
      "content_pieces": [
        "context",
        "satisfies",
        "open",
        "trading",
        "condition"
      ],
      "glue_excess_raw": 3,
      "glue_excess_content": 3,
      "source_grounded_content_piece_count": 2,
      "advisory_grounded_content_piece_count": 2,
      "source_grounded_content_piece_ratio": 0.4,
      "advisory_grounded_content_piece_ratio": 0.4
    },
    {
      "identifier": "determination_decides_whether_context_is_trading_day",
      "raw_piece_count": 7,
      "content_piece_count": 6,
      "raw_pieces": [
        "determination",
        "decides",
        "whether",
        "context",
        "is",
        "trading",
        "day"
      ],
      "content_pieces": [
        "determination",
        "decides",
        "whether",
        "context",
        "trading",
        "day"
      ],
      "glue_excess_raw": 4,
      "glue_excess_content": 4,
      "source_grounded_content_piece_count": 3,
      "advisory_grounded_content_piece_count": 3,
      "source_grounded_content_piece_ratio": 0.5,
      "advisory_grounded_content_piece_ratio": 0.5
    },
    {
      "identifier": "market_disruption_counterfactual_condition",
      "raw_piece_count": 4,
      "content_piece_count": 4,
      "raw_pieces": [
        "market",
        "disruption",
        "counterfactual",
        "condition"
      ],
      "content_pieces": [
        "market",
        "disruption",
        "counterfactual",
        "condition"
      ],
      "glue_excess_raw": 1,
      "glue_excess_content": 2,
      "source_grounded_content_piece_count": 2,
      "advisory_grounded_content_piece_count": 2,
      "source_grounded_content_piece_ratio": 0.5,
      "advisory_grounded_content_piece_ratio": 0.5
    },
    {
      "identifier": "trading_day_context_definition",
      "raw_piece_count": 4,
      "content_piece_count": 4,
      "raw_pieces": [
        "trading",
        "day",
        "context",
        "definition"
      ],
      "content_pieces": [
        "trading",
        "day",
        "context",
        "definition"
      ],
      "glue_excess_raw": 1,
      "glue_excess_content": 2,
      "source_grounded_content_piece_count": 2,
      "advisory_grounded_content_piece_count": 2,
      "source_grounded_content_piece_ratio": 0.5,
      "advisory_grounded_content_piece_ratio": 0.5
    },
    {
      "identifier": "valid_trading_day_context",
      "raw_piece_count": 4,
      "content_piece_count": 4,
      "raw_pieces": [
        "valid",
        "trading",
        "day",
        "context"
      ],
      "content_pieces": [
        "valid",
        "trading",
        "day",
        "context"
      ],
      "glue_excess_raw": 1,
      "glue_excess_content": 2,
      "source_grounded_content_piece_count": 2,
      "advisory_grounded_content_piece_count": 2,
      "source_grounded_content_piece_ratio": 0.5,
      "advisory_grounded_content_piece_ratio": 0.5
    },
    {
      "identifier": "context_component",
      "raw_piece_count": 2,
      "content_piece_count": 2,
      "raw_pieces": [
        "context",
        "component"
      ],
      "content_pieces": [
        "context",
        "component"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 0,
      "source_grounded_content_piece_count": 1,
      "advisory_grounded_content_piece_count": 1,
      "source_grounded_content_piece_ratio": 0.5,
      "advisory_grounded_content_piece_ratio": 0.5
    },
    {
      "identifier": "context_day",
      "raw_piece_count": 2,
      "content_piece_count": 2,
      "raw_pieces": [
        "context",
        "day"
      ],
      "content_pieces": [
        "context",
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
      "identifier": "context_exchange",
      "raw_piece_count": 2,
      "content_piece_count": 2,
      "raw_pieces": [
        "context",
        "exchange"
      ],
      "content_pieces": [
        "context",
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
      "identifier": "inclusion_component",
      "raw_piece_count": 2,
      "content_piece_count": 2,
      "raw_pieces": [
        "inclusion",
        "component"
      ],
      "content_pieces": [
        "inclusion",
        "component"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 0,
      "source_grounded_content_piece_count": 1,
      "advisory_grounded_content_piece_count": 1,
      "source_grounded_content_piece_ratio": 0.5,
      "advisory_grounded_content_piece_ratio": 0.5
    },
    {
      "identifier": "inclusion_day",
      "raw_piece_count": 2,
      "content_piece_count": 2,
      "raw_pieces": [
        "inclusion",
        "day"
      ],
      "content_pieces": [
        "inclusion",
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
      "identifier": "inclusion_index",
      "raw_piece_count": 2,
      "content_piece_count": 2,
      "raw_pieces": [
        "inclusion",
        "index"
      ],
      "content_pieces": [
        "inclusion",
        "index"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 0,
      "source_grounded_content_piece_count": 1,
      "advisory_grounded_content_piece_count": 1,
      "source_grounded_content_piece_ratio": 0.5,
      "advisory_grounded_content_piece_ratio": 0.5
    },
    {
      "identifier": "context_excluded_by_scheduled_shortened_period",
      "raw_piece_count": 6,
      "content_piece_count": 5,
      "raw_pieces": [
        "context",
        "excluded",
        "by",
        "scheduled",
        "shortened",
        "period"
      ],
      "content_pieces": [
        "context",
        "excluded",
        "scheduled",
        "shortened",
        "period"
      ],
      "glue_excess_raw": 3,
      "glue_excess_content": 3,
      "source_grounded_content_piece_count": 3,
      "advisory_grounded_content_piece_count": 3,
      "source_grounded_content_piece_ratio": 0.6,
      "advisory_grounded_content_piece_ratio": 0.6
    },
    {
      "identifier": "index_administrator_responsibility_for_trading_day_determination",
      "raw_piece_count": 7,
      "content_piece_count": 6,
      "raw_pieces": [
        "index",
        "administrator",
        "responsibility",
        "for",
        "trading",
        "day",
        "determination"
      ],
      "content_pieces": [
        "index",
        "administrator",
        "responsibility",
        "trading",
        "day",
        "determination"
      ],
      "glue_excess_raw": 4,
      "glue_excess_content": 4,
      "source_grounded_content_piece_count": 4,
      "advisory_grounded_content_piece_count": 4,
      "source_grounded_content_piece_ratio": 0.6666666666666666,
      "advisory_grounded_content_piece_ratio": 0.6666666666666666
    },
    {
      "identifier": "context_rebalance_day",
      "raw_piece_count": 3,
      "content_piece_count": 3,
      "raw_pieces": [
        "context",
        "rebalance",
        "day"
      ],
      "content_pieces": [
        "context",
        "rebalance",
        "day"
      ],
      "glue_excess_raw": 0,
      "glue_excess_content": 1,
      "source_grounded_content_piece_count": 2,
      "advisory_grounded_content_piece_count": 2,
      "source_grounded_content_piece_ratio": 0.6666666666666666,
      "advisory_grounded_content_piece_ratio": 0.6666666666666666
    }
  ],
  "entity_relation_target_fusion_examples": [
    {
      "identifier": "calculation_day_immediately_following_rebalance_day",
      "raw_piece_count": 6,
      "content_piece_count": 6,
      "raw_pieces": [
        "calculation",
        "day",
        "immediately",
        "following",
        "rebalance",
        "day"
      ],
      "content_pieces": [
        "calculation",
        "day",
        "immediately",
        "following",
        "rebalance",
        "day"
      ],
      "glue_excess_raw": 3,
      "glue_excess_content": 4,
      "source_grounded_content_piece_count": 6,
      "advisory_grounded_content_piece_count": 6,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    },
    {
      "identifier": "context_component_included_at_rebalance_day",
      "raw_piece_count": 6,
      "content_piece_count": 5,
      "raw_pieces": [
        "context",
        "component",
        "included",
        "at",
        "rebalance",
        "day"
      ],
      "content_pieces": [
        "context",
        "component",
        "included",
        "rebalance",
        "day"
      ],
      "glue_excess_raw": 3,
      "glue_excess_content": 3,
      "source_grounded_content_piece_count": 4,
      "advisory_grounded_content_piece_count": 4,
      "source_grounded_content_piece_ratio": 0.8,
      "advisory_grounded_content_piece_ratio": 0.8
    },
    {
      "identifier": "context_component_included_at_following_calculation_day",
      "raw_piece_count": 7,
      "content_piece_count": 6,
      "raw_pieces": [
        "context",
        "component",
        "included",
        "at",
        "following",
        "calculation",
        "day"
      ],
      "content_pieces": [
        "context",
        "component",
        "included",
        "following",
        "calculation",
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
      "identifier": "context_satisfies_open_for_trading_condition",
      "raw_piece_count": 6,
      "content_piece_count": 5,
      "raw_pieces": [
        "context",
        "satisfies",
        "open",
        "for",
        "trading",
        "condition"
      ],
      "content_pieces": [
        "context",
        "satisfies",
        "open",
        "trading",
        "condition"
      ],
      "glue_excess_raw": 3,
      "glue_excess_content": 3,
      "source_grounded_content_piece_count": 2,
      "advisory_grounded_content_piece_count": 2,
      "source_grounded_content_piece_ratio": 0.4,
      "advisory_grounded_content_piece_ratio": 0.4
    },
    {
      "identifier": "would_have_been_open_for_trading_without_market_disruption",
      "raw_piece_count": 9,
      "content_piece_count": 8,
      "raw_pieces": [
        "would",
        "have",
        "been",
        "open",
        "for",
        "trading",
        "without",
        "market",
        "disruption"
      ],
      "content_pieces": [
        "would",
        "have",
        "been",
        "open",
        "trading",
        "without",
        "market",
        "disruption"
      ],
      "glue_excess_raw": 6,
      "glue_excess_content": 6,
      "source_grounded_content_piece_count": 7,
      "advisory_grounded_content_piece_count": 7,
      "source_grounded_content_piece_ratio": 0.875,
      "advisory_grounded_content_piece_ratio": 0.875
    },
    {
      "identifier": "security_to_be_included_in_index_as_new_index_component",
      "raw_piece_count": 10,
      "content_piece_count": 6,
      "raw_pieces": [
        "security",
        "to",
        "be",
        "included",
        "in",
        "index",
        "as",
        "new",
        "index",
        "component"
      ],
      "content_pieces": [
        "security",
        "included",
        "index",
        "new",
        "index",
        "component"
      ],
      "glue_excess_raw": 7,
      "glue_excess_content": 4,
      "source_grounded_content_piece_count": 5,
      "advisory_grounded_content_piece_count": 5,
      "source_grounded_content_piece_ratio": 0.8333333333333334,
      "advisory_grounded_content_piece_ratio": 0.8333333333333334
    },
    {
      "identifier": "context_captures_new_index_component_close_of_trading",
      "raw_piece_count": 8,
      "content_piece_count": 7,
      "raw_pieces": [
        "context",
        "captures",
        "new",
        "index",
        "component",
        "close",
        "of",
        "trading"
      ],
      "content_pieces": [
        "context",
        "captures",
        "new",
        "index",
        "component",
        "close",
        "trading"
      ],
      "glue_excess_raw": 5,
      "glue_excess_content": 5,
      "source_grounded_content_piece_count": 5,
      "advisory_grounded_content_piece_count": 5,
      "source_grounded_content_piece_ratio": 0.7142857142857143,
      "advisory_grounded_content_piece_ratio": 0.7142857142857143
    },
    {
      "identifier": "determination_decides_whether_context_is_trading_day",
      "raw_piece_count": 7,
      "content_piece_count": 6,
      "raw_pieces": [
        "determination",
        "decides",
        "whether",
        "context",
        "is",
        "trading",
        "day"
      ],
      "content_pieces": [
        "determination",
        "decides",
        "whether",
        "context",
        "trading",
        "day"
      ],
      "glue_excess_raw": 4,
      "glue_excess_content": 4,
      "source_grounded_content_piece_count": 3,
      "advisory_grounded_content_piece_count": 3,
      "source_grounded_content_piece_ratio": 0.5,
      "advisory_grounded_content_piece_ratio": 0.5
    },
    {
      "identifier": "ultimately_responsible_for_trading_day_determination",
      "raw_piece_count": 6,
      "content_piece_count": 5,
      "raw_pieces": [
        "ultimately",
        "responsible",
        "for",
        "trading",
        "day",
        "determination"
      ],
      "content_pieces": [
        "ultimately",
        "responsible",
        "trading",
        "day",
        "determination"
      ],
      "glue_excess_raw": 3,
      "glue_excess_content": 3,
      "source_grounded_content_piece_count": 4,
      "advisory_grounded_content_piece_count": 4,
      "source_grounded_content_piece_ratio": 0.8,
      "advisory_grounded_content_piece_ratio": 0.8
    },
    {
      "identifier": "following_calculation_day_component_scope",
      "raw_piece_count": 5,
      "content_piece_count": 4,
      "raw_pieces": [
        "following",
        "calculation",
        "day",
        "component",
        "scope"
      ],
      "content_pieces": [
        "following",
        "calculation",
        "day",
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
      "identifier": "index_administrator_responsibility_for_trading_day_determination",
      "raw_piece_count": 7,
      "content_piece_count": 6,
      "raw_pieces": [
        "index",
        "administrator",
        "responsibility",
        "for",
        "trading",
        "day",
        "determination"
      ],
      "content_pieces": [
        "index",
        "administrator",
        "responsibility",
        "trading",
        "day",
        "determination"
      ],
      "glue_excess_raw": 4,
      "glue_excess_content": 4,
      "source_grounded_content_piece_count": 4,
      "advisory_grounded_content_piece_count": 4,
      "source_grounded_content_piece_ratio": 0.6666666666666666,
      "advisory_grounded_content_piece_ratio": 0.6666666666666666
    }
  ],
  "conditional_relation_name_packing_examples": [
    {
      "identifier": "calculation_day_immediately_following_rebalance_day",
      "raw_piece_count": 6,
      "content_piece_count": 6,
      "raw_pieces": [
        "calculation",
        "day",
        "immediately",
        "following",
        "rebalance",
        "day"
      ],
      "content_pieces": [
        "calculation",
        "day",
        "immediately",
        "following",
        "rebalance",
        "day"
      ],
      "glue_excess_raw": 3,
      "glue_excess_content": 4,
      "source_grounded_content_piece_count": 6,
      "advisory_grounded_content_piece_count": 6,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    },
    {
      "identifier": "context_component_included_at_following_calculation_day",
      "raw_piece_count": 7,
      "content_piece_count": 6,
      "raw_pieces": [
        "context",
        "component",
        "included",
        "at",
        "following",
        "calculation",
        "day"
      ],
      "content_pieces": [
        "context",
        "component",
        "included",
        "following",
        "calculation",
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
      "identifier": "context_excluded_by_prior_to_close_cessation",
      "raw_piece_count": 7,
      "content_piece_count": 5,
      "raw_pieces": [
        "context",
        "excluded",
        "by",
        "prior",
        "to",
        "close",
        "cessation"
      ],
      "content_pieces": [
        "context",
        "excluded",
        "prior",
        "close",
        "cessation"
      ],
      "glue_excess_raw": 4,
      "glue_excess_content": 3,
      "source_grounded_content_piece_count": 2,
      "advisory_grounded_content_piece_count": 2,
      "source_grounded_content_piece_ratio": 0.4,
      "advisory_grounded_content_piece_ratio": 0.4
    },
    {
      "identifier": "would_have_been_open_for_trading_without_market_disruption",
      "raw_piece_count": 9,
      "content_piece_count": 8,
      "raw_pieces": [
        "would",
        "have",
        "been",
        "open",
        "for",
        "trading",
        "without",
        "market",
        "disruption"
      ],
      "content_pieces": [
        "would",
        "have",
        "been",
        "open",
        "trading",
        "without",
        "market",
        "disruption"
      ],
      "glue_excess_raw": 6,
      "glue_excess_content": 6,
      "source_grounded_content_piece_count": 7,
      "advisory_grounded_content_piece_count": 7,
      "source_grounded_content_piece_ratio": 0.875,
      "advisory_grounded_content_piece_ratio": 0.875
    },
    {
      "identifier": "following_calculation_day_component_scope",
      "raw_piece_count": 5,
      "content_piece_count": 4,
      "raw_pieces": [
        "following",
        "calculation",
        "day",
        "component",
        "scope"
      ],
      "content_pieces": [
        "following",
        "calculation",
        "day",
        "component"
      ],
      "glue_excess_raw": 2,
      "glue_excess_content": 2,
      "source_grounded_content_piece_count": 4,
      "advisory_grounded_content_piece_count": 4,
      "source_grounded_content_piece_ratio": 1.0,
      "advisory_grounded_content_piece_ratio": 1.0
    }
  ]
}
```

## parameterization

```json
{
  "callable_symbol_count": 32,
  "callable_symbol_with_args_count": 32,
  "top_level_parameter_slot_count": 54,
  "quantifier_parameter_slot_count": 34,
  "total_parameter_slot_mass": 88,
  "factorization_count": 32,
  "parameter_slots_per_factor": 1.6875,
  "factorization_index": 0.5925925925925926,
  "focus_symbol_signature": "missing",
  "focus_symbol_arity": null
}
```

## assertion_complexity

```json
{
  "assertion_count": 10,
  "mean_assertion_node_count": 21.1,
  "max_assertion_node_count": 27,
  "total_assertion_node_count": 211,
  "mean_assertion_depth": 7.9,
  "max_assertion_depth": 9,
  "total_ite_count": 0,
  "max_ite_count_per_assertion": 0,
  "total_quantifier_count": 34,
  "total_connective_count": 25,
  "total_branching_point_count": 45,
  "max_branching_point_count_per_assertion": 6,
  "mean_call_count_per_assertion": 5.8,
  "single_assertion_logic_share": 0.12796208530805686,
  "overcompressed_single_assertion_flag": 0,
  "top_complex_assertions": [
    {
      "name": "following_calculation_day_component_scope",
      "assert_kind": "constraint",
      "node_count": 27,
      "depth": 9,
      "ite_count": 0,
      "quantifier_count": 5,
      "connective_count": 2,
      "branching_point_count": 6,
      "max_fanout": 6,
      "call_count": 7
    },
    {
      "name": "trading_day_context_definition",
      "assert_kind": "constraint",
      "node_count": 26,
      "depth": 9,
      "ite_count": 0,
      "quantifier_count": 4,
      "connective_count": 3,
      "branching_point_count": 6,
      "max_fanout": 5,
      "call_count": 8
    },
    {
      "name": "early_cessation_exclusion",
      "assert_kind": "constraint",
      "node_count": 25,
      "depth": 9,
      "ite_count": 0,
      "quantifier_count": 4,
      "connective_count": 2,
      "branching_point_count": 5,
      "max_fanout": 5,
      "call_count": 7
    },
    {
      "name": "new_index_components_close_of_trading_clarification",
      "assert_kind": "constraint",
      "node_count": 24,
      "depth": 9,
      "ite_count": 0,
      "quantifier_count": 4,
      "connective_count": 2,
      "branching_point_count": 5,
      "max_fanout": 5,
      "call_count": 7
    },
    {
      "name": "rebalance_day_component_scope",
      "assert_kind": "constraint",
      "node_count": 23,
      "depth": 8,
      "ite_count": 0,
      "quantifier_count": 4,
      "connective_count": 2,
      "branching_point_count": 5,
      "max_fanout": 5,
      "call_count": 6
    },
    {
      "name": "scheduled_shortened_period_exclusion",
      "assert_kind": "constraint",
      "node_count": 20,
      "depth": 8,
      "ite_count": 0,
      "quantifier_count": 4,
      "connective_count": 2,
      "branching_point_count": 4,
      "max_fanout": 4,
      "call_count": 5
    },
    {
      "name": "trading_day_definition",
      "assert_kind": "constraint",
      "node_count": 19,
      "depth": 7,
      "ite_count": 0,
      "quantifier_count": 1,
      "connective_count": 6,
      "branching_point_count": 5,
      "max_fanout": 3,
      "call_count": 6
    },
    {
      "name": "market_disruption_counterfactual_condition",
      "assert_kind": "constraint",
      "node_count": 19,
      "depth": 7,
      "ite_count": 0,
      "quantifier_count": 3,
      "connective_count": 2,
      "branching_point_count": 4,
      "max_fanout": 4,
      "call_count": 5
    },
    {
      "name": "open_for_trading_condition",
      "assert_kind": "constraint",
      "node_count": 16,
      "depth": 7,
      "ite_count": 0,
      "quantifier_count": 3,
      "connective_count": 2,
      "branching_point_count": 3,
      "max_fanout": 3,
      "call_count": 4
    },
    {
      "name": "index_administrator_responsibility_for_trading_day_determination",
      "assert_kind": "constraint",
      "node_count": 12,
      "depth": 6,
      "ite_count": 0,
      "quantifier_count": 2,
      "connective_count": 2,
      "branching_point_count": 2,
      "max_fanout": 2,
      "call_count": 3
    }
  ],
  "normalized_clause_count": 1,
  "node_count_per_normalized_clause": 211.0,
  "branching_point_count_per_normalized_clause": 45.0
}
```

## normalized_alignment

```json
{
  "normalized_clause_count": 1,
  "logic_block_count": 10,
  "clause_to_logic_block_ratio": 0.1,
  "logic_block_to_clause_ratio": 10.0,
  "clause_underdecomposition_mass": 0,
  "clause_overdecomposition_mass": 9,
  "focus_symbol_arity": null,
  "helper_factorization_count": 32,
  "single_assertion_logic_share": 0.12796208530805686,
  "underdecomposed_logic_flag": 0
}
```

## normalized_relative

```json
{
  "new_formula_content_token_rate_vs_reference_mass": 0.90625,
  "new_full_surface_content_token_rate_vs_reference_mass": 1.203125,
  "formula_repeat_overuse_rate": 5.78125,
  "full_surface_repeat_overuse_rate": 6.203125,
  "parameter_slot_mass_per_clause": 88.0,
  "parameter_slot_mass_per_reference_token": 1.375,
  "factorization_per_clause": 32.0,
  "factorization_per_reference_token": 0.5,
  "notes_content_token_rate_vs_reference_mass": 0.359375
}
```

## tradeoff

```json
{
  "render_bertscore_f1_to_normalized_per_parameter_slot_mass": 0.008299463851885363,
  "render_bertscore_f1_to_source_per_parameter_slot_mass": 0.008299463851885363,
  "render_nli_ir_implies_text_per_parameter_slot_mass": 0.009687552397901361,
  "render_nli_text_implies_ir_per_parameter_slot_mass": 0.005292851477861404,
  "render_bertscore_f1_to_normalized_per_formula_repeat_overuse_mass": 0.0019739265377457078,
  "render_nli_text_implies_ir_per_formula_repeat_overuse_mass": 0.001258840351491361,
  "render_nli_ir_implies_text_per_formula_repeat_overuse_mass": 0.0023040665162576213,
  "render_bertscore_f1_to_normalized_per_full_surface_repeat_overuse_mass": 0.0018396796447504077,
  "render_nli_text_implies_ir_per_full_surface_repeat_overuse_mass": 0.0011732265240599587,
  "pairwise_structure_similarity_mean_per_parameter_slot_mass": null,
  "focus_signature_mode_share_per_parameter_slot_mass": 0.011363636363636364
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
  "parameter_slot_mass_mean": 88.0,
  "parameter_slot_mass_stddev": 0.0,
  "factorization_count_mean": 32.0,
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
  "render_back_text": "constraint trading day context definition states that for every ctx of type trading day context, valid trading day context for ctx if and only if there exists rd of type rebalance day, there exists d of type day, there exists c of type index component, (context rebalance day for ctx and rd, context day for ctx and d, context component for ctx and c, context exchange for ctx and relevant exchange for c, and (context component included at rebalance day for ctx or context component included at following calculation day for ctx)). constraint rebalance day component scope states that for every ctx of type trading day context, context component included at rebalance day for ctx if and only if there exists rd of type rebalance day, there exists c of type index component, there exists inc of type index component inclusion, (context rebalance day for ctx and rd, context component for ctx and c, inclusion component for inc and c, inclusion index for inc and the index, and inclusion day for inc and rd). constraint following calculation day component scope states that for every ctx of type trading day context, context component included at following calculation day for ctx if and only if there exists rd of type rebalance day, there exists cd of type calculation day, there exists c of type index component, there exists inc of type index component inclusion, (context rebalance day for ctx and rd, calculation day immediately following rebalance day for cd and rd, context component for ctx and c, inclusion component for inc and c, inclusion index for inc and the index, and inclusion day for inc and cd). constraint open for trading condition states that for every ctx of type trading day context, context satisfies open for trading condition for ctx if and only if there exists d of type day, there exists ex of type exchange, (context day for ctx and d, context exchange for ctx and ex, and exchange open for trading for ex and d). constraint market disruption counterfactual condition states that for every ctx of type trading day context, context satisfies market disruption counterfactual for ctx if and only if there exists d of type day, there exists ex of type exchange, (context day for ctx and d, context exchange for ctx and ex, market disruption occurred for ex and d, and would have been open for trading without market disruption for ex and d). constraint early cessation exclusion states that for every ctx of type trading day context, context excluded by prior to close cessation for ctx if and only if there exists d of type day, there exists ex of type exchange, there exists cp of type trading cessation possibility, (context day for ctx and d, context exchange for ctx and ex, cessation possibility exchange for cp and ex, cessation possibility day for cp and d, and prior to for cp and scheduled exchange closing time for ex and d). constraint scheduled shortened period exclusion states that for every ctx of type trading day context, context excluded by scheduled shortened period for ctx if and only if there exists d of type day, there exists ex of type exchange, there exists sp of type scheduled shortened period, (context day for ctx and d, context exchange for ctx and ex, shortened period exchange for sp and ex, and shortened period day for sp and d). constraint trading day definition states that for every ctx of type trading day context, if valid trading day context for ctx, then trading day for ctx if and only if ((context satisfies open for trading condition for ctx or context satisfies market disruption counterfactual for ctx), not (context excluded by prior to close cessation for ctx), and not (context excluded by scheduled shortened period for ctx)). constraint new index components close of trading clarification states that for every ctx of type trading day context, context captures new index component close of trading for ctx if and only if there exists rd of type rebalance day, there exists c of type index component, there exists close of type close of trading, (context rebalance day for ctx and rd, context component for ctx and c, security to be included in index as new index component for c and the index, close of trading exchange for close and relevant exchange for c, and close of trading rebalance day for close and rd). constraint index administrator responsibility for trading day determination states that for every det of type trading day determination, for every ctx of type trading day context, if (determination decides whether context is trading day for det and ctx and valid trading day context for ctx), then ultimately responsible for trading day determination for the index administrator and det. index is a type. security is a type. index component is a type. rebalance day is a type. calculation day is a type. exchange is a type. index administrator is a type. index administrator for this index is a type. index component inclusion is a type. trading day context is a type. trading day determination is a type. exchange closing time is a type. trading cessation possibility is a type. scheduled shortened period is a type. close of trading is a type. the index is a distinguished entity. the index administrator is a distinguished entity. relevant exchange maps index component to exchange. scheduled exchange closing time maps exchange and day to exchange closing time. inclusion component holds between index component inclusion and index component. inclusion index holds between index component inclusion and index. inclusion day holds between index component inclusion and day. calculation day immediately following rebalance day holds between calculation day and rebalance day. context rebalance day holds between trading day context and rebalance day. context day holds between trading day context and day. context component holds between trading day context and index component. context exchange holds between trading day context and exchange. valid trading day context holds between trading day context. context component included at rebalance day holds between trading day context. context component included at following calculation day holds between trading day context. context satisfies open for trading condition holds between trading day context. context satisfies market disruption counterfactual holds between trading day context. context excluded by prior to close cessation holds between trading day context. context excluded by scheduled shortened period holds between trading day context. trading day holds between trading day context. exchange open for trading holds between exchange and day. market disruption occurred holds between exchange and day. would have been open for trading without market disruption holds between exchange and day. cessation possibility exchange holds between trading cessation possibility and exchange. cessation possibility day holds between trading cessation possibility and day. prior to holds between trading cessation possibility and exchange closing time. shortened period exchange holds between scheduled shortened period and exchange. shortened period day holds between scheduled shortened period and day. security to be included in index as new index component holds between security and index. close of trading exchange holds between close of trading and exchange. close of trading rebalance day holds between close of trading and rebalance day. context captures new index component close of trading holds between trading day context. determination decides whether context is trading day holds between trading day determination and trading day context. ultimately responsible for trading day determination holds between index administrator for this index and trading day determination.",
  "render_bertscore_precision_to_normalized": 0.7035390734672546,
  "render_bertscore_recall_to_normalized": 0.759291410446167,
  "render_bertscore_f1_to_normalized": 0.7303528189659119,
  "render_bertscore_precision_to_source": 0.7035390734672546,
  "render_bertscore_recall_to_source": 0.759291410446167,
  "render_bertscore_f1_to_source": 0.7303528189659119,
  "render_nli_ir_implies_text": 0.8525046110153198,
  "render_nli_text_implies_ir": 0.4657709300518036,
  "render_nli_ir_implies_source": 0.8525046110153198,
  "render_nli_source_implies_ir": 0.4657709300518036,
  "render_nli_render_to_normalized": {
    "entailment": 0.8525046110153198,
    "neutral": 0.08994428813457489,
    "contradiction": 0.057551030069589615
  },
  "render_nli_normalized_to_render": {
    "entailment": 0.4657709300518036,
    "neutral": 0.4632653295993805,
    "contradiction": 0.07096380740404129
  },
  "render_nli_render_to_source": {
    "entailment": 0.8525046110153198,
    "neutral": 0.08994428813457489,
    "contradiction": 0.057551030069589615
  },
  "render_nli_source_to_render": {
    "entailment": 0.4657709300518036,
    "neutral": 0.4632653295993805,
    "contradiction": 0.07096380740404129
  },
  "render_contradiction_score": 0.07096380740404129
}
```

## silver_reference

```json
{
  "disabled_for_manual_reference": false,
  "silver_reference_found": true,
  "silver_reference_path": "D:\\OneDrive\\Documents\\Study\\MIPT\\VKR\\research_experiments\\2026-02_pipeline\\IR\\outputs\\runs\\silver_baseline\\definitions_full6_multivariant_critic_v1_with_gold.md",
  "silver_reference_ir": "constraint trading_day_requires_exchange_trading_day_or_market_disruption_case : forall s: Security, d: CalendarDate, TradingDay(s, d) implies (TradingDayAtExchange(ExchangeFor(s), d) or WouldBeTradingDayButForMarketDisruption(ExchangeFor(s), d)) constraint trading_day_excludes_early_close : forall s: Security, d: CalendarDate, TradingDay(s, d) implies not TradingCeasedBeforeScheduledClose(ExchangeFor(s), d) constraint trading_day_excludes_scheduled_shortened_period : forall s: Security, d: CalendarDate, TradingDay(s, d) implies not ExchangeOpenForScheduledShortenedPeriod(ExchangeFor(s), d) constraint trading_day_scope_definition : forall s: Security, d: CalendarDate, TradingDay(s, d) implies (exists r: CalendarDate, RebalanceDay(r) and (IndexComponent(s, r) or (exists c: CalendarDate, CalculationDay(c) and ImmediatelyFollowingDate(c, r) and IndexComponent(s, c))))",
  "top_level_cosine": 0.28524895269256473,
  "logic_cosine": 0.6600778505528795,
  "arity_cosine": null,
  "silver_structure_similarity": 0.47266340162272213
}
```
