# Financial Methodology Entry Checks: N20

- generated_at: `2026-05-10T19:58:59`
- with_llm: `True`
- overall_status: `ok`

## Summary

- clean_gate: `accepted`
- blocking_conditions: ``
- semantic_lint findings: `0` (strong `0`, soft `0`)
- token coverage: `8/8` (`1.0`)
- phrase coverage: `1/1` (`1.0`)
- lowering smells: `1`
- provenance_lint findings: `0` (strong `0`, soft `0`)
- provenance back-translation: status `ok`, score `0.968`, warnings `0`
- diagnostic gate: `needs_review` (fail `0`, warning `28`)
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
| parser_strict | ok | 0 | 2.276 |
| semantic_lint | ok | 0 | 0.124 |
| token_provenance | ok | 0 | 2.378 |
| provenance_lint | ok | 0 | 0.176 |
| provenance_backtranslation | ok | 0 | 0.186 |
| family_coverage | ok | 0 | 0.109 |
| source_phrase_coverage | ok | 0 | 0.15 |
| lowering_audit | ok | 0 | 0.105 |
| legacy_metrics | ok | 0 | 21.146 |
| diagnostic_suite_skip_llm | ok | 0 | 2.039 |
| quality_snapshot | ok | 0 | 2.368 |
| single_semantic_judge_and_render | ok | 0 | 23.503 |
| multi_judge | ok | 0 | 36.437 |
| corpus_aware_multi_judge | ok | 0 | 57.121 |
| diagnostic_suite_with_llm | ok | 0 | 14.62 |
| quality_snapshot_final | ok | 0 | 2.436 |
