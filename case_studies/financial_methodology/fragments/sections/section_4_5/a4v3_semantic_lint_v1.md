# A4V3 Semantic Lint: section_4_5

- total_findings: `5`
- strong/soft/style/advisory: `0` / `5` / `0` / `0`
- unused rel/fun: `0`
- arity > 5 hard findings: `0`
- arity > 2 without role explanation: `5`
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
- contract classes: `{"role_contract": 5}`

## Findings

### `relation_or_function_arity_gt_2_without_role_explanation` / `adjustment_between_regular_rebalance_days`

- severity: `soft`
- line: `77`
- reason: Relation/function arity is above 2. This is allowed for local IR, but roles must be clearly explained in translator_notes.md or provenance.yaml; otherwise prefer a carrier plus binary role relations.
- contract_class: `role_contract`
- raw: `rel adjustment_between_regular_rebalance_days :`

### `relation_or_function_arity_gt_2_without_role_explanation` / `implemented_from_to`

- severity: `soft`
- line: `81`
- reason: Relation/function arity is above 2. This is allowed for local IR, but roles must be clearly explained in translator_notes.md or provenance.yaml; otherwise prefer a carrier plus binary role relations.
- contract_class: `role_contract`
- raw: `rel implemented_from_to :`

### `relation_or_function_arity_gt_2_without_role_explanation` / `methodology_contains_definition`

- severity: `soft`
- line: `91`
- reason: Relation/function arity is above 2. This is allowed for local IR, but roles must be clearly explained in translator_notes.md or provenance.yaml; otherwise prefer a carrier plus binary role relations.
- contract_class: `role_contract`
- raw: `rel methodology_contains_definition :`

### `relation_or_function_arity_gt_2_without_role_explanation` / `methodology_specifies_relevant_adjustment_to_index_variable`

- severity: `soft`
- line: `93`
- reason: Relation/function arity is above 2. This is allowed for local IR, but roles must be clearly explained in translator_notes.md or provenance.yaml; otherwise prefer a carrier plus binary role relations.
- contract_class: `role_contract`
- raw: `rel methodology_specifies_relevant_adjustment_to_index_variable :`

### `relation_or_function_arity_gt_2_without_role_explanation` / `considers_relevant_for_index_maintenance`

- severity: `soft`
- line: `119`
- reason: Relation/function arity is above 2. This is allowed for local IR, but roles must be clearly explained in translator_notes.md or provenance.yaml; otherwise prefer a carrier plus binary role relations.
- contract_class: `role_contract`
- raw: `rel considers_relevant_for_index_maintenance :`
