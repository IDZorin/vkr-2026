# Semantic Claim Alignment: section_2_3

This ledger maps source claims to candidate IR blocks. It is a review surface, not a proof.

## Summary

- claim_count: `4`
- strong_candidate_count: `2`
- partial_candidate_count: `1`
- weak_or_missing_candidate_count: `1`
- reviewed_count: `0`
- approved_count: `0`
- needs_revision_count: `0`
- average_top3_token_coverage: `0.711`
- all_claims_review_approved: `False`

## Review Status Values

- `approved`: source claim is faithfully represented by the approved IR block(s).
- `needs_ir_revision`: source claim is missing, distorted, or only present in names.
- `source_ambiguous`: source itself needs interpretation before judging IR.
- `not_formalized_by_design`: claim is intentionally left as metadata/waiver/support text.

## Claims

### C01 `strong_candidate`

> ### 2.3 Weighting of the Index Components

- top3 token coverage: `1.0`
- review status: `unreviewed`
- uncovered by top3: none

Candidate IR blocks:
- `declaration:fun:weight` line `9` score `0.86`, recall `1.0`
  `fun[required] weight : SelectionDay, IndexComponent -> Weight`
- `assertion:constraint:single_index_component_weight_capped` line `22` score `0.838`, recall `1.0`
  `constraint single_index_component_weight_capped : forall d: SelectionDay, forall c: IndexComponent, weight(d, c) <= 5%`
- `assertion:constraint:weights_redistributed_proportionally` line `26` score `0.832`, recall `1.0`
  `constraint weights_redistributed_proportionally : forall d: SelectionDay, forall c: IndexComponent, redistributed_proportionally(d, c)`
- `assertion:constraint:weight_based_on_float_market_capizatlization` line `14` score `0.829`, recall `1.0`
  `constraint weight_based_on_float_market_capizatlization : forall d: SelectionDay, forall c: IndexComponent, based_on_float_market_capizatlization(d, c)`
- `assertion:constraint:region_represents_exactly_50_percent` line `18` score `0.827`, recall `1.0`
  `constraint region_represents_exactly_50_percent : forall d: SelectionDay, forall r: Region, sum(c in IndexComponent where region(c) = r, weight(d, c)) = 50%`

### C02 `partial_candidate`

> On each Selection Day, each Index Component is assigned a weight based on its Float Market Capizatlization subject to the following constraints:

- top3 token coverage: `0.692`
- review status: `unreviewed`
- uncovered by top3: `assign` (assigned), `subject` (subject), `follow` (following), `constraint` (constraints)

Candidate IR blocks:
- `assertion:constraint:weight_based_on_float_market_capizatlization` line `14` score `0.659`, recall `0.692`
  `constraint weight_based_on_float_market_capizatlization : forall d: SelectionDay, forall c: IndexComponent, based_on_float_market_capizatlization(d, c)`
- `declaration:rel:based_on_float_market_capizatlization` line `11` score `0.617`, recall `0.615`
  `rel based_on_float_market_capizatlization : SelectionDay, IndexComponent`
- `declaration:fun:float_market_capizatlization` line `8` score `0.525`, recall `0.538`
  `fun[required] float_market_capizatlization : SelectionDay, IndexComponent -> FloatMarketCapizatlization`
- `declaration:fun:weight` line `9` score `0.408`, recall `0.385`
  `fun[required] weight : SelectionDay, IndexComponent -> Weight`
- `assertion:constraint:single_index_component_weight_capped` line `22` score `0.37`, recall `0.385`
  `constraint single_index_component_weight_capped : forall d: SelectionDay, forall c: IndexComponent, weight(d, c) <= 5%`

### C03 `strong_candidate`

> - Each region must represent exactly 50% of the total Index
- The weight of any single Index Component is capped at 5%.

- top3 token coverage: `0.818`
- review status: `unreviewed`
- uncovered by top3: `must` (must), `total` (total)

Candidate IR blocks:
- `assertion:constraint:region_represents_exactly_50_percent` line `18` score `0.582`, recall `0.636`
  `constraint region_represents_exactly_50_percent : forall d: SelectionDay, forall r: Region, sum(c in IndexComponent where region(c) = r, weight(d, c)) = 50%`
- `assertion:constraint:single_index_component_weight_capped` line `22` score `0.439`, recall `0.455`
  `constraint single_index_component_weight_capped : forall d: SelectionDay, forall c: IndexComponent, weight(d, c) <= 5%`
- `declaration:fun:region` line `7` score `0.318`, recall `0.273`
  `fun[required] region : IndexComponent -> Region`
- `declaration:opaque:IndexComponent` line `2` score `0.279`, recall `0.182`
  `sort IndexComponent`
- `declaration:fun:weight` line `9` score `0.278`, recall `0.273`
  `fun[required] weight : SelectionDay, IndexComponent -> Weight`

### C04 `weak_or_missing_candidate`

> The weights are redistributed proportionally in an iterative process until both constraints are satisfied.

- top3 token coverage: `0.333`
- review status: `unreviewed`
- uncovered by top3: `iterative` (iterative), `proc` (process), `until` (until), `both` (both), `constraint` (constraints), `satisfi` (satisfied)

Candidate IR blocks:
- `assertion:constraint:weights_redistributed_proportionally` line `26` score `0.33`, recall `0.333`
  `constraint weights_redistributed_proportionally : forall d: SelectionDay, forall c: IndexComponent, redistributed_proportionally(d, c)`
- `declaration:opaque:Weight` line `4` score `0.289`, recall `0.111`
  `sort Weight`
- `declaration:rel:redistributed_proportionally` line `12` score `0.239`, recall `0.222`
  `rel redistributed_proportionally : SelectionDay, IndexComponent`
- `declaration:fun:weight` line `9` score `0.109`, recall `0.111`
  `fun[required] weight : SelectionDay, IndexComponent -> Weight`
- `assertion:constraint:single_index_component_weight_capped` line `22` score `0.101`, recall `0.111`
  `constraint single_index_component_weight_capped : forall d: SelectionDay, forall c: IndexComponent, weight(d, c) <= 5%`
