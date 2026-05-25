# Financial Methodology Backend Projection Report v1

Status: `passed_with_review_items`

## Summary

- `target_count`: `61`
- `target_count_by_kind`: `{"section": 22, "definition": 32, "appendix": 1, "bridge": 2, "merge": 1, "process": 3}`
- `backend_check_status_counts`: `{"rdf:ok": 61, "owl:ok": 61, "shacl:ok": 61}`
- `backend_emission_diagnostic_counts`: `{"rdf": 0, "owl": 302, "shacl": 124}`
- `hard_findings`: `0`
- `soft_findings`: `0`
- `advisory_findings`: `426`
- `smt_probe_summary`: `{"path": "case_studies\\financial_methodology\\reasoning\\smt_probe_results_v1.json", "status": "passed_with_review_items", "smt_mode": "hybrid", "probe_count": 332, "hard_findings": 0, "soft_findings": 0, "advisory_findings": 332}`
- `owl_union`: `{"union_path": "case_studies\\financial_methodology\\backend_projection\\all\\methodology_owl_union.ttl", "manifest_path": "case_studies\\financial_methodology\\backend_projection\\all\\methodology_owl_union_manifest.json", "check_path": "case_studies\\financial_methodology\\backend_projection\\all\\methodology_owl_union.check.json", "target_count": 61, "check": {"backend": "owl", "status": "ok", "triple_count": 13192, "message": "OWL RL closure completed", "triple_count_before": 13192, "triple_count_after": 28224}}`
- `owl_resolved`: `{"schema": "methodology_owl_resolved_manifest_v1", "status": "ok", "union_path": "case_studies\\financial_methodology\\backend_projection\\all\\methodology_owl_union.ttl", "resolved_path": "case_studies\\financial_methodology\\backend_projection\\all\\methodology_owl_resolved.ttl", "manifest_path": "case_studies\\financial_methodology\\backend_projection\\all\\methodology_owl_resolved_manifest.json", "check_path": "case_studies\\financial_methodology\\backend_projection\\all\\methodology_owl_resolved.check.json", "review_items_path": "case_studies\\financial_methodology\\backend_projection\\all\\methodology_owl_resolved_review_items_v1.json", "review_summary_path": "case_studies\\financial_methodology\\backend_projection\\all\\methodology_owl_resolved_review_items_summary.md", "bridge_path": "case_studies\\financial_methodology\\bridge\\main_bridge.a4v3", "bridge_parse_warning_count": 0, "resolution_counts": {"axiom:owl:equivalentClass:same_sort": 43, "axiom:owl:sameAs:same_entity": 11, "axiom:owl:sameAs:same_index": 5, "axiom:owl:equivalentProperty:same_relation": 20, "decision:resolved_as_scoped_projection_adapter": 1, "axiom:owl:inverseOf:reversed_relation_adapter": 3, "decision:resolved_as_inverse_adapter": 3, "decision:resolved_as_domain_specialized_relation": 2, "axiom:owl:sameAs:family:AnnouncementSectionFamily": 3, "decision:resolved_as_projection_family": 12, "decision:resolved_as_non_identity_related_concept": 40, "axiom:owl:equivalentClass:family:CalculationTimeSortFamily": 1, "axiom:owl:equivalentClass:family:CanonicalCalculationDaySortFamily": 3, "axiom:owl:equivalentClass:family:CanonicalEffortSortFamily": 1, "axiom:owl:equivalentClass:family:CanonicalGbsIndexSortFamily": 3, "axiom:owl:sameAs:family:CanonicalGuidelineEntityFamily": 3, "axiom:owl:equivalentClass:family:CanonicalIndexAdministratorSortFamily": 10, "axiom:owl:equivalentClass:family:CanonicalIndexMethodologySortFamily": 6, "axiom:owl:equivalentClass:family:CanonicalIndexSortFamily": 276, "axiom:owl:equivalentClass:family:CanonicalIndexTypeSortFamily": 1, "axiom:owl:equivalentClass:family:CanonicalPriceSortFamily": 6, "axiom:owl:equivalentClass:family:CanonicalSelectionDaySortFamily": 21, "axiom:owl:sameAs:family:CanonicalSolactiveEntityFamily": 55, "axiom:owl:equivalentClass:family:CoreIndexComponentSortFamily": 78, "axiom:owl:equivalentClass:family:CoreSecuritySortFamily": 36, "axiom:owl:equivalentClass:family:CorporateActionSortFamily": 1, "axiom:owl:equivalentClass:family:DataVendorSortFamily": 1, "axiom:owl:equivalentClass:family:DiscretionaryDecisionSortFamily": 1, "axiom:owl:sameAs:family:EquityIndexMethodologyFamily": 10, "axiom:owl:sameAs:family:EquityIndexMethodologyUrlFamily": 1, "axiom:owl:equivalentClass:family:ErrorSortFamily": 1, "axiom:owl:equivalentClass:family:FloatMarketCapitalizationReviewFamily": 3, "axiom:owl:sameAs:family:GBSBenchmarkSeriesDocumentFamily": 1, "axiom:owl:sameAs:family:GBSBenchmarkSeriesUrlFamily": 1, "axiom:owl:sameAs:family:GbsIndexSpecifiedInSection2_1Family": 1, "axiom:owl:equivalentProperty:family_signature:GbsIndexSpecifiedInSectionRelationFamily": 1, "decision:resolved_as_pairwise_signature_equivalence": 117, "decision:resolved_as_family_split": 300, "axiom:owl:equivalentProperty:family_signature:GenericDocumentAvailabilityRelationFamily": 106, "axiom:owl:equivalentProperty:family_signature:GreatestPossibleRelationFamily": 1, "axiom:owl:equivalentClass:family:IndexCalculationSortFamily": 1, "axiom:owl:equivalentProperty:family_signature:IndexComponentRequirementsRelationFamily": 1, "axiom:owl:equivalentProperty:family_signature:IndexCurrencyFunctionFamily": 3, "axiom:owl:equivalentClass:family:IndexLevelSortFamily": 10, "axiom:owl:equivalentProperty:family_signature:IndexOfRelationFamily": 3, "axiom:owl:equivalentClass:family:IndexRuleSortFamily": 1, "axiom:owl:equivalentProperty:family_signature:IndexTypeFunctionFamily": 1, "axiom:owl:equivalentClass:family:IsinSortFamily": 1, "axiom:owl:equivalentProperty:family_signature:MethodologyOfIndexRelationFamily": 1, "axiom:owl:sameAs:family:MethodologyPolicyUrlFamily": 1, "axiom:owl:sameAs:family:NewsAnnouncementsUrlFamily": 6, "axiom:owl:equivalentClass:family:NoticeSortFamily": 1, "axiom:owl:equivalentClass:family:PolicySortFamily": 1, "axiom:owl:equivalentClass:family:RegionSortFamily": 1, "axiom:owl:equivalentClass:family:ShareCountSortFamily": 1, "axiom:owl:sameAs:family:SolactiveGreatestPossibleEffortsFamily": 1, "axiom:owl:equivalentClass:family:SolactiveOrganizationSortFamily": 10, "axiom:owl:sameAs:family:SolactiveWebsiteFamily": 55, "axiom:owl:sameAs:family:TheIndexAdministratorFamily": 1, "axiom:owl:sameAs:family:TheIndexLocalPlaceholderFamily": 136, "axiom:owl:sameAs:family:ThisGuidelineFamily": 6, "axiom:owl:sameAs:family:VarietyReasonsVagueTermFamily": 1}, "identity_axiom_count": 957, "resolved_triple_count": 1282, "resolved_decision_count": 475, "review_item_count": 0, "review_annotation_line_count": 0, "unresolved_symbol_count": 0, "unresolved_symbols": {}, "check": {"backend": "owl", "status": "ok", "triple_count": 21124, "message": "OWL RL closure completed", "triple_count_before": 21124, "triple_count_after": 56175}}`

## Backend Meaning

- `rdf.ttl`: structural graph projection of A4V3 declarations and assertions.
- `owl.ttl`: OWL/RDF ontology-style projection of sorts, entities, and simple properties.
- `shacl_shapes.ttl`: SHACL structural validation shapes for supported unary/binary symbols.
- SMT is linked through the dedicated `smt_probe_runner_v1` report instead of duplicated here.

## Targets

| Target | Kind | RDF | OWL | SHACL | Diagnostics |
| --- | --- | --- | --- | --- | ---: |
| `section_1_1` | `section` | `ok` | `ok` | `ok` | 2 |
| `section_1_2` | `section` | `ok` | `ok` | `ok` | 9 |
| `section_1_3` | `section` | `ok` | `ok` | `ok` | 10 |
| `section_1_4` | `section` | `ok` | `ok` | `ok` | 63 |
| `section_1_5` | `section` | `ok` | `ok` | `ok` | 1 |
| `section_2_1` | `section` | `ok` | `ok` | `ok` | 35 |
| `section_2_2` | `section` | `ok` | `ok` | `ok` | 19 |
| `section_2_3` | `section` | `ok` | `ok` | `ok` | 11 |
| `section_3_1` | `section` | `ok` | `ok` | `ok` | 11 |
| `section_3_2` | `section` | `ok` | `ok` | `ok` | 1 |
| `section_4_1` | `section` | `ok` | `ok` | `ok` | 30 |
| `section_4_2` | `section` | `ok` | `ok` | `ok` | 3 |
| `section_4_3` | `section` | `ok` | `ok` | `ok` | 1 |
| `section_4_4` | `section` | `ok` | `ok` | `ok` | 7 |
| `section_4_5` | `section` | `ok` | `ok` | `ok` | 24 |
| `section_4_6` | `section` | `ok` | `ok` | `ok` | 6 |
| `section_4_7` | `section` | `ok` | `ok` | `ok` | 6 |
| `section_5_1` | `section` | `ok` | `ok` | `ok` | 1 |
| `section_5_2` | `section` | `ok` | `ok` | `ok` | 8 |
| `section_5_3` | `section` | `ok` | `ok` | `ok` | 11 |
| `section_5_4` | `section` | `ok` | `ok` | `ok` | 20 |
| `section_5_5` | `section` | `ok` | `ok` | `ok` | 6 |
| `N01` | `definition` | `ok` | `ok` | `ok` | 9 |
| `N02` | `definition` | `ok` | `ok` | `ok` | 0 |
| `N03` | `definition` | `ok` | `ok` | `ok` | 0 |
| `N04` | `definition` | `ok` | `ok` | `ok` | 1 |
| `N05` | `definition` | `ok` | `ok` | `ok` | 1 |
| `N06` | `definition` | `ok` | `ok` | `ok` | 0 |
| `N07` | `definition` | `ok` | `ok` | `ok` | 8 |
| `N08` | `definition` | `ok` | `ok` | `ok` | 7 |
| `N09` | `definition` | `ok` | `ok` | `ok` | 1 |
| `N10` | `definition` | `ok` | `ok` | `ok` | 3 |
| `N11` | `definition` | `ok` | `ok` | `ok` | 1 |
| `N12` | `definition` | `ok` | `ok` | `ok` | 5 |
| `N13` | `definition` | `ok` | `ok` | `ok` | 9 |
| `N14` | `definition` | `ok` | `ok` | `ok` | 1 |
| `N15` | `definition` | `ok` | `ok` | `ok` | 1 |
| `N16` | `definition` | `ok` | `ok` | `ok` | 0 |
| `N17` | `definition` | `ok` | `ok` | `ok` | 0 |
| `N18` | `definition` | `ok` | `ok` | `ok` | 0 |
| `N19` | `definition` | `ok` | `ok` | `ok` | 1 |
| `N20` | `definition` | `ok` | `ok` | `ok` | 0 |
| `N21` | `definition` | `ok` | `ok` | `ok` | 1 |
| `N22` | `definition` | `ok` | `ok` | `ok` | 0 |
| `N23` | `definition` | `ok` | `ok` | `ok` | 1 |
| `N24` | `definition` | `ok` | `ok` | `ok` | 0 |
| `N25` | `definition` | `ok` | `ok` | `ok` | 0 |
| `N26` | `definition` | `ok` | `ok` | `ok` | 5 |
| `N27` | `definition` | `ok` | `ok` | `ok` | 4 |
| `N28` | `definition` | `ok` | `ok` | `ok` | 0 |
| `N29` | `definition` | `ok` | `ok` | `ok` | 0 |
| `N30` | `definition` | `ok` | `ok` | `ok` | 12 |
| `N31` | `definition` | `ok` | `ok` | `ok` | 8 |
| `N32` | `definition` | `ok` | `ok` | `ok` | 0 |
| `appendix_8_1` | `appendix` | `ok` | `ok` | `ok` | 0 |
| `bridge_main_bridge` | `bridge` | `ok` | `ok` | `ok` | 10 |
| `bridge_resolved_bridge_decisions_v1` | `bridge` | `ok` | `ok` | `ok` | 4 |
| `merge_canonical_ontology_v1` | `merge` | `ok` | `ok` | `ok` | 18 |
| `process_ontology_v1` | `process` | `ok` | `ok` | `ok` | 10 |
| `ordinary_rebalance_workflow_v1` | `process` | `ok` | `ok` | `ok` | 10 |
| `exception_overlays_v1` | `process` | `ok` | `ok` | `ok` | 10 |
