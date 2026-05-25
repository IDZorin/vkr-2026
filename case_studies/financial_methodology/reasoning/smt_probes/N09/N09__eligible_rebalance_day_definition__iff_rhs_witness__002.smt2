(set-logic ALL)
(set-option :produce-unsat-cores true)

(declare-sort Day 0)
(declare-sort Exchange 0)

(declare-fun EligibleRebalanceDay (Day) Bool)

(declare-const EUREXExchange Exchange)
(declare-const LondonStockExchange Exchange)
(declare-const NewYorkStockExchange Exchange)
(declare-const TokyoStockExchange Exchange)

(declare-fun eligible_rebalance_day (Day) Bool)
(declare-fun trading_day_at_exchange (Day Exchange) Bool)

(assert (! (forall ((eligible_rebalance_day_arg0 Day)) (=> (eligible_rebalance_day eligible_rebalance_day_arg0) (EligibleRebalanceDay eligible_rebalance_day_arg0))) :named TYPE_symbol_eligible_rebalance_day))

(assert (! (forall ((d Day)) (=> (EligibleRebalanceDay d) (= (eligible_rebalance_day d) (and (trading_day_at_exchange d NewYorkStockExchange) (trading_day_at_exchange d LondonStockExchange) (trading_day_at_exchange d EUREXExchange) (trading_day_at_exchange d TokyoStockExchange))))) :named TEXT_eligible_rebalance_day_definition))
; Probe N09__eligible_rebalance_day_definition__iff_rhs_witness__002: iff_rhs_witness
(check-sat)
(push 1)
(assert (! (exists ((d Day)) (and (EligibleRebalanceDay d) (and (trading_day_at_exchange d NewYorkStockExchange) (trading_day_at_exchange d LondonStockExchange) (trading_day_at_exchange d EUREXExchange) (trading_day_at_exchange d TokyoStockExchange)))) :named PROBE_N09__eligible_rebalance_day_definition__iff_rhs_witness__002))
(check-sat)
(pop 1)
