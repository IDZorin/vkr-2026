# N26 Translator Notes

This file records translator decisions for the current `main_ir.a4v3`.

## Changelog

### 2026-05-20T00:00:00+02:00

Decision: define scheduled Rebalance Day and Rebalance Day predicates over `Day`.

Accepted:

- Changed `scheduled_rebalance_day`, `rebalance_day`, and `immediately_following_eligible_rebalance_day_after` to use `Day`-typed arguments.
- Kept `RebalanceDay` and `ScheduledRebalanceDay` sorts as local category names for bridge/canonical alignment.
- Added a structural definition for `immediately_following_eligible_rebalance_day_after` using `strictly_before` and a no-intermediate-eligible-day condition.

Rationale:

- The source defines which days count as Rebalance Days.
- Defining the predicates over `Day` avoids a circular-looking pattern where only already-typed `RebalanceDay` values are checked against the definition.
- This also aligns the local `eligible_rebalance_day : Day` predicate with the canonical calendar vocabulary.
- The phrase "immediately following" carries ordering semantics; the added constraint makes that ordering explicit instead of relying only on the relation name.

### 2026-05-17T00:45:00+02:00

Decision: expose the ordinal in "first Wednesday" as numeric value `1`.

Accepted:

- Replaced `first_wednesday_in_month(day, month)` with `nth_wednesday_in_month(day, month, ordinal)`.
- Added `FirstWeekdayOrdinal = 1`.

Rationale:

- `first` is not just a proper-name fragment here; it is the ordinal that determines which Wednesday in May and November is scheduled.
- Making the ordinal explicit keeps the rule extensible for future phrases such as "second Wednesday" without inventing a new relation name.
