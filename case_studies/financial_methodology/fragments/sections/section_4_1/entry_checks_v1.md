# Financial Methodology Entry Checks: section_4_1

- generated_at: `2026-05-14T20:53:20`
- with_llm: `False`
- overall_status: `ok`

## Summary

- clean_gate: `accepted`
- blocking_conditions: ``
- semantic_lint findings: `0` (strong `0`, soft `0`)
- token coverage: `68/81` (`0.84`)
- phrase coverage: `19/20` (`0.95`)
- lowering smells: `0`
- provenance_lint findings: `0` (strong `0`, soft `0`)
- provenance back-translation: status `ok`, score `0.76`, warnings `5`
- role annotation lint: status `ok`, findings `0` (strong `0`, soft `0`)
- role annotation judge: `consistent` / `correct` (issues `0`)
- diagnostic gate: `needs_review` (fail `0`, warning `33`)
- single semantic judge: `corresponds` / `exact_equivalence`
- multi judge: `partially_corresponds` (agreement `1.0`, unanimous `True`)
- corpus-aware multi judge: local `partially_corresponds` / corpus `corresponds` (agreement `1.0`)

## Uncovered Tokens

- `stipulat`, `account`, `case`, `other`, `than`, `call`, `such`, `more`, `can`, `under`, `construction`, `follow`, `where`

## Uncovered Phrases

- `Where`

## Steps

| step | status | returncode | duration_s |
| --- | --- | ---: | ---: |
| parser_strict | ok | 0 | 2.416 |
| semantic_lint | ok | 0 | 0.142 |
| token_provenance | ok | 0 | 2.606 |
| provenance_lint | ok | 0 | 0.271 |
| provenance_backtranslation | ok | 0 | 0.265 |
| family_coverage | ok | 0 | 0.143 |
| source_phrase_coverage | ok | 0 | 0.171 |
| lowering_audit | ok | 0 | 0.129 |
| role_annotation_lint | ok | 0 | 0.259 |
| legacy_metrics | ok | 0 | 25.299 |
| diagnostic_suite_skip_llm | ok | 0 | 2.845 |
| quality_snapshot | ok | 0 | 2.875 |
