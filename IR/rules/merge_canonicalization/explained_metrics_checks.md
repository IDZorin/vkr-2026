# Explained Metrics and Checks: merge_canonicalization

Metric count: 63
Check count: 24

## Metrics
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

### `avg_structure_similarity_to_other_successful_runs`
- kind: `comparative`
- what it checks: how close the current artifact is to the rest of the successful cohort.
- how it is computed: for the chosen artifact, compute mean structure similarity to every other successful artifact in the cohort.
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

### `embedded_concept_without_formula_link_count`
- kind: `hard_warning`
- what it checks: symbol names with compositional tokens such as `ExchangeOf`, `IndexUniverseRequirements`, or similar that never appear as explicit linked concepts in formula.
- how it is computed: inspect multi-token symbol names and count cases where one embedded concept is absent from the expression graph.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `explicit_link_violation_count`
- kind: `hard_warning`
- what it checks: cases where a symbol name embeds another concept that the formula body never links explicitly.
- how it is computed: count checklist violations of `keep_links_explicit`.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

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

### `llm_bertscore`
- kind: not documented in metric catalog
- what it checks: not documented
- how it is computed: not documented
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `llm_contradiction`
- kind: not documented in metric catalog
- what it checks: not documented
- how it is computed: not documented
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Compare render-back/verdict against normalized text and repair semantic drift.

### `llm_ir_to_text`
- kind: not documented in metric catalog
- what it checks: not documented
- how it is computed: not documented
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `llm_text_to_ir`
- kind: not documented in metric catalog
- what it checks: not documented
- how it is computed: not documented
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
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

### `parameter_slots_per_factor`
- kind: `continuous`
- what it checks: average argument mass per factor.
- how it is computed: `top_level_parameter_slot_count / max(1, factorization_count)`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `quantifier_parameter_slot_count`
- kind: `continuous`
- what it checks: total bound-variable slots introduced by quantifiers.
- how it is computed: recursively count variables introduced by `forall` and `exists` nodes in assertions.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Make the lost scope/exception/negation/temporal/responsibility structure explicit in IR.

### `relation_type`
- kind: not documented in metric catalog
- what it checks: not documented
- how it is computed: not documented
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

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

### `render_nli_ir_implies_text_per_parameter_slot_mass`
- kind: `comparative`
- what it checks: entailment from IR render-back to normalized text per unit of parameter mass.
- how it is computed: `render_nli_ir_implies_text / total_parameter_slot_mass`.
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

### `semantic_coverage_retry_count`
- kind: `continuous`
- what it checks: how many times semantic coverage hints forced a retry.
- how it is computed: count semantic-coverage-triggered repair rounds.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Compare render-back/verdict against normalized text and repair semantic drift.

### `semantic_verdict`
- kind: not documented in metric catalog
- what it checks: not documented
- how it is computed: not documented
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Compare render-back/verdict against normalized text and repair semantic drift.

### `sort_choice_stability`
- kind: `comparative`
- what it checks: whether different variants agree on sorts for the same argument positions.
- how it is computed: compare argument-sort tuples across variants; report agreement ratio.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `top_level_parameter_slot_count`
- kind: `continuous`
- what it checks: total argument slots declared at symbol level.
- how it is computed: sum the arities of all local `fun` and `rel` declarations.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `total_parameter_slot_mass`
- kind: `continuous`
- what it checks: total parameter burden of the artifact, independent of how it is factorized.
- how it is computed: `top_level_parameter_slot_count + quantifier_parameter_slot_count`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

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

### `variant_diversity_score`
- kind: `comparative`
- what it checks: how different the variants really are.
- how it is computed: average pairwise structural distance across variants.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

## Checks
### `bridge_family`
- what it checks: Merge/canonicalization check.
- what is wrong when it fails: The merge may lose provenance, flatten distinctions, or regress quality.
- likely action: Use overlay, bridge, conflict split, or backtest before accepting.

### `bridge_supertype`
- what it checks: Merge/canonicalization check.
- what is wrong when it fails: The merge may lose provenance, flatten distinctions, or regress quality.
- likely action: Use overlay, bridge, conflict split, or backtest before accepting.

### `codomain_split_value_families`
- what it checks: Declaration/ontology/identifier lint finding.
- what is wrong when it fails: The declaration layer or naming shape may be unsafe.
- likely action: Review lint details, then split, bridge, rename, or waive with provenance.

### `conflict_split`
- what it checks: Merge/canonicalization check.
- what is wrong when it fails: The merge may lose provenance, flatten distinctions, or regress quality.
- likely action: Use overlay, bridge, conflict split, or backtest before accepting.

### `enum_value_mapping_candidates`
- what it checks: Declaration/ontology/identifier lint finding.
- what is wrong when it fails: The declaration layer or naming shape may be unsafe.
- likely action: Review lint details, then split, bridge, rename, or waive with provenance.

### `exact_merge_overlay`
- what it checks: Merge/canonicalization check.
- what is wrong when it fails: The merge may lose provenance, flatten distinctions, or regress quality.
- likely action: Use overlay, bridge, conflict split, or backtest before accepting.

### `higher_is_better_within_tolerance`
- what it checks: Merge/canonicalization check.
- what is wrong when it fails: The merge may lose provenance, flatten distinctions, or regress quality.
- likely action: Use overlay, bridge, conflict split, or backtest before accepting.

### `identifier_glue_metrics`
- what it checks: Merge/canonicalization check.
- what is wrong when it fails: The merge may lose provenance, flatten distinctions, or regress quality.
- likely action: Use overlay, bridge, conflict split, or backtest before accepting.

### `identifier_structural_anchor_gap`
- what it checks: Policy check for important identifier token without structural anchor.
- what is wrong when it fails: Token is covered only by name.
- likely action: Anchor via formula, declaration, ontology, overlay, user hint, or waiver.

### `keep_separate_with_link`
- what it checks: Merge/canonicalization check.
- what is wrong when it fails: The merge may lose provenance, flatten distinctions, or regress quality.
- likely action: Use overlay, bridge, conflict split, or backtest before accepting.

### `local_formulas_unchanged`
- what it checks: Merge/canonicalization check.
- what is wrong when it fails: The merge may lose provenance, flatten distinctions, or regress quality.
- likely action: Use overlay, bridge, conflict split, or backtest before accepting.

### `lower_is_better_within_tolerance`
- what it checks: Merge/canonicalization check.
- what is wrong when it fails: The merge may lose provenance, flatten distinctions, or regress quality.
- likely action: Use overlay, bridge, conflict split, or backtest before accepting.

### `no_new_hard_declaration_conflict`
- what it checks: Merge/canonicalization check.
- what is wrong when it fails: The merge may lose provenance, flatten distinctions, or regress quality.
- likely action: Use overlay, bridge, conflict split, or backtest before accepting.

### `no_overlay_drift`
- what it checks: Merge/canonicalization check.
- what is wrong when it fails: The merge may lose provenance, flatten distinctions, or regress quality.
- likely action: Use overlay, bridge, conflict split, or backtest before accepting.

### `numeric_window_fusion_forbidden`
- what it checks: Declaration/ontology/identifier lint finding.
- what is wrong when it fails: The declaration layer or naming shape may be unsafe.
- likely action: Review lint details, then split, bridge, rename, or waive with provenance.

### `ontology_decision_recorded`
- what it checks: Merge/canonicalization check.
- what is wrong when it fails: The merge may lose provenance, flatten distinctions, or regress quality.
- likely action: Use overlay, bridge, conflict split, or backtest before accepting.

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

### `relation_type_not_worse`
- what it checks: Merge/canonicalization check.
- what is wrong when it fails: The merge may lose provenance, flatten distinctions, or regress quality.
- likely action: Use overlay, bridge, conflict split, or backtest before accepting.

### `role_link`
- what it checks: Merge/canonicalization check.
- what is wrong when it fails: The merge may lose provenance, flatten distinctions, or regress quality.
- likely action: Use overlay, bridge, conflict split, or backtest before accepting.

### `same_symbol_different_codomains`
- what it checks: Declaration/ontology/identifier lint finding.
- what is wrong when it fails: The declaration layer or naming shape may be unsafe.
- likely action: Review lint details, then split, bridge, rename, or waive with provenance.

### `semantic_load_in_name`
- what it checks: Declaration/ontology/identifier lint finding.
- what is wrong when it fails: The declaration layer or naming shape may be unsafe.
- likely action: Review lint details, then split, bridge, rename, or waive with provenance.

### `semantic_verdict_not_worse`
- what it checks: Merge/canonicalization check.
- what is wrong when it fails: The merge may lose provenance, flatten distinctions, or regress quality.
- likely action: Use overlay, bridge, conflict split, or backtest before accepting.
