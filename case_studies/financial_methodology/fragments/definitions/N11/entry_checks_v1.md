# Financial Methodology Entry Checks: N11

- generated_at: `2026-05-16T23:10:03`
- with_llm: `False`
- overall_status: `ok`

## Summary

- clean_gate: `accepted`
- blocking_conditions: ``
- semantic_lint findings: `0` (strong `0`, soft `0`)
- token coverage: `3/3` (`1.0`)
- phrase coverage: `2/2` (`1.0`)
- lowering smells: `0`
- provenance_lint findings: `0` (strong `0`, soft `0`)
- provenance back-translation: status `ok`, score `0.857`, warnings `0`
- role annotation lint: status `None`, findings `None` (strong `None`, soft `None`)
- role annotation judge: `None` / `None` (issues `0`)
- diagnostic gate: `needs_review` (fail `0`, warning `25`)
- single semantic judge: `corresponds` / `exact_equivalence`
- multi judge: `None` (agreement `None`, unanimous `None`)
- corpus-aware multi judge: local `None` / corpus `None` (agreement `None`)

## Uncovered Tokens

- none

## Uncovered Phrases

- none

## Steps

| step | status | returncode | duration_s |
| --- | --- | ---: | ---: |
| parser_strict | ok | 0 | 3.772 |
| semantic_lint | ok | 0 | 0.2 |
| token_provenance | ok | 0 | 3.152 |
| provenance_lint | ok | 0 | 0.288 |
| provenance_backtranslation | ok | 0 | 0.36 |
| family_coverage | ok | 0 | 0.252 |
| source_phrase_coverage | ok | 0 | 0.229 |
| lowering_audit | ok | 0 | 0.479 |
| legacy_metrics | ok | 0 | 54.258 |
| diagnostic_suite_skip_llm | ok | 0 | 2.8 |
| quality_snapshot | ok | 0 | 3.288 |
