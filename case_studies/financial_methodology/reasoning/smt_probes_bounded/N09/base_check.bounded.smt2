(set-logic ALL)
(set-option :produce-unsat-cores true)

(declare-sort Day 0)
(declare-sort Exchange 0)

(declare-fun EligibleRebalanceDay (Day) Bool)

(declare-const EUREXExchange Exchange)
(declare-const LondonStockExchange Exchange)
(declare-const NewYorkStockExchange Exchange)
(declare-const TokyoStockExchange Exchange)
(declare-const W_d_EligibleRebalanceDay Day)

(assert (! (EligibleRebalanceDay W_d_EligibleRebalanceDay) :named TYPE_witness_W_d_EligibleRebalanceDay))

(declare-fun eligible_rebalance_day (Day) Bool)
(declare-fun trading_day_at_exchange (Day Exchange) Bool)

(assert (! (and (EligibleRebalanceDay W_d_EligibleRebalanceDay) (= (eligible_rebalance_day W_d_EligibleRebalanceDay) (and (trading_day_at_exchange W_d_EligibleRebalanceDay NewYorkStockExchange) (trading_day_at_exchange W_d_EligibleRebalanceDay LondonStockExchange) (trading_day_at_exchange W_d_EligibleRebalanceDay EUREXExchange) (trading_day_at_exchange W_d_EligibleRebalanceDay TokyoStockExchange)))) :named BOUNDED_TEXT_eligible_rebalance_day_definition))
(check-sat)
