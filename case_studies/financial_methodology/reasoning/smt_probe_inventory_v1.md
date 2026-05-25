# SMT Probe Inventory v1

This sidecar layer generates SMT probe/witness candidates from existing local
seed methodology `main_ir.a4v3` files. It does not modify local IR.

## Probe Types

- `non_vacuity_guard`: checks that an `implies` antecedent can be realized.
- `iff_lhs_witness`: checks that the left side of an `iff` can be realized.
- `iff_rhs_witness`: checks that the right side of an `iff` can be realized.
- `or_branch_witness`: checks that each explicit `or` branch can be realized.
- `existential_witness`: checks that explicit existential scenarios can be realized.
- `negative_condition_witness`: checks that explicit `not ...` conditions can be realized.

## SMT v1 Scope

The v1 compiler is intentionally shallow. It supports relational skeletons,
subtype predicates, quantifiers, Boolean connectives, equality, numeric
comparisons, arithmetic, relation calls, and function calls. Aggregates such as
`count` and `sum` are marked unsupported instead of guessed.

## SMT Modes

- `full`: emit and solve the direct first-order SMT lowering.
- `bounded-witness`: replace quantified variables with stable witness constants
  per variable-name/sort inside each generated SMT file. This is a fast
  vacuity/conflict smoke check and deliberately avoids unbounded `forall`.
- `hybrid`: run `full` first; if Z3 times out or returns an unresolved status,
  generate and run the bounded-witness fallback for that base/probe.

## Severity

UNSAT base theories are hard findings. UNSAT non-mandatory probes are soft
review signals. Unsupported probe candidates are advisory and document where
future SMT coverage can grow.
