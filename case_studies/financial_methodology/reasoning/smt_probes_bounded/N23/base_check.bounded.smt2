(set-logic ALL)
(set-option :produce-unsat-cores true)

(declare-sort FinancialInstrument 0)
(declare-sort IndexUniverse 0)
(declare-sort IndexUniverseRequirements 0)

(declare-const TheIndexUniverse IndexUniverse)
(declare-const TheIndexUniverseRequirements IndexUniverseRequirements)
(declare-const W_fi_FinancialInstrument FinancialInstrument)

(declare-fun financial_instrument_in_index_universe (FinancialInstrument IndexUniverse) Bool)
(declare-fun fulfills_index_universe_requirements (FinancialInstrument IndexUniverseRequirements) Bool)
(declare-fun index_universe_is_sum_of_financial_instruments_fulfilling_requirements (IndexUniverse IndexUniverseRequirements) Bool)

(assert (! (index_universe_is_sum_of_financial_instruments_fulfilling_requirements TheIndexUniverse TheIndexUniverseRequirements) :named BOUNDED_TEXT_index_universe_sum_source_phrase))
(assert (! (= (financial_instrument_in_index_universe W_fi_FinancialInstrument TheIndexUniverse) (fulfills_index_universe_requirements W_fi_FinancialInstrument TheIndexUniverseRequirements)) :named BOUNDED_TEXT_index_universe_definition))
(check-sat)
