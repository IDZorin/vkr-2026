# SMT Probe Results v1

Status: `passed_with_review_items`
SMT mode: `hybrid`

## Summary

- `entry_count`: `55`
- `probe_count`: `332`
- `solver_available`: `true`
- `base_compile_counts`: `{"executable": 38, "unsupported": 17}`
- `base_solver_counts`: `{"sat": 38, "not_run": 17}`
- `bounded_base_compile_counts`: `{"not_run": 55}`
- `bounded_base_solver_counts`: `{"not_run": 55}`
- `probe_compile_counts`: `{"executable": 172, "unsupported": 160}`
- `probe_solver_counts`: `{"sat": 172, "not_applicable_unsupported": 160}`
- `bounded_probe_compile_counts`: `{"not_run": 332}`
- `bounded_probe_solver_counts`: `{"not_run": 332}`
- `hard_findings`: `0`
- `soft_findings`: `0`
- `advisory_findings`: `332`

## Fixture

- `fixture_id`: `fixture_rebalance_day_non_trading_third_friday`
- `solver_status`: `sat`
- `observed_statuses`: `['sat', 'unsat']`
- `passed`: `True`

## Entry Table

| Entry | Probes | Executable | Unsupported | SAT | UNSAT | UNKNOWN | Timeout | Bounded SAT | Bounded UNSAT | Bounded Timeout |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `section_1_1` | 3 | 3 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 |
| `section_1_2` | 7 | 0 | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `section_1_3` | 5 | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `section_1_4` | 24 | 24 | 0 | 24 | 0 | 0 | 0 | 0 | 0 | 0 |
| `section_1_5` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `section_2_1` | 29 | 0 | 29 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `section_2_2` | 24 | 0 | 24 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `section_2_3` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `section_3_1` | 8 | 0 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `section_3_2` | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| `section_4_1` | 7 | 0 | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `section_4_2` | 4 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `section_4_3` | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| `section_4_4` | 12 | 0 | 12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `section_4_5` | 18 | 18 | 0 | 18 | 0 | 0 | 0 | 0 | 0 | 0 |
| `section_4_6` | 6 | 6 | 0 | 6 | 0 | 0 | 0 | 0 | 0 | 0 |
| `section_4_7` | 17 | 17 | 0 | 17 | 0 | 0 | 0 | 0 | 0 | 0 |
| `section_5_1` | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| `section_5_2` | 7 | 0 | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `section_5_3` | 13 | 13 | 0 | 13 | 0 | 0 | 0 | 0 | 0 | 0 |
| `section_5_4` | 33 | 0 | 33 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `section_5_5` | 8 | 0 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `N01` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `N02` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `N03` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `N04` | 7 | 0 | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `N05` | 7 | 0 | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `N06` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `N07` | 3 | 3 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 |
| `N08` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `N09` | 2 | 2 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `N10` | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| `N11` | 2 | 2 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `N12` | 2 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `N13` | 2 | 2 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `N14` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `N15` | 2 | 2 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `N16` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `N17` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `N18` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `N19` | 2 | 2 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `N20` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `N21` | 3 | 3 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 |
| `N22` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `N23` | 2 | 2 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| `N24` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `N25` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `N26` | 13 | 13 | 0 | 13 | 0 | 0 | 0 | 0 | 0 | 0 |
| `N27` | 3 | 3 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 |
| `N28` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `N29` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `N30` | 49 | 49 | 0 | 49 | 0 | 0 | 0 | 0 | 0 | 0 |
| `N31` | 4 | 4 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 |
| `N32` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| `appendix_8_1` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## Interpretation

Executable probes have an SMT-LIB sidecar file. Unsupported probes are kept as explicit candidates for later compiler expansion. In `hybrid` mode, full SMT is attempted first and bounded-witness SMT is used only when full SMT times out or returns an unresolved status. Bounded witness results are smoke checks, not replacements for full first-order proofs.
