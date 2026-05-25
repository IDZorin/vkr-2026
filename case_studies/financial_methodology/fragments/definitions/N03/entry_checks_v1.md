# Financial Methodology Entry Checks: N03

- generated_at: `2026-05-10T20:28:40`
- with_llm: `False`
- overall_status: `ok`

## Summary

- clean_gate: `accepted`
- blocking_conditions: ``
- semantic_lint findings: `0` (strong `0`, soft `0`)
- token coverage: `6/6` (`1.0`)
- phrase coverage: `1/1` (`1.0`)
- lowering smells: `1`
- provenance_lint findings: `0` (strong `0`, soft `0`)
- provenance back-translation: status `ok`, score `0.959`, warnings `0`
- diagnostic gate: `needs_review` (fail `0`, warning `28`)
- single semantic judge: `does_not_correspond` / `unclear`
- multi judge: `corresponds` (agreement `1.0`, unanimous `True`)
- corpus-aware multi judge: local `corresponds` / corpus `corresponds` (agreement `1.0`)

## Uncovered Tokens

- none

## Uncovered Phrases

- none

## Steps

| step | status | returncode | duration_s |
| --- | --- | ---: | ---: |
| parser_strict | ok | 0 | 2.852 |
| semantic_lint | ok | 0 | 0.126 |
| token_provenance | ok | 0 | 2.675 |
| provenance_lint | ok | 0 | 0.221 |
| provenance_backtranslation | ok | 0 | 0.2 |
| family_coverage | ok | 0 | 0.122 |
| source_phrase_coverage | ok | 0 | 0.179 |
| lowering_audit | ok | 0 | 0.1 |
| legacy_metrics | ok | 0 | 19.798 |
| diagnostic_suite_skip_llm | ok | 0 | 2.274 |
| quality_snapshot | ok | 0 | 2.458 |
