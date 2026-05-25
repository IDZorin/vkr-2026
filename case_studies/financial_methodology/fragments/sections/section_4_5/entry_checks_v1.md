# Financial Methodology Entry Checks: section_4_5

- generated_at: `2026-05-14T16:13:06`
- with_llm: `False`
- overall_status: `ok`

## Summary

- clean_gate: `accepted`
- blocking_conditions: ``
- semantic_lint findings: `5` (strong `0`, soft `5`)
- token coverage: `85/95` (`0.895`)
- phrase coverage: `21/21` (`1.0`)
- lowering smells: `0`
- provenance_lint findings: `0` (strong `0`, soft `0`)
- provenance back-translation: status `ok`, score `0.831`, warnings `2`
- role annotation lint: status `ok`, findings `0` (strong `0`, soft `0`)
- role annotation judge: `consistent` / `correct` (issues `0`)
- diagnostic gate: `needs_review` (fail `0`, warning `35`)
- single semantic judge: `corresponds` / `exact_equivalence`
- multi judge: `partially_corresponds` (agreement `0.75`, unanimous `False`)
- corpus-aware multi judge: local `corresponds` / corpus `corresponds` (agreement `0.8`)

## Uncovered Tokens

- `part`, `variou`, `referr`, `two`, `such`, `therefore`, `respective`, `while`, `case`, `follow`

## Uncovered Phrases

- none

## Steps

| step | status | returncode | duration_s |
| --- | --- | ---: | ---: |
| parser_strict | ok | 0 | 2.562 |
| semantic_lint | ok | 0 | 0.149 |
| token_provenance | ok | 0 | 3.007 |
| provenance_lint | ok | 0 | 0.218 |
| provenance_backtranslation | ok | 0 | 0.219 |
| family_coverage | ok | 0 | 1.809 |
| source_phrase_coverage | ok | 0 | 0.242 |
| lowering_audit | ok | 0 | 0.184 |
| role_annotation_lint | ok | 0 | 0.296 |
| legacy_metrics | ok | 0 | 35.701 |
| diagnostic_suite_skip_llm | ok | 0 | 5.056 |
| quality_snapshot | ok | 0 | 3.455 |
