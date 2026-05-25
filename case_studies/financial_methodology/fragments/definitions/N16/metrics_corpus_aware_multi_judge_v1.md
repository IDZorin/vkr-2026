# Corpus-Aware Multi Judge: N16

- generated_at: `2026-05-10T19:50:44+02:00`
- skipped: `False`
- local_source_alignment_mode: `corresponds`
- corpus_alignment_mode: `corresponds`
- corpus_alignment_agreement: `1.0`
- needs_context_count: `0`
- mean_confidence: `0.99`

## Included Context

```json
{
  "entry": "N16",
  "entry_dir": "<PRIVATE_WORKSPACE>\\case_studies\\financial_methodology\\definitions\\N16",
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

The IR captures the source as a cross-reference definition: the quoted term is modeled as a defined term, the referenced section as a document part, and the fact states that Guideline has its meaning defined in Introduction. This matches the source sentence without adding substantive meaning or deontic force.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR uses a generic relation name for definitional cross-reference, which is acceptable and consistent with the provenance notes.
- Entity names are schematic rather than lexical, but they preserve the source referents.

### gpt-5.4

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `none`
- confidence: `0.98`

Reason:

The IR captures the sole source claim: the defined term "Guideline" has its meaning defined in Section "Introduction". The entities for the term and referenced section, plus the fact relating them, match the source without adding substantive meaning or misreading "shall" as an obligation.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR uses surrogate names `GuidelineTerm` and `IntroductionSection` rather than the quoted surface text; this is a naming choice, not semantic drift.
- The relation name `term_shall_have_meaning_defined_in_section` is more explicit than the source wording but preserves the same definitional-reference meaning.

### claude-haiku-4-5

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `provenance, translator_notes`
- confidence: `0.99`

Reason:

The source sentence states that the term 'Guideline' shall have the meaning defined in Section 'Introduction'. The IR faithfully encodes this as a cross-reference definition: GuidelineTerm is a DefinedTerm, IntroductionSection is a DocumentPart, and the fact term_shall_have_meaning_defined_in_section(GuidelineTerm, IntroductionSection) records the definitional reference. The provenance and translator notes confirm that 'shall' is interpreted as a definitional pointer, not a deontic obligation, and that the substantive meaning is intentionally deferred to the referenced section. No semantic content is lost or contradicted.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR uses the entity name 'GuidelineTerm' rather than 'Guideline' to clarify that it represents the quoted term as a symbol, not the concept itself.
- The IR uses 'IntroductionSection' as a DocumentPart entity rather than a bare string reference, making the location explicit and referenceable.
- The relation name 'term_shall_have_meaning_defined_in_section' is verbose but semantically precise, capturing the definitional-reference pattern.

### deepseek-v4-pro

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `provenance, translator_notes`
- confidence: `1.0`

Reason:

The IR fact directly encodes the source sentence's cross-reference definition: the term 'Guideline' has its meaning defined in Section 'Introduction'. The relation term_shall_have_meaning_defined_in_section captures the exact intent without adding substantive content.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- Entities GuidelineTerm and IntroductionSection are named exactly for the quoted source terms, and the relation name is verbose but faithful.
- The provenance and translator notes confirm that 'shall' is treated as definitional drafting, not deontic obligation, which matches the IR's fact.

### qwen/qwen3.6-plus

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `provenance, translator_notes`
- confidence: `1.0`

Reason:

The IR accurately models the source sentence as a cross-reference definition, mapping the quoted term to a DefinedTerm entity and the referenced section to a DocumentPart entity. The relation name explicitly captures the definitional phrasing. Corpus context confirms this is a deliberate design choice to defer substantive meaning and treat 'shall' as definitional rather than deontic, which aligns perfectly with the IR structure.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- none
