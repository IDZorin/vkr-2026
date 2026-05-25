# Financial Methodology Entry Checks: section_5_3

- generated_at: `2026-05-14T21:19:25`
- with_llm: `False`
- overall_status: `ok`

## Summary

- clean_gate: `accepted`
- blocking_conditions: ``
- semantic_lint findings: `0` (strong `0`, soft `0`)
- token coverage: `48/55` (`0.873`)
- phrase coverage: `3/4` (`0.75`)
- lowering smells: `0`
- provenance_lint findings: `0` (strong `0`, soft `0`)
- provenance back-translation: status `ok`, score `0.735`, warnings `8`
- role annotation lint: status `ok`, findings `0` (strong `0`, soft `0`)
- role annotation judge: `consistent` / `correct` (issues `0`)
- diagnostic gate: `needs_review` (fail `0`, warning `33`)
- single semantic judge: `partially_corresponds` / `partial_overlap`
- multi judge: `corresponds` (agreement `0.5`, unanimous `False`)
- corpus-aware multi judge: local `corresponds` / corpus `corresponds` (agreement `0.5`)

## Uncovered Tokens

- `however`, `cannot`, `exclud`, `order`, `oblig`, `such`, `despite`

## Uncovered Phrases

- `Despite`

## Steps

| step | status | returncode | duration_s |
| --- | --- | ---: | ---: |
| parser_strict | ok | 0 | 2.399 |
| semantic_lint | ok | 0 | 0.124 |
| token_provenance | ok | 0 | 2.678 |
| provenance_lint | ok | 0 | 0.464 |
| provenance_backtranslation | ok | 0 | 0.646 |
| family_coverage | ok | 0 | 0.24 |
| source_phrase_coverage | ok | 0 | 0.344 |
| lowering_audit | ok | 0 | 0.16 |
| role_annotation_lint | ok | 0 | 0.288 |
| legacy_metrics | ok | 0 | 24.494 |
| diagnostic_suite_skip_llm | ok | 0 | 2.898 |
| quality_snapshot | ok | 0 | 3.328 |
