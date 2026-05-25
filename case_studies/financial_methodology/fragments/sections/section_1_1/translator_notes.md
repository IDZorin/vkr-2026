# Section 1.1 Translator Notes

This file records translation decisions behind the current `main_ir.a4v3`.
It is an audit note, not an additional source of methodology claims.

## Changelog

### 2026-05-10T18:55:00+02:00

Decision: keep `NoRebalancingFee` as the source-facing enum value for the table cell `Rebalancing Fee | -`, and add a positive carrier relation for contradiction detection:

```a4v3
rel rebalancing_fee_charged : Index

constraint no_rebalancing_fee_means_rebalancing_fee_not_charged :
  forall i: Index,
    rebalancing_fee_status(i) = NoRebalancingFee
    implies not rebalancing_fee_charged(i)
```

Rationale: the table convention `-` is read as "no rebalancing fee", not as missing data. The explicit positive carrier lets merged checks detect a later conflict such as "a rebalancing fee is charged".
