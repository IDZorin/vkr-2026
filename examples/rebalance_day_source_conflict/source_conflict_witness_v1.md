# Source Conflict Witness

This sidecar SMT probe checks the intended source-level contradiction preserved in `main_ir.a4v3`.

The probe asserts a witness scenario:

- there is a scheduled rebalance day;
- that scheduled day is not a trading day;
- there is an immediately following trading day.

Under that witness, the fallback clause implies that the following day is a `rebalance_day`, while the fixed-date/no-postponement clause implies that the same following day is not a `rebalance_day`.

Expected solver result: `unsat`.

Observed solver result:

```text
status: unsat
unsat_core: ['fallback_to_following_trading_day', 'fixed_date_no_postponement_claim', 'scheduled_non_trading_witness']
```

Interpretation: the local IR preserves the source contradiction. The contradiction appears only when the source-discussed scheduled-non-trading scenario is asserted as a witness.
