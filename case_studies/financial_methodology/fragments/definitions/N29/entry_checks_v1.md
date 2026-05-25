# Financial Methodology Entry Checks: N29

- generated_at: `2026-05-10T20:14:26`
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
| parser_strict | ok | 0 | 2.382 |
| semantic_lint | ok | 0 | 0.131 |
| token_provenance | ok | 0 | 2.286 |
| provenance_lint | ok | 0 | 0.172 |
| provenance_backtranslation | ok | 0 | 0.203 |
| family_coverage | ok | 0 | 0.111 |
| source_phrase_coverage | ok | 0 | 0.142 |
| lowering_audit | ok | 0 | 0.103 |
| legacy_metrics | ok | 0 | 19.797 |
| diagnostic_suite_skip_llm | ok | 0 | 1.945 |
| quality_snapshot | ok | 0 | 2.321 |
| single_semantic_judge_and_render | ok | 0 | 21.282 |
| multi_judge | ok | 0 | 31.849 |
| corpus_aware_multi_judge | ok | 0 | 53.878 |
| diagnostic_suite_with_llm | ok | 0 | 13.705 |
| quality_snapshot_final | ok | 0 | 2.29 |
