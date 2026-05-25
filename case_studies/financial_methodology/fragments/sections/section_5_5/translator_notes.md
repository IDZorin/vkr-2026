# Section 5.5 Translator Notes

This file records the translation decisions behind the current `main_ir.a4v3`.
It is not a source of additional methodology claims. It is an audit note for future review
sessions so that the same semantic tradeoffs do not need to be rediscovered.

## Changelog

### 2026-05-20T00:00:00+02:00

Decision: make approval and responsibility roles more direct.

Accepted:

- Replaced the existential concrete `Decision` witness with `responsible_for_decisions_regarding(OversightCommittee, amendment)`.
- Changed the submission obligation target from `OversightCommittee` to the amendment being submitted.
- Added `OversightCommitteePriorApproval` and `approval_by(OversightCommitteePriorApproval, OversightCommittee)` so the scope records that prior approval is by the Oversight Committee.
- Strengthened `may_result_in` from a bare scoped relation to a possible Guideline-amendment witness for each Index-rule amendment.

Rationale:

- The source says the committee is responsible for decisions regarding amendments, but it does not require one concrete Decision object to exist for every amendment.
- In the submission clause, the amendment is what is submitted; the committee is the destination/approval authority.
- The source phrase "which may result in an amendment of the Guideline" is a possible-result statement, not merely a typing condition on a relation if that relation happens to be present.

### 2026-05-06T20:28:24+02:00

Decision: remove the self-referential `scope: IndexRuleAmendment` from the compliance obligation.

Accepted:

- `make_index_rule_amendment_in_compliance_with_methodology_policy` keeps `amendment: IndexRuleAmendment` as the affected amendment parameter.
- `target: MethodologyPolicy` keeps the policy object.
- No `scope` field is used for this obligation because repeating `IndexRuleAmendment` as scope adds no context.

Rejected / alternatives:

- Do not use `scope: IndexRuleAmendment`; it duplicates the parameter sort.
- Do not use `scope: MethodologyPolicy`; it would duplicate the target.

Rationale: in A4V3 deontic style, `scope` should add contextual framing, as in `scope: Cessation` or `scope: PriorApproval`. If the parameter and target already identify the duty, an empty/absent scope is cleaner than a self-reference.

### 2026-05-06T17:39:59+02:00

Decision: make both submission and compliance deontic obligations, and restore action-style obligation naming.

Accepted:

- The submission obligation is named `submit_index_rule_amendment_for_prior_approval`, not `submitted_...`.
- `submitted` is not encoded by making the obligation name past-participial; if token provenance needs it, it is handled as a reviewed morphology/action waiver.
- `will be made in compliance with the Methodology Policy` is represented as a second `DeonticDecl.obligation`.
- The hard `constraint index_rule_amendment_compliance` and `rel made_in_compliance_with` are removed.

Rejected / alternatives:

- Do not use `submitted_index_rule...` just to satisfy token coverage, because it reads like an already-completed submission rather than a duty to submit.
- Do not represent compliance as a hard invariant while submission is deontic; that split invited unnecessary disagreement about legal force.

Rationale: A4V3 deontic examples use action-style names such as `ReturnBook` and `TakeOutside`. Section 5.5 has two legal/procedural duties: submit for prior approval, and make the amendment in compliance with the Methodology Policy. Modeling both as obligations is more uniform and easier to defend.

### 2026-05-06T17:23:40+02:00

Decision: keep the current governance/deontic shape for section 5.5.

Accepted:

- Submission for prior approval is modeled as `DeonticDecl.obligation`, not as a hard logical constraint.
- Responsibility is modeled existentially per `IndexRuleAmendment`.
- `may_result_in` is kept to preserve possible-result modality.
- `PriorApproval` stays as the obligation scope; no custom `prior_to` relation is introduced for now.
- This entry was later refined by the 2026-05-06T17:39:59+02:00 changelog item.

Reason: this version best preserves legal/deontic force, avoids making violation impossible, keeps source modality visible, and passes the clean financial methodology gate.

## Source

`source.md` states one governance paragraph:

- The Oversight Committee is composed of staff from Solactive and its subsidiaries.
- The Oversight Committee is responsible for decisions regarding amendments to the rules of the Index.
- Any such amendment may result in an amendment of the Guideline.
- Any such amendment must be submitted to the Oversight Committee for prior approval.
- The amendment will be made in compliance with the Methodology Policy.
- The Methodology Policy is available on the Solactive website at the explicit URL.

## Current Chosen Shape

The current IR is intentionally a governance/deontic representation, not a pure factual
state model.

- Committee composition is represented by `composed_of`, `staff_from`, and `subsidiary_of`.
- Index-rule amendment scope is represented by `IndexRuleAmendment`, `IndexRule`, `amendment_of_rule`, and `rule_of`.
- Responsibility is represented directly by `responsible_for_decisions_regarding(OversightCommittee, a)`.
- Possible Guideline amendment is represented by `may_result_in(a, g)` with a possible Guideline-amendment witness.
- Submission for prior approval is represented as a `DeonticDecl.obligation`, not as a hard `AssertDecl.constraint`.
- Compliance with Methodology Policy is represented as a `DeonticDecl.obligation`, not as a hard `AssertDecl.constraint`.
- URL preservation is represented by `document_url(MethodologyPolicy, HttpsWwwSolactiveComDocumentsMethodologyPolicy)`.

## Decisions And Rationale

### 1. Submission Is An Obligation, Not A Hard Constraint

Rejected form:

```a4v3
constraint index_rule_amendment_submission_for_prior_approval :
  forall a: IndexRuleAmendment,
    exists p: PriorApproval,
      submitted_to_for_approval(a, OversightCommittee, p)
```

Reason: the source says the amendment `must be submitted`. In A4V3, `must` maps better to
`DeonticDecl.obligation` because deontic obligations preserve violation semantics. A hard
constraint would say submission is logically impossible to violate, which is stronger than
the methodology wording.

Chosen form:

```a4v3
obligation submit_index_rule_amendment_for_prior_approval(amendment: IndexRuleAmendment)
  action: submit
  target: OversightCommittee
  scope: PriorApproval
```

The `submitted_to_for_approval` relation was removed because it became unused after the hard
constraint was removed.

### 2. Prior Approval Is Kept As `PriorApproval`

We considered reintroducing a relation such as:

```a4v3
rel prior_to : Approval, IndexRuleAmendment
```

Reason rejected for now: this creates a custom temporal relation without a stable local
pattern for what the approval is prior to: the amendment decision, submission, effective
amendment, or Guideline amendment. The source phrase is fixed legal/procedural wording
`for prior approval`; the least risky representation is the typed scope `PriorApproval`
inside the obligation.

If later A4V3 deontic conventions define a canonical `deadline`, `guard`, or temporal
process pattern for prior approval, this can be refined.

### 3. Responsibility Is Direct, Not A Concrete Decision Witness

Rejected weak form:

```a4v3
forall d: Decision, forall a: IndexRuleAmendment,
  decision_regarding(d, a)
  implies responsible_for(OversightCommittee, d)
```

Reason: this is too weak because it is vacuously true when no decision exists. The source
says the Oversight Committee is responsible for decisions regarding any amendments, so the
current financial methodology choice links the committee directly to the amendment-decision topic.

Chosen form:

```a4v3
forall a: IndexRuleAmendment,
  responsible_for_decisions_regarding(OversightCommittee, a)
```

This avoids both vacuity and the stronger claim that each amendment already has a concrete
decision object.

### 4. `may_result_in` Is Kept

Alternative considered:

```a4v3
rel result_in : IndexRuleAmendment, GuidelineAmendment
```

Reason rejected for now: the source says `may result in`, not `results in`. Encoding the
modality only by omitting an existential assertion is too implicit for manual financial methodology quality.
The relation name `may_result_in` keeps the possible-result semantics visible. The current
IR uses an existential witness for a possible Guideline amendment, not for an actually
realized amendment.

Important distinction: this `may` is not deontic permission. It is possibility/modality of
an outcome.

### 5. Compliance Is Also An Obligation

The source says the amendment `will be made in compliance with the Methodology Policy`.
For consistency with the submission clause, this is represented as a deontic obligation,
not as a hard logical invariant.

Current form:

```a4v3
obligation make_index_rule_amendment_in_compliance_with_methodology_policy(amendment: IndexRuleAmendment)
  action: make_in_compliance_with
  target: MethodologyPolicy
```

Reason: legal `will be made in compliance` is close enough to a procedural duty that a hard
constraint would overstate the model. Deontic representation keeps violation semantics
available and avoids treating non-compliant amendments as logically impossible.

## Waiver Decisions

Current human-approved token waivers:

- `such`: an anaphoric surface marker. It refers back to `IndexRuleAmendment`; no standalone
  logical predicate is needed.
- `submitted`: represented by the action-style obligation
  `submit_index_rule_amendment_for_prior_approval` and `action: submit`; the waiver covers
  only token-provenance morphology, not missing semantics.
- `will`: legal/modal future in `will be made in compliance with`. It is represented by the
  compliance obligation, not by a separate temporal operator.
- `made`: represented by the compliance obligation
  `make_index_rule_amendment_in_compliance_with_methodology_policy` and
  `action: make_in_compliance_with`; the waiver covers only token-provenance morphology.

The active waivers here are not semantic omissions. They are either anaphora (`such`) or
token-provenance limitations around deontic action morphology (`submitted`, `made`) and
legal future/deontic force (`will`).

## Validation Status

At the time of this note:

- strict A4V3 parse: pass
- clean gate: accepted
- phrase coverage: 6/6
- token waiver-accounted coverage: 31/31
- exact URL preservation: 1/1
- raw diagnostic suite: still `needs_review` only because of legacy precision alarms; clean
  categorization reports zero blocking diagnostic fails.

## Open Review Questions

- Should `PriorApproval` later be refined into a canonical temporal/deontic pattern once the
  project has a stable A4V3 convention for prior approval?
- Should `may_result_in` become a general prelude relation for possible outcomes, or stay
  local until more sections need the same pattern?
