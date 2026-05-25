# Financial Methodology Entry Checks: N32

- generated_at: `2026-05-10T20:19:18`
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
- provenance back-translation: status `ok`, score `0.968`, warnings `0`
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
| parser_strict | ok | 0 | 2.015 |
| semantic_lint | ok | 0 | 0.112 |
| token_provenance | ok | 0 | 2.208 |
| provenance_lint | ok | 0 | 0.166 |
| provenance_backtranslation | ok | 0 | 0.19 |
| family_coverage | ok | 0 | 0.115 |
| source_phrase_coverage | ok | 0 | 0.146 |
| lowering_audit | ok | 0 | 0.101 |
| legacy_metrics | ok | 0 | 20.32 |
| diagnostic_suite_skip_llm | ok | 0 | 2.079 |
| quality_snapshot | ok | 0 | 2.616 |
| single_semantic_judge_and_render | ok | 0 | 21.578 |
| multi_judge | ok | 0 | 40.732 |
| corpus_aware_multi_judge | ok | 0 | 48.53 |
| diagnostic_suite_with_llm | ok | 0 | 15.53 |
| quality_snapshot_final | ok | 0 | 2.422 |
