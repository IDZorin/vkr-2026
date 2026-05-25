# A4V3 Semantic Lint: section_2_1

- total_findings: `1`
- strong/soft/style/advisory: `0` / `1` / `0` / `0`
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
- contract classes: `{}`

## Findings

### `unused_declaration` / `AvoidFrequentChangesBetweenTwoShareClasses`

- severity: `soft`
- line: `158`
- reason: Declaration is not referenced by any assertion body, deontic field, or another declaration signature.
- raw: `entity AvoidFrequentChangesBetweenTwoShareClasses : VagueTerm`
