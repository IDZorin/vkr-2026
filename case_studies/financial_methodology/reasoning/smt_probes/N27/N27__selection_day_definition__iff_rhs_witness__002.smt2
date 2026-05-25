(set-logic ALL)
(set-option :produce-unsat-cores true)

(declare-sort Day 0)

(declare-fun BusinessDayCount (Int) Bool)
(declare-fun RebalanceDay (Day) Bool)
(declare-fun SelectionDay (Day) Bool)

(declare-const TwentyBusinessDays Int)

(assert (! (BusinessDayCount TwentyBusinessDays) :named TYPE_entity_TwentyBusinessDays))

(declare-fun business_day_count_before (Day Day) Int)
(declare-fun change_of_rebalance_day_disregarded_for_selection_day (Day Day) Bool)
(declare-fun selection_day_for_rebalance_day (Day Day) Bool)

(assert (! (forall ((business_day_count_before_arg0 Day) (business_day_count_before_arg1 Day)) (BusinessDayCount (business_day_count_before business_day_count_before_arg0 business_day_count_before_arg1))) :named TYPE_symbol_business_day_count_before))
(assert (! (forall ((change_of_rebalance_day_disregarded_for_selection_day_arg0 Day) (change_of_rebalance_day_disregarded_for_selection_day_arg1 Day)) (=> (change_of_rebalance_day_disregarded_for_selection_day change_of_rebalance_day_disregarded_for_selection_day_arg0 change_of_rebalance_day_disregarded_for_selection_day_arg1) (and (SelectionDay change_of_rebalance_day_disregarded_for_selection_day_arg0) (RebalanceDay change_of_rebalance_day_disregarded_for_selection_day_arg1)))) :named TYPE_symbol_change_of_rebalance_day_disregarded_for_selection_day))
(assert (! (forall ((selection_day_for_rebalance_day_arg0 Day) (selection_day_for_rebalance_day_arg1 Day)) (=> (selection_day_for_rebalance_day selection_day_for_rebalance_day_arg0 selection_day_for_rebalance_day_arg1) (and (SelectionDay selection_day_for_rebalance_day_arg0) (RebalanceDay selection_day_for_rebalance_day_arg1)))) :named TYPE_symbol_selection_day_for_rebalance_day))

(assert (! (= TwentyBusinessDays 20) :named TEXT_twenty_business_days_count))
(assert (! (forall ((sd Day)) (=> (SelectionDay sd) (forall ((rd Day)) (=> (RebalanceDay rd) (= (selection_day_for_rebalance_day sd rd) (= (business_day_count_before sd rd) TwentyBusinessDays)))))) :named TEXT_selection_day_definition))
(assert (! (forall ((sd Day)) (=> (SelectionDay sd) (forall ((rd Day)) (=> (RebalanceDay rd) (=> (selection_day_for_rebalance_day sd rd) (change_of_rebalance_day_disregarded_for_selection_day sd rd)))))) :named TEXT_rebalance_day_change_disregarded_for_selection_day))
; Probe N27__selection_day_definition__iff_rhs_witness__002: iff_rhs_witness
(check-sat)
(push 1)
(assert (! (exists ((sd Day) (rd Day)) (and (SelectionDay sd) (RebalanceDay rd) (= (business_day_count_before sd rd) TwentyBusinessDays))) :named PROBE_N27__selection_day_definition__iff_rhs_witness__002))
(check-sat)
(pop 1)
