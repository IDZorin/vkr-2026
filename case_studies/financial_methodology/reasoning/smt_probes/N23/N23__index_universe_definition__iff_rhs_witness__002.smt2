(set-logic ALL)
(set-option :produce-unsat-cores true)

(declare-sort FinancialInstrument 0)
(declare-sort IndexUniverse 0)
(declare-sort IndexUniverseRequirements 0)

(declare-const TheIndexUniverse IndexUniverse)
(declare-const TheIndexUniverseRequirements IndexUniverseRequirements)

(declare-fun financial_instrument_in_index_universe (FinancialInstrument IndexUniverse) Bool)
(declare-fun fulfills_index_universe_requirements (FinancialInstrument IndexUniverseRequirements) Bool)
(declare-fun index_universe_is_sum_of_financial_instruments_fulfilling_requirements (IndexUniverse IndexUniverseRequirements) Bool)

(assert (! (index_universe_is_sum_of_financial_instruments_fulfilling_requirements TheIndexUniverse TheIndexUniverseRequirements) :named TEXT_index_universe_sum_source_phrase))
(assert (! (forall ((fi FinancialInstrument)) (= (financial_instrument_in_index_universe fi TheIndexUniverse) (fulfills_index_universe_requirements fi TheIndexUniverseRequirements))) :named TEXT_index_universe_definition))
; Probe N23__index_universe_definition__iff_rhs_witness__002: iff_rhs_witness
(check-sat)
(push 1)
(assert (! (exists ((fi FinancialInstrument)) (fulfills_index_universe_requirements fi TheIndexUniverseRequirements)) :named PROBE_N23__index_universe_definition__iff_rhs_witness__002))
(check-sat)
(pop 1)
