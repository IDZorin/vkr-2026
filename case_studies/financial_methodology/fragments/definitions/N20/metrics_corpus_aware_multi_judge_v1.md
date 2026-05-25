# Corpus-Aware Multi Judge: N20

- generated_at: `2026-05-10T19:58:42+02:00`
- skipped: `False`
- local_source_alignment_mode: `corresponds`
- corpus_alignment_mode: `corresponds`
- corpus_alignment_agreement: `1.0`
- needs_context_count: `0`
- mean_confidence: `0.992`

## Included Context

```json
{
  "entry": "N20",
  "entry_dir": "D:\\OneDrive\\Documents\\Study\\MIPT\\VKR\\research_experiments\\2026-02_pipeline\\case_studies\\financial_methodology\\definitions\\N20",
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
- confidence: `0.99`

Reason:

The IR faithfully encodes the quoted term as a defined term and the Section 2.2 reference as a definitional cross-reference, matching the source sentence. The provenance and translator notes confirm that "shall" is intended as definitional wording, not an obligation, and that no substantive Section 2.2 content should be duplicated here.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR uses a technical relation name rather than the source’s legal phrasing, but the meaning is preserved.
- Section2_2 is modeled as a DocumentPart, which is a naming/typing choice consistent with the reference.

### gpt-5.4

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `none`
- confidence: `0.98`

Reason:

The source states that the defined term "Index Component Requirements" has the meaning defined in Section 2.2, and the IR encodes exactly that as a fact relating the term entity to the document part Section2_2. The IR does not add substantive Section 2.2 content or misread "shall" as an obligation.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR introduces a helper sort `DefinedTerm`, which is a modeling choice rather than a semantic change.
- The relation name `term_shall_have_meaning_defined_in_section` is slightly formalized wording of the source cross-reference sentence.
- `Section2_2` is represented as a `DocumentPart`, which is a structural encoding choice consistent with the source reference.

### claude-haiku-4-5

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `provenance, translator_notes`
- confidence: `0.99`

Reason:

The source sentence states that the term 'Index Component Requirements' shall have the meaning defined in Section 2.2. The IR captures this as a cross-reference definition via the fact `term_shall_have_meaning_defined_in_section(IndexComponentRequirementsTerm, Section2_2)`. The provenance and translator notes confirm that 'shall' is interpreted as a definitional reference, not a deontic obligation, and that the IR correctly represents the pointer to Section 2.2 without duplicating substantive content. No semantic divergence exists between source and IR.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR uses the entity name `IndexComponentRequirementsTerm` rather than the quoted string; this is standard IR practice for representing defined terms.
- The IR uses the entity name `Section2_2` rather than the prose reference; this is standard IR practice for representing document locations.
- The relation name `term_shall_have_meaning_defined_in_section` is a formal encoding of the source phrase 'shall have the meaning as defined in'; the provenance explicitly justifies this choice.

### deepseek-v4-pro

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `none`
- confidence: `1.0`

Reason:

The IR directly encodes the source cross-reference definition: the term 'Index Component Requirements' is linked to Section 2.2 via a relation, matching the source's intent without importing external content.

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

The IR directly models the source sentence by declaring entities for the quoted term and the referenced section, and asserting a fact that links them via a relation explicitly named to capture the 'shall have the meaning as defined in' phrasing. The corpus context confirms that 'shall' is intentionally modeled as a definitional cross-reference rather than a deontic obligation, and that substantive rules from Section 2.2 are correctly deferred to a merge layer. The translation is faithful and complete.

Semantic differences:

- none

Context-resolved issues:

- Potential ambiguity regarding whether 'shall' implies a deontic obligation or a definitional reference is resolved by the translator notes and provenance, which explicitly classify it as a cross-reference definition.

Stylistic notes:

- The relation name 'term_shall_have_meaning_defined_in_section' is highly descriptive but verbose; it accurately reflects the source phrasing without introducing semantic drift.
