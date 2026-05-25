# Financial Methodology Entry Checks: N08

- generated_at: `2026-05-20T03:36:55`
- with_llm: `False`
- overall_status: `ok`

## Summary

- clean_gate: `accepted`
- blocking_conditions: ``
- semantic_lint findings: `0` (strong `0`, soft `0`)
- token coverage: `16/18` (`0.889`)
- phrase coverage: `5/5` (`1.0`)
- lowering smells: `0`
- provenance_lint findings: `0` (strong `0`, soft `0`)
- provenance back-translation: status `ok`, score `0.893`, warnings `0`
- role annotation lint: status `ok`, findings `0` (strong `0`, soft `0`)
- role annotation judge: `None` / `None` (issues `0`)
- diagnostic gate: `needs_review` (fail `0`, warning `26`)
- single semantic judge: `corresponds` / `exact_equivalence`
- multi judge: `partially_corresponds` (agreement `0.75`, unanimous `False`)
- corpus-aware multi judge: local `None` / corpus `None` (agreement `None`)

## Uncovered Tokens

- `mean`, `respect`

## Uncovered Phrases

- none

## Steps

| step | status | returncode | duration_s |
| --- | --- | ---: | ---: |
| parser_strict | ok | 0 | 2.779 |
| semantic_lint | ok | 0 | 0.144 |
| token_provenance | ok | 0 | 4.343 |
| provenance_lint | ok | 0 | 0.258 |
| provenance_backtranslation | ok | 0 | 0.359 |
| family_coverage | ok | 0 | 0.161 |
| source_phrase_coverage | ok | 0 | 0.177 |
| lowering_audit | ok | 0 | 0.124 |
| role_annotation_lint | ok | 0 | 0.223 |
| legacy_metrics | ok | 0 | 35.45 |
| diagnostic_suite_skip_llm | ok | 0 | 3.154 |
| quality_snapshot | ok | 0 | 4.631 |
