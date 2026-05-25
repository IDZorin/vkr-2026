(set-logic ALL)
(set-option :produce-unsat-cores true)

(declare-sort Day 0)
(declare-sort FloatMarketCapizatlization 0)
(declare-sort IndexComponent 0)
(declare-sort Percent 0)
(declare-sort Region 0)
(declare-sort WeightRedistributionProcess 0)

(declare-fun SelectionDay (Day) Bool)

(declare-const W_c_IndexComponent IndexComponent)
(declare-const W_d_SelectionDay Day)

(assert (! (SelectionDay W_d_SelectionDay) :named TYPE_witness_W_d_SelectionDay))

(declare-fun float_market_capizatlization (Day IndexComponent) FloatMarketCapizatlization)
(declare-fun iterative_process (WeightRedistributionProcess) Bool)
(declare-fun redistributes_weight_proportionally (WeightRedistributionProcess IndexComponent Percent) Bool)
(declare-fun region (IndexComponent) Region)
(declare-fun weight (Day IndexComponent) Percent)
(declare-fun weight_has_float_market_capizatlization_basis (Percent FloatMarketCapizatlization) Bool)
(declare-fun weight_redistribution_process (Day) WeightRedistributionProcess)

(assert (! (and (SelectionDay W_d_SelectionDay) (weight_has_float_market_capizatlization_basis (weight W_d_SelectionDay W_c_IndexComponent) (float_market_capizatlization W_d_SelectionDay W_c_IndexComponent))) :named BOUNDED_TEXT_weight_based_on_float_market_capizatlization))
(assert (! (and (SelectionDay W_d_SelectionDay) (<= (weight W_d_SelectionDay W_c_IndexComponent) (/ 5 100))) :named BOUNDED_TEXT_single_index_component_weight_capped))
(assert (! (and (SelectionDay W_d_SelectionDay) (iterative_process (weight_redistribution_process W_d_SelectionDay))) :named BOUNDED_TEXT_weight_redistribution_process_is_iterative))
(assert (! (and (SelectionDay W_d_SelectionDay) (redistributes_weight_proportionally (weight_redistribution_process W_d_SelectionDay) W_c_IndexComponent (weight W_d_SelectionDay W_c_IndexComponent))) :named BOUNDED_TEXT_weights_redistributed_proportionally))
(check-sat)
