# Corpus-Aware Multi Judge: section_5_3

- generated_at: `2026-05-10T13:01:06+02:00`
- skipped: `False`
- local_source_alignment_mode: `corresponds`
- corpus_alignment_mode: `corresponds`
- corpus_alignment_agreement: `0.5`
- needs_context_count: `0`
- mean_confidence: `0.9`

## Included Context

```json
{
  "entry": "section_5_3",
  "entry_dir": "D:\\OneDrive\\Documents\\Study\\MIPT\\VKR\\research_experiments\\2026-02_pipeline\\case_studies\\financial_methodology\\sections\\section_5_3",
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
- confidence: `0.96`

Reason:

The IR captures the section’s claims and deontic structure: final and binding application, mandatory application of the described method, possible change reasons, permitted deemed changes with the listed qualitative conditions, no duty to provide information, and the obligation to take appropriate steps for consistency. The local symbols and predicates are source-grounded, and the corpus notes confirm the chosen deontic approximations and modeling decisions.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- Some source phrases are normalized into legal/structural predicates (e.g. 'final and binding', 'not obliged') rather than mirrored verbatim, but this is faithful modeling rather than drift.
- The use of VagueTerm entities for 'obvious', 'demonstrable', 'necessary', and 'desirable' is a stylistic/representation choice documented in the notes.

### gpt-5.4

- local_source_alignment: `partially_corresponds`
- corpus_alignment: `partially_corresponds`
- relation_type: `partial_overlap`
- needs_context: `False`
- context_used: `provenance, translator_notes`
- confidence: `0.84`

Reason:

The IR captures most of the section's structure and deontic content well: final/binding application, duty to apply the described method, possible reasons for changes, permitted change class, no-duty-to-inform approximated deontically, and the final duty to take appropriate steps for consistency. However, the local IR overstates the source in two places: it models the permitted changes as requiring both necessity and desirability rather than what the administrator deems necessary and desirable, and it turns the source's disjunctive permission to change terms and conditions and/or the calculation method into an exclusive either-or condition for each DeemedModificationOrChange. Corpus notes acknowledge some approximation choices but do not eliminate these semantic mismatches.

Semantic differences:

- `deemed_modification_or_change_scope` requires both `deemed_by(ch, ..., Necessary)` and `deemed_by(ch, ..., Desirable)`, whereas the source says the administrator may make changes that it deems 'necessary and desirable'; the IR thereby hard-codes both labels rather than directly representing the combined evaluative phrase, which may be stronger or at least more specific than the text.
- `deemed_modification_or_change_scope` says each DeemedModificationOrChange changes either the Index terms and conditions or the applied calculation method. The source permits changes to the terms and conditions of the Index and the method applied to calculate the Index, which supports changes affecting both; the IR excludes that possibility for this subtype.
- The permission `not_provide_information_on_modification_or_change` is only an approximation of 'is not obliged to provide information'; this is weaker as a mismatch than the two issues above, but it is not exact equivalence.

Context-resolved issues:

- Provenance and translator notes clarify that `potential_method_change_reasons` is intended as possibility only, not as assertion that changes actually occur.
- Provenance and translator notes clarify that the final consistency clause is intentionally modeled as an obligation rather than a hard invariant, preserving violability rather than making compliance logically necessary.
- Provenance and translator notes clarify that the no-information clause is intended as a deontic approximation, not as an obligation to withhold information.
- Local placeholder entities such as `TheIndex`, `ThisDocument`, and `DescribedMethod` are source-grounded local anchors rather than unsupported cross-section imports.

Stylistic notes:

- Using `VagueTerm` entities (`Obvious`, `Demonstrable`, `Necessary`, `Desirable`) is a reasonable modeling choice and not by itself semantic drift.
- `AppropriateSteps` as a named step entity is a structural convenience for the final obligation.
- `calculation_method_applied(TheIndex)` is a more formal rendering of 'the method applied to calculate the Index'.
