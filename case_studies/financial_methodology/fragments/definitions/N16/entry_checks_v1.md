# Financial Methodology Entry Checks: N16

- generated_at: `2026-05-10T19:51:03`
- with_llm: `True`
- overall_status: `ok`

## Summary

- clean_gate: `accepted`
- blocking_conditions: ``
- semantic_lint findings: `0` (strong `0`, soft `0`)
- token coverage: `6/6` (`1.0`)
- phrase coverage: `2/2` (`1.0`)
- lowering smells: `1`
- provenance_lint findings: `0` (strong `0`, soft `0`)
- provenance back-translation: status `ok`, score `0.959`, warnings `0`
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
| parser_strict | ok | 0 | 2.331 |
| semantic_lint | ok | 0 | 0.132 |
| token_provenance | ok | 0 | 2.843 |
| provenance_lint | ok | 0 | 0.272 |
| provenance_backtranslation | ok | 0 | 0.282 |
| family_coverage | ok | 0 | 0.151 |
| source_phrase_coverage | ok | 0 | 0.214 |
| lowering_audit | ok | 0 | 0.146 |
| legacy_metrics | ok | 0 | 26.388 |
| diagnostic_suite_skip_llm | ok | 0 | 2.438 |
| quality_snapshot | ok | 0 | 2.681 |
| single_semantic_judge_and_render | ok | 0 | 24.85 |
| multi_judge | ok | 0 | 37.921 |
| corpus_aware_multi_judge | ok | 0 | 36.338 |
| diagnostic_suite_with_llm | ok | 0 | 15.871 |
| quality_snapshot_final | ok | 0 | 2.778 |
