# Financial Methodology Entry Checks: N30

- generated_at: `2026-05-12T22:36:50`
- with_llm: `True`
- overall_status: `ok`

## Summary

- clean_gate: `accepted`
- blocking_conditions: ``
- semantic_lint findings: `5` (strong `0`, soft `5`)
- token coverage: `41/41` (`1.0`)
- phrase coverage: `9/9` (`1.0`)
- lowering smells: `3`
- provenance_lint findings: `0` (strong `0`, soft `0`)
- provenance back-translation: status `ok`, score `0.762`, warnings `3`
- diagnostic gate: `needs_review` (fail `0`, warning `34`)
- single semantic judge: `corresponds` / `same_meaning_poor_wording`
- multi judge: `partially_corresponds` (agreement `0.75`, unanimous `False`)
- corpus-aware multi judge: local `corresponds` / corpus `corresponds` (agreement `0.8`)

## Uncovered Tokens

- none

## Uncovered Phrases

- none

## Steps

| step | status | returncode | duration_s |
| --- | --- | ---: | ---: |
| parser_strict | ok | 0 | 2.154 |
| semantic_lint | ok | 0 | 0.126 |
| token_provenance | ok | 0 | 2.353 |
| provenance_lint | ok | 0 | 0.197 |
| provenance_backtranslation | ok | 0 | 0.208 |
| family_coverage | ok | 0 | 0.118 |
| source_phrase_coverage | ok | 0 | 0.153 |
| lowering_audit | ok | 0 | 0.105 |
| legacy_metrics | ok | 0 | 21.963 |
| diagnostic_suite_skip_llm | ok | 0 | 2.486 |
| quality_snapshot | ok | 0 | 2.359 |
| single_semantic_judge_and_render | ok | 0 | 21.698 |
| multi_judge | ok | 0 | 66.217 |
| corpus_aware_multi_judge | ok | 0 | 187.813 |
| diagnostic_suite_with_llm | ok | 0 | 26.584 |
| quality_snapshot_final | ok | 0 | 3.092 |
