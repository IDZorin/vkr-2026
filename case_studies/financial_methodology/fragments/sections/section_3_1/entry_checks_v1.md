# Financial Methodology Entry Checks: section_3_1

- generated_at: `2026-05-12T12:45:01`
- with_llm: `False`
- overall_status: `ok`

## Summary

- clean_gate: `accepted`
- blocking_conditions: ``
- semantic_lint findings: `0` (strong `0`, soft `0`)
- token coverage: `49/51` (`0.961`)
- phrase coverage: `11/11` (`1.0`)
- lowering smells: `2`
- provenance_lint findings: `0` (strong `0`, soft `0`)
- provenance back-translation: status `ok`, score `0.779`, warnings `4`
- diagnostic gate: `needs_review` (fail `0`, warning `33`)
- single semantic judge: `corresponds` / `exact_equivalence`
- multi judge: `partially_corresponds` (agreement `0.75`, unanimous `False`)
- corpus-aware multi judge: local `corresponds` / corpus `corresponds` (agreement `0.8`)

## Uncovered Tokens

- `order`, `please`

## Uncovered Phrases

- none

## Steps

| step | status | returncode | duration_s |
| --- | --- | ---: | ---: |
| parser_strict | ok | 0 | 2.097 |
| semantic_lint | ok | 0 | 0.129 |
| token_provenance | ok | 0 | 2.435 |
| provenance_lint | ok | 0 | 0.183 |
| provenance_backtranslation | ok | 0 | 0.196 |
| family_coverage | ok | 0 | 0.115 |
| source_phrase_coverage | ok | 0 | 0.148 |
| lowering_audit | ok | 0 | 0.101 |
| legacy_metrics | ok | 0 | 20.589 |
| diagnostic_suite_skip_llm | ok | 0 | 2.32 |
| quality_snapshot | ok | 0 | 2.379 |
