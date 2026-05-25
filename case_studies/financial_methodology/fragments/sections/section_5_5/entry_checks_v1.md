# Financial Methodology Entry Checks: section_5_5

- generated_at: `2026-05-20T04:03:56`
- with_llm: `False`
- overall_status: `ok`

## Summary

- clean_gate: `accepted`
- blocking_conditions: ``
- semantic_lint findings: `0` (strong `0`, soft `0`)
- token coverage: `29/31` (`0.935`)
- phrase coverage: `6/6` (`1.0`)
- lowering smells: `4`
- provenance_lint findings: `0` (strong `0`, soft `0`)
- provenance back-translation: status `ok`, score `0.812`, warnings `1`
- role annotation lint: status `ok`, findings `0` (strong `0`, soft `0`)
- role annotation judge: `None` / `None` (issues `0`)
- diagnostic gate: `needs_review` (fail `0`, warning `36`)
- single semantic judge: `corresponds` / `same_meaning_poor_wording`
- multi judge: `partially_corresponds` (agreement `0.8`, unanimous `False`)
- corpus-aware multi judge: local `None` / corpus `None` (agreement `None`)

## Uncovered Tokens

- `such`, `submitt`

## Uncovered Phrases

- none

## Steps

| step | status | returncode | duration_s |
| --- | --- | ---: | ---: |
| parser_strict | ok | 0 | 3.058 |
| semantic_lint | ok | 0 | 0.166 |
| token_provenance | ok | 0 | 2.809 |
| provenance_lint | ok | 0 | 0.217 |
| provenance_backtranslation | ok | 0 | 1.885 |
| family_coverage | ok | 0 | 0.214 |
| source_phrase_coverage | ok | 0 | 0.228 |
| lowering_audit | ok | 0 | 0.165 |
| role_annotation_lint | ok | 0 | 0.268 |
| legacy_metrics | ok | 0 | 33.631 |
| diagnostic_suite_skip_llm | ok | 0 | 3.262 |
| quality_snapshot | ok | 0 | 5.137 |
