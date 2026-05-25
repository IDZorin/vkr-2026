# Financial Methodology Entry Checks: section_3_2

- generated_at: `2026-05-11T09:34:47`
- with_llm: `False`
- overall_status: `ok`

## Summary

- clean_gate: `accepted`
- blocking_conditions: ``
- semantic_lint findings: `0` (strong `0`, soft `0`)
- token coverage: `6/6` (`1.0`)
- phrase coverage: `1/1` (`1.0`)
- lowering smells: `0`
- provenance_lint findings: `0` (strong `0`, soft `0`)
- provenance back-translation: status `ok`, score `0.52`, warnings `1`
- diagnostic gate: `needs_review` (fail `0`, warning `26`)
- single semantic judge: `corresponds` / `exact_equivalence`
- multi judge: `corresponds` (agreement `1.0`, unanimous `True`)
- corpus-aware multi judge: local `corresponds` / corpus `corresponds` (agreement `1.0`)

## Uncovered Tokens

- none

## Uncovered Phrases

- none

## Steps

| step | status | returncode | duration_s |
| --- | --- | ---: | ---: |
| parser_strict | ok | 0 | 2.147 |
| semantic_lint | ok | 0 | 0.114 |
| token_provenance | ok | 0 | 2.119 |
| provenance_lint | ok | 0 | 0.188 |
| provenance_backtranslation | ok | 0 | 0.178 |
| family_coverage | ok | 0 | 0.115 |
| source_phrase_coverage | ok | 0 | 0.138 |
| lowering_audit | ok | 0 | 0.091 |
| legacy_metrics | ok | 0 | 21.165 |
| diagnostic_suite_skip_llm | ok | 0 | 2.133 |
| quality_snapshot | ok | 0 | 2.203 |
