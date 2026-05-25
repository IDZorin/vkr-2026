# Financial Methodology Entry Checks: N05

- generated_at: `2026-05-12T14:18:54`
- with_llm: `False`
- overall_status: `ok`

## Summary

- clean_gate: `accepted`
- blocking_conditions: ``
- semantic_lint findings: `0` (strong `0`, soft `0`)
- token coverage: `6/6` (`1.0`)
- phrase coverage: `3/3` (`1.0`)
- lowering smells: `0`
- provenance_lint findings: `0` (strong `0`, soft `0`)
- provenance back-translation: status `ok`, score `0.87`, warnings `0`
- diagnostic gate: `needs_review` (fail `0`, warning `25`)
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
| parser_strict | ok | 0 | 2.759 |
| semantic_lint | ok | 0 | 0.142 |
| token_provenance | ok | 0 | 2.856 |
| provenance_lint | ok | 0 | 0.22 |
| provenance_backtranslation | ok | 0 | 0.23 |
| family_coverage | ok | 0 | 0.136 |
| source_phrase_coverage | ok | 0 | 0.187 |
| lowering_audit | ok | 0 | 0.119 |
| legacy_metrics | ok | 0 | 24.507 |
| diagnostic_suite_skip_llm | ok | 0 | 2.766 |
| quality_snapshot | ok | 0 | 2.865 |
