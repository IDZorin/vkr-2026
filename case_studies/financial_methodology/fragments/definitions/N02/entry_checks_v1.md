# Financial Methodology Entry Checks: N02

- generated_at: `2026-05-10T19:45:51`
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
- multi judge: `corresponds` (agreement `0.8`, unanimous `False`)
- corpus-aware multi judge: local `corresponds` / corpus `corresponds` (agreement `1.0`)

## Uncovered Tokens

- none

## Uncovered Phrases

- none

## Steps

| step | status | returncode | duration_s |
| --- | --- | ---: | ---: |
| parser_strict | ok | 0 | 2.175 |
| semantic_lint | ok | 0 | 0.126 |
| token_provenance | ok | 0 | 2.516 |
| provenance_lint | ok | 0 | 0.19 |
| provenance_backtranslation | ok | 0 | 0.198 |
| family_coverage | ok | 0 | 0.119 |
| source_phrase_coverage | ok | 0 | 0.16 |
| lowering_audit | ok | 0 | 0.124 |
| legacy_metrics | ok | 0 | 23.366 |
| diagnostic_suite_skip_llm | ok | 0 | 3.573 |
| quality_snapshot | ok | 0 | 3.083 |
| single_semantic_judge_and_render | ok | 0 | 29.545 |
| multi_judge | ok | 0 | 47.509 |
| corpus_aware_multi_judge | ok | 0 | 50.718 |
| diagnostic_suite_with_llm | ok | 0 | 13.521 |
| quality_snapshot_final | ok | 0 | 2.69 |
