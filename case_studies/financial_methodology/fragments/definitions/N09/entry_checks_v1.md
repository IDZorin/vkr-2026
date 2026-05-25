# Financial Methodology Entry Checks: N09

- generated_at: `2026-05-15T12:21:41`
- with_llm: `False`
- overall_status: `ok`

## Summary

- clean_gate: `accepted`
- blocking_conditions: ``
- semantic_lint findings: `0` (strong `0`, soft `0`)
- token coverage: `11/11` (`1.0`)
- phrase coverage: `6/6` (`1.0`)
- lowering smells: `0`
- provenance_lint findings: `0` (strong `0`, soft `0`)
- provenance back-translation: status `ok`, score `0.919`, warnings `0`
- role annotation lint: status `None`, findings `None` (strong `None`, soft `None`)
- role annotation judge: `None` / `None` (issues `0`)
- diagnostic gate: `needs_review` (fail `0`, warning `26`)
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
| parser_strict | ok | 0 | 3.989 |
| semantic_lint | ok | 0 | 0.198 |
| token_provenance | ok | 0 | 3.816 |
| provenance_lint | ok | 0 | 0.216 |
| provenance_backtranslation | ok | 0 | 0.228 |
| family_coverage | ok | 0 | 0.166 |
| source_phrase_coverage | ok | 0 | 0.197 |
| lowering_audit | ok | 0 | 0.144 |
| legacy_metrics | ok | 0 | 30.044 |
| diagnostic_suite_skip_llm | ok | 0 | 3.281 |
| quality_snapshot | ok | 0 | 4.689 |
