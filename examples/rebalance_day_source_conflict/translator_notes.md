# Translator Notes

## Source-Conflict Preservation

This fragment intentionally preserves a source-level conflict between two clauses:

- The fallback clause says that if the scheduled rebalance day is not a trading day, the immediately following trading day is the Rebalance Day.
- The no-postponement clarification says that in the same scheduled-non-trading scenario, the Rebalance Day is fixed and is not postponed.

The local IR therefore keeps both source claims as separate constraints. This is not an operational resolution rule. A later process or canonical policy layer may choose a precedence rule, but the local translation remains source-faithful and conflict-preserving.

## Compact Month Encoding

`RebalanceQuarterMonth` is a closed local enum for the source-listed months `March`, `June`, `September`, and `December`. The scheduled-day definition quantifies over this scoped enum to avoid repeating four `or` branches while still keeping the month list source-visible and safe under merge with a broader canonical `Month` sort.

## Arity Note

`nth_friday_in_month(day, month, ordinal)` is intentionally ternary because the source phrase binds all three roles: candidate day, listed month, and weekday ordinal. A carrier-style decomposition would be possible, but the ternary relation is clearer for this small calendar definition.
