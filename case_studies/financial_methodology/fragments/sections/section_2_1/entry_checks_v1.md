# Financial Methodology Entry Checks: section_2_1

- generated_at: `2026-05-17T10:37:58`
- with_llm: `False`
- overall_status: `ok`

## Summary

- clean_gate: `accepted`
- blocking_conditions: ``
- semantic_lint findings: `1` (strong `0`, soft `1`)
- token coverage: `82/90` (`0.911`)
- phrase coverage: `25/25` (`1.0`)
- lowering smells: `0`
- provenance_lint findings: `0` (strong `0`, soft `0`)
- provenance back-translation: status `ok`, score `0.756`, warnings `12`
- role annotation lint: status `ok`, findings `0` (strong `0`, soft `0`)
- role annotation judge: `consistent` / `correct` (issues `0`)
- diagnostic gate: `needs_review` (fail `0`, warning `36`)
- single semantic judge: `corresponds` / `exact_equivalence`
- multi judge: `None` (agreement `None`, unanimous `None`)
- corpus-aware multi judge: local `None` / corpus `None` (agreement `None`)

## Uncovered Tokens

- `compris`, `fulfill`, `below`, `under`, `inclusion`, `appli`, `follow`, `see`

## Uncovered Phrases

- none

## Steps

| step | status | returncode | duration_s |
| --- | --- | ---: | ---: |
| parser_strict | ok | 0 | 3.114 |
| semantic_lint | ok | 0 | 0.214 |
| token_provenance | ok | 0 | 3.138 |
| provenance_lint | ok | 0 | 0.243 |
| provenance_backtranslation | ok | 0 | 0.284 |
| family_coverage | ok | 0 | 0.164 |
| source_phrase_coverage | ok | 0 | 0.22 |
| lowering_audit | ok | 0 | 0.142 |
| role_annotation_lint | ok | 0 | 0.35 |
| legacy_metrics | ok | 0 | 28.92 |
| diagnostic_suite_skip_llm | ok | 0 | 4.09 |
| quality_snapshot | ok | 0 | 3.594 |
