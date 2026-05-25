# Financial Methodology Entry Checks: N13

- generated_at: `2026-05-16T21:14:48`
- with_llm: `False`
- overall_status: `ok`

## Summary

- clean_gate: `accepted`
- blocking_conditions: ``
- semantic_lint findings: `0` (strong `0`, soft `0`)
- token coverage: `23/24` (`0.958`)
- phrase coverage: `6/6` (`1.0`)
- lowering smells: `0`
- provenance_lint findings: `0` (strong `0`, soft `0`)
- provenance back-translation: status `ok`, score `0.846`, warnings `0`
- role annotation lint: status `ok`, findings `0` (strong `0`, soft `0`)
- role annotation judge: `None` / `None` (issues `0`)
- diagnostic gate: `needs_review` (fail `0`, warning `32`)
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
| parser_strict | ok | 0 | 2.413 |
| semantic_lint | ok | 0 | 0.133 |
| token_provenance | ok | 0 | 2.744 |
| provenance_lint | ok | 0 | 0.216 |
| provenance_backtranslation | ok | 0 | 0.218 |
| family_coverage | ok | 0 | 0.157 |
| source_phrase_coverage | ok | 0 | 0.185 |
| lowering_audit | ok | 0 | 0.114 |
| role_annotation_lint | ok | 0 | 0.209 |
| legacy_metrics | ok | 0 | 21.505 |
| diagnostic_suite_skip_llm | ok | 0 | 2.415 |
| quality_snapshot | ok | 0 | 2.457 |
