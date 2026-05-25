# Semantic Claim Alignment: section_2_1

This ledger maps source claims to candidate IR blocks. It is a review surface, not a proof.

## Summary

- claim_count: `12`
- strong_candidate_count: `9`
- partial_candidate_count: `3`
- weak_or_missing_candidate_count: `0`
- reviewed_count: `0`
- approved_count: `0`
- needs_revision_count: `0`
- average_top3_token_coverage: `0.846`
- all_claims_review_approved: `False`

## Review Status Values

- `approved`: source claim is faithfully represented by the approved IR block(s).
- `needs_ir_revision`: source claim is missing, distorted, or only present in names.
- `source_ambiguous`: source itself needs interpretation before judging IR.
- `not_formalized_by_design`: claim is intentionally left as metadata/waiver/support text.

## Claims

### C01 `strong_candidate`

> ### 2.1 Index Universe Requirements

- top3 token coverage: `1.0`
- review status: `unreviewed`
- uncovered by top3: none

Candidate IR blocks:
- `assertion:constraint:eligible_for_index_universe_requirements` line `247` score `0.808`, recall `1.0`
  `constraint eligible_for_index_universe_requirements : forall d: SelectionDay, forall sc: ShareClass, eligible_for_index_universe(d, sc) iff security_in_starting_list_of_financial_instruments( d, sc, starting_list_of_financial_instruments( d, SolactiveGBSGlobalMarketsAllCapUSDIndexPR ) ) and ( gbs_index_universe_classification(d, sc) = DevelopedMarketsEurope or gbs_index_universe_classification(d, sc) = Canada or gbs_index_universe_classification(d, sc) = UnitedStates ) and minimum_average_daily_`
- `declaration:opaque:GbsIndexUniverse` line `7` score `0.633`, recall `0.667`
  `sort GbsIndexUniverse`
- `declaration:opaque:DeterminationOfIndexUniverse` line `125` score `0.6`, recall `0.667`
  `sort DeterminationOfIndexUniverse`
- `declaration:fun:gbs_index_universe` line `14` score `0.583`, recall `0.667`
  `fun[required] gbs_index_universe : GbsIndex -> GbsIndexUniverse`
- `declaration:entity:GbsIndexUniverseFrameworkDocumentPart` line `22` score `0.578`, recall `0.667`
  `entity GbsIndexUniverseFrameworkDocumentPart : DocumentPart`

### C02 `partial_candidate`

> The Index Universe is comprised of all financial instruments which fulfill the below requirements

- top3 token coverage: `0.667`
- review status: `unreviewed`
- uncovered by top3: `compris` (comprised), `fulfill` (fulfill), `below` (below)

Candidate IR blocks:
- `assertion:constraint:eligible_for_index_universe_requirements` line `247` score `0.549`, recall `0.667`
  `constraint eligible_for_index_universe_requirements : forall d: SelectionDay, forall sc: ShareClass, eligible_for_index_universe(d, sc) iff security_in_starting_list_of_financial_instruments( d, sc, starting_list_of_financial_instruments( d, SolactiveGBSGlobalMarketsAllCapUSDIndexPR ) ) and ( gbs_index_universe_classification(d, sc) = DevelopedMarketsEurope or gbs_index_universe_classification(d, sc) = Canada or gbs_index_universe_classification(d, sc) = UnitedStates ) and minimum_average_daily_`
- `assertion:constraint:gbs_index_universe_starting_list_definition` line `138` score `0.474`, recall `0.556`
  `constraint gbs_index_universe_starting_list_definition : forall d: SelectionDay, forall s: Security, security_in_starting_list_of_financial_instruments( d, s, starting_list_of_financial_instruments( d, SolactiveGBSGlobalMarketsAllCapUSDIndexPR ) ) iff part_component_of_gbs_index_universe( d, s, gbs_index_universe(SolactiveGBSGlobalMarketsAllCapUSDIndexPR) )`
- `declaration:fun:starting_list_of_financial_instruments` line `132` score `0.307`, recall `0.333`
  `fun[required] starting_list_of_financial_instruments : SelectionDay, GbsIndex -> StartingListOfFinancialInstruments`
- `declaration:opaque:GbsIndexUniverse` line `7` score `0.278`, recall `0.222`
  `sort GbsIndexUniverse`
- `declaration:subtype:Security` line `2` score `0.244`, recall `0.222`
  `sort Security extends FinancialInstrument`

### C03 `strong_candidate`

> (the "Index Universe Requirements"):

- top3 token coverage: `1.0`
- review status: `unreviewed`
- uncovered by top3: none

Candidate IR blocks:
- `assertion:constraint:eligible_for_index_universe_requirements` line `247` score `0.808`, recall `1.0`
  `constraint eligible_for_index_universe_requirements : forall d: SelectionDay, forall sc: ShareClass, eligible_for_index_universe(d, sc) iff security_in_starting_list_of_financial_instruments( d, sc, starting_list_of_financial_instruments( d, SolactiveGBSGlobalMarketsAllCapUSDIndexPR ) ) and ( gbs_index_universe_classification(d, sc) = DevelopedMarketsEurope or gbs_index_universe_classification(d, sc) = Canada or gbs_index_universe_classification(d, sc) = UnitedStates ) and minimum_average_daily_`
- `declaration:opaque:GbsIndexUniverse` line `7` score `0.633`, recall `0.667`
  `sort GbsIndexUniverse`
- `declaration:opaque:DeterminationOfIndexUniverse` line `125` score `0.6`, recall `0.667`
  `sort DeterminationOfIndexUniverse`
- `declaration:fun:gbs_index_universe` line `14` score `0.583`, recall `0.667`
  `fun[required] gbs_index_universe : GbsIndex -> GbsIndexUniverse`
- `declaration:entity:GbsIndexUniverseFrameworkDocumentPart` line `22` score `0.578`, recall `0.667`
  `entity GbsIndexUniverseFrameworkDocumentPart : DocumentPart`

### C04 `strong_candidate`

> Part/ Component of the GBS Index Universe of the Solactive GBS Global Markets All Cap USD Index PR (ISIN: DE000SLA78E2), on a Selection Day.
2.

- top3 token coverage: `1.0`
- review status: `unreviewed`
- uncovered by top3: none

Candidate IR blocks:
- `assertion:constraint:gbs_index_universe_starting_list_definition` line `138` score `0.838`, recall `0.938`
  `constraint gbs_index_universe_starting_list_definition : forall d: SelectionDay, forall s: Security, security_in_starting_list_of_financial_instruments( d, s, starting_list_of_financial_instruments( d, SolactiveGBSGlobalMarketsAllCapUSDIndexPR ) ) iff part_component_of_gbs_index_universe( d, s, gbs_index_universe(SolactiveGBSGlobalMarketsAllCapUSDIndexPR) )`
- `assertion:fact:gbs_index_isin` line `16` score `0.718`, recall `0.688`
  `fact gbs_index_isin : isin(SolactiveGBSGlobalMarketsAllCapUSDIndexPR) = DE000SLA78E2`
- `assertion:constraint:eligible_for_index_universe_requirements` line `247` score `0.682`, recall `0.812`
  `constraint eligible_for_index_universe_requirements : forall d: SelectionDay, forall sc: ShareClass, eligible_for_index_universe(d, sc) iff security_in_starting_list_of_financial_instruments( d, sc, starting_list_of_financial_instruments( d, SolactiveGBSGlobalMarketsAllCapUSDIndexPR ) ) and ( gbs_index_universe_classification(d, sc) = DevelopedMarketsEurope or gbs_index_universe_classification(d, sc) = Canada or gbs_index_universe_classification(d, sc) = UnitedStates ) and minimum_average_daily_`
- `declaration:entity:SolactiveGBSGlobalMarketsAllCapUSDIndexPR` line `10` score `0.644`, recall `0.625`
  `entity SolactiveGBSGlobalMarketsAllCapUSDIndexPR : GbsIndex`
- `assertion:fact:gbs_index_universe_framework_document_part` line `28` score `0.476`, recall `0.5`
  `fact gbs_index_universe_framework_document_part : part_of_document(GbsIndexUniverseFrameworkDocumentPart, SolactiveGBSBenchmarkSeriesPdf)`

### C05 `strong_candidate`

> Security must be classified as Developed Markets Europe, Canada or United States under the Gbs Index Universe framework ( https://www.solactive.com/downloads/Guideline-Solactive-GBS-Benchmark-Series.pdf ).
3.

- top3 token coverage: `0.864`
- review status: `unreviewed`
- uncovered by top3: `must` (must), `under` (under), `3` (3)

Candidate IR blocks:
- `assertion:fact:gbs_index_universe_framework_document_part_url` line `34` score `0.55`, recall `0.5`
  `fact gbs_index_universe_framework_document_part_url : document_part_url(GbsIndexUniverseFrameworkDocumentPart, HttpsWwwSolactiveComDownloadsGuidelineSolactiveGBSBenchmarkSeriesPdf)`
- `assertion:constraint:eligible_for_index_universe_requirements` line `247` score `0.515`, recall `0.591`
  `constraint eligible_for_index_universe_requirements : forall d: SelectionDay, forall sc: ShareClass, eligible_for_index_universe(d, sc) iff security_in_starting_list_of_financial_instruments( d, sc, starting_list_of_financial_instruments( d, SolactiveGBSGlobalMarketsAllCapUSDIndexPR ) ) and ( gbs_index_universe_classification(d, sc) = DevelopedMarketsEurope or gbs_index_universe_classification(d, sc) = Canada or gbs_index_universe_classification(d, sc) = UnitedStates ) and minimum_average_daily_`
- `assertion:fact:solactive_gbs_benchmark_series_pdf_url` line `25` score `0.441`, recall `0.364`
  `fact solactive_gbs_benchmark_series_pdf_url : document_url(SolactiveGBSBenchmarkSeriesPdf, HttpsWwwSolactiveComDownloadsGuidelineSolactiveGBSBenchmarkSeriesPdf)`
- `declaration:entity:HttpsWwwSolactiveComDownloadsGuidelineSolactiveGBSBenchmarkSeriesPdf` line `21` score `0.425`, recall `0.318`
  `entity HttpsWwwSolactiveComDownloadsGuidelineSolactiveGBSBenchmarkSeriesPdf : Url`
- `declaration:entity:DevelopedMarketsEurope` line `39` score `0.397`, recall `0.364`
  `entity DevelopedMarketsEurope : GbsIndexUniverseClassification`

### C06 `strong_candidate`

> Security must have a minimum Average Daily Value Traded over 1 and 6 months prior to and including the Selection Day of at least USD 5 million.
4.

- top3 token coverage: `0.75`
- review status: `unreviewed`
- uncovered by top3: `must` (must), `least` (least), `5` (5), `million` (million), `4` (4)

Candidate IR blocks:
- `assertion:constraint:minimum_average_daily_value_traded_over_1_and_6_months` line `82` score `0.72`, recall `0.75`
  `constraint minimum_average_daily_value_traded_over_1_and_6_months : forall d: SelectionDay, forall s: Security, minimum_average_daily_value_traded(d, s) <= average_daily_value_traded(d, s, one_month_prior_including_selection_day(d)) and minimum_average_daily_value_traded(d, s) <= average_daily_value_traded(d, s, six_months_prior_including_selection_day(d)) and ( minimum_average_daily_value_traded(d, s) = average_daily_value_traded(d, s, one_month_prior_including_selection_day(d)) or minimum_aver`
- `declaration:fun:minimum_average_daily_value_traded` line `80` score `0.436`, recall `0.4`
  `fun[required] minimum_average_daily_value_traded : SelectionDay, Security -> AverageDailyValueTraded`
- `assertion:constraint:not_current_company_buffer_rule` line `221` score `0.411`, recall `0.45`
  `constraint not_current_company_buffer_rule [realizes: NotCurrentCompanyBufferRule] : forall d: SelectionDay, forall sc: ShareClass, eligible_by_not_current_company_buffer_rule(d, sc) iff not company_currently_included_in_index(d, company(sc)) and highest_minimum_average_daily_value_traded(d, sc)`
- `assertion:constraint:current_company_buffer_rule` line `208` score `0.406`, recall `0.45`
  `constraint current_company_buffer_rule [realizes: CurrentCompanyBufferRule] : forall d: SelectionDay, forall sc: ShareClass, eligible_by_current_company_buffer_rule(d, sc) iff company_currently_included_in_index(d, company(sc)) and share_class_currently_included_in_index(d, sc) and forall other: ShareClass, company(other) = company(sc) and other != sc implies minimum_average_daily_value_traded(d, sc) >= 60% * minimum_average_daily_value_traded(d, other)`
- `assertion:constraint:highest_minimum_average_daily_value_traded_share_class_company` line `184` score `0.4`, recall `0.4`
  `constraint highest_minimum_average_daily_value_traded_share_class_company : forall d: SelectionDay, forall co: Company, company(share_class_with_highest_minimum_average_daily_value_traded(d, co)) = co`

### C07 `strong_candidate`

> Only one share class of each company is eligible for inclusion in the Index Universe.

- top3 token coverage: `0.889`
- review status: `unreviewed`
- uncovered by top3: `inclusion` (inclusion)

Candidate IR blocks:
- `assertion:constraint:only_one_share_class_of_each_company` line `271` score `0.791`, recall `0.889`
  `constraint only_one_share_class_of_each_company : forall d: SelectionDay, forall co: Company, count(sc in ShareClass where eligible_for_index_universe(d, sc) and company(sc) = co) <= 1`
- `declaration:rel:eligible_for_index_universe` line `129` score `0.532`, recall `0.556`
  `rel eligible_for_index_universe : SelectionDay, ShareClass`
- `assertion:constraint:index_universe_bridge` line `243` score `0.511`, recall `0.556`
  `constraint index_universe_bridge : forall d: SelectionDay, forall sc: ShareClass, index_universe(d, sc) iff eligible_for_index_universe(d, sc)`
- `assertion:constraint:not_current_company_buffer_rule` line `221` score `0.482`, recall `0.556`
  `constraint not_current_company_buffer_rule [realizes: NotCurrentCompanyBufferRule] : forall d: SelectionDay, forall sc: ShareClass, eligible_by_not_current_company_buffer_rule(d, sc) iff not company_currently_included_in_index(d, company(sc)) and highest_minimum_average_daily_value_traded(d, sc)`
- `assertion:constraint:current_company_buffer_rule` line `208` score `0.478`, recall `0.556`
  `constraint current_company_buffer_rule [realizes: CurrentCompanyBufferRule] : forall d: SelectionDay, forall sc: ShareClass, eligible_by_current_company_buffer_rule(d, sc) iff company_currently_included_in_index(d, company(sc)) and share_class_currently_included_in_index(d, sc) and forall other: ShareClass, company(other) = company(sc) and other != sc implies minimum_average_daily_value_traded(d, sc) >= 60% * minimum_average_daily_value_traded(d, other)`

### C08 `partial_candidate`

> To avoid frequent changes between two share-classes of a company, the Index Administrator applies the following buffer rules:
   1.

- top3 token coverage: `0.714`
- review status: `unreviewed`
- uncovered by top3: `administrator` (Administrator), `appli` (applies), `follow` (following), `1` (1)

Candidate IR blocks:
- `declaration:entity:AvoidFrequentChangesBetweenTwoShareClasses` line `177` score `0.465`, recall `0.429`
  `entity AvoidFrequentChangesBetweenTwoShareClasses : VagueTerm`
- `declaration:entity:CurrentCompanyBufferRule` line `175` score `0.34`, recall `0.286`
  `entity CurrentCompanyBufferRule : IndexBufferRule`
- `declaration:entity:NotCurrentCompanyBufferRule` line `176` score `0.34`, recall `0.286`
  `entity NotCurrentCompanyBufferRule : IndexBufferRule`
- `assertion:constraint:not_current_company_buffer_rule` line `221` score `0.318`, recall `0.357`
  `constraint not_current_company_buffer_rule [realizes: NotCurrentCompanyBufferRule] : forall d: SelectionDay, forall sc: ShareClass, eligible_by_not_current_company_buffer_rule(d, sc) iff not company_currently_included_in_index(d, company(sc)) and highest_minimum_average_daily_value_traded(d, sc)`
- `assertion:constraint:current_company_buffer_rule` line `208` score `0.315`, recall `0.357`
  `constraint current_company_buffer_rule [realizes: CurrentCompanyBufferRule] : forall d: SelectionDay, forall sc: ShareClass, eligible_by_current_company_buffer_rule(d, sc) iff company_currently_included_in_index(d, company(sc)) and share_class_currently_included_in_index(d, sc) and forall other: ShareClass, company(other) = company(sc) and other != sc implies minimum_average_daily_value_traded(d, sc) >= 60% * minimum_average_daily_value_traded(d, other)`

### C09 `strong_candidate`

> If the company is currently included in the Index: The share class currently included in the Index will be eligible for the Index Universe if its minimum Average Daily Value Traded over 1 month and over 6 months prior to and including the Selection Day is at least 60% of the minimum Average Daily Value Traded over 1 month and over 6 months prior to and including the Selection Day of any other share class of the company.

- top3 token coverage: `0.875`
- review status: `unreviewed`
- uncovered by top3: `will` (will), `universe` (Universe), `least` (least)

Candidate IR blocks:
- `assertion:constraint:current_company_buffer_rule` line `208` score `0.629`, recall `0.667`
  `constraint current_company_buffer_rule [realizes: CurrentCompanyBufferRule] : forall d: SelectionDay, forall sc: ShareClass, eligible_by_current_company_buffer_rule(d, sc) iff company_currently_included_in_index(d, company(sc)) and share_class_currently_included_in_index(d, sc) and forall other: ShareClass, company(other) = company(sc) and other != sc implies minimum_average_daily_value_traded(d, sc) >= 60% * minimum_average_daily_value_traded(d, other)`
- `assertion:constraint:not_current_company_buffer_rule` line `221` score `0.564`, recall `0.583`
  `constraint not_current_company_buffer_rule [realizes: NotCurrentCompanyBufferRule] : forall d: SelectionDay, forall sc: ShareClass, eligible_by_not_current_company_buffer_rule(d, sc) iff not company_currently_included_in_index(d, company(sc)) and highest_minimum_average_daily_value_traded(d, sc)`
- `assertion:constraint:minimum_average_daily_value_traded_over_1_and_6_months` line `82` score `0.53`, recall `0.542`
  `constraint minimum_average_daily_value_traded_over_1_and_6_months : forall d: SelectionDay, forall s: Security, minimum_average_daily_value_traded(d, s) <= average_daily_value_traded(d, s, one_month_prior_including_selection_day(d)) and minimum_average_daily_value_traded(d, s) <= average_daily_value_traded(d, s, six_months_prior_including_selection_day(d)) and ( minimum_average_daily_value_traded(d, s) = average_daily_value_traded(d, s, one_month_prior_including_selection_day(d)) or minimum_aver`
- `assertion:constraint:highest_minimum_average_daily_value_traded_definition` line `188` score `0.461`, recall `0.458`
  `constraint highest_minimum_average_daily_value_traded_definition : forall d: SelectionDay, forall co: Company, forall other: ShareClass, company(other) = co and other != share_class_with_highest_minimum_average_daily_value_traded(d, co) implies minimum_average_daily_value_traded( d, share_class_with_highest_minimum_average_daily_value_traded(d, co) ) >= minimum_average_daily_value_traded(d, other)`
- `assertion:constraint:highest_minimum_average_daily_value_traded_share_class_company` line `184` score `0.453`, recall `0.417`
  `constraint highest_minimum_average_daily_value_traded_share_class_company : forall d: SelectionDay, forall co: Company, company(share_class_with_highest_minimum_average_daily_value_traded(d, co)) = co`

### C10 `strong_candidate`

> If the company is currently not included in the Index: The share class with the highest minimum Average Daily Value Traded over 1 month and over 6 months prior to and including the Selection Day is included in the Index Universe.
5.

- top3 token coverage: `0.905`
- review status: `unreviewed`
- uncovered by top3: `universe` (Universe), `5` (5)

Candidate IR blocks:
- `assertion:constraint:not_current_company_buffer_rule` line `221` score `0.631`, recall `0.667`
  `constraint not_current_company_buffer_rule [realizes: NotCurrentCompanyBufferRule] : forall d: SelectionDay, forall sc: ShareClass, eligible_by_not_current_company_buffer_rule(d, sc) iff not company_currently_included_in_index(d, company(sc)) and highest_minimum_average_daily_value_traded(d, sc)`
- `assertion:constraint:minimum_average_daily_value_traded_over_1_and_6_months` line `82` score `0.592`, recall `0.619`
  `constraint minimum_average_daily_value_traded_over_1_and_6_months : forall d: SelectionDay, forall s: Security, minimum_average_daily_value_traded(d, s) <= average_daily_value_traded(d, s, one_month_prior_including_selection_day(d)) and minimum_average_daily_value_traded(d, s) <= average_daily_value_traded(d, s, six_months_prior_including_selection_day(d)) and ( minimum_average_daily_value_traded(d, s) = average_daily_value_traded(d, s, one_month_prior_including_selection_day(d)) or minimum_aver`
- `assertion:constraint:current_company_buffer_rule` line `208` score `0.579`, recall `0.619`
  `constraint current_company_buffer_rule [realizes: CurrentCompanyBufferRule] : forall d: SelectionDay, forall sc: ShareClass, eligible_by_current_company_buffer_rule(d, sc) iff company_currently_included_in_index(d, company(sc)) and share_class_currently_included_in_index(d, sc) and forall other: ShareClass, company(other) = company(sc) and other != sc implies minimum_average_daily_value_traded(d, sc) >= 60% * minimum_average_daily_value_traded(d, other)`
- `assertion:constraint:highest_minimum_average_daily_value_traded_share_class_company` line `184` score `0.547`, recall `0.524`
  `constraint highest_minimum_average_daily_value_traded_share_class_company : forall d: SelectionDay, forall co: Company, company(share_class_with_highest_minimum_average_daily_value_traded(d, co)) = co`
- `declaration:fun:share_class_with_highest_minimum_average_daily_value_traded` line `179` score `0.542`, recall `0.524`
  `fun[required] share_class_with_highest_minimum_average_daily_value_traded : SelectionDay, Company -> ShareClass`

### C11 `partial_candidate`

> Security must be classified in one of these FactSet Revere Business Industry Classification System ("RBICS") Subindustry Classification (see Appendix).

- top3 token coverage: `0.692`
- review status: `unreviewed`
- uncovered by top3: `securiti` (Security), `must` (must), `one` (one), `see` (see)

Candidate IR blocks:
- `assertion:constraint:appendix_rbics_subindustry_classification_definition` line `111` score `0.669`, recall `0.692`
  `constraint appendix_rbics_subindustry_classification_definition : forall cls: RBICSSubindustryClassification, appendix_rbics_subindustry_classification(cls) iff rbics_subindustry_classification_of_system( cls, FactSetRevereBusinessIndustryClassificationSystem ) and rbics_subindustry_classification_in_appendix( cls, IndexGuidelineAppendix )`
- `declaration:entity:FactSetRevereBusinessIndustryClassificationSystem` line `100` score `0.532`, recall `0.462`
  `entity FactSetRevereBusinessIndustryClassificationSystem : BusinessIndustryClassificationSystem`
- `declaration:rel:rbics_subindustry_classification_of_system` line `103` score `0.523`, recall `0.462`
  `rel rbics_subindustry_classification_of_system : RBICSSubindustryClassification, BusinessIndustryClassificationSystem`
- `declaration:opaque:BusinessIndustryClassificationSystem` line `96` score `0.429`, recall `0.308`
  `sort BusinessIndustryClassificationSystem`
- `declaration:rel:rbics_subindustry_classification_in_appendix` line `106` score `0.394`, recall `0.308`
  `rel rbics_subindustry_classification_in_appendix : RBICSSubindustryClassification, Appendix`

### C12 `strong_candidate`

> The determination of the Index Universe is fully rule-based and the Index Administrator cannot make any discretionary decisions.

- top3 token coverage: `0.8`
- review status: `unreviewed`
- uncovered by top3: `cannot` (cannot), `make` (make)

Candidate IR blocks:
- `declaration:prohibition:index_administrator_discretionary_decision` line `279` score `0.603`, recall `0.6`
  `prohibition index_administrator_discretionary_decision( agent: IndexAdministrator, determination: DeterminationOfIndexUniverse, decision: DiscretionaryDecision )`
- `declaration:rel:fully_rule_based` line `241` score `0.529`, recall `0.5`
  `rel fully_rule_based : DeterminationOfIndexUniverse`
- `assertion:constraint:determination_of_index_universe_fully_rule_based` line `275` score `0.482`, recall `0.5`
  `constraint determination_of_index_universe_fully_rule_based : forall d: SelectionDay, fully_rule_based(determination_of_index_universe(d))`
- `declaration:opaque:DeterminationOfIndexUniverse` line `125` score `0.373`, recall `0.3`
  `sort DeterminationOfIndexUniverse`
- `declaration:opaque:DiscretionaryDecision` line `126` score `0.31`, recall `0.2`
  `sort DiscretionaryDecision`
