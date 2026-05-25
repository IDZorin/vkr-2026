# Financial Methodology Entry Checks: N10

- generated_at: `2026-05-15T12:22:22`
- with_llm: `False`
- overall_status: `ok`

## Summary

- clean_gate: `accepted`
- blocking_conditions: ``
- semantic_lint findings: `0` (strong `0`, soft `0`)
- token coverage: `12/13` (`0.923`)
- phrase coverage: `3/3` (`1.0`)
- lowering smells: `0`
- provenance_lint findings: `0` (strong `0`, soft `0`)
- provenance back-translation: status `ok`, score `0.956`, warnings `0`
- role annotation lint: status `None`, findings `None` (strong `None`, soft `None`)
- role annotation judge: `None` / `None` (issues `0`)
- diagnostic gate: `needs_review` (fail `0`, warning `28`)
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
| parser_strict | ok | 0 | 2.809 |
| semantic_lint | ok | 0 | 0.163 |
| token_provenance | ok | 0 | 2.942 |
| provenance_lint | ok | 0 | 0.232 |
| provenance_backtranslation | ok | 0 | 0.255 |
| family_coverage | ok | 0 | 0.149 |
| source_phrase_coverage | ok | 0 | 0.199 |
| lowering_audit | ok | 0 | 0.17 |
| legacy_metrics | ok | 0 | 26.853 |
| diagnostic_suite_skip_llm | ok | 0 | 2.573 |
| quality_snapshot | ok | 0 | 4.174 |
