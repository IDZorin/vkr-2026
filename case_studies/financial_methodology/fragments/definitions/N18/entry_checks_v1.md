# Financial Methodology Entry Checks: N18

- generated_at: `2026-05-10T19:56:14`
- with_llm: `True`
- overall_status: `ok`

## Summary

- clean_gate: `accepted`
- blocking_conditions: ``
- semantic_lint findings: `0` (strong `0`, soft `0`)
- token coverage: `7/7` (`1.0`)
- phrase coverage: `2/2` (`1.0`)
- lowering smells: `1`
- provenance_lint findings: `0` (strong `0`, soft `0`)
- provenance back-translation: status `ok`, score `0.964`, warnings `0`
- diagnostic gate: `needs_review` (fail `0`, warning `29`)
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
| parser_strict | ok | 0 | 2.302 |
| semantic_lint | ok | 0 | 0.12 |
| token_provenance | ok | 0 | 2.451 |
| provenance_lint | ok | 0 | 0.18 |
| provenance_backtranslation | ok | 0 | 0.193 |
| family_coverage | ok | 0 | 0.117 |
| source_phrase_coverage | ok | 0 | 0.151 |
| lowering_audit | ok | 0 | 0.107 |
| legacy_metrics | ok | 0 | 23.152 |
| diagnostic_suite_skip_llm | ok | 0 | 2.192 |
| quality_snapshot | ok | 0 | 2.555 |
| single_semantic_judge_and_render | ok | 0 | 23.436 |
| multi_judge | ok | 0 | 36.317 |
| corpus_aware_multi_judge | ok | 0 | 43.624 |
| diagnostic_suite_with_llm | ok | 0 | 16.985 |
| quality_snapshot_final | ok | 0 | 2.513 |
