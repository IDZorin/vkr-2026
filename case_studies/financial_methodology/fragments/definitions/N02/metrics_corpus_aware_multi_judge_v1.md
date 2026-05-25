# Corpus-Aware Multi Judge: N02

- generated_at: `2026-05-10T19:45:34+02:00`
- skipped: `False`
- local_source_alignment_mode: `corresponds`
- corpus_alignment_mode: `corresponds`
- corpus_alignment_agreement: `1.0`
- needs_context_count: `0`
- mean_confidence: `0.988`

## Included Context

```json
{
  "entry": "N02",
  "entry_dir": "<PRIVATE_WORKSPACE>\\case_studies\\financial_methodology\\definitions\\N02",
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

The IR captures the source as a cross-reference definition: the quoted term is modeled as a defined term, and the fact states that it has its meaning defined in the Introduction section. The provenance and translator notes explicitly confirm that no substantive meaning or deontic obligation was intended.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- `IntroductionSection` is a document-part name for the cited section; `term_shall_have_meaning_defined_in_section` is a verbose but faithful encoding of the legal drafting formula.

### gpt-5.4

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `none`
- confidence: `0.98`

Reason:

The local IR captures the sole source claim: the defined term "Benchmark Regulation" has its meaning defined in Section "Introduction". The IR does not add substantive meaning, and its relation expresses a definitional cross-reference rather than an obligation, which matches the source wording in context.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR uses the normalized symbol name `BenchmarkRegulationTerm` for the quoted term "Benchmark Regulation".
- `IntroductionSection` is a catalog name for the referenced Section "Introduction".
- The relation name `term_shall_have_meaning_defined_in_section` is slightly formalized but semantically matches the drafting formula.

### claude-haiku-4-5

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `provenance, translator_notes`
- confidence: `0.98`

Reason:

The source sentence states that 'Benchmark Regulation' shall have the meaning as defined in Section 'Introduction'. The IR faithfully captures this as a cross-reference definition: an entity BenchmarkRegulationTerm, a DocumentPart IntroductionSection, and a relation term_shall_have_meaning_defined_in_section linking them. The provenance and translator notes confirm that 'shall' is correctly interpreted as a definitional reference, not a deontic obligation, and that the IR appropriately refrains from inventing the substantive meaning locally. No semantic divergence exists.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- Entity naming uses CamelCase (BenchmarkRegulationTerm, IntroductionSection) which is standard a4v3 convention; source uses quoted strings.
- Relation name term_shall_have_meaning_defined_in_section is verbose but semantically precise and documented in provenance.

### deepseek-v4-pro

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `none`
- confidence: `1.0`

Reason:

The IR directly encodes the source sentence as a defined term referencing a document section, without adding or omitting content.

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

The IR directly and accurately models the source sentence by representing the quoted phrase as a DefinedTerm, the referenced location as a DocumentPart, and the definitional pointer as a binary relation. The provenance and translator notes confirm that the modal 'shall' is intentionally treated as a cross-referential definition rather than a deontic obligation, which aligns perfectly with the IR's declarative fact structure. No semantic content is added, omitted, or distorted.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The relation name term_shall_have_meaning_defined_in_section closely mirrors the source phrasing, ensuring high traceability while explicitly avoiding deontic semantics.
