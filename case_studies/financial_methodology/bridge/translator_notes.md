# Financial Methodology Bridge Translator Notes

## 2026-05-09T19:55:00+02:00 — Separate source-local IR from global bridge identity

Decision: keep section-level `main_ir.a4v3` files source-local and store cross-section identity links in the global bridge layer.

Accepted:

- `sections/section_4_1/main_ir.a4v3` uses local source names: `PriceReturnIndexVersion`, `NTRIndexVersion`, `GTRIndexVersion`, `AdjustedReturnVersion`, and `SOLTCA50`.
- `bridge/main_bridge.a4v3` links those local names to canonical index entities introduced in `sections/section_1_2/main_ir.a4v3`.
- Bridge links are treated as `cross_section_identity` / `SourceAlias` / `TickerAlias`, not as local section source claims.

Rejected:

- Do not put `SolactiveTransatlanticCleanEnergyEURIndex5PercentAR` directly into section 4.1 merely to satisfy cross-section reuse.
- Do not ask a source-only judge to accept cross-section identity links unless provenance and relevant source context are included.

Rationale:

Section 4.1 says "adjusted return version", "NTR Index version", "GTR Index version", and "SOLTCA50". Section 1.2 gives the published concrete index names and identifiers. If section 4.1 directly uses the concrete section 1.2 entities, source-only semantic judges see them as extra local claims. Keeping `main_ir.a4v3` source-local and moving identity links to `bridge/main_bridge.a4v3` makes the distinction explicit:

- local translation = what this source section says;
- bridge = how this section's local symbols align with symbols from other sections.

Validation:

- This bridge decision was created after multi-judge feedback on section 4.1: the judges treated concrete section 1.2 index entities inside local 4.1 IR as over-specific additions.
- The intended follow-up is to evaluate local `main_ir.a4v3` against local `source.md`, and evaluate `bridge/main_bridge.a4v3` with cross-section context.

## 2026-05-10T16:55:00+02:00 — Bridge section 2.1 RBICS reference to Appendix 8.1 enumeration

Decision: keep `sections/section_2_1/main_ir.a4v3` and `appendix/appendix_8_1/main_ir.a4v3` source-local, and connect them in the global bridge layer.

Accepted:

- `sections/section_2_1/main_ir.a4v3` keeps the abstract source phrase `RBICSSubindustryClassification` and `IndexGuidelineAppendix`.
- `appendix/appendix_8_1/main_ir.a4v3` keeps the concrete table ontology: `RbicsSubindustry`, `Appendix8`, `RBICS`, and per-row facts.
- `bridge/main_bridge.a4v3` records `same_sort`, `same_entity`, and `same_relation` links between the abstract 2.1 vocabulary and the concrete Appendix 8.1 population.
- Relation aliases record `ReversedArgumentOrder` where 2.1 says `classification in appendix` but Appendix 8.1 says `appendix includes subindustry`, and where 2.1 says `classification of system` but Appendix 8.1 says `RBICS classifies subindustry`.

Rejected:

- Do not rename Appendix 8.1 symbols to exactly match 2.1. The appendix is a table ontology and should remain readable as a concrete enumeration.
- Do not silently assume the two local vocabularies are identical during merge. The equivalence is now explicit bridge evidence.

Rationale:

Section 2.1 uses the appendix as an eligibility reference. Appendix 8.1 is the actual list. This is a canonical bridge use case: one local entry states a requirement by reference, another local entry enumerates the referenced ontology.

## 2026-05-10T20:40:00+02:00 -- Bridge repeated cross-reference definition pattern

Decision: keep the 12 small definition entries source-local and self-contained, but record their repeated cross-reference structure in the global bridge layer.

Accepted:

- Definitions `N02`, `N03`, `N16`, `N17`, `N18`, `N20`, `N22`, `N24`, `N25`, `N28`, `N29`, and `N32` each declare a local `DefinedTerm`.
- Each entry keeps its own local referenced `DocumentPart`, such as `IntroductionSection`, `Section1_3`, `Section2_1`, or `Section5_5`.
- `bridge/main_bridge.a4v3` links the repeated `DefinedTerm` sorts and the repeated `term_shall_have_meaning_defined_in_section` relation as aliases of one merge-level pattern.
- Repeated referenced section carriers are also linked where there is genuine repetition: the six `IntroductionSection` carriers and the two `Section1_3` carriers.

Rejected:

- Do not duplicate the substantive content of the referenced section inside the definition entry.
- Do not force all definitions to import a canonical Introduction ontology before that ontology is explicitly selected.
- Do not treat `shall have the meaning...` as a local deontic obligation.

Rationale:

These definitions are cross-reference pointers. Local IR answers "where is this term defined?", not "what is the full content of that definition?". The bridge prevents us from forgetting that the repeated local declarations are the same merge pattern, while preserving the source-local discipline of each definition entry.

Follow-up:

When Introduction is translated, add bridge links from placeholders such as `N17_IndexTerm` and `N03_BMRTerm` to the canonical Introduction entities if the source supports those identities.

## 2026-05-17T00:00:00+02:00 -- Bridge recent manual definitions before merge

Decision: add a pre-merge bridge pass for the manually translated definitions `N07`, `N08`, `N09`, `N10`, `N12`, `N13`, `N14`, `N23`, `N26`, `N27`, `N30`, and `N31`.

Accepted:

- Safe same-arity aliases are formal bridge links, e.g. `N07_closing_price` to `N08_closing_price`, `N07_respective_exchange` to `N08_respective_exchange` / `N31_respective_exchange`, and `N12_share_class` to `N13_share_class`.
- Calendar carriers are aligned as sort aliases where they have the same source role: `SelectionDay`, `RebalanceDay`, `TradingDay`, and `RegularRebalanceDay` families.
- `N10_respective_exchange_for_index_component` is a scoped relation alias of the one-argument `respective_exchange` functions, because N10 carries an explicit `Index` argument.
- `N30_TradingDayContext` is only `RelatedConcept` to the simpler `TradingDay` sorts. It is not a sort alias because N30 intentionally reifies the Trading Day definition as a context object.
- `N14_GbsIndexUniverse` is a sort alias of section 2.1's `GbsIndexUniverse`, but only `RelatedConcept` to N23's generic `IndexUniverse`.
- Drift is represented explicitly with `UnresolvedDrift` rather than hidden by name matching.
- `N31_trading_price` is linked to section 1.4's `current_trading_price` only as `RelatedConcept`, because section 1.4 adds intraday calculation scope.
- `N07_last_trading_price` is bridged to section 1.4's `last_available_trading_price` as a Medium-confidence `RelationAlias`: both use `(IndexComponent, TradingDay) -> TradingPrice`, but the source wording differs.
- `N07_closing_price_available` and section 1.4's `current_trading_price_available` are only `RelatedConcept`, because they gate different fallback branches.

Rejected:

- Do not merge every relation with the same surface name. `sourced_from_data_vendor` has different first-argument types in N12 and N13, so it remains drift until the merge layer chooses a higher-level vendor-source pattern.
- Do not directly merge `section_4_1.index_component_of(Index, CalculationDay, IndexComponent)` with `section_4_7.index_component_of(IndexComponent, Index)`. The section 4.1 relation is calculation-day scoped; the section 4.7 relation is not.
- Do not bridge NYSE/LSE/EUREX/TSE to `Reuters` or `IntercontinentalExchange`. In these local IR files, the first group are trading venues; the second group are rate/fixing providers.

Rationale:

Bridge and merge are deliberately separate. The bridge records identity, alias, scoped-alias, related-concept, and unresolved-drift decisions. The merge step should consume those decisions instead of guessing from identifier similarity.

Automatic checks:

- The bridge file should parse as A4V3.
- Every `BridgeSymbol` should have at least one `bridge_declared_in` location.
- Every `same_sort`, `same_entity`, `same_index`, or `same_relation` pair should have `bridge_link_type` and `bridge_confidence`.
- Every `same_relation` pair should have `bridge_argument_order`.
- `UnresolvedDrift` links should be allowed, but should not be silently treated as `same_relation` by merge tooling.
- `bridge_candidate_audit_v1` should be run as a heuristic pre-merge search over IR declarations, assertion identifiers, and repeated source phrases. Its output is a review backlog, not an automatic merge instruction.

## 2026-05-17T00:30:00+02:00 -- Add BridgeFamily layer for high-cardinality repeated symbols

Decision: add a `BridgeFamily` layer for repeated local symbols that recur across many entries and would be noisy or fragile as pairwise all-to-all links.

Accepted:

- `TheIndexLocalPlaceholderFamily` groups repeated local `TheIndex` placeholders. This is a local-placeholder identity family, not a claim that each local `TheIndex` is a separate published index variant.
- Shared document/web infrastructure is grouped explicitly: `SolactiveWebsiteFamily`, URL families, and `GenericDocumentAvailabilityRelationFamily`.
- Shared core vocabulary is grouped explicitly: `Security`, `IndexComponent`, `IndexLevel`, `SolactiveOrganization`, `CorporateAction`, `Notice`, `Region`, `ISIN`, `Policy`, `IndexRule`, and similar families.
- Same-name but different-signature items are not blindly merged. Where the relationship is safe but scoped, the bridge uses `RelatedConcept`, `ScopedRelationAlias`, or `UnresolvedDrift` instead of a hard alias.
- `Canada` and `UnitedStates` are `RelatedConcept` families because section 2.1 and section 2.2 type them differently (`GbsIndexUniverseClassification` versus `CountryAssignment`).
- `IndexQuality` is a `RelatedConcept` family because the enum values differ across sections; merge should align overlapping values such as `Comparability` deliberately.

Rejected:

- Do not infer bridge links only from source text recurrence. Repeated source phrases are discovery candidates, not merge instructions.
- Do not make `index_component`, `index_universe`, or older unary `incorporated_by_reference` relations aliases solely because their names repeat; their signatures and scopes differ and need separate semantic review.
- Do not collapse `Region` functions in section 2.2 and section 2.3 as identical functions. They are related but have different argument structure.

Validation:

- `bridge_lint_v1` now checks family anchors, members, link types, and confidence values.
- `bridge_candidate_audit_v1` scans repeated declarations, same-name/different-signature declarations, repeated source phrases, and external-looking identifiers used inside fact/constraint bodies.
- Current pre-merge audit result after the family layer: `unbridged_repeated_exact_count = 0`, `assertion_external_identifier_count = 0`.

Rationale:

Bridge is not the same thing as merge. The bridge should make cross-entry identity and drift decisions visible enough that merge can be deterministic and auditable. The family layer gives us that visibility without forcing hundreds of pairwise links.

## 2026-05-17T01:05:00+02:00 -- Add canonical merge expansion families

Decision: extend the bridge with canonical merge-expansion families for repeated
core symbols that were still visible in the merge-readiness audit.

Accepted:

- `CanonicalIndexSortFamily` aligns repeated local `Index` sort declarations.
- `CanonicalSolactiveEntityFamily` aligns repeated local `Solactive` entities.
- `CanonicalIndexAdministratorSortFamily`, `CanonicalCalculationDaySortFamily`,
  `CanonicalSelectionDaySortFamily`, `CanonicalPriceSortFamily`,
  `CanonicalGbsIndexSortFamily`, `CanonicalIndexTypeSortFamily`,
  `CanonicalEffortSortFamily`, and `CanonicalIndexMethodologySortFamily` align
  repeated sort-level carriers needed for canonical merge.
- Section 1.3's concrete index entities are declared as bridge indices so that
  the initial-level section can be connected to the published variants from
  section 1.2 and the index-version bridge from section 4.1.
- `CanonicalIndexComponentRelationFamily` and
  `CanonicalIndexUniverseRelationFamily` are `RelatedConcept`, not exact
  relation aliases, because their local arity and scope differ by section.
- Legacy unary `incorporated_by_reference` is a related concept to the newer
  binary `incorporated_by_reference_into` pattern, not an exact alias.

Rejected:

- Do not mechanically merge every repeated `index_component` or
  `index_universe` relation into one predicate. Merge should project these into
  canonical role-aware relations.
- Do not treat section-reference entities such as `Section2_1` and `Section2_2`
  as domain concepts. They are document pointers and remain separated from
  business ontology concepts.

Validation:

- `bridge_lint_v1`: passed with 0 hard and 0 soft findings.
- `bridge_candidate_audit_v1`: 0 parser warnings, 0 unbridged repeated exact
  declarations, 0 assertion external identifiers.
- `merge_readiness_audit_v1`: passed with review items only; remaining findings
  are the deliberate same-name/different-signature review bucket and the
  lexical/source-phrase review bucket.

## 2026-05-17T02:10:00+02:00 -- Add frame projection bridge for value observations

Decision: add an initial OWL-friendly projection layer for local value-bearing
functions and relations.

Accepted:

- Bridge now has `BridgeFrame` and `BridgeRole` carriers for observation-style
  mappings. These are not local source symbols; they are integration targets
  for the canonical ontology and future RDF/OWL lowering.
- Local price/value functions such as `closing_price`, `trading_price`,
  `daily_value_traded`, `average_daily_value_traded`, `initial_level`,
  `index_level`, `free_float`, `share_count`, `index_currency`, and
  `respective_exchange` project to explicit observation frames.
- Argument positions are mapped to short roles such as
  `ObservationSubjectRole`, `ObservationDayContextRole`,
  `ObservationSelectionDayContextRole`, `ObservationIndexRole`, and observed
  value roles.
- Projection compatibility does not imply exact aliasing. For example,
  section 1.4 `closing_price(IndexComponent, CalculationDay)` and definition
  N07 `closing_price(IndexComponent, TradingDay)` both project to
  `ClosingPriceObservationFrame`, but only same-signature definition pairs are
  marked as high-confidence `RelationAlias`.

Rejected:

- Do not flatten all local functions into one renamed canonical function.
- Do not erase meaningful context differences such as `TradingDay` versus
  `CalculationDay`; the projection frame records them as role-compatible, not
  necessarily identical.

Validation:

- `bridge_lint_v1` now validates projection frames, roles, relation targets,
  argument positions, and projection confidence.

## 2026-05-17T02:35:00+02:00 -- Add second observation projection batch

Decision: extend the frame projection bridge to cover weight, region, component
price, and float market capitalization observations.

Accepted:

- `section_2_3.weight` and `section_4_1.component_weight` project to
  `ComponentWeightObservationFrame`.
- `section_2_2.free_float_market_capizatlization` projects to
  `FreeFloatMarketCapitalizationObservationFrame`. The local source explicitly
  says "Free Float Market Capizatlization", so this is the FFMC concept despite
  the typo.
- `section_2_3.float_market_capizatlization` projects to
  `FreeFloatMarketCapitalizationObservationFrame` with High confidence. The
  section 2.3 phrase "Float Market Capizatlization" is interpreted as
  shorthand for the Free Float Market Capitalization value defined in N13 and
  used for ranking in section 2.2.
- `section_2_2.region` and `section_2_3.region` project to
  `RegionClassificationObservationFrame`.
- `section_4_1.component_price` projects to `ComponentPriceObservationFrame`.
- `section_4_1.component_price_change` projects to
  `PriceChangeObservationFrame`.

Architecture note:

- `BridgeFrame` names intentionally mirror `CanonicalFrame` names. They are
  bridge-local handles for canonical frame targets, not new domain concepts.

## 2026-05-17T03:05:00+02:00 -- Add index-component membership state projections

Decision: model repeated `index_component` / `index_component_of` symbols as
membership states rather than exact same relations.

Accepted:

- Canonical `IndexComponent` is treated as a role assignment, not as a subtype
  of `Security`. The underlying instrument is connected through a security
  role, and the component-role object is connected through an assignment role.
- Definition N19 and section 4.7 project to
  `GenericIndexComponentMembershipFrame`: they state that a security/component
  is an Index Component of an Index without a day-specific lifecycle context.
- Section 2.2 projects to `SelectionDayIndexComponentMembershipFrame`: it
  records the selection-day state where a security has been selected for index
  inclusion.
- Sections 1.4 and 4.1 project to
  `CalculationDayIndexComponentMembershipFrame`: they describe component
  membership in calculation/formula contexts.
- Projection roles distinguish `MembershipSecurityRole`,
  `MembershipComponentAssignmentRole`,
  `MembershipIndexRole`, `MembershipSelectionDayRole`, and
  `MembershipCalculationDayRole`.
- The earlier generic `MembershipComponentRole` was removed after this split,
  because it no longer carried enough semantic information for merge readers.

Rejected:

- Do not merge all local `index_component` declarations into one binary
  predicate. Their arity differences encode real lifecycle context, not just
  syntactic drift.

Merge note:

- Projection to a membership frame is weaker than an exact alias. It gives the
  merge layer enough structure to reason about lifecycle states while keeping
  local source-faithful formulas untouched.

## 2026-05-17T17:05:00+02:00 -- Clarify eligible rebalance day and frame count

Decision: keep `EligibleRebalanceDay` as an eligibility day, not as a subtype of
actual `RebalanceDay`.

Reason:

- N09 defines eligibility across exchanges.
- N26 defines the actual Rebalance Day by selecting the scheduled day if it is
  eligible, or the immediately following eligible day otherwise.
- Therefore eligibility is an input condition for the rebalance-day rule, not
  itself the actual rebalance-day state.

Also confirmed:

- The bridge/canonical frame count is 18 intentionally. There is no separate
  `FloatMarketCapitalizationObservationFrame`; section 2.3's "Float Market
  Capizatlization" is projected to `FreeFloatMarketCapitalizationObservationFrame`
  because N13 defines the FFMC value used by the selection and weighting steps.

## 2026-05-17T03:35:00+02:00 -- Add process-critical calendar bridge

Decision: add explicit bridge families for calendar concepts needed by the
future process/workflow layer.

Accepted:

- `BusinessDayProcessFamily` links N04 `business_day` with N27
  `business_day_count_before`, `BusinessDayCount`, and `TwentyBusinessDays`.
  This records that Selection Day counting depends on the Business Day
  definition without treating a predicate, a count function, and a numeric
  entity as exact aliases.
- `CloseOfBusinessProcessFamily` links N06 `CloseOfBusiness` with section 3.1
  `CloseOfBusiness` / `close_of_business_on_day`. This is a related-concept
  bridge because N06 models the term as a calculation time while section 3.1
  uses it as a rebalance timing marker.
- `FixingDayProcessFamily` links N11 `fixing_day` / `selection_day` with
  section 3.1 `FixingDay` and `fixing_day_of_rebalance`.

Rejected:

- Do not exact-merge N06 `CloseOfBusiness` and section 3.1
  `CloseOfBusiness`. The former is a term-definition calculation time; the
  latter is an event/time-marker carrier for workflow.

## 2026-05-17T03:55:00+02:00 -- Review remaining uncovered lexical candidates

Decision: close the seven lexical candidates that were not covered by bridge
symbol guesses.

Exact aliases accepted:

- Section 2.1 `SolactiveGBSBenchmarkSeriesPdf` and definition N14
  `SolactiveGBSBenchmarkSeriesGuideline` are the same referenced GBS Benchmark
  Series document. The sources use the same PDF path; N14 omits `www`.
- Section 2.1
  `HttpsWwwSolactiveComDownloadsGuidelineSolactiveGBSBenchmarkSeriesPdf` and
  N14 `HttpsSolactiveComDownloadsGuidelineSolactiveGBSBenchmarkSeriesPdf` are
  URL aliases for the same PDF path.
- Section 2.2 `FreeFloatMarketCapizatlization` and section 2.3
  `FloatMarketCapizatlization` are aliases for the same FFMC value. The
  difference is local wording/context: section 2.2 ranks eligible securities by
  FFMC, while section 2.3 weights selected Index Components by the same
  capitalization measure.
- Section 4.6 `VarietyReasons` and section 4.7 `VarietyOfReasons` are the
  same vague source phrase family.

Related-only decisions:

- `section_1_3_index` and `section_4_1_index` are both section-local index
  scope predicates, but they are not exact aliases. The index entities are
  bridged separately.
- Section 4.4 `adjustment_of_index` and section 4.5 `adjustment_to_index` are
  related adjustment-to-index relations, but one is a generic index adjustment
  and the other is a corporate-action adjustment.
- N15 `security_reflected_in_gbs_index` and N19 `security_reflected_in_index`
  are related reflection relations, but N15 targets the GBS Index while N19
  targets the methodology Index.

## 2026-05-17T04:25:00+02:00 -- Add fuzzy-audit bridge aliases

Decision: close additional fuzzy candidates found by manual semantic review.

Accepted:

- N13 `FreeFloatMarketCapitalization` and section 2.2
  `FreeFloatMarketCapizatlization` are the same FFMC sort. Section 2.2 keeps
  the source typo in the local IR name.
- N13 `free_float_market_capitalization` and section 2.2
  `free_float_market_capizatlization` are the same FFMC observation function
  with the same argument order.
- Section 4.2 `announcement_by` and section 4.4 `announced_by` are the same
  announcement-agent relation under noun/past-participle naming variation.
- Section 4.2 `announcement_under_section` and section 4.4
  `announced_under_section` are the same announcement-section relation under
  noun/past-participle naming variation.
- Section 4.4 `AnnouncementsSection` is an alias of the existing
  `AnnouncementSectionFamily`.

Rejected:

- Do not bridge section 4.1 `EffectiveDate` and section 4.4 `EffectiveDay` as
  exact aliases. Section 4.1 uses an ex-date/effective-date concept for
  dividend/payment treatment; section 4.4 uses a notice implementation day.
- Do not bridge N12 `Share` and section 3.1 `Shares` as exact aliases. N12
  models individual share units for free-float counting; section 3.1 models
  implementing shares for rebalance execution.
- Do not bridge `Index` and `GbsIndex` by lexical similarity. `GbsIndex`
  belongs to the Solactive GBS Benchmark Series reference ontology; `Index`
  is the methodology's own index/family/variant concept. Only specific
  relations such as GBS Index Universe references are bridged.
- Do not bridge section 1.4 `CalculationMode` with section 5.3
  `CalculationMethod`. The former classifies intraday/closing calculation
  timing; the latter is the described methodology applied to composition and
  calculation.
- Do not bridge N06 `CalculationTime` with section 1.4 `CalculationMode`.
  Time and mode are separate carriers even when both appear in calculation
  clauses.
