# Financial Methodology Entry Checks: section_4_7

- generated_at: `2026-05-14T23:11:04`
- with_llm: `False`
- overall_status: `ok`

## Summary

- clean_gate: `accepted`
- blocking_conditions: ``
- semantic_lint findings: `0` (strong `0`, soft `0`)
- token coverage: `37/38` (`0.974`)
- phrase coverage: `4/4` (`1.0`)
- lowering smells: `3`
- provenance_lint findings: `0` (strong `0`, soft `0`)
- provenance back-translation: status `ok`, score `0.866`, warnings `1`
- role annotation lint: status `ok`, findings `0` (strong `0`, soft `0`)
- role annotation judge: `consistent` / `correct` (issues `0`)
- diagnostic gate: `needs_review` (fail `0`, warning `35`)
- single semantic judge: `corresponds` / `same_meaning_poor_wording`
- multi judge: `partially_corresponds` (agreement `0.75`, unanimous `False`)
- corpus-aware multi judge: local `corresponds` / corpus `corresponds` (agreement `0.8`)

## Uncovered Tokens

- `such`

## Uncovered Phrases

- none

## Steps

| step | status | returncode | duration_s |
| --- | --- | ---: | ---: |
| parser_strict | ok | 0 | 2.758 |
| semantic_lint | ok | 0 | 0.167 |
| token_provenance | ok | 0 | 2.987 |
| provenance_lint | ok | 0 | 0.244 |
| provenance_backtranslation | ok | 0 | 0.259 |
| family_coverage | ok | 0 | 0.157 |
| source_phrase_coverage | ok | 0 | 0.21 |
| lowering_audit | ok | 0 | 0.447 |
| role_annotation_lint | ok | 0 | 0.252 |
| legacy_metrics | ok | 0 | 56.653 |
| diagnostic_suite_skip_llm | ok | 0 | 3.043 |
| quality_snapshot | ok | 0 | 2.838 |
