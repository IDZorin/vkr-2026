# Financial Methodology Entry Checks: section_1_2

- generated_at: `2026-05-14T22:42:13`
- with_llm: `False`
- overall_status: `ok`

## Summary

- clean_gate: `accepted`
- blocking_conditions: ``
- semantic_lint findings: `0` (strong `0`, soft `0`)
- token coverage: `65/70` (`0.929`)
- phrase coverage: `12/12` (`1.0`)
- lowering smells: `0`
- provenance_lint findings: `0` (strong `0`, soft `0`)
- provenance back-translation: status `ok`, score `0.823`, warnings `3`
- role annotation lint: status `ok`, findings `0` (strong `0`, soft `0`)
- role annotation judge: `consistent` / `correct` (issues `0`)
- diagnostic gate: `needs_review` (fail `0`, warning `35`)
- single semantic judge: `corresponds` / `exact_equivalence`
- multi judge: `None` (agreement `None`, unanimous `None`)
- corpus-aware multi judge: local `None` / corpus `None` (agreement `None`)

## Uncovered Tokens

- `mean`, `calculat`, `addition`, `distribut`, `whether`

## Uncovered Phrases

- none

## Steps

| step | status | returncode | duration_s |
| --- | --- | ---: | ---: |
| parser_strict | ok | 0 | 2.444 |
| semantic_lint | ok | 0 | 0.134 |
| token_provenance | ok | 0 | 2.712 |
| provenance_lint | ok | 0 | 0.215 |
| provenance_backtranslation | ok | 0 | 0.22 |
| family_coverage | ok | 0 | 0.129 |
| source_phrase_coverage | ok | 0 | 0.158 |
| lowering_audit | ok | 0 | 0.104 |
| role_annotation_lint | ok | 0 | 0.207 |
| legacy_metrics | ok | 0 | 23.663 |
| diagnostic_suite_skip_llm | ok | 0 | 2.223 |
| quality_snapshot | ok | 0 | 2.524 |
