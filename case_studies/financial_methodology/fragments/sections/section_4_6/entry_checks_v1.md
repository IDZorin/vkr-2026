# Financial Methodology Entry Checks: section_4_6

- generated_at: `2026-05-14T22:50:48`
- with_llm: `False`
- overall_status: `ok`

## Summary

- clean_gate: `accepted`
- blocking_conditions: ``
- semantic_lint findings: `1` (strong `0`, soft `1`)
- token coverage: `44/46` (`0.957`)
- phrase coverage: `3/3` (`1.0`)
- lowering smells: `8`
- provenance_lint findings: `0` (strong `0`, soft `0`)
- provenance back-translation: status `ok`, score `0.711`, warnings `3`
- role annotation lint: status `ok`, findings `0` (strong `0`, soft `0`)
- role annotation judge: `consistent` / `correct` (issues `0`)
- diagnostic gate: `needs_review` (fail `0`, warning `37`)
- single semantic judge: `corresponds` / `exact_equivalence`
- multi judge: `partially_corresponds` (agreement `0.75`, unanimous `False`)
- corpus-aware multi judge: local `corresponds` / corpus `corresponds` (agreement `1.0`)

## Uncovered Tokens

- `however`, `therefore`

## Uncovered Phrases

- none

## Steps

| step | status | returncode | duration_s |
| --- | --- | ---: | ---: |
| parser_strict | ok | 0 | 3.182 |
| semantic_lint | ok | 0 | 0.186 |
| token_provenance | ok | 0 | 3.593 |
| provenance_lint | ok | 0 | 0.253 |
| provenance_backtranslation | ok | 0 | 0.265 |
| family_coverage | ok | 0 | 0.163 |
| source_phrase_coverage | ok | 0 | 0.208 |
| lowering_audit | ok | 0 | 0.144 |
| role_annotation_lint | ok | 0 | 0.268 |
| legacy_metrics | ok | 0 | 30.749 |
| diagnostic_suite_skip_llm | ok | 0 | 3.5 |
| quality_snapshot | ok | 0 | 3.047 |
