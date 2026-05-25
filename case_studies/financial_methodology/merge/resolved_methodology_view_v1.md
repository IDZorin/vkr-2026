# Resolved Methodology View v1

Status: `generated`

This is a derived inspection view, not a rewritten merged IR.
The source of truth remains local `main_ir.a4v3` files plus provenance, bridge, and canonical ontology.

## Summary

- `entry_count`: 55
- `local_declaration_count`: 1531
- `resolved_declaration_count`: 442
- `local_only_declaration_count`: 1089
- `assertion_or_deontic_count`: 373
- `bridge_family_count`: 68
- `bridge_symbol_count`: 442
- `bridge_pair_group_count`: 38
- `bridge_frame_count`: 18
- `bridge_role_count`: 27
- `bridge_projection_count`: 40
- `canonical_declaration_count`: 227
- `canonical_subtype_edge_count`: 75

## Resolution Counts

- `bridge_family`: 282
- `bridge_pair_group`: 107
- `declared_bridge_symbol`: 53
- `local_only`: 1089

## Top Bridge Families

- `GenericDocumentAvailabilityRelationFamily`: 29 local declarations; link_type `RelationAlias`; confidence `High`
- `CanonicalIndexSortFamily`: 24 local declarations; link_type `SortAlias`; confidence `High`
- `TheIndexLocalPlaceholderFamily`: 17 local declarations; link_type `EntityAlias`; confidence `High`
- `CoreIndexComponentSortFamily`: 13 local declarations; link_type `SortAlias`; confidence `High`
- `CanonicalSolactiveEntityFamily`: 11 local declarations; link_type `EntityAlias`; confidence `High`
- `SolactiveWebsiteFamily`: 11 local declarations; link_type `EntityAlias`; confidence `High`
- `CoreSecuritySortFamily`: 9 local declarations; link_type `SortAlias`; confidence `High`
- `CanonicalSelectionDaySortFamily`: 7 local declarations; link_type `SortAlias`; confidence `High`
- `CanonicalIndexAdministratorSortFamily`: 5 local declarations; link_type `SortAlias`; confidence `High`
- `EquityIndexMethodologyFamily`: 5 local declarations; link_type `EntityAlias`; confidence `High`
- `IndexLevelSortFamily`: 5 local declarations; link_type `SortAlias`; confidence `High`
- `SolactiveOrganizationSortFamily`: 5 local declarations; link_type `SortAlias`; confidence `High`
- `SectionReferenceEntityFamily`: 5 local declarations; link_type `RelatedConcept`; confidence `Medium`
- `NewsAnnouncementsUrlFamily`: 4 local declarations; link_type `EntityAlias`; confidence `High`
- `CanonicalPriceSortFamily`: 4 local declarations; link_type `SortAlias`; confidence `High`
- `AverageDailyValueTradedFamily`: 4 local declarations; link_type `RelatedConcept`; confidence `High`
- `FixingDayProcessFamily`: 4 local declarations; link_type `RelatedConcept`; confidence `High`
- `CloseOfBusinessProcessFamily`: 4 local declarations; link_type `RelatedConcept`; confidence `Medium`
- `CanonicalIndexMethodologySortFamily`: 4 local declarations; link_type `SortAlias`; confidence `High`
- `ThisGuidelineFamily`: 4 local declarations; link_type `EntityAlias`; confidence `High`

## Projection Frames

- `IndexCurrencyObservationFrame`: 4 local declarations project to this frame
- `TradingPriceObservationFrame`: 4 local declarations project to this frame
- `ClosingPriceObservationFrame`: 4 local declarations project to this frame
- `ExchangeObservationFrame`: 4 local declarations project to this frame
- `FreeFloatMarketCapitalizationObservationFrame`: 3 local declarations project to this frame
- `IndexLevelObservationFrame`: 3 local declarations project to this frame
- `CalculationDayIndexComponentMembershipFrame`: 2 local declarations project to this frame
- `AverageDailyValueTradedObservationFrame`: 2 local declarations project to this frame
- `RegionClassificationObservationFrame`: 2 local declarations project to this frame
- `ComponentWeightObservationFrame`: 2 local declarations project to this frame
- `GenericIndexComponentMembershipFrame`: 2 local declarations project to this frame
- `DailyValueTradedObservationFrame`: 2 local declarations project to this frame
- `InitialIndexLevelObservationFrame`: 1 local declarations project to this frame
- `SelectionDayIndexComponentMembershipFrame`: 1 local declarations project to this frame
- `ComponentPriceObservationFrame`: 1 local declarations project to this frame
- `PriceChangeObservationFrame`: 1 local declarations project to this frame
- `FreeFloatObservationFrame`: 1 local declarations project to this frame
- `ShareCountObservationFrame`: 1 local declarations project to this frame

## Canonical Ontology Snapshot

- `entity`: 64
- `rel`: 67
- `sort`: 96

## Rule Dependency View

Each assertion/deontic block keeps its local text, but this report records which local declarations it touches and how those declarations resolve via bridge/canonical layers.

- `BridgePairGroup:Appendix8_1_RBICS`: used by 109 local rule dependencies
- `BridgePairGroup:Appendix8_1_Appendix8`: used by 109 local rule dependencies
- `BridgePairGroup:Appendix8_1_appendix_includes_rbics_subindustry`: used by 109 local rule dependencies
- `BridgePairGroup:Appendix8_1_rbics_classifies_subindustry`: used by 109 local rule dependencies
- `Local:Appendix8_1_rbics_classification_level`: used by 108 local rule dependencies
- `Local:Appendix8_1_rbics_number_code`: used by 108 local rule dependencies
- `Local:Appendix8_1_rbics_subindustry_name`: used by 108 local rule dependencies
- `BridgeFamily:TheIndexLocalPlaceholderFamily`: used by 44 local rule dependencies
- `BridgeFamily:CoreIndexComponentSortFamily`: used by 36 local rule dependencies
- `BridgeFamily:CanonicalSelectionDaySortFamily`: used by 35 local rule dependencies
- `BridgeFamily:CanonicalSolactiveEntityFamily`: used by 33 local rule dependencies
- `BridgeFamily:GenericDocumentAvailabilityRelationFamily`: used by 30 local rule dependencies
- `BridgeFamily:CanonicalIndexSortFamily`: used by 24 local rule dependencies
- `BridgeFamily:SolactiveWebsiteFamily`: used by 20 local rule dependencies
- `BridgeFamily:CanonicalCalculationDaySortFamily`: used by 19 local rule dependencies
- `BridgeFamily:EquityIndexMethodologyFamily`: used by 18 local rule dependencies
- `BridgeFamily:CoreSecuritySortFamily`: used by 16 local rule dependencies
- `BridgeFamily:CanonicalIndexComponentRelationFamily`: used by 13 local rule dependencies
- `BridgePairGroup:N02_term_shall_have_meaning_defined_in_section`: used by 12 local rule dependencies
- `BridgeFamily:IndexCurrencyFunctionFamily`: used by 11 local rule dependencies
- `BridgePairGroup:N26_RebalanceDay`: used by 10 local rule dependencies
- `BridgeSymbol:N30_TradingDayContext`: used by 10 local rule dependencies
- `BridgePairGroup:N12_ShareClass`: used by 9 local rule dependencies
- `BridgeFamily:CalculationTimeSortFamily`: used by 8 local rule dependencies
- `BridgeFamily:AnnouncementSectionFamily`: used by 8 local rule dependencies

## Review Prompts

No local-only core-like symbols in the capped prompt set.

## Interpretation

Bridge/canonical resolution makes cross-fragment references inspectable, but it is still a view. Process/workflow rules and operational lowering remain separate layers.
