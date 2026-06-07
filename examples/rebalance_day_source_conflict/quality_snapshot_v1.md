# Quality Snapshot: rebalance_day_source_conflict

- clean_gate: `needs_review`
- blocking_conditions: `invalid_ast_or_combined_validation, missing_required_artifacts`
- ast_valid / combined_validation_ok: `None` / `None`
- effective grounding counts: symbols `None`, sorts `None`, callees `None`
- raw legacy grounding counts: symbols `None`, sorts `None`, refs `None`, callees `None`, origin `None`
- required/advisory family gaps: `0` / `0`
- source phrase coverage: `6/6` (`1.0`)
- source phrase waiver-adjusted coverage: `6/6` (`1.0`)
- token direct coverage: `13/19` (`0.684`)
- token waiver-accounted coverage: `19/19` (`1.0`)
- human-approved token waivers: `6/6`
- exact URL preservation: `0/0` (`None`)
- lowering smells: `3`
- a4v3 semantic lint findings: `1` (strong `0`, soft `1`, style `0`, advisory `0`)
- provenance lint findings: `0` (strong `0`, soft `0`, advisory `0`)
- artifact consistency: `missing_required_artifacts` (required stale `0`, required missing `2`, advisory stale `0`)
- raw diagnostic gate/fails/warnings: `None` / `0` / `None`
- blocking diagnostic fails after clean categorization: `0`

## Nonblocking Raw Alarms

- waiver-adjusted legacy lexical fails: `0`
- render-NLI advisory fails: `0`
- source-normalization NLI advisory fails: `0`
