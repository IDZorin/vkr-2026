# Financial Methodology Entry Checks: section_4_4

- generated_at: `2026-05-11T17:19:28`
- with_llm: `True`
- overall_status: `ok`

## Summary

- clean_gate: `accepted`
- blocking_conditions: ``
- semantic_lint findings: `2` (strong `0`, soft `2`)
- token coverage: `47/47` (`1.0`)
- phrase coverage: `10/10` (`1.0`)
- lowering smells: `6`
- provenance_lint findings: `0` (strong `0`, soft `0`)
- provenance back-translation: status `ok`, score `0.869`, warnings `2`
- diagnostic gate: `needs_review` (fail `0`, warning `37`)
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
| parser_strict | ok | 0 | 2.625 |
| semantic_lint | ok | 0 | 0.14 |
| token_provenance | ok | 0 | 4.335 |
| provenance_lint | ok | 0 | 0.218 |
| provenance_backtranslation | ok | 0 | 0.246 |
| family_coverage | ok | 0 | 0.142 |
| source_phrase_coverage | ok | 0 | 0.178 |
| lowering_audit | ok | 0 | 0.125 |
| legacy_metrics | ok | 0 | 34.684 |
| diagnostic_suite_skip_llm | ok | 0 | 4.197 |
| quality_snapshot | ok | 0 | 5.151 |
| single_semantic_judge_and_render | ok | 0 | 33.971 |
| multi_judge | ok | 0 | 78.136 |
| corpus_aware_multi_judge | ok | 0 | 103.506 |
| diagnostic_suite_with_llm | ok | 0 | 21.836 |
| quality_snapshot_final | ok | 0 | 4.394 |
