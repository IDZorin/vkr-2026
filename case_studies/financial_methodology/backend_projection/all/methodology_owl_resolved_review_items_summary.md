# Financial Methodology OWL Resolved Review Items v1

This report explains why the remaining bridge links were not promoted to strong OWL identity/equivalence axioms.
It is not a waiver dump: each item is either an adapter case, a relation-family case without pairwise argument-order evidence, or a related-concept family that is intentionally weaker than identity.

## Summary

- Strong identity/equivalence axioms emitted: `957`
- Adapter / non-identity decisions closed: `475`
- Review items: `0`
- Resolved decision policy counts: `{"resolved_as_scoped_projection_adapter": 1, "resolved_as_inverse_adapter": 3, "resolved_as_domain_specialized_relation": 2, "resolved_as_projection_family": 12, "resolved_as_non_identity_related_concept": 40, "resolved_as_pairwise_signature_equivalence": 117, "resolved_as_family_split": 300}`
- Resolved decision attention counts: `{"high": 16, "medium": 459}`
- Open review policy counts: `{}`
- Open review attention counts: `{}`

## Resolution Policy

- `not_equivalent_property`: the bridge has a relation alias, but OWL property equivalence would be dishonest because argument order or arity differs.
- `family_relation_review_only`: the bridge groups relations into a family, but the family does not provide pairwise argument-order evidence for every pair.
- `family_review_only`: the bridge explicitly says `RelatedConcept` or another non-identity link type, so the resolved graph keeps it as a review/related link.

## Closed Adapter / Non-Identity Decisions

| Family | Decisions | Attention | Policies | Why Closed | Samples |
| --- | ---: | --- | --- | --- | --- |
| `GenericDocumentAvailabilityRelationFamily` | 406 | `medium:406` | `resolved_as_family_split:300, resolved_as_pairwise_signature_equivalence:106` | family relation pair has matching local name and exact local signature | `Section1_2_available_on ↔ Section1_2_website_of; Section1_2_available_on ↔ Section3_1_available_on; Section1_2_available_on ↔ Section3_1_incorporated_by_reference_into` |
| `SectionReferenceEntityFamily` | 10 | `medium:10` | `resolved_as_non_identity_related_concept:10` | SectionReferenceEntityFamily has non-identity link type and is resolved below OWL equality | `N06_Section1_4 ↔ N14_Section2_1; N06_Section1_4 ↔ N15_Section2_1; N06_Section1_4 ↔ Section3_1_Section2_1` |
| `AverageDailyValueTradedFamily` | 6 | `high:6` | `resolved_as_projection_family:6` | AverageDailyValueTradedFamily has non-identity link type and is resolved below OWL equality | `N01_AverageDailyValueTraded ↔ N01_average_daily_value_traded; N01_AverageDailyValueTraded ↔ Section2_1_AverageDailyValueTraded; N01_AverageDailyValueTraded ↔ Section2_1_average_daily_value_traded` |
| `BusinessDayProcessFamily` | 6 | `medium:6` | `resolved_as_non_identity_related_concept:6` | BusinessDayProcessFamily has non-identity link type and is resolved below OWL equality | `N04_business_day ↔ N27_BusinessDayCount; N04_business_day ↔ N27_TwentyBusinessDays; N04_business_day ↔ N27_business_day_count_before` |
| `CloseOfBusinessProcessFamily` | 6 | `medium:6` | `resolved_as_non_identity_related_concept:6` | CloseOfBusinessProcessFamily has non-identity link type and is resolved below OWL equality | `N06_CloseOfBusiness ↔ N06_calculation_time_of_closing_level_of_index; N06_CloseOfBusiness ↔ Section3_1_CloseOfBusiness; N06_CloseOfBusiness ↔ Section3_1_close_of_business_on_day` |
| `DailyValueTradedFamily` | 6 | `medium:6` | `resolved_as_non_identity_related_concept:6` | DailyValueTradedFamily has non-identity link type and is resolved below OWL equality | `N01_DailyValueTraded ↔ N01_daily_value_traded; N01_DailyValueTraded ↔ N08_DailyValueTraded; N01_DailyValueTraded ↔ N08_daily_value_traded` |
| `FixingDayProcessFamily` | 6 | `medium:6` | `resolved_as_non_identity_related_concept:6` | FixingDayProcessFamily has non-identity link type and is resolved below OWL equality | `N11_fixing_day ↔ N11_selection_day; N11_fixing_day ↔ Section3_1_FixingDay; N11_fixing_day ↔ Section3_1_fixing_day_of_rebalance` |
| `(direct pair)` | 4 | `high:4` | `resolved_as_scoped_projection_adapter:1, resolved_as_inverse_adapter:3` | bridge records ReversedArgumentOrder for binary relations | `N07_respective_exchange ↔ N10_respective_exchange_for_index_component; N27_selection_day_for_rebalance_day ↔ Section3_1_selection_day_of_rebalance; Section2_1_rbics_subindustry_classification_in_appendix ↔ Appendix8_1_appendix_includes_rbics_subindustry` |
| `CanonicalIndexComponentRelationFamily` | 3 | `high:3` | `resolved_as_projection_family:3` | CanonicalIndexComponentRelationFamily has non-identity link type and is resolved below OWL equality | `N19_index_component ↔ Section1_4_index_component; N19_index_component ↔ Section2_2_index_component; Section1_4_index_component ↔ Section2_2_index_component` |
| `IndexCurrencyFunctionFamily` | 3 | `medium:3` | `resolved_as_pairwise_signature_equivalence:3` | family relation pair has matching local name and exact local signature | `Section1_2_index_currency ↔ Section1_4_index_currency; Section1_2_index_currency ↔ Section4_1_index_currency; Section1_4_index_currency ↔ Section4_1_index_currency` |
| `IndexOfRelationFamily` | 3 | `medium:3` | `resolved_as_pairwise_signature_equivalence:3` | family relation pair has matching local name and exact local signature | `Section4_6_index_of ↔ Section4_7_index_of; Section4_6_index_of ↔ Section5_4_index_of; Section4_7_index_of ↔ Section5_4_index_of` |
| `AnnouncementOnRelationFamily` | 1 | `medium:1` | `resolved_as_domain_specialized_relation:1` | AnnouncementOnRelationFamily reuses the same predicate wording over different domain carriers | `Section4_2_announced_on ↔ Section4_4_announced_on` |
| `CanadaClassificationFamily` | 1 | `medium:1` | `resolved_as_non_identity_related_concept:1` | CanadaClassificationFamily has non-identity link type and is resolved below OWL equality | `Section2_1_Canada ↔ Section2_2_Canada` |
| `CanonicalIndexUniverseRelationFamily` | 1 | `high:1` | `resolved_as_projection_family:1` | CanonicalIndexUniverseRelationFamily has non-identity link type and is resolved below OWL equality | `Section2_1_index_universe ↔ Section2_2_index_universe` |
| `FullyRuleBasedRelationFamily` | 1 | `medium:1` | `resolved_as_domain_specialized_relation:1` | FullyRuleBasedRelationFamily reuses the same predicate wording over different domain carriers | `Section2_1_fully_rule_based ↔ Section2_2_fully_rule_based` |
| `GbsIndexSpecifiedInSectionRelationFamily` | 1 | `medium:1` | `resolved_as_pairwise_signature_equivalence:1` | family relation pair has matching local name and exact local signature | `N14_gbs_index_specified_in_section ↔ N15_gbs_index_specified_in_section` |
| `GreatestPossibleRelationFamily` | 1 | `medium:1` | `resolved_as_pairwise_signature_equivalence:1` | family relation pair has matching local name and exact local signature | `Section4_6_greatest_possible ↔ Section5_4_greatest_possible` |
| `IndexAdjustmentRelationReviewFamily` | 1 | `high:1` | `resolved_as_projection_family:1` | IndexAdjustmentRelationReviewFamily has non-identity link type and is resolved below OWL equality | `Section4_4_adjustment_of_index ↔ Section4_5_adjustment_to_index` |
| `IndexComponentRequirementsRelationFamily` | 1 | `high:1` | `resolved_as_pairwise_signature_equivalence:1` | family relation pair has matching local name and exact local signature | `N12_fulfills_index_component_requirements ↔ N13_fulfills_index_component_requirements` |
| `IndexQualitySortFamily` | 1 | `medium:1` | `resolved_as_non_identity_related_concept:1` | IndexQualitySortFamily has non-identity link type and is resolved below OWL equality | `Section4_5_IndexQuality ↔ Section5_4_IndexQuality` |
| `IndexTypeFunctionFamily` | 1 | `medium:1` | `resolved_as_pairwise_signature_equivalence:1` | family relation pair has matching local name and exact local signature | `Section1_2_index_type ↔ Section4_1_index_type` |
| `LegacyIncorporatedByReferenceRelationFamily` | 1 | `medium:1` | `resolved_as_non_identity_related_concept:1` | LegacyIncorporatedByReferenceRelationFamily has non-identity link type and is resolved below OWL equality | `Section4_1_incorporated_by_reference ↔ Section5_4_incorporated_by_reference` |
| `MethodologyOfIndexRelationFamily` | 1 | `medium:1` | `resolved_as_pairwise_signature_equivalence:1` | family relation pair has matching local name and exact local signature | `Section5_2_methodology_of_index ↔ Section5_4_methodology_of_index` |
| `RegionFunctionFamily` | 1 | `medium:1` | `resolved_as_projection_family:1` | RegionFunctionFamily has non-identity link type and is resolved below OWL equality | `Section2_2_region ↔ Section2_3_region` |
| `SectionLocalIndexScopeRelationReviewFamily` | 1 | `medium:1` | `resolved_as_non_identity_related_concept:1` | SectionLocalIndexScopeRelationReviewFamily has non-identity link type and is resolved below OWL equality | `Section1_3_section_1_3_index ↔ Section4_1_section_4_1_index` |
| `SecurityReflectedRelationReviewFamily` | 1 | `medium:1` | `resolved_as_non_identity_related_concept:1` | SecurityReflectedRelationReviewFamily has non-identity link type and is resolved below OWL equality | `N15_security_reflected_in_gbs_index ↔ N19_security_reflected_in_index` |
| `UnitedStatesClassificationFamily` | 1 | `medium:1` | `resolved_as_non_identity_related_concept:1` | UnitedStatesClassificationFamily has non-identity link type and is resolved below OWL equality | `Section2_1_UnitedStates ↔ Section2_2_UnitedStates` |

## Open Review Items

No open review items remain after adapter/projection/non-identity resolution.

## Interpretation

A review item is not an uncovered token and not a hidden merge failure.
It is a recorded refusal to make a stronger OWL claim than the bridge evidence supports.
High-attention items are the ones worth reading first before a final thesis/report claim that all semantic merge decisions are closed.
