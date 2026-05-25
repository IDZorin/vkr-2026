# Appendix 8.1 Translator Notes

## Changelog

### 2026-05-10T14:52:21Z

- Modeled Appendix 8.1 as a deterministic RBICS ontology table, not as prose-like constraints.
- Normalized RBICS codes by removing comma separators. Example: `101,025,153,010` becomes `RbicsNumberCode101025153010`.
- Modeled every unique table row as one `RbicsSubindustry` entity with explicit `rbics_code`, `rbics_subindustry_name`, and `rbics_classification_level`.
- Modeled RBICS itself as `RBICS : RbicsClassificationSystem` and linked each subindustry to it with `rbics_classifies_subindustry`.
- Deduplicated repeated source rows instead of creating duplicate IR entities.

## Table Summary

- Source rows parsed: 161
- Unique RBICS rows modeled: 108
- Duplicate rows skipped: 53
- Classification levels found: 6

## Translation Decisions

- RBICS numbers are treated as codes, not numeric quantities. Therefore they are represented as `RbicsNumberCode...` entities, not `Nat` or `Real` values.
- Classification level is represented as an enum value `RbicsClassificationLevel6`, because all parsed rows have level `6`.
- Subindustry names are represented as named entities under `RbicsSubindustryName`; the source phrase is preserved in `provenance.yaml`.
- Duplicate table rows are a source-table artifact. They preserve no additional ontology facts, so the IR keeps one fact per unique row.
- Cross-section identity with section 2.1 is handled in `case_studies/financial_methodology/bridge/main_bridge.a4v3`. Appendix 8.1 remains a concrete table ontology, while section 2.1 keeps its abstract reference vocabulary.
