# Explained Metrics and Checks: quality_evaluation

Metric count: 247
Check count: 50

## Metrics
### `advisory_grounded_content_piece_ratio_mean`
- kind: `continuous`
- what it checks: how grounded identifier pieces are if advisory vocabulary is also counted as a license source.
- how it is computed: same as above, but expand the lexicon with advisory text.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `advisory_only_symbol_count`
- kind: `hard_warning`
- what it checks: symbols whose only license comes from advisory prose rather than source text or normalized clauses.
- how it is computed: count symbols found in advisory names but not in source-term inventory or normalized token inventory.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `annotation_node_count`
- kind: `continuous`
- what it checks: number of explicit non-formula semantic annotation nodes used to preserve clarification, responsibility, or provenance.
- how it is computed: count accepted annotation structures beyond bare notes.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `arg_arity_stability`
- kind: `comparative`
- what it checks: whether different variants agree on argument count.
- how it is computed: compare top-level focus symbol arity across variants; report agreement ratio.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `artifact_signature_entropy`
- kind: `comparative`
- what it checks: how evenly the artifact space is spread across distinct signatures rather than collapsing to one dominant form.
- how it is computed: Shannon entropy over normalized artifact signatures or focus signatures.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `assertion_count`
- kind: `continuous`
- what it checks: number of top-level assertion blocks in the IR.
- how it is computed: count AST assertions.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `assertion_shape_error_count`
- kind: `continuous`
- what it checks: AST errors specifically attached to assertion nodes.
- how it is computed: count validation errors whose path begins with `ir_ast.assertions`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Fix AST/surface syntax, declaration shape, expression shape, or combined validation.

### `ast_error_count`
- kind: `continuous`
- what it checks: total number of canonical AST validation errors.
- how it is computed: the length of `_validate_canonical_drafter_payload(payload)`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Fix AST/surface syntax, declaration shape, expression shape, or combined validation.

### `ast_valid`
- kind: `hard_fail`
- what it checks: whether the emitted payload satisfies the canonical AST contract.
- how it is computed: `1` if `_validate_canonical_drafter_payload(payload)` returns zero errors, else `0`.
- what is wrong when it fails or looks bad: If this fails, the artifact should not be accepted.
- likely action: Fix AST/surface syntax, declaration shape, expression shape, or combined validation.

### `avg_call_latency_s`
- kind: `continuous`
- what it checks: average latency of one successful model completion.
- how it is computed: mean of per-call durations.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `avg_structure_similarity_to_other_successful_runs`
- kind: `comparative`
- what it checks: how close the current artifact is to the rest of the successful cohort.
- how it is computed: for the chosen artifact, compute mean structure similarity to every other successful artifact in the cohort.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `best_content_token_jaccard`
- kind: not documented in metric catalog
- what it checks: not documented
- how it is computed: not documented
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `best_content_token_recall`
- kind: not documented in metric catalog
- what it checks: not documented
- how it is computed: not documented
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `biconditional_present_when_expected`
- kind: `continuous`
- what it checks: whether predicate-like definitions are encoded with `iff` or semantically equivalent bidirectional structure when appropriate.
- how it is computed: boolean flag comparing focus-term kind to expression structure.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `callable_symbol_count`
- kind: `continuous`
- what it checks: number of declared callable local symbols.
- how it is computed: count local `fun` and `rel` declarations.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `callable_symbol_with_args_count`
- kind: `continuous`
- what it checks: number of callable local symbols that actually take arguments.
- how it is computed: count local `fun` and `rel` declarations whose arity is greater than zero.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `candidate_reading_count`
- kind: `continuous`
- what it checks: number of advisory candidate readings proposed.
- how it is computed: `len(candidate_readings)`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `carrier_choice_stability`
- kind: `comparative`
- what it checks: whether different runs choose the same carrier family, for example function vs relation or exchange-level vs component-level predicate.
- how it is computed: compare chosen carrier signatures across variants or reruns; report agreement ratio.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `clarification_loss_count`
- kind: `hard_warning`
- what it checks: clarification clauses that disappear or survive only as unstructured notes.
- how it is computed: count clarification fragments not present in formula or explicit clarification annotation nodes.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Make the lost scope/exception/negation/temporal/responsibility structure explicit in IR.

### `clause_coverage_ratio`
- kind: `continuous`
- what it checks: fraction of normalized clauses that are represented somewhere in IR or explicit accepted annotation nodes.
- how it is computed: `covered_clause_count / normalized_clause_count`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Check whether every normalized logic burden is represented in formula-bearing IR.

### `clause_overdecomposition_mass`
- kind: `continuous`
- what it checks: how many extra logic blocks were introduced beyond normalized clause count.
- how it is computed: `max(0, logic_block_count - normalized_clause_count)`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Check whether every normalized logic burden is represented in formula-bearing IR.

### `clause_to_logic_block_ratio`
- kind: `continuous`
- what it checks: how many normalized clauses are being carried, on average, by one logic block.
- how it is computed: `normalized_clause_count / max(1, logic_block_count)`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Check whether every normalized logic burden is represented in formula-bearing IR.

### `clause_underdecomposition_mass`
- kind: `hard_warning`
- what it checks: how many normalized clauses have no corresponding top-level logic block if we compare counts naively.
- how it is computed: `max(0, normalized_clause_count - logic_block_count)`.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Check whether every normalized logic burden is represented in formula-bearing IR.

### `combined_validation_ok`
- kind: `hard_fail`
- what it checks: whether the draft validates when combined with the current section IR or section theory.
- how it is computed: `1` if combined parse/validation succeeds, else `0`.
- what is wrong when it fails or looks bad: If this fails, the artifact should not be accepted.
- likely action: Fix AST/surface syntax, declaration shape, expression shape, or combined validation.

### `compound_identifier_count_content`
- kind: `hard_warning`
- what it checks: identifiers with at least 3 non-stopword content pieces.
- how it is computed: split each identifier, remove stopwords/syntax pieces, then count identifiers with at least 3 remaining pieces.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Split overloaded names and add structural anchors in declarations/formulas/ontology.

### `compound_identifier_count_raw`
- kind: `hard_warning`
- what it checks: identifiers whose raw split length is already large.
- how it is computed: split each identifier at camel/snake boundaries and count those with at least 4 raw pieces.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Split overloaded names and add structural anchors in declarations/formulas/ontology.

### `compound_identifier_rate_content`
- kind: `continuous`
- what it checks: how large the content-level glued-name population is relative to the whole identifier inventory.
- how it is computed: `compound_identifier_count_content / identifier_count`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Split overloaded names and add structural anchors in declarations/formulas/ontology.

### `compound_identifier_rate_raw`
- kind: `continuous`
- what it checks: how large the raw glued-name population is relative to the whole identifier inventory.
- how it is computed: `compound_identifier_count_raw / identifier_count`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Split overloaded names and add structural anchors in declarations/formulas/ontology.

### `consensus_margin`
- kind: `comparative`
- what it checks: how strongly majority or plurality favored the selected advisory reading.
- how it is computed: `winning_vote_count - runner_up_vote_count`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `consensus_sample_count`
- kind: `continuous`
- what it checks: number of advisory samples or committee votes used.
- how it is computed: count sampled advisory runs.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `content_token_jaccard`
- kind: `continuous`
- what it checks: overlap between source content tokens and IR content tokens.
- how it is computed: `|intersection| / |union|`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `content_token_multiset_precision`
- kind: `continuous`
- what it checks: precision with repeated token occurrences taken seriously.
- how it is computed: multiset overlap count divided by total IR content-token multiplicity.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `content_token_multiset_recall`
- kind: `continuous`
- what it checks: recall with repeated token occurrences taken seriously.
- how it is computed: multiset overlap count divided by total source content-token multiplicity.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `content_token_precision`
- kind: `continuous`
- what it checks: how much of the IR content-token inventory is source-licensed.
- how it is computed: `matched IR content tokens / total IR content tokens`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `content_token_recall`
- kind: `continuous`
- what it checks: how much of the source content-token inventory appears in IR.
- how it is computed: `matched source content tokens / total source content tokens`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `core_term_centeredness_score`
- kind: `continuous`
- what it checks: how central the focus term is in the final IR.
- how it is computed: weighted score from top-level declaration presence, assertion-body appearance, and dependency centrality; for example a normalized score in `[0,1]`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `cost_estimate_tokens_in`
- kind: `continuous`
- what it checks: approximate prompt-token budget consumed.
- how it is computed: sum prompt-token counts from logged completions when available.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `cost_estimate_tokens_out`
- kind: `continuous`
- what it checks: approximate completion-token budget consumed.
- how it is computed: sum completion-token counts from logged completions when available.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `counterfactual_loss_count`
- kind: `hard_warning`
- what it checks: lost counterfactual semantics such as `would have been ... if ... had not occurred`.
- how it is computed: count counterfactual fragments lacking explicit counterfactual predicate or equivalent guarded representation.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Make the lost scope/exception/negation/temporal/responsibility structure explicit in IR.

### `covered_only_in_notes_count`
- kind: `hard_warning`
- what it checks: semantic fragments that appear only in notes or residual prose, not in formula or structured annotation.
- how it is computed: count coverage-audit items with status `covered_only_in_notes`.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `critic_confidence`
- kind: `comparative`
- what it checks: confidence reported by the critic for the selected variant.
- how it is computed: normalized critic confidence field or calibrated mapping from critic output.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `critic_margin`
- kind: `comparative`
- what it checks: gap between best and second-best variant according to critic ranking.
- how it is computed: if critic provides scores, subtract rank-2 score from rank-1 score; otherwise derive an ordinal margin from ranking evidence.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `critic_merge_recommended`
- kind: `comparative`
- what it checks: whether the critic thinks no single variant is fully adequate.
- how it is computed: boolean flag from critic output.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `cross_reference_dropout_count`
- kind: `hard_warning`
- what it checks: cross-referenced concepts discussed upstream but omitted from final IR.
- how it is computed: `expected cross-reference count - used cross-reference count`.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `cross_reference_usage_count`
- kind: `continuous`
- what it checks: number of related entries or cross-referenced concepts actually used in final IR.
- how it is computed: count cross-reference ids from advisory that survive into formula or accepted annotation.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `declaration_only_downgrade_flag`
- kind: `hard_warning`
- what it checks: whether a definitional clause was reduced to a bare declaration with no meaningful body.
- how it is computed: `1` when the source is definitional but the IR contains only declarations and no definitional assertion or equation.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `declaration_shape_error_count`
- kind: `continuous`
- what it checks: AST errors specifically attached to declaration nodes.
- how it is computed: count validation errors whose path begins with `ir_ast.declarations`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Fix AST/surface syntax, declaration shape, expression shape, or combined validation.

### `definition_body_present`
- kind: `continuous`
- what it checks: whether the definition includes a semantic body, not just a carrier.
- how it is computed: boolean flag based on presence of definitional assertions or body-bearing constructs.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `definitional_equation_present`
- kind: `continuous`
- what it checks: whether a value-like definition is expressed as an equation.
- how it is computed: boolean flag when the focus term appears on one side of an equality-like definition.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `dependency_link_count`
- kind: `continuous`
- what it checks: number of explicit dependency symbols or cross-entry concepts actually used in formula.
- how it is computed: count distinct dependency symbols referenced in declarations or assertions.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `dependency_link_recall`
- kind: `continuous`
- what it checks: share of expected dependency concepts that are explicitly linked in formula.
- how it is computed: `explicitly linked dependency count / expected dependency count`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `draft_variant_count`
- kind: `continuous`
- what it checks: number of concrete IR variants drafted.
- how it is computed: `len(drafter_variants)`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `duplication_suspected`
- kind: not documented in metric catalog
- what it checks: not documented
- how it is computed: not documented
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `embedded_concept_without_formula_link_count`
- kind: `hard_warning`
- what it checks: symbol names with compositional tokens such as `ExchangeOf`, `IndexUniverseRequirements`, or similar that never appear as explicit linked concepts in formula.
- how it is computed: inspect multi-token symbol names and count cases where one embedded concept is absent from the expression graph.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `exception_visibility_violation_count`
- kind: `hard_warning`
- what it checks: exceptions or exclusions that disappear or are blurred into opaque helpers.
- how it is computed: count checklist violations of `preserve_negation_scope_and_exceptions`.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Make the lost scope/exception/negation/temporal/responsibility structure explicit in IR.

### `explicit_link_violation_count`
- kind: `hard_warning`
- what it checks: cases where a symbol name embeds another concept that the formula body never links explicitly.
- how it is computed: count checklist violations of `keep_links_explicit`.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `expr_shape_error_count`
- kind: `continuous`
- what it checks: AST errors specifically attached to expression nodes.
- how it is computed: count validation errors whose path contains `.expr`, `.left`, `.right`, `.args`, `.body`, `.cond`, `.then`, or `.else`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Fix AST/surface syntax, declaration shape, expression shape, or combined validation.

### `factorization_count`
- kind: `continuous`
- what it checks: how many separate callable factors carry argument structure.
- how it is computed: count local callable symbols whose arity is greater than zero.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `factorization_index`
- kind: `continuous`
- what it checks: how fragmented the argument structure is.
- how it is computed: `factorization_count / max(1, top_level_parameter_slot_count)`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `factorization_per_clause`
- kind: `continuous`
- what it checks: how fragmented the callable structure is per normalized clause.
- how it is computed: `factorization_count / normalized_clause_count`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Check whether every normalized logic burden is represented in formula-bearing IR.

### `factorization_per_reference_token`
- kind: `continuous`
- what it checks: how fragmented the callable structure is relative to normalized token mass.
- how it is computed: `factorization_count / normalized_content_token_mass`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `failed_llm_call_count`
- kind: `continuous`
- what it checks: failed model completions.
- how it is computed: `llm_call_count - successful_llm_call_count`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `focus_signature_mode_share`
- kind: `comparative`
- what it checks: how dominant the most common focus-symbol signature is.
- how it is computed: `max(signature frequency) / usable_variant_count`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `focus_signature_mode_share_per_parameter_slot_mass`
- kind: `comparative`
- what it checks: carrier-stability bought per unit of parameter mass.
- how it is computed: `focus_signature_mode_share / total_parameter_slot_mass`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `focus_signature_unique_count`
- kind: `comparative`
- what it checks: how many different focus-symbol signatures appear across variants or reruns.
- how it is computed: extract the declared signature of the focus term, for example `rel(IndexComponent,Day)` vs `rel(Day,Exchange)`, and count unique values.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `focus_symbol_arity`
- kind: `comparative`
- what it checks: the arity chosen for the focus term itself.
- how it is computed: read the declared argument count of the focus symbol.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `focus_symbol_signature`
- kind: `comparative`
- what it checks: the effective carrier signature chosen for the focus term.
- how it is computed: inspect the declaration for the focus term and serialize it as a normalized signature, for example `rel(IndexComponent,Day)` or `fun(IndexComponent)->Exchange`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `focus_term_explicitly_modeled`
- kind: `hard_fail`
- what it checks: whether the defined term is explicit in IR rather than hidden behind helpers.
- how it is computed: `1` if the focus term appears as a top-level declaration or clearly in formula body, else `0`.
- what is wrong when it fails or looks bad: If this fails, the artifact should not be accepted.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `focus_term_in_formula_body`
- kind: `continuous`
- what it checks: whether the focus term appears in the semantic body of assertions, not only as a declaration.
- how it is computed: boolean flag over expression references and calls.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `focus_term_in_top_level_decl`
- kind: `continuous`
- what it checks: whether the focus term appears as a top-level sort/entity/symbol declaration.
- how it is computed: boolean flag over declaration names.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `formula_bearing_item_count`
- kind: `continuous`
- what it checks: number of top-level IR items that carry executable rule semantics.
- how it is computed: count assertions and any other formula-bearing IR nodes considered semantically substantive.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `formula_content_token_mass`
- kind: `continuous`
- what it checks: total multiplicity of content tokens in formal IR surface.
- how it is computed: tokenize rendered IR into content tokens and count all occurrences.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `formula_repeat_overuse_examples`
- kind: `comparative`
- what it checks: the most obviously overused content tokens in formal IR.
- how it is computed: rank tokens by `formula_count - source_count` and keep the top examples.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `formula_repeat_overuse_mass`
- kind: `hard_warning`
- what it checks: total excess repetition mass in formal IR.
- how it is computed: sum `max(0, formula_count - source_count)` over all source-licensed content tokens.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `formula_repeat_overuse_rate`
- kind: `hard_warning`
- what it checks: repetition inflation in formal IR relative to normalized token mass.
- how it is computed: `formula_repeat_overuse_mass / normalized_content_token_mass`.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `formula_repeat_overuse_token_count`
- kind: `hard_warning`
- what it checks: how many source-licensed content tokens are repeated more often in formal IR than in the source.
- how it is computed: compare content-token counters for source and formula surface, then count tokens where `formula_count > source_count`.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `formula_repeat_underuse_mass`
- kind: `continuous`
- what it checks: total missing repetition mass in formal IR.
- how it is computed: sum `max(0, source_count - formula_count)` over all source content tokens.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `formula_repeat_underuse_token_count`
- kind: `continuous`
- what it checks: how many source content tokens appear fewer times in formal IR than in the source.
- how it is computed: count tokens where `formula_count < source_count`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `formula_to_clause_compression_ratio`
- kind: `continuous`
- what it checks: how many normalized clauses are carried per formula-bearing IR item.
- how it is computed: `normalized_clause_count / max(1, formula_bearing_item_count)`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Check whether every normalized logic burden is represented in formula-bearing IR.

### `full_surface_content_token_mass`
- kind: `continuous`
- what it checks: total multiplicity of content tokens across formal IR and prose fields together.
- how it is computed: tokenize rendered IR plus prose fields and count all occurrences.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `full_surface_repeat_overuse_examples`
- kind: `comparative`
- what it checks: the strongest repetition-inflation examples anywhere in the artifact.
- how it is computed: rank tokens by `full_surface_count - source_count` and keep the top examples.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `full_surface_repeat_overuse_mass`
- kind: `hard_warning`
- what it checks: total excess repetition mass across IR plus prose.
- how it is computed: sum `max(0, full_surface_count - source_count)` over all content tokens.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `full_surface_repeat_overuse_rate`
- kind: `hard_warning`
- what it checks: repetition inflation across IR plus prose relative to normalized token mass.
- how it is computed: `full_surface_repeat_overuse_mass / normalized_content_token_mass`.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `full_surface_repeat_overuse_token_count`
- kind: `hard_warning`
- what it checks: how many content tokens are repeated more often in IR plus notes than in the source.
- how it is computed: compare source token counter with the combined counter over rendered IR and prose fields.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `gold_clause_alignment`
- kind: `gold_only`
- what it checks: fraction of gold semantic blocks aligned by the candidate IR.
- how it is computed: align candidate clause coverage map against gold clause inventory.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Check whether every normalized logic burden is represented in formula-bearing IR.

### `gold_counterfactual_recall`
- kind: `gold_only`
- what it checks: share of gold counterfactual semantics preserved.
- how it is computed: `matched gold counterfactual fragments / total gold counterfactual fragments`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Make the lost scope/exception/negation/temporal/responsibility structure explicit in IR.

### `gold_dependency_recall`
- kind: `gold_only`
- what it checks: share of explicit concept links in gold that are preserved in the candidate.
- how it is computed: `matched gold dependency links / total gold dependency links`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `gold_exception_recall`
- kind: `gold_only`
- what it checks: share of gold exclusion semantics preserved.
- how it is computed: `matched gold exception fragments / total gold exception fragments`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Make the lost scope/exception/negation/temporal/responsibility structure explicit in IR.

### `gold_helper_overuse_delta`
- kind: `gold_only`
- what it checks: how much more helper machinery the candidate introduces than the gold.
- how it is computed: `candidate helper count - gold helper count`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Split overloaded names and add structural anchors in declarations/formulas/ontology.

### `gold_modulo_renaming_match`
- kind: `gold_only`
- what it checks: whether candidate and gold are equivalent up to safe renaming and trivial formatting differences.
- how it is computed: canonicalize names and compare normalized structure.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `gold_render_similarity`
- kind: `gold_only`
- what it checks: semantic similarity between candidate render-back and gold render-back.
- how it is computed: BERTScore, NLI, or clause-aligned similarity on verbalized forms.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Compare render-back/verdict against normalized text and repair semantic drift.

### `gold_scope_recall`
- kind: `gold_only`
- what it checks: share of gold scope semantics preserved.
- how it is computed: `matched gold scope fragments / total gold scope fragments`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Make the lost scope/exception/negation/temporal/responsibility structure explicit in IR.

### `gold_structure_similarity`
- kind: `gold_only`
- what it checks: structural similarity modulo renaming between candidate IR and gold IR.
- how it is computed: compare declaration graph, assertion skeleton, and operator shapes after normalization of names.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `guard_loss_count`
- kind: `hard_warning`
- what it checks: lost guard conditions or antecedents.
- how it is computed: compare conditional source fragments against IR implication, guard predicates, or `ite` conditions.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Make the lost scope/exception/negation/temporal/responsibility structure explicit in IR.

### `helper_explosion_count`
- kind: `hard_warning`
- what it checks: excessive proliferation of helper symbols relative to source complexity.
- how it is computed: `max(0, helper_symbol_count - expected_helper_budget)` where the budget depends on clause count and role complexity.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Split overloaded names and add structural anchors in declarations/formulas/ontology.

### `identifier_count`
- kind: `continuous`
- what it checks: number of unique IR identifiers inspected by the glue analysis.
- how it is computed: collect unique declaration names, assertion names, and named references/callees from the AST.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Split overloaded names and add structural anchors in declarations/formulas/ontology.

### `identifier_glue_excess_mass_content`
- kind: `continuous`
- what it checks: total content-level over-glue mass.
- how it is computed: for each identifier, compute `max(0, content_piece_count - 2)` and sum over identifiers.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Split overloaded names and add structural anchors in declarations/formulas/ontology.

### `identifier_glue_excess_mass_raw`
- kind: `continuous`
- what it checks: total raw over-glue mass.
- how it is computed: for each identifier, compute `max(0, raw_piece_count - 3)` and sum over identifiers.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Split overloaded names and add structural anchors in declarations/formulas/ontology.

### `identifier_glue_excess_rate_content`
- kind: `continuous`
- what it checks: average content-level over-glue burden per identifier.
- how it is computed: `identifier_glue_excess_mass_content / identifier_count`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Split overloaded names and add structural anchors in declarations/formulas/ontology.

### `identifier_glue_excess_rate_raw`
- kind: `continuous`
- what it checks: average raw over-glue burden per identifier.
- how it is computed: `identifier_glue_excess_mass_raw / identifier_count`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Split overloaded names and add structural anchors in declarations/formulas/ontology.

### `invented_helper_sort_count`
- kind: `hard_warning`
- what it checks: helper sorts introduced without strong textual license.
- how it is computed: count newly declared sorts that are not direct concept names from source/advisory and are not Prelude or built-in sorts.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Check whether new symbols/tokens are licensed by source, prelude, ontology, overlay, or user hint.

### `invented_helper_symbol_count`
- kind: `hard_warning`
- what it checks: helper symbols introduced by the IR that are technically grounded by token overlap but are not justified as minimal abstractions.
- how it is computed: count declared non-focus symbols that are not in source term inventory, not in Prelude, and not referenced in clause-to-IR mapping as necessary support symbols.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Check whether new symbols/tokens are licensed by source, prelude, ontology, overlay, or user hint.

### `ir_to_source_token_gap_count`
- kind: `continuous`
- what it checks: IR-side content tokens without source, advisory, Prelude, or A4V3 support.
- how it is computed: count IR content tokens missing from the allowed vocabulary pool.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `legacy_surface_token_count`
- kind: `hard_warning`
- what it checks: presence of legacy pre-canonical surface tokens in the AST payload.
- how it is computed: count tokens such as `forall`, `implies`, `call`, `var`, `params`, `return_sort`, `totality` when they appear in forbidden legacy surface form rather than canonical node shape.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `llm_call_count`
- kind: `continuous`
- what it checks: total number of model completions in the run.
- how it is computed: count assistant/completion turns emitted by the runtime.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `logic_block_count`
- kind: `continuous`
- what it checks: number of top-level IR logic blocks.
- how it is computed: count AST assertions.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `logic_block_to_clause_ratio`
- kind: `continuous`
- what it checks: how densely the IR logic-block count tracks normalized clause count.
- how it is computed: `logic_block_count / max(1, normalized_clause_count)`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Check whether every normalized logic burden is represented in formula-bearing IR.

### `low_source_grounded_glued_identifier_count`
- kind: `hard_warning`
- what it checks: suspicious identifiers that are both long and weakly grounded in the source.
- how it is computed: count identifiers with at least 3 content pieces and source-grounded content-piece ratio below `0.67`.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Split overloaded names and add structural anchors in declarations/formulas/ontology.

### `low_source_grounded_glued_identifier_rate`
- kind: `continuous`
- what it checks: how much of the identifier inventory is simultaneously glued and weakly source-grounded.
- how it is computed: `low_source_grounded_glued_identifier_count / identifier_count`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Split overloaded names and add structural anchors in declarations/formulas/ontology.

### `lowest_source_grounded_identifiers`
- kind: `comparative`
- what it checks: identifiers whose pieces are least grounded in the source.
- how it is computed: rank identifiers by source-grounded content-piece ratio ascending, then by content-piece count descending.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Split overloaded names and add structural anchors in declarations/formulas/ontology.

### `max_assertion_depth`
- kind: `hard_warning`
- what it checks: nesting depth of the deepest assertion.
- how it is computed: recursively compute expression depth and take the maximum.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `max_assertion_node_count`
- kind: `hard_warning`
- what it checks: size of the single most complex assertion.
- how it is computed: recursively count expression nodes inside each assertion and take the maximum.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `max_branching_point_count_per_assertion`
- kind: `hard_warning`
- what it checks: worst single-assertion branching burden.
- how it is computed: compute branching-point count per assertion and take the maximum.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `max_call_latency_s`
- kind: `continuous`
- what it checks: slowest successful model completion.
- how it is computed: maximum of per-call durations.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `max_clause_collapse_size`
- kind: `hard_warning`
- what it checks: the largest number of normalized clauses collapsed into one formula-bearing item.
- how it is computed: maximum clause-to-formula fan-in over the clause-to-IR map.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Check whether every normalized logic burden is represented in formula-bearing IR.

### `max_identifier_piece_count_content`
- kind: `continuous`
- what it checks: worst-case content-piece identifier length.
- how it is computed: maximum non-stopword content-piece count across identifiers.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Split overloaded names and add structural anchors in declarations/formulas/ontology.

### `max_identifier_piece_count_raw`
- kind: `continuous`
- what it checks: worst-case raw identifier length.
- how it is computed: maximum raw split-piece count across identifiers.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Split overloaded names and add structural anchors in declarations/formulas/ontology.

### `max_ite_count_per_assertion`
- kind: `hard_warning`
- what it checks: largest number of `ite` branches inside a single assertion.
- how it is computed: recursively count `ite` nodes per assertion and take the maximum.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `mean_assertion_depth`
- kind: `continuous`
- what it checks: average nesting depth of assertion expressions.
- how it is computed: recursively compute expression depth per assertion and average.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `mean_assertion_node_count`
- kind: `continuous`
- what it checks: average expression-tree size per assertion.
- how it is computed: recursively count expression nodes inside each assertion and average.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `mean_identifier_piece_count_content`
- kind: `continuous`
- what it checks: average content-piece identifier length.
- how it is computed: mean non-stopword content-piece count across identifiers.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Split overloaded names and add structural anchors in declarations/formulas/ontology.

### `mean_identifier_piece_count_raw`
- kind: `continuous`
- what it checks: average raw identifier length.
- how it is computed: mean raw split-piece count across identifiers.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Split overloaded names and add structural anchors in declarations/formulas/ontology.

### `mean_significant_tokens_per_formula_item`
- kind: `continuous`
- what it checks: average semantic density per formula-bearing item.
- how it is computed: total significant source tokens represented formally divided by formula-bearing item count.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `missing_fragment_count`
- kind: `hard_warning`
- what it checks: semantic fragments absent from both formula and prose.
- how it is computed: count coverage-audit items with status `missing`.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Check whether every normalized logic burden is represented in formula-bearing IR.

### `multi_clause_merge_count`
- kind: `hard_warning`
- what it checks: cases where multiple normalized clauses are collapsed into a single formula-bearing item without explicit traceability.
- how it is computed: for each formula-bearing item, count how many clauses map to it; sum all excess over `1`.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Check whether every normalized logic burden is represented in formula-bearing IR.

### `named_exclusion_count`
- kind: `continuous`
- what it checks: number of exclusions represented as explicit distinct predicates or conjuncts.
- how it is computed: count exclusion-bearing constructs mapped from exclusion clauses.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `named_scope_predicate_count`
- kind: `continuous`
- what it checks: number of explicit scope predicates or guards.
- how it is computed: count distinct scope-bearing predicates, guard expressions, or annotation nodes.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Make the lost scope/exception/negation/temporal/responsibility structure explicit in IR.

### `negation_loss_count`
- kind: `hard_warning`
- what it checks: lost negative operators such as `not`, `excluding`, `unless not`, and analogous semantics.
- how it is computed: compare negation-bearing source fragments against IR and count missing negation semantics.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Make the lost scope/exception/negation/temporal/responsibility structure explicit in IR.

### `new_formula_content_token_count_vs_text_only`
- kind: `hard_warning`
- what it checks: semantically meaningful new formula tokens relative to source plus normalized text only.
- how it is computed: same as above, but remove stopwords and syntax-only tokens before counting.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Check whether new symbols/tokens are licensed by source, prelude, ontology, overlay, or user hint.

### `new_formula_content_token_rate_vs_reference_mass`
- kind: `continuous`
- what it checks: density of newly introduced content tokens in formal IR relative to normalized token mass.
- how it is computed: `new_formula_content_token_count / normalized_content_token_mass`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Check whether new symbols/tokens are licensed by source, prelude, ontology, overlay, or user hint.

### `new_formula_token_count_vs_text_only`
- kind: `continuous`
- what it checks: all new formula tokens relative to source plus normalized text only, without forgiving Prelude.
- how it is computed: tokenize rendered formula surface; subtract token set from source excerpt, source term, normalized clauses, and A4V3 syntax; count the residue.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Check whether new symbols/tokens are licensed by source, prelude, ontology, overlay, or user hint.

### `new_full_surface_content_token_count_vs_text_only`
- kind: `hard_warning`
- what it checks: semantically meaningful new tokens in rendered IR plus prose fields relative to source plus normalized text only.
- how it is computed: same as above, but remove stopwords and syntax-only tokens before counting.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Check whether new symbols/tokens are licensed by source, prelude, ontology, overlay, or user hint.

### `new_full_surface_content_token_rate_vs_reference_mass`
- kind: `continuous`
- what it checks: density of newly introduced content tokens across IR plus prose relative to normalized token mass.
- how it is computed: `new_full_surface_content_token_count / normalized_content_token_mass`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Check whether new symbols/tokens are licensed by source, prelude, ontology, overlay, or user hint.

### `new_full_surface_token_count_vs_text_only`
- kind: `continuous`
- what it checks: all new tokens in rendered IR plus prose fields relative to source plus normalized text only.
- how it is computed: tokenize formula plus prose fields; subtract token set from source excerpt, source term, normalized clauses, and A4V3 syntax; count the residue.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Check whether new symbols/tokens are licensed by source, prelude, ontology, overlay, or user hint.

### `new_surface_content_token_count`
- kind: `hard_warning`
- what it checks: semantically meaningful new tokens, excluding syntax and stopwords.
- how it is computed: same as `new_surface_token_count`, but after removing stopwords and A4V3 syntax tokens.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Check whether new symbols/tokens are licensed by source, prelude, ontology, overlay, or user hint.

### `new_surface_token_count`
- kind: `continuous`
- what it checks: all lexical tokens appearing in rendered IR or structured prose fields that do not belong to the union of source text, normalized text, advisory text, Prelude, and whitelisted A4V3 syntax.
- how it is computed: tokenize rendered IR plus prose fields; subtract token sets from source, advisory, Prelude, and A4V3 whitelist; count the residue.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Check whether new symbols/tokens are licensed by source, prelude, ontology, overlay, or user hint.

### `normalized_clause_count`
- kind: `continuous`
- what it checks: number of normalized clauses presented to IR drafting.
- how it is computed: `len(normalized_clauses)`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Review source vs normalized text for deletion, addition, repetition, or changed scope.

### `normalized_content_mass_per_clause`
- kind: `continuous`
- what it checks: average content-token mass per normalized clause.
- how it is computed: `normalized_content_token_mass / normalized_clause_count`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Review source vs normalized text for deletion, addition, repetition, or changed scope.

### `normalized_content_token_count`
- kind: `continuous`
- what it checks: distinct content tokens in normalized clauses.
- how it is computed: tokenize concatenated normalized clauses into content tokens and count unique types.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Review source vs normalized text for deletion, addition, repetition, or changed scope.

### `normalized_content_token_jaccard`
- kind: `continuous`
- what it checks: set-overlap between source content tokens and normalized content tokens.
- how it is computed: `|intersection| / |union|`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Review source vs normalized text for deletion, addition, repetition, or changed scope.

### `normalized_content_token_mass`
- kind: `continuous`
- what it checks: total multiplicity of content tokens in normalized clauses.
- how it is computed: tokenize concatenated normalized clauses into content tokens and count all occurrences.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Review source vs normalized text for deletion, addition, repetition, or changed scope.

### `normalized_content_token_multiset_precision_to_source`
- kind: `continuous`
- what it checks: how much of normalized token mass is licensed directly by source wording.
- how it is computed: multiset overlap between normalized and source token counters divided by normalized token mass.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Review source vs normalized text for deletion, addition, repetition, or changed scope.

### `normalized_content_token_multiset_recall_from_source`
- kind: `continuous`
- what it checks: how much of the source token mass survives into normalization.
- how it is computed: multiset overlap between normalized and source token counters divided by source token mass.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Review source vs normalized text for deletion, addition, repetition, or changed scope.

### `normalized_content_token_precision_to_source`
- kind: `continuous`
- what it checks: how source-grounded the normalized token inventory is.
- how it is computed: `matched normalized/source content token types / normalized content token types`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Review source vs normalized text for deletion, addition, repetition, or changed scope.

### `normalized_content_token_recall_from_source`
- kind: `continuous`
- what it checks: how much of the original source token inventory survives into normalization.
- how it is computed: `matched normalized/source content token types / source content token types`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Review source vs normalized text for deletion, addition, repetition, or changed scope.

### `normalized_implies_source_entailment`
- kind: `continuous`
- what it checks: whether normalization semantically entails the source.
- how it is computed: NLI entailment score with `premise = normalized`, `hypothesis = source`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Review source vs normalized text for deletion, addition, repetition, or changed scope.

### `normalized_length_ratio_vs_source_mass`
- kind: `continuous`
- what it checks: how much normalization expands or compresses source token mass.
- how it is computed: `normalized_content_token_mass / source_excerpt_content_token_mass`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Review source vs normalized text for deletion, addition, repetition, or changed scope.

### `normalized_repeat_overuse_examples`
- kind: `comparative`
- what it checks: top examples of normalization inflating token repetition.
- how it is computed: rank tokens by `normalized_count - source_count` and keep top examples.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Review source vs normalized text for deletion, addition, repetition, or changed scope.

### `normalized_repeat_overuse_mass`
- kind: `hard_warning`
- what it checks: total excess repetition introduced by normalization.
- how it is computed: sum `max(0, normalized_count - source_count)` over all content tokens.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Review source vs normalized text for deletion, addition, repetition, or changed scope.

### `normalized_repeat_overuse_token_count`
- kind: `hard_warning`
- what it checks: number of source-licensed content tokens repeated more often in normalization than in source.
- how it is computed: compare normalized token counter with source token counter and count tokens where `normalized_count > source_count`.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Review source vs normalized text for deletion, addition, repetition, or changed scope.

### `normalized_to_source_new_token_count`
- kind: `hard_warning`
- what it checks: distinct content tokens introduced by normalization that were not present in source.
- how it is computed: count `normalized_token_set - source_token_set`.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Review source vs normalized text for deletion, addition, repetition, or changed scope.

### `notes_content_token_count`
- kind: `hard_warning`
- what it checks: content-token mass left in prose rather than formal IR or explicit annotation nodes.
- how it is computed: tokenize prose fields, remove stopwords and syntax, and count the residue.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `notes_content_token_rate_vs_reference_mass`
- kind: `hard_warning`
- what it checks: how much content mass is parked in notes relative to normalized input size.
- how it is computed: `notes_content_token_count / normalized_content_token_mass`.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `notes_to_formula_content_ratio`
- kind: `continuous`
- what it checks: how much semantic content lives in notes relative to formula.
- how it is computed: `notes_content_token_count / max(1, formula_content_token_count)`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `notes_token_count`
- kind: `continuous`
- what it checks: total token count in prose-only fields such as rendering notes and residual risks.
- how it is computed: tokenize prose fields and count all tokens.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `opaque_support_symbol_count`
- kind: `continuous`
- what it checks: number of intentionally opaque support symbols used to preserve semantics.
- how it is computed: count helper symbols explicitly marked or inferable as support abstractions rather than primary focus symbols.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Split overloaded names and add structural anchors in declarations/formulas/ontology.

### `opaque_support_symbol_ratio`
- kind: `continuous`
- what it checks: share of support abstractions among all local declared symbols.
- how it is computed: `opaque_support_symbol_count / local_declared_symbol_count`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Split overloaded names and add structural anchors in declarations/formulas/ontology.

### `overcompressed_single_assertion_flag`
- kind: `hard_warning`
- what it checks: whether a multi-clause definition appears packed into one overly large assertion.
- how it is computed: fire when `normalized_clause_count >= 3`, `assertion_count == 1`, and the lone assertion is large/deep/branchy or uses `ite`.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `pairwise_structure_distance_mean`
- kind: `comparative`
- what it checks: mean structural drift between all pairs of variants or reruns.
- how it is computed: `1 - pairwise_structure_similarity_mean`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `pairwise_structure_similarity_mean`
- kind: `comparative`
- what it checks: mean structural similarity between all pairs of variants or reruns.
- how it is computed: compare declaration mix, logical-operator mix, and arity profile pairwise; average the pairwise cosine similarities.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `pairwise_structure_similarity_mean_per_parameter_slot_mass`
- kind: `comparative`
- what it checks: structural stability bought per unit of parameter mass.
- how it is computed: `pairwise_structure_similarity_mean / total_parameter_slot_mass`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `pairwise_token_jaccard_mean`
- kind: `comparative`
- what it checks: average lexical overlap between rendered IR artifacts.
- how it is computed: compute content-token Jaccard for every pair, then average.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `parameter_slot_mass_per_clause`
- kind: `continuous`
- what it checks: how much parameter structure the IR spends per normalized clause.
- how it is computed: `total_parameter_slot_mass / normalized_clause_count`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Check whether every normalized logic burden is represented in formula-bearing IR.

### `parameter_slot_mass_per_reference_token`
- kind: `continuous`
- what it checks: how much parameter structure the IR spends per normalized content token.
- how it is computed: `total_parameter_slot_mass / normalized_content_token_mass`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `parameter_slots_per_factor`
- kind: `continuous`
- what it checks: average argument mass per factor.
- how it is computed: `top_level_parameter_slot_count / max(1, factorization_count)`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `parse_retry_count`
- kind: `continuous`
- what it checks: how many times parsing or JSON extraction had to be retried.
- how it is computed: count parser/JSON-extraction retries before a valid candidate was accepted.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `prelude_redeclaration_count`
- kind: `hard_fail`
- what it checks: attempts to redeclare Prelude sorts, entities, or functions.
- how it is computed: count redeclaration errors raised by `_validate_symbol_origins(...)`.
- what is wrong when it fails or looks bad: If this fails, the artifact should not be accepted.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `prelude_symbol_ratio`
- kind: `continuous`
- what it checks: share of used symbols coming from Prelude or explicit built-ins.
- how it is computed: `Prelude or built-in symbol usage count / total symbol usage count`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `probe_clarification_preserved`
- kind: `hard_warning`
- what it checks: whether clarification semantics remain visible in formula or explicit annotation.
- how it is computed: targeted probe over clarification fragments.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Make the lost scope/exception/negation/temporal/responsibility structure explicit in IR.

### `probe_counterfactual_preserved`
- kind: `hard_warning`
- what it checks: whether counterfactual semantics survive targeted probing.
- how it is computed: targeted probe over counterfactual fragments such as `would have been ... if ... had not occurred`.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Make the lost scope/exception/negation/temporal/responsibility structure explicit in IR.

### `probe_exception_preserved`
- kind: `hard_warning`
- what it checks: whether exclusion clauses survive targeted probing.
- how it is computed: targeted probe over exclusion fragments.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Make the lost scope/exception/negation/temporal/responsibility structure explicit in IR.

### `probe_negation_preserved`
- kind: `hard_warning`
- what it checks: whether negative force survives targeted probing.
- how it is computed: targeted probe over negation-bearing fragments.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Make the lost scope/exception/negation/temporal/responsibility structure explicit in IR.

### `probe_reference_preserved`
- kind: `hard_warning`
- what it checks: whether external reference semantics such as `as defined in Section X` survive.
- how it is computed: targeted probe over reference-bearing fragments.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `probe_responsibility_preserved`
- kind: `hard_warning`
- what it checks: whether responsibility or authority semantics remain visible where required.
- how it is computed: targeted probe over responsibility fragments.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Make the lost scope/exception/negation/temporal/responsibility structure explicit in IR.

### `probe_scope_preserved`
- kind: `hard_warning`
- what it checks: whether scope semantics survive targeted probing.
- how it is computed: ask a targeted classifier or rule-based probe whether the scope condition in normalized text is present in IR or render-back.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Make the lost scope/exception/negation/temporal/responsibility structure explicit in IR.

### `probe_temporal_order_preserved`
- kind: `hard_warning`
- what it checks: whether temporal ordering survives, for example `immediately following`, `preceding`, `after`.
- how it is computed: targeted probe over temporal-order fragments.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Make the lost scope/exception/negation/temporal/responsibility structure explicit in IR.

### `probe_value_source_preserved`
- kind: `hard_warning`
- what it checks: whether value-source semantics such as `most recent published price` or `as sourced from data vendors` survive where intended.
- how it is computed: targeted probe over value-source fragments.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `procedural_note_leak_count`
- kind: `continuous`
- what it checks: procedural or governance material left as plain prose rather than structured residual annotations.
- how it is computed: count responsibility or governance fragments whose only representation is free prose.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `prose_leak_count`
- kind: `hard_warning`
- what it checks: clause-sized semantic fragments left only in prose after stopword filtering.
- how it is computed: count `covered_only_in_notes` or `missing` fragments whose significant-token count exceeds the chosen threshold.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Check whether every normalized logic burden is represented in formula-bearing IR.

### `quantifier_loss_count`
- kind: `hard_warning`
- what it checks: lost universal or existential force.
- how it is computed: compare quantification cues like `each`, `every`, `all`, `exists`, `for any` against quantifier structure in IR.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Make the lost scope/exception/negation/temporal/responsibility structure explicit in IR.

### `quantifier_parameter_slot_count`
- kind: `continuous`
- what it checks: total bound-variable slots introduced by quantifiers.
- how it is computed: recursively count variables introduced by `forall` and `exists` nodes in assertions.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Make the lost scope/exception/negation/temporal/responsibility structure explicit in IR.

### `reflexive_equality_count`
- kind: `hard_warning`
- what it checks: number of equality assertions whose left and right normalized forms are identical.
- how it is computed: count equality nodes whose rendered operands match modulo whitespace and trivial renaming.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `render_back_available`
- kind: `continuous`
- what it checks: whether a verbalized natural-language rendering of the IR exists.
- how it is computed: boolean flag set when the render-back stage succeeds.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Compare render-back/verdict against normalized text and repair semantic drift.

### `render_back_clause_count`
- kind: `continuous`
- what it checks: number of natural-language blocks in the render-back.
- how it is computed: count render-back sentences or blocks aligned to IR assertions and annotations.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Compare render-back/verdict against normalized text and repair semantic drift.

### `render_bertscore_f1_to_normalized`
- kind: `continuous`
- what it checks: semantic similarity between render-back text and normalized clauses.
- how it is computed: BERTScore F1 between concatenated render-back and concatenated normalized clauses.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Review source vs normalized text for deletion, addition, repetition, or changed scope.

### `render_bertscore_f1_to_normalized_per_formula_repeat_overuse_mass`
- kind: `comparative`
- what it checks: normalized-text similarity per unit of repetition inflation inside formal IR.
- how it is computed: `render_bertscore_f1_to_normalized / formula_repeat_overuse_mass`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Review source vs normalized text for deletion, addition, repetition, or changed scope.

### `render_bertscore_f1_to_normalized_per_parameter_slot_mass`
- kind: `comparative`
- what it checks: normalized-text similarity divided by parameter mass.
- how it is computed: `render_bertscore_f1_to_normalized / total_parameter_slot_mass`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Review source vs normalized text for deletion, addition, repetition, or changed scope.

### `render_bertscore_f1_to_source`
- kind: `continuous`
- what it checks: semantic similarity between render-back text and original source excerpt.
- how it is computed: BERTScore F1 between render-back and source excerpt.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Compare render-back/verdict against normalized text and repair semantic drift.

### `render_content_token_precision`
- kind: `continuous`
- what it checks: how much of the render-back’s content-token mass is licensed by normalized text.
- how it is computed: overlap between render-back content tokens and normalized content tokens divided by total render-back content tokens.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Compare render-back/verdict against normalized text and repair semantic drift.

### `render_content_token_recall`
- kind: `continuous`
- what it checks: how many normalized-text content tokens reappear in IR render-back.
- how it is computed: token overlap between render-back and normalized clauses.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Compare render-back/verdict against normalized text and repair semantic drift.

### `render_contradiction_score`
- kind: `hard_warning`
- what it checks: probability or score that render-back contradicts normalized text.
- how it is computed: contradiction output from NLI model.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Compare render-back/verdict against normalized text and repair semantic drift.

### `render_nli_ir_implies_text`
- kind: `continuous`
- what it checks: whether the render-back semantically entails the normalized text.
- how it is computed: NLI model score for `premise = render-back`, `hypothesis = normalized text`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Compare render-back/verdict against normalized text and repair semantic drift.

### `render_nli_ir_implies_text_per_parameter_slot_mass`
- kind: `comparative`
- what it checks: entailment from IR render-back to normalized text per unit of parameter mass.
- how it is computed: `render_nli_ir_implies_text / total_parameter_slot_mass`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Compare render-back/verdict against normalized text and repair semantic drift.

### `render_nli_text_implies_ir`
- kind: `continuous`
- what it checks: whether the normalized text semantically entails the render-back.
- how it is computed: NLI model score for `premise = normalized text`, `hypothesis = render-back`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Compare render-back/verdict against normalized text and repair semantic drift.

### `render_nli_text_implies_ir_per_formula_repeat_overuse_mass`
- kind: `comparative`
- what it checks: semantic adequacy per unit of formal repetition inflation.
- how it is computed: `render_nli_text_implies_ir / formula_repeat_overuse_mass`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Compare render-back/verdict against normalized text and repair semantic drift.

### `render_nli_text_implies_ir_per_full_surface_repeat_overuse_mass`
- kind: `comparative`
- what it checks: semantic adequacy per unit of repetition inflation across IR plus prose.
- how it is computed: `render_nli_text_implies_ir / full_surface_repeat_overuse_mass`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Compare render-back/verdict against normalized text and repair semantic drift.

### `render_nli_text_implies_ir_per_parameter_slot_mass`
- kind: `comparative`
- what it checks: entailment from normalized text back to IR render-back per unit of parameter mass.
- how it is computed: `render_nli_text_implies_ir / total_parameter_slot_mass`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Compare render-back/verdict against normalized text and repair semantic drift.

### `render_similarity_threshold_pass`
- kind: `hard_warning`
- what it checks: whether render-back similarity passes the configured threshold.
- how it is computed: boolean over chosen threshold on BERTScore, NLI, or hybrid render-alignment score.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Compare render-back/verdict against normalized text and repair semantic drift.

### `render_threshold`
- kind: not documented in metric catalog
- what it checks: not documented
- how it is computed: not documented
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Compare render-back/verdict against normalized text and repair semantic drift.

### `rendering_ok`
- kind: `hard_fail`
- what it checks: whether the renderer produced IR text from the AST without renderer failure.
- how it is computed: `1` if `rendering_status == "rendered_from_ast"`, else `0`.
- what is wrong when it fails or looks bad: If this fails, the artifact should not be accepted.
- likely action: Compare render-back/verdict against normalized text and repair semantic drift.

### `repair_calls_count`
- kind: `continuous`
- what it checks: number of completions spent on repair rather than first-pass generation.
- how it is computed: count completion calls tied to validator or critic repair prompts.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `responsibility_loss_count`
- kind: `hard_warning`
- what it checks: responsibility, governance, or authority clauses omitted entirely when the modeling policy expects them to remain visible.
- how it is computed: count responsibility fragments absent from IR or structured annotation layer.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Make the lost scope/exception/negation/temporal/responsibility structure explicit in IR.

### `same_parameter_mass_different_structure_pair_count`
- kind: `comparative`
- what it checks: how often two artifacts have the same total parameter mass but different structure.
- how it is computed: among all pairs, count those with equal `total_parameter_slot_mass` but non-identical structural signature.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `same_parameter_mass_different_structure_pair_ratio`
- kind: `comparative`
- what it checks: rate of decomposition drift after controlling for parameter mass.
- how it is computed: `same_parameter_mass_different_structure_pair_count / total_pair_count`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `schema_repair_round_count`
- kind: `continuous`
- what it checks: how many times the drafter needed repair prompts to satisfy schema requirements.
- how it is computed: count repair iterations triggered by AST or schema validation failure.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `scope_visibility_violation_count`
- kind: `hard_warning`
- what it checks: scope restrictions that are lost, blurred, or pushed into symbol names only.
- how it is computed: count checklist or coverage findings where scope text is not visible in formula or accepted annotation nodes.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Make the lost scope/exception/negation/temporal/responsibility structure explicit in IR.

### `semantic_coverage_retry_count`
- kind: `continuous`
- what it checks: how many times semantic coverage hints forced a retry.
- how it is computed: count semantic-coverage-triggered repair rounds.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Compare render-back/verdict against normalized text and repair semantic drift.

### `single_assertion_logic_share`
- kind: `continuous`
- what it checks: how much of all assertion logic mass lives in the largest single assertion.
- how it is computed: `max_assertion_node_count / total_assertion_node_count`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `sort_choice_stability`
- kind: `comparative`
- what it checks: whether different variants agree on sorts for the same argument positions.
- how it is computed: compare argument-sort tuples across variants; report agreement ratio.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `source_content_token_mass`
- kind: `continuous`
- what it checks: total multiplicity of content tokens in the source text, not just distinct token types.
- how it is computed: tokenize normalized text into content tokens and count all occurrences.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `source_excerpt_content_token_count`
- kind: `continuous`
- what it checks: distinct source-side content tokens in the original source excerpt.
- how it is computed: tokenize source excerpt into content tokens and count unique types.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `source_excerpt_content_token_mass`
- kind: `continuous`
- what it checks: total multiplicity of content tokens in the original source excerpt.
- how it is computed: tokenize source excerpt into content tokens and count all occurrences.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `source_grounded_content_piece_ratio_mean`
- kind: `continuous`
- what it checks: how grounded identifier pieces are in source text, normalized text, and Prelude vocabulary.
- how it is computed: for each identifier, compute the share of content pieces found in the source-side lexicon; then average across identifiers.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `source_implies_normalized_entailment`
- kind: `continuous`
- what it checks: whether the source semantically entails the normalization.
- how it is computed: NLI entailment score with `premise = source`, `hypothesis = normalized`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Review source vs normalized text for deletion, addition, repetition, or changed scope.

### `source_normalized_bertscore_f1`
- kind: `continuous`
- what it checks: semantic similarity between original source excerpt and normalized clauses.
- how it is computed: BERTScore F1 between concatenated normalized clauses and source excerpt.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Review source vs normalized text for deletion, addition, repetition, or changed scope.

### `source_to_ir_token_gap_count`
- kind: `continuous`
- what it checks: source-side content tokens missing from IR surface.
- how it is computed: count source content tokens absent from rendered IR and accepted annotation nodes.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `source_to_normalized_token_gap_count`
- kind: `hard_warning`
- what it checks: distinct source content tokens that normalization dropped completely.
- how it is computed: count `source_token_set - normalized_token_set`.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Review source vs normalized text for deletion, addition, repetition, or changed scope.

### `source_vs_normalized_contradiction_score`
- kind: `hard_warning`
- what it checks: contradiction risk between source and normalization.
- how it is computed: take the max contradiction score from the two NLI directions.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Review source vs normalized text for deletion, addition, repetition, or changed scope.

### `successful_llm_call_count`
- kind: `continuous`
- what it checks: successful model completions.
- how it is computed: count completion calls that returned valid responses.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `support_only_clause_count`
- kind: `continuous`
- what it checks: number of clauses explicitly marked support-only.
- how it is computed: count normalized clauses whose role is classified as support-only or whose coverage record says they are intentionally non-formula-bearing.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Check whether every normalized logic burden is represented in formula-bearing IR.

### `support_only_clause_ratio`
- kind: `continuous`
- what it checks: share of all normalized clauses treated as support-only.
- how it is computed: `support_only_clause_count / normalized_clause_count`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Check whether every normalized logic burden is represented in formula-bearing IR.

### `symbol_grounding_hard_finding_count`
- kind: not documented in metric catalog
- what it checks: not documented
- how it is computed: not documented
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `temporal_link_loss_count`
- kind: `hard_warning`
- what it checks: lost temporal relations such as `immediately following`, `preceding`, `after`, `before`.
- how it is computed: count temporal source fragments not mapped into explicit temporal predicates, functions, or annotations.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Make the lost scope/exception/negation/temporal/responsibility structure explicit in IR.

### `text_licensed_symbol_ratio`
- kind: `continuous`
- what it checks: share of declared local symbols that can be grounded directly in source or normalized text.
- how it is computed: `text-grounded local symbol count / total local symbol count`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `threshold`
- kind: not documented in metric catalog
- what it checks: not documented
- how it is computed: not documented
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `timeout_count`
- kind: `continuous`
- what it checks: number of model or network calls that failed by timeout.
- how it is computed: count logged timeout exceptions.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `top_complex_assertions`
- kind: `comparative`
- what it checks: the most structurally complex assertions in the artifact.
- how it is computed: rank assertions by node count, depth, then branching-point count.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `top_glued_identifiers`
- kind: `comparative`
- what it checks: the most over-glued identifiers in the artifact.
- how it is computed: rank identifiers by content glue excess, then raw glue excess, then low source-groundedness.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Split overloaded names and add structural anchors in declarations/formulas/ontology.

### `top_level_parameter_slot_count`
- kind: `continuous`
- what it checks: total argument slots declared at symbol level.
- how it is computed: sum the arities of all local `fun` and `rel` declarations.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `total_assertion_node_count`
- kind: `continuous`
- what it checks: total logic mass across all assertions.
- how it is computed: sum expression-node counts over assertions.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `total_branching_point_count`
- kind: `continuous`
- what it checks: total branching burden in the logic.
- how it is computed: sum branch contributions from `and/or` fanout, `ite`, and multi-variable quantifier binders.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `total_connective_count`
- kind: `continuous`
- what it checks: total number of logical connectives such as `and`, `or`, `not`, `implies`, `iff`.
- how it is computed: recursively count logical connective nodes across assertions.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `total_ite_count`
- kind: `hard_warning`
- what it checks: total number of explicit `ite` branches in the IR.
- how it is computed: recursively count `ite` nodes across assertions.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `total_parameter_slot_mass`
- kind: `continuous`
- what it checks: total parameter burden of the artifact, independent of how it is factorized.
- how it is computed: `top_level_parameter_slot_count + quantifier_parameter_slot_count`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `total_quantifier_count`
- kind: `continuous`
- what it checks: total number of quantifier nodes in assertions.
- how it is computed: recursively count `forall` and `exists` nodes.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Make the lost scope/exception/negation/temporal/responsibility structure explicit in IR.

### `uncovered_clause_count`
- kind: `hard_warning`
- what it checks: normalized clauses that are not represented in formula, annotation, or accepted residual structure.
- how it is computed: `normalized_clause_count - covered_clause_count`.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Check whether every normalized logic burden is represented in formula-bearing IR.

### `underdecomposed_logic_flag`
- kind: `hard_warning`
- what it checks: whether a multi-clause normalized definition has been collapsed into too few logic blocks and one dominant assertion.
- how it is computed: fire when `normalized_clause_count >= 3`, `logic_block_count <= 1`, and `overcompressed_single_assertion_flag = 1`.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `ungrounded_callee_count`
- kind: `hard_fail`
- what it checks: callee names used in calls that are not declared, Prelude, or whitelisted A4V3 builtins.
- how it is computed: count callee-origin failures from `_validate_expr_symbol_origins(...)`.
- what is wrong when it fails or looks bad: If this fails, the artifact should not be accepted.
- likely action: Check whether new symbols/tokens are licensed by source, prelude, ontology, overlay, or user hint.

### `ungrounded_ref_count`
- kind: `hard_fail`
- what it checks: expression references that are not locally bound, declared, or grounded.
- how it is computed: count ref-origin failures from `_validate_expr_symbol_origins(...)`.
- what is wrong when it fails or looks bad: If this fails, the artifact should not be accepted.
- likely action: Check whether new symbols/tokens are licensed by source, prelude, ontology, overlay, or user hint.

### `ungrounded_sort_count`
- kind: `hard_fail`
- what it checks: sort names that are neither Prelude, built-in, locally declared, nor text/advisory grounded.
- how it is computed: count sort-origin validation failures.
- what is wrong when it fails or looks bad: If this fails, the artifact should not be accepted.
- likely action: Check whether new symbols/tokens are licensed by source, prelude, ontology, overlay, or user hint.

### `ungrounded_symbol_count`
- kind: `hard_fail`
- what it checks: symbols declared in IR that are not grounded in source, advisory, Prelude, or built-in A4V3 vocabulary.
- how it is computed: count `symbol` declaration errors emitted by `_validate_symbol_origins(...)`.
- what is wrong when it fails or looks bad: If this fails, the artifact should not be accepted.
- likely action: Check whether new symbols/tokens are licensed by source, prelude, ontology, overlay, or user hint.

### `unique_ir_variant_count`
- kind: `comparative`
- what it checks: number of materially distinct IR variants.
- how it is computed: cluster variants by normalized carrier, focus symbol signature, and formula skeleton; count clusters.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `unique_variant_signature_count`
- kind: `comparative`
- what it checks: how many materially distinct IR outputs appear inside one run.
- how it is computed: normalize rendered IR strings and count distinct values, or cluster by structural signature.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `usable_variant_count`
- kind: `comparative`
- what it checks: number of drafted variants that are actually usable for comparison.
- how it is computed: count variants with `status = ok`, canonical AST, and non-empty rendered IR.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `vacuous_constraint_flag`
- kind: `hard_warning`
- what it checks: whether a constraint is tautological or semantically empty.
- how it is computed: `1` for reflexive equalities such as `Exchange(x) = Exchange(x)` or other trivially true shells.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `variant_diversity_score`
- kind: `comparative`
- what it checks: how different the variants really are.
- how it is computed: average pairwise structural distance across variants.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `wall_clock_seconds`
- kind: `continuous`
- what it checks: end-to-end runtime for the entry.
- how it is computed: run end time minus run start time.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

## Checks
### `accepted`
- what it checks: Acceptance policy check.
- what is wrong when it fails: The artifact does not satisfy the requested acceptance level.
- likely action: Repair blockers or classify as soft_review/needs_review.

### `avoid_padding_or_repetition`
- what it checks: Checks that normalized text does not add filler or duplicated content.
- what is wrong when it fails: Normalization repeats or strengthens content without need.
- likely action: Remove padding; keep repetition only when it exposes structure.

### `canonical_subterm_reuse_candidates`
- what it checks: Declaration/ontology/identifier lint finding.
- what is wrong when it fails: The declaration layer or naming shape may be unsafe.
- likely action: Review lint details, then split, bridge, rename, or waive with provenance.

### `canonical_subterm_reuse_gap`
- what it checks: Declaration/ontology/identifier lint finding.
- what is wrong when it fails: The declaration layer or naming shape may be unsafe.
- likely action: Review lint details, then split, bridge, rename, or waive with provenance.

### `codomain_split_value_families`
- what it checks: Declaration/ontology/identifier lint finding.
- what is wrong when it fails: The declaration layer or naming shape may be unsafe.
- likely action: Review lint details, then split, bridge, rename, or waive with provenance.

### `combined_validation_ok_acceptance_gate`
- what it checks: Acceptance policy check.
- what is wrong when it fails: The artifact does not satisfy the requested acceptance level.
- likely action: Repair blockers or classify as soft_review/needs_review.

### `composite_identifier_crosslink_candidates`
- what it checks: Declaration/ontology/identifier lint finding.
- what is wrong when it fails: The declaration layer or naming shape may be unsafe.
- likely action: Review lint details, then split, bridge, rename, or waive with provenance.

### `composite_identifier_crosslink_gap`
- what it checks: Declaration/ontology/identifier lint finding.
- what is wrong when it fails: The declaration layer or naming shape may be unsafe.
- likely action: Review lint details, then split, bridge, rename, or waive with provenance.

### `cover_every_normalized_block`
- what it checks: IR checklist or validator check.
- what is wrong when it fails: The IR does not preserve a required normalized-text property.
- likely action: Repair IR structure and rerun checks.

### `declaration_hard_issue_count_gate`
- what it checks: Acceptance policy check.
- what is wrong when it fails: The artifact does not satisfy the requested acceptance level.
- likely action: Repair blockers or classify as soft_review/needs_review.

### `decomposition_policy_candidates`
- what it checks: Declaration/ontology/identifier lint finding.
- what is wrong when it fails: The declaration layer or naming shape may be unsafe.
- likely action: Review lint details, then split, bridge, rename, or waive with provenance.

### `decomposition_policy_gap`
- what it checks: Declaration/ontology/identifier lint finding.
- what is wrong when it fails: The declaration layer or naming shape may be unsafe.
- likely action: Review lint details, then split, bridge, rename, or waive with provenance.

### `definition_role_alignment_failed`
- what it checks: Normalization validator code.
- what is wrong when it fails: The source-to-normalized transformation is not faithful enough.
- likely action: Repair normalized text or document the decision.

### `draft_ir_parse_failed`
- what it checks: IR checklist or validator check.
- what is wrong when it fails: The IR does not preserve a required normalized-text property.
- likely action: Repair IR structure and rerun checks.

### `draft_ir_validation_failed`
- what it checks: IR checklist or validator check.
- what is wrong when it fails: The IR does not preserve a required normalized-text property.
- likely action: Repair IR structure and rerun checks.

### `enum_value_mapping_candidates`
- what it checks: Declaration/ontology/identifier lint finding.
- what is wrong when it fails: The declaration layer or naming shape may be unsafe.
- likely action: Review lint details, then split, bridge, rename, or waive with provenance.

### `formula_item_count_below_normalized_clause_count`
- what it checks: IR checklist or validator check.
- what is wrong when it fails: The IR does not preserve a required normalized-text property.
- likely action: Repair IR structure and rerun checks.

### `hard_structural_issue_count_gate`
- what it checks: Acceptance policy check.
- what is wrong when it fails: The artifact does not satisfy the requested acceptance level.
- likely action: Repair blockers or classify as soft_review/needs_review.

### `identifier_source_lexical_crosslink_candidates`
- what it checks: Declaration/ontology/identifier lint finding.
- what is wrong when it fails: The declaration layer or naming shape may be unsafe.
- likely action: Review lint details, then split, bridge, rename, or waive with provenance.

### `identifier_source_lexical_crosslink_gap`
- what it checks: Declaration/ontology/identifier lint finding.
- what is wrong when it fails: The declaration layer or naming shape may be unsafe.
- likely action: Review lint details, then split, bridge, rename, or waive with provenance.

### `invalid_surface_correction`
- what it checks: Normalization validator code.
- what is wrong when it fails: The source-to-normalized transformation is not faithful enough.
- likely action: Repair normalized text or document the decision.

### `keep_clause_boundaries_honest`
- what it checks: Checks that clause splitting preserves conditions and exceptions.
- what is wrong when it fails: Scope or exception was buried during splitting.
- likely action: Split again or repeat the needed scope explicitly.

### `keep_grounding_auditable`
- what it checks: IR checklist or validator check.
- what is wrong when it fails: The IR does not preserve a required normalized-text property.
- likely action: Repair IR structure and rerun checks.

### `keep_links_explicit`
- what it checks: IR checklist or validator check.
- what is wrong when it fails: The IR does not preserve a required normalized-text property.
- likely action: Repair IR structure and rerun checks.

### `keep_render_back_close_to_normalized_text`
- what it checks: IR checklist or validator check.
- what is wrong when it fails: The IR does not preserve a required normalized-text property.
- likely action: Repair IR structure and rerun checks.

### `keep_unresolved_ambiguity_visible`
- what it checks: Checks that vague source text stays appropriately cautious.
- what is wrong when it fails: Normalization guessed a certainty not in source.
- likely action: Restore ambiguity or record a user clarification.

### `lexical_preservation_below_threshold`
- what it checks: Normalization validator code.
- what is wrong when it fails: The source-to-normalized transformation is not faithful enough.
- likely action: Repair normalized text or document the decision.

### `make_edits_explicit`
- what it checks: Checks that typo/casing/punctuation fixes are recorded.
- what is wrong when it fails: A surface repair is hidden and not auditable.
- likely action: Add a correction note or avoid the silent edit.

### `missing_render_targets`
- what it checks: IR checklist or validator check.
- what is wrong when it fails: The IR does not preserve a required normalized-text property.
- likely action: Repair IR structure and rerun checks.

### `needs_review`
- what it checks: Acceptance policy check.
- what is wrong when it fails: The artifact does not satisfy the requested acceptance level.
- likely action: Repair blockers or classify as soft_review/needs_review.

### `normalization_duplicate_content_repetition`
- what it checks: Normalization validator code.
- what is wrong when it fails: The source-to-normalized transformation is not faithful enough.
- likely action: Repair normalized text or document the decision.

### `numeric_window_fusion_forbidden`
- what it checks: Declaration/ontology/identifier lint finding.
- what is wrong when it fails: The declaration layer or naming shape may be unsafe.
- likely action: Review lint details, then split, bridge, rename, or waive with provenance.

### `ontology_level_mixing`
- what it checks: Declaration/ontology/identifier lint finding.
- what is wrong when it fails: The declaration layer or naming shape may be unsafe.
- likely action: Review lint details, then split, bridge, rename, or waive with provenance.

### `opaque_helper_predicates`
- what it checks: Declaration/ontology/identifier lint finding.
- what is wrong when it fails: The declaration layer or naming shape may be unsafe.
- likely action: Review lint details, then split, bridge, rename, or waive with provenance.

### `overlay_consistency_drift`
- what it checks: Declaration/ontology/identifier lint finding.
- what is wrong when it fails: The declaration layer or naming shape may be unsafe.
- likely action: Review lint details, then split, bridge, rename, or waive with provenance.

### `preserve_meaning`
- what it checks: Checks that normalization keeps actors, conditions, numbers, exceptions, and obligations.
- what is wrong when it fails: Meaning disappeared or appeared during normalization.
- likely action: Restore missing source content or remove invented content.

### `preserve_negation_scope_and_exceptions`
- what it checks: IR checklist or validator check.
- what is wrong when it fails: The IR does not preserve a required normalized-text property.
- likely action: Repair IR structure and rerun checks.

### `quality_issue_count_gate`
- what it checks: Acceptance policy check.
- what is wrong when it fails: The artifact does not satisfy the requested acceptance level.
- likely action: Repair blockers or classify as soft_review/needs_review.

### `render_alignment_below_threshold`
- what it checks: IR checklist or validator check.
- what is wrong when it fails: The IR does not preserve a required normalized-text property.
- likely action: Repair IR structure and rerun checks.

### `same_symbol_different_codomains`
- what it checks: Declaration/ontology/identifier lint finding.
- what is wrong when it fails: The declaration layer or naming shape may be unsafe.
- likely action: Review lint details, then split, bridge, rename, or waive with provenance.

### `semantic_load_in_name`
- what it checks: Declaration/ontology/identifier lint finding.
- what is wrong when it fails: The declaration layer or naming shape may be unsafe.
- likely action: Review lint details, then split, bridge, rename, or waive with provenance.

### `shared_base_phrase_family_candidates`
- what it checks: Declaration/ontology/identifier lint finding.
- what is wrong when it fails: The declaration layer or naming shape may be unsafe.
- likely action: Review lint details, then split, bridge, rename, or waive with provenance.

### `silent_addition`
- what it checks: Validator code for content added without source support.
- what is wrong when it fails: New meaning was introduced.
- likely action: Remove the invention or record ontology/user-hint provenance.

### `silent_deletion`
- what it checks: Validator code for source content missing after transformation.
- what is wrong when it fails: Important source content was dropped.
- likely action: Restore the deleted content or document why it is intentionally excluded.

### `soft_review`
- what it checks: Acceptance policy check.
- what is wrong when it fails: The artifact does not satisfy the requested acceptance level.
- likely action: Repair blockers or classify as soft_review/needs_review.

### `source_phrase_identifier_crosslink_candidates`
- what it checks: Declaration/ontology/identifier lint finding.
- what is wrong when it fails: The declaration layer or naming shape may be unsafe.
- likely action: Review lint details, then split, bridge, rename, or waive with provenance.

### `source_phrase_identifier_crosslink_gap`
- what it checks: Declaration/ontology/identifier lint finding.
- what is wrong when it fails: The declaration layer or naming shape may be unsafe.
- likely action: Review lint details, then split, bridge, rename, or waive with provenance.

### `symbol_name_embeds_concept_without_explicit_link`
- what it checks: IR checklist or validator check.
- what is wrong when it fails: The IR does not preserve a required normalized-text property.
- likely action: Repair IR structure and rerun checks.

### `symbol_name_embeds_entity_without_explicit_link`
- what it checks: IR checklist or validator check.
- what is wrong when it fails: The IR does not preserve a required normalized-text property.
- likely action: Repair IR structure and rerun checks.

### `use_valid_ir_surface_forms`
- what it checks: IR checklist or validator check.
- what is wrong when it fails: The IR does not preserve a required normalized-text property.
- likely action: Repair IR structure and rerun checks.
