# N08 Translator Notes

This file records translator decisions for the current `main_ir.a4v3`.
It is review memory, not an additional source of methodology claims.

## Changelog

### 2026-05-20

Decision: represent traded volume as an explicit observation carrier.

Accepted:

- Added `VolumeTradedObservation`.
- Added binary role relations from the observation to the `IndexComponent`,
  `TradingDay`, `Exchange`, and numeric `VolumeNumberOfShares`.
- Kept `daily_value_traded(c, d)`, `closing_price(c, d)`,
  `volume_number_of_shares(c, d)`, and `respective_exchange(c)` unchanged so
  existing bridge/canonical projections remain stable.

Rejected / alternatives:

- Do not leave the Exchange/day qualifier only as a relation from the numeric
  volume value to the Exchange; the source qualifies the observed traded
  volume by component, Exchange, and Trading Day together.
- Do not replace the existing two-argument value functions, because they are
  already used as stable local projections in bridge/merge.

Rationale: the previous version captured the product equation, but the volume
qualifier was too implicit for downstream lowering. The observation carrier
makes the source roles explicit without breaking existing projection symbols.

### 2026-05-20, second review pass

Decision: replace the temporary observation carrier with a qualified volume
function after multi-judge review.

Accepted:

- Added `volume_traded_on_exchange_during_trading_day(c, exchange, d)`.
- Defined `daily_value_traded(c, d)` using that qualified volume directly.
- Kept `volume_number_of_shares(c, d)` as a bridge-stable projection and
  equated it to the qualified volume for `respective_exchange(c)` and `d`.

Rejected / alternatives:

- Do not keep the temporary existential `VolumeTradedObservation` in the main
  IR. The multi-judge panel correctly treated it as extra reification for a
  simple definitional source sentence.

Rationale: the qualified function keeps all source roles explicit while
remaining closer to the source's product definition than an existential carrier.

### 2026-05-20, third review pass

Decision: remove the two-argument `volume_number_of_shares` projection.

Accepted:

- `daily_value_traded(c, d)` is now defined directly with
  `volume_traded_on_exchange_during_trading_day(c, respective_exchange(c), d)`.
- `VolumeNumberOfShares` remains as the numeric return sort, preserving the
  source parenthetical "measured as a number of shares".

Rejected / alternatives:

- Do not keep a separate `volume_number_of_shares(c, d)` function merely as a
  projection. Multi-judge review correctly flagged the extra equality as
  unnecessary for this local definition, and bridge search showed no current
  bridge dependency on that local function.

Rationale: this is the most source-direct version: one product formula, one
qualified volume term, and no additional observation/projection layer.
