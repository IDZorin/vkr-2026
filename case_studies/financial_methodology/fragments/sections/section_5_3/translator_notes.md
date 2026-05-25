# Section 5.3 Translator Notes

This file records the translation decisions behind the current `main_ir.a4v3`.
It is an audit note, not an additional source of methodology claims.

## Changelog

### 2026-05-10T12:56:00+02:00

Decision: use Copy 2 as the base and incorporate the stronger VagueTerm pattern from Copy 3.

Accepted:

- `apply_described_method` is represented as an obligation because the source says the Index Administrator `shall apply` the method.
- The possible change reasons are represented as `ChangeReason` enum values linked to `potentially_requires_change_to_method`, not as actual mandatory changes.
- The qualitative terms `obvious`, `demonstrable`, `necessary`, and `desirable` are represented by `VagueTerm` entities.
- `DeemedModificationOrChange` is constrained to be a change that is deemed both necessary and desirable and that serves one of the source-listed purposes.
- `not obliged to provide information` is represented as permission to withhold information about the modification or change, with an explicit bridge to `not provide_information`.
- `will take the appropriate steps` is represented as an obligation, not as a hard invariant.

Rejected / alternatives:

- Do not use Copy 1 as the base because it lacks an explicit obligation for `shall apply` and uses complex boolean expressions in deontic `scope`.
- Do not use Copy 3 as the base because it is too compressed and omits some source alternatives such as `remedy` and `supplement`.
- Do not encode the final consistency clause as a hard constraint. That would make failure logically impossible, while the legal text is better treated as a procedural duty.

Rationale: the selected shape keeps the legal/deontic force visible while avoiding double-coding a duty as both a permission/obligation and a hard logical fact.

## Source Claims

- The application by the Index Administrator of the described method is final and binding.
- The Index Administrator shall apply the described method for the composition and calculation of the Index.
- Market environment, supervisory, legal, financial, or tax reasons may require changes to the method.
- The Index Administrator may make changes to the Index terms and conditions or calculation method if it deems those changes necessary and desirable for the listed correction/prevention purposes.
- The Index Administrator is not obliged to provide information about such modifications or changes.
- Despite modifications and changes, the Index Administrator will take appropriate steps to ensure that the applied calculation method remains consistent with the described method.

## Current Chosen Shape

- `DescribedMethod` is the method described in the Guideline and above in the document.
- `MethodPurpose = Composition | Calculation` captures the two purposes for which the method must be applied.
- `potentially_requires_change_to_method` captures the possibility that a reason may require a change without asserting that a change actually occurs.
- `DeemedModificationOrChange` captures the subset of changes that the Index Administrator may make under the source-listed conditions.
- `AppropriateSteps` is the deontic target of the final consistency obligation.

## Decisions And Rationale

### 1. Possible Reasons Are Not Actual Changes

The source says it cannot be excluded that five reason classes may require changes. The IR therefore records each listed reason as a possible reason that may require a change to the method:

```a4v3
fact potential_method_change_reasons :
  potentially_requires_change_to_method(MarketEnvironment, DescribedMethod)
  and potentially_requires_change_to_method(SupervisoryReason, DescribedMethod)
  and potentially_requires_change_to_method(LegalReason, DescribedMethod)
  and potentially_requires_change_to_method(FinancialReason, DescribedMethod)
  and potentially_requires_change_to_method(TaxReason, DescribedMethod)
```

This does not assert that any actual change is made.

### 2. Qualitative Terms Are VagueTerm Anchors

The source terms `obvious`, `demonstrable`, `necessary`, and `desirable` are qualitative legal terms rather than computable predicates. They are represented as `VagueTerm` entities and connected structurally through formula bodies:

```a4v3
deemed_by(ch, TheIndexAdministrator, Necessary)
and deemed_by(ch, TheIndexAdministrator, Desirable)
...
error_described_by(e, Obvious) or error_described_by(e, Demonstrable)
```

This avoids hiding those qualifiers only inside predicate names.

### 3. No-Information Clause Is Deontic

The source says the Index Administrator is not obliged to provide information on such modifications or changes. A4V3 has no separate first-class "absence of obligation" field in this local style, so the clause is represented as permission to withhold information:

```a4v3
permission withhold_information_on_modification_or_change(...)
```

This is a deontic approximation, not an assertion that information must be withheld.

To keep the polarity machine-visible for later contradiction checks, the positive carrier is also exposed:

```a4v3
rel provide_information_on_modification_or_change :
  IndexAdministrator, ModificationOrChange, Information
rel information_withheld_on_modification_or_change :
  IndexAdministrator, ModificationOrChange, Information

constraint information_withheld_means_information_not_provided :
  forall a: IndexAdministrator, forall ch: ModificationOrChange,
    information_withheld_on_modification_or_change(a, ch, ModificationOrChangeInformation)
    iff not provide_information_on_modification_or_change(a, ch, ModificationOrChangeInformation)
```

### 4. Final Consistency Clause Is An Obligation

The source says the Index Administrator `will take the appropriate steps` to ensure a consistent calculation method despite changes. This is represented as an obligation:

```a4v3
obligation take_appropriate_steps_for_consistent_calculation_method(...)
```

The target `AppropriateSteps` is linked to the applied calculation method and the described method by:

```a4v3
step_ensures_consistency_with(
  AppropriateSteps,
  calculation_method_applied(TheIndex),
  DescribedMethod
)
```

This keeps the duty deontic while still exposing the consistency target in formula-bearing IR.

## Waiver Decisions

Current human-approved token waivers:

- `however`: discourse marker introducing the change-reasons clause; no standalone IR predicate is needed.
- `cannot` / `excluded`: represented by `potentially_requires_change_to_method`; no separate `not_excluded` relation is introduced.
- `made`: represented by `ModificationOrChange` and the permission `make_deemed_modification_or_change`.
- `order`: absorbed as purpose structure in `deemed_modification_or_change_scope`.
- `obliged`: represented by the deontic permission/no-obligation pattern `withhold_information_on_modification_or_change`, plus the explicit bridge to `not provide_information_on_modification_or_change`.
- `such`: anaphoric surface marker referring to modifications or changes already represented by `ModificationOrChange`.
- `despite`: represented by the `change: ModificationOrChange` parameter of the final consistency obligation.
- `will`: legal/modal future represented by the obligation `take_appropriate_steps_for_consistent_calculation_method`.

These waivers are token-provenance decisions, not semantic omissions.
