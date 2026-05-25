# A4V3 Semantic Lint: section_4_4

- total_findings: `2`
- strong/soft/style/advisory: `0` / `2` / `0` / `0`
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
- contract classes: `{"dependency_contract": 2}`

## Findings

### `shared_name_token_without_structural_carrier` / `index_adjustment_notice_publication`

- severity: `soft`
- line: `142`
- reason: A non-generic semantic token is repeated across multiple predicate/function names in one claim, but the token has no structural carrier such as a sort, entity, signature argument, or formula-body argument. The relation may live only in names.
- contract_class: `dependency_contract`

### `shared_name_token_without_structural_carrier` / `notice_period_at_least_two_trading_days`

- severity: `soft`
- line: `151`
- reason: A non-generic semantic token is repeated across multiple predicate/function names in one claim, but the token has no structural carrier such as a sort, entity, signature argument, or formula-body argument. The relation may live only in names.
- contract_class: `dependency_contract`
