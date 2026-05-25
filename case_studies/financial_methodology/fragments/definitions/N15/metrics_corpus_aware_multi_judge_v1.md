# Corpus-Aware Multi Judge: N15

- generated_at: `2026-05-12T14:34:20+02:00`
- skipped: `False`
- local_source_alignment_mode: `corresponds`
- corpus_alignment_mode: `corresponds`
- corpus_alignment_agreement: `1.0`
- needs_context_count: `0`
- mean_confidence: `0.974`

## Included Context

```json
{
  "entry": "N15",
  "entry_dir": "<PRIVATE_WORKSPACE>\\case_studies\\financial_methodology\\definitions\\N15",
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
- confidence: `0.97`

Reason:

The IR captures the source definition as a universal biconditional over Security and preserves the Section 2.1 reference via a local GbsIndex entity and fact. The separate reflected-in predicate matches the source wording, and the provenance/notes confirm this is the intended strict definitional reading.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR uses 'GbsIndex' and 'GbsIndexSpecifiedInSection2_1' as local identifiers for the source's GBS Index phrase; this is naming, not semantic drift.
- 'each security' is rendered as universal quantification over Security, which is a standard formalization choice.

### gpt-5.4

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `none`
- confidence: `0.97`

Reason:

The IR captures the single source sentence as a definition: for every Security, being a gbs_index_component of the GBS Index specified in Section 2.1 is equivalent to being reflected in that same index, and it separately records that the referenced index is the one specified in Section 2.1. This matches the source’s definitional content without adding a conflicting claim.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR reifies the phrase "GBS Index specified in Section 2.1" as the entity `GbsIndexSpecifiedInSection2_1` plus a linking fact to `Section2_1`; this is a modeling choice, not semantic drift.
- `Security extends FinancialInstrument` is ontology-level typing not stated in the sentence, but it does not alter the local definitional meaning.
- The defined term is modeled relationally as `gbs_index_component(Security, GbsIndex)` rather than as a unary predicate or subtype; this is acceptable wording/structure variation.

### claude-haiku-4-5

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `provenance, translator_notes`
- confidence: `0.98`

Reason:

The source sentence defines 'Gbs Index Component' as each security reflected in the GBS Index specified in Section 2.1. The IR captures this with a biconditional constraint (gbs_index_component_definition) that makes the term true exactly when security_reflected_in_gbs_index holds, plus a fact anchoring the GBS Index to Section 2.1. The IR vocabulary (Security, GbsIndex, gbs_index_component, security_reflected_in_gbs_index) traces directly to source phrases. No contradiction exists between source and IR; corpus context confirms the translator's deliberate choice to keep 'reflected in' as a separate predicate rather than hiding it in the relation name.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- IR uses snake_case identifiers (gbs_index_component, security_reflected_in_gbs_index) while source uses title case ('Gbs Index Component'). This is standard a4v3 naming convention, not semantic drift.
- IR introduces entity GbsIndexSpecifiedInSection2_1 as a local reference; the source phrase 'GBS Index specified in Section 2.1' is preserved in provenance vocabulary_notes. Cross-section alignment of this entity with Section 2.1's actual index definitions is deferred to bridge/merge work, as documented in provenance notes.
- IR separates gbs_index_component (the defined term) from security_reflected_in_gbs_index (the structural property). This preserves source vocabulary visibility and is justified in translator_notes as a deliberate design choice.

### deepseek-v4-pro

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `none`
- confidence: `0.95`

Reason:

The IR constraint biconditionally defines 'gbs_index_component' for the specific GBS Index entity as exactly the securities reflected in that index, exactly matching the source sentence's definitional intent.

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

The IR precisely formalizes the single-sentence definition using a biconditional constraint over the Security sort, correctly scoping it to the GBS Index referenced in Section 2.1. The separation of the defined-term relation and the 'reflected in' relation, along with the explicit DocumentPart fact, aligns perfectly with the source phrasing and is explicitly justified by the translator notes and provenance ledger.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR separates `gbs_index_component` and `security_reflected_in_gbs_index` to preserve explicit source vocabulary, as documented in translator notes.
- Entity name `GbsIndexSpecifiedInSection2_1` is descriptive but verbose; it correctly anchors the cross-reference without importing external section content.
- `Security extends FinancialInstrument` follows established domain patterns rather than appearing in the source sentence, but does not alter the definitional semantics.
