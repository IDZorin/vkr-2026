# Semantic Claim Alignment: section_5_4

This ledger maps source claims to candidate IR blocks. It is a review surface, not a proof.

## Summary

- claim_count: `6`
- strong_candidate_count: `3`
- partial_candidate_count: `3`
- weak_or_missing_candidate_count: `0`
- reviewed_count: `0`
- approved_count: `0`
- needs_revision_count: `0`
- average_top3_token_coverage: `0.818`
- all_claims_review_approved: `False`

## Review Status Values

- `approved`: source claim is faithfully represented by the approved IR block(s).
- `needs_ir_revision`: source claim is missing, distorted, or only present in names.
- `source_ambiguous`: source itself needs interpretation before judging IR.
- `not_formalized_by_design`: claim is intentionally left as metadata/waiver/support text.

## Claims

### C01 `strong_candidate`

> Solactive makes the greatest possible efforts to ensure the resilience and continued integrity of its indices over time.

- top3 token coverage: `0.917`
- review status: `unreviewed`
- uncovered by top3: `mak` (makes)

Candidate IR blocks:
- `assertion:constraint:solactive_efforts_for_resilience_and_integrity` line `130` score `0.689`, recall `0.75`
  `constraint solactive_efforts_for_resilience_and_integrity : forall i: Index, index_of(i, Solactive) implies effort_to_ensure(SolactiveGreatestPossibleEfforts, i, Resilience) and effort_to_ensure( SolactiveGreatestPossibleEfforts, i, ContinuedIntegrity )`
- `assertion:fact:solactive_effort` line `125` score `0.493`, recall `0.5`
  `fact solactive_effort : effort_by(SolactiveGreatestPossibleEfforts, Solactive) and greatest_possible(SolactiveGreatestPossibleEfforts) and over_time(SolactiveGreatestPossibleEfforts)`
- `declaration:entity:SolactiveGreatestPossibleEfforts` line `28` score `0.392`, recall `0.333`
  `entity SolactiveGreatestPossibleEfforts : Effort`
- `declaration:rel:greatest_possible` line `45` score `0.35`, recall `0.25`
  `rel greatest_possible : Effort`
- `declaration:rel:over_time` line `46` score `0.35`, recall `0.25`
  `rel over_time : Effort`

### C02 `strong_candidate`

> Where necessary, Solactive follows a clearly defined and transparent procedure to adapt Index methodologies to changing underlying markets (see Section 5.2 вЂњMethodology ReviewвЂќ) in order to maintain continued reliability and comparability of the indices.

- top3 token coverage: `0.955`
- review status: `unreviewed`
- uncovered by top3: `order` (order)

Candidate IR blocks:
- `assertion:constraint:methodology_adaptation_where_necessary` line `141` score `0.858`, recall `0.955`
  `constraint methodology_adaptation_where_necessary : forall i: Index, forall m: IndexMethodology, forall u: UnderlyingMarket, index_of(i, Solactive) and methodology_of_index(m, i) and necessary_to_adapt_methodology(m, u) and changing_underlying_market(u) implies exists p: Procedure, follows(Solactive, p) and clearly_defined(p) and transparent(p) and adapts_index_methodology(p, m, u) and procedure_maintains(p, i, ContinuedReliability) and procedure_maintains(p, i, Comparability) and see(p, Section`
- `declaration:rel:necessary_to_adapt_methodology` line `49` score `0.343`, recall `0.273`
  `rel necessary_to_adapt_methodology : IndexMethodology, UnderlyingMarket`
- `declaration:rel:adapts_index_methodology` line `55` score `0.338`, recall `0.273`
  `rel adapts_index_methodology : Procedure, IndexMethodology, UnderlyingMarket`
- `declaration:rel:transparent` line `54` score `0.273`, recall `0.091`
  `rel transparent : Procedure`
- `declaration:rel:changing_underlying_market` line `51` score `0.259`, recall `0.136`
  `rel changing_underlying_market : UnderlyingMarket`

### C03 `partial_candidate`

> Nevertheless, if no other options are available the orderly cessation of the Index may be indicated.

- top3 token coverage: `0.667`
- review status: `unreviewed`
- uncovered by top3: `neverthel` (Nevertheless), `other` (other), `may` (may)

Candidate IR blocks:
- `assertion:constraint:orderly_cessation_indicated_if_no_options` line `212` score `0.594`, recall `0.667`
  `constraint orderly_cessation_indicated_if_no_options : forall i: Index, index_of(i, Solactive) and usual_case_for_cessation(i) and count(o in Option where available_option_for_index(o, i)) = 0 implies exists c: Cessation, cessation_of_index(c, i) and orderly(c) and indicated(c)`
- `declaration:rel:available_option_for_index` line `60` score `0.387`, recall `0.333`
  `rel available_option_for_index : Option, Index`
- `declaration:rel:orderly` line `63` score `0.378`, recall `0.222`
  `rel orderly : Cessation`
- `declaration:rel:indicated` line `64` score `0.378`, recall `0.222`
  `rel indicated : Cessation`
- `declaration:permission:indicate_orderly_cessation` line `107` score `0.367`, recall `0.333`
  `permission indicate_orderly_cessation(agent: Organization, target: Index) action: indicate scope: Cessation`

### C04 `partial_candidate`

> This is usually the case when the underlying market or economic reality, which an index is set to measure or to reflect, changes substantially and in a way not foreseeable at the time of inception of the index, the index rules, and particularly the selection criteria, can no longer be applied coherently or the index is no longer used as the underlying value for financial instruments, investment funds and financial contracts.

- top3 token coverage: `0.688`
- review status: `unreviewed`
- uncovered by top3: `way` (way), `time` (time), `rul` (rules), `particularli` (particularly), `selection` (selection), `criteria` (criteria), `can` (can), `longer` (longer), `appli` (applied), `coherentli` (coherently)

Candidate IR blocks:
- `assertion:constraint:cessation_usual_when_underlying_market_changes` line `157` score `0.403`, recall `0.406`
  `constraint cessation_usual_when_underlying_market_changes : forall i: Index, ( exists u: UnderlyingMarket, ( index_set_to_measure_underlying_market(i, u) or index_set_to_reflect_underlying_market(i, u) ) and underlying_market_changes(u) and underlying_market_change_described_by(u, Substantially) and not underlying_market_change_foreseeable_at_inception(u, i) ) implies usual_case_for_cessation(i)`
- `assertion:constraint:cessation_usual_when_economic_reality_changes` line `171` score `0.396`, recall `0.406`
  `constraint cessation_usual_when_economic_reality_changes : forall i: Index, ( exists e: EconomicReality, ( index_set_to_measure_economic_reality(i, e) or index_set_to_reflect_economic_reality(i, e) ) and economic_reality_changes(e) and economic_reality_change_described_by(e, Substantially) and not economic_reality_change_foreseeable_at_inception(e, i) ) implies usual_case_for_cessation(i)`
- `assertion:constraint:cessation_usual_when_index_not_used_as_underlying_value` line `194` score `0.38`, recall `0.375`
  `constraint cessation_usual_when_index_not_used_as_underlying_value : forall i: Index, ( not exists fi: FinancialInstrument, used_as_underlying_value_for_financial_instrument(i, fi) ) and ( not exists f: InvestmentFund, used_as_underlying_value_for_investment_fund(i, f) ) and ( not exists c: FinancialContract, used_as_underlying_value_for_financial_contract(i, c) ) implies usual_case_for_cessation(i)`
- `declaration:rel:underlying_market_change_foreseeable_at_inception` line `75` score `0.295`, recall `0.188`
  `rel underlying_market_change_foreseeable_at_inception : UnderlyingMarket, Index`
- `declaration:rel:used_as_underlying_value_for_financial_instrument` line `83` score `0.283`, recall `0.188`
  `rel used_as_underlying_value_for_financial_instrument : Index, FinancialInstrument`

### C05 `partial_candidate`

> Solactive has established and maintains clear guidelines on how to identify situations in which the cessation of an index is unavoidable, how stakeholders are to be informed and consulted and the procedures to be followed for a termination or the transition to an alternative index.

- top3 token coverage: `0.684`
- review status: `unreviewed`
- uncovered by top3: `how` (how), `identifi` (identify), `situation` (situations), `unavoidable` (unavoidable), `follow` (followed), `terminate` (termination)

Candidate IR blocks:
- `assertion:constraint:guidelines_include_transition_procedure` line `243` score `0.372`, recall `0.368`
  `constraint guidelines_include_transition_procedure : exists p: Procedure, exists a: AlternativeIndex, procedure_in_guidelines(SolactiveCessationGuidelines, p) and procedure_for_transition_to_alternative_index(p, a)`
- `assertion:constraint:guidelines_inform_and_consult_stakeholders` line `233` score `0.364`, recall `0.316`
  `constraint guidelines_inform_and_consult_stakeholders : forall s: Stakeholder, guidelines_inform(SolactiveCessationGuidelines, s) and guidelines_consult(SolactiveCessationGuidelines, s)`
- `assertion:fact:solactive_cessation_guidelines` line `223` score `0.344`, recall `0.316`
  `fact solactive_cessation_guidelines : established_by(SolactiveCessationGuidelines, Solactive) and maintained_by(SolactiveCessationGuidelines, Solactive) and clear(SolactiveCessationGuidelines)`
- `assertion:constraint:guidelines_identify_unavoidable_cessation_situations` line `228` score `0.341`, recall `0.316`
  `constraint guidelines_identify_unavoidable_cessation_situations : forall s: CessationSituation, guidelines_identify(SolactiveCessationGuidelines, s) implies unavoidable(s)`
- `declaration:rel:guidelines_inform` line `95` score `0.293`, recall `0.158`
  `rel guidelines_inform : Guidelines, Stakeholder`

### C06 `strong_candidate`

> Details are specified in the Solactive Termination Policy, which is incorporated by reference and available on the Solactive website: [https://www.solactive.com/documents/termination-policy/](https://www.solactive.com/documents/termination-policy/) .

- top3 token coverage: `1.0`
- review status: `unreviewed`
- uncovered by top3: none

Candidate IR blocks:
- `assertion:fact:termination_policy_location` line `117` score `0.647`, recall `0.692`
  `fact termination_policy_location : document_url( SolactiveTerminationPolicy, HttpsWwwSolactiveComDocumentsTerminationPolicy ) and available_on(SolactiveTerminationPolicy, SolactiveWebsite) and website_of(SolactiveWebsite, Solactive)`
- `declaration:entity:HttpsWwwSolactiveComDocumentsTerminationPolicy` line `39` score `0.577`, recall `0.538`
  `entity HttpsWwwSolactiveComDocumentsTerminationPolicy : Url`
- `assertion:fact:termination_policy_details` line `248` score `0.52`, recall `0.538`
  `fact termination_policy_details : details_specified_in( SolactiveCessationGuidelines, SolactiveTerminationPolicy ) and incorporated_by_reference(SolactiveTerminationPolicy)`
- `declaration:rel:incorporated_by_reference` line `103` score `0.373`, recall `0.308`
  `rel incorporated_by_reference : TerminationPolicy`
- `declaration:rel:details_specified_in` line `102` score `0.359`, recall `0.308`
  `rel details_specified_in : Guidelines, TerminationPolicy`
