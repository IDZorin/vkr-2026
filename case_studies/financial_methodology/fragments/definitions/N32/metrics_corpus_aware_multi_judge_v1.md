# Corpus-Aware Multi Judge: N32

- generated_at: `2026-05-10T20:19:00+02:00`
- skipped: `False`
- local_source_alignment_mode: `corresponds`
- corpus_alignment_mode: `corresponds`
- corpus_alignment_agreement: `1.0`
- needs_context_count: `0`
- mean_confidence: `0.988`

## Included Context

```json
{
  "entry": "N32",
  "entry_dir": "<PRIVATE_WORKSPACE>\\case_studies\\financial_methodology\\definitions\\N32",
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

The IR captures the source as a definitional cross-reference: the quoted term is modeled as a DefinedTerm, Section 1.4 as a DocumentPart, and the fact states that the term has its meaning defined in that section. This matches the source sentence and the documented translation intent.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR uses a symbolic term name without punctuation, which is a naming choice rather than a semantic change.
- The relation name is verbose but consistent with the documented definitional-reading convention.

### gpt-5.4

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `none`
- confidence: `0.98`

Reason:

The local IR captures the sole source claim: the defined term "WM / Refinitiv Rate" has its meaning defined in Section 1.4. The IR does not add substantive Section 1.4 content or misread "shall" as an obligation; it records the definitional cross-reference expressed in the source.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR normalizes the quoted phrase "WM / Refinitiv Rate" into the entity name WMRefinitivRateTerm.
- Section 1.4 is represented abstractly as DocumentPart entity Section1_4 rather than preserving the exact textual formatting.
- The relation name term_shall_have_meaning_defined_in_section is a formalized paraphrase of the drafting phrase rather than a verbatim rendering.

### claude-haiku-4-5

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `provenance, translator_notes`
- confidence: `0.98`

Reason:

The source sentence is a cross-reference definition stating that the term 'WM / Refinitiv Rate' has its meaning defined in Section 1.4. The IR faithfully captures this by introducing a DefinedTerm entity for the quoted term, a DocumentPart entity for the referenced section, and a relation asserting that the term's meaning is defined in that section. The provenance and translator notes confirm this interpretation and explicitly reject alternative readings (e.g., treating 'shall' as deontic obligation or duplicating substantive content). No semantic divergence exists between source and IR.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- Entity name 'WMRefinitivRateTerm' uses camelCase abbreviation; source uses quoted string with spaces and slash. This is standard IR naming convention, not semantic drift.
- Entity name 'Section1_4' uses underscore notation; source uses 'Section 1.4'. Again, standard IR entity naming, not semantic content change.

### deepseek-v4-pro

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `provenance, translator_notes`
- confidence: `1.0`

Reason:

The IR directly encodes the source sentence: a fact linking the defined term 'WM / Refinitiv Rate' to the section where its meaning is defined, Section 1.4. The relation precisely captures the definitional cross-reference without distortion.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The entity name 'WMRefinitivRateTerm' normalizes the quoted source phrase 'WM / Refinitiv Rate' by removing slashes and converting to camel case, a common naming convention in formal ontologies.
- The relation name 'term_shall_have_meaning_defined_in_section' includes the word 'shall' from the source, which is acceptable but the source's 'shall' is legal-definition drafting, not deontic obligation, and the IR correctly does not model it as an obligation.

### qwen/qwen3.6-plus

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `provenance, translator_notes`
- confidence: `1.0`

Reason:

The IR faithfully captures the source sentence as a definitional cross-reference, linking the quoted term to the specified document section. The relation name and entity types directly mirror the source structure. Corpus context confirms the intentional treatment of 'shall' as definitional rather than deontic and validates the deferral of substantive rate logic to the referenced section.

Semantic differences:

- none

Context-resolved issues:

- Potential ambiguity around the modal 'shall' being interpreted as a deontic obligation is resolved by explicit translator notes and provenance, confirming it functions purely as a definitional pointer.

Stylistic notes:

- The relation name is highly descriptive and closely tracks the source legal phrasing, which is appropriate for cross-reference definitions.
