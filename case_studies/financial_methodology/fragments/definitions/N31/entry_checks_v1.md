# Financial Methodology Entry Checks: N31

- generated_at: `2026-05-20T03:50:26`
- with_llm: `False`
- overall_status: `ok`

## Summary

- clean_gate: `accepted`
- blocking_conditions: ``
- semantic_lint findings: `0` (strong `0`, soft `0`)
- token coverage: `10/11` (`0.909`)
- phrase coverage: `4/4` (`1.0`)
- lowering smells: `0`
- provenance_lint findings: `0` (strong `0`, soft `0`)
- provenance back-translation: status `ok`, score `0.887`, warnings `0`
- role annotation lint: status `ok`, findings `0` (strong `0`, soft `0`)
- role annotation judge: `None` / `None` (issues `0`)
- diagnostic gate: `needs_review` (fail `0`, warning `31`)
- single semantic judge: `corresponds` / `same_meaning_poor_wording`
- multi judge: `partially_corresponds` (agreement `0.5`, unanimous `False`)
- corpus-aware multi judge: local `None` / corpus `None` (agreement `None`)

## Uncovered Tokens

- `respect`

## Uncovered Phrases

- none

## Steps

| step | status | returncode | duration_s |
| --- | --- | ---: | ---: |
| parser_strict | ok | 0 | 3.64 |
| semantic_lint | ok | 0 | 0.209 |
| token_provenance | ok | 0 | 5.58 |
| provenance_lint | ok | 0 | 0.32 |
| provenance_backtranslation | ok | 0 | 0.282 |
| family_coverage | ok | 0 | 0.176 |
| source_phrase_coverage | ok | 0 | 0.214 |
| lowering_audit | ok | 0 | 0.146 |
| role_annotation_lint | ok | 0 | 0.268 |
| legacy_metrics | ok | 0 | 44.533 |
| diagnostic_suite_skip_llm | ok | 0 | 5.883 |
| quality_snapshot | ok | 0 | 5.514 |
