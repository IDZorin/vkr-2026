(set-logic ALL)
(set-option :produce-unsat-cores true)

(declare-sort Day 0)

(declare-const W_d_Day Day)

(declare-fun business_day (Day) Bool)
(check-sat)
