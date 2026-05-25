# Process Reasoning Audit v1

Status: `passed_with_review_items`

## Summary

- `process_step_count`: 32
- `workflow_count`: 7
- `step_edge_count`: 26
- `grounding_target_count`: 18
- `hard_findings`: 0
- `soft_findings`: 0
- `advisory_findings`: 29

## Findings

1. `advisory` `external_input_accepted`: Input CorporateActionPriceEffectInput required by AccountForCorporateActionInCalculation is accepted as external/source-backed.
   Data: `{"step": "AccountForCorporateActionInCalculation", "input": "CorporateActionPriceEffectInput", "input_kinds": ["ObservationFrameIO"]}`
2. `advisory` `external_input_accepted`: Input EquityIndexMethodologyInput required by AccountForCorporateActionInCalculation is accepted as external/source-backed.
   Data: `{"step": "AccountForCorporateActionInCalculation", "input": "EquityIndexMethodologyInput", "input_kinds": ["DomainConceptIO"]}`
3. `advisory` `external_input_accepted`: Input DisruptionPolicyInput required by ApplyDisruptionPolicyArrangements is accepted as external/source-backed.
   Data: `{"step": "ApplyDisruptionPolicyArrangements", "input": "DisruptionPolicyInput", "input_kinds": ["DomainConceptIO"]}`
4. `advisory` `external_input_accepted`: Input FreeFloatMarketCapitalizationInput required by CalculateSelectionDayWeights is accepted as external/source-backed.
   Data: `{"step": "CalculateSelectionDayWeights", "input": "FreeFloatMarketCapitalizationInput", "input_kinds": ["ObservationFrameIO"]}`
5. `advisory` `external_input_accepted`: Input SelectedComponentsInput required by CalculateSelectionDayWeights is accepted as external/source-backed.
   Data: `{"step": "CalculateSelectionDayWeights", "input": "SelectedComponentsInput", "input_kinds": ["ProcessStateIO"]}`
6. `advisory` `external_input_accepted`: Input CorporateActionEventInput required by DetectCorporateActionEvent is accepted as external/source-backed.
   Data: `{"step": "DetectCorporateActionEvent", "input": "CorporateActionEventInput", "input_kinds": ["DomainConceptIO"]}`
7. `advisory` `external_input_accepted`: Input AdjustedReturnIndexCalculationInput required by DetectZeroOrNegativeAdjustedReturnIndexLevel is accepted as external/source-backed.
   Data: `{"step": "DetectZeroOrNegativeAdjustedReturnIndexLevel", "input": "AdjustedReturnIndexCalculationInput", "input_kinds": ["ObservationFrameIO"]}`
8. `advisory` `external_input_accepted`: Input AffectedIndexComponentInput required by DetermineCorporateActionAdjustmentNeed is accepted as external/source-backed.
   Data: `{"step": "DetermineCorporateActionAdjustmentNeed", "input": "AffectedIndexComponentInput", "input_kinds": ["DomainConceptIO"]}`
9. `advisory` `external_input_accepted`: Input CorporateActionKindInput required by DetermineCorporateActionAdjustmentNeed is accepted as external/source-backed.
   Data: `{"step": "DetermineCorporateActionAdjustmentNeed", "input": "CorporateActionKindInput", "input_kinds": ["DomainConceptIO"]}`
10. `advisory` `external_input_accepted`: Input CorrectionPolicyInput required by DetermineCorrectionMeasures is accepted as external/source-backed.
   Data: `{"step": "DetermineCorrectionMeasures", "input": "CorrectionPolicyInput", "input_kinds": ["DomainConceptIO"]}`
11. `advisory` `external_input_accepted`: Input ComponentWeightsInput required by DetermineFixingDayShares is accepted as external/source-backed.
   Data: `{"step": "DetermineFixingDayShares", "input": "ComponentWeightsInput", "input_kinds": ["ObservationFrameIO"]}`
12. `advisory` `external_input_accepted`: Input AffectedPriceInput required by DetermineIndexUnderDisruptedConditions is accepted as external/source-backed.
   Data: `{"step": "DetermineIndexUnderDisruptedConditions", "input": "AffectedPriceInput", "input_kinds": ["ObservationFrameIO"]}`
13. `advisory` `external_input_accepted`: Input DeterminationErrorInput required by IdentifyDeterminationError is accepted as external/source-backed.
   Data: `{"step": "IdentifyDeterminationError", "input": "DeterminationErrorInput", "input_kinds": ["DomainConceptIO"]}`
14. `advisory` `external_input_accepted`: Input CorporateActionNoticeInput required by ImplementCorporateActionAdjustment is accepted as external/source-backed.
   Data: `{"step": "ImplementCorporateActionAdjustment", "input": "CorporateActionNoticeInput", "input_kinds": ["DomainConceptIO"]}`
15. `advisory` `external_input_accepted`: Input FixingDaySharesInput required by ImplementOrdinaryRebalance is accepted as external/source-backed.
   Data: `{"step": "ImplementOrdinaryRebalance", "input": "FixingDaySharesInput", "input_kinds": ["DomainConceptIO"]}`
16. `advisory` `external_input_accepted`: Input SelectedComponentsInput required by ImplementOrdinaryRebalance is accepted as external/source-backed.
   Data: `{"step": "ImplementOrdinaryRebalance", "input": "SelectedComponentsInput", "input_kinds": ["ProcessStateIO"]}`
17. `advisory` `external_input_accepted`: Input MethodologyPolicyInput required by MakeMethodologyChangeInPolicy is accepted as external/source-backed.
   Data: `{"step": "MakeMethodologyChangeInPolicy", "input": "MethodologyPolicyInput", "input_kinds": ["DomainConceptIO"]}`
18. `advisory` `external_input_accepted`: Input ProposedAmendmentInput required by ProposeRuleOrGuidelineAmendment is accepted as external/source-backed.
   Data: `{"step": "ProposeRuleOrGuidelineAmendment", "input": "ProposedAmendmentInput", "input_kinds": ["DomainConceptIO"]}`
19. `advisory` `external_input_accepted`: Input PlannedComponentChangesInput required by PublishRebalanceComponentChanges is accepted as external/source-backed.
   Data: `{"step": "PublishRebalanceComponentChanges", "input": "PlannedComponentChangesInput", "input_kinds": ["ProcessStateIO"]}`
20. `advisory` `external_input_accepted`: Input MethodologyReviewInput required by ReviewMethodologyAtLeastAnnually is accepted as external/source-backed.
   Data: `{"step": "ReviewMethodologyAtLeastAnnually", "input": "MethodologyReviewInput", "input_kinds": ["DomainConceptIO"]}`
21. `advisory` `external_input_accepted`: Input IndexUniverseInput required by SelectIndexComponents is accepted as external/source-backed.
   Data: `{"step": "SelectIndexComponents", "input": "IndexUniverseInput", "input_kinds": ["DomainConceptIO"]}`
22. `advisory` `external_input_accepted`: Input OversightCommitteeInput required by SubmitAmendmentForPriorApproval is accepted as external/source-backed.
   Data: `{"step": "SubmitAmendmentForPriorApproval", "input": "OversightCommitteeInput", "input_kinds": ["DomainConceptIO"]}`
23. `advisory` `modify_continue_without_adjusted_artifact`: ModifyAndContinue step DetectCorporateActionEvent has no obviously adjusted/changed output or state.
   Data: `{"step": "DetectCorporateActionEvent"}`
24. `advisory` `modify_continue_without_adjusted_artifact`: ModifyAndContinue step DetectMarketDisruptionCondition has no obviously adjusted/changed output or state.
   Data: `{"step": "DetectMarketDisruptionCondition"}`
25. `advisory` `modify_continue_without_adjusted_artifact`: ModifyAndContinue step EvaluateCorporateActionProcedureDeviation has no obviously adjusted/changed output or state.
   Data: `{"step": "EvaluateCorporateActionProcedureDeviation"}`
26. `advisory` `modify_continue_without_adjusted_artifact`: ModifyAndContinue step IdentifyMethodologyChangeNeed has no obviously adjusted/changed output or state.
   Data: `{"step": "IdentifyMethodologyChangeNeed"}`
27. `advisory` `modify_continue_without_adjusted_artifact`: ModifyAndContinue step ReviewMethodologyAtLeastAnnually has no obviously adjusted/changed output or state.
   Data: `{"step": "ReviewMethodologyAtLeastAnnually"}`
28. `advisory` `trigger_temporal_relation_without_grounding`: trigger_temporal_relation(FixingDayTrigger, RebalanceDayAfterCloseOfBusinessTrigger, Before) has no trigger_relation_grounded_in.
   Data: `{"from": "FixingDayTrigger", "to": "RebalanceDayAfterCloseOfBusinessTrigger", "relation": "Before"}`
29. `advisory` `trigger_temporal_relation_without_grounding`: trigger_temporal_relation(SufficientNoticeBeforeRebalanceDayTrigger, RebalanceDayAfterCloseOfBusinessTrigger, Before) has no trigger_relation_grounded_in.
   Data: `{"from": "SufficientNoticeBeforeRebalanceDayTrigger", "to": "RebalanceDayAfterCloseOfBusinessTrigger", "relation": "Before"}`

## Interpretation

Hard findings block process-layer readiness. Soft findings require an explicit modeling decision or note. Advisory findings document accepted external inputs, intentional deferrals, or useful review prompts.
