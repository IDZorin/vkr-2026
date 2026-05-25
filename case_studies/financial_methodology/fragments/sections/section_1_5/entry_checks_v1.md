# Financial Methodology Entry Checks: section_1_5

- generated_at: `2026-05-11T08:45:41`
- with_llm: `False`
- overall_status: `ok`

## Summary

- clean_gate: `accepted`
- blocking_conditions: ``
- semantic_lint findings: `0` (strong `0`, soft `0`)
- token coverage: `19/19` (`1.0`)
- phrase coverage: `3/3` (`1.0`)
- lowering smells: `0`
- provenance_lint findings: `0` (strong `0`, soft `0`)
- provenance back-translation: status `ok`, score `0.73`, warnings `2`
- diagnostic gate: `needs_review` (fail `0`, warning `28`)
- single semantic judge: `corresponds` / `exact_equivalence`
- multi judge: `partially_corresponds` (agreement `0.75`, unanimous `False`)
- corpus-aware multi judge: local `corresponds` / corpus `corresponds` (agreement `1.0`)

## Uncovered Tokens

- none

## Uncovered Phrases

- none

## Steps

| step | status | returncode | duration_s |
| --- | --- | ---: | ---: |
| parser_strict | ok | 0 | 2.026 |
| semantic_lint | ok | 0 | 0.133 |
| token_provenance | ok | 0 | 2.009 |
| provenance_lint | ok | 0 | 0.167 |
| provenance_backtranslation | ok | 0 | 0.183 |
| family_coverage | ok | 0 | 0.12 |
| source_phrase_coverage | ok | 0 | 0.151 |
| lowering_audit | ok | 0 | 0.375 |
| legacy_metrics | ok | 0 | 18.871 |
| diagnostic_suite_skip_llm | ok | 0 | 2.343 |
| quality_snapshot | ok | 0 | 2.11 |
