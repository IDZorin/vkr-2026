# Financial Methodology Entry Checks: N26

- generated_at: `2026-05-20T03:59:12`
- with_llm: `False`
- overall_status: `ok`

## Summary

- clean_gate: `accepted`
- blocking_conditions: ``
- semantic_lint findings: `2` (strong `0`, soft `2`)
- token coverage: `10/11` (`0.909`)
- phrase coverage: `4/4` (`1.0`)
- lowering smells: `2`
- provenance_lint findings: `0` (strong `0`, soft `0`)
- provenance back-translation: status `ok`, score `0.675`, warnings `3`
- role annotation lint: status `ok`, findings `0` (strong `0`, soft `0`)
- role annotation judge: `None` / `None` (issues `0`)
- diagnostic gate: `needs_review` (fail `0`, warning `35`)
- single semantic judge: `partially_corresponds` / `partial_overlap`
- multi judge: `partially_corresponds` (agreement `1.0`, unanimous `True`)
- corpus-aware multi judge: local `None` / corpus `None` (agreement `None`)

## Uncovered Tokens

- `not`

## Uncovered Phrases

- none

## Steps

| step | status | returncode | duration_s |
| --- | --- | ---: | ---: |
| parser_strict | ok | 0 | 5.104 |
| semantic_lint | ok | 0 | 0.185 |
| token_provenance | ok | 0 | 3.1 |
| provenance_lint | ok | 0 | 0.233 |
| provenance_backtranslation | ok | 0 | 0.249 |
| family_coverage | ok | 0 | 0.147 |
| source_phrase_coverage | ok | 0 | 0.19 |
| lowering_audit | ok | 0 | 0.123 |
| role_annotation_lint | ok | 0 | 0.217 |
| legacy_metrics | ok | 0 | 34.724 |
| diagnostic_suite_skip_llm | ok | 0 | 4.692 |
| quality_snapshot | ok | 0 | 3.142 |
