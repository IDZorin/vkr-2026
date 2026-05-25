# A4V3 Semantic Lint: N30

- total_findings: `5`
- strong/soft/style/advisory: `0` / `5` / `0` / `0`
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
- shared name tokens without structural carrier: `5`
- semantic contract gaps: `0` (strong `0`, repair candidates `0`)
- contract classes: `{"dependency_contract": 5}`

## Findings

### `shared_name_token_without_structural_carrier` / `open_for_trading_condition`

- severity: `soft`
- line: `98`
- reason: A non-generic semantic token is repeated across multiple predicate/function names in one claim, but the token has no structural carrier such as a sort, entity, signature argument, or formula-body argument. The relation may live only in names.
- contract_class: `dependency_contract`

### `shared_name_token_without_structural_carrier` / `market_disruption_counterfactual_condition`

- severity: `soft`
- line: `107`
- reason: A non-generic semantic token is repeated across multiple predicate/function names in one claim, but the token has no structural carrier such as a sort, entity, signature argument, or formula-body argument. The relation may live only in names.
- contract_class: `dependency_contract`

### `shared_name_token_without_structural_carrier` / `market_disruption_counterfactual_condition`

- severity: `soft`
- line: `107`
- reason: A non-generic semantic token is repeated across multiple predicate/function names in one claim, but the token has no structural carrier such as a sort, entity, signature argument, or formula-body argument. The relation may live only in names.
- contract_class: `dependency_contract`

### `shared_name_token_without_structural_carrier` / `trading_day_definition`

- severity: `soft`
- line: `138`
- reason: A non-generic semantic token is repeated across multiple predicate/function names in one claim, but the token has no structural carrier such as a sort, entity, signature argument, or formula-body argument. The relation may live only in names.
- contract_class: `dependency_contract`

### `shared_name_token_without_structural_carrier` / `trading_day_definition`

- severity: `soft`
- line: `138`
- reason: A non-generic semantic token is repeated across multiple predicate/function names in one claim, but the token has no structural carrier such as a sort, entity, signature argument, or formula-body argument. The relation may live only in names.
- contract_class: `dependency_contract`
