# Definition N19 Translator Notes

This file records translator decisions for the current `main_ir.a4v3`.
It is review memory, not an additional source of methodology claims.

## Changelog

### 2026-05-12T13:25:00+02:00

Decision: represent `"Index Component" is each security reflected in the Index` as a strict biconditional over `Security`.

Accepted:

- `index_component(s, TheIndex)` is true exactly for securities reflected in the Index.
- `Security extends FinancialInstrument` follows the established financial methodology pattern from Sections 2.1 / 2.2.
- `TheIndex` is local-first; cross-section identity with canonical index entities belongs to bridge/merge work.
- The source phrase "reflected in the Index" is kept as a separate predicate (`security_reflected_in_index`) rather than hidden inside the name `index_component`; the biconditional ties the source vocabulary and the defined term.

Rejected / alternatives:

- Do not model `IndexComponent` as a separate subtype in this definition file unless later merge work needs type-level separation.
- Do not encode only `index_component implies reflected`; the source is definitional.

Rationale: the source is a one-sentence term definition. The formula keeps the semantic link visible instead of relying on the name `index_component`.
