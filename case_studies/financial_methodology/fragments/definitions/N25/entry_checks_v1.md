# Financial Methodology Entry Checks: N25

- generated_at: `2026-05-10T20:08:52`
- with_llm: `True`
- overall_status: `ok`

## Summary

- clean_gate: `accepted`
- blocking_conditions: ``
- semantic_lint findings: `0` (strong `0`, soft `0`)
- token coverage: `7/7` (`1.0`)
- phrase coverage: `1/1` (`1.0`)
- lowering smells: `1`
- provenance_lint findings: `0` (strong `0`, soft `0`)
- provenance back-translation: status `ok`, score `0.964`, warnings `0`
- diagnostic gate: `needs_review` (fail `0`, warning `29`)
- single semantic judge: `corresponds` / `exact_equivalence`
- multi judge: `corresponds` (agreement `0.8`, unanimous `False`)
- corpus-aware multi judge: local `corresponds` / corpus `corresponds` (agreement `1.0`)

## Uncovered Tokens

- none

## Uncovered Phrases

- none

## Steps

| step | status | returncode | duration_s |
| --- | --- | ---: | ---: |
| parser_strict | ok | 0 | 2.284 |
| semantic_lint | ok | 0 | 0.114 |
| token_provenance | ok | 0 | 2.532 |
| provenance_lint | ok | 0 | 0.194 |
| provenance_backtranslation | ok | 0 | 0.211 |
| family_coverage | ok | 0 | 0.151 |
| source_phrase_coverage | ok | 0 | 0.165 |
| lowering_audit | ok | 0 | 0.113 |
| legacy_metrics | ok | 0 | 21.341 |
| diagnostic_suite_skip_llm | ok | 0 | 2.176 |
| quality_snapshot | ok | 0 | 2.581 |
| single_semantic_judge_and_render | ok | 0 | 24.088 |
| multi_judge | ok | 0 | 31.959 |
| corpus_aware_multi_judge | ok | 0 | 45.383 |
| diagnostic_suite_with_llm | ok | 0 | 14.052 |
| quality_snapshot_final | ok | 0 | 2.831 |
