(set-logic ALL)
(set-option :produce-unsat-cores true)

(declare-sort Day 0)

(declare-fun fixing_day (Day) Bool)
(declare-fun selection_day (Day) Bool)

(assert (! (forall ((d Day)) (= (fixing_day d) (selection_day d))) :named TEXT_fixing_day_definition))
; Probe N11__fixing_day_definition__iff_lhs_witness__001: iff_lhs_witness
(check-sat)
(push 1)
(assert (! (exists ((d Day)) (fixing_day d)) :named PROBE_N11__fixing_day_definition__iff_lhs_witness__001))
(check-sat)
(pop 1)
