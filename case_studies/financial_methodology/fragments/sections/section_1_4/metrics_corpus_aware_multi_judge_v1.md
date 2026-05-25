# Corpus-Aware Multi Judge: section_1_4

- generated_at: `2026-05-10T11:52:01+02:00`
- skipped: `False`
- local_source_alignment_mode: `corresponds`
- corpus_alignment_mode: `corresponds`
- corpus_alignment_agreement: `0.5`
- needs_context_count: `1`
- mean_confidence: `0.925`

## Included Context

```json
{
  "entry": "section_1_4",
  "entry_dir": "D:\\OneDrive\\Documents\\Study\\MIPT\\VKR\\research_experiments\\2026-02_pipeline\\case_studies\\financial_methodology\\sections\\section_1_4",
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

The IR captures the intraday calculation window, Trading Price basis, ICE FX conversion, missing-price fallback via later_of, and the separate closing-level flow with WM Fixing conversion and last-available fallback. The extra symbols and helper structure are source-local scaffolding rather than contradictions, and the documented corpus context does not change the source-local reading.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- Some names are implementation-oriented scaffolding (e.g. intraday_source_price, closing_calculation_price, later_of) rather than source wording, but this does not affect meaning.
- The IR uses a local TheIndex entity instead of canonical cross-section index entities; that is a bridge-layer concern, not a local semantic issue.

### gpt-5.4

- local_source_alignment: `partially_corresponds`
- corpus_alignment: `partially_corresponds`
- relation_type: `partial_overlap`
- needs_context: `True`
- context_used: `provenance, translator_notes`
- confidence: `0.89`

Reason:

The IR captures the main intraday and closing-price calculation structure, currency-conversion conditions, fallback to later-of two price candidates, and WM-fixing fallback logic. Corpus context resolves that several helper constructs (`later_of`, calculation-time scaffolding, local `TheIndex`) are intentional translation devices rather than drift. However, even with context, the IR adds at least one real derived claim not explicit in the source: it states that the last-available 4:00 p.m. London WM fixing is quoted by Reuters and has that fixing time, whereas the source only explicitly attributes Reuters to the regular WM fixing sentence and does not separately state that attribution for the fallback observation.

Semantic differences:

- The fact `last_available_wm_fixing_4pm_london_quoted_by_reuters` adds that every fallback last-available 04:00 p.m. London WM Fixing is quoted by Reuters and has that fixing time; this is documented as a derived invariant, but it is still stronger than the explicit source text.

Context-resolved issues:

- `TheIndex` is a source-local stand-in for the source phrase "the Index" rather than an unsupported cross-section canonicalization.
- The helper function `later_of` is not left purely name-based: provenance and translator notes document explicit bridge constraints that make its selection behavior correspond to the source phrase "the later of".
- The use of `CalculationTime`, `CalculationMode`, and time-window relations is documented as IR scaffolding for the source phrase "from 1:00 a.m. to 10:50 p.m. CET" rather than extra business semantics.
- The no-conversion branches for prices already in the Index Currency are documented as the contraposed complement of the source's "not listed in the Index Currency are converted" condition.

Stylistic notes:

- `intraday_level_uses_exchange_trading_prices` and `closing_level_based_on_closing_prices` model "based on" via `price_used_for_level`, which is acceptable but more structural than the prose.
- `price_selection_order` is a somewhat technical helper name for the source word "later"; notes clarify it is not a value comparison relation.
- The IR explicitly separates raw source prices from post-conversion calculation prices (`intraday_source_price`/`intraday_calculation_price`, `closing_price`/`closing_calculation_price`), making an implicit source pipeline explicit.
