# Definition N05 Translator Notes

This file records translator decisions for the current `main_ir.a4v3`.
It is review memory, not an additional source of methodology claims.

## Changelog

### 2026-05-12T13:25:00+02:00

Decision: represent `"Calculation Day" is every weekday from Monday to Friday` as a strict biconditional over `Day`.

Accepted:

- `calculation_day` is a predicate over `Day`, not a separate subtype.
- `WeekdayOf(d)` is the prelude function used to expose the weekday dimension.
- The phrase "from Monday to Friday" is expanded to Monday, Tuesday, Wednesday, Thursday, and Friday.
- The definition is expressed as `calculation_day(d) iff WeekdayOf(d)` is one of those five weekdays.
- This definition is intentionally independent from N04 `business_day`, even though the weekday formula is identical. A later bridge/merge layer may add `calculation_day(d) iff business_day(d)` if the methodology-wide ontology wants that alias.

Rejected / alternatives:

- Do not model `CalculationDay` as a separate subtype unless later sections need type-level separation.
- Do not use only `calculation_day(d) implies ...`, because the source is definitional.
- Do not hide weekday semantics only inside the name `calculation_day`.

Rationale: the source is a short definitional sentence. A biconditional preserves the closed meaning directly, while using `WeekdayOf` keeps the calendar semantics visible in the formula body.
