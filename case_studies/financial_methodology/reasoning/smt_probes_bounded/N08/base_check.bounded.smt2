(set-logic ALL)
(set-option :produce-unsat-cores true)

(declare-sort Day 0)
(declare-sort Exchange 0)
(declare-sort FinancialInstrument 0)
(declare-sort MonetaryAmount 0)

(declare-fun ClosingPrice (MonetaryAmount) Bool)
(declare-fun DailyValueTraded (MonetaryAmount) Bool)
(declare-fun IndexComponent (FinancialInstrument) Bool)
(declare-fun TradingDay (Day) Bool)
(declare-fun VolumeNumberOfShares (Int) Bool)

(declare-const W_c_IndexComponent FinancialInstrument)
(declare-const W_d_TradingDay Day)

(assert (! (IndexComponent W_c_IndexComponent) :named TYPE_witness_W_c_IndexComponent))
(assert (! (TradingDay W_d_TradingDay) :named TYPE_witness_W_d_TradingDay))

(declare-fun closing_price (FinancialInstrument Day) MonetaryAmount)
(declare-fun daily_value_traded (FinancialInstrument Day) MonetaryAmount)
(declare-fun respective_exchange (FinancialInstrument) Exchange)
(declare-fun volume_number_of_shares (FinancialInstrument Day) Int)
(declare-fun volume_on_exchange_during_trading_day (Int Exchange) Bool)

(assert (! (and (IndexComponent W_c_IndexComponent) (and (TradingDay W_d_TradingDay) (and (= (daily_value_traded W_c_IndexComponent W_d_TradingDay) (* (closing_price W_c_IndexComponent W_d_TradingDay) (volume_number_of_shares W_c_IndexComponent W_d_TradingDay))) (volume_on_exchange_during_trading_day (volume_number_of_shares W_c_IndexComponent W_d_TradingDay) (respective_exchange W_c_IndexComponent))))) :named BOUNDED_TEXT_daily_value_traded_product_definition))
(check-sat)
