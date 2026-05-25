# Definition N04 Translator Notes

This file records translator decisions for the current `main_ir.a4v3`.
It is review memory, not an additional source of methodology claims.

## Changelog

### 2026-05-10T19:20:00+02:00

Decision: represent `"Business Day" is every weekday from Monday to Friday` as a strict biconditional over `Day`.

Accepted:

- `business_day` is a predicate over `Day`, not a separate subtype.
- `WeekdayOf(d)` is the prelude function used to expose the weekday dimension.
- The phrase "from Monday to Friday" is expanded to Monday, Tuesday, Wednesday, Thursday, and Friday.
- The definition is expressed as `business_day(d) iff WeekdayOf(d)` is one of those five weekdays.

Rejected / alternatives:

- Do not model `BusinessDay` as a separate subtype unless later sections need type-level separation.
- Do not use only `business_day(d) implies ...`, because the source is definitional.
- Do not hide weekday semantics only inside the name `business_day`.

Rationale: the source is a short definitional sentence. A biconditional preserves the closed meaning directly, while using `WeekdayOf` keeps the calendar semantics visible in the formula body.
