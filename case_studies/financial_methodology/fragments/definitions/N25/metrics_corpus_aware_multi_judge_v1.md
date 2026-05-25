# Corpus-Aware Multi Judge: N25

- generated_at: `2026-05-10T20:08:35+02:00`
- skipped: `False`
- local_source_alignment_mode: `corresponds`
- corpus_alignment_mode: `corresponds`
- corpus_alignment_agreement: `1.0`
- needs_context_count: `0`
- mean_confidence: `0.988`

## Included Context

```json
{
  "entry": "N25",
  "entry_dir": "<PRIVATE_WORKSPACE>\\case_studies\\financial_methodology\\definitions\\N25",
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

The IR captures the quoted term as a DefinedTerm and records that it has its meaning defined in Section 5.5, which matches the source’s cross-reference definition. The provenance and translator notes confirm that the relation is intended as a definitional reference, not an obligation, and no substantive Section 5.5 content is included here.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR uses a symbolic term/entity name rather than the quoted surface form, which is a normal translation choice.
- Section 5.5 is represented as Section5_5, a naming normalization only.

### gpt-5.4

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `none`
- confidence: `0.98`

Reason:

The local IR captures the sole source claim: the defined term "Oversight Committee" has its meaning defined in Section 5.5. The IR treats this as a definitional cross-reference rather than an obligation, which matches the source wording in context and does not omit or add substantive content.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR uses a generic relation name `term_shall_have_meaning_defined_in_section` instead of repeating the exact legal drafting phrase; this is wording normalization, not semantic drift.
- `OversightCommitteeTerm` and `Section5_5` are normalized symbol names for the quoted term and referenced section.

### claude-haiku-4-5

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `provenance, translator_notes`
- confidence: `0.98`

Reason:

The source sentence is a cross-reference definition: it states that the term 'Oversight Committee' has its meaning defined elsewhere, specifically in Section 5.5. The IR captures this precisely: OversightCommitteeTerm is linked to Section5_5 via the term_shall_have_meaning_defined_in_section relation. The provenance and translator notes confirm that 'shall' here is not a deontic obligation but a definitional pointer, and the IR correctly avoids duplicating substantive content from Section 5.5. No semantic divergence exists.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR uses camelCase entity names (OversightCommitteeTerm, Section5_5) while the source uses quoted strings and section notation; this is standard IR naming convention and not a semantic issue.
- The relation name term_shall_have_meaning_defined_in_section is verbose but semantically precise and documented in the provenance.

### deepseek-v4-pro

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `provenance, translator_notes`
- confidence: `1.0`

Reason:

The source sentence is a definition cross-reference that is fully captured by the IR fact linking the term entity to the section entity via the relation indicating where the meaning is defined. All semantic content is preserved without distortion.

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

The IR directly formalizes the source sentence by linking a term entity to a document part entity via a relation that captures the cross-reference definition. The corpus context confirms the deliberate choice to model 'shall' as definitional rather than deontic, ensuring the IR aligns perfectly with the source intent without introducing external obligations.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The relation name `term_shall_have_meaning_defined_in_section` is highly verbose but explicitly preserves the source's legal phrasing, which aids traceability.
