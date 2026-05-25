# Semantic Claim Alignment: section_1_2

This ledger maps source claims to candidate IR blocks. It is a review surface, not a proof.

## Summary

- claim_count: `9`
- strong_candidate_count: `6`
- partial_candidate_count: `3`
- weak_or_missing_candidate_count: `0`
- reviewed_count: `0`
- approved_count: `0`
- needs_revision_count: `0`
- average_top3_token_coverage: `0.795`
- all_claims_review_approved: `False`

## Review Status Values

- `approved`: source claim is faithfully represented by the approved IR block(s).
- `needs_ir_revision`: source claim is missing, distorted, or only present in names.
- `source_ambiguous`: source itself needs interpretation before judging IR.
- `not_formalized_by_design`: claim is intentionally left as metadata/waiver/support text.

## Claims

### C01 `partial_candidate`

> ### 1.2 Identifiers and Publication

- top3 token coverage: `0.5`
- review status: `unreviewed`
- uncovered by top3: `identifier` (Identifiers)

Candidate IR blocks:
- `declaration:opaque:IndexPublication` line `18` score `0.486`, recall `0.5`
  `sort IndexPublication`
- `declaration:subtype:GuidelineAmendment` line `20` score `0.455`, recall `0.5`
  `sort GuidelineAmendment extends IndexPublication`
- `declaration:subtype:NoticePublication` line `19` score `0.45`, recall `0.5`
  `sort NoticePublication extends IndexPublication`
- `declaration:rel:publication_in_relation_to_index` line `92` score `0.45`, recall `0.5`
  `rel publication_in_relation_to_index : IndexPublication, Index`
- `declaration:rel:available_at` line `93` score `0.446`, recall `0.5`
  `rel available_at : IndexPublication, WebResource`

### C02 `strong_candidate`

> The Index is published under the following identifiers:

- top3 token coverage: `1.0`
- review status: `unreviewed`
- uncovered by top3: none

Candidate IR blocks:
- `declaration:rel:published_under_following_identifiers` line `82` score `0.96`, recall `1.0`
  `rel published_under_following_identifiers : Index`
- `assertion:constraint:published_index_on_index_administrator_website` line `177` score `0.876`, recall `1.0`
  `constraint published_index_on_index_administrator_website : forall i: Index, published_under_following_identifiers(i) implies published_on(i, SolactiveWebsite)`
- `assertion:constraint:published_index_available_via_boerse_stuttgart` line `182` score `0.852`, recall `1.0`
  `constraint published_index_available_via_boerse_stuttgart : forall i: Index, published_under_following_identifiers(i) implies available_via(i, BoerseStuttgartGmbHPriceMarketingServices)`
- `assertion:constraint:vendor_decides_distribution_or_display` line `191` score `0.834`, recall `1.0`
  `constraint vendor_decides_distribution_or_display : forall v: AffiliatedVendor, forall i: Index, forall a: VendorAction, published_under_following_identifiers(i) implies individual_basis(vendor_decision(v, i, a)) and via_information_systems(vendor_decision(v, i, a), information_systems(v))`
- `assertion:fact:index_ntr_identifiers` line `130` score `0.824`, recall `1.0`
  `fact index_ntr_identifiers : published_under_following_identifiers(SolactiveTransatlanticCleanEnergyEURIndexNTR) and index_name(SolactiveTransatlanticCleanEnergyEURIndexNTR) = SolactiveTransatlanticCleanEnergyEURIndexNTRName and index_isin(SolactiveTransatlanticCleanEnergyEURIndexNTR) = DE000SL0R4C2 and index_currency(SolactiveTransatlanticCleanEnergyEURIndexNTR) = EUR and index_type(SolactiveTransatlanticCleanEnergyEURIndexNTR) = NetTotalReturn and index_ric(SolactiveTransatlanticCleanEnergyEUR`

### C03 `strong_candidate`

> | Name                                                 | ISIN         | Currency   | Type   | RIC       | BBG ticker   |
|------------------------------------------------------|--------------|------------|--------|-----------|--------------|
| Solactive Transatlantic Clean Energy EUR Index PR    | DE000SL0R4B4 | EUR        | PR*    | .SOLTCEYP | SOLTCEYP     |
| Solactive Transatlantic Clean Energy EUR Index NTR   | DE000SL0R4C2 | EUR        | NTR*   | .SOLTCEYN |              |
| Solactive Transatlantic Clean Energy EUR Index TR    | DE000SL0R4D0 | EUR        | GTR*   | .SOLTCEYT | SOLTCEYT     |
| Solactive Transatlantic Clean Energy EUR Index 50 AR | DE000SL0R4E8 | EUR        | AR**   | .SOLTCA50 | SOLTCA50     |
| Solactive Transatlantic Clean Energy EUR Index 5% AR | DE000SL0R4F5 | EUR        | AR*    | .SOLTCEA5 | SOLTCEA5     |

- top3 token coverage: `1.0`
- review status: `unreviewed`
- uncovered by top3: none

Candidate IR blocks:
- `assertion:fact:index_50_ar_identifiers` line `149` score `0.896`, recall `1.0`
  `fact index_50_ar_identifiers : published_under_following_identifiers(SolactiveTransatlanticCleanEnergyEURIndex50AR) and index_name(SolactiveTransatlanticCleanEnergyEURIndex50AR) = SolactiveTransatlanticCleanEnergyEURIndex50ARName and index_isin(SolactiveTransatlanticCleanEnergyEURIndex50AR) = DE000SL0R4E8 and index_currency(SolactiveTransatlanticCleanEnergyEURIndex50AR) = EUR and index_type(SolactiveTransatlanticCleanEnergyEURIndex50AR) = AdjustedReturnIndex and index_ric(SolactiveTransatlanticC`
- `assertion:fact:index_pr_identifiers` line `120` score `0.891`, recall `1.0`
  `fact index_pr_identifiers : published_under_following_identifiers(SolactiveTransatlanticCleanEnergyEURIndexPR) and index_name(SolactiveTransatlanticCleanEnergyEURIndexPR) = SolactiveTransatlanticCleanEnergyEURIndexPRName and index_isin(SolactiveTransatlanticCleanEnergyEURIndexPR) = DE000SL0R4B4 and index_currency(SolactiveTransatlanticCleanEnergyEURIndexPR) = EUR and index_type(SolactiveTransatlanticCleanEnergyEURIndexPR) = PriceReturn and index_ric(SolactiveTransatlanticCleanEnergyEURIndexPR) =`
- `assertion:fact:index_5_percent_ar_identifiers` line `159` score `0.889`, recall `1.0`
  `fact index_5_percent_ar_identifiers : published_under_following_identifiers(SolactiveTransatlanticCleanEnergyEURIndex5PercentAR) and index_name(SolactiveTransatlanticCleanEnergyEURIndex5PercentAR) = SolactiveTransatlanticCleanEnergyEURIndex5PercentARName and index_isin(SolactiveTransatlanticCleanEnergyEURIndex5PercentAR) = DE000SL0R4F5 and index_currency(SolactiveTransatlanticCleanEnergyEURIndex5PercentAR) = EUR and index_type(SolactiveTransatlanticCleanEnergyEURIndex5PercentAR) = AdjustedReturn`
- `assertion:fact:index_tr_identifiers` line `139` score `0.885`, recall `1.0`
  `fact index_tr_identifiers : published_under_following_identifiers(SolactiveTransatlanticCleanEnergyEURIndexTR) and index_name(SolactiveTransatlanticCleanEnergyEURIndexTR) = SolactiveTransatlanticCleanEnergyEURIndexTRName and index_isin(SolactiveTransatlanticCleanEnergyEURIndexTR) = DE000SL0R4D0 and index_currency(SolactiveTransatlanticCleanEnergyEURIndexTR) = EUR and index_type(SolactiveTransatlanticCleanEnergyEURIndexTR) = GrossTotalReturn and index_ric(SolactiveTransatlanticCleanEnergyEURIndex`
- `assertion:constraint:ntr_has_no_bbg_ticker` line `169` score `0.806`, recall `0.833`
  `constraint ntr_has_no_bbg_ticker : not exists t: BBGTicker, bbg_ticker(SolactiveTransatlanticCleanEnergyEURIndexNTR, t)`

### C04 `strong_candidate`

> *PR, NTR, GTR, AR means that the Index is calculated as price return, net total return, gross total return, adjusted return Index as described in the Equity Index Methodology, which is available on the Solactive website: [https://www.solactive.com/documents/equity-index-methodology/](https://www.solactive.com/documents/equity-index-methodology/)

- top3 token coverage: `0.857`
- review status: `unreviewed`
- uncovered by top3: `mean` (means), `calculat` (calculated), `describ` (described)

Candidate IR blocks:
- `assertion:fact:equity_index_methodology_location` line `105` score `0.485`, recall `0.476`
  `fact equity_index_methodology_location : document_url(EquityIndexMethodology, HttpsWwwSolactiveComDocumentsEquityIndexMethodology) and available_on(EquityIndexMethodology, SolactiveWebsite)`
- `assertion:fact:index_type_identifier_meanings` line `95` score `0.484`, recall `0.476`
  `fact index_type_identifier_meanings : index_type_identifier(PriceReturn) = PR and index_type_identifier(NetTotalReturn) = NTR and index_type_identifier(GrossTotalReturn) = GTR and index_type_identifier(AdjustedReturnIndex) = AR`
- `declaration:entity:HttpsWwwSolactiveComDocumentsEquityIndexMethodology` line `68` score `0.455`, recall `0.381`
  `entity HttpsWwwSolactiveComDocumentsEquityIndexMethodology : Url`
- `declaration:enum:IndexType` line `7` score `0.43`, recall `0.381`
  `sort IndexType = PriceReturn | NetTotalReturn | GrossTotalReturn | AdjustedReturnIndex`
- `assertion:fact:index_ntr_identifiers` line `130` score `0.426`, recall `0.476`
  `fact index_ntr_identifiers : published_under_following_identifiers(SolactiveTransatlanticCleanEnergyEURIndexNTR) and index_name(SolactiveTransatlanticCleanEnergyEURIndexNTR) = SolactiveTransatlanticCleanEnergyEURIndexNTRName and index_isin(SolactiveTransatlanticCleanEnergyEURIndexNTR) = DE000SL0R4C2 and index_currency(SolactiveTransatlanticCleanEnergyEURIndexNTR) = EUR and index_type(SolactiveTransatlanticCleanEnergyEURIndexNTR) = NetTotalReturn and index_ric(SolactiveTransatlanticCleanEnergyEUR`

### C05 `strong_candidate`

> **AR means that the Index is calculated as an adjusted return index, following the formula specified in Section 4.

- top3 token coverage: `0.8`
- review status: `unreviewed`
- uncovered by top3: `mean` (means), `calculat` (calculated)

Candidate IR blocks:
- `assertion:fact:index_50_ar_identifiers` line `149` score `0.676`, recall `0.8`
  `fact index_50_ar_identifiers : published_under_following_identifiers(SolactiveTransatlanticCleanEnergyEURIndex50AR) and index_name(SolactiveTransatlanticCleanEnergyEURIndex50AR) = SolactiveTransatlanticCleanEnergyEURIndex50ARName and index_isin(SolactiveTransatlanticCleanEnergyEURIndex50AR) = DE000SL0R4E8 and index_currency(SolactiveTransatlanticCleanEnergyEURIndex50AR) = EUR and index_type(SolactiveTransatlanticCleanEnergyEURIndex50AR) = AdjustedReturnIndex and index_ric(SolactiveTransatlanticC`
- `assertion:fact:index_5_percent_ar_identifiers` line `159` score `0.419`, recall `0.5`
  `fact index_5_percent_ar_identifiers : published_under_following_identifiers(SolactiveTransatlanticCleanEnergyEURIndex5PercentAR) and index_name(SolactiveTransatlanticCleanEnergyEURIndex5PercentAR) = SolactiveTransatlanticCleanEnergyEURIndex5PercentARName and index_isin(SolactiveTransatlanticCleanEnergyEURIndex5PercentAR) = DE000SL0R4F5 and index_currency(SolactiveTransatlanticCleanEnergyEURIndex5PercentAR) = EUR and index_type(SolactiveTransatlanticCleanEnergyEURIndex5PercentAR) = AdjustedReturn`
- `declaration:rel:formula_specified_in` line `84` score `0.34`, recall `0.3`
  `rel formula_specified_in : Index, DocumentPart`
- `assertion:fact:index_ntr_identifiers` line `130` score `0.335`, recall `0.4`
  `fact index_ntr_identifiers : published_under_following_identifiers(SolactiveTransatlanticCleanEnergyEURIndexNTR) and index_name(SolactiveTransatlanticCleanEnergyEURIndexNTR) = SolactiveTransatlanticCleanEnergyEURIndexNTRName and index_isin(SolactiveTransatlanticCleanEnergyEURIndexNTR) = DE000SL0R4C2 and index_currency(SolactiveTransatlanticCleanEnergyEURIndexNTR) = EUR and index_type(SolactiveTransatlanticCleanEnergyEURIndexNTR) = NetTotalReturn and index_ric(SolactiveTransatlanticCleanEnergyEUR`
- `assertion:fact:index_pr_identifiers` line `120` score `0.334`, recall `0.4`
  `fact index_pr_identifiers : published_under_following_identifiers(SolactiveTransatlanticCleanEnergyEURIndexPR) and index_name(SolactiveTransatlanticCleanEnergyEURIndexPR) = SolactiveTransatlanticCleanEnergyEURIndexPRName and index_isin(SolactiveTransatlanticCleanEnergyEURIndexPR) = DE000SL0R4B4 and index_currency(SolactiveTransatlanticCleanEnergyEURIndexPR) = EUR and index_type(SolactiveTransatlanticCleanEnergyEURIndexPR) = PriceReturn and index_ric(SolactiveTransatlanticCleanEnergyEURIndexPR) =`

### C06 `partial_candidate`

> The Index is published on the website of the Index Administrator ( [www.solactive.com](https://www.solactive.com) ) and is, in addition, available via the price marketing services of Boerse Stuttgart GmbH and may be distributed to all of its affiliated vendors.

- top3 token coverage: `0.455`
- review status: `unreviewed`
- uncovered by top3: `website` (website), `administrator` (Administrator), `www` (www), `solactive` (solactive), `com` (com), `http` (https), `addition` (addition), `may` (may), `distribut` (distributed), `all` (all), `affiliat` (affiliated), `vendor` (vendors)

Candidate IR blocks:
- `assertion:constraint:published_index_available_via_boerse_stuttgart` line `182` score `0.46`, recall `0.455`
  `constraint published_index_available_via_boerse_stuttgart : forall i: Index, published_under_following_identifiers(i) implies available_via(i, BoerseStuttgartGmbHPriceMarketingServices)`
- `declaration:rel:available_via` line `89` score `0.357`, recall `0.273`
  `rel available_via : Index, PriceMarketingServices`
- `declaration:entity:BoerseStuttgartGmbHPriceMarketingServices` line `24` score `0.336`, recall `0.273`
  `entity BoerseStuttgartGmbHPriceMarketingServices : PriceMarketingServices`
- `assertion:fact:announcements_website` line `113` score `0.331`, recall `0.318`
  `fact announcements_website : has_url(IndexAdministratorAnnouncementsWebsite, HttpsWwwSolactiveComNewsAnnouncements) and website_of(IndexAdministratorAnnouncementsWebsite, Solactive)`
- `declaration:permission:index_distribution_to_affiliated_vendors` line `187` score `0.328`, recall `0.273`
  `permission index_distribution_to_affiliated_vendors(agent: PriceMarketingServices, target: AffiliatedVendor) action: distribute scope: Index`

### C07 `strong_candidate`

> Each vendor decides on an individual basis as to whether it will distribute or display the Index via its information systems.

- top3 token coverage: `0.833`
- review status: `unreviewed`
- uncovered by top3: `whether` (whether), `will` (will)

Candidate IR blocks:
- `assertion:constraint:vendor_decides_distribution_or_display` line `191` score `0.668`, recall `0.75`
  `constraint vendor_decides_distribution_or_display : forall v: AffiliatedVendor, forall i: Index, forall a: VendorAction, published_under_following_identifiers(i) implies individual_basis(vendor_decision(v, i, a)) and via_information_systems(vendor_decision(v, i, a), information_systems(v))`
- `declaration:rel:via_information_systems` line `91` score `0.376`, recall `0.333`
  `rel via_information_systems : VendorDecision, InformationSystem`
- `declaration:enum:VendorAction` line `16` score `0.36`, recall `0.25`
  `sort VendorAction = Distribute | Display`
- `declaration:fun:information_systems` line `78` score `0.3`, recall `0.25`
  `fun[required] information_systems : Vendor -> InformationSystem`
- `declaration:rel:individual_basis` line `90` score `0.3`, recall `0.25`
  `rel individual_basis : VendorDecision`

### C08 `strong_candidate`

> Any publication in relation to the Index (e.g.

- top3 token coverage: `1.0`
- review status: `unreviewed`
- uncovered by top3: none

Candidate IR blocks:
- `declaration:rel:publication_in_relation_to_index` line `92` score `0.9`, recall `1.0`
  `rel publication_in_relation_to_index : IndexPublication, Index`
- `assertion:constraint:index_publications_available_at_announcements_website` line `198` score `0.844`, recall `1.0`
  `constraint index_publications_available_at_announcements_website : forall p: IndexPublication, forall i: Index, publication_in_relation_to_index(p, i) implies available_at(p, IndexAdministratorAnnouncementsWebsite)`
- `declaration:opaque:IndexPublication` line `18` score `0.648`, recall `0.667`
  `sort IndexPublication`
- `declaration:subtype:GuidelineAmendment` line `20` score `0.606`, recall `0.667`
  `sort GuidelineAmendment extends IndexPublication`
- `declaration:subtype:NoticePublication` line `19` score `0.6`, recall `0.667`
  `sort NoticePublication extends IndexPublication`

### C09 `partial_candidate`

> notices, amendments to the Guideline) will be available at the website of the Index Administrator: [https://www.solactive.com/news/announcements/](https://www.solactive.com/news/announcements/) .

- top3 token coverage: `0.714`
- review status: `unreviewed`
- uncovered by top3: `notic` (notices), `amendment` (amendments), `guideline` (Guideline), `will` (will)

Candidate IR blocks:
- `assertion:fact:announcements_website` line `113` score `0.629`, recall `0.643`
  `fact announcements_website : has_url(IndexAdministratorAnnouncementsWebsite, HttpsWwwSolactiveComNewsAnnouncements) and website_of(IndexAdministratorAnnouncementsWebsite, Solactive)`
- `declaration:entity:HttpsWwwSolactiveComNewsAnnouncements` line `70` score `0.481`, recall `0.429`
  `entity HttpsWwwSolactiveComNewsAnnouncements : Url`
- `assertion:fact:equity_index_methodology_location` line `105` score `0.459`, recall `0.5`
  `fact equity_index_methodology_location : document_url(EquityIndexMethodology, HttpsWwwSolactiveComDocumentsEquityIndexMethodology) and available_on(EquityIndexMethodology, SolactiveWebsite)`
- `assertion:fact:solactive_website` line `101` score `0.371`, recall `0.357`
  `fact solactive_website : has_url(SolactiveWebsite, HttpsWwwSolactiveCom) and website_of(SolactiveWebsite, Solactive)`
- `declaration:entity:HttpsWwwSolactiveComDocumentsEquityIndexMethodology` line `68` score `0.361`, recall `0.357`
  `entity HttpsWwwSolactiveComDocumentsEquityIndexMethodology : Url`
