# Section 1.2 Translator Notes

This file records translator decisions for the current `main_ir.a4v3`.
It is review memory, not an additional source of methodology claims.

## Changelog

### 2026-05-09T12:49:35+02:00

Decision: keep section 1.2 local publication examples as relation predicates, but mark them as merge-level ontology candidates.

Accepted:

- `notice_publication_in_relation_to_index(...)` stays in section 1.2 as a local publication-relation predicate.
- `guideline_amendment_publication_in_relation_to_index(...)` stays in section 1.2 as a local publication-relation predicate.
- Cross-section review found later behavior for both concepts:
  - section 4.4 uses `Notice` with notice-period / affected-component / effective-day behavior;
  - section 5.5 uses `GuidelineAmendment` with possible-result and document-amendment behavior.
- These are therefore `global_ontology_candidate` concepts for the merge layer.

Rejected / alternatives:

- Do not reintroduce local `NoticePublication` / `GuidelineAmendment` subtypes in section 1.2 solely because the words occur elsewhere.
- Do not silently rewrite the local section 1.2 gold IR to anticipate merge. The local IR should remain source-local.

Rationale: in section 1.2, notices and amendments are only examples of publications available at the announcements website. Later sections give these words real behavior. The right split is: keep 1.2 local and clean, then add merge bridges from the section 1.2 relation predicates to the global `Notice` / `GuidelineAmendment` ontology concepts.

### 2026-05-09T11:18:23+02:00

Decision: remove remaining over-strong universal distribution and redundant publication-example constraints.

Accepted:

- `may be distributed to all affiliated vendors` is carried by `permission index_distribution_to_affiliated_vendors(...)`; no separate hard constraint now asserts that every listed index is actually available to every affiliated vendor.
- The permission agent is `PriceMarketingServices`, not generic `Organization`, to avoid granting unrelated organizations the same distribution permission.
- Vendor discretion is represented as a descriptive `fact vendor_decides_distribution_or_display`, not as a hard constraint making the decision relation an admissibility condition.
- `notices` and `amendments to the Guideline` are represented as alternative publication-in-relation predicates inside the single announcement-website rule. This keeps the source examples traceable without creating duplicate rules for the same announcement-location claim.

Rejected / alternatives:

- Do not keep `distribution_to_affiliated_vendor_available(i, v)` as a hard universal relation. It overstates `may be distributed` as actual availability for every affiliated vendor.
- Do not model `notices` and `amendments` as separate subtypes with separate announcement constraints unless the section later needs subtype-specific behavior.

Rationale: the previous version passed deterministic clean gate and single semantic judge, but the multi-judge panel consistently flagged distribution/vendor rules as too strong. This revision keeps the same source evidence while avoiding obligation-like readings for an explicitly permissive sentence.

### 2026-05-09T10:58:00+02:00

Decision: soften over-strong publication/vendor encodings while preserving row-level identifier evidence.

Accepted:

- Table attribute functions (`index_name`, `index_isin`, `index_currency`, `index_type`, `index_type_identifier`, `index_ric`) are `fun[optional]`, not `fun[required]`. The source gives values for the listed rows, but does not state a total schema for every possible `Index`.
- The blank BBG ticker in the NTR row is represented by omission of a `bbg_ticker(...)` fact, not by a hard closed-world `not exists` constraint.
- Publication on Solactive and availability via Boerse Stuttgart are represented as explicit facts for the five listed index variants, rather than as a universal rule over any future `Index` marked by `published_under_following_identifiers`.
- `may be distributed to all affiliated vendors` is represented by both a minimal `permission` carrier for the `may be` modality and `distribution_to_affiliated_vendor_available(i, v)` for the descriptive availability relation.
- Vendor discretion is represented by an existential `VendorDistributionOrDisplayDecision` with individual-basis and information-system links. This avoids the previous over-strong `forall VendorAction` reading.
- The examples `notices` and `amendments to the Guideline` are represented as `NoticePublication` and `GuidelineAmendment` subtypes, and are used in example-specific announcement-availability constraints so the declarations are not dead.

Rejected / alternatives:

- Do not assert `ntr_has_no_bbg_ticker` as hard negation from a blank table cell. The table omission is enough for this local ledger unless a closed-world export explicitly requires it.
- Do not require every vendor/action pair to have a decision. The source says each vendor decides whether it will distribute or display, not that every action is positively decided.
- Do not keep subtype declarations for examples if no formula uses them. If the examples are declared, they must participate in formula bodies.

Rationale: these edits keep the same source coverage but reduce over-formalization flagged by the multi-judge panel: total functions, hard negation for the blank BBG cell, universal publication/channel constraints, and vendor-decision totality. The deontic permission remains because the clean gate treats `may be` as a required A4V3 family signal.

### 2026-05-06T17:27:25+02:00

Decision: represent section 1.2 as an identifier/publication ledger plus publication and distribution obligations.

Accepted:

- Each published index row is represented as an `Index` entity with explicit name, ISIN, currency, type, RIC, and optional BBG ticker facts.
- `IndexType` and `IndexTypeIdentifier` are separated so PR/NTR/GTR/AR are mapped by explicit equalities instead of a vague `means` relation.
- The missing BBG ticker for the NTR row is represented negatively by `ntr_has_no_bbg_ticker`.
- AR variants are split by source evidence: 50 AR uses `formula_specified_in(..., Section4)`, while the 5% AR row remains tied to the Equity Index Methodology wording.
- Exact URLs are preserved as URL entities and `document_url` / `has_url` facts.
- Distribution to affiliated vendors is represented as `permission`, not as a hard fact that every vendor actually receives or displays the Index.
- Vendor behavior is represented by a choice space `VendorAction = Distribute | Display` and `vendor_decision`.

Rejected / alternatives:

- Do not create a first-class calculation algorithm from `calculated as`; the section points to methodology/formula references but does not specify the algorithm locally.
- Do not treat `whether` or `will` as separate temporal/deontic rules beyond the vendor choice and publication availability structures.
- Do not ignore URLs: exact URL preservation is part of the local claim.

Rationale: the section is mostly tabular identifiers and publication availability. The chosen IR preserves row-level facts, optional/missing ticker information, document references, vendor permission, and exact URLs without inventing calculation mechanics.

Waiver rationale:

- `means` is absorbed by explicit identifier-to-type mappings.
- `calculated` is absorbed by type and document/formula references.
- `in addition`, `whether`, and `will` are discourse/choice/modality surface forms already represented by the structure.
- `distributed` is represented by the deontic permission with `action: distribute`.

Validation:

- clean gate: accepted
- phrase coverage: 12/12
- token accounted coverage: 70/70
- exact URLs: 3/3
- waivers: 6/6
