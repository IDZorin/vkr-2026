# Corpus-Aware Multi Judge: N22

- generated_at: `2026-05-10T20:01:45+02:00`
- skipped: `False`
- local_source_alignment_mode: `corresponds`
- corpus_alignment_mode: `corresponds`
- corpus_alignment_agreement: `1.0`
- needs_context_count: `0`
- mean_confidence: `0.978`

## Included Context

```json
{
  "entry": "N22",
  "entry_dir": "<PRIVATE_WORKSPACE>\\case_studies\\financial_methodology\\definitions\\N22",
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

The IR captures the quoted defined term and its cross-reference to Section 2.1 without turning the sentence into an obligation. The provenance and translator notes explicitly confirm this is a definitional reference, matching the source exactly.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- `IndexUniverseRequirementsTerm` is a normalized entity name for the quoted term.
- `Section2_1` is a document-part identifier for the cited section.

### gpt-5.4

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `none`
- confidence: `0.98`

Reason:

The IR captures the sole source claim as a definitional cross-reference: the defined term "Index Universe Requirements" has its meaning defined in Section 2.1. This matches the source sentence, and there is no contradiction, omission, or added substantive rule in the local IR.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR uses a generic relation name `term_shall_have_meaning_defined_in_section` rather than repeating the exact legal drafting phrase; this is wording normalization, not semantic drift.
- `IndexUniverseRequirementsTerm` and `Section2_1` are normalized symbol names for the quoted term and referenced section.

### claude-haiku-4-5

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `provenance, translator_notes`
- confidence: `0.98`

Reason:

The source sentence 'Index Universe Requirements' shall have the meaning as defined in Section 2.1 is faithfully encoded in the IR as a cross-reference definition. The IR introduces a DefinedTerm entity for the quoted term, a DocumentPart entity for the referenced section, and a relation stating that the term's meaning is defined in that section. The provenance and translator notes confirm this is the intended reading: the 'shall' is definitional, not deontic, and the IR correctly avoids duplicating substantive content from Section 2.1. No semantic divergence exists between source and IR.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR uses camelCase entity naming (IndexUniverseRequirementsTerm, Section2_1) which is standard a4v3 convention and does not constitute semantic drift from the source's quoted string form.
- The relation name term_shall_have_meaning_defined_in_section is a formal encoding of the source's 'shall have the meaning as defined in' phrasing; the translator notes explicitly justify treating 'shall' as definitional rather than deontic.

### deepseek-v4-pro

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `none`
- confidence: `0.95`

Reason:

The IR directly encodes the source sentence as a fact linking the defined term to the document part via a relation that captures the definitional cross-reference.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- Naming conventions use underscores and capitalization, but no semantic drift.

### qwen/qwen3.6-plus

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `provenance, translator_notes`
- confidence: `1.0`

Reason:

The IR faithfully captures the source sentence as a definitional cross-reference, mapping the quoted term to a DefinedTerm entity and the target section to a DocumentPart entity. The relation name explicitly preserves the 'shall have the meaning as defined in' phrasing while correctly avoiding a deontic interpretation. Corpus context confirms this modeling choice and validates that substantive rules from Section 2.1 are intentionally deferred to a merge layer.

Semantic differences:

- none

Context-resolved issues:

- Potential ambiguity of 'shall' as a deontic obligation vs. definitional drafting is explicitly resolved by provenance and translator notes, confirming the IR's correct non-deontic modeling.

Stylistic notes:

- The relation name term_shall_have_meaning_defined_in_section is highly descriptive and closely mirrors the source phrasing; a more normalized schema might prefer a shorter predicate like term_defined_in_section, but the current choice is clear and unambiguous.
