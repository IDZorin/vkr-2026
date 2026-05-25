# Corpus-Aware Multi Judge: N29

- generated_at: `2026-05-10T20:14:10+02:00`
- skipped: `False`
- local_source_alignment_mode: `corresponds`
- corpus_alignment_mode: `corresponds`
- corpus_alignment_agreement: `1.0`
- needs_context_count: `0`
- mean_confidence: `0.984`

## Included Context

```json
{
  "entry": "N29",
  "entry_dir": "D:\\OneDrive\\Documents\\Study\\MIPT\\VKR\\research_experiments\\2026-02_pipeline\\case_studies\\financial_methodology\\definitions\\N29",
  "global_bridge": false,
  "related_sections": [],
  "artifacts": {
    "source.md": true,
    "normalized.md": true,
    "main_ir.a4v3": true,
    "repair.a4v3": false,
    "provenance.yaml": true,
    "translator_notes.md": true,
    "waivers.yaml": false,
    "waivers_v1.yaml": false
  }
}
```

## Judges

### gpt-5.4-mini

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `provenance, translator_notes`
- confidence: `0.98`

Reason:

The IR captures the quoted term as a defined term and records that its meaning is defined in Section 1.3, which matches the source sentence. The provenance and translator notes confirm that the relation is intended as a cross-reference definition rather than an obligation, with no added substantive content.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- Section 1.3 is represented as `Section1_3`, and the quoted term is normalized to `StartDateTerm`; these are naming choices only.

### gpt-5.4

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `none`
- confidence: `0.98`

Reason:

The local IR faithfully captures the sole source claim: the defined term "Start Date" has its meaning defined in Section 1.3. The IR does not add substantive Section 1.3 content or misread "shall" as an obligation; instead it records the cross-reference definition exactly as the source states.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR uses a normalized symbol `StartDateTerm` for the quoted term "Start Date".
- `Section1_3` is a normalized entity name for the referenced document location Section 1.3.
- The relation name `term_shall_have_meaning_defined_in_section` is slightly formalized wording but preserves the source meaning.

### claude-haiku-4-5

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `provenance, translator_notes`
- confidence: `0.98`

Reason:

The source sentence is a cross-reference definition: '"Start Date" shall have the meaning as defined in Section 1.3.' The IR faithfully captures this by declaring StartDateTerm as a DefinedTerm, Section1_3 as a DocumentPart, and asserting the relation term_shall_have_meaning_defined_in_section(StartDateTerm, Section1_3). The provenance and translator notes confirm that 'shall' here is not a deontic obligation but a definitional pointer, and that the IR correctly avoids duplicating substantive content from Section 1.3. No semantic divergence exists between source and IR.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR uses the entity name StartDateTerm (camelCase) to represent the quoted source term "Start Date" (with quotes and space). This is standard IR naming convention and introduces no semantic drift.
- The IR uses Section1_3 (camelCase, underscore) to represent the source reference 'Section 1.3'. Again, standard IR naming; no semantic issue.

### deepseek-v4-pro

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `none`
- confidence: `0.98`

Reason:

The IR faithfully represents the source sentence as a cross-reference definition, using explicit entities for the term and section and a relation capturing the 'shall have the meaning as defined in' phrasing. No divergence or omission.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- none

### qwen/qwen3.6-plus

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `provenance, translator_notes`
- confidence: `1.0`

Reason:

The IR directly and accurately captures the source sentence by modeling the quoted term and the referenced section as entities linked by a relation that explicitly encodes the definitional cross-reference. The corpus context confirms that the relation name intentionally reflects legal drafting conventions without implying deontic obligation, fully aligning with the source intent.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The relation name term_shall_have_meaning_defined_in_section is verbose but precisely mirrors the source phrasing and correctly avoids deontic semantics.
