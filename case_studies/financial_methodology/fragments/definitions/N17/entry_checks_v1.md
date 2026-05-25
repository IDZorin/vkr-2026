# Financial Methodology Entry Checks: N17

- generated_at: `2026-05-10T20:29:10`
- with_llm: `False`
- overall_status: `ok`

## Summary

- clean_gate: `accepted`
- blocking_conditions: ``
- semantic_lint findings: `0` (strong `0`, soft `0`)
- token coverage: `6/6` (`1.0`)
- phrase coverage: `2/2` (`1.0`)
- lowering smells: `1`
- provenance_lint findings: `0` (strong `0`, soft `0`)
- provenance back-translation: status `ok`, score `0.959`, warnings `0`
- diagnostic gate: `needs_review` (fail `0`, warning `28`)
- single semantic judge: `does_not_correspond` / `unclear`
- multi judge: `corresponds` (agreement `0.8`, unanimous `False`)
- corpus-aware multi judge: local `corresponds` / corpus `corresponds` (agreement `1.0`)

## Uncovered Tokens

- none

## Uncovered Phrases

- none

## Steps

| step | status | returncode | duration_s |
| --- | --- | ---: | ---: |
| parser_strict | ok | 0 | 2.161 |
| semantic_lint | ok | 0 | 0.12 |
| token_provenance | ok | 0 | 2.282 |
| provenance_lint | ok | 0 | 0.163 |
| provenance_backtranslation | ok | 0 | 0.178 |
| family_coverage | ok | 0 | 0.113 |
| source_phrase_coverage | ok | 0 | 0.146 |
| lowering_audit | ok | 0 | 0.097 |
| legacy_metrics | ok | 0 | 20.049 |
| diagnostic_suite_skip_llm | ok | 0 | 2.337 |
| quality_snapshot | ok | 0 | 2.288 |
