# Semantic Claim Alignment: N11

This ledger maps source claims to candidate IR blocks. It is a review surface, not a proof.

## Summary

- claim_count: `1`
- strong_candidate_count: `1`
- partial_candidate_count: `0`
- weak_or_missing_candidate_count: `0`
- reviewed_count: `0`
- approved_count: `0`
- needs_revision_count: `0`
- average_top3_token_coverage: `1.0`
- all_claims_review_approved: `False`

## Review Status Values

- `approved`: source claim is faithfully represented by the approved IR block(s).
- `needs_ir_revision`: source claim is missing, distorted, or only present in names.
- `source_ambiguous`: source itself needs interpretation before judging IR.
- `not_formalized_by_design`: claim is intentionally left as metadata/waiver/support text.

## Claims

### C01 `strong_candidate`

> "Fixing Day" is Selection Day.

- top3 token coverage: `1.0`
- review status: `unreviewed`
- uncovered by top3: none

Candidate IR blocks:
- `assertion:constraint:fixing_day_definition` line `4` score `0.873`, recall `1.0`
  `constraint fixing_day_definition : forall d: Day, fixing_day(d) iff selection_day(d)`
- `declaration:rel:fixing_day` line `1` score `0.653`, recall `0.667`
  `rel fixing_day : Day`
- `declaration:rel:selection_day` line `2` score `0.633`, recall `0.667`
  `rel selection_day : Day`
