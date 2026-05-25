# Corpus-Aware Multi Judge: N24

- generated_at: `2026-05-10T20:06:05+02:00`
- skipped: `False`
- local_source_alignment_mode: `corresponds`
- corpus_alignment_mode: `corresponds`
- corpus_alignment_agreement: `1.0`
- needs_context_count: `0`
- mean_confidence: `0.99`

## Included Context

```json
{
  "entry": "N24",
  "entry_dir": "D:\\OneDrive\\Documents\\Study\\MIPT\\VKR\\research_experiments\\2026-02_pipeline\\case_studies\\financial_methodology\\definitions\\N24",
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

The IR captures the source as a cross-reference definition: the quoted term is modeled as a defined term, Section 1.3 as the referenced document part, and the fact states that the term’s meaning is defined there. This matches the source sentence and the documented translation intent.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR uses a normalized entity name `LiveDateTerm` for the quoted source term "Live Date".
- `Section1_3` is a structural identifier for the cited section, not a semantic change.

### gpt-5.4

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `none`
- confidence: `0.98`

Reason:

The local IR captures the sole source claim: the defined term "Live Date" has its meaning defined in Section 1.3. The IR does not add substantive Section 1.3 content or misread "shall" as an obligation; instead it records the definitional cross-reference expressed in the source sentence.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR uses the normalized symbol name LiveDateTerm for the quoted term "Live Date".
- Section1_3 is a symbolic identifier for the referenced document location Section 1.3.
- The relation name term_shall_have_meaning_defined_in_section is slightly formalized but matches the legal drafting function of the source sentence.

### claude-haiku-4-5

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `provenance, translator_notes`
- confidence: `0.99`

Reason:

The source sentence is a single cross-reference definition: the term 'Live Date' is defined elsewhere in Section 1.3. The IR faithfully captures this by introducing DefinedTerm and DocumentPart entities and a relation stating that the term's meaning is defined in that section. The provenance and translator notes confirm this is the intended reading and explicitly reject alternative interpretations (deontic obligation, duplication of substantive content). No semantic divergence exists between source and IR.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR uses entity names LiveDateTerm and Section1_3 (snake_case) to represent the quoted term and section reference; these are conventional IR naming choices and do not alter meaning.
- The relation name term_shall_have_meaning_defined_in_section is verbose but explicit; it clarifies that 'shall' here is definitional, not deontic.

### deepseek-v4-pro

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `none`
- confidence: `1.0`

Reason:

The IR directly encodes the source statement as a fact relating a DefinedTerm entity (LiveDateTerm) and a DocumentPart entity (Section1_3) via a relation that captures the definitional cross-reference.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The relation name 'term_shall_have_meaning_defined_in_section' is a literal rendering of the source phrasing, which is stylistically acceptable.

### qwen/qwen3.6-plus

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `provenance, translator_notes`
- confidence: `1.0`

Reason:

The IR accurately captures the source sentence as a cross-reference definition, mapping the quoted term to a DefinedTerm entity, the target location to a DocumentPart, and the definitional link to a dedicated relation. The corpus context explicitly validates the decision to treat 'shall' as non-deontic legal drafting and to defer substantive definition content to the referenced section. No semantic divergence exists between the source and the IR.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The relation name `term_shall_have_meaning_defined_in_section` is highly specific to this exact phrasing; a more generalized name like `term_defined_in` could improve reusability if this pattern recurs, but the current naming is precise and unambiguous.
