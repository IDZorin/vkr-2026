# Financial Methodology Entry Checks: section_5_4

- generated_at: `2026-05-14T21:34:01`
- with_llm: `False`
- overall_status: `ok`

## Summary

- clean_gate: `accepted`
- blocking_conditions: ``
- semantic_lint findings: `0` (strong `0`, soft `0`)
- token coverage: `82/92` (`0.891`)
- phrase coverage: `6/7` (`0.857`)
- lowering smells: `0`
- provenance_lint findings: `0` (strong `0`, soft `0`)
- provenance back-translation: status `ok`, score `0.851`, warnings `1`
- role annotation lint: status `ok`, findings `0` (strong `0`, soft `0`)
- role annotation judge: `consistent` / `correct` (issues `0`)
- diagnostic gate: `needs_review` (fail `0`, warning `34`)
- single semantic judge: `corresponds` / `exact_equivalence`
- multi judge: `None` (agreement `None`, unanimous `None`)
- corpus-aware multi judge: local `None` / corpus `None` (agreement `None`)

## Uncovered Tokens

- `mak`, `order`, `neverthel`, `other`, `indicat`, `way`, `particularli`, `can`, `longer`, `how`

## Uncovered Phrases

- `Nevertheless`

## Steps

| step | status | returncode | duration_s |
| --- | --- | ---: | ---: |
| parser_strict | ok | 0 | 2.225 |
| semantic_lint | ok | 0 | 0.127 |
| token_provenance | ok | 0 | 2.529 |
| provenance_lint | ok | 0 | 0.213 |
| provenance_backtranslation | ok | 0 | 0.215 |
| family_coverage | ok | 0 | 0.127 |
| source_phrase_coverage | ok | 0 | 0.167 |
| lowering_audit | ok | 0 | 0.103 |
| role_annotation_lint | ok | 0 | 0.219 |
| legacy_metrics | ok | 0 | 22.865 |
| diagnostic_suite_skip_llm | ok | 0 | 2.308 |
| quality_snapshot | ok | 0 | 2.495 |
