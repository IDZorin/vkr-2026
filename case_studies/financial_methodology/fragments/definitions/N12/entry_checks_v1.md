# Financial Methodology Entry Checks: N12

- generated_at: `2026-05-16T21:14:15`
- with_llm: `False`
- overall_status: `ok`

## Summary

- clean_gate: `accepted`
- blocking_conditions: ``
- semantic_lint findings: `0` (strong `0`, soft `0`)
- token coverage: `29/30` (`0.967`)
- phrase coverage: `5/5` (`1.0`)
- lowering smells: `0`
- provenance_lint findings: `0` (strong `0`, soft `0`)
- provenance back-translation: status `ok`, score `0.848`, warnings `0`
- role annotation lint: status `ok`, findings `0` (strong `0`, soft `0`)
- role annotation judge: `None` / `None` (issues `0`)
- diagnostic gate: `needs_review` (fail `0`, warning `33`)
- single semantic judge: `None` / `None`
- multi judge: `None` (agreement `None`, unanimous `None`)
- corpus-aware multi judge: local `None` / corpus `None` (agreement `None`)

## Uncovered Tokens

- `regard`

## Uncovered Phrases

- none

## Steps

| step | status | returncode | duration_s |
| --- | --- | ---: | ---: |
| parser_strict | ok | 0 | 2.355 |
| semantic_lint | ok | 0 | 0.136 |
| token_provenance | ok | 0 | 2.455 |
| provenance_lint | ok | 0 | 0.193 |
| provenance_backtranslation | ok | 0 | 0.199 |
| family_coverage | ok | 0 | 0.117 |
| source_phrase_coverage | ok | 0 | 0.158 |
| lowering_audit | ok | 0 | 0.119 |
| role_annotation_lint | ok | 0 | 0.187 |
| legacy_metrics | ok | 0 | 21.88 |
| diagnostic_suite_skip_llm | ok | 0 | 2.454 |
| quality_snapshot | ok | 0 | 2.565 |
