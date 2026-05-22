# Explained Metrics and Checks: source_normalization

Metric count: 26
Check count: 11

## Metrics
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

### `duplication_suspected`
- kind: not documented in metric catalog
- what it checks: not documented
- how it is computed: not documented
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

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

### `threshold`
- kind: not documented in metric catalog
- what it checks: not documented
- how it is computed: not documented
- what is wrong when it fails or looks bad: Use this value to diagnose drift, coverage, complexity, or tradeoffs.
- likely action: Inspect the artifact and the relevant module rules before accepting or repairing.

## Checks
### `preserve_meaning`
- what it checks: Checks that normalization keeps actors, conditions, numbers, exceptions, and obligations.
- what is wrong when it fails: Meaning disappeared or appeared during normalization.
- likely action: Restore missing source content or remove invented content.

### `make_edits_explicit`
- what it checks: Checks that typo/casing/punctuation fixes are recorded.
- what is wrong when it fails: A surface repair is hidden and not auditable.
- likely action: Add a correction note or avoid the silent edit.

### `keep_clause_boundaries_honest`
- what it checks: Checks that clause splitting preserves conditions and exceptions.
- what is wrong when it fails: Scope or exception was buried during splitting.
- likely action: Split again or repeat the needed scope explicitly.

### `avoid_padding_or_repetition`
- what it checks: Checks that normalized text does not add filler or duplicated content.
- what is wrong when it fails: Normalization repeats or strengthens content without need.
- likely action: Remove padding; keep repetition only when it exposes structure.

### `keep_unresolved_ambiguity_visible`
- what it checks: Checks that vague source text stays appropriately cautious.
- what is wrong when it fails: Normalization guessed a certainty not in source.
- likely action: Restore ambiguity or record a user clarification.

### `silent_deletion`
- what it checks: Validator code for source content missing after transformation.
- what is wrong when it fails: Important source content was dropped.
- likely action: Restore the deleted content or document why it is intentionally excluded.

### `silent_addition`
- what it checks: Validator code for content added without source support.
- what is wrong when it fails: New meaning was introduced.
- likely action: Remove the invention or record ontology/user-hint provenance.

### `lexical_preservation_below_threshold`
- what it checks: Normalization validator code.
- what is wrong when it fails: The source-to-normalized transformation is not faithful enough.
- likely action: Repair normalized text or document the decision.

### `invalid_surface_correction`
- what it checks: Normalization validator code.
- what is wrong when it fails: The source-to-normalized transformation is not faithful enough.
- likely action: Repair normalized text or document the decision.

### `definition_role_alignment_failed`
- what it checks: Normalization validator code.
- what is wrong when it fails: The source-to-normalized transformation is not faithful enough.
- likely action: Repair normalized text or document the decision.

### `normalization_duplicate_content_repetition`
- what it checks: Normalization validator code.
- what is wrong when it fails: The source-to-normalized transformation is not faithful enough.
- likely action: Repair normalized text or document the decision.
