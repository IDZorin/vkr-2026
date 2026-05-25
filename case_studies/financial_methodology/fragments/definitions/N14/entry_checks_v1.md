# Financial Methodology Entry Checks: N14

- generated_at: `2026-05-16T21:15:20`
- with_llm: `False`
- overall_status: `ok`

## Summary

- clean_gate: `accepted`
- blocking_conditions: ``
- semantic_lint findings: `0` (strong `0`, soft `0`)
- token coverage: `17/17` (`1.0`)
- phrase coverage: `6/6` (`1.0`)
- lowering smells: `0`
- provenance_lint findings: `0` (strong `0`, soft `0`)
- provenance back-translation: status `ok`, score `0.89`, warnings `1`
- role annotation lint: status `ok`, findings `0` (strong `0`, soft `0`)
- role annotation judge: `None` / `None` (issues `0`)
- diagnostic gate: `needs_review` (fail `0`, warning `30`)
- single semantic judge: `None` / `None`
- multi judge: `None` (agreement `None`, unanimous `None`)
- corpus-aware multi judge: local `None` / corpus `None` (agreement `None`)

## Uncovered Tokens

- none

## Uncovered Phrases

- none

## Steps

| step | status | returncode | duration_s |
| --- | --- | ---: | ---: |
| parser_strict | ok | 0 | 2.251 |
| semantic_lint | ok | 0 | 0.123 |
| token_provenance | ok | 0 | 2.375 |
| provenance_lint | ok | 0 | 0.218 |
| provenance_backtranslation | ok | 0 | 0.222 |
| family_coverage | ok | 0 | 0.126 |
| source_phrase_coverage | ok | 0 | 0.169 |
| lowering_audit | ok | 0 | 0.114 |
| role_annotation_lint | ok | 0 | 0.197 |
| legacy_metrics | ok | 0 | 21.331 |
| diagnostic_suite_skip_llm | ok | 0 | 2.399 |
| quality_snapshot | ok | 0 | 2.545 |
