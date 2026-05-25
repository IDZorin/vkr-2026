(set-logic ALL)
(set-option :produce-unsat-cores true)

(declare-sort Discretion 0)
(declare-sort ExerciseBasis 0)
(declare-sort Index 0)
(declare-sort IndexDeterminationMatter 0)
(declare-sort StrictRule 0)

(declare-fun IndexDeterminationDiscretion (Discretion) Bool)

(declare-const DeterminationOfIndex IndexDeterminationMatter)
(declare-const DeterminationOfIndexUniverse IndexDeterminationMatter)
(declare-const ExerciseOfDiscretion ExerciseBasis)
(declare-const ExerciseOfExpertJudgement ExerciseBasis)
(declare-const OtherRelevantDecisionInRelationToIndex IndexDeterminationMatter)
(declare-const SelectionOfIndexComponents IndexDeterminationMatter)
(declare-const StrictRulesForDiscretionAndExpertJudgement StrictRule)
(declare-const TheIndex Index)

(assert (! (distinct ExerciseOfDiscretion ExerciseOfExpertJudgement) :named TYPE_enum_distinct_ExerciseBasis))
(assert (! (distinct DeterminationOfIndex DeterminationOfIndexUniverse SelectionOfIndexComponents OtherRelevantDecisionInRelationToIndex) :named TYPE_enum_distinct_IndexDeterminationMatter))

(declare-fun discretion_in_relation_to_index (Discretion Index) Bool)
(declare-fun discretion_in_relation_to_matter (Discretion IndexDeterminationMatter) Bool)
(declare-fun if_applicable (IndexDeterminationMatter) Bool)
(declare-fun other_relevant_decision_in_relation_to_index (IndexDeterminationMatter) Bool)
(declare-fun potential_need_to_exercise (Discretion) Bool)
(declare-fun rules_regarding_exercise (StrictRule ExerciseBasis) Bool)
(declare-fun strict_rules (StrictRule) Bool)

(assert (! (forall ((discretion_in_relation_to_index_arg0 Discretion) (discretion_in_relation_to_index_arg1 Index)) (=> (discretion_in_relation_to_index discretion_in_relation_to_index_arg0 discretion_in_relation_to_index_arg1) (IndexDeterminationDiscretion discretion_in_relation_to_index_arg0))) :named TYPE_symbol_discretion_in_relation_to_index))
(assert (! (forall ((discretion_in_relation_to_matter_arg0 Discretion) (discretion_in_relation_to_matter_arg1 IndexDeterminationMatter)) (=> (discretion_in_relation_to_matter discretion_in_relation_to_matter_arg0 discretion_in_relation_to_matter_arg1) (IndexDeterminationDiscretion discretion_in_relation_to_matter_arg0))) :named TYPE_symbol_discretion_in_relation_to_matter))
(assert (! (forall ((potential_need_to_exercise_arg0 Discretion)) (=> (potential_need_to_exercise potential_need_to_exercise_arg0) (IndexDeterminationDiscretion potential_need_to_exercise_arg0))) :named TYPE_symbol_potential_need_to_exercise))

(assert (! (forall ((d Discretion)) (=> (IndexDeterminationDiscretion d) (and (potential_need_to_exercise d) (discretion_in_relation_to_index d TheIndex) (exists ((m IndexDeterminationMatter)) (discretion_in_relation_to_matter d m))))) :named TEXT_index_determination_discretion_scope))
(assert (! (and (if_applicable DeterminationOfIndexUniverse) (if_applicable SelectionOfIndexComponents) (other_relevant_decision_in_relation_to_index OtherRelevantDecisionInRelationToIndex)) :named TEXT_applicable_example_matters))
(assert (! (and (strict_rules StrictRulesForDiscretionAndExpertJudgement) (rules_regarding_exercise StrictRulesForDiscretionAndExpertJudgement ExerciseOfDiscretion) (rules_regarding_exercise StrictRulesForDiscretionAndExpertJudgement ExerciseOfExpertJudgement)) :named TEXT_strict_rules_for_discretion_or_expert_judgement))
(check-sat)
