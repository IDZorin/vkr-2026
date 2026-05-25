# Section 4.5 Translator Notes

## Changelog

### 2026-05-10T17:36:12+02:00

- Final `main_ir.a4v3` was built as a hybrid: Copy 3 was used as the structural base, while important semantic details from Copy 2 were restored.
- The final IR keeps the corporate-action list open by using `CorporateActionKind` as an open sort and the twelve source-listed items as `ListedCorporateActionKind` entities.
- The final IR keeps `non_conclusive(RelevantCorporateActionList)` as an explicit source marker for "following, but not conclusive, list".
- The final IR uses deontic declarations for passive normative claims: `account_for_corporate_action_in_index_calculation` and `make_corporate_action_adjustment_in_compliance_with_equity_index_methodology`.
- The final IR uses a `permission` declaration for Solactive's retained right to deviate from standard procedures.

## Translation Decisions

### Will Consider

The source phrase "Solactive will consider various events" is represented as the relation `considers_for_index_maintenance(Solactive, ca, IndexMaintenanceOfTheIndex)`, not as a separate obligation.

Rationale: in this sentence, "will consider" primarily introduces the process scope for corporate actions handled during Index maintenance. Treating it as a standalone obligation would add a stronger deontic claim that the source does not clearly isolate.

### Non-Conclusive List

The source phrase "following, but not conclusive, list" is represented by `non_conclusive(RelevantCorporateActionList)`.

Rationale: the listed corporate-action kinds are guaranteed examples; the parent sort `CorporateActionKind` remains open so later or unlisted corporate-action kinds are not excluded.

The polarity is also made explicit:

```a4v3
constraint non_conclusive_means_not_conclusive :
  forall l: CorporateActionList,
    non_conclusive(l) iff not conclusive(l)
```

This keeps the source-facing predicate `non_conclusive` while giving contradiction checks a positive counterpart `conclusive` and an explicit `not`.

### Passive Obligations Without Agent

The obligations for "need to be accounted for" and "will be made in compliance" do not specify an explicit agent.

Rationale: both source clauses are passive. The IR preserves the obligation on the action/result without inventing an explicit responsible agent. Solactive remains explicit where the source explicitly says Solactive retains a right.

### Deviation Permission Scope

The permission `deviate_from_standard_procedures` uses `scope: EquityIndexMethodology`.

Rationale: the source says Solactive retains the right "in accordance with the Equity Index Methodology" to deviate from standard procedures. The scope field records that methodological context, while `corporate_action_deviation_conditions` records the concrete admissibility conditions for a permitted deviation.

### Deviation Conditions

`corporate_action_deviation_conditions` is a defining universal over `PermittedCorporateActionDeviation`.

Rationale: it defines what counts as a permitted deviation in this section. The condition preserves the source disjunction: unusual corporate action, complex corporate action, or a deviation made to preserve comparability and representativeness of the Index over time.

### Coincides With Price Effect

The source phrase "so that the adjustment to the Index coincides with the occurrence of the price effect" is represented by:

```a4v3
rel adjustment_coincides_with_price_effect_occurrence :
  CorporateActionAdjustment, PriceEffect
```

Rationale: this keeps the source-level claim "coincides with the occurrence of the price effect" explicit without reducing it to equality between two day-valued functions. Equality would be a stronger temporal commitment than the source requires.
