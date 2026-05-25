(set-logic ALL)
(set-option :produce-unsat-cores true)

(declare-sort Day 0)

(declare-fun BusinessDayCount (Int) Bool)
(declare-fun RebalanceDay (Day) Bool)
(declare-fun SelectionDay (Day) Bool)

(declare-const TwentyBusinessDays Int)
(declare-const W_rd_RebalanceDay Day)
(declare-const W_sd_SelectionDay Day)

(assert (! (BusinessDayCount TwentyBusinessDays) :named TYPE_entity_TwentyBusinessDays))
(assert (! (RebalanceDay W_rd_RebalanceDay) :named TYPE_witness_W_rd_RebalanceDay))
(assert (! (SelectionDay W_sd_SelectionDay) :named TYPE_witness_W_sd_SelectionDay))

(declare-fun business_day_count_before (Day Day) Int)
(declare-fun change_of_rebalance_day_disregarded_for_selection_day (Day Day) Bool)
(declare-fun selection_day_for_rebalance_day (Day Day) Bool)

(assert (! (= TwentyBusinessDays 20) :named BOUNDED_TEXT_twenty_business_days_count))
(assert (! (and (SelectionDay W_sd_SelectionDay) (and (RebalanceDay W_rd_RebalanceDay) (= (selection_day_for_rebalance_day W_sd_SelectionDay W_rd_RebalanceDay) (= (business_day_count_before W_sd_SelectionDay W_rd_RebalanceDay) TwentyBusinessDays)))) :named BOUNDED_TEXT_selection_day_definition))
(assert (! (and (SelectionDay W_sd_SelectionDay) (and (RebalanceDay W_rd_RebalanceDay) (=> (selection_day_for_rebalance_day W_sd_SelectionDay W_rd_RebalanceDay) (change_of_rebalance_day_disregarded_for_selection_day W_sd_SelectionDay W_rd_RebalanceDay)))) :named BOUNDED_TEXT_rebalance_day_change_disregarded_for_selection_day))

(check-sat)
(push 1)
(assert (! (and (SelectionDay W_sd_SelectionDay) (RebalanceDay W_rd_RebalanceDay) (= (business_day_count_before W_sd_SelectionDay W_rd_RebalanceDay) TwentyBusinessDays)) :named BOUNDED_PROBE_N27__selection_day_definition__iff_rhs_witness__002))
(check-sat)
(pop 1)
