# Corpus-Aware Multi Judge: N06

- generated_at: `2026-05-12T13:16:35+02:00`
- skipped: `False`
- local_source_alignment_mode: `corresponds`
- corpus_alignment_mode: `corresponds`
- corpus_alignment_agreement: `1.0`
- needs_context_count: `1`
- mean_confidence: `0.97`

## Included Context

```json
{
  "entry": "N06",
  "entry_dir": "D:\\OneDrive\\Documents\\Study\\MIPT\\VKR\\research_experiments\\2026-02_pipeline\\case_studies\\financial_methodology\\definitions\\N06",
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

The IR captures the single source sentence as a named CalculationTime entity that is the calculation time of the Index’s closing level and is outlined in Section 1.4. The provenance and translator notes confirm this is intended as a local definitional fact, not a universal rule, and the Section 1.4 reference is only a target, not imported content.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR uses a structured relation and a named entity rather than the spaced source phrase; this is a modeling choice, not a semantic change.

### gpt-5.4

- local_source_alignment: `partially_corresponds`
- corpus_alignment: `corresponds`
- relation_type: `same_meaning_poor_wording`
- needs_context: `True`
- context_used: `provenance, translator_notes`
- confidence: `0.89`

Reason:

The local IR captures the core definitional content that Close of Business is the calculation time of the closing level of the Index and links it to Section 1.4, but source-only it is slightly underdetermined because the phrase "as outlined in Section 1.4" could modify the closing-level calculation time rather than assert that Close of Business itself is outlined there. The documented provenance and translator notes explicitly state that Section 1.4 is being represented as a reference target without importing its mechanics, which resolves the intended reading and makes the translation acceptable at corpus level.

Semantic differences:

- none

Context-resolved issues:

- Source-only, the attachment of "as outlined in Section 1.4" is somewhat ambiguous; corpus documentation clarifies that the IR intentionally models it as a reference from the defined calculation time to Section 1.4.
- Source-only, the IR's use of a named CalculationTime entity rather than a fuller imported Section 1.4 definition could look incomplete; provenance and translator notes explicitly justify that this section is only a local definitional stub and not the place to encode Section 1.4 mechanics.

Stylistic notes:

- The relation name `outlined_in_section` is a structural paraphrase rather than a close lexical rendering of the source wording.
- `calculation_time_of_closing_level_of_index` is a compressed ontology label for the source noun phrase and reads less naturally than the source sentence.
- The IR uses `TheIndex` and `Section1_4` as local identifiers, which is naming normalization rather than semantic drift.

### claude-haiku-4-5

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `provenance, translator_notes`
- confidence: `0.98`

Reason:

The source sentence makes a single definitional claim: 'Close of Business' is the calculation time of the closing level of the Index as outlined in Section 1.4. The IR captures this exactly via two relations: calculation_time_of_closing_level_of_index(CloseOfBusiness, TheIndex) and outlined_in_section(CloseOfBusiness, Section1_4). The provenance and translator notes document the deliberate choice to model this as a named CalculationTime entity rather than a universal rule or event, which is faithful to the source's identification of a specific term. No contradiction exists between source and IR.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR uses camelCase identifiers (CloseOfBusiness, TheIndex, Section1_4) while the source uses spaced phrases and quoted terms; this is standard IR naming convention and does not constitute semantic drift.
- The relation names (calculation_time_of_closing_level_of_index, outlined_in_section) are verbose but directly trace to source phrases; they prioritize traceability over brevity.

### deepseek-v4-pro

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `none`
- confidence: `1.0`

Reason:

The IR fact directly captures the source definition: CloseOfBusiness is a calculation time of the closing level of the Index as outlined in Section 1.4. No semantic drift.

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

The IR directly maps the source definition to a named CalculationTime entity (CloseOfBusiness) linked to TheIndex and Section1_4 via explicit relations. The conjunction of relations accurately captures the source's compound predicate without adding or omitting semantic content. Corpus context confirms the deliberate choice to avoid universal quantification or cross-section imports, aligning perfectly with the source's intent.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- Relation names are verbose but directly trace to source phrases.
- Splitting the definition into two conjunctive relations is a standard structural normalization for compound predicates.
