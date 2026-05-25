# Corpus-Aware Multi Judge: N03

- generated_at: `2026-05-10T20:23:37+02:00`
- skipped: `False`
- local_source_alignment_mode: `corresponds`
- corpus_alignment_mode: `corresponds`
- corpus_alignment_agreement: `1.0`
- needs_context_count: `0`
- mean_confidence: `0.984`

## Included Context

```json
{
  "entry": "N03",
  "entry_dir": "<PRIVATE_WORKSPACE>\\case_studies\\financial_methodology\\definitions\\N03",
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

The IR faithfully encodes the quoted term, the referenced section, and the definitional cross-reference without inventing substantive meaning or treating the sentence as an obligation. The provenance and translator notes confirm the intended reading and the role of the label bridges, but they are not needed to resolve any mismatch.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR uses explicit carrier entities and label bridges, which is more formal than the source but semantically aligned.
- 'shall have the meaning as defined in Section' is represented as a definitional relation rather than deontic modality, matching the documented drafting convention.

### gpt-5.4

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `none`
- confidence: `0.98`

Reason:

The local IR faithfully captures the single source sentence as a cross-reference definition: it identifies the quoted term "BMR", identifies the referenced Section "Introduction", and states that the term has the meaning defined in that section. The added label-linking conjuncts make lexical identity explicit and do not change the substantive meaning.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR uses auxiliary label relations (`defined_term_source_label`, `document_part_source_label`) for traceability; these are review-oriented and not semantic drift.
- `term_shall_have_meaning_defined_in_section` is a slightly formalized rendering of the drafting phrase "shall have the meaning as defined in Section ...", but preserves the definitional-reference reading.

### claude-haiku-4-5

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `provenance, translator_notes`
- confidence: `0.98`

Reason:

The source sentence states that 'BMR' shall have the meaning defined in Section 'Introduction'. The IR captures this as a cross-reference definition via three coordinated claims: (1) the term 'BMR' is labeled and identified as BMRTerm, (2) the section 'Introduction' is labeled and identified as IntroductionSection, and (3) a definitional relation links the term to the section. The provenance and translator notes confirm that 'shall' is correctly interpreted as a definitional pointer, not a deontic obligation, and that the label bridges are included for review/merge support. No substantive meaning is invented locally. The IR is faithful to the source.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR uses formal relation names (defined_term_source_label, document_part_source_label, term_shall_have_meaning_defined_in_section) rather than the source's natural-language phrasing, but this is standard IR abstraction, not drift.
- The IR introduces intermediate sorts (DefinedTerm, DocumentPart, DefinedTermLabel, DocumentPartLabel) to structure the cross-reference; the source does not explicitly name these categories, but they are justified by the prelude methodology and translator decision record.

### deepseek-v4-pro

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `provenance, translator_notes`
- confidence: `0.98`

Reason:

The IR faithfully represents the cross-reference definition, capturing the defined term, the section, and the relation that the definition is found there. No semantic drift.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR introduces entity-label relations to explicitly tie the formal symbols to the quoted source strings, which is a standard translation practice.

### qwen/qwen3.6-plus

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `provenance, translator_notes`
- confidence: `1.0`

Reason:

The IR faithfully captures the source's cross-reference definition by modeling 'BMR' as a DefinedTerm and 'Introduction' as a DocumentPart, explicitly binding their literal labels and asserting the definitional relationship. The corpus context confirms that the structural label bridges and the non-deontic interpretation of 'shall' are intentional modeling choices that preserve the source's legal drafting intent without adding or omitting substantive meaning.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR uses explicit label-bridge relations (defined_term_source_label, document_part_source_label) to preserve lexical identity, which is a structural normalization choice rather than a semantic divergence.
