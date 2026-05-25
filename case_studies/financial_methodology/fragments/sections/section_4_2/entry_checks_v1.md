# Financial Methodology Entry Checks: section_4_2

- generated_at: `2026-05-14T23:54:40`
- with_llm: `False`
- overall_status: `ok`

## Summary

- clean_gate: `accepted`
- blocking_conditions: ``
- semantic_lint findings: `3` (strong `0`, soft `2`)
- token coverage: `32/37` (`0.865`)
- phrase coverage: `1/1` (`1.0`)
- lowering smells: `0`
- provenance_lint findings: `0` (strong `0`, soft `0`)
- provenance back-translation: status `ok`, score `0.699`, warnings `2`
- role annotation lint: status `ok`, findings `0` (strong `0`, soft `0`)
- role annotation judge: `consistent` / `correct` (issues `0`)
- diagnostic gate: `needs_review` (fail `0`, warning `39`)
- single semantic judge: `None` / `None`
- multi judge: `None` (agreement `None`, unanimous `None`)
- corpus-aware multi judge: local `None` / corpus `None` (agreement `None`)

## Uncovered Tokens

- `negative`, `respective`, `such`, `available`, `clarification`

## Uncovered Phrases

- none

## Steps

| step | status | returncode | duration_s |
| --- | --- | ---: | ---: |
| parser_strict | ok | 0 | 2.162 |
| semantic_lint | ok | 0 | 0.119 |
| token_provenance | ok | 0 | 2.47 |
| provenance_lint | ok | 0 | 0.209 |
| provenance_backtranslation | ok | 0 | 0.2 |
| family_coverage | ok | 0 | 0.118 |
| source_phrase_coverage | ok | 0 | 0.156 |
| lowering_audit | ok | 0 | 0.113 |
| role_annotation_lint | ok | 0 | 0.21 |
| legacy_metrics | ok | 0 | 22.042 |
| diagnostic_suite_skip_llm | ok | 0 | 2.406 |
| quality_snapshot | ok | 0 | 2.505 |
