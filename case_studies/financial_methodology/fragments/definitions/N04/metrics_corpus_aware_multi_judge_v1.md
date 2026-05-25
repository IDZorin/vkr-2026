# Corpus-Aware Multi Judge: N04

- generated_at: `2026-05-10T19:24:29+02:00`
- skipped: `False`
- local_source_alignment_mode: `corresponds`
- corpus_alignment_mode: `corresponds`
- corpus_alignment_agreement: `1.0`
- needs_context_count: `0`
- mean_confidence: `0.992`

## Included Context

```json
{
  "entry": "N04",
  "entry_dir": "D:\\OneDrive\\Documents\\Study\\MIPT\\VKR\\research_experiments\\2026-02_pipeline\\case_studies\\financial_methodology\\definitions\\N04",
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
- confidence: `0.99`

Reason:

The IR states that Business Day holds exactly for days whose weekday is Monday through Friday, which matches the source definition. The provenance and translator notes confirm the intended biconditional reading and the expansion of the range into the five weekdays, but they are not needed to resolve any mismatch.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR uses the predicate name business_day and the prelude function WeekdayOf to make the definition explicit; this is a wording/representation choice, not a semantic difference.

### gpt-5.4

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `none`
- confidence: `0.98`

Reason:

The IR faithfully renders the source as a definition: a day is a business day iff its weekday is Monday, Tuesday, Wednesday, Thursday, or Friday. Expanding the range phrase "from Monday to Friday" into the five listed weekdays preserves the source meaning, and the biconditional matches the definitional wording.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR uses the identifier `business_day` for the quoted source term "Business Day".
- The source phrase "every weekday from Monday to Friday" is rendered extensionally by enumerating Monday through Friday via `WeekdayOf(d)`.
- The IR makes the weekday dimension explicit with `WeekdayOf` rather than leaving it implicit in the predicate name.

### claude-haiku-4-5

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `provenance, translator_notes`
- confidence: `0.99`

Reason:

The source sentence 'Business Day is every weekday from Monday to Friday' is directly and faithfully encoded in the IR constraint as a biconditional over Day, where business_day(d) holds iff WeekdayOf(d) is one of the five explicitly listed weekdays. The expansion of the range 'from Monday to Friday' into the five discrete weekday values is justified by the source phrase itself and documented in provenance. No contradiction exists between source and IR; the corpus context confirms the translator's deliberate choice to use a biconditional (not merely an implication) because the source is definitional.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR uses the predicate identifier 'business_day' (lowercase, underscore) while the source uses the quoted term '"Business Day"' (title case, spaced). This is standard IR naming convention and does not constitute semantic drift.
- The IR makes explicit use of the prelude function WeekdayOf(d) to expose the weekday dimension, whereas the source uses the informal phrase 'every weekday'. This is a design choice documented in translator notes and does not alter the meaning.
- The disjunction of five weekday cases in the IR is the faithful expansion of the source's range notation 'from Monday to Friday', explicitly justified in provenance.

### deepseek-v4-pro

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `none`
- confidence: `1.0`

Reason:

The IR defines business_day as a predicate over Day, using a biconditional over the five weekdays from Monday to Friday. This exactly matches the source definitional sentence.

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

The source defines 'Business Day' as encompassing all weekdays from Monday through Friday. The IR accurately captures this as a biconditional constraint over the Day sort, explicitly enumerating the five weekdays via the prelude WeekdayOf function. The translation is semantically exact and fully consistent with the documented provenance and translator notes.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- none
