# Corpus-Aware Multi Judge: N18

- generated_at: `2026-05-10T19:55:54+02:00`
- skipped: `False`
- local_source_alignment_mode: `corresponds`
- corpus_alignment_mode: `corresponds`
- corpus_alignment_agreement: `1.0`
- needs_context_count: `0`
- mean_confidence: `0.99`

## Included Context

```json
{
  "entry": "N18",
  "entry_dir": "<PRIVATE_WORKSPACE>\\case_studies\\financial_methodology\\definitions\\N18",
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

The IR captures the quoted defined term and the cross-reference to Section "Introduction" without adding substantive meaning or deontic force. The provenance and translator notes explicitly confirm this is a definitional reference, matching the source sentence.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- `DefinedTerm` and `IntroductionSection` are implementation-level names for the quoted term and referenced section; this is a naming choice, not a semantic change.

### gpt-5.4

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `none`
- confidence: `0.98`

Reason:

The local IR faithfully captures the sole source claim: the defined term "Index Administrator" has its meaning defined in the section identified as "Introduction." The IR does not add substantive meaning, and its relation expresses a definitional cross-reference rather than an obligation, which matches the source wording in context.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR uses the normalized symbol name `IndexAdministratorTerm` for the quoted defined term "Index Administrator".
- `IntroductionSection` is a catalog name for the referenced Section "Introduction".
- The relation name `term_shall_have_meaning_defined_in_section` is slightly formalized but semantically matches the drafting phrase.

### claude-haiku-4-5

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `provenance, translator_notes`
- confidence: `0.99`

Reason:

The source sentence is a cross-reference definition stating that 'Index Administrator' shall have the meaning defined in Section 'Introduction'. The IR faithfully encodes this as a fact that the term IndexAdministratorTerm has its meaning defined in IntroductionSection via the relation term_shall_have_meaning_defined_in_section. The provenance and translator notes confirm this is the intended reading: the IR records the definitional reference without inventing substantive content, and correctly interprets 'shall' as a definitional pointer rather than a deontic obligation. No semantic divergence exists.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR uses camelCase entity names (IndexAdministratorTerm, IntroductionSection) while the source uses quoted strings with spaces ('Index Administrator', 'Section "Introduction"'). This is standard IR naming convention and not a semantic issue.
- The relation name term_shall_have_meaning_defined_in_section is verbose but semantically precise; it explicitly captures the 'shall have the meaning as defined in' phrasing from the source.

### deepseek-v4-pro

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `none`
- confidence: `1.0`

Reason:

The source sentence is a cross-reference definition, and the IR captures exactly that with a fact linking the term entity to the document part via a dedicated relation.

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

The IR accurately models the source sentence as a definitional cross-reference, mapping the quoted term to a DefinedTerm entity and the referenced section to a DocumentPart entity. The relation term_shall_have_meaning_defined_in_section directly captures the source phrasing without incorrectly treating 'shall' as a deontic obligation, aligning perfectly with both the source text and the documented translator decisions.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- none
