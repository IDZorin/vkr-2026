# Section 3.2 Translator Notes

This file records translator decisions for the current `main_ir.a4v3`.
It is review memory, not an additional source of methodology claims.

## Changelog

### 2026-05-11T09:05:00+02:00

Decision: translate "The Index is not rebalanced extraordinarily" as an explicit negative constraint over a positive rebalance relation.

Accepted:

- `not` is represented in the formula body: `not rebalance_of_index(r, TheIndex)`.
- `ExtraordinaryRebalance` is a subtype of `Rebalance`, grounding the source adverb "extraordinarily" without creating a negative symbol name.
- The claim is modeled as a hard absence constraint, not as a `prohibition`, because the source is descriptive/passive and does not specify an agent or normative rule-maker.

Rejected / alternatives:

- Do not encode the whole sentence as `rel no_extraordinary_rebalance : Index`; that would hide the negation in a symbol name and make contradiction detection weaker.
- Do not assert an existential rebalance event; the source says no extraordinary rebalance exists for the Index.

Validation:

- Deterministic checks: `clean_gate=accepted`, semantic lint `0`, token coverage `1.0`, phrase coverage `1.0`.
- LLM checks: single semantic judge `corresponds`; ordinary multi judge `corresponds`; corpus-aware multi judge `corresponds`.
