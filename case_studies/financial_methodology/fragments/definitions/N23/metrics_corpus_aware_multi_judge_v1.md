# Corpus-Aware Multi Judge: N23

- generated_at: `2026-05-12T14:33:36+02:00`
- skipped: `False`
- local_source_alignment_mode: `corresponds`
- corpus_alignment_mode: `corresponds`
- corpus_alignment_agreement: `1.0`
- needs_context_count: `1`
- mean_confidence: `0.962`

## Included Context

```json
{
  "entry": "N23",
  "entry_dir": "D:\\OneDrive\\Documents\\Study\\MIPT\\VKR\\research_experiments\\2026-02_pipeline\\case_studies\\financial_methodology\\definitions\\N23",
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

The IR preserves the source definition by marking the “sum of all financial instruments” phrasing and by stating the defining biconditional that a financial instrument is in the Index Universe exactly when it fulfills the Index Universe Requirements. The provenance and translator notes confirm that “sum” is intentionally treated as collection language, not arithmetic, so there is no contradiction.

Semantic differences:

- none

Context-resolved issues:

- The source phrase “sum of all” is rendered as a source-surface collection marker rather than arithmetic addition.
- The local entity names are documented as placeholders for the source terms “Index Universe” and “Index Universe Requirements.”

Stylistic notes:

- The IR is more formal and explicit than the source sentence, but this is a definitional paraphrase rather than a semantic shift.

### gpt-5.4

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `same_meaning_poor_wording`
- needs_context: `False`
- context_used: `none`
- confidence: `0.95`

Reason:

The IR captures the source definition by introducing an Index Universe, Index Universe Requirements, and a biconditional stating that a financial instrument is in the Index Universe iff it fulfills the requirements. The extra fact preserving the phrase "sum of all" is consistent with the source, though somewhat awkwardly worded as a separate relation rather than directly encoded as set-collection language.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- Using a dedicated relation `index_universe_is_sum_of_financial_instruments_fulfilling_requirements` is stylistically heavy for what is essentially source-surface wording.
- The sort names `IndexUniverse` and `IndexUniverseRequirements` are reasonable nominalizations of the quoted source terms.
- The IR operationalizes "sum of all" via membership equivalence rather than literal arithmetic, which is good methodology wording even if the source phrase is informal.

### claude-haiku-4-5

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `provenance, translator_notes`
- confidence: `0.98`

Reason:

The source sentence 'Index Universe is the sum of all financial instruments which fulfill the Index Universe Requirements' is faithfully translated into the IR via two complementary declarations: (1) a fact preserving the source-surface phrase 'sum of all' as a collection marker, and (2) a biconditional constraint that operationalizes the membership condition. The IR correctly interprets 'sum' as set-membership language rather than arithmetic addition, and the constraint forall fi: FinancialInstrument, financial_instrument_in_index_universe(fi, TheIndexUniverse) iff fulfills_index_universe_requirements(fi, TheIndexUniverseRequirements) directly encodes the definition. No semantic divergence exists between source and IR.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR uses two separate declarations (fact + constraint) to represent a single source sentence. This is a deliberate design choice documented in translator_notes to preserve both the source phrasing ('sum of all') and the operational membership semantics. Not a drift; a methodological decision.
- Entity names TheIndexUniverse and TheIndexUniverseRequirements are capitalized local references; provenance notes correctly flag that cross-section identity with Section 2.1 is deferred to bridge/merge work.

### deepseek-v4-pro

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `provenance, translator_notes`
- confidence: `0.95`

Reason:

The IR captures the source definition with a correct biconditional: an instrument is in the Index Universe iff it fulfills the requirements; the 'sum of all' phrase is treated as collection language, not arithmetic, which matches the source intent.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- none

### qwen/qwen3.6-plus

- local_source_alignment: `partially_corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `True`
- context_used: `provenance, translator_notes`
- confidence: `0.95`

Reason:

Locally, the source phrase 'sum of all' introduces ambiguity between arithmetic addition and set membership, and the IR's split into a surface fact and a biconditional constraint is not immediately obvious from the source alone. Corpus context explicitly resolves this by documenting the intentional set-membership interpretation and the rationale for preserving the source phrasing separately from the operational definition. With this context, the IR fully corresponds to the source intent.

Semantic differences:

- none

Context-resolved issues:

- Ambiguity of 'sum of all' as arithmetic vs. set membership is resolved by translator notes specifying collection semantics.
- The dual IR structure (surface fact + biconditional constraint) is justified by provenance as a deliberate traceability and operationalization strategy.

Stylistic notes:

- Relation name `index_universe_is_sum_of_financial_instruments_fulfilling_requirements` is highly verbose but intentionally preserves exact source wording for auditability.
- Singleton entities `TheIndexUniverse` and `TheIndexUniverseRequirements` appropriately reflect the definite phrasing in the source.
