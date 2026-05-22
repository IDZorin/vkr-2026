# Rules audit v2 — unified_methodology_v1

- Total: **634**
- Working (have implementation, real value): **581**
- Unimplemented (value=None — concept stub in extended): **53**
- Unimplemented (no key in any metric file): **0**

## Working rules — by Where
| where | rules |
|---|---:|
| `ir` | 421 |
| `triangle` | 59 |
| `ir_vs_text` | 55 |
| `text_vs_normalized` | 42 |
| `corpus` | 4 |

## Working rules — by What (measurement type)
| what | rules |
|---|---:|
| `count` | 229 |
| `other` | 157 |
| `ratio` | 79 |
| `statistic` | 47 |
| `similarity` | 27 |
| `boolean_check` | 22 |
| `lint_pattern` | 15 |
| `shape_validation` | 4 |
| `categorical` | 1 |

## Working rules — by Why (role for agent)
| why | rules |
|---|---:|
| `coverage_indicator` | 329 |
| `actionable_fix` | 219 |
| `layer_alignment` | 19 |
| `structural_compliance` | 14 |

## Working rules — by threshold state
| state | rules |
|---|---:|
| `trivial_warning` | 229 |
| `inspect_only` | 217 |
| `auto_judge` | 135 |

## Cross-table (where × what × why) — top 20
| where | what | why | rules |
|---|---|---|---:|
| `ir` | `count` | `coverage_indicator` | 99 |
| `ir` | `other` | `coverage_indicator` | 89 |
| `ir` | `count` | `actionable_fix` | 53 |
| `ir` | `ratio` | `actionable_fix` | 35 |
| `ir` | `other` | `actionable_fix` | 31 |
| `ir` | `ratio` | `coverage_indicator` | 29 |
| `ir_vs_text` | `count` | `actionable_fix` | 26 |
| `ir` | `statistic` | `coverage_indicator` | 17 |
| `triangle` | `other` | `coverage_indicator` | 17 |
| `triangle` | `count` | `coverage_indicator` | 16 |
| `ir` | `similarity` | `actionable_fix` | 12 |
| `ir_vs_text` | `statistic` | `coverage_indicator` | 10 |
| `ir` | `lint_pattern` | `coverage_indicator` | 9 |
| `triangle` | `similarity` | `actionable_fix` | 8 |
| `text_vs_normalized` | `count` | `coverage_indicator` | 8 |
| `ir` | `boolean_check` | `coverage_indicator` | 8 |
| `text_vs_normalized` | `ratio` | `actionable_fix` | 8 |
| `text_vs_normalized` | `statistic` | `coverage_indicator` | 8 |
| `ir_vs_text` | `count` | `coverage_indicator` | 7 |
| `ir` | `statistic` | `actionable_fix` | 6 |

## Working rules — per where, per why

### where = `ir` — 421 rules

#### why = `coverage_indicator` (251 rules)

| name | module | what | thr | actionable | what_it_counts |
|---|---|---|---|---|---|
| `annotation_node_count` | `formula_ir_drafting` | `count` | `trivial_warning` |   | number of explicit non-formula semantic annotation nodes used to preserve clarif |
| `annotation_node_count` | `quality_evaluation` | `count` | `trivial_warning` |   | number of explicit non-formula semantic annotation nodes used to preserve clarif |
| `artifact_signature_entropy` | `merge_canonicalization` | `other` | `inspect_only` |   | how evenly the artifact space is spread across distinct signatures rather than c |
| `artifact_signature_entropy` | `quality_evaluation` | `other` | `inspect_only` |   | how evenly the artifact space is spread across distinct signatures rather than c |
| `assertion_count` | `formula_ir_drafting` | `count` | `trivial_warning` |   | number of top-level assertion blocks in the IR. |
| `assertion_count` | `quality_evaluation` | `count` | `trivial_warning` |   | number of top-level assertion blocks in the IR. |
| `avoid_padding_or_repetition` | `quality_evaluation` | `other` | `inspect_only` |   |  |
| `avoid_padding_or_repetition` | `source_normalization` | `other` | `inspect_only` |   |  |
| `biconditional_present_when_expected` | `formula_ir_drafting` | `boolean_check` | `inspect_only` |   | whether predicate-like definitions are encoded with `iff` or semantically equiva |
| `biconditional_present_when_expected` | `quality_evaluation` | `boolean_check` | `inspect_only` |   | whether predicate-like definitions are encoded with `iff` or semantically equiva |
| `bridge_family` | `merge_canonicalization` | `other` | `inspect_only` |   |  |
| `bridge_supertype` | `merge_canonicalization` | `other` | `inspect_only` |   |  |
| `callable_symbol_count` | `formula_ir_drafting` | `count` | `trivial_warning` |   | number of declared callable local symbols. |
| `callable_symbol_count` | `merge_canonicalization` | `count` | `trivial_warning` |   | number of declared callable local symbols. |
| `callable_symbol_count` | `quality_evaluation` | `count` | `trivial_warning` |   | number of declared callable local symbols. |
| `callable_symbol_with_args_count` | `formula_ir_drafting` | `count` | `trivial_warning` |   | number of callable local symbols that actually take arguments. |
| `callable_symbol_with_args_count` | `merge_canonicalization` | `count` | `trivial_warning` |   | number of callable local symbols that actually take arguments. |
| `callable_symbol_with_args_count` | `quality_evaluation` | `count` | `trivial_warning` |   | number of callable local symbols that actually take arguments. |
| `candidate_reading_count` | `merge_canonicalization` | `count` | `trivial_warning` |   | number of advisory candidate readings proposed. |
| `candidate_reading_count` | `quality_evaluation` | `count` | `trivial_warning` |   | number of advisory candidate readings proposed. |
| `canonical_subterm_reuse_candidates` | `ontology_planning` | `lint_pattern` | `inspect_only` |   |  |
| `canonical_subterm_reuse_candidates` | `quality_evaluation` | `lint_pattern` | `inspect_only` |   |  |
| `canonical_subterm_reuse_gap` | `ontology_planning` | `other` | `inspect_only` |   |  |
| `canonical_subterm_reuse_gap` | `quality_evaluation` | `other` | `inspect_only` |   |  |
| `clause_coverage_ratio` | `formula_ir_drafting` | `ratio` | `inspect_only` |   | fraction of normalized clauses that are represented somewhere in IR or explicit  |
| `clause_coverage_ratio` | `quality_evaluation` | `ratio` | `inspect_only` |   | fraction of normalized clauses that are represented somewhere in IR or explicit  |
| `clause_overdecomposition_mass` | `formula_ir_drafting` | `statistic` | `trivial_warning` |   | how many extra logic blocks were introduced beyond normalized clause count. |
| `clause_overdecomposition_mass` | `quality_evaluation` | `statistic` | `trivial_warning` |   | how many extra logic blocks were introduced beyond normalized clause count. |
| `clause_to_logic_block_ratio` | `formula_ir_drafting` | `ratio` | `inspect_only` |   | how many normalized clauses are being carried, on average, by one logic block. |
| `clause_to_logic_block_ratio` | `quality_evaluation` | `ratio` | `inspect_only` |   | how many normalized clauses are being carried, on average, by one logic block. |
| `clause_underdecomposition_mass` | `formula_ir_drafting` | `statistic` | `trivial_warning` |   | how many normalized clauses have no corresponding top-level logic block if we co |
| `clause_underdecomposition_mass` | `quality_evaluation` | `statistic` | `trivial_warning` |   | how many normalized clauses have no corresponding top-level logic block if we co |
| `codomain_split_value_families` | `merge_canonicalization` | `other` | `inspect_only` |   |  |
| `codomain_split_value_families` | `ontology_planning` | `other` | `inspect_only` |   |  |
| `codomain_split_value_families` | `quality_evaluation` | `other` | `inspect_only` |   |  |
| `conflict_split` | `merge_canonicalization` | `other` | `inspect_only` |   |  |
| `cover_every_normalized_block` | `formula_ir_drafting` | `other` | `inspect_only` |   |  |
| `cover_every_normalized_block` | `quality_evaluation` | `other` | `inspect_only` |   |  |
| `covered_only_in_notes_count` | `formula_ir_drafting` | `count` | `trivial_warning` |   | semantic fragments that appear only in notes or residual prose, not in formula o |
| `covered_only_in_notes_count` | `quality_evaluation` | `count` | `trivial_warning` |   | semantic fragments that appear only in notes or residual prose, not in formula o |
| `critic_confidence` | `merge_canonicalization` | `other` | `inspect_only` |   | confidence reported by the critic for the selected variant. |
| `critic_confidence` | `quality_evaluation` | `other` | `inspect_only` |   | confidence reported by the critic for the selected variant. |
| `cross_reference_dropout_count` | `formula_ir_drafting` | `count` | `trivial_warning` |   | cross-referenced concepts discussed upstream but omitted from final IR. |
| `cross_reference_dropout_count` | `merge_canonicalization` | `count` | `trivial_warning` |   | cross-referenced concepts discussed upstream but omitted from final IR. |
| `cross_reference_dropout_count` | `ontology_planning` | `count` | `trivial_warning` |   | cross-referenced concepts discussed upstream but omitted from final IR. |
| `cross_reference_dropout_count` | `quality_evaluation` | `count` | `trivial_warning` |   | cross-referenced concepts discussed upstream but omitted from final IR. |
| `cross_reference_usage_count` | `formula_ir_drafting` | `count` | `trivial_warning` |   | number of related entries or cross-referenced concepts actually used in final IR |
| `cross_reference_usage_count` | `merge_canonicalization` | `count` | `trivial_warning` |   | number of related entries or cross-referenced concepts actually used in final IR |
| `cross_reference_usage_count` | `ontology_planning` | `count` | `trivial_warning` |   | number of related entries or cross-referenced concepts actually used in final IR |
| `cross_reference_usage_count` | `quality_evaluation` | `count` | `trivial_warning` |   | number of related entries or cross-referenced concepts actually used in final IR |
| _...+201 more_ |

#### why = `actionable_fix` (147 rules)

| name | module | what | thr | actionable | what_it_counts |
|---|---|---|---|---|---|
| `ast_error_count` | `formula_ir_drafting` | `count` | `auto_judge` | ✓ | total number of canonical AST validation errors. |
| `ast_error_count` | `quality_evaluation` | `count` | `auto_judge` | ✓ | total number of canonical AST validation errors. |
| `combined_validation_ok` | `formula_ir_drafting` | `other` | `inspect_only` | ✓ | whether the draft validates when combined with the current section IR or section |
| `combined_validation_ok` | `quality_evaluation` | `other` | `inspect_only` | ✓ | whether the draft validates when combined with the current section IR or section |
| `composite_identifier_crosslink_candidates` | `ontology_planning` | `lint_pattern` | `inspect_only` | ✓ |  |
| `composite_identifier_crosslink_candidates` | `quality_evaluation` | `lint_pattern` | `inspect_only` | ✓ |  |
| `composite_identifier_crosslink_gap` | `ontology_planning` | `other` | `inspect_only` | ✓ |  |
| `composite_identifier_crosslink_gap` | `quality_evaluation` | `other` | `inspect_only` | ✓ |  |
| `compound_identifier_count_content` | `formula_ir_drafting` | `count` | `trivial_warning` | ✓ | identifiers with at least 3 non-stopword content pieces. |
| `compound_identifier_count_content` | `ontology_planning` | `count` | `trivial_warning` | ✓ | identifiers with at least 3 non-stopword content pieces. |
| `compound_identifier_count_content` | `quality_evaluation` | `count` | `trivial_warning` | ✓ | identifiers with at least 3 non-stopword content pieces. |
| `compound_identifier_count_raw` | `formula_ir_drafting` | `count` | `trivial_warning` | ✓ | identifiers whose raw split length is already large. |
| `compound_identifier_count_raw` | `ontology_planning` | `count` | `trivial_warning` | ✓ | identifiers whose raw split length is already large. |
| `compound_identifier_count_raw` | `quality_evaluation` | `count` | `trivial_warning` | ✓ | identifiers whose raw split length is already large. |
| `compound_identifier_rate_content` | `formula_ir_drafting` | `ratio` | `inspect_only` | ✓ | how large the content-level glued-name population is relative to the whole ident |
| `compound_identifier_rate_content` | `ontology_planning` | `ratio` | `inspect_only` | ✓ | how large the content-level glued-name population is relative to the whole ident |
| `compound_identifier_rate_content` | `quality_evaluation` | `ratio` | `inspect_only` | ✓ | how large the content-level glued-name population is relative to the whole ident |
| `compound_identifier_rate_raw` | `formula_ir_drafting` | `ratio` | `inspect_only` | ✓ | how large the raw glued-name population is relative to the whole identifier inve |
| `compound_identifier_rate_raw` | `ontology_planning` | `ratio` | `inspect_only` | ✓ | how large the raw glued-name population is relative to the whole identifier inve |
| `compound_identifier_rate_raw` | `quality_evaluation` | `ratio` | `inspect_only` | ✓ | how large the raw glued-name population is relative to the whole identifier inve |
| `content_token_multiset_precision` | `formula_ir_drafting` | `ratio` | `auto_judge` | ✓ | precision with repeated token occurrences taken seriously. |
| `content_token_multiset_precision` | `quality_evaluation` | `ratio` | `auto_judge` | ✓ | precision with repeated token occurrences taken seriously. |
| `content_token_multiset_precision` | `source_normalization` | `ratio` | `auto_judge` | ✓ | precision with repeated token occurrences taken seriously. |
| `content_token_multiset_recall` | `formula_ir_drafting` | `ratio` | `auto_judge` | ✓ | recall with repeated token occurrences taken seriously. |
| `content_token_multiset_recall` | `quality_evaluation` | `ratio` | `auto_judge` | ✓ | recall with repeated token occurrences taken seriously. |
| `content_token_multiset_recall` | `source_normalization` | `ratio` | `auto_judge` | ✓ | recall with repeated token occurrences taken seriously. |
| `content_token_precision` | `formula_ir_drafting` | `ratio` | `auto_judge` | ✓ | how much of the IR content-token inventory is source-licensed. |
| `content_token_precision` | `quality_evaluation` | `ratio` | `auto_judge` | ✓ | how much of the IR content-token inventory is source-licensed. |
| `content_token_precision` | `source_normalization` | `ratio` | `auto_judge` | ✓ | how much of the IR content-token inventory is source-licensed. |
| `content_token_recall` | `formula_ir_drafting` | `ratio` | `auto_judge` | ✓ | how much of the source content-token inventory appears in IR. |
| `content_token_recall` | `quality_evaluation` | `ratio` | `auto_judge` | ✓ | how much of the source content-token inventory appears in IR. |
| `content_token_recall` | `source_normalization` | `ratio` | `auto_judge` | ✓ | how much of the source content-token inventory appears in IR. |
| `critic_merge_recommended` | `merge_canonicalization` | `other` | `inspect_only` | ✓ | whether the critic thinks no single variant is fully adequate. |
| `critic_merge_recommended` | `quality_evaluation` | `other` | `inspect_only` | ✓ | whether the critic thinks no single variant is fully adequate. |
| `draft_variant_count` | `merge_canonicalization` | `count` | `trivial_warning` | ✓ | number of concrete IR variants drafted. |
| `draft_variant_count` | `quality_evaluation` | `count` | `trivial_warning` | ✓ | number of concrete IR variants drafted. |
| `exact_merge_overlay` | `merge_canonicalization` | `other` | `inspect_only` | ✓ |  |
| `helper_explosion_count` | `formula_ir_drafting` | `count` | `trivial_warning` | ✓ | excessive proliferation of helper symbols relative to source complexity. |
| `helper_explosion_count` | `quality_evaluation` | `count` | `trivial_warning` | ✓ | excessive proliferation of helper symbols relative to source complexity. |
| `identifier_count` | `formula_ir_drafting` | `count` | `trivial_warning` | ✓ | number of unique IR identifiers inspected by the glue analysis. |
| `identifier_count` | `ontology_planning` | `count` | `trivial_warning` | ✓ | number of unique IR identifiers inspected by the glue analysis. |
| `identifier_count` | `quality_evaluation` | `count` | `trivial_warning` | ✓ | number of unique IR identifiers inspected by the glue analysis. |
| `identifier_glue_excess_mass_content` | `formula_ir_drafting` | `statistic` | `trivial_warning` | ✓ | total content-level over-glue mass. |
| `identifier_glue_excess_mass_content` | `ontology_planning` | `statistic` | `trivial_warning` | ✓ | total content-level over-glue mass. |
| `identifier_glue_excess_mass_content` | `quality_evaluation` | `statistic` | `trivial_warning` | ✓ | total content-level over-glue mass. |
| `identifier_glue_excess_mass_raw` | `formula_ir_drafting` | `statistic` | `trivial_warning` | ✓ | total raw over-glue mass. |
| `identifier_glue_excess_mass_raw` | `ontology_planning` | `statistic` | `trivial_warning` | ✓ | total raw over-glue mass. |
| `identifier_glue_excess_mass_raw` | `quality_evaluation` | `statistic` | `trivial_warning` | ✓ | total raw over-glue mass. |
| `identifier_glue_excess_rate_content` | `formula_ir_drafting` | `ratio` | `inspect_only` | ✓ | average content-level over-glue burden per identifier. |
| `identifier_glue_excess_rate_content` | `ontology_planning` | `ratio` | `inspect_only` | ✓ | average content-level over-glue burden per identifier. |
| _...+97 more_ |

#### why = `structural_compliance` (14 rules)

| name | module | what | thr | actionable | what_it_counts |
|---|---|---|---|---|---|
| `assertion_shape_error_count` | `formula_ir_drafting` | `count` | `auto_judge` | ✓ | AST errors specifically attached to assertion nodes. |
| `assertion_shape_error_count` | `quality_evaluation` | `count` | `auto_judge` | ✓ | AST errors specifically attached to assertion nodes. |
| `ast_valid` | `formula_ir_drafting` | `shape_validation` | `inspect_only` | ✓ | whether the emitted payload satisfies the canonical AST contract. |
| `ast_valid` | `quality_evaluation` | `shape_validation` | `inspect_only` | ✓ | whether the emitted payload satisfies the canonical AST contract. |
| `declaration_shape_error_count` | `formula_ir_drafting` | `count` | `auto_judge` | ✓ | AST errors specifically attached to declaration nodes. |
| `declaration_shape_error_count` | `quality_evaluation` | `count` | `auto_judge` | ✓ | AST errors specifically attached to declaration nodes. |
| `draft_ir_parse_failed` | `formula_ir_drafting` | `boolean_check` | `inspect_only` |   |  |
| `draft_ir_parse_failed` | `quality_evaluation` | `boolean_check` | `inspect_only` |   |  |
| `draft_ir_validation_failed` | `formula_ir_drafting` | `boolean_check` | `inspect_only` | ✓ |  |
| `draft_ir_validation_failed` | `quality_evaluation` | `boolean_check` | `inspect_only` | ✓ |  |
| `expr_shape_error_count` | `formula_ir_drafting` | `count` | `auto_judge` | ✓ | AST errors specifically attached to expression nodes. |
| `expr_shape_error_count` | `quality_evaluation` | `count` | `auto_judge` | ✓ | AST errors specifically attached to expression nodes. |
| `rendering_ok` | `formula_ir_drafting` | `shape_validation` | `inspect_only` | ✓ | whether the renderer produced IR text from the AST without renderer failure. |
| `rendering_ok` | `quality_evaluation` | `shape_validation` | `inspect_only` | ✓ | whether the renderer produced IR text from the AST without renderer failure. |

#### why = `layer_alignment` (9 rules)

| name | module | what | thr | actionable | what_it_counts |
|---|---|---|---|---|---|
| `content_token_jaccard` | `formula_ir_drafting` | `similarity` | `auto_judge` |   | overlap between source content tokens and IR content tokens. |
| `content_token_jaccard` | `quality_evaluation` | `similarity` | `auto_judge` |   | overlap between source content tokens and IR content tokens. |
| `definition_role_alignment_failed` | `formula_ir_drafting` | `boolean_check` | `inspect_only` |   |  |
| `definition_role_alignment_failed` | `quality_evaluation` | `boolean_check` | `inspect_only` |   |  |
| `definition_role_alignment_failed` | `source_normalization` | `boolean_check` | `inspect_only` |   |  |
| `ir_to_source_token_gap_count` | `formula_ir_drafting` | `count` | `trivial_warning` |   | IR-side content tokens without source, advisory, Prelude, or A4V3 support. |
| `ir_to_source_token_gap_count` | `quality_evaluation` | `count` | `trivial_warning` |   | IR-side content tokens without source, advisory, Prelude, or A4V3 support. |
| `source_to_ir_token_gap_count` | `formula_ir_drafting` | `count` | `trivial_warning` |   | source-side content tokens missing from IR surface. |
| `source_to_ir_token_gap_count` | `quality_evaluation` | `count` | `trivial_warning` |   | source-side content tokens missing from IR surface. |

### where = `triangle` — 59 rules

#### why = `coverage_indicator` (34 rules)

| name | module | what | thr | actionable | what_it_counts |
|---|---|---|---|---|---|
| `clarification_loss_count` | `formula_ir_drafting` | `count` | `auto_judge` |   | clarification clauses that disappear or survive only as unstructured notes. |
| `clarification_loss_count` | `quality_evaluation` | `count` | `auto_judge` |   | clarification clauses that disappear or survive only as unstructured notes. |
| `counterfactual_loss_count` | `formula_ir_drafting` | `count` | `auto_judge` |   | lost counterfactual semantics such as `would have been ... if ... had not occurr |
| `counterfactual_loss_count` | `quality_evaluation` | `count` | `auto_judge` |   | lost counterfactual semantics such as `would have been ... if ... had not occurr |
| `exception_visibility_violation_count` | `formula_ir_drafting` | `count` | `auto_judge` |   | exceptions or exclusions that disappear or are blurred into opaque helpers. |
| `exception_visibility_violation_count` | `quality_evaluation` | `count` | `auto_judge` |   | exceptions or exclusions that disappear or are blurred into opaque helpers. |
| `explicit_link_violation_count` | `formula_ir_drafting` | `count` | `auto_judge` |   | cases where a symbol name embeds another concept that the formula body never lin |
| `explicit_link_violation_count` | `merge_canonicalization` | `count` | `auto_judge` |   | cases where a symbol name embeds another concept that the formula body never lin |
| `explicit_link_violation_count` | `ontology_planning` | `count` | `auto_judge` |   | cases where a symbol name embeds another concept that the formula body never lin |
| `explicit_link_violation_count` | `quality_evaluation` | `count` | `auto_judge` |   | cases where a symbol name embeds another concept that the formula body never lin |
| `probe_clarification_preserved` | `formula_ir_drafting` | `other` | `auto_judge` |   | whether clarification semantics remain visible in formula or explicit annotation |
| `probe_clarification_preserved` | `quality_evaluation` | `other` | `auto_judge` |   | whether clarification semantics remain visible in formula or explicit annotation |
| `probe_counterfactual_preserved` | `formula_ir_drafting` | `count` | `auto_judge` |   | whether counterfactual semantics survive targeted probing. |
| `probe_counterfactual_preserved` | `quality_evaluation` | `count` | `auto_judge` |   | whether counterfactual semantics survive targeted probing. |
| `probe_exception_preserved` | `formula_ir_drafting` | `other` | `auto_judge` |   | whether exclusion clauses survive targeted probing. |
| `probe_exception_preserved` | `quality_evaluation` | `other` | `auto_judge` |   | whether exclusion clauses survive targeted probing. |
| `probe_negation_preserved` | `formula_ir_drafting` | `other` | `auto_judge` |   | whether negative force survives targeted probing. |
| `probe_negation_preserved` | `quality_evaluation` | `other` | `auto_judge` |   | whether negative force survives targeted probing. |
| `probe_reference_preserved` | `formula_ir_drafting` | `other` | `auto_judge` |   | whether external reference semantics such as `as defined in Section X` survive. |
| `probe_reference_preserved` | `quality_evaluation` | `other` | `auto_judge` |   | whether external reference semantics such as `as defined in Section X` survive. |
| `probe_responsibility_preserved` | `formula_ir_drafting` | `other` | `auto_judge` |   | whether responsibility or authority semantics remain visible where required. |
| `probe_responsibility_preserved` | `quality_evaluation` | `other` | `auto_judge` |   | whether responsibility or authority semantics remain visible where required. |
| `probe_scope_preserved` | `formula_ir_drafting` | `other` | `auto_judge` |   | whether scope semantics survive targeted probing. |
| `probe_scope_preserved` | `quality_evaluation` | `other` | `auto_judge` |   | whether scope semantics survive targeted probing. |
| `probe_temporal_order_preserved` | `formula_ir_drafting` | `other` | `auto_judge` |   | whether temporal ordering survives, for example `immediately following`, `preced |
| `probe_temporal_order_preserved` | `quality_evaluation` | `other` | `auto_judge` |   | whether temporal ordering survives, for example `immediately following`, `preced |
| `probe_value_source_preserved` | `formula_ir_drafting` | `other` | `auto_judge` |   | whether value-source semantics such as `most recent published price` or `as sour |
| `probe_value_source_preserved` | `quality_evaluation` | `other` | `auto_judge` |   | whether value-source semantics such as `most recent published price` or `as sour |
| `relation_type` | `merge_canonicalization` | `other` | `inspect_only` |   | not documented in catalog |
| `responsibility_loss_count` | `formula_ir_drafting` | `count` | `auto_judge` |   | responsibility, governance, or authority clauses omitted entirely when the model |
| `responsibility_loss_count` | `quality_evaluation` | `count` | `auto_judge` |   | responsibility, governance, or authority clauses omitted entirely when the model |
| `scope_visibility_violation_count` | `formula_ir_drafting` | `count` | `auto_judge` |   | scope restrictions that are lost, blurred, or pushed into symbol names only. |
| `scope_visibility_violation_count` | `quality_evaluation` | `count` | `auto_judge` |   | scope restrictions that are lost, blurred, or pushed into symbol names only. |
| `semantic_verdict` | `merge_canonicalization` | `categorical` | `inspect_only` |   | not documented in catalog |

#### why = `actionable_fix` (25 rules)

| name | module | what | thr | actionable | what_it_counts |
|---|---|---|---|---|---|
| `counterexample_source_ir_agreement_rate` | `source_to_ir_fidelity` | `ratio` | `auto_judge` | ✓ | fraction of generated counterexample scenarios where source and IR agree on the  |
| `fact_precision_to_source` | `source_to_ir_fidelity` | `ratio` | `auto_judge` | ✓ | fraction of render-back facts that have a corresponding source fact (i.e. NOT ha |
| `fact_recall_to_source` | `source_to_ir_fidelity` | `ratio` | `auto_judge` | ✓ | fraction of source-extracted atomic facts that have a corresponding fact in the  |
| `missing_source_fact_count` | `source_to_ir_fidelity` | `count` | `auto_judge` | ✓ | absolute count of source-fact items that B5 marked as 'missing' (no aligned rend |
| `modality_quantifier_loss_in_render` | `source_to_ir_fidelity` | `other` | `auto_judge` | ✓ | count of modal verbs / quantifiers / temporal markers that exist in source but d |
| `multi_judge_mode_corresponds` | `source_to_ir_fidelity` | `other` | `auto_judge` | ✓ | whether the panel's mode verdict is `corresponds` (vs `partially_corresponds` or |
| `multi_judge_unanimous` | `source_to_ir_fidelity` | `other` | `auto_judge` | ✓ | whether the N-model judge panel unanimously returned the same verdict. |
| `render_back_available` | `formula_ir_drafting` | `boolean_check` | `inspect_only` | ✓ | whether a verbalized natural-language rendering of the IR exists. |
| `render_back_available` | `quality_evaluation` | `boolean_check` | `inspect_only` | ✓ | whether a verbalized natural-language rendering of the IR exists. |
| `render_back_clause_count` | `formula_ir_drafting` | `count` | `trivial_warning` | ✓ | number of natural-language blocks in the render-back. |
| `render_back_clause_count` | `quality_evaluation` | `count` | `trivial_warning` | ✓ | number of natural-language blocks in the render-back. |
| `render_bertscore_f1_to_normalized` | `formula_ir_drafting` | `similarity` | `auto_judge` | ✓ | semantic similarity between render-back text and normalized clauses. |
| `render_bertscore_f1_to_normalized` | `quality_evaluation` | `similarity` | `auto_judge` | ✓ | semantic similarity between render-back text and normalized clauses. |
| `render_bertscore_f1_to_source` | `formula_ir_drafting` | `similarity` | `auto_judge` | ✓ | semantic similarity between render-back text and original source excerpt. |
| `render_bertscore_f1_to_source` | `quality_evaluation` | `similarity` | `auto_judge` | ✓ | semantic similarity between render-back text and original source excerpt. |
| `render_contradiction_score` | `formula_ir_drafting` | `statistic` | `inspect_only` | ✓ | probability or score that render-back contradicts normalized text. |
| `render_contradiction_score` | `quality_evaluation` | `statistic` | `inspect_only` | ✓ | probability or score that render-back contradicts normalized text. |
| `render_hallucinated_fact_count` | `source_to_ir_fidelity` | `count` | `auto_judge` | ✓ | absolute count of render-only fact items (B5 render_only list). |
| `render_nli_ir_implies_text` | `formula_ir_drafting` | `similarity` | `auto_judge` | ✓ | whether the render-back semantically entails the normalized text. |
| `render_nli_ir_implies_text` | `quality_evaluation` | `similarity` | `auto_judge` | ✓ | whether the render-back semantically entails the normalized text. |
| `render_nli_text_implies_ir` | `formula_ir_drafting` | `similarity` | `auto_judge` | ✓ | whether the normalized text semantically entails the render-back. |
| `render_nli_text_implies_ir` | `quality_evaluation` | `similarity` | `auto_judge` | ✓ | whether the normalized text semantically entails the render-back. |
| `stronger_pair_count` | `source_to_ir_fidelity` | `count` | `auto_judge` | ✓ | B5 alignment pairs marked match=stronger — render claim is strictly stronger tha |
| `targeted_probe_preservation_rate` | `source_to_ir_fidelity` | `ratio` | `auto_judge` | ✓ | fraction of 9 targeted probes (negation/scope/temporal/responsibility/...) where |
| `weaker_pair_count` | `source_to_ir_fidelity` | `count` | `auto_judge` | ✓ | B5 alignment pairs marked match=weaker — render claim is strictly weaker than so |

### where = `ir_vs_text` — 55 rules

#### why = `actionable_fix` (34 rules)

| name | module | what | thr | actionable | what_it_counts |
|---|---|---|---|---|---|
| `deontic_lowering_correct` | `source_to_ir_fidelity` | `other` | `inspect_only` | ✓ | for each source signal in {modality_obligation, modality_permission, modality_pr |
| `expected_family_present` | `source_to_ir_fidelity` | `boolean_check` | `auto_judge` | ✓ | for each source signal (modality/temporal/...) that triggers an expected a4v3 fa |
| `formula_repeat_underuse_mass` | `formula_ir_drafting` | `statistic` | `trivial_warning` | ✓ | total missing repetition mass in formal IR. |
| `formula_repeat_underuse_mass` | `quality_evaluation` | `statistic` | `trivial_warning` | ✓ | total missing repetition mass in formal IR. |
| `formula_repeat_underuse_token_count` | `formula_ir_drafting` | `count` | `trivial_warning` | ✓ | how many source content tokens appear fewer times in formal IR than in the sourc |
| `formula_repeat_underuse_token_count` | `quality_evaluation` | `count` | `trivial_warning` | ✓ | how many source content tokens appear fewer times in formal IR than in the sourc |
| `innf_family_diversity` | `source_to_ir_fidelity` | `other` | `inspect_only` | ✓ | how many of the 12 INNF families are used in the IR (TypeDecl/SymbolDecl/AssertD |
| `new_formula_content_token_count_vs_text_only` | `formula_ir_drafting` | `count` | `trivial_warning` | ✓ | semantically meaningful new formula tokens relative to source plus normalized te |
| `new_formula_content_token_count_vs_text_only` | `ontology_planning` | `count` | `trivial_warning` | ✓ | semantically meaningful new formula tokens relative to source plus normalized te |
| `new_formula_content_token_count_vs_text_only` | `quality_evaluation` | `count` | `trivial_warning` | ✓ | semantically meaningful new formula tokens relative to source plus normalized te |
| `new_formula_token_count_vs_text_only` | `formula_ir_drafting` | `count` | `trivial_warning` | ✓ | all new formula tokens relative to source plus normalized text only, without for |
| `new_formula_token_count_vs_text_only` | `ontology_planning` | `count` | `trivial_warning` | ✓ | all new formula tokens relative to source plus normalized text only, without for |
| `new_formula_token_count_vs_text_only` | `quality_evaluation` | `count` | `trivial_warning` | ✓ | all new formula tokens relative to source plus normalized text only, without for |
| `new_full_surface_content_token_count_vs_text_only` | `formula_ir_drafting` | `count` | `trivial_warning` | ✓ | semantically meaningful new tokens in rendered IR plus prose fields relative to  |
| `new_full_surface_content_token_count_vs_text_only` | `ontology_planning` | `count` | `trivial_warning` | ✓ | semantically meaningful new tokens in rendered IR plus prose fields relative to  |
| `new_full_surface_content_token_count_vs_text_only` | `quality_evaluation` | `count` | `trivial_warning` | ✓ | semantically meaningful new tokens in rendered IR plus prose fields relative to  |
| `new_full_surface_token_count_vs_text_only` | `formula_ir_drafting` | `count` | `trivial_warning` | ✓ | all new tokens in rendered IR plus prose fields relative to source plus normaliz |
| `new_full_surface_token_count_vs_text_only` | `ontology_planning` | `count` | `trivial_warning` | ✓ | all new tokens in rendered IR plus prose fields relative to source plus normaliz |
| `new_full_surface_token_count_vs_text_only` | `quality_evaluation` | `count` | `trivial_warning` | ✓ | all new tokens in rendered IR plus prose fields relative to source plus normaliz |
| `source_phrase_coverage_rate` | `source_to_ir_fidelity` | `ratio` | `auto_judge` | ✓ | fraction of noun-ish phrases extracted from source that have ≥50% token overlap  |
| `temporal_lowering_correct` | `source_to_ir_fidelity` | `other` | `inspect_only` | ✓ | for each source signal in {temporal_eventually, temporal_always, temporal_order} |
| `uncovered_source_phrases` | `source_to_ir_fidelity` | `other` | `auto_judge` | ✓ | absolute count of phrases extracted from source.md that have <50% token overlap  |
| `ungrounded_callee_count` | `formula_ir_drafting` | `count` | `auto_judge` | ✓ | callee names used in calls that are not declared, Prelude, or whitelisted A4V3 b |
| `ungrounded_callee_count` | `ontology_planning` | `count` | `auto_judge` | ✓ | callee names used in calls that are not declared, Prelude, or whitelisted A4V3 b |
| `ungrounded_callee_count` | `quality_evaluation` | `count` | `auto_judge` | ✓ | callee names used in calls that are not declared, Prelude, or whitelisted A4V3 b |
| `ungrounded_ref_count` | `formula_ir_drafting` | `count` | `auto_judge` | ✓ | expression references that are not locally bound, declared, or grounded. |
| `ungrounded_ref_count` | `ontology_planning` | `count` | `auto_judge` | ✓ | expression references that are not locally bound, declared, or grounded. |
| `ungrounded_ref_count` | `quality_evaluation` | `count` | `auto_judge` | ✓ | expression references that are not locally bound, declared, or grounded. |
| `ungrounded_sort_count` | `formula_ir_drafting` | `count` | `auto_judge` | ✓ | sort names that are neither Prelude, built-in, locally declared, nor text/adviso |
| `ungrounded_sort_count` | `ontology_planning` | `count` | `auto_judge` | ✓ | sort names that are neither Prelude, built-in, locally declared, nor text/adviso |
| `ungrounded_sort_count` | `quality_evaluation` | `count` | `auto_judge` | ✓ | sort names that are neither Prelude, built-in, locally declared, nor text/adviso |
| `ungrounded_symbol_count` | `formula_ir_drafting` | `count` | `auto_judge` | ✓ | symbols declared in IR that are not grounded in source, advisory, Prelude, or bu |
| `ungrounded_symbol_count` | `ontology_planning` | `count` | `auto_judge` | ✓ | symbols declared in IR that are not grounded in source, advisory, Prelude, or bu |
| `ungrounded_symbol_count` | `quality_evaluation` | `count` | `auto_judge` | ✓ | symbols declared in IR that are not grounded in source, advisory, Prelude, or bu |

#### why = `coverage_indicator` (21 rules)

| name | module | what | thr | actionable | what_it_counts |
|---|---|---|---|---|---|
| `formula_content_token_mass` | `formula_ir_drafting` | `statistic` | `trivial_warning` |   | total multiplicity of content tokens in formal IR surface. |
| `formula_content_token_mass` | `quality_evaluation` | `statistic` | `trivial_warning` |   | total multiplicity of content tokens in formal IR surface. |
| `formula_repeat_overuse_examples` | `formula_ir_drafting` | `other` | `trivial_warning` |   | the most obviously overused content tokens in formal IR. |
| `formula_repeat_overuse_examples` | `quality_evaluation` | `other` | `trivial_warning` |   | the most obviously overused content tokens in formal IR. |
| `formula_repeat_overuse_mass` | `formula_ir_drafting` | `statistic` | `trivial_warning` |   | total excess repetition mass in formal IR. |
| `formula_repeat_overuse_mass` | `quality_evaluation` | `statistic` | `trivial_warning` |   | total excess repetition mass in formal IR. |
| `formula_repeat_overuse_token_count` | `formula_ir_drafting` | `count` | `trivial_warning` |   | how many source-licensed content tokens are repeated more often in formal IR tha |
| `formula_repeat_overuse_token_count` | `quality_evaluation` | `count` | `trivial_warning` |   | how many source-licensed content tokens are repeated more often in formal IR tha |
| `full_surface_content_token_mass` | `formula_ir_drafting` | `statistic` | `trivial_warning` |   | total multiplicity of content tokens across formal IR and prose fields together. |
| `full_surface_content_token_mass` | `quality_evaluation` | `statistic` | `trivial_warning` |   | total multiplicity of content tokens across formal IR and prose fields together. |
| `full_surface_repeat_overuse_examples` | `formula_ir_drafting` | `other` | `trivial_warning` |   | the strongest repetition-inflation examples anywhere in the artifact. |
| `full_surface_repeat_overuse_examples` | `quality_evaluation` | `other` | `trivial_warning` |   | the strongest repetition-inflation examples anywhere in the artifact. |
| `full_surface_repeat_overuse_mass` | `formula_ir_drafting` | `statistic` | `trivial_warning` |   | total excess repetition mass across IR plus prose. |
| `full_surface_repeat_overuse_mass` | `quality_evaluation` | `statistic` | `trivial_warning` |   | total excess repetition mass across IR plus prose. |
| `full_surface_repeat_overuse_token_count` | `formula_ir_drafting` | `count` | `trivial_warning` |   | how many content tokens are repeated more often in IR plus notes than in the sou |
| `full_surface_repeat_overuse_token_count` | `quality_evaluation` | `count` | `trivial_warning` |   | how many content tokens are repeated more often in IR plus notes than in the sou |
| `prelude_redeclaration_count` | `formula_ir_drafting` | `count` | `trivial_warning` |   | attempts to redeclare Prelude sorts, entities, or functions. |
| `prelude_redeclaration_count` | `ontology_planning` | `count` | `trivial_warning` |   | attempts to redeclare Prelude sorts, entities, or functions. |
| `prelude_redeclaration_count` | `quality_evaluation` | `count` | `trivial_warning` |   | attempts to redeclare Prelude sorts, entities, or functions. |
| `source_content_token_mass` | `formula_ir_drafting` | `statistic` | `trivial_warning` |   | total multiplicity of content tokens in the source text, not just distinct token |
| `source_content_token_mass` | `quality_evaluation` | `statistic` | `trivial_warning` |   | total multiplicity of content tokens in the source text, not just distinct token |

### where = `text_vs_normalized` — 42 rules

#### why = `coverage_indicator` (22 rules)

| name | module | what | thr | actionable | what_it_counts |
|---|---|---|---|---|---|
| `normalized_clause_count` | `formula_ir_drafting` | `count` | `trivial_warning` |   | number of normalized clauses presented to IR drafting. |
| `normalized_clause_count` | `quality_evaluation` | `count` | `trivial_warning` |   | number of normalized clauses presented to IR drafting. |
| `normalized_content_mass_per_clause` | `quality_evaluation` | `statistic` | `trivial_warning` |   | average content-token mass per normalized clause. |
| `normalized_content_mass_per_clause` | `source_normalization` | `statistic` | `trivial_warning` |   | average content-token mass per normalized clause. |
| `normalized_content_token_count` | `quality_evaluation` | `count` | `trivial_warning` |   | distinct content tokens in normalized clauses. |
| `normalized_content_token_count` | `source_normalization` | `count` | `trivial_warning` |   | distinct content tokens in normalized clauses. |
| `normalized_content_token_mass` | `quality_evaluation` | `statistic` | `trivial_warning` |   | total multiplicity of content tokens in normalized clauses. |
| `normalized_content_token_mass` | `source_normalization` | `statistic` | `trivial_warning` |   | total multiplicity of content tokens in normalized clauses. |
| `normalized_implies_source_entailment` | `quality_evaluation` | `other` | `auto_judge` |   | whether normalization semantically entails the source. |
| `normalized_implies_source_entailment` | `source_normalization` | `other` | `auto_judge` |   | whether normalization semantically entails the source. |
| `normalized_repeat_overuse_examples` | `quality_evaluation` | `other` | `trivial_warning` |   | top examples of normalization inflating token repetition. |
| `normalized_repeat_overuse_examples` | `source_normalization` | `other` | `trivial_warning` |   | top examples of normalization inflating token repetition. |
| `normalized_repeat_overuse_mass` | `quality_evaluation` | `statistic` | `trivial_warning` |   | total excess repetition introduced by normalization. |
| `normalized_repeat_overuse_mass` | `source_normalization` | `statistic` | `trivial_warning` |   | total excess repetition introduced by normalization. |
| `normalized_repeat_overuse_token_count` | `quality_evaluation` | `count` | `trivial_warning` |   | number of source-licensed content tokens repeated more often in normalization th |
| `normalized_repeat_overuse_token_count` | `source_normalization` | `count` | `trivial_warning` |   | number of source-licensed content tokens repeated more often in normalization th |
| `source_excerpt_content_token_count` | `quality_evaluation` | `count` | `trivial_warning` |   | distinct source-side content tokens in the original source excerpt. |
| `source_excerpt_content_token_count` | `source_normalization` | `count` | `trivial_warning` |   | distinct source-side content tokens in the original source excerpt. |
| `source_excerpt_content_token_mass` | `quality_evaluation` | `statistic` | `trivial_warning` |   | total multiplicity of content tokens in the original source excerpt. |
| `source_excerpt_content_token_mass` | `source_normalization` | `statistic` | `trivial_warning` |   | total multiplicity of content tokens in the original source excerpt. |
| `source_implies_normalized_entailment` | `quality_evaluation` | `other` | `auto_judge` |   | whether the source semantically entails the normalization. |
| `source_implies_normalized_entailment` | `source_normalization` | `other` | `auto_judge` |   | whether the source semantically entails the normalization. |

#### why = `actionable_fix` (12 rules)

| name | module | what | thr | actionable | what_it_counts |
|---|---|---|---|---|---|
| `normalized_content_token_multiset_precision_to_source` | `quality_evaluation` | `ratio` | `auto_judge` | ✓ | how much of normalized token mass is licensed directly by source wording. |
| `normalized_content_token_multiset_precision_to_source` | `source_normalization` | `ratio` | `auto_judge` | ✓ | how much of normalized token mass is licensed directly by source wording. |
| `normalized_content_token_multiset_recall_from_source` | `quality_evaluation` | `ratio` | `auto_judge` | ✓ | how much of the source token mass survives into normalization. |
| `normalized_content_token_multiset_recall_from_source` | `source_normalization` | `ratio` | `auto_judge` | ✓ | how much of the source token mass survives into normalization. |
| `normalized_content_token_precision_to_source` | `quality_evaluation` | `ratio` | `auto_judge` | ✓ | how source-grounded the normalized token inventory is. |
| `normalized_content_token_precision_to_source` | `source_normalization` | `ratio` | `auto_judge` | ✓ | how source-grounded the normalized token inventory is. |
| `normalized_content_token_recall_from_source` | `quality_evaluation` | `ratio` | `auto_judge` | ✓ | how much of the original source token inventory survives into normalization. |
| `normalized_content_token_recall_from_source` | `source_normalization` | `ratio` | `auto_judge` | ✓ | how much of the original source token inventory survives into normalization. |
| `normalized_to_source_new_token_count` | `quality_evaluation` | `count` | `trivial_warning` | ✓ | distinct content tokens introduced by normalization that were not present in sou |
| `normalized_to_source_new_token_count` | `source_normalization` | `count` | `trivial_warning` | ✓ | distinct content tokens introduced by normalization that were not present in sou |
| `source_vs_normalized_contradiction_score` | `quality_evaluation` | `statistic` | `inspect_only` | ✓ | contradiction risk between source and normalization. |
| `source_vs_normalized_contradiction_score` | `source_normalization` | `statistic` | `inspect_only` | ✓ | contradiction risk between source and normalization. |

#### why = `layer_alignment` (8 rules)

| name | module | what | thr | actionable | what_it_counts |
|---|---|---|---|---|---|
| `normalized_content_token_jaccard` | `quality_evaluation` | `similarity` | `auto_judge` |   | set-overlap between source content tokens and normalized content tokens. |
| `normalized_content_token_jaccard` | `source_normalization` | `similarity` | `auto_judge` |   | set-overlap between source content tokens and normalized content tokens. |
| `normalized_length_ratio_vs_source_mass` | `quality_evaluation` | `ratio` | `trivial_warning` |   | how much normalization expands or compresses source token mass. |
| `normalized_length_ratio_vs_source_mass` | `source_normalization` | `ratio` | `trivial_warning` |   | how much normalization expands or compresses source token mass. |
| `source_normalized_bertscore_f1` | `quality_evaluation` | `similarity` | `auto_judge` |   | semantic similarity between original source excerpt and normalized clauses. |
| `source_normalized_bertscore_f1` | `source_normalization` | `similarity` | `auto_judge` |   | semantic similarity between original source excerpt and normalized clauses. |
| `source_to_normalized_token_gap_count` | `quality_evaluation` | `count` | `trivial_warning` |   | distinct source content tokens that normalization dropped completely. |
| `source_to_normalized_token_gap_count` | `source_normalization` | `count` | `trivial_warning` |   | distinct source content tokens that normalization dropped completely. |

### where = `corpus` — 4 rules

#### why = `layer_alignment` (2 rules)

| name | module | what | thr | actionable | what_it_counts |
|---|---|---|---|---|---|
| `llm_bertscore` | `merge_canonicalization` | `similarity` | `inspect_only` |   | not documented in catalog |
| `llm_ir_to_text` | `merge_canonicalization` | `other` | `inspect_only` |   | not documented in catalog |

#### why = `actionable_fix` (1 rules)

| name | module | what | thr | actionable | what_it_counts |
|---|---|---|---|---|---|
| `llm_contradiction` | `merge_canonicalization` | `other` | `inspect_only` | ✓ | not documented in catalog |

#### why = `coverage_indicator` (1 rules)

| name | module | what | thr | actionable | what_it_counts |
|---|---|---|---|---|---|
| `llm_text_to_ir` | `merge_canonicalization` | `other` | `inspect_only` |   | not documented in catalog |

---

## Unimplemented rules — decisions pending

### value=None (concept declared in `extended` but stubbed) — 53

| name | module | what_it_counts | how_to_compute |
|---|---|---|---|
| `accepted` | `quality_evaluation` | (no description) | (no description) |
| `critic_margin` | `merge_canonicalization` | gap between best and second-best variant according to critic ranking. | if critic provides scores, subtract rank-2 score from rank-1 score; otherwise de |
| `critic_margin` | `quality_evaluation` | gap between best and second-best variant according to critic ranking. | if critic provides scores, subtract rank-2 score from rank-1 score; otherwise de |
| `dependency_link_recall` | `formula_ir_drafting` | share of expected dependency concepts that are explicitly linked in formula. | `explicitly linked dependency count / expected dependency count`. |
| `dependency_link_recall` | `merge_canonicalization` | share of expected dependency concepts that are explicitly linked in formula. | `explicitly linked dependency count / expected dependency count`. |
| `dependency_link_recall` | `ontology_planning` | share of expected dependency concepts that are explicitly linked in formula. | `explicitly linked dependency count / expected dependency count`. |
| `dependency_link_recall` | `quality_evaluation` | share of expected dependency concepts that are explicitly linked in formula. | `explicitly linked dependency count / expected dependency count`. |
| `focus_symbol_arity` | `formula_ir_drafting` | the arity chosen for the focus term itself. | read the declared argument count of the focus symbol. |
| `focus_symbol_arity` | `merge_canonicalization` | the arity chosen for the focus term itself. | read the declared argument count of the focus symbol. |
| `focus_symbol_arity` | `quality_evaluation` | the arity chosen for the focus term itself. | read the declared argument count of the focus symbol. |
| `gold_clause_alignment` | `merge_canonicalization` | fraction of gold semantic blocks aligned by the candidate IR. | align candidate clause coverage map against gold clause inventory. |
| `gold_clause_alignment` | `quality_evaluation` | fraction of gold semantic blocks aligned by the candidate IR. | align candidate clause coverage map against gold clause inventory. |
| `gold_counterfactual_recall` | `merge_canonicalization` | share of gold counterfactual semantics preserved. | `matched gold counterfactual fragments / total gold counterfactual fragments`. |
| `gold_counterfactual_recall` | `quality_evaluation` | share of gold counterfactual semantics preserved. | `matched gold counterfactual fragments / total gold counterfactual fragments`. |
| `gold_dependency_recall` | `merge_canonicalization` | share of explicit concept links in gold that are preserved in the candidate. | `matched gold dependency links / total gold dependency links`. |
| `gold_dependency_recall` | `quality_evaluation` | share of explicit concept links in gold that are preserved in the candidate. | `matched gold dependency links / total gold dependency links`. |
| `gold_exception_recall` | `merge_canonicalization` | share of gold exclusion semantics preserved. | `matched gold exception fragments / total gold exception fragments`. |
| `gold_exception_recall` | `quality_evaluation` | share of gold exclusion semantics preserved. | `matched gold exception fragments / total gold exception fragments`. |
| `gold_helper_overuse_delta` | `merge_canonicalization` | how much more helper machinery the candidate introduces than the gold. | `candidate helper count - gold helper count`. |
| `gold_helper_overuse_delta` | `quality_evaluation` | how much more helper machinery the candidate introduces than the gold. | `candidate helper count - gold helper count`. |
| `gold_modulo_renaming_match` | `merge_canonicalization` | whether candidate and gold are equivalent up to safe renaming and trivial format | canonicalize names and compare normalized structure. |
| `gold_modulo_renaming_match` | `quality_evaluation` | whether candidate and gold are equivalent up to safe renaming and trivial format | canonicalize names and compare normalized structure. |
| `gold_render_similarity` | `merge_canonicalization` | semantic similarity between candidate render-back and gold render-back. | BERTScore, NLI, or clause-aligned similarity on verbalized forms. |
| `gold_render_similarity` | `quality_evaluation` | semantic similarity between candidate render-back and gold render-back. | BERTScore, NLI, or clause-aligned similarity on verbalized forms. |
| `gold_scope_recall` | `merge_canonicalization` | share of gold scope semantics preserved. | `matched gold scope fragments / total gold scope fragments`. |
| `gold_scope_recall` | `quality_evaluation` | share of gold scope semantics preserved. | `matched gold scope fragments / total gold scope fragments`. |
| `gold_structure_similarity` | `merge_canonicalization` | structural similarity modulo renaming between candidate IR and gold IR. | compare declaration graph, assertion skeleton, and operator shapes after normali |
| `gold_structure_similarity` | `quality_evaluation` | structural similarity modulo renaming between candidate IR and gold IR. | compare declaration graph, assertion skeleton, and operator shapes after normali |
| `keep_unresolved_ambiguity_visible` | `quality_evaluation` | (no description) | (no description) |
| `keep_unresolved_ambiguity_visible` | `source_normalization` | (no description) | (no description) |
| `needs_review` | `quality_evaluation` | (no description) | (no description) |
| `pairwise_structure_distance_mean` | `merge_canonicalization` | mean structural drift between all pairs of variants or reruns. | `1 - pairwise_structure_similarity_mean`. |
| `pairwise_structure_distance_mean` | `quality_evaluation` | mean structural drift between all pairs of variants or reruns. | `1 - pairwise_structure_similarity_mean`. |
| `pairwise_structure_similarity_mean` | `merge_canonicalization` | mean structural similarity between all pairs of variants or reruns. | compare declaration mix, logical-operator mix, and arity profile pairwise; avera |
| `pairwise_structure_similarity_mean` | `quality_evaluation` | mean structural similarity between all pairs of variants or reruns. | compare declaration mix, logical-operator mix, and arity profile pairwise; avera |
| `pairwise_structure_similarity_mean_per_parameter_slot_mass` | `merge_canonicalization` | structural stability bought per unit of parameter mass. | `pairwise_structure_similarity_mean / total_parameter_slot_mass`. |
| `pairwise_structure_similarity_mean_per_parameter_slot_mass` | `quality_evaluation` | structural stability bought per unit of parameter mass. | `pairwise_structure_similarity_mean / total_parameter_slot_mass`. |
| `pairwise_token_jaccard_mean` | `merge_canonicalization` | average lexical overlap between rendered IR artifacts. | compute content-token Jaccard for every pair, then average. |
| `pairwise_token_jaccard_mean` | `quality_evaluation` | average lexical overlap between rendered IR artifacts. | compute content-token Jaccard for every pair, then average. |
| `preserve_meaning` | `quality_evaluation` | (no description) | (no description) |
| `preserve_meaning` | `source_normalization` | (no description) | (no description) |
| `role_link` | `merge_canonicalization` | (no description) | (no description) |
| `same_parameter_mass_different_structure_pair_ratio` | `merge_canonicalization` | rate of decomposition drift after controlling for parameter mass. | `same_parameter_mass_different_structure_pair_count / total_pair_count`. |
| `same_parameter_mass_different_structure_pair_ratio` | `quality_evaluation` | rate of decomposition drift after controlling for parameter mass. | `same_parameter_mass_different_structure_pair_count / total_pair_count`. |
| `soft_review` | `quality_evaluation` | (no description) | (no description) |
| `sort_choice_stability` | `formula_ir_drafting` | whether different variants agree on sorts for the same argument positions. | compare argument-sort tuples across variants; report agreement ratio. |
| `sort_choice_stability` | `merge_canonicalization` | whether different variants agree on sorts for the same argument positions. | compare argument-sort tuples across variants; report agreement ratio. |
| `sort_choice_stability` | `ontology_planning` | whether different variants agree on sorts for the same argument positions. | compare argument-sort tuples across variants; report agreement ratio. |
| `sort_choice_stability` | `quality_evaluation` | whether different variants agree on sorts for the same argument positions. | compare argument-sort tuples across variants; report agreement ratio. |
| `threshold` | `quality_evaluation` | not documented in catalog | not documented in catalog |
| `threshold` | `source_normalization` | not documented in catalog | not documented in catalog |
| `variant_diversity_score` | `merge_canonicalization` | how different the variants really are. | average pairwise structural distance across variants. |
| `variant_diversity_score` | `quality_evaluation` | how different the variants really are. | average pairwise structural distance across variants. |

### no key in any metric file (no implementation at all) — 0

| name | module | what_it_counts | how_to_compute |
|---|---|---|---|