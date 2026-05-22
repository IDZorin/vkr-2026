# Source Normalization Metrics and Checks

Metric count: 26
Check count: 11

## Metrics
- `content_token_multiset_precision`
- `content_token_multiset_recall`
- `content_token_precision`
- `content_token_recall`
- `duplication_suspected`
- `normalized_content_mass_per_clause`
- `normalized_content_token_count`
- `normalized_content_token_jaccard`
- `normalized_content_token_mass`
- `normalized_content_token_multiset_precision_to_source`
- `normalized_content_token_multiset_recall_from_source`
- `normalized_content_token_precision_to_source`
- `normalized_content_token_recall_from_source`
- `normalized_implies_source_entailment`
- `normalized_length_ratio_vs_source_mass`
- `normalized_repeat_overuse_examples`
- `normalized_repeat_overuse_mass`
- `normalized_repeat_overuse_token_count`
- `normalized_to_source_new_token_count`
- `source_excerpt_content_token_count`
- `source_excerpt_content_token_mass`
- `source_implies_normalized_entailment`
- `source_normalized_bertscore_f1`
- `source_to_normalized_token_gap_count`
- `source_vs_normalized_contradiction_score`
- `threshold`

## Checks
- `preserve_meaning`
- `make_edits_explicit`
- `keep_clause_boundaries_honest`
- `avoid_padding_or_repetition`
- `keep_unresolved_ambiguity_visible`
- `silent_deletion`
- `silent_addition`
- `lexical_preservation_below_threshold`
- `invalid_surface_correction`
- `definition_role_alignment_failed`
- `normalization_duplicate_content_repetition`
