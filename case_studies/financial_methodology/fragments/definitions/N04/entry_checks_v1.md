# Financial Methodology Entry Checks: N04

- generated_at: `2026-05-10T19:24:46`
- with_llm: `True`
- overall_status: `ok`

## Summary

- clean_gate: `accepted`
- blocking_conditions: ``
- semantic_lint findings: `0` (strong `0`, soft `0`)
- token coverage: `6/6` (`1.0`)
- phrase coverage: `3/3` (`1.0`)
- lowering smells: `0`
- provenance_lint findings: `0` (strong `0`, soft `0`)
- provenance back-translation: status `ok`, score `0.87`, warnings `0`
- diagnostic gate: `needs_review` (fail `0`, warning `25`)
- single semantic judge: `corresponds` / `exact_equivalence`
- multi judge: `corresponds` (agreement `1.0`, unanimous `True`)
- corpus-aware multi judge: local `corresponds` / corpus `corresponds` (agreement `1.0`)

## Uncovered Tokens

- none

## Uncovered Phrases

- none

## Steps

| step | status | returncode | duration_s |
| --- | --- | ---: | ---: |
| parser_strict | ok | 0 | 2.283 |
| semantic_lint | ok | 0 | 0.111 |
| token_provenance | ok | 0 | 2.344 |
| provenance_lint | ok | 0 | 0.179 |
| provenance_backtranslation | ok | 0 | 0.191 |
| family_coverage | ok | 0 | 0.116 |
| source_phrase_coverage | ok | 0 | 0.155 |
| lowering_audit | ok | 0 | 0.106 |
| legacy_metrics | ok | 0 | 22.308 |
| diagnostic_suite_skip_llm | ok | 0 | 2.766 |
| quality_snapshot | ok | 0 | 3.211 |
| single_semantic_judge_and_render | ok | 0 | 27.644 |
| multi_judge | ok | 0 | 26.785 |
| corpus_aware_multi_judge | ok | 0 | 46.342 |
| diagnostic_suite_with_llm | ok | 0 | 14.605 |
| quality_snapshot_final | ok | 0 | 2.714 |
