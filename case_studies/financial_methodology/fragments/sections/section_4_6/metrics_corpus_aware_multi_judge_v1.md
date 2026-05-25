# Corpus-Aware Multi Judge: section_4_6

- generated_at: `2026-05-11T10:36:45+02:00`
- skipped: `False`
- local_source_alignment_mode: `corresponds`
- corpus_alignment_mode: `corresponds`
- corpus_alignment_agreement: `1.0`
- needs_context_count: `0`
- mean_confidence: `0.964`

## Included Context

```json
{
  "entry": "section_4_6",
  "entry_dir": "<PRIVATE_WORKSPACE>\\case_studies\\financial_methodology\\sections\\section_4_6",
  "global_bridge": true,
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
- context_used: `none`
- confidence: `0.97`

Reason:

The IR captures all source claims: best-efforts to calculate and maintain indices, possible errors not completely ruled out with internal/external reasons, correction of identified errors within a reasonable period, the underlying-dependent understanding and measures, and the correction policy’s incorporation by reference and website availability. The corpus context is consistent with the local IR and does not change the reading.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- Some source phrases are rendered with carrier entities and relations rather than direct natural-language wording, but this is a modeling choice rather than semantic drift.
- The guideline target of the incorporation-by-reference relation is named `ThisGuideline`, which is a local document carrier rather than a textual quote.

### gpt-5.4

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `none`
- confidence: `0.97`

Reason:

The local IR faithfully captures the section’s claims: Solactive’s greatest possible efforts regarding accurate calculation and maintenance of its indices, the possibility of determination-process errors occurring from time to time for internal or external reasons and not being completely ruled out, Solactive’s endeavor to correct identified determination-process errors within a reasonable period, the dependence of the understanding of that period and general measures on the underlying, and the specification/reference status of the Solactive Correction Policy on the Solactive website. Corpus materials mainly confirm and explain these modeling choices rather than fixing any mismatch.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR uses structural carrier entities such as `Effort`, `ErrorPossibility`, `Understanding`, and `PolicySpecification`; this is a modeling choice, not semantic drift.
- `cannot be completely ruled out` is represented via explicit negation of `completely_ruled_out(...)`, which is semantically appropriate though stylistically indirect.
- `variety reasons` is preserved literally as a vague-term carrier despite the apparent source typo; this is faithful to source wording.
- `ThisGuideline` is a local document carrier for the incorporation-by-reference target; the source does not name the host document explicitly, but the relation direction matches the sentence.

### claude-haiku-4-5

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `provenance, translator_notes`
- confidence: `0.98`

Reason:

The main_ir.a4v3 faithfully translates all substantive claims in the source text. Every source sentence maps to at least one IR declaration (fact, constraint, or relation), and no IR formula contradicts the source. The provenance ledger and translator notes document the translation decisions (e.g., using ErrorPossibility rather than asserting actual errors, representing 'cannot be completely ruled out' as explicit negation, treating 'endeavors' as best-effort rather than strict obligation) and these decisions are consistent with the source phrasing and the a4v3 specification. The IR introduces no cross-section claims, no domain-knowledge inferences, and no content beyond what the source text and prelude justify.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The source uses the informal phrase 'for variety reasons' (likely a typo for 'for a variety of reasons'); the IR captures this as VarietyReasons, a VagueTerm carrier, preserving the source's vagueness without correcting it.
- The source says 'depending on the underlying' without naming a specific underlying; the IR models this as an existential dependency fact rather than a universal rule, which is appropriate for source-level vagueness.
- The relation name 'incorporated_by_reference_into' is directional (policy into guideline) and matches the source's phrasing 'incorporated by reference'; the IR does not invent a URL because the source names the website but does not print a concrete URL.
- The source uses 'endeavors to correct', which the translator notes correctly treat as a best-effort commitment (not a strict obligation), reflected in the constraint structure rather than a deontic modal.

### deepseek-v4-pro

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `none`
- confidence: `0.95`

Reason:

The IR directly captures all source claims: the greatest-possible-efforts commitment for accurate calculation/maintenance, error possibility with its qualifications, the endeavor to correct identified errors within a reasonable period, the dependency of the period understanding and measures on an underlying, and the specification by the Correction Policy. The translator’s decisions—modeling errors as a possibility, scoping universals, using an existential underlying, and treating 'endeavors' as a best-effort carrier—are faithful to the source and documented in the provenance and translator notes.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- Carrier names are long but explicit (e.g., DeterminationProcessErrorPossibility, ReasonablePeriodOfTimeUnderstanding).
- The negation 'cannot be completely ruled out' is represented as `not completely_ruled_out(...)` over a positive polarity relation, which is a clean logical choice.
- The vague term 'reasonable period of time' is properly encoded as a VagueTerm, and the one-way endeavor is modeled without deontic force.

### qwen/qwen3.6-plus

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `provenance, translator_notes`
- confidence: `0.95`

Reason:

The IR systematically translates each source sentence into structured facts and constraints, using explicit carriers for modalities, vague terms, and best-effort commitments. Provenance and translator notes confirm that design choices (e.g., ErrorPossibility for "may occur", Endeavor for "endeavors", and ThisGuideline for the implicit incorporation target) are intentional and source-grounded, resulting in full semantic alignment without contradictions.

Semantic differences:

- none

Context-resolved issues:

- The implicit target of 'incorporated by reference' is explicitly modeled as ThisGuideline, justified by provenance notes.
- The modal 'may occur' and non-deontic 'endeavors' are modeled via ErrorPossibility and Endeavor sorts rather than strict existence or obligation, aligning with translator notes.

Stylistic notes:

- Extensive use of structural carriers (Description, VagueTerm, ErrorPossibility) for source qualifiers increases IR verbosity but preserves precise semantic scoping.
- Enum sorts (IndexEffortGoal, Reason) cleanly separate adverbial modifiers from core relations.
