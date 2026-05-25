(set-logic ALL)
(set-option :produce-unsat-cores true)

(declare-sort Index 0)
(declare-sort Rebalance 0)

(declare-fun ExtraordinaryRebalance (Rebalance) Bool)

(declare-const TheIndex Index)

(declare-fun rebalance_of_index (Rebalance Index) Bool)

(assert (! (forall ((r Rebalance)) (=> (ExtraordinaryRebalance r) (not (rebalance_of_index r TheIndex)))) :named TEXT_index_not_rebalanced_extraordinarily))
; Probe section_3_2__index_not_rebalanced_extraordinarily__negative_condition_witness__001: negative_condition_witness
(check-sat)
(push 1)
(assert (! (exists ((r Rebalance)) (and (ExtraordinaryRebalance r) (not (rebalance_of_index r TheIndex)))) :named PROBE_section_3_2__index_not_rebalanced_extraordinarily__negative_condition_witness__001))
(check-sat)
(pop 1)
