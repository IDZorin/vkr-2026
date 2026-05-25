# Section 5.4 Translator Notes

This file records translator decisions for the current `main_ir.a4v3`.
It is review memory, not an additional source of methodology claims.

## Changelog

### 2026-05-09T10:44:10+02:00

Decision: keep the explicit selection-criteria cessation trigger as traceability duplication.

Accepted:

- `cessation_usual_when_selection_criteria_not_applied_coherently` remains in the IR even though it is logically entailed by `cessation_usual_when_rules_not_applied_coherently`.
- The duplication is intentional because the source says the index rules, and particularly the selection criteria, may no longer be applied coherently. The separate constraint makes that source emphasis visible to reviewers and downstream render-back/judge tooling.

Rejected / alternatives:

- Do not treat this as a new independent semantic condition. Since `SelectionCriteria extends IndexRule`, it is a specialized traceability clause, not additional logic beyond the broader `IndexRule` cessation trigger.
- Do not remove it solely for logical minimality while the current gold objective is auditable source-to-IR coverage. If a future backend requires a logically minimal theory, this clause may be collapsed into the broader rule with a comment/provenance annotation.

Rationale: this follows the IR checklist principle that important source links should stay auditable. Here the cost is benign logical redundancy; the benefit is preserving the source's explicit "particularly the selection criteria" emphasis without changing the accepted 5.4 semantics.

### 2026-05-08T15:34:53+02:00

Decision: weaken 5.4 procedural/modality claims that were stronger than the source.

Accepted:

- `may be indicated` is no longer modeled as a hard existence constraint for an indicated cessation. The IR now derives `orderly_cessation_indication_available(i)` under the no-options/usual-case condition, while the deontic `permission indicate_orderly_cessation(...)` preserves the optional/modal character.
- Stakeholder wording is represented as guideline procedures for informing and consulting stakeholders, not as a universal assertion that every `Stakeholder` is actually informed and consulted.
- Termination and transition procedure content is represented as `fact`, because it states what the guidelines contain rather than imposing an admissibility constraint.

Rejected / alternatives:

- Do not encode `may be indicated` as `exists c: Cessation, ... indicated(c)`; that turns a permitted/possible indication into a guaranteed outcome.
- Do not use `forall s: Stakeholder, guidelines_inform(..., s) and guidelines_consult(..., s)`; the source says the guidelines explain how stakeholders are to be informed and consulted, not that every possible stakeholder is already covered as an event/result.
- Do not leave procedure-content existential claims as `constraint`; they are descriptive facts about the established guidelines.

Rationale: this keeps the accepted 5.4 policy structure, but avoids over-strengthening source modality and guideline procedure content. The source gives governance/procedure descriptions, not a deterministic execution trace.

### 2026-05-09T00:00:00+02:00

Decision: make the shared stakeholder target structural rather than lexical.

Accepted:

- Stakeholder information/consultation procedures now use a shared carrier `Stakeholders : Stakeholder`.
- `procedure_for_informing(p, Stakeholders)` and `procedure_for_consulting(q, Stakeholders)` replace the previous unary predicates `procedure_for_informing_stakeholders(p)` and `procedure_for_consulting_stakeholders(q)`.

Rejected / alternatives:

- Do not keep `stakeholders` only as a repeated token in predicate names; repeated content tokens should become formula structure when they identify a shared target.
- Do not return to `forall s: Stakeholder, ...`; the source describes guideline procedure content, not actual information/consultation events for every stakeholder.

Rationale: this preserves the weaker procedural interpretation while making the common stakeholder audience recoverable from the formula body.

### 2026-05-08T12:19:13+02:00

Decision: resolve the remaining semantic-lint soft findings without dropping source emphasis.

Accepted:

- `SelectionCriteria` is kept and now appears in a formula body through `cessation_usual_when_selection_criteria_not_applied_coherently`, because the source says index rules, and particularly the selection criteria, may no longer be applied coherently.
- `guidelines_inform_and_consult_stakeholders` is now a `fact`, because it describes procedural content of the guidelines rather than a hard admissibility constraint.

Rejected / alternatives:

- Do not delete `SelectionCriteria` merely to silence an unused-declaration warning; that would lose the source's explicit “particularly the selection criteria” emphasis.
- Do not keep stakeholder information/consultation as a `constraint`; this is policy/procedure content of the guidelines, not a numeric or logical eligibility condition.

Rationale: the substantive fallback constraints remain the usual-case cessation triggers. This change improves traceability and A4V3 family choice while preserving the previously accepted 5.4 interpretation.

### 2026-05-06T17:27:25+02:00

Decision: represent section 5.4 as resilience/adaptation governance plus fallback cessation conditions and Termination Policy provenance.

Accepted:

- Solactive's `greatest possible efforts` are represented as an `Effort` object with `effort_by`, `greatest_possible`, and `over_time`.
- Resilience and continued integrity are represented as `IndexQuality` targets of the effort.
- Necessary methodology adaptation is represented as a procedure followed by Solactive, with `clearly_defined`, `transparent`, `adapts_index_methodology`, and maintenance of continued reliability/comparability.
- The Section 5.2 Methodology Review reference is preserved as a document-part locator.
- Cessation is represented as a fallback when no options are available and usual-case conditions hold.
- The main usual-case families are separated: substantial unforeseeable market change, substantial unforeseeable economic reality change, rules not applicable coherently, and no longer used as underlying value.
- `SelectionCriteria extends IndexRule` preserves the source emphasis that selection criteria are part of index rules.
- Indication of orderly cessation is represented as a `permission`, not a mandatory action.
- Guidelines are represented as established/maintained/clear, identifying unavoidable cessation situations, informing and consulting stakeholders, and containing termination/transition procedures.
- The Termination Policy URL is preserved exactly and linked through `document_url`, `available_on`, and `website_of`.

Rejected / alternatives:

- Do not trigger `ActionDecl` merely from the phrase `transition to`; the source lists procedure content, not a concrete state transition here.
- Do not treat `may be indicated` as an immediate hard outcome. It is represented as permitted indication plus a conditional cessation formula.
- Do not encode `Nevertheless` as a separate SHACL step or domain object; it is a discourse contrast marker between adaptation and fallback cessation.
- Do not over-formalize `substantially` into a numeric threshold; it remains a `VagueTerm`.
- Do not use frame alignment as the gold acceptance gate; the semantic-frame experiments around this section were diagnostic and unstable.

Rationale: section 5.4 is policy/procedure prose. The chosen IR keeps the difference between efforts, procedures, fallback cessation conditions, stakeholder process, and policy incorporation visible without turning every procedural word into an action transition.

Waiver rationale:

- `makes`, `in order to`, `Nevertheless`, `other`, `indicated`, `way`, `particularly`, `can`, `longer`, and `how` are absorbed by explicit effort/procedure/negation/guideline structures.
- `indicated` is not represented as a hard outcome because the source says `may be indicated`; the optional indication is represented through `permission indicate_orderly_cessation(...)` and `orderly_cessation_indication_available(i)`.
- The fallback relation is visible through `count(o in Option where available_option_for_index(o, i)) = 0` and `usual_case_for_cessation(i)`.

Validation:

- clean gate: accepted
- phrase coverage: 6/7, waiver-adjusted 7/7
- token accounted coverage: 92/92
- exact URLs: 1/1
- waivers: 10/10

Research note: this section was compared across seed methodology/manual, unified, and semantic experiment outputs. Manual seed methodology remained preferred because it preserved more explicit governance structure and passed clean checks; unified was more compact but too sketch-like; semantic generated versions were useful diagnostics but not gold.
