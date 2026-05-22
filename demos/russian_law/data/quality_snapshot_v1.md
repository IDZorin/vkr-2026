# Quality Snapshot: data

- clean_gate: `needs_review`
- blocking_conditions: `invalid_ast_or_combined_validation, missing_required_artifacts`
- ast_valid / combined_validation_ok: `None` / `None`
- effective grounding counts: symbols `None`, sorts `None`, callees `None`
- raw legacy grounding counts: symbols `None`, sorts `None`, refs `None`, callees `None`, origin `None`
- required/advisory family gaps: `0` / `0`
- source phrase coverage: `1/1` (`1.0`)
- source phrase waiver-adjusted coverage: `1/1` (`1.0`)
- token direct coverage: `15/26` (`0.577`)
- token waiver-accounted coverage: `26/26` (`1.0`)
- human-approved token waivers: `11/11`
- exact URL preservation: `2/2` (`1.0`)
- lowering smells: `0`
- a4v3 semantic lint findings: `22` (strong `0`, soft `22`, style `0`, advisory `0`)
- provenance lint findings: `0` (strong `0`, soft `0`, advisory `0`)
- artifact consistency: `missing_required_artifacts` (required stale `0`, required missing `3`, advisory stale `0`)
- raw diagnostic gate/fails/warnings: `None` / `0` / `None`
- blocking diagnostic fails after clean categorization: `0`

## Nonblocking Raw Alarms

- waiver-adjusted legacy lexical fails: `0`
- render-NLI advisory fails: `0`
- source-normalization NLI advisory fails: `0`
