# Quality Snapshot: data

- clean_gate: `needs_review`
- blocking_conditions: `invalid_ast_or_combined_validation, missing_required_artifacts`
- ast_valid / combined_validation_ok: `None` / `None`
- effective grounding counts: symbols `None`, sorts `None`, callees `None`
- raw legacy grounding counts: symbols `None`, sorts `None`, refs `None`, callees `None`, origin `None`
- required/advisory family gaps: `0` / `2`
- source phrase coverage: `31/31` (`1.0`)
- source phrase waiver-adjusted coverage: `31/31` (`1.0`)
- token direct coverage: `137/228` (`0.601`)
- token waiver-accounted coverage: `228/228` (`1.0`)
- human-approved token waivers: `91/91`
- exact URL preservation: `1/1` (`1.0`)
- lowering smells: `4`
- a4v3 semantic lint findings: `8` (strong `0`, soft `7`, style `0`, advisory `1`)
- provenance lint findings: `0` (strong `0`, soft `0`, advisory `0`)
- artifact consistency: `missing_required_artifacts` (required stale `0`, required missing `3`, advisory stale `0`)
- raw diagnostic gate/fails/warnings: `None` / `0` / `None`
- blocking diagnostic fails after clean categorization: `0`

## Nonblocking Raw Alarms

- waiver-adjusted legacy lexical fails: `0`
- render-NLI advisory fails: `0`
- source-normalization NLI advisory fails: `0`
