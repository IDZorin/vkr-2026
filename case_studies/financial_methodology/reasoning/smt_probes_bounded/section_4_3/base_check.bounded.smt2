(set-logic ALL)
(set-option :produce-unsat-cores true)

(declare-sort Index 0)
(declare-sort RoundingPrecision 0)

(declare-fun DecimalPlaceCount (Int) Bool)
(declare-fun IndexLevel (Real) Bool)

(declare-const TheIndex Index)
(declare-const TwoDecimalPlaces RoundingPrecision)
(declare-const W_l_IndexLevel Real)

(assert (! (IndexLevel W_l_IndexLevel) :named TYPE_witness_W_l_IndexLevel))

(declare-fun decimal_place_count (RoundingPrecision) Int)
(declare-fun level_of_index (Real Index) Bool)
(declare-fun rounded_to_precision (Real RoundingPrecision) Bool)

(assert (! (= (decimal_place_count TwoDecimalPlaces) 2) :named BOUNDED_TEXT_two_decimal_places_precision))
(assert (! (and (IndexLevel W_l_IndexLevel) (=> (level_of_index W_l_IndexLevel TheIndex) (rounded_to_precision W_l_IndexLevel TwoDecimalPlaces))) :named BOUNDED_TEXT_index_level_rounded_to_two_decimal_places))
(check-sat)
