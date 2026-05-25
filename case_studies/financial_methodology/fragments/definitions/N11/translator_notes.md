# Definition N11 Translator Notes

This file records translator decisions for the current `main_ir.a4v3`.
It is review memory, not an additional source of methodology claims.

## Changelog

### 2026-05-06T17:27:25+02:00

Decision: represent `"Fixing Day" is Selection Day` as a strict biconditional definition.

Accepted:

- `fixing_day` and `selection_day` are predicates over `Day`.
- The definition is expressed as `fixing_day(d) iff selection_day(d)`.

Rejected / alternatives:

- Do not model `FixingDay` as a separate subtype unless later sections need type-level separation.
- Do not use a one-way implication because the source states identity/equivalence, not only inclusion.

Rationale: the source is a short definitional sentence. A biconditional preserves the symmetric meaning directly and avoids adding unsupported lifecycle or event semantics.

Validation:

- clean gate: accepted
- token accounted coverage: 3/3
- waivers: none
