(set-logic ALL)
(set-option :produce-unsat-cores true)

(declare-sort Day 0)
(declare-const scheduled_day Day)
(declare-const following_day Day)

(declare-fun scheduled_rebalance_day (Day) Bool)
(declare-fun trading_day (Day) Bool)
(declare-fun immediately_following_trading_day_after (Day Day) Bool)
(declare-fun rebalance_day (Day) Bool)

; Source clause 2: fallback to the immediately following trading day.
(assert (!
  (forall ((s Day) (d Day))
    (=> (and
          (scheduled_rebalance_day s)
          (not (trading_day s))
          (immediately_following_trading_day_after d s))
        (rebalance_day d)))
  :named fallback_to_following_trading_day))

; Source clause 3: fixed date / no postponement in the same scenario.
(assert (!
  (forall ((s Day) (d Day))
    (=> (and
          (scheduled_rebalance_day s)
          (not (trading_day s))
          (immediately_following_trading_day_after d s))
        (not (rebalance_day d))))
  :named fixed_date_no_postponement_claim))

; Witness scenario: the scheduled day is not a trading day and has a following trading day.
(assert (!
  (and
    (scheduled_rebalance_day scheduled_day)
    (not (trading_day scheduled_day))
    (immediately_following_trading_day_after following_day scheduled_day))
  :named scheduled_non_trading_witness))

(check-sat)
(get-unsat-core)
