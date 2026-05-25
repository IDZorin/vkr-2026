# Financial Methodology Entry Checks: N19

- generated_at: `2026-05-12T14:18:56`
- with_llm: `False`
- overall_status: `ok`

## Summary

- clean_gate: `accepted`
- blocking_conditions: ``
- semantic_lint findings: `0` (strong `0`, soft `0`)
- token coverage: `4/4` (`1.0`)
- phrase coverage: `2/2` (`1.0`)
- lowering smells: `0`
- provenance_lint findings: `0` (strong `0`, soft `0`)
- provenance back-translation: status `ok`, score `0.839`, warnings `0`
- diagnostic gate: `needs_review` (fail `0`, warning `27`)
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
| parser_strict | ok | 0 | 2.876 |
| semantic_lint | ok | 0 | 0.164 |
| token_provenance | ok | 0 | 2.887 |
| provenance_lint | ok | 0 | 0.22 |
| provenance_backtranslation | ok | 0 | 0.227 |
| family_coverage | ok | 0 | 0.148 |
| source_phrase_coverage | ok | 0 | 0.184 |
| lowering_audit | ok | 0 | 0.128 |
| legacy_metrics | ok | 0 | 26.295 |
| diagnostic_suite_skip_llm | ok | 0 | 2.688 |
| quality_snapshot | ok | 0 | 2.772 |
