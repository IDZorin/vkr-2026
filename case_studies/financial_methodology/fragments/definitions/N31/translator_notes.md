# N31 Translator Notes

This file records translator decisions for the current `main_ir.a4v3`.

## Changelog

### 2026-05-20T00:00:00+02:00

Decision: make "most recent published" contextual to the Index Component and Trading Day.

Accepted:

- Replaced global `most_recent_published_trade(t)` with `most_recent_published_trade_for(t, c, d)`.
- Kept explicit temporal ordering and uniqueness constraints for the contextual most-recent trade.

Rationale:

- The source defines Trading Price "in respect of an Index Component and a Trading Day".
- A global most-recent trade would be stronger than the source and could incorrectly compare trades across unrelated components or days.
- The contextual predicate keeps the comparative phrase formal while preserving the source scope.
