# Corpus-Aware Multi Judge: N28

- generated_at: `2026-05-10T20:11:37+02:00`
- skipped: `False`
- local_source_alignment_mode: `corresponds`
- corpus_alignment_mode: `corresponds`
- corpus_alignment_agreement: `1.0`
- needs_context_count: `0`
- mean_confidence: `0.98`

## Included Context

```json
{
  "entry": "N28",
  "entry_dir": "<PRIVATE_WORKSPACE>\\case_studies\\financial_methodology\\definitions\\N28",
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

The IR captures the source as a cross-reference definition: the quoted term Solactive is linked to the Introduction section as the place where its meaning is defined, without inventing substantive meaning or treating shall as an obligation. The documented provenance and translator notes confirm this reading.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- `DefinedTerm` is a reasonable catalog sort for the quoted term.
- `IntroductionSection` as a `DocumentPart` is a naming choice matching the referenced section.

### gpt-5.4

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `none`
- confidence: `0.98`

Reason:

The local IR faithfully captures the single source claim: the defined term "Solactive" has its meaning defined in the section identified as "Introduction." The IR does not add substantive meaning, and its relation is consistent with a definitional cross-reference rather than an obligation.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR uses the surrogate name `SolactiveTerm` for the quoted term "Solactive", which is a naming choice rather than a semantic change.
- `IntroductionSection` models Section "Introduction" as a `DocumentPart`, which is an ontological representation choice consistent with the source.
- The relation name `term_shall_have_meaning_defined_in_section` is more explicit than the source wording but preserves the same meaning.

### claude-haiku-4-5

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `provenance, translator_notes`
- confidence: `0.99`

Reason:

The source sentence is a cross-reference definition stating that the term 'Solactive' has its meaning defined in Section 'Introduction'. The IR faithfully encodes this as a fact that the DefinedTerm 'SolactiveTerm' has its meaning defined in the DocumentPart 'IntroductionSection', via the relation 'term_shall_have_meaning_defined_in_section'. The provenance and translator notes confirm this is the intended reading: the 'shall' is definitional, not deontic, and the IR correctly avoids inventing substantive content. No contradiction exists between source and IR.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR uses entity names 'SolactiveTerm' and 'IntroductionSection' rather than inline string literals; this is standard IR practice and does not constitute semantic drift.
- The relation name 'term_shall_have_meaning_defined_in_section' is a formal encoding of the source phrase 'shall have the meaning as defined in Section'; the provenance explicitly justifies this choice.

### deepseek-v4-pro

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `translator_notes, provenance`
- confidence: `1.0`

Reason:

The source sentence is a definitional cross-reference. The IR captures this directly with an entity for the term, an entity for the referenced section, a relation that means 'shall have the meaning as defined in', and a fact linking them. No semantic divergence.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- IR naming is transparent and follows the source phrasing closely.

### qwen/qwen3.6-plus

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `provenance, translator_notes`
- confidence: `0.95`

Reason:

The IR faithfully captures the source sentence as a definitional cross-reference, mapping the quoted term and target section to entities and linking them via a dedicated relation. The corpus context explicitly validates the modeling decisions, confirming that "shall" functions as legal drafting rather than a deontic obligation and that the substantive definition is intentionally deferred to the referenced section.

Semantic differences:

- none

Context-resolved issues:

- Potential misinterpretation of 'shall' as a deontic obligation is resolved by explicit translator guidance
- Absence of the actual definition in the IR is justified by provenance notes deferring substantive meaning to the referenced section

Stylistic notes:

- The relation name term_shall_have_meaning_defined_in_section is highly verbose but precisely mirrors the source phrasing
- Introduction of the DefinedTerm sort provides a clean, reusable abstraction for quoted terms
