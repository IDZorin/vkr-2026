(set-logic ALL)
(set-option :produce-unsat-cores true)

(declare-sort Index 0)
(declare-sort RoundingPrecision 0)

(declare-fun DecimalPlaceCount (Int) Bool)
(declare-fun IndexLevel (Real) Bool)

(declare-const TheIndex Index)
(declare-const TwoDecimalPlaces RoundingPrecision)

(declare-fun decimal_place_count (RoundingPrecision) Int)
(declare-fun level_of_index (Real Index) Bool)
(declare-fun rounded_to_precision (Real RoundingPrecision) Bool)

(assert (! (forall ((decimal_place_count_arg0 RoundingPrecision)) (DecimalPlaceCount (decimal_place_count decimal_place_count_arg0))) :named TYPE_symbol_decimal_place_count))
(assert (! (forall ((level_of_index_arg0 Real) (level_of_index_arg1 Index)) (=> (level_of_index level_of_index_arg0 level_of_index_arg1) (IndexLevel level_of_index_arg0))) :named TYPE_symbol_level_of_index))
(assert (! (forall ((rounded_to_precision_arg0 Real) (rounded_to_precision_arg1 RoundingPrecision)) (=> (rounded_to_precision rounded_to_precision_arg0 rounded_to_precision_arg1) (IndexLevel rounded_to_precision_arg0))) :named TYPE_symbol_rounded_to_precision))

(assert (! (= (decimal_place_count TwoDecimalPlaces) 2) :named TEXT_two_decimal_places_precision))
(assert (! (forall ((l Real)) (=> (IndexLevel l) (=> (level_of_index l TheIndex) (rounded_to_precision l TwoDecimalPlaces)))) :named TEXT_index_level_rounded_to_two_decimal_places))
(check-sat)
