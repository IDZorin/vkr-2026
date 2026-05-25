# Section 2.3 Translator Notes

This file records translator decisions for the current `main_ir.a4v3`.
It is review memory, not an additional source of methodology claims.

## Changelog

### 2026-05-08T10:46:30+02:00

Decision: mark descriptive basis/procedure statements as `fact`, not `constraint`.

Accepted:

- `weight_based_on_float_market_capizatlization` is now a fact because it records the source's basis/provenance relation between the final `weight(d, c)` value and `float_market_capizatlization(d, c)`, but does not provide a calculable formula.
- `weight_redistribution_process_is_iterative` is now a fact because the source describes the redistribution procedure as iterative, but does not give a checkable numeric/temporal transition rule.
- `weights_redistributed_proportionally` is now a fact because the source says redistribution is proportional, but does not provide the exact proportional redistribution formula.
- The hard constraints remain only the two explicit terminal requirements: each region represents exactly `50%` of the total Index, and each component weight is capped at `5%`.

Rejected / alternatives:

- Do not encode basis/procedural statements as hard `constraint` declarations. They are descriptive/provenance/procedural claims, not admissibility conditions like `weight(d, c) <= 5%`.
- Do not introduce a synthetic `constraints_satisfied` or full fixed-point transition system only to cover `until both constraints are satisfied`.

Rationale: the terminal condition of the iterative process is represented by the two explicit numeric constraints. The exact weight formula, iteration trace, fixed-point/stopping predicate, and proportional redistribution formula remain intentionally outside the local static IR because the source does not specify them.

Validation expectation: semantic lint should not report fact-like universal constraints for these descriptive basis/procedure claims after this change.

### 2026-05-08T10:05:17+02:00

Decision: strengthen the local 2.3 IR so that semantic dependencies live in formula bodies, not only in names.

Accepted:

- `weight(d, c)` now returns `Percent`, because the source constraints compare and aggregate weights as percentage values (`50%`, `5%`).
- The Float Market Capizatlization basis is represented by a formula body linking both terms: `weight(d, c)` and `float_market_capizatlization(d, c)`.
- Proportional redistribution is represented as a weak process/result relation over the resulting `weight(d, c)`, via `weight_redistribution_process(d)` and `redistributes_weight_proportionally(...)`.
- The source typo `Float Market Capizatlization` is intentionally preserved in local symbols for source-token provenance.

Rejected / alternatives:

- Do not keep label-only constraints such as `forall d,c, based_on_float_market_capizatlization(d,c)`; they cover words but do not encode the dependency.
- Do not keep opaque `sort Weight` while using `weight(...)` in numeric comparison and `sum(...)`.
- Do not introduce a full iterative transition system for `until both constraints are satisfied`; that would require process states, iteration steps, and a stopping condition beyond this local static IR.

Rationale: the two numeric constraints remain exact, and the basis relation now explicitly connects the final percentage weight to the Float Market Capizatlization term. The redistribution sentence remains weaker than a full algorithmic model, but it is no longer a pure name-only assertion: it is tied to a per-Selection-Day redistribution process and the resulting component weights.

Waiver rationale:

- `assigned` remains absorbed by the resulting `weight(...)` function.
- `subject`, `following`, and `constraints` remain list/framing words for the two following constraints.
- `total` remains absorbed by the normalized regional weight sum.
- `until`, `both`, and `satisfied` remain absorbed by the two explicit target constraints and are not modeled as a separate temporal stopping predicate.

Validation:

- clean gate: accepted
- A4V3 semantic lint: 0 findings
- phrase coverage: 4/4
- token accounted coverage: 28/28
- waivers: 8/8

### 2026-05-06T17:27:25+02:00

Decision: represent weighting as value constraints plus a deliberately weak/local representation of proportional redistribution.

Accepted:

- Weight is modeled as `weight(d, c)` over `SelectionDay` and `IndexComponent`.
- Float Market Capizatlization basis is represented by `based_on_float_market_capizatlization(d, c)`.
- The regional 50% requirement is represented as `sum(c in IndexComponent where region(c) = r, weight(d, c)) = 50%`.
- The single-component cap is represented as `weight(d, c) <= 5%`.
- Proportional redistribution is represented by `redistributed_proportionally(d, c)`.

Rejected / alternatives:

- Do not model the full iterative process/trace in this manual local IR. A full representation would require first-class process state, iteration steps, and a stopping condition.
- Do not add a helper `constraints_satisfied` relation only to cover `until both constraints are satisfied`; the two target constraints themselves are present as top-level formulas.
- Do not treat `until` as a TemporalDecl in this local gold version, because the IR does not introduce a temporal transition system.

Rationale: the source has two exact numeric constraints and one procedural sentence. The numeric constraints are represented exactly. The procedural redistribution wording is preserved as a proportional redistribution predicate, while the detailed iteration/until semantics is documented as intentionally absorbed/weak.

Waiver rationale:

- `assigned` is absorbed by the resulting `weight(...)` function.
- `subject`, `following`, and `constraints` are list/framing words for the following constraints.
- `total` is absorbed by the normalized regional weight sum.
- `iterative`, `process`, `until`, `both`, and `satisfied` are absorbed by the minimal redistribution representation plus the two final constraints; they are not modeled as a full process trace.

Validation:

- clean gate: accepted
- phrase coverage: 4/4
- token accounted coverage: 28/28
- waivers: 10/10

Research note: this section was later used for frame/roundtrip experiments. The experiment showed that frame alignment can help diagnose loss of numbers, comparators, scope, and role direction, but the manual financial methodology acceptance here remains based on explicit IR review plus clean checks.
