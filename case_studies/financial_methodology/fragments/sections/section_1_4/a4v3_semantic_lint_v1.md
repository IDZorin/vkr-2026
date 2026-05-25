# A4V3 Semantic Lint: section_1_4

- total_findings: `6`
- strong/soft/style/advisory: `0` / `6` / `0` / `0`
- unused rel/fun: `0`
- arity > 5 hard findings: `0`
- arity > 2 without role explanation: `6`
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
- contract classes: `{"role_contract": 6}`

## Findings

### `relation_or_function_arity_gt_2_without_role_explanation` / `most_recent_closing_price`

- severity: `soft`
- line: `41`
- reason: Relation/function arity is above 2. This is allowed for local IR, but roles must be clearly explained in translator_notes.md or provenance.yaml; otherwise prefer a carrier plus binary role relations.
- contract_class: `role_contract`
- raw: `fun[required] most_recent_closing_price : IndexComponent, CalculationDay, CalculationTime -> ClosingPrice`

### `relation_or_function_arity_gt_2_without_role_explanation` / `listed_on_exchanges`

- severity: `soft`
- line: `63`
- reason: Relation/function arity is above 2. This is allowed for local IR, but roles must be clearly explained in translator_notes.md or provenance.yaml; otherwise prefer a carrier plus binary role relations.
- contract_class: `role_contract`
- raw: `rel listed_on_exchanges : CalculationDay, IndexComponent, Exchange`

### `relation_or_function_arity_gt_2_without_role_explanation` / `intraday_level_calculated_on`

- severity: `soft`
- line: `65`
- reason: Relation/function arity is above 2. This is allowed for local IR, but roles must be clearly explained in translator_notes.md or provenance.yaml; otherwise prefer a carrier plus binary role relations.
- contract_class: `role_contract`
- raw: `rel intraday_level_calculated_on : IndexLevel, CalculationDay, CalculationTime`

### `relation_or_function_arity_gt_2_without_role_explanation` / `current_trading_price_available`

- severity: `soft`
- line: `68`
- reason: Relation/function arity is above 2. This is allowed for local IR, but roles must be clearly explained in translator_notes.md or provenance.yaml; otherwise prefer a carrier plus binary role relations.
- contract_class: `role_contract`
- raw: `rel current_trading_price_available : IndexComponent, CalculationDay, CalculationTime`

### `relation_or_function_arity_gt_2_without_role_explanation` / `converted_from_using`

- severity: `soft`
- line: `70`
- reason: Relation/function arity is above 2. This is allowed for local IR, but roles must be clearly explained in translator_notes.md or provenance.yaml; otherwise prefer a carrier plus binary role relations.
- contract_class: `role_contract`
- raw: `rel converted_from_using : Price, Price, ForeignExchangeRate`

### `relation_or_function_arity_gt_2_without_role_explanation` / `wm_fixing_4pm_london_available`

- severity: `soft`
- line: `72`
- reason: Relation/function arity is above 2. This is allowed for local IR, but roles must be clearly explained in translator_notes.md or provenance.yaml; otherwise prefer a carrier plus binary role relations.
- contract_class: `role_contract`
- raw: `rel wm_fixing_4pm_london_available : Currency, Currency, CalculationDay`
