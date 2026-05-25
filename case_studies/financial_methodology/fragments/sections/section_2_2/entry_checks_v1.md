# Financial Methodology Entry Checks: section_2_2

- generated_at: `2026-05-16T23:10:05`
- with_llm: `False`
- overall_status: `ok`

## Summary

- clean_gate: `accepted`
- blocking_conditions: ``
- semantic_lint findings: `1` (strong `0`, soft `0`)
- token coverage: `48/55` (`0.873`)
- phrase coverage: `14/14` (`1.0`)
- lowering smells: `0`
- provenance_lint findings: `0` (strong `0`, soft `0`)
- provenance back-translation: status `ok`, score `0.82`, warnings `2`
- role annotation lint: status `None`, findings `None` (strong `None`, soft `None`)
- role annotation judge: `None` / `None` (issues `0`)
- diagnostic gate: `needs_review` (fail `0`, warning `29`)
- single semantic judge: `corresponds` / `same_meaning_poor_wording`
- multi judge: `partially_corresponds` (agreement `1.0`, unanimous `True`)
- corpus-aware multi judge: local `None` / corpus `None` (agreement `None`)

## Uncovered Tokens

- `accordance`, `follow`, `under`, `framework`, `case`, `contain`, `total`

## Uncovered Phrases

- none

## Steps

| step | status | returncode | duration_s |
| --- | --- | ---: | ---: |
| parser_strict | ok | 0 | 2.763 |
| semantic_lint | ok | 0 | 0.235 |
| token_provenance | ok | 0 | 3.454 |
| provenance_lint | ok | 0 | 0.257 |
| provenance_backtranslation | ok | 0 | 0.249 |
| family_coverage | ok | 0 | 0.149 |
| source_phrase_coverage | ok | 0 | 0.194 |
| lowering_audit | ok | 0 | 0.129 |
| legacy_metrics | ok | 0 | 54.344 |
| diagnostic_suite_skip_llm | ok | 0 | 3.115 |
| quality_snapshot | ok | 0 | 3.208 |
