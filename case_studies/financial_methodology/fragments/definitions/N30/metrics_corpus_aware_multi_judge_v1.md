# Corpus-Aware Multi Judge: N30

- generated_at: `2026-05-12T22:36:20+02:00`
- skipped: `False`
- local_source_alignment_mode: `corresponds`
- corpus_alignment_mode: `corresponds`
- corpus_alignment_agreement: `0.8`
- needs_context_count: `0`
- mean_confidence: `0.94`

## Included Context

```json
{
  "entry": "N30",
  "entry_dir": "<PRIVATE_WORKSPACE>\\case_studies\\financial_methodology\\definitions\\N30",
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
- context_used: `none`
- confidence: `0.98`

Reason:

The IR tracks the source’s Trading Day definition with a reified context, the two component-scope cases, the open-for-trading and market-disruption counterfactual branches, the two exclusions, the clarification about new Index Components, and the final responsibility sentence. No documented corpus context is needed to reconcile the source with the IR.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR is more formal and reified than the source, but this is a modeling choice rather than a semantic change.

### gpt-5.4

- local_source_alignment: `partially_corresponds`
- corpus_alignment: `partially_corresponds`
- relation_type: `partial_overlap`
- needs_context: `False`
- context_used: `provenance, translator_notes`
- confidence: `0.84`

Reason:

The IR captures the main structure of the definition: scope over components at the Rebalance Day or immediately following Calculation Day, the open-for-trading branch, the market-disruption counterfactual branch, the two exclusions, and the Index Administrator's ultimate responsibility. However, the parenthetical clarification is only represented as a separate clarification predicate and is not linked into the core Trading Day scope or definition, so the IR does not fully encode that the provision is intended to capture those new Index Components. In addition, the source says 'every Index Component' in the scoped classes, while the IR defines valid contexts and conditions for arbitrary contexts rather than explicitly asserting universal coverage over all such components/days.

Semantic differences:

- The parenthetical clarification about securities to be included in the Index as new Index Components with close of trading on the relevant Exchange on the Rebalance Day is modeled only as a separate predicate `context_captures_new_index_component_close_of_trading` and does not affect or connect to `valid_trading_day_context` or `trading_day`, so the intended capture is not fully integrated into the operative definition.
- The source's scoped phrase includes 'every Index Component included in the Index at the Calculation Day immediately following the Rebalance Day' (and similarly the Rebalance Day class), but the IR mainly characterizes when a given context qualifies; it does not explicitly state universal coverage over all such components or otherwise force existence/coverage of contexts for each such component.

Context-resolved issues:

- The reified `TradingDayContext` and `TradingDayDetermination` are documented and consistent with the source; this is a modeling choice rather than semantic drift.
- The market-disruption branch is correctly treated as a counterfactual open-for-trading condition rather than as disruption itself being a positive Trading Day condition.
- The two exclusions are correctly separated and assembled negatively in the final Trading Day definition.
- Responsibility is localized to `TheIndexAdministrator` for determinations of whether a context is a Trading Day, matching the final sentence's authority allocation.

Stylistic notes:

- `Exchange` is introduced as an unconstrained sort rather than extending a prelude sort such as Organization; this is an ontology choice, not a demonstrated semantic error from the local source.
- `TradingCessationPossibility` and `ScheduledShortenedPeriod` are reified helper constructs used to unpack dense source wording.
- The IR decomposes one long sentence into helper predicates and a final assembly constraint; this improves auditability but changes presentation.

### claude-haiku-4-5

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `provenance, translator_notes`
- confidence: `0.98`

Reason:

The IR faithfully represents the source definition of Trading Day through a carefully decomposed set of constraints. Each source clause—the component scope (Rebalance Day and following Calculation Day), the positive conditions (open for trading or market-disruption counterfactual), the two exclusions (prior-to-close cessation and scheduled shortened period), the clarification about new Index Components, and the Index Administrator responsibility—is explicitly captured in the provenance ledger with source quotes and back-translations. The reification of TradingDayContext and TradingDayDetermination is a sound modeling choice documented in translator notes and does not contradict the source. No semantic drift is present.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The source uses a long compound sentence; the IR decomposes it into nine separate constraints for auditability. This is a structural choice, not a semantic change.
- The source phrase 'with respect to an Index Component' is reified as a TradingDayContext carrying roles (day, component, rebalance day, exchange). This avoids high-arity relations and is explicitly justified in translator notes.
- The market-disruption clause 'or a day that would have been such a day if a market disruption had not occurred' is correctly modeled as a conjunction of market_disruption_occurred AND would_have_been_open_for_trading_without_market_disruption, preserving the counterfactual polarity (disruption alone does not qualify; only disruption + would-have-been-open does).
- The exclusion 'trading may be ceased prior to the scheduled Exchange closing time' is reified as TradingCessationPossibility with a prior_to relation to scheduled_exchange_closing_time. The translator notes explicitly reject modeling this as a positive condition and correctly represent it as an exclusion.
- The parenthetical clarification about new Index Components is separated into its own constraint (new_index_components_close_of_trading_clarification) rather than silently merged into the main definition. This preserves traceability.
- The final responsibility sentence is modeled via TradingDayDetermination and ultimately_responsible_for_trading_day_determination, which is more precise than a generic obligation and is justified in translator notes.

### deepseek-v4-pro

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `provenance, translator_notes`
- confidence: `0.95`

Reason:

The IR fully captures all source clauses: the scoped definition of Trading Day relative to Index Components at Rebalance Day or the following Calculation Day, the open-for-trading and market-disruption counterfactual conditions, the two exclusions, the clarification about new Index Components, and the Index Administrator's responsibility. The reified TradingDayContext pattern faithfully encodes the 'with respect to' dependencies without loss.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- IR adopts a reified TradingDayContext to carry scope roles, which is a formalization choice suitable for the source's relational phrasing.
- Relation names are descriptive and long, typical of auto-generated IR.
- Separate helper constraints decompose the dense source sentence into auditable pieces.

### qwen/qwen3.6-plus

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `provenance, translator_notes`
- confidence: `0.95`

Reason:

The IR faithfully captures all semantic components of the source definition: the component scope (Rebalance Day and following Calculation Day), the positive trading condition (open or counterfactual disruption), the two explicit exclusions (early cessation and shortened period), the parenthetical clarification, and the Index Administrator's authority. The reified context and constraint decomposition are structural modeling choices that preserve exact logical equivalence without altering meaning.

Semantic differences:

- none

Context-resolved issues:

- Initial appearance of over-reification (TradingDayContext, TradingDayDetermination) is resolved by translator notes explaining it avoids high-arity predicates and separates logical clauses for auditability.
- Counterfactual polarity of the market disruption clause is explicitly clarified in notes to ensure it requires both disruption occurrence and hypothetical openness, matching the source's 'would have been such a day if...' phrasing.

Stylistic notes:

- Decomposition of a single dense source sentence into multiple helper constraints improves modularity but does not change semantics.
- prior_to is modeled as a static ordering relation rather than a temporal logic operator, aligning with the source's lack of trace-temporal semantics.
