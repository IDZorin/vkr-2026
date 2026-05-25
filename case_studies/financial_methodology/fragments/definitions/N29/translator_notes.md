# Definition N29 Translator Notes

This file records translator decisions for the current `main_ir.a4v3`.
It is review memory, not an additional source of methodology claims.

## Changelog

### 2026-05-10T19:35:00+02:00

Decision: represent `"Start Date" shall have the meaning as defined in Section 1.3` as a cross-reference definition.

Accepted:

- The quoted term is represented as a `DefinedTerm`.
- The referenced location is represented as a `DocumentPart`.
- `shall have the meaning as defined in Section ...` is encoded by `term_shall_have_meaning_defined_in_section`.

Rejected / alternatives:

- Do not duplicate the substantive Section 1.3 date facts inside the definition entry.
- Do not model this `shall` as a deontic obligation.

Rationale: the definition entry only points to where the term is defined. The substantive content belongs to Section 1.3 or a later merge/bridge layer.
