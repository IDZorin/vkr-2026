# Definition N15 Translator Notes

This file records translator decisions for the current `main_ir.a4v3`.
It is review memory, not an additional source of methodology claims.

## Changelog

### 2026-05-12T13:45:00+02:00

Decision: represent `"Gbs Index Component" is each security reflected in the GBS Index specified in Section 2.1` as a strict biconditional over `Security`, plus a Section 2.1 reference fact.

Accepted:

- `gbs_index_component(s, GbsIndexSpecifiedInSection2_1)` is true exactly for securities reflected in the GBS Index specified in Section 2.1.
- `Security extends FinancialInstrument` follows the established financial methodology pattern from Sections 2.1 / 2.2 / N19.
- `security_reflected_in_gbs_index` is kept separate from `gbs_index_component` so the source phrase "reflected in the GBS Index" remains explicit in formula structure.
- Section 2.1 is represented as a local DocumentPart reference; detailed cross-section alignment belongs to bridge/merge work.

Rejected / alternatives:

- Do not import the full Section 2.1 Index Universe machinery into this short definition.
- Do not model `GbsIndexComponent` as a separate subtype unless later merge work needs type-level separation.
- Do not encode only `gbs_index_component implies reflected`; the source is definitional.

Rationale: the source is a one-sentence term definition with an embedded cross-reference. The formula keeps both the defined term and the source vocabulary visible.
