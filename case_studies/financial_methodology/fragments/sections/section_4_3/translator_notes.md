# Section 4.3 Translator Notes

This file records translator decisions for the current `main_ir.a4v3`.
It is review memory, not an additional source of methodology claims.

## Changelog

### 2026-05-11T14:10:00+02:00

Decision: model rounding as a calculation-output constraint with an explicit
two-decimal-place precision carrier.

Accepted:

- `will be rounded` is treated as a hard calculation rule for index levels,
  not as a deontic `obligation`, because the source describes the resulting
  level format rather than assigning an actor a duty.
- `TwoDecimalPlaces` preserves the source phrase "two decimal places".
- `decimal_place_count(TwoDecimalPlaces) = 2` records the numeric value needed
  for backend checks while keeping the source-facing phrase visible.
- The rule is scoped to levels of `TheIndex` through
  `level_of_index(l, TheIndex)`.

Rejected / alternatives:

- Do not encode only `rounded_decimal_places(level) = 2`; that would preserve
  the numeric value but hide the source phrase "two decimal places" from
  provenance/token-level audit.
- Do not introduce a rounding event/carrier: the section contains only a
  simple formatting rule, and all relation arities remain at most 2.
