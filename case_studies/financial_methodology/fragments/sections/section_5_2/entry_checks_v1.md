# Financial Methodology Entry Checks: section_5_2

- generated_at: `2026-05-10T19:08:47`
- with_llm: `False`
- overall_status: `ok`

## Summary

- clean_gate: `accepted`
- blocking_conditions: ``
- semantic_lint findings: `2` (strong `0`, soft `0`)
- token coverage: `49/54` (`0.907`)
- phrase coverage: `5/5` (`1.0`)
- lowering smells: `1`
- provenance_lint findings: `0` (strong `0`, soft `0`)
- provenance back-translation: status `ok`, score `0.844`, warnings `3`
- diagnostic gate: `needs_review` (fail `0`, warning `36`)
- single semantic judge: `None` / `None`
- multi judge: `None` (agreement `None`, unanimous `None`)
- corpus-aware multi judge: local `None` / corpus `None` (agreement `None`)

## Uncovered Tokens

- `case`, `such`, `present`, `announc`, `under`

## Uncovered Phrases

- none

## Steps

| step | status | returncode | duration_s |
| --- | --- | ---: | ---: |
| parser_strict | ok | 0 | 2.423 |
| semantic_lint | ok | 0 | 0.15 |
| token_provenance | ok | 0 | 2.723 |
| provenance_lint | ok | 0 | 0.349 |
| provenance_backtranslation | ok | 0 | 0.296 |
| family_coverage | ok | 0 | 0.156 |
| source_phrase_coverage | ok | 0 | 0.19 |
| lowering_audit | ok | 0 | 0.126 |
| legacy_metrics | ok | 0 | 24.79 |
| diagnostic_suite_skip_llm | ok | 0 | 2.401 |
| quality_snapshot | ok | 0 | 2.475 |
