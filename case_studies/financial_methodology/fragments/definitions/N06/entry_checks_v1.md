# Financial Methodology Entry Checks: N06

- generated_at: `2026-05-12T14:18:56`
- with_llm: `False`
- overall_status: `ok`

## Summary

- clean_gate: `accepted`
- blocking_conditions: ``
- semantic_lint findings: `0` (strong `0`, soft `0`)
- token coverage: `10/10` (`1.0`)
- phrase coverage: `4/4` (`1.0`)
- lowering smells: `0`
- provenance_lint findings: `0` (strong `0`, soft `0`)
- provenance back-translation: status `ok`, score `1.0`, warnings `0`
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
| parser_strict | ok | 0 | 2.853 |
| semantic_lint | ok | 0 | 0.157 |
| token_provenance | ok | 0 | 2.919 |
| provenance_lint | ok | 0 | 0.218 |
| provenance_backtranslation | ok | 0 | 0.227 |
| family_coverage | ok | 0 | 0.147 |
| source_phrase_coverage | ok | 0 | 0.184 |
| lowering_audit | ok | 0 | 0.131 |
| legacy_metrics | ok | 0 | 26.501 |
| diagnostic_suite_skip_llm | ok | 0 | 2.666 |
| quality_snapshot | ok | 0 | 2.737 |
