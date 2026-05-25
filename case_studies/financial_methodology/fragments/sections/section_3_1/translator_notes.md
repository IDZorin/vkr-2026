# Section 3.1 Translator Notes

## 2026-05-12

- The phrase "sufficient notice before the Rebalance Day" is modeled as a vague timing formula rather than as the prelude `day_before` relation.
- `SufficientNoticeBeforeRebalanceDay : VagueTerm` preserves the qualitative notice threshold without committing to a concrete number of days.
- `notice_for_rebalance_day(n, rd)` keeps the structural link between the notice and the relevant Rebalance Day, but avoids the over-specific reading "exactly the previous day".
- This is not modeled as `TemporalDecl`: the source does not introduce trace-temporal semantics (`always`, `eventually`, `until`, etc.), only a static/vague notice timing requirement.
- The publication sentence is split into a deontic obligation (`publish_index_component_change`) and structural notice properties (`solactive_publishes_index_component_changes_with_notice`).
