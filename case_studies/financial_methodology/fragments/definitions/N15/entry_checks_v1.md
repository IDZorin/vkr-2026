# Financial Methodology Entry Checks: N15

- generated_at: `2026-05-14T15:43:25`
- with_llm: `False`
- overall_status: `ok`

## Summary

- clean_gate: `accepted`
- blocking_conditions: ``
- semantic_lint findings: `0` (strong `0`, soft `0`)
- token coverage: `9/9` (`1.0`)
- phrase coverage: `2/2` (`1.0`)
- lowering smells: `0`
- provenance_lint findings: `0` (strong `0`, soft `0`)
- provenance back-translation: status `ok`, score `0.885`, warnings `0`
- role annotation lint: status `None`, findings `None` (strong `None`, soft `None`)
- role annotation judge: `None` / `None` (issues `0`)
- diagnostic gate: `needs_review` (fail `0`, warning `29`)
- single semantic judge: `corresponds` / `exact_equivalence`
- multi judge: `partially_corresponds` (agreement `0.75`, unanimous `False`)
- corpus-aware multi judge: local `corresponds` / corpus `corresponds` (agreement `1.0`)

## Uncovered Tokens

- none

## Uncovered Phrases

- none

## Steps

| step | status | returncode | duration_s |
| --- | --- | ---: | ---: |
| parser_strict | ok | 0 | 13.695 |
| semantic_lint | ok | 0 | 0.19 |
| token_provenance | ok | 0 | 4.378 |
| provenance_lint | ok | 0 | 0.247 |
| provenance_backtranslation | ok | 0 | 0.243 |
| family_coverage | ok | 0 | 0.153 |
| source_phrase_coverage | ok | 0 | 0.188 |
| lowering_audit | ok | 0 | 0.123 |
| legacy_metrics | ok | 0 | 129.085 |
| diagnostic_suite_skip_llm | ok | 0 | 2.158 |
| quality_snapshot | ok | 0 | 2.555 |
