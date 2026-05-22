# SOLTCEY Real Mutation Benchmark v2

Benchmark generated with seed `20260429` from copied real SOLTCEY blocks under `IR/outputs/runs/unified_methodology_v1`.
Original files are not modified; each case stores `source_original.md`, mutated `source.md`, mutation-specific IR, backend results, and IR metrics.

## Headline

- Source run: `<WORKSPACE_ROOT>\IR\outputs\runs\unified_methodology_v1`
- Real base blocks available: `55`
- Total experiments: `137`
- Injected semantic errors: `96`
- Negative controls: `23`
- Stress/system-break cases: `18`
- TP / FP / FN / TN / STRESS: `47` / `6` / `49` / `17` / `18`
- Raw recall over semantic errors: `49.0%`
- Applicable recall: `47` / `47` = `100.0%`
- False positive rate: `26.1%`
- False negative rate: `51.0%`
- Precision: `88.7%`
- F1: `63.1%`
- Severity-weighted recall: `54.4%`
- Graceful failure rate on stress cases: `83.3%`
- Wilson 95% interval for raw recall: `39.2%` .. `58.8%`

## Metrics By Level

| Level | Cases | Semantic errors | Detected | Missed | Controls | FP | Stress | Graceful stress | Expected signal met | Partial/diagnostic |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `methodology_level_mutation` | 33 | 33 | 17 | 16 | 0 | 0 | 0 | 0 | 33 | 33 |
| `negative_control` | 23 | 0 | 0 | 0 | 23 | 6 | 0 | 0 | 17 | 23 |
| `section_level_mutation` | 46 | 46 | 30 | 16 | 0 | 0 | 0 | 0 | 46 | 46 |
| `stress_system_break` | 18 | 0 | 0 | 0 | 0 | 0 | 18 | 15 | 15 | 15 |
| `unsupported_backend_semantics` | 17 | 17 | 0 | 17 | 0 | 0 | 0 | 0 | 17 | 17 |

## Metrics By Error Class

| Class | Cases | Errors | Detected | Missed | Controls | FP | Stress | Graceful stress | Detection rate | FP rate | Limitation |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| `action_transition_unsupported` | 4 | 4 | 0 | 4 | 0 | 0 | 0 | 0 | `0.0%` | `n/a` | construct delegated/unsupported by selected validation backends |
| `bad_quantifier_body` | 3 | 0 | 0 | 0 | 0 | 0 | 3 | 3 | `n/a` | `n/a` | stress case, excluded from semantic TP/FN |
| `cross_section_conflict_without_symbol_unification` | 8 | 8 | 0 | 8 | 0 | 0 | 0 | 0 | `0.0%` | `n/a` | global assembler did not unify two section-local symbols for the same domain term |
| `deontic_obligation_unsupported` | 4 | 4 | 0 | 4 | 0 | 0 | 0 | 0 | `0.0%` | `n/a` | construct delegated/unsupported by selected validation backends |
| `fallback_choice_reversal` | 7 | 7 | 7 | 0 | 0 | 0 | 0 | 0 | `100.0%` | `n/a` | none |
| `false_positive_overstrict_ir_or_lowering` | 6 | 0 | 0 | 0 | 6 | 6 | 0 | 0 | `n/a` | `100.0%` | false positive control: source is safe, but mutated IR/lowering adds an over-strict invariant |
| `financial_entity_typology_confusion_without_domain_profile` | 8 | 8 | 0 | 8 | 0 | 0 | 0 | 0 | `0.0%` | `n/a` | requires a domain ontology profile with disjoint Currency/Exchange/Rate/Price classes |
| `guard_polarity_flip` | 8 | 8 | 8 | 0 | 0 | 0 | 0 | 0 | `100.0%` | `n/a` | none |
| `internally_consistent_but_domain_wrong_formula` | 9 | 9 | 0 | 9 | 0 | 0 | 0 | 0 | `0.0%` | `n/a` | no external invariant in the current domain ontology refutes the wrong formula |
| `invalid_rel_returns_sort` | 4 | 0 | 0 | 0 | 0 | 0 | 4 | 4 | `n/a` | `n/a` | stress case, excluded from semantic TP/FN |
| `numeric_bound_violation` | 6 | 6 | 6 | 0 | 0 | 0 | 0 | 0 | `100.0%` | `n/a` | none |
| `probabilistic_property_unsupported` | 4 | 4 | 0 | 4 | 0 | 0 | 0 | 0 | `0.0%` | `n/a` | construct delegated/unsupported by selected validation backends |
| `semantic_error_without_witness` | 7 | 7 | 0 | 7 | 0 | 0 | 0 | 0 | `0.0%` | `n/a` | no witness/data world or downstream consistency contract |
| `stylistic_paraphrase_or_synonym_no_semantic_change` | 8 | 0 | 0 | 0 | 8 | 0 | 0 | 0 | `n/a` | `0.0%` | none |
| `surface_typo_or_morphology_no_semantic_change` | 9 | 0 | 0 | 0 | 9 | 0 | 0 | 0 | `n/a` | `0.0%` | none |
| `temporal_until_or_liveness_unsupported` | 5 | 5 | 0 | 5 | 0 | 0 | 0 | 0 | `0.0%` | `n/a` | construct delegated/unsupported by selected validation backends |
| `time_order_violation` | 9 | 9 | 9 | 0 | 0 | 0 | 0 | 0 | `100.0%` | `n/a` | none |
| `type_mismatch` | 3 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | `n/a` | `n/a` | stress case, excluded from semantic TP/FN |
| `undeclared_symbol_reference` | 4 | 0 | 0 | 0 | 0 | 0 | 4 | 4 | `n/a` | `n/a` | stress case, excluded from semantic TP/FN |
| `unknown_construct` | 4 | 0 | 0 | 0 | 0 | 0 | 4 | 4 | `n/a` | `n/a` | stress case, excluded from semantic TP/FN |
| `whole_methodology_definition_conflict` | 9 | 9 | 9 | 0 | 0 | 0 | 0 | 0 | `100.0%` | `n/a` | none |
| `whole_methodology_forward_reference` | 8 | 8 | 8 | 0 | 0 | 0 | 0 | 0 | `100.0%` | `n/a` | none |

## Backend Summary

| Backend | Expected catches | Caught | Expected+caught | Unexpected catch | Partial/diagnostic rows |
| --- | ---: | ---: | ---: | ---: | ---: |
| `smt` | 39 | 48 | 39 | 9 | 16 |
| `shacl` | 47 | 56 | 47 | 9 | 24 |
| `owl` | 0 | 9 | 0 | 9 | 98 |
| `rdf` | 0 | 0 | 0 | 0 | 0 |

## Interpretation

- This is a SOLTCEY-real copied-source benchmark: every case is anchored to a real block from the unified methodology run.
- The mutation-specific IR is backend-checkable local/global surface IR stored next to the copied source; original SOLTCEY artifacts are preserved separately as references.
- The benchmark intentionally includes false negatives: section errors without witness/context, internally consistent but domain-wrong formulas, financial typology confusion without a domain ontology profile, unsupported temporal/deontic/probabilistic/action semantics, and missing global symbol unification.
- Negative controls test false positives: safe surface typos/morphological replacements and paraphrases/synonyms should stay silent, while over-strict IR/lowering controls intentionally demonstrate false alarms.
- Stress cases are excluded from semantic TP/FN and measured through graceful failure.

## Files

- Full JSON: `<WORKSPACE_ROOT>\IR\outputs\runs\soltcey_real_mutation_benchmark_v2\reports\soltcey_real_mutation_benchmark_v2.json`
- Cases CSV: `<WORKSPACE_ROOT>\IR\outputs\runs\soltcey_real_mutation_benchmark_v2\reports\soltcey_real_mutation_benchmark_v2_cases.csv`
- Backend CSV: `<WORKSPACE_ROOT>\IR\outputs\runs\soltcey_real_mutation_benchmark_v2\reports\soltcey_real_mutation_benchmark_v2_backend_outcomes.csv`
- Correlation matrix CSV: `<WORKSPACE_ROOT>\IR\outputs\runs\soltcey_real_mutation_benchmark_v2\reports\soltcey_real_mutation_benchmark_v2_correlation_matrix.csv`
- Case root: `<WORKSPACE_ROOT>\IR\outputs\runs\soltcey_real_mutation_benchmark_v2\cases`
