# Financial Methodology Entry Checks: section_2_3

- generated_at: `2026-05-14T23:11:03`
- with_llm: `False`
- overall_status: `ok`

## Summary

- clean_gate: `accepted`
- blocking_conditions: ``
- semantic_lint findings: `0` (strong `0`, soft `0`)
- token coverage: `20/28` (`0.714`)
- phrase coverage: `4/4` (`1.0`)
- lowering smells: `0`
- provenance_lint findings: `0` (strong `0`, soft `0`)
- provenance back-translation: status `ok`, score `0.833`, warnings `1`
- role annotation lint: status `ok`, findings `0` (strong `0`, soft `0`)
- role annotation judge: `consistent` / `correct` (issues `0`)
- diagnostic gate: `needs_review` (fail `0`, warning `31`)
- single semantic judge: `corresponds` / `exact_equivalence`
- multi judge: `None` (agreement `None`, unanimous `None`)
- corpus-aware multi judge: local `None` / corpus `None` (agreement `None`)

## Uncovered Tokens

- `assign`, `subject`, `follow`, `constraint`, `total`, `until`, `both`, `satisfi`

## Uncovered Phrases

- none

## Steps

| step | status | returncode | duration_s |
| --- | --- | ---: | ---: |
| parser_strict | ok | 0 | 2.812 |
| semantic_lint | ok | 0 | 0.167 |
| token_provenance | ok | 0 | 2.953 |
| provenance_lint | ok | 0 | 0.222 |
| provenance_backtranslation | ok | 0 | 0.252 |
| family_coverage | ok | 0 | 0.166 |
| source_phrase_coverage | ok | 0 | 0.205 |
| lowering_audit | ok | 0 | 0.45 |
| role_annotation_lint | ok | 0 | 0.24 |
| legacy_metrics | ok | 0 | 56.121 |
| diagnostic_suite_skip_llm | ok | 0 | 2.76 |
| quality_snapshot | ok | 0 | 2.885 |
