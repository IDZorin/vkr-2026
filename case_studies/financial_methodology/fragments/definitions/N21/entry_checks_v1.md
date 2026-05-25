# Financial Methodology Entry Checks: N21

- generated_at: `2026-05-12T14:46:47`
- with_llm: `True`
- overall_status: `ok`

## Summary

- clean_gate: `accepted`
- blocking_conditions: ``
- semantic_lint findings: `0` (strong `0`, soft `0`)
- token coverage: `7/7` (`1.0`)
- phrase coverage: `2/2` (`1.0`)
- lowering smells: `0`
- provenance_lint findings: `0` (strong `0`, soft `0`)
- provenance back-translation: status `ok`, score `0.863`, warnings `0`
- diagnostic gate: `needs_review` (fail `0`, warning `30`)
- single semantic judge: `corresponds` / `exact_equivalence`
- multi judge: `partially_corresponds` (agreement `0.75`, unanimous `False`)
- corpus-aware multi judge: local `corresponds` / corpus `corresponds` (agreement `1.0`)

## Uncovered Tokens

- none

## Uncovered Phrases

- none

## Steps

| step | status | returncode | duration_s |
| --- | --- | ---: | ---: |
| parser_strict | ok | 0 | 2.096 |
| semantic_lint | ok | 0 | 0.115 |
| token_provenance | ok | 0 | 2.264 |
| provenance_lint | ok | 0 | 0.173 |
| provenance_backtranslation | ok | 0 | 0.185 |
| family_coverage | ok | 0 | 0.116 |
| source_phrase_coverage | ok | 0 | 0.153 |
| lowering_audit | ok | 0 | 0.098 |
| legacy_metrics | ok | 0 | 20.337 |
| diagnostic_suite_skip_llm | ok | 0 | 2.121 |
| quality_snapshot | ok | 0 | 2.409 |
| single_semantic_judge_and_render | ok | 0 | 22.29 |
| multi_judge | ok | 0 | 71.265 |
| corpus_aware_multi_judge | ok | 0 | 65.424 |
| diagnostic_suite_with_llm | ok | 0 | 2.29 |
| quality_snapshot_final | ok | 0 | 3.318 |
