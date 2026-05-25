# Definition N21 Translator Notes

This file records translator decisions for the current `main_ir.a4v3`.
It is review memory, not an additional source of methodology claims.

## Changelog

### 2026-05-12T14:05:00+02:00

Decision: represent `"Index Currency" is the currency specified in the column "Currency" in the table in Section 1.2` as a strict biconditional between `index_currency(i, c)` and a reified Section 1.2 table specification whose roles bind the Index, currency value, Currency column, and table.

Accepted:

- `index_currency(i, c)` is true exactly when `c` is the currency specified for `i` in the Currency column of the Section 1.2 table.
- The table and column are represented by local entities `Section1_2IndexTable` and `CurrencyColumn`.
- The actual rows and concrete values from Section 1.2 are not duplicated here.
- The definition uses `IndexCurrencySpecification` with binary role relations instead of a high-arity table-row-column relation; this keeps arity low while making the table/column link explicit in the formula body.

Rejected / alternatives:

- Do not import the full Section 1.2 index table into this definition.
- Do not make `Index Currency` a standalone singleton currency; the Section 1.2 table is per-index even if the current rows may share the same value.
- Do not treat the column reference as mere prose; it is captured by explicit table/column entities.

Rationale: the source is a cross-reference definition. The IR keeps the defined term, the currency value, and the Section 1.2 table-column pointer visible in formula structure without turning this definition into a duplicate of Section 1.2.
