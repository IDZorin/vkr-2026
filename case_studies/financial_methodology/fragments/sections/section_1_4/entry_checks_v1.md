# Financial Methodology Entry Checks: section_1_4

- generated_at: `2026-05-14T20:15:50`
- with_llm: `False`
- overall_status: `ok`

## Summary

- clean_gate: `accepted`
- blocking_conditions: ``
- semantic_lint findings: `6` (strong `0`, soft `6`)
- token coverage: `43/48` (`0.896`)
- phrase coverage: `16/16` (`1.0`)
- lowering smells: `0`
- provenance_lint findings: `0` (strong `0`, soft `0`)
- provenance back-translation: status `ok`, score `0.725`, warnings `8`
- role annotation lint: status `ok`, findings `0` (strong `0`, soft `0`)
- role annotation judge: `consistent` / `correct` (issues `0`)
- diagnostic gate: `needs_review` (fail `0`, warning `31`)
- single semantic judge: `corresponds` / `exact_equivalence`
- multi judge: `partially_corresponds` (agreement `1.0`, unanimous `True`)
- corpus-aware multi judge: local `corresponds` / corpus `corresponds` (agreement `0.5`)

## Uncovered Tokens

- `frequenci`, `should`, `addition`, `respective`, `relevant`

## Uncovered Phrases

- none

## Steps

| step | status | returncode | duration_s |
| --- | --- | ---: | ---: |
| parser_strict | ok | 0 | 2.403 |
| semantic_lint | ok | 0 | 0.158 |
| token_provenance | ok | 0 | 2.497 |
| provenance_lint | ok | 0 | 0.223 |
| provenance_backtranslation | ok | 0 | 0.219 |
| family_coverage | ok | 0 | 0.123 |
| source_phrase_coverage | ok | 0 | 0.163 |
| lowering_audit | ok | 0 | 0.106 |
| role_annotation_lint | ok | 0 | 0.228 |
| legacy_metrics | ok | 0 | 23.432 |
| diagnostic_suite_skip_llm | ok | 0 | 2.446 |
| quality_snapshot | ok | 0 | 2.767 |
