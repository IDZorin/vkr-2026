# Section 1.5 Translator Notes

This file records translator decisions for the current `main_ir.a4v3`.
It is review memory, not an additional source of methodology claims.

## Changelog

### 2026-05-10T22:05:00+02:00

Decision: translate "Licenses ... may be issued ... by Solactive" as a permission over an index-underlying-value license class.

Accepted:

- `may be issued` is represented by `permission issue_index_underlying_value_license`, not by an existential fact that a license has already been issued.
- `Solactive` is an entity of subtype `SolactiveOrganization`; the permission parameter uses the type `SolactiveOrganization`, avoiding `agent: Solactive`.
- `LicensesToUseIndexAsUnderlyingValue` carries the source-listed use categories and recipient categories.
- `IndexUnderlyingValueLicenseIssuance` carries the issuance structure (`to` recipient categories and `by` Solactive), so "issued" is not only hidden in relation names.
- `IndexUnderlyingValueLicense` is a subtype of `License`; the permission target is a possible concrete license, linked to the class-level carrier by `license_instance_of_class`.
- The three use categories and four recipient categories are encoded as enum values, not as seven unrelated opaque sorts.
- The listed use categories are read comprehensively: the licensing programme/class covers financial instruments, investment funds, and financial contracts.
- The listed recipient categories are read comprehensively: the issuance programme is available to stock exchanges, banks, financial services providers, and investment houses.

Rejected / alternatives:

- Do not use `forall l: License`; that would make every license in the model a license to use the Index as an underlying value.
- Do not assert `exists l: License`; the source says licenses may be issued, not that any license has already been issued.
- Do not require each concrete license instance to be issued to all recipient categories simultaneously.
- Do not lose the local `TheIndex` binding by writing `exists i: Index`.
- Do not model recipient categories as separate permissions unless a later merge task needs recipient-specific deontic reasoning. In this section, recipient information remains attached to the explicit issuance carrier.

Rationale: the sentence is a licensing availability statement. The important semantics are the agent (Solactive), the modality (may be issued), the object (licenses to use the Index as underlying value), and the listed use/recipient categories. A class-level carrier preserves the category lists without over-committing to a concrete issued license instance; a separate issuance carrier keeps the "issued to/by" structure explicit. The instance-to-class bridge keeps the permission's `IndexUnderlyingValueLicense` target aligned with the class-level carrier.

Validation:

- Deterministic checks: `clean_gate=accepted`, semantic lint `0`, token coverage `1.0`, phrase coverage `1.0`, lowering smells `0`.
- LLM checks: single semantic judge `corresponds`; corpus-aware multi judge `corresponds`; ordinary multi judge `partially_corresponds`.
- The ordinary multi-judge objection is about expected A4V3 structural reification (`LicenseClass`, `LicenseIssuance`, category enums, and `permission` for "may be issued"), not about an uncovered source phrase. This is accepted because seed methodology translations intentionally make source roles and modality explicit while provenance records the class-level interpretation.
