# Corpus-Aware Multi Judge: N17

- generated_at: `2026-05-10T20:26:55+02:00`
- skipped: `False`
- local_source_alignment_mode: `corresponds`
- corpus_alignment_mode: `corresponds`
- corpus_alignment_agreement: `1.0`
- needs_context_count: `0`
- mean_confidence: `0.988`

## Included Context

```json
{
  "entry": "N17",
  "entry_dir": "D:\\OneDrive\\Documents\\Study\\MIPT\\VKR\\research_experiments\\2026-02_pipeline\\case_studies\\financial_methodology\\definitions\\N17",
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

The IR faithfully encodes the source as a cross-reference definition: the term carrier is linked to the quoted label "Index" and the referenced document part is linked to "Introduction", with the meaning-defining relation asserted and no substantive local meaning invented. The provenance and translator notes confirm this is intended as definitional reference rather than obligation.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR uses explicit label-bridge symbols and carrier entities, which is more formal than the source but semantically aligned.

### gpt-5.4

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `none`
- confidence: `0.98`

Reason:

The local IR faithfully captures the single source sentence by introducing a carrier for the defined term "Index," a carrier for the referenced Section "Introduction," explicit source-label links for both, and a relation stating that the term has its meaning defined in that section. Nothing in the IR contradicts the source, and it does not improperly invent the substantive definition.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR uses carrier entities (`IndexTerm`, `IntroductionSection`) plus label relations instead of quoting the source text directly; this is a modeling choice, not semantic drift.
- The relation name `term_shall_have_meaning_defined_in_section` appropriately encodes the definitional cross-reference, though it is more formalized than the source wording.

### claude-haiku-4-5

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `provenance, translator_notes`
- confidence: `0.98`

Reason:

The source sentence states that 'Index' shall have the meaning defined in Section 'Introduction'. The IR captures this as a cross-reference definition via three coordinated claims: (1) the term 'Index' is a DefinedTerm with source label 'Index', (2) the referenced location is a DocumentPart with source label 'Introduction', and (3) a relation asserting that the term's meaning is defined in that section. The provenance and translator notes confirm this representation is intentional and correct: the 'shall' is not deontic but definitional, and the label bridges are explicit for review/merge support. No substantive meaning is invented locally. The IR faithfully encodes the source's cross-reference structure.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR uses three separate facts (two label bindings and one relation) to express what the source states in a single sentence. This is a deliberate design choice to make lexical identity and document structure explicit for downstream merge operations, not a semantic divergence.

### deepseek-v4-pro

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `none`
- confidence: `1.0`

Reason:

The IR faithfully captures the source statement that the term 'Index' is defined in Section 'Introduction' through an entity-relation structure that records the cross-reference without adding substantive meaning.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR introduces explicit label entities (DefinedTermLabel, DocumentPartLabel) to attach the source strings, which is a design choice for clarity in review and merge contexts.

### qwen/qwen3.6-plus

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `provenance, translator_notes`
- confidence: `1.0`

Reason:

The IR accurately models the source sentence as a cross-reference definition. It introduces entities for the term and section, explicitly binds them to their quoted lexical labels, and asserts a definitional relationship. The corpus context confirms that 'shall' is treated as definitional rather than deontic and that no substantive meaning is invented, which aligns perfectly with the source's intent.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR uses explicit label-binding relations to preserve lexical identity, which is a robust modeling choice for cross-references but adds structural overhead compared to a direct string reference.
