# Diagnostic Rules: source_normalization

- metric_count: `26`
- check_count: `11`
- rule_count: `37`

## `content_token_multiset_precision`

- type: `metric`
- bad value means: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair target: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- value paths:
  - `<search recursive metrics JSON for key `content_token_multiset_precision`>`
- evidence paths:
  - `grounding.new_formula_content_tokens_vs_text_only`
  - `grounding.new_full_surface_content_tokens_vs_text_only`
  - `lexical_coverage.formula_repeat_overuse_examples`
  - `grounding.origin_error_count`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `content_token_multiset_recall`

- type: `metric`
- bad value means: Some source/normalized content is absent from the target representation; report the missing token/fragment list.
- repair target: Add the missing concepts as explicit formula structure, or document why they are intentionally excluded.
- value paths:
  - `<search recursive metrics JSON for key `content_token_multiset_recall`>`
- evidence paths:
  - `lexical_coverage.source_content_tokens_missing_from_formula`
  - `lexical_coverage.source_content_tokens_missing_from_full_surface`
  - `lexical_coverage.formula_repeat_underuse_mass`
  - `coverage.missing_fragment_count`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `content_token_precision`

- type: `metric`
- bad value means: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair target: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- value paths:
  - `<search recursive metrics JSON for key `content_token_precision`>`
- evidence paths:
  - `grounding.new_formula_content_tokens_vs_text_only`
  - `grounding.new_full_surface_content_tokens_vs_text_only`
  - `lexical_coverage.formula_repeat_overuse_examples`
  - `grounding.origin_error_count`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `content_token_recall`

- type: `metric`
- bad value means: Some source/normalized content is absent from the target representation; report the missing token/fragment list.
- repair target: Add the missing concepts as explicit formula structure, or document why they are intentionally excluded.
- value paths:
  - `<search recursive metrics JSON for key `content_token_recall`>`
- evidence paths:
  - `lexical_coverage.source_content_tokens_missing_from_formula`
  - `lexical_coverage.source_content_tokens_missing_from_full_surface`
  - `lexical_coverage.formula_repeat_underuse_mass`
  - `coverage.missing_fragment_count`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `duplication_suspected`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `duplication_suspected`>`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `normalized_content_mass_per_clause`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `source_vs_normalized.normalized_content_mass_per_clause`
- evidence paths:
  - `coverage.normalized_clause_count`
  - `coverage.formula_bearing_item_count`
  - `coverage.missing_fragment_count`
  - `coverage.prose_leak_count`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `normalized_content_token_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `source_vs_normalized.normalized_content_token_count`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `normalized_content_token_jaccard`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `source_vs_normalized.normalized_content_token_jaccard`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `normalized_content_token_mass`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `source_vs_normalized.normalized_content_token_mass`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `normalized_content_token_multiset_precision_to_source`

- type: `metric`
- bad value means: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair target: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- value paths:
  - `source_vs_normalized.normalized_content_token_multiset_precision_to_source`
- evidence paths:
  - `grounding.new_formula_content_tokens_vs_text_only`
  - `grounding.new_full_surface_content_tokens_vs_text_only`
  - `lexical_coverage.formula_repeat_overuse_examples`
  - `grounding.origin_error_count`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `normalized_content_token_multiset_recall_from_source`

- type: `metric`
- bad value means: Some source/normalized content is absent from the target representation; report the missing token/fragment list.
- repair target: Add the missing concepts as explicit formula structure, or document why they are intentionally excluded.
- value paths:
  - `source_vs_normalized.normalized_content_token_multiset_recall_from_source`
- evidence paths:
  - `lexical_coverage.source_content_tokens_missing_from_formula`
  - `lexical_coverage.source_content_tokens_missing_from_full_surface`
  - `lexical_coverage.formula_repeat_underuse_mass`
  - `coverage.missing_fragment_count`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `normalized_content_token_precision_to_source`

- type: `metric`
- bad value means: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair target: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- value paths:
  - `source_vs_normalized.normalized_content_token_precision_to_source`
- evidence paths:
  - `grounding.new_formula_content_tokens_vs_text_only`
  - `grounding.new_full_surface_content_tokens_vs_text_only`
  - `lexical_coverage.formula_repeat_overuse_examples`
  - `grounding.origin_error_count`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `normalized_content_token_recall_from_source`

- type: `metric`
- bad value means: Some source/normalized content is absent from the target representation; report the missing token/fragment list.
- repair target: Add the missing concepts as explicit formula structure, or document why they are intentionally excluded.
- value paths:
  - `source_vs_normalized.normalized_content_token_recall_from_source`
- evidence paths:
  - `lexical_coverage.source_content_tokens_missing_from_formula`
  - `lexical_coverage.source_content_tokens_missing_from_full_surface`
  - `lexical_coverage.formula_repeat_underuse_mass`
  - `coverage.missing_fragment_count`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `normalized_implies_source_entailment`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `source_vs_normalized.normalized_implies_source_entailment`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `normalized_length_ratio_vs_source_mass`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `source_vs_normalized.normalized_length_ratio_vs_source_mass`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `normalized_repeat_overuse_examples`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `source_vs_normalized.normalized_repeat_overuse_examples`
  - `source_vs_normalized.normalized_repeat_overuse_examples[0]`
  - `source_vs_normalized.normalized_repeat_overuse_examples[1]`
  - `source_vs_normalized.normalized_repeat_overuse_examples[2]`
  - `source_vs_normalized.normalized_repeat_overuse_examples[3]`
  - `source_vs_normalized.normalized_repeat_overuse_examples[4]`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `normalized_repeat_overuse_mass`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `source_vs_normalized.normalized_repeat_overuse_mass`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `normalized_repeat_overuse_token_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `source_vs_normalized.normalized_repeat_overuse_token_count`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `normalized_to_source_new_token_count`

- type: `metric`
- bad value means: Target contains unsupported or excessive content; report the exact new/ungrounded/overused token or symbol list.
- repair target: Remove unsupported content, rename symbols, or add explicit prelude/ontology/user-hint provenance.
- value paths:
  - `source_vs_normalized.normalized_to_source_new_token_count`
- evidence paths:
  - `grounding.new_formula_content_tokens_vs_text_only`
  - `grounding.new_full_surface_content_tokens_vs_text_only`
  - `lexical_coverage.formula_repeat_overuse_examples`
  - `grounding.origin_error_count`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `source_excerpt_content_token_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `source_vs_normalized.source_excerpt_content_token_count`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `source_excerpt_content_token_mass`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `source_vs_normalized.source_excerpt_content_token_mass`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `source_implies_normalized_entailment`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `source_vs_normalized.source_implies_normalized_entailment`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `source_normalized_bertscore_f1`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `source_vs_normalized.source_normalized_bertscore_f1`
- evidence paths:
  - `render_back.render_back_text`
  - `render_back.render_nli_text_implies_ir`
  - `render_back.render_nli_ir_implies_text`
  - `render_back.render_contradiction_score`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `source_to_normalized_token_gap_count`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `source_vs_normalized.source_to_normalized_token_gap_count`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `source_vs_normalized_contradiction_score`

- type: `metric`
- bad value means: Rendered IR does not preserve entailment/equivalence; report render text and entailment/contradiction values.
- repair target: Repair IR until render-back and entailment preserve normalized meaning.
- value paths:
  - `source_vs_normalized.source_vs_normalized_contradiction_score`
- evidence paths:
  - `render_back.render_back_text`
  - `render_back.render_nli_text_implies_ir`
  - `render_back.render_nli_ir_implies_text`
  - `render_back.render_contradiction_score`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `threshold`

- type: `metric`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<search recursive metrics JSON for key `threshold`>`
- evidence paths:
  - `<same JSON key as metric name when present>`
  - `<related section in metrics JSON>`
- diagnostic output must include:
  - actual value
  - severity
  - evidence values from evidence_paths when present
  - exact missing/extra/unlinked tokens or symbols when the JSON provides them
  - artifact paths used for comparison

## `preserve_meaning`

- type: `check`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<check output, lint report, checklist result, or generated diagnostic finding>`
- evidence paths:
  - `<check-specific rows in checklist/lint/judge output>`
- diagnostic output must include:
  - check name
  - severity
  - exact row/code that fired
  - source path and target path when available
  - symbol/token/line number when available

## `make_edits_explicit`

- type: `check`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<check output, lint report, checklist result, or generated diagnostic finding>`
- evidence paths:
  - `<check-specific rows in checklist/lint/judge output>`
- diagnostic output must include:
  - check name
  - severity
  - exact row/code that fired
  - source path and target path when available
  - symbol/token/line number when available

## `keep_clause_boundaries_honest`

- type: `check`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<check output, lint report, checklist result, or generated diagnostic finding>`
- evidence paths:
  - `<check-specific rows in checklist/lint/judge output>`
- diagnostic output must include:
  - check name
  - severity
  - exact row/code that fired
  - source path and target path when available
  - symbol/token/line number when available

## `avoid_padding_or_repetition`

- type: `check`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<check output, lint report, checklist result, or generated diagnostic finding>`
- evidence paths:
  - `<check-specific rows in checklist/lint/judge output>`
- diagnostic output must include:
  - check name
  - severity
  - exact row/code that fired
  - source path and target path when available
  - symbol/token/line number when available

## `keep_unresolved_ambiguity_visible`

- type: `check`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<check output, lint report, checklist result, or generated diagnostic finding>`
- evidence paths:
  - `<check-specific rows in checklist/lint/judge output>`
- diagnostic output must include:
  - check name
  - severity
  - exact row/code that fired
  - source path and target path when available
  - symbol/token/line number when available

## `silent_deletion`

- type: `check`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<check output, lint report, checklist result, or generated diagnostic finding>`
- evidence paths:
  - `missing token list`
  - `new token list`
  - `source.md`
  - `normalized.md`
- diagnostic output must include:
  - check name
  - severity
  - exact row/code that fired
  - source path and target path when available
  - symbol/token/line number when available

## `silent_addition`

- type: `check`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<check output, lint report, checklist result, or generated diagnostic finding>`
- evidence paths:
  - `missing token list`
  - `new token list`
  - `source.md`
  - `normalized.md`
- diagnostic output must include:
  - check name
  - severity
  - exact row/code that fired
  - source path and target path when available
  - symbol/token/line number when available

## `lexical_preservation_below_threshold`

- type: `check`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<check output, lint report, checklist result, or generated diagnostic finding>`
- evidence paths:
  - `missing token list`
  - `new token list`
  - `source.md`
  - `normalized.md`
- diagnostic output must include:
  - check name
  - severity
  - exact row/code that fired
  - source path and target path when available
  - symbol/token/line number when available

## `invalid_surface_correction`

- type: `check`
- bad value means: The artifact is structurally invalid; report parser/schema/combined validation errors.
- repair target: Fix A4V3 syntax, declarations, references, signatures, or combined theory conflicts.
- value paths:
  - `<check output, lint report, checklist result, or generated diagnostic finding>`
- evidence paths:
  - `parse errors`
  - `validation errors`
  - `main_ir.a4v3`
- diagnostic output must include:
  - check name
  - severity
  - exact row/code that fired
  - source path and target path when available
  - symbol/token/line number when available

## `definition_role_alignment_failed`

- type: `check`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<check output, lint report, checklist result, or generated diagnostic finding>`
- evidence paths:
  - `<check-specific rows in checklist/lint/judge output>`
- diagnostic output must include:
  - check name
  - severity
  - exact row/code that fired
  - source path and target path when available
  - symbol/token/line number when available

## `normalization_duplicate_content_repetition`

- type: `check`
- bad value means: Metric indicates a possible quality issue; report the value and all available neighboring evidence fields.
- repair target: Inspect relevant artifacts and apply module-specific repair rules.
- value paths:
  - `<check output, lint report, checklist result, or generated diagnostic finding>`
- evidence paths:
  - `<check-specific rows in checklist/lint/judge output>`
- diagnostic output must include:
  - check name
  - severity
  - exact row/code that fired
  - source path and target path when available
  - symbol/token/line number when available
