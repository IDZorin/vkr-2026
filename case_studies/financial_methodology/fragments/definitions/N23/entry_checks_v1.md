# Financial Methodology Entry Checks: N23

- generated_at: `2026-05-12T15:11:45`
- with_llm: `False`
- overall_status: `ok`

## Summary

- clean_gate: `accepted`
- blocking_conditions: ``
- semantic_lint findings: `0` (strong `0`, soft `0`)
- token coverage: `8/8` (`1.0`)
- phrase coverage: `2/2` (`1.0`)
- lowering smells: `0`
- provenance_lint findings: `0` (strong `0`, soft `0`)
- provenance back-translation: status `ok`, score `0.875`, warnings `0`
- diagnostic gate: `needs_review` (fail `0`, warning `27`)
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
| parser_strict | ok | 0 | 2.533 |
| semantic_lint | ok | 0 | 0.132 |
| token_provenance | ok | 0 | 2.726 |
| provenance_lint | ok | 0 | 0.202 |
| provenance_backtranslation | ok | 0 | 0.214 |
| family_coverage | ok | 0 | 0.131 |
| source_phrase_coverage | ok | 0 | 0.167 |
| lowering_audit | ok | 0 | 0.117 |
| legacy_metrics | ok | 0 | 24.992 |
| diagnostic_suite_skip_llm | ok | 0 | 2.531 |
| quality_snapshot | ok | 0 | 2.625 |
