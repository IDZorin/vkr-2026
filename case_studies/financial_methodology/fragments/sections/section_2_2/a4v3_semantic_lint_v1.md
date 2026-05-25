# A4V3 Semantic Lint: section_2_2

- total_findings: `1`
- strong/soft/style/advisory: `0` / `0` / `0` / `1`
- unused rel/fun: `0`
- arity > 5 hard findings: `0`
- arity > 2 without role explanation: `0`
- sentence-like literals in formula bodies: `0`
- permission source asserts concrete event instances: `0`
- unbound deontic role parameters: `0`
- deontic parameters typed by entities: `0`
- self-referential deontic scope: `0`
- possible double-coded deontic norms: `0`
- vacuous responsibility implications: `0`
- bare universal predicate constraints: `0`
- fact-like universal constraints: `0`
- numeric operations on non-numeric sorts: `0`
- based-on claims without value link: `0`
- shared name tokens without structural carrier: `0`
- semantic contract gaps: `1` (strong `0`, repair candidates `1`)
- contract classes: `{"cardinality_contract": 1}`

## Findings

### `semantic_contract_gap` / `selected_for_index_inclusion`

- severity: `advisory`
- line: `66`
- reason: The main IR selects by a rank cutoff, which relies on a hidden top-k/cardinality contract. Without a cardinality guard or rank uniqueness/tie-break contract, a backend can assign the same rank to many objects and still satisfy the rank cutoff.
- contract_class: `cardinality_contract`
- usage: `selected_for_index_inclusion(...) iff ... rank(...) <= 20`
- repair_status: `has_repair_candidate`
- repair_candidates: `at_most_20_selected_per_region`
- source_triggers:
  - The top 20 securities for each region are selected for Index inclusion.
