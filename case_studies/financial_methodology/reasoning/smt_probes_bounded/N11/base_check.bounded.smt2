(set-logic ALL)
(set-option :produce-unsat-cores true)

(declare-sort Day 0)

(declare-const W_d_Day Day)

(declare-fun fixing_day (Day) Bool)
(declare-fun selection_day (Day) Bool)

(assert (! (= (fixing_day W_d_Day) (selection_day W_d_Day)) :named BOUNDED_TEXT_fixing_day_definition))
(check-sat)
