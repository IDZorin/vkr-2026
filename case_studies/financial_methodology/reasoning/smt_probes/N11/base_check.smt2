(set-logic ALL)
(set-option :produce-unsat-cores true)

(declare-sort Day 0)

(declare-fun fixing_day (Day) Bool)
(declare-fun selection_day (Day) Bool)

(assert (! (forall ((d Day)) (= (fixing_day d) (selection_day d))) :named TEXT_fixing_day_definition))
(check-sat)
