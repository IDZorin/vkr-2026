# A4V3 Semantic Lint: section_5_2

- total_findings: `2`
- strong/soft/style/advisory: `0` / `0` / `0` / `2`
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
- semantic contract gaps: `0` (strong `0`, repair candidates `0`)
- contract classes: `{"modality_contract": 2}`

## Findings

### `temporal_rel_in_deontic_context` / `example_condition_changed_since_launch_of_index`

- severity: `advisory`
- line: `51`
- reason: Temporal relation is used in assertion bodies while the file has deontic declarations; inspect whether temporal/deontic structure should be first-class instead.
- contract_class: `modality_contract`

### `temporal_rel_in_deontic_context` / `reflects_reality_as_before`

- severity: `advisory`
- line: `61`
- reason: Temporal relation is used in assertion bodies while the file has deontic declarations; inspect whether temporal/deontic structure should be first-class instead.
- contract_class: `modality_contract`
