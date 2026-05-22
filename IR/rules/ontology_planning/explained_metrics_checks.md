# Explained Metrics and Checks: ontology_planning

Metric count: 44
Check count: 24

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

### `arg_arity_stability`
- kind: `comparative`
- what it checks: whether different variants agree on argument count.
- how it is computed: compare top-level focus symbol arity across variants; report agreement ratio.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `carrier_choice_stability`
- kind: `comparative`
- what it checks: whether different runs choose the same carrier family, for example function vs relation or exchange-level vs component-level predicate.
- how it is computed: compare chosen carrier signatures across variants or reruns; report agreement ratio.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

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

### `new_formula_content_token_count_vs_text_only`
- kind: `hard_warning`
- what it checks: semantically meaningful new formula tokens relative to source plus normalized text only.
- how it is computed: same as above, but remove stopwords and syntax-only tokens before counting.
- what is wrong when it fails or looks bad: If this is bad, the artifact may parse but is semantically unsafe or incomplete.
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

### `sort_choice_stability`
- kind: `comparative`
- what it checks: whether different variants agree on sorts for the same argument positions.
- how it is computed: compare argument-sort tuples across variants; report agreement ratio.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `source_grounded_content_piece_ratio_mean`
- kind: `continuous`
- what it checks: how grounded identifier pieces are in source text, normalized text, and Prelude vocabulary.
- how it is computed: for each identifier, compute the share of content pieces found in the source-side lexicon; then average across identifiers.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `text_licensed_symbol_ratio`
- kind: `continuous`
- what it checks: share of declared local symbols that can be grounded directly in source or normalized text.
- how it is computed: `text-grounded local symbol count / total local symbol count`.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

### `top_glued_identifiers`
- kind: `comparative`
- what it checks: the most over-glued identifiers in the artifact.
- how it is computed: rank identifiers by content glue excess, then raw glue excess, then low source-groundedness.
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Split overloaded names and add structural anchors in declarations/formulas/ontology.

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

## Checks
### `declarations_use_real_world_ontology`
- what it checks: No detailed explanation recorded yet.
- what is wrong when it fails: Unknown without manual review.
- likely action: Add explanation to the check map.

### `constraints_remain_source_faithful`
- what it checks: No detailed explanation recorded yet.
- what is wrong when it fails: Unknown without manual review.
- likely action: Add explanation to the check map.

### `concept_link_not_only_in_symbol_name`
- what it checks: No detailed explanation recorded yet.
- what is wrong when it fails: Unknown without manual review.
- likely action: Add explanation to the check map.

### `editorial_inconsistency_resolved_in_declarations_or_overlay`
- what it checks: No detailed explanation recorded yet.
- what is wrong when it fails: Unknown without manual review.
- likely action: Add explanation to the check map.

### `identifier_structural_anchor_gap`
- what it checks: Policy check for important identifier token without structural anchor.
- what is wrong when it fails: Token is covered only by name.
- likely action: Anchor via formula, declaration, ontology, overlay, user hint, or waiver.

### `same_symbol_different_codomains`
- what it checks: Declaration/ontology/identifier lint finding.
- what is wrong when it fails: The declaration layer or naming shape may be unsafe.
- likely action: Review lint details, then split, bridge, rename, or waive with provenance.

### `ontology_level_mixing`
- what it checks: Declaration/ontology/identifier lint finding.
- what is wrong when it fails: The declaration layer or naming shape may be unsafe.
- likely action: Review lint details, then split, bridge, rename, or waive with provenance.

### `enum_value_mapping_candidates`
- what it checks: Declaration/ontology/identifier lint finding.
- what is wrong when it fails: The declaration layer or naming shape may be unsafe.
- likely action: Review lint details, then split, bridge, rename, or waive with provenance.

### `codomain_split_value_families`
- what it checks: Declaration/ontology/identifier lint finding.
- what is wrong when it fails: The declaration layer or naming shape may be unsafe.
- likely action: Review lint details, then split, bridge, rename, or waive with provenance.

### `overlay_consistency_drift`
- what it checks: Declaration/ontology/identifier lint finding.
- what is wrong when it fails: The declaration layer or naming shape may be unsafe.
- likely action: Review lint details, then split, bridge, rename, or waive with provenance.

### `semantic_load_in_name`
- what it checks: Declaration/ontology/identifier lint finding.
- what is wrong when it fails: The declaration layer or naming shape may be unsafe.
- likely action: Review lint details, then split, bridge, rename, or waive with provenance.

### `opaque_helper_predicates`
- what it checks: Declaration/ontology/identifier lint finding.
- what is wrong when it fails: The declaration layer or naming shape may be unsafe.
- likely action: Review lint details, then split, bridge, rename, or waive with provenance.

### `numeric_window_fusion_forbidden`
- what it checks: Declaration/ontology/identifier lint finding.
- what is wrong when it fails: The declaration layer or naming shape may be unsafe.
- likely action: Review lint details, then split, bridge, rename, or waive with provenance.

### `identifier_source_lexical_crosslink_gap`
- what it checks: Declaration/ontology/identifier lint finding.
- what is wrong when it fails: The declaration layer or naming shape may be unsafe.
- likely action: Review lint details, then split, bridge, rename, or waive with provenance.

### `identifier_source_lexical_crosslink_candidates`
- what it checks: Declaration/ontology/identifier lint finding.
- what is wrong when it fails: The declaration layer or naming shape may be unsafe.
- likely action: Review lint details, then split, bridge, rename, or waive with provenance.

### `source_phrase_identifier_crosslink_gap`
- what it checks: Declaration/ontology/identifier lint finding.
- what is wrong when it fails: The declaration layer or naming shape may be unsafe.
- likely action: Review lint details, then split, bridge, rename, or waive with provenance.

### `source_phrase_identifier_crosslink_candidates`
- what it checks: Declaration/ontology/identifier lint finding.
- what is wrong when it fails: The declaration layer or naming shape may be unsafe.
- likely action: Review lint details, then split, bridge, rename, or waive with provenance.

### `composite_identifier_crosslink_gap`
- what it checks: Declaration/ontology/identifier lint finding.
- what is wrong when it fails: The declaration layer or naming shape may be unsafe.
- likely action: Review lint details, then split, bridge, rename, or waive with provenance.

### `composite_identifier_crosslink_candidates`
- what it checks: Declaration/ontology/identifier lint finding.
- what is wrong when it fails: The declaration layer or naming shape may be unsafe.
- likely action: Review lint details, then split, bridge, rename, or waive with provenance.

### `shared_base_phrase_family_candidates`
- what it checks: Declaration/ontology/identifier lint finding.
- what is wrong when it fails: The declaration layer or naming shape may be unsafe.
- likely action: Review lint details, then split, bridge, rename, or waive with provenance.

### `canonical_subterm_reuse_gap`
- what it checks: Declaration/ontology/identifier lint finding.
- what is wrong when it fails: The declaration layer or naming shape may be unsafe.
- likely action: Review lint details, then split, bridge, rename, or waive with provenance.

### `canonical_subterm_reuse_candidates`
- what it checks: Declaration/ontology/identifier lint finding.
- what is wrong when it fails: The declaration layer or naming shape may be unsafe.
- likely action: Review lint details, then split, bridge, rename, or waive with provenance.

### `decomposition_policy_gap`
- what it checks: Declaration/ontology/identifier lint finding.
- what is wrong when it fails: The declaration layer or naming shape may be unsafe.
- likely action: Review lint details, then split, bridge, rename, or waive with provenance.

### `decomposition_policy_candidates`
- what it checks: Declaration/ontology/identifier lint finding.
- what is wrong when it fails: The declaration layer or naming shape may be unsafe.
- likely action: Review lint details, then split, bridge, rename, or waive with provenance.
