# Financial Methodology Entry Checks: section_4_3

- generated_at: `2026-05-11T16:30:47`
- with_llm: `False`
- overall_status: `ok`

## Summary

- clean_gate: `accepted`
- blocking_conditions: ``
- semantic_lint findings: `0` (strong `0`, soft `0`)
- token coverage: `7/7` (`1.0`)
- phrase coverage: `1/1` (`1.0`)
- lowering smells: `0`
- provenance_lint findings: `0` (strong `0`, soft `0`)
- provenance back-translation: status `ok`, score `0.781`, warnings `1`
- diagnostic gate: `needs_review` (fail `0`, warning `34`)
- single semantic judge: `corresponds` / `exact_equivalence`
- multi judge: `corresponds` (agreement `0.5`, unanimous `False`)
- corpus-aware multi judge: local `corresponds` / corpus `corresponds` (agreement `1.0`)

## Uncovered Tokens

- none

## Uncovered Phrases

- none

## Steps

| step | status | returncode | duration_s |
| --- | --- | ---: | ---: |
| parser_strict | ok | 0 | 2.244 |
| semantic_lint | ok | 0 | 0.121 |
| token_provenance | ok | 0 | 2.819 |
| provenance_lint | ok | 0 | 0.215 |
| provenance_backtranslation | ok | 0 | 0.224 |
| family_coverage | ok | 0 | 0.144 |
| source_phrase_coverage | ok | 0 | 0.188 |
| lowering_audit | ok | 0 | 0.146 |
| legacy_metrics | ok | 0 | 21.39 |
| diagnostic_suite_skip_llm | ok | 0 | 2.386 |
| quality_snapshot | ok | 0 | 2.505 |
