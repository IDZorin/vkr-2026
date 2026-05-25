# Section 5.2 Translator Notes

## Changelog

### 2026-05-10T13:45:00+02:00

Decision: model "regular review, at least annually" as both an existential source claim and a section-local universal constraint over reviews of `TheIndexMethodology`.

Rationale: the source says the methodology is subject to regular review at least annually, and the next sentence refers to a need identified "within such review". The IR therefore keeps one witness that such a review exists and also treats reviews of this methodology in this section as regular and at least annual. This avoids making regularity a consequence of identifying a change need.

### 2026-05-10T13:45:00+02:00

Decision: represent the parenthetical "e.g. ... i.e. ..." as a flat `MethodologyChangeNeedExampleCondition` catalog.

Rationale: the parenthetical is explanatory, not a hard rule that every need must simultaneously have all listed properties. The IR preserves the named conditions from the source while avoiding a conjunctive bundle that would over-strengthen the methodology.

### 2026-05-10T13:45:00+02:00

Decision: use `incorporated_by_reference_into(SolactiveMethodologyPolicy, Guideline)` instead of a unary incorporated-by-reference flag.

Rationale: the source says the Solactive Methodology Policy is incorporated by reference in this Guideline. The binary relation keeps the target document explicit.

### 2026-05-10T13:45:00+02:00

Decision: use `change_of_methodology(change, methodology)` as a relation, not a required total function.

Rationale: this section only needs to connect review-identified changes to the current methodology. A total function over all `MethodologyChange` values would create unnecessary cross-section commitments.

### 2026-05-10T14:10:00+02:00

Decision: represent "the present methodology is based on obsolete assumptions and factors" with one explicit relation, `methodology_has_obsolete_basis(methodology, condition)`.

Rationale: earlier financial methodology sections treat real "based on" dependencies as formula-body links, not waivers. The relation is used only for `ObsoleteAssumption` and `ObsoleteFactor`, so it preserves the source wording without turning the whole e.g./i.e. parenthetical into a hard conjunctive rule for every methodology-change need.

### 2026-05-10T18:55:00+02:00

Decision: keep `NoLongerReflectsReality` as the source-facing example-condition enum value, but add a positive carrier relation for contradiction detection:

```a4v3
rel reflects_reality_as_before :
  IndexMethodology, ReflectionQuality

constraint no_longer_reflects_reality_condition_means_not_reflects_reality_as_before :
  forall q: ReflectionQuality,
    example_condition_reflection_quality(NoLongerReflectsReality, q)
    implies not reflects_reality_as_before(TheIndexMethodology, q)
```

Rationale: the source phrase contains explicit negative polarity ("no longer reflects"). Encoding that only in the enum value would make later contradiction detection depend on parsing an identifier. The positive carrier exposes a conflict point for a future claim that the methodology still reflects reality as before.
