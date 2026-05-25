# Corpus-Aware Multi Judge: N05

- generated_at: `2026-05-12T13:10:31+02:00`
- skipped: `False`
- local_source_alignment_mode: `corresponds`
- corpus_alignment_mode: `corresponds`
- corpus_alignment_agreement: `1.0`
- needs_context_count: `0`
- mean_confidence: `0.992`

## Included Context

```json
{
  "entry": "N05",
  "entry_dir": "D:\\OneDrive\\Documents\\Study\\MIPT\\VKR\\research_experiments\\2026-02_pipeline\\case_studies\\financial_methodology\\definitions\\N05",
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

The IR states that Calculation Day holds exactly for days whose weekday is Monday through Friday, matching the source definition. The provenance and translator notes confirm the intended biconditional reading and the expansion of the weekday range, but they do not change the substance of the claim.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR uses the predicate name calculation_day and the explicit WeekdayOf(d) function, which is a stylistic/structural choice rather than a semantic difference.

### gpt-5.4

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `none`
- confidence: `0.98`

Reason:

The IR faithfully renders the source as a definition: a day is a Calculation Day iff its weekday is Monday, Tuesday, Wednesday, Thursday, or Friday. This matches the source phrase "every weekday from Monday to Friday" without adding or contradicting content.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR uses the identifier `calculation_day` for the quoted source term "Calculation Day".
- The source range phrase "from Monday to Friday" is spelled out extensionally as five weekday constants.
- The weekday notion is made explicit via `WeekdayOf(d)` rather than being implicit in the predicate name.

### claude-haiku-4-5

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `provenance, translator_notes`
- confidence: `0.99`

Reason:

The source sentence 'Calculation Day is every weekday from Monday to Friday' is directly and faithfully rendered as a biconditional constraint over Day. The IR predicate calculation_day(d) holds iff WeekdayOf(d) is one of the five weekdays Monday through Friday. The expansion of the range 'from Monday to Friday' into the five explicit weekday values is standard and correct. The use of a biconditional (iff) rather than a one-way implication correctly captures the definitional nature of the source claim. All vocabulary (calculation_day, WeekdayOf, the five weekday entities) traces to the source or prelude. No semantic divergence exists.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR uses the predicate name 'calculation_day' (snake_case) while the source uses the quoted phrase 'Calculation Day' (title case). This is standard identifier normalization and does not constitute semantic drift.
- The IR makes the weekday dimension explicit via the prelude function WeekdayOf(d), whereas the source phrase 'every weekday' is more colloquial. This is a clarifying design choice documented in translator notes and does not alter meaning.
- The disjunctive expansion (or-chain of five weekday comparisons) is equivalent to the source's range notation 'from Monday to Friday' and is the natural way to express it in first-order logic.

### deepseek-v4-pro

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `provenance, translator_notes`
- confidence: `1.0`

Reason:

The IR defines calculation_day as a predicate over Day, exactly equivalent to the source definition of 'Calculation Day' being every weekday from Monday to Friday. The biconditional and the explicit enumeration of weekdays capture the definition faithfully.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- IR uses lowercase predicate calculation_day instead of a quoted term; WeekdayOf function is introduced to surface the weekday dimension.

### qwen/qwen3.6-plus

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `provenance, translator_notes`
- confidence: `1.0`

Reason:

The source defines 'Calculation Day' as every weekday from Monday to Friday. The IR accurately captures this as a biconditional constraint over the Day sort, explicitly enumerating the five weekdays via the prelude WeekdayOf function. The translation preserves the definitional scope and meaning without loss or addition.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- none
