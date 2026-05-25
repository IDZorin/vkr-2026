# Definition N23 Translator Notes

This file records translator decisions for the current `main_ir.a4v3`.
It is review memory, not an additional source of methodology claims.

## Changelog

### 2026-05-12T14:05:00+02:00

Decision: represent `"Index Universe" is the sum of all financial instruments which fulfill the Index Universe Requirements` as a set-membership biconditional, with a separate source-surface fact preserving the phrase "sum of all".

Accepted:

- A financial instrument is in `TheIndexUniverse` exactly when it fulfills `TheIndexUniverseRequirements`.
- `"sum of all"` is treated as collection/set language, not numeric addition.
- `TheIndexUniverseRequirements` is a local reference to the defined requirements; detailed requirement content belongs to N22 / Section 2.1 and later bridge/merge work.

Rejected / alternatives:

- Do not model "sum" as arithmetic.
- Do not import the full Section 2.1 universe-requirements machinery here.
- Do not use only a fact marker for "sum of all"; the membership biconditional is needed to make the definition operational.

Rationale: this is a compact term definition. The IR preserves the source vocabulary while making the actual membership condition explicit.
