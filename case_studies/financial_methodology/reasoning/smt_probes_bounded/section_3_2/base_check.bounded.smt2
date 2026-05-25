(set-logic ALL)
(set-option :produce-unsat-cores true)

(declare-sort Index 0)
(declare-sort Rebalance 0)

(declare-fun ExtraordinaryRebalance (Rebalance) Bool)

(declare-const TheIndex Index)
(declare-const W_r_ExtraordinaryRebalance Rebalance)

(assert (! (ExtraordinaryRebalance W_r_ExtraordinaryRebalance) :named TYPE_witness_W_r_ExtraordinaryRebalance))

(declare-fun rebalance_of_index (Rebalance Index) Bool)

(assert (! (and (ExtraordinaryRebalance W_r_ExtraordinaryRebalance) (not (rebalance_of_index W_r_ExtraordinaryRebalance TheIndex))) :named BOUNDED_TEXT_index_not_rebalanced_extraordinarily))
(check-sat)
