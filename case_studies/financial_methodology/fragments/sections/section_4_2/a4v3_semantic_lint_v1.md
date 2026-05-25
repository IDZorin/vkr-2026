# A4V3 Semantic Lint: section_4_2

- total_findings: `3`
- strong/soft/style/advisory: `0` / `2` / `0` / `1`
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
- shared name tokens without structural carrier: `2`
- semantic contract gaps: `0` (strong `0`, repair candidates `0`)
- contract classes: `{"modality_contract": 1, "dependency_contract": 2}`

## Findings

### `temporal_rel_in_deontic_context` / `after`

- severity: `advisory`
- line: `33`
- reason: Temporal relation is used in assertion bodies while the file has deontic declarations; inspect whether temporal/deontic structure should be first-class instead.
- contract_class: `modality_contract`

### `shared_name_token_without_structural_carrier` / `termination_and_announcement_at_zero_or_below`

- severity: `soft`
- line: `47`
- reason: A non-generic semantic token is repeated across multiple predicate/function names in one claim, but the token has no structural carrier such as a sort, entity, signature argument, or formula-body argument. The relation may live only in names.
- contract_class: `dependency_contract`

### `shared_name_token_without_structural_carrier` / `termination_and_announcement_at_zero_or_below`

- severity: `soft`
- line: `47`
- reason: A non-generic semantic token is repeated across multiple predicate/function names in one claim, but the token has no structural carrier such as a sort, entity, signature argument, or formula-body argument. The relation may live only in names.
- contract_class: `dependency_contract`
