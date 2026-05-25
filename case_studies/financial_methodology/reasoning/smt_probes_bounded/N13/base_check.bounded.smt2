(set-logic ALL)
(set-option :produce-unsat-cores true)

(declare-sort DataVendor 0)
(declare-sort Day 0)
(declare-sort FinancialInstrument 0)
(declare-sort MonetaryAmount 0)
(declare-sort ShareClass 0)

(declare-fun ClosingPrice (MonetaryAmount) Bool)
(declare-fun FreeFloatMarketCapitalization (MonetaryAmount) Bool)
(declare-fun Security (FinancialInstrument) Bool)
(declare-fun SelectionDay (Day) Bool)
(declare-fun ShareCount (Int) Bool)

(declare-const W_d_SelectionDay Day)
(declare-const W_s_Security FinancialInstrument)
(declare-const W_vendor_DataVendor DataVendor)

(assert (! (SelectionDay W_d_SelectionDay) :named TYPE_witness_W_d_SelectionDay))
(assert (! (Security W_s_Security) :named TYPE_witness_W_s_Security))

(declare-fun closing_price_of_share_class (Day ShareClass) MonetaryAmount)
(declare-fun free_float_market_capitalization (Day FinancialInstrument) MonetaryAmount)
(declare-fun fulfills_index_component_requirements (Day FinancialInstrument) Bool)
(declare-fun share_class (Day FinancialInstrument) ShareClass)
(declare-fun shares_outstanding_in_free_float (Day ShareClass) Int)
(declare-fun sourced_from_data_vendor (Int DataVendor) Bool)

(assert (! (and (SelectionDay W_d_SelectionDay) (and (Security W_s_Security) (=> (fulfills_index_component_requirements W_d_SelectionDay W_s_Security) (and (= (free_float_market_capitalization W_d_SelectionDay W_s_Security) (* (shares_outstanding_in_free_float W_d_SelectionDay (share_class W_d_SelectionDay W_s_Security)) (closing_price_of_share_class W_d_SelectionDay (share_class W_d_SelectionDay W_s_Security)))) (sourced_from_data_vendor (shares_outstanding_in_free_float W_d_SelectionDay (share_class W_d_SelectionDay W_s_Security)) W_vendor_DataVendor))))) :named BOUNDED_TEXT_free_float_market_capitalization_calculated_as_multiplication_definition))
(check-sat)
