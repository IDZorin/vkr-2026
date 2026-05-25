# Corpus-Aware Multi Judge: N19

- generated_at: `2026-05-12T13:11:20+02:00`
- skipped: `False`
- local_source_alignment_mode: `corresponds`
- corpus_alignment_mode: `corresponds`
- corpus_alignment_agreement: `1.0`
- needs_context_count: `0`
- mean_confidence: `0.966`

## Included Context

```json
{
  "entry": "N19",
  "entry_dir": "D:\\OneDrive\\Documents\\Study\\MIPT\\VKR\\research_experiments\\2026-02_pipeline\\case_studies\\financial_methodology\\definitions\\N19",
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

The IR matches the source definition: it states that an Index Component is exactly a security reflected in the Index, using a biconditional over Security and the local TheIndex placeholder. The documented provenance and translator notes confirm this is an intentional definitional encoding, not a weaker implication or a different claim.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- TheIndex is a local placeholder for “the Index”; the relation names are structural rather than source wording, but this does not change meaning.

### gpt-5.4

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `none`
- confidence: `0.97`

Reason:

The local IR faithfully renders the single source sentence as a definition: for every Security, being an index_component of TheIndex holds iff being reflected in TheIndex holds. This matches the source’s definitional force for "Index Component" and its reference to each security reflected in the Index. Corpus materials confirm the same reading but are not needed to resolve any apparent mismatch.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR uses a local entity name `TheIndex` for the source phrase "the Index"; this is a naming choice, not semantic drift.
- The source phrase "Index Component" is modeled as a relation `index_component` rather than as a separate subtype; this is an acceptable representational choice for a definition.
- `Security extends FinancialInstrument` adds ontology detail not stated in the sentence, but it does not alter the meaning of the definitional constraint.

### claude-haiku-4-5

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `provenance, translator_notes`
- confidence: `0.98`

Reason:

The source sentence 'Index Component is each security reflected in the Index' is a definitional claim that establishes equivalence between the term 'Index Component' and the condition 'security reflected in the Index'. The IR captures this via a biconditional constraint over the Security sort, with index_component(s, TheIndex) iff security_reflected_in_index(s, TheIndex). The universal quantification correctly represents 'each security', and the biconditional correctly encodes the definitional nature of the source. Provenance and translator notes confirm this interpretation and justify the design choices (local TheIndex entity, biconditional rather than one-way implication, no separate IndexComponent subtype).

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR uses two relation names (index_component and security_reflected_in_index) where the source uses one term ('Index Component') and one phrase ('reflected in the Index'). This is a vocabulary design choice, not a semantic divergence; provenance explicitly documents the mapping.
- TheIndex is introduced as a local entity rather than cross-referenced to a canonical index definition. Provenance notes this is intentional and defers cross-section identity to merge work.

### deepseek-v4-pro

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `none`
- confidence: `0.95`

Reason:

The IR's constraint directly encodes the source definition as a biconditional between being an Index Component and being reflected in the Index. The introduction of Security extends FinancialInstrument does not contradict the source and is a standard interpretation.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- IR uses underscore identifiers (e.g., index_component) rather than spaced source phrases; this is a non-semantic naming convention.

### qwen/qwen3.6-plus

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `provenance, translator_notes`
- confidence: `0.95`

Reason:

The IR formalizes the source definition by mapping 'Index Component' and 'reflected in the Index' to relations over Security and TheIndex, connected via a biconditional constraint. Universal quantification correctly captures 'each security'. The additional sort and entity declarations are standard IR scaffolding that preserve the source meaning without introducing drift. Corpus context explicitly validates the definitional biconditional, the local scoping of TheIndex, and the inheritance pattern for Security, confirming full alignment.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR introduces a separate relation `security_reflected_in_index` to explicitly model the source phrase 'reflected in the Index', which is a structural choice for clarity rather than a direct lexical mapping.
- `Security extends FinancialInstrument` follows a documented cross-section pattern rather than being explicitly stated in the source sentence.
