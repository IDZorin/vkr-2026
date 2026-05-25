# Financial Methodology Entry Checks: section_5_1

- generated_at: `2026-05-10T16:01:40`
- with_llm: `False`
- overall_status: `ok`

## Summary

- clean_gate: `accepted`
- blocking_conditions: ``
- semantic_lint findings: `0` (strong `0`, soft `0`)
- token coverage: `21/24` (`0.875`)
- phrase coverage: `3/3` (`1.0`)
- lowering smells: `0`
- provenance_lint findings: `0` (strong `0`, soft `0`)
- provenance back-translation: status `ok`, score `0.891`, warnings `1`
- diagnostic gate: `needs_review` (fail `0`, warning `31`)
- single semantic judge: `None` / `None`
- multi judge: `None` (agreement `None`, unanimous `None`)
- corpus-aware multi judge: local `None` / corpus `None` (agreement `None`)

## Uncovered Tokens

- `may`, `exercis`, `made`

## Uncovered Phrases

- none

## Steps

| step | status | returncode | duration_s |
| --- | --- | ---: | ---: |
| parser_strict | ok | 0 | 2.451 |
| semantic_lint | ok | 0 | 0.113 |
| token_provenance | ok | 0 | 2.665 |
| provenance_lint | ok | 0 | 0.206 |
| provenance_backtranslation | ok | 0 | 0.214 |
| family_coverage | ok | 0 | 0.114 |
| source_phrase_coverage | ok | 0 | 0.164 |
| lowering_audit | ok | 0 | 0.106 |
| legacy_metrics | ok | 0 | 22.472 |
| diagnostic_suite_skip_llm | ok | 0 | 2.135 |
| quality_snapshot | ok | 0 | 2.929 |
