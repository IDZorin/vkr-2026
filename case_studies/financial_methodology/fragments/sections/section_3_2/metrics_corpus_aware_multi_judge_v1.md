# Corpus-Aware Multi Judge: section_3_2

- generated_at: `2026-05-11T09:33:33+02:00`
- skipped: `False`
- local_source_alignment_mode: `corresponds`
- corpus_alignment_mode: `corresponds`
- corpus_alignment_agreement: `1.0`
- needs_context_count: `0`
- mean_confidence: `0.988`

## Included Context

```json
{
  "entry": "section_3_2",
  "entry_dir": "<PRIVATE_WORKSPACE>\\case_studies\\financial_methodology\\sections\\section_3_2",
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
- context_used: `provenance, translator_notes, bridge`
- confidence: `0.98`

Reason:

The IR states that for every ExtraordinaryRebalance r, rebalance_of_index(r, TheIndex) does not hold, which matches the source claim that the Index is not rebalanced extraordinarily. The extra sort and relation vocabulary are supported by the provenance and translator notes, and the bridge context is not needed for this section.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR uses a hard negative constraint rather than a deontic prohibition, which is a wording choice documented in provenance.
- The subtype ExtraordinaryRebalance and the positive carrier relation rebalance_of_index are implementation choices, not semantic drift.

### gpt-5.4

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `none`
- confidence: `0.98`

Reason:

The local IR faithfully encodes the sole source claim by stating that no extraordinary rebalance event is a rebalance of TheIndex. The ontology choices (`Index`, `Rebalance`, `ExtraordinaryRebalance`, `TheIndex`, `rebalance_of_index`) are straightforward carriers for the sentence and do not add conflicting meaning. Corpus materials confirm this reading but are not needed to establish alignment.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The source's passive wording is rendered via an explicit event relation `rebalance_of_index` rather than a passive predicate; this is a modeling choice, not semantic drift.
- Negation is placed in the constraint body instead of being baked into a symbol name such as `no_extraordinary_rebalance`; this improves clarity without changing meaning.
- `ExtraordinaryRebalance extends Rebalance` makes the adverbial modifier explicit as a subtype; this is acceptable ontology wording for the source phrase 'rebalanced extraordinarily'.
- The back-translation 'has no extraordinary rebalance' is slightly more nominal than the source's passive verbal form, but semantically equivalent here.

### claude-haiku-4-5

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `provenance, translator_notes`
- confidence: `0.98`

Reason:

The source statement 'The Index is not rebalanced extraordinarily' is faithfully encoded as a hard negative constraint `not rebalance_of_index(r, TheIndex)` over an explicit positive relation and a subtype `ExtraordinaryRebalance`. The IR vocabulary (Index, Rebalance, ExtraordinaryRebalance, TheIndex, rebalance_of_index) traces directly to source phrases and prelude sorts. The provenance and translator notes document the deliberate choice to represent negation in the formula body rather than in symbol names, which is a sound translation decision that preserves contradiction-detection capability. No semantic drift or undocumented additions are present.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR uses the formal name `ExtraordinaryRebalance` (extends Rebalance) to ground the source adverb 'extraordinarily', rather than encoding it as a negative symbol name like `no_extraordinary_rebalance`. This is a deliberate design choice documented in translator notes and is semantically sound.
- The entity `TheIndex` is a local placeholder for the source phrase 'The Index'. The provenance notes that cross-section identity with published index entities belongs to the bridge layer, not the local section IR. This separation is correct and does not constitute drift.

### deepseek-v4-pro

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `provenance, translator_notes`
- confidence: `1.0`

Reason:

The IR accurately formalizes the source statement 'The Index is not rebalanced extraordinarily' as a constraint that no ExtraordinaryRebalance event is related to TheIndex via rebalance_of_index. Corpus context confirms this translation decision without contradiction.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR introduces subtypes and a relation name to capture the negation explicitly; the translation style is logical and faithful.

### qwen/qwen3.6-plus

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `provenance, translator_notes`
- confidence: `1.0`

Reason:

The source text asserts a single factual claim that the Index does not undergo extraordinary rebalancing. The IR captures this exactly by defining a Rebalance sort, an ExtraordinaryRebalance subtype, a rebalance_of_index relation, and a universal constraint that negates the relation for TheIndex. The provenance and translator notes explicitly document the deliberate choice to use a hard negative constraint over a positive relation, confirming that the IR is a faithful and precise formalization of the source.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR expands the adverb 'extraordinarily' into a dedicated subtype sort (ExtraordinaryRebalance), which is a standard ontological modeling choice that preserves the source meaning without introducing drift.
