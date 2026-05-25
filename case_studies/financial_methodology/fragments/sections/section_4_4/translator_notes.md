# Section 4.4 Translator Notes

## Changelog

### 2026-05-11T16:58:00+02:00

- Built the final `main_ir.a4v3` as a synthesis of the three drafts: Copy 2 supplied the stronger event/day/notice structure, while Copy 3 supplied the correct deontic treatment for "will announce" and "will be made".
- Replaced deontic-as-constraint patterns with explicit obligations for making the required adjustment, making the adjustment in compliance with the Solactive Equity Index Methodology, and announcing the adjustment.
- Scoped those obligations to `RequiredIndexAdjustment`, a subtype of `IndexAdjustment`, so the deontic claims apply only to adjustments created by the source-described corporate-action trigger.
- Added provenance coverage for the final IR, including back-translations and vocabulary notes.

## Translation Decisions

### Possibility, Not Actual Necessity

The source phrase "may be necessary" is represented with an `IndexAdjustmentPossibility` carrier plus the vague-term markers `CertainCircumstances` and `MayBeNecessary`.

Rationale: the source states a possibility under certain circumstances; it does not assert that an adjustment is always necessary.

### Required Adjustment Trigger

The source phrase "Such adjustment has to be made if a corporate action ... occurs" is split into two pieces:

```a4v3
constraint corporate_action_creates_required_index_adjustment
obligation make_required_index_adjustment
```

Rationale: the constraint creates a required adjustment carrier when the corporate-action trigger holds, while the obligation keeps the normative force of "has to be made". This avoids silently turning a possible violation into a logical impossibility.

The required-adjustment carrier is represented as a subtype:

```a4v3
sort RequiredIndexAdjustment extends IndexAdjustment
```

This keeps the obligations anchored to the triggered adjustment class rather than to every possible `IndexAdjustment` in the model.

### Section 4.4 Below

The reference to "Section 4.4 below" is used as an antecedent condition:

```a4v3
specified_in(ca, Section4_4Below)
```

Rationale: this avoids a bare universal claim that every corporate action in the universe is specified in this section.

### Adjustment Effects

The phrase "in relation to an Index Component and/or ... affect the number ... and/or the weighting of certain Index Components" is represented as a disjunction over `IndexAdjustmentEffect`.

Rationale: the source gives possible effect scopes, not a claim that every adjustment has all three effects. The qualifier "certain Index Components" is preserved with a `VagueTerm` entity.

### Equity Index Methodology Reference

The Solactive Equity Index Methodology is modeled with a directed incorporation relation:

```a4v3
incorporated_by_reference_into(SolactiveEquityIndexMethodology, ThisGuideline)
```

Rationale: this follows the current financial methodology pattern used in later policy-reference sections and keeps the direction of incorporation auditable.

### Announcement Section

The Announcements section is represented as a `DocumentPart` of the Solactive website.

Rationale: the source says the notice appears on the Solactive website under the section "Announcements". It does not provide a concrete URL, so no URL entity is introduced.

### Notice Period

The notice period is represented as a `NoticePeriod` carrier with at least two component-specific `TradingDay` values before the notice's effective day.

Rationale: this keeps the "with respect to the affected Index Component" qualifier attached to the notice-period calculation, rather than treating Trading Days as global days.

Notice relations are scoped to `RequiredIndexAdjustment`, not the broader `IndexAdjustment` sort, because the source's phrase "the Index adjustment" refers back to the required adjustment introduced by the corporate-action trigger.

### Effective Day

The implementation date is modeled as an operational rule:

```a4v3
implemented_on(a, effective_day_specified_in_respective_notice(n))
```

Rationale: the source fixes implementation by reference to the respective notice. It is not represented as a separate obligation because the deontic force is already captured by the adjustment-making obligations.
