# Financial Methodology Entry Checks: N27

- generated_at: `2026-05-15T12:23:49`
- with_llm: `False`
- overall_status: `ok`

## Summary

- clean_gate: `accepted`
- blocking_conditions: ``
- semantic_lint findings: `0` (strong `0`, soft `0`)
- token coverage: `8/8` (`1.0`)
- phrase coverage: `3/3` (`1.0`)
- lowering smells: `0`
- provenance_lint findings: `0` (strong `0`, soft `0`)
- provenance back-translation: status `ok`, score `0.621`, warnings `3`
- role annotation lint: status `None`, findings `None` (strong `None`, soft `None`)
- role annotation judge: `None` / `None` (issues `0`)
- diagnostic gate: `needs_review` (fail `0`, warning `31`)
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
| parser_strict | ok | 0 | 3.312 |
| semantic_lint | ok | 0 | 0.14 |
| token_provenance | ok | 0 | 2.962 |
| provenance_lint | ok | 0 | 0.247 |
| provenance_backtranslation | ok | 0 | 0.255 |
| family_coverage | ok | 0 | 0.142 |
| source_phrase_coverage | ok | 0 | 0.189 |
| lowering_audit | ok | 0 | 0.125 |
| legacy_metrics | ok | 0 | 28.022 |
| diagnostic_suite_skip_llm | ok | 0 | 2.752 |
| quality_snapshot | ok | 0 | 3.805 |
