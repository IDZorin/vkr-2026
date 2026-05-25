(set-logic ALL)
(set-option :produce-unsat-cores true)

(declare-sort Event 0)
(declare-sort Day 0)

(declare-fun ThirdFriday (Event) Day)
(declare-fun TradingDay (Day) Bool)
(declare-fun NextTradingDay (Day) Day)
(declare-fun RebalanceDay (Event) Day)

(assert (! (forall ((e Event))
  (= (RebalanceDay e) (ThirdFriday e)))
  :named TEXT_S1))

(assert (! (forall ((e Event))
  (=> (not (TradingDay (ThirdFriday e)))
      (= (RebalanceDay e) (NextTradingDay (ThirdFriday e)))))
  :named TEXT_S2))

(assert (! (forall ((e Event))
  (=> (not (TradingDay (ThirdFriday e)))
      (and (= (RebalanceDay e) (ThirdFriday e))
           (not (= (RebalanceDay e) (NextTradingDay (ThirdFriday e)))))))
  :named TEXT_S3))

(check-sat)
(push 1)
(assert (! (exists ((e Event))
  (not (TradingDay (ThirdFriday e))))
  :named PROBE_non_trading_third_friday))
(check-sat)
(get-unsat-core)
(pop 1)
