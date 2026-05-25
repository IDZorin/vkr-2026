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

(assert (! (WeekdayOrdinal FirstWeekdayOrdinal) :named TYPE_entity_FirstWeekdayOrdinal))
(assert (! (distinct May November) :named TYPE_enum_distinct_Month))

(declare-fun eligible_rebalance_day (Day) Bool)
(declare-fun immediately_following_eligible_rebalance_day_after (Day Day) Bool)
(declare-fun nth_wednesday_in_month (Day Month Int) Bool)
(declare-fun rebalance_day (Day) Bool)
(declare-fun scheduled_rebalance_day (Day) Bool)
(declare-fun strictly_before (Day Day) Bool)

(assert (! (forall ((nth_wednesday_in_month_arg0 Day) (nth_wednesday_in_month_arg1 Month) (nth_wednesday_in_month_arg2 Int)) (=> (nth_wednesday_in_month nth_wednesday_in_month_arg0 nth_wednesday_in_month_arg1 nth_wednesday_in_month_arg2) (WeekdayOrdinal nth_wednesday_in_month_arg2))) :named TYPE_symbol_nth_wednesday_in_month))

(assert (! (= FirstWeekdayOrdinal 1) :named TEXT_first_weekday_ordinal_value))
(assert (! (forall ((d Day)) (= (scheduled_rebalance_day d) (or (nth_wednesday_in_month d May FirstWeekdayOrdinal) (nth_wednesday_in_month d November FirstWeekdayOrdinal)))) :named TEXT_scheduled_rebalance_day_definition))
(assert (! (forall ((d Day)) (= (rebalance_day d) (or (and (scheduled_rebalance_day d) (eligible_rebalance_day d)) (exists ((s Day)) (and (scheduled_rebalance_day s) (not (eligible_rebalance_day s)) (eligible_rebalance_day d) (immediately_following_eligible_rebalance_day_after d s)))))) :named TEXT_rebalance_day_definition))
(assert (! (forall ((d Day)) (forall ((s Day)) (=> (immediately_following_eligible_rebalance_day_after d s) (and (strictly_before s d) (eligible_rebalance_day d) (forall ((e Day)) (=> (and (strictly_before s e) (strictly_before e d)) (not (eligible_rebalance_day e)))))))) :named TEXT_immediately_following_eligible_rebalance_day_definition))
; Probe N26__scheduled_rebalance_day_definition__iff_rhs_witness__002: iff_rhs_witness
(check-sat)
(push 1)
(assert (! (exists ((d Day)) (or (nth_wednesday_in_month d May FirstWeekdayOrdinal) (nth_wednesday_in_month d November FirstWeekdayOrdinal))) :named PROBE_N26__scheduled_rebalance_day_definition__iff_rhs_witness__002))
(check-sat)
(pop 1)
