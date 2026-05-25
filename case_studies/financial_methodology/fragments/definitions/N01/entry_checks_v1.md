# Financial Methodology Entry Checks: N01

- generated_at: `2026-05-15T12:20:54`
- with_llm: `False`
- overall_status: `ok`

## Summary

- clean_gate: `accepted`
- blocking_conditions: ``
- semantic_lint findings: `0` (strong `0`, soft `0`)
- token coverage: `14/16` (`0.875`)
- phrase coverage: `3/3` (`1.0`)
- lowering smells: `0`
- provenance_lint findings: `0` (strong `0`, soft `0`)
- provenance back-translation: status `ok`, score `0.87`, warnings `0`
- role annotation lint: status `None`, findings `None` (strong `None`, soft `None`)
- role annotation judge: `None` / `None` (issues `0`)
- diagnostic gate: `needs_review` (fail `0`, warning `30`)
- single semantic judge: `None` / `None`
- multi judge: `None` (agreement `None`, unanimous `None`)
- corpus-aware multi judge: local `None` / corpus `None` (agreement `None`)

## Uncovered Tokens

- `mean`, `respect`

## Uncovered Phrases

- none

## Steps

| step | status | returncode | duration_s |
| --- | --- | ---: | ---: |
| parser_strict | ok | 0 | 4.072 |
| semantic_lint | ok | 0 | 0.184 |
| token_provenance | ok | 0 | 2.797 |
| provenance_lint | ok | 0 | 0.223 |
| provenance_backtranslation | ok | 0 | 0.232 |
| family_coverage | ok | 0 | 0.139 |
| source_phrase_coverage | ok | 0 | 0.196 |
| lowering_audit | ok | 0 | 0.127 |
| legacy_metrics | ok | 0 | 29.229 |
| diagnostic_suite_skip_llm | ok | 0 | 4.313 |
| quality_snapshot | ok | 0 | 3.7 |
