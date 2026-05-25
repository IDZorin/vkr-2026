# Financial Methodology Entry Checks: N22

- generated_at: `2026-05-10T20:02:03`
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
| parser_strict | ok | 0 | 2.298 |
| semantic_lint | ok | 0 | 0.121 |
| token_provenance | ok | 0 | 2.349 |
| provenance_lint | ok | 0 | 0.169 |
| provenance_backtranslation | ok | 0 | 0.188 |
| family_coverage | ok | 0 | 0.13 |
| source_phrase_coverage | ok | 0 | 0.158 |
| lowering_audit | ok | 0 | 0.112 |
| legacy_metrics | ok | 0 | 21.188 |
| diagnostic_suite_skip_llm | ok | 0 | 2.252 |
| quality_snapshot | ok | 0 | 2.571 |
| single_semantic_judge_and_render | ok | 0 | 24.469 |
| multi_judge | ok | 0 | 52.547 |
| corpus_aware_multi_judge | ok | 0 | 57.577 |
| diagnostic_suite_with_llm | ok | 0 | 14.217 |
| quality_snapshot_final | ok | 0 | 3.39 |
