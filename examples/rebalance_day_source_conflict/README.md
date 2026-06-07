# Rebalance Day Source Conflict Example

This checked example shows how A4V3 can preserve a source-level conflict instead
of silently resolving it during translation.

The source fragment contains three claims:

- `REBALANCE DAY` is the third Friday in March, June, September, and December.
- If that scheduled day is not a trading day, the immediately following trading
  day is the `REBALANCE DAY`.
- For avoidance of doubt, the `REBALANCE DAY` is fixed and is not postponed when
  the scheduled day is not a trading day.

The local IR keeps the fallback clause and the no-postponement clarification as
separate constraints. The sidecar SMT witness demonstrates that, under a
scheduled-non-trading scenario, these two source clauses are jointly
inconsistent.

## Files

- `source.md` - compact source fragment.
- `normalized.md` - normalized source fragment used by deterministic checks.
- `main_ir.a4v3` - source-faithful A4V3 translation.
- `provenance.yaml` - claim-level grounding and back-translation.
- `translator_notes.md` - notes explaining conflict preservation and modeling
  choices.
- `source_conflict_witness_v1.smt2` - SMT witness for the contradiction.
- `source_conflict_witness_v1.out` - recorded solver result.
- `a4v3_semantic_lint_v1.*` - deterministic semantic-lint output.

This directory is a curated result artifact. It intentionally omits intermediate
drafts, chat history, and agent-run logs; it is not presented as a fully
autonomous one-shot LLM run.

## Check

From the repository root:

```bash
python tools/check_entry.py examples/rebalance_day_source_conflict
```

The recorded SMT witness result is:

```text
status: unsat
unsat_core: ['fallback_to_following_trading_day', 'fixed_date_no_postponement_claim', 'scheduled_non_trading_witness']
```
