# Definition N30 Translator Notes

This file records translator decisions for the current `main_ir.a4v3`.
It is review memory, not an additional source of methodology claims.

## Changelog

### 2026-05-12T15:05:00+02:00

Decision: represent the Trading Day definition with a reified `TradingDayContext` and a separate `TradingDayDetermination`.

Accepted:

- The positive Trading Day condition is `exchange open for trading OR market disruption occurred AND the Exchange would have been open without that disruption`.
- The market-disruption parenthetical is not encoded as `market disruption prevents trading` as a positive condition; that would reverse the source polarity.
- The two exclusions are explicit negative conditions: no prior-to-close cessation possibility, and no scheduled shortened period.
- `prior_to(cp, scheduled_exchange_closing_time(...))` is a static temporal relation between a cessation possibility and a scheduled closing-time value. It is not modeled as `TemporalDecl`, because the source does not introduce trace-temporal semantics such as `always`, `eventually`, `until`, or state transitions.
- `TradingDayContext` carries the candidate day, Index Component, Rebalance Day, and relevant Exchange roles. This avoids high-arity `trading_day(RebalanceDay, Day, Component)` relations.
- The parenthetical clarification about new Index Components and close of trading is represented as a separate traceable clarification constraint. It does not silently alter the core Trading Day definition.
- The final responsibility sentence is modeled as responsibility for a `TradingDayDetermination`, not as a generic obligation applying to every organization.
- The long source sentence is decomposed into separate helper constraints for the two component scopes, the ordinary open-for-trading branch, the market-disruption counterfactual branch, and the two exclusions. The final `trading_day_definition` only assembles these helper predicates.

Rejected / alternatives:

- Do not use `market_disruption_prevents_trading` as a positive Trading Day condition.
- Do not quantify over every `IndexAdministrator`; the source refers to the Index Administrator for this methodology.
- Do not model "may be ceased" as a positive label hidden in a name; it is an exclusion and is represented with `not exists`.
- Do not keep the Copy 1 high-arity responsibility relation; the final version uses a determination object with binary role relations.
- Do not add a dummy `TemporalDecl` for "prior to"; static temporal ordering is sufficient here.

Rationale: N30 is a dense definition with scope, counterfactual, exclusions, a clarification, and authority. The final IR keeps these layers separate so that later checks can inspect polarity and roles directly.
