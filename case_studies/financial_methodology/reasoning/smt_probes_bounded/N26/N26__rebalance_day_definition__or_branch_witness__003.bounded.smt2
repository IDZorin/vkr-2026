(set-logic ALL)
(set-option :produce-unsat-cores true)

(declare-sort Day 0)
(declare-sort Month 0)

(declare-fun RebalanceDay (Day) Bool)
(declare-fun ScheduledRebalanceDay (Day) Bool)
(declare-fun WeekdayOrdinal (Int) Bool)

(declare-const FirstWeekdayOrdinal Int)
(declare-const May Month)
(declare-const November Month)
(declare-const W_d_RebalanceDay Day)
(declare-const W_d_ScheduledRebalanceDay Day)
(declare-const W_s_ScheduledRebalanceDay Day)

(assert (! (WeekdayOrdinal FirstWeekdayOrdinal) :named TYPE_entity_FirstWeekdayOrdinal))
(assert (! (RebalanceDay W_d_RebalanceDay) :named TYPE_witness_W_d_RebalanceDay))
(assert (! (ScheduledRebalanceDay W_d_ScheduledRebalanceDay) :named TYPE_witness_W_d_ScheduledRebalanceDay))
(assert (! (ScheduledRebalanceDay W_s_ScheduledRebalanceDay) :named TYPE_witness_W_s_ScheduledRebalanceDay))
(assert (! (distinct May November) :named TYPE_enum_distinct_Month))

(declare-fun eligible_rebalance_day (Day) Bool)
(declare-fun immediately_following_eligible_rebalance_day_after (Day Day) Bool)
(declare-fun nth_wednesday_in_month (Day Month Int) Bool)
(declare-fun rebalance_day (Day) Bool)
(declare-fun scheduled_rebalance_day (Day) Bool)

(assert (! (= FirstWeekdayOrdinal 1) :named BOUNDED_TEXT_first_weekday_ordinal_value))
(assert (! (and (ScheduledRebalanceDay W_d_ScheduledRebalanceDay) (= (scheduled_rebalance_day W_d_ScheduledRebalanceDay) (or (nth_wednesday_in_month W_d_ScheduledRebalanceDay May FirstWeekdayOrdinal) (nth_wednesday_in_month W_d_ScheduledRebalanceDay November FirstWeekdayOrdinal)))) :named BOUNDED_TEXT_scheduled_rebalance_day_definition))
(assert (! (and (RebalanceDay W_d_RebalanceDay) (= (rebalance_day W_d_RebalanceDay) (or (and (ScheduledRebalanceDay W_s_ScheduledRebalanceDay) (and (= W_d_RebalanceDay W_s_ScheduledRebalanceDay) (scheduled_rebalance_day W_s_ScheduledRebalanceDay) (eligible_rebalance_day W_s_ScheduledRebalanceDay))) (and (ScheduledRebalanceDay W_s_ScheduledRebalanceDay) (and (scheduled_rebalance_day W_s_ScheduledRebalanceDay) (not (eligible_rebalance_day W_s_ScheduledRebalanceDay)) (eligible_rebalance_day W_d_RebalanceDay) (immediately_following_eligible_rebalance_day_after W_d_RebalanceDay W_s_ScheduledRebalanceDay)))))) :named BOUNDED_TEXT_rebalance_day_definition))

(check-sat)
(push 1)
(assert (! (and (RebalanceDay W_d_RebalanceDay) (and (ScheduledRebalanceDay W_s_ScheduledRebalanceDay) (and (= W_d_RebalanceDay W_s_ScheduledRebalanceDay) (scheduled_rebalance_day W_s_ScheduledRebalanceDay) (eligible_rebalance_day W_s_ScheduledRebalanceDay)))) :named BOUNDED_PROBE_N26__rebalance_day_definition__or_branch_witness__003))
(check-sat)
(pop 1)
