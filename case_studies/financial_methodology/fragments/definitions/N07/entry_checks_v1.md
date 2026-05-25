# Financial Methodology Entry Checks: N07

- generated_at: `2026-05-16T21:13:10`
- with_llm: `False`
- overall_status: `ok`

## Summary

- clean_gate: `accepted`
- blocking_conditions: ``
- semantic_lint findings: `0` (strong `0`, soft `0`)
- token coverage: `19/20` (`0.95`)
- phrase coverage: `6/6` (`1.0`)
- lowering smells: `0`
- provenance_lint findings: `0` (strong `0`, soft `0`)
- provenance back-translation: status `ok`, score `0.734`, warnings `1`
- role annotation lint: status `ok`, findings `0` (strong `0`, soft `0`)
- role annotation judge: `None` / `None` (issues `0`)
- diagnostic gate: `needs_review` (fail `0`, warning `31`)
- single semantic judge: `None` / `None`
- multi judge: `None` (agreement `None`, unanimous `None`)
- corpus-aware multi judge: local `None` / corpus `None` (agreement `None`)

## Uncovered Tokens

- `respect`

## Uncovered Phrases

- none

## Steps

| step | status | returncode | duration_s |
| --- | --- | ---: | ---: |
| parser_strict | ok | 0 | 2.492 |
| semantic_lint | ok | 0 | 0.129 |
| token_provenance | ok | 0 | 2.447 |
| provenance_lint | ok | 0 | 0.198 |
| provenance_backtranslation | ok | 0 | 0.205 |
| family_coverage | ok | 0 | 0.121 |
| source_phrase_coverage | ok | 0 | 0.156 |
| lowering_audit | ok | 0 | 0.106 |
| role_annotation_lint | ok | 0 | 0.194 |
| legacy_metrics | ok | 0 | 22.171 |
| diagnostic_suite_skip_llm | ok | 0 | 2.504 |
| quality_snapshot | ok | 0 | 2.465 |
