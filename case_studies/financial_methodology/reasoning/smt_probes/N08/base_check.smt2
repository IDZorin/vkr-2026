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

(declare-fun closing_price (FinancialInstrument Day) MonetaryAmount)
(declare-fun daily_value_traded (FinancialInstrument Day) MonetaryAmount)
(declare-fun respective_exchange (FinancialInstrument) Exchange)
(declare-fun volume_traded_on_exchange_during_trading_day (FinancialInstrument Exchange Day) Int)

(assert (! (forall ((closing_price_arg0 FinancialInstrument) (closing_price_arg1 Day)) (ClosingPrice (closing_price closing_price_arg0 closing_price_arg1))) :named TYPE_symbol_closing_price))
(assert (! (forall ((daily_value_traded_arg0 FinancialInstrument) (daily_value_traded_arg1 Day)) (DailyValueTraded (daily_value_traded daily_value_traded_arg0 daily_value_traded_arg1))) :named TYPE_symbol_daily_value_traded))
(assert (! (forall ((volume_traded_on_exchange_during_trading_day_arg0 FinancialInstrument) (volume_traded_on_exchange_during_trading_day_arg1 Exchange) (volume_traded_on_exchange_during_trading_day_arg2 Day)) (VolumeNumberOfShares (volume_traded_on_exchange_during_trading_day volume_traded_on_exchange_during_trading_day_arg0 volume_traded_on_exchange_during_trading_day_arg1 volume_traded_on_exchange_during_trading_day_arg2))) :named TYPE_symbol_volume_traded_on_exchange_during_trading_day))

(assert (! (forall ((c FinancialInstrument)) (=> (IndexComponent c) (forall ((d Day)) (=> (TradingDay d) (= (daily_value_traded c d) (* (closing_price c d) (volume_traded_on_exchange_during_trading_day c (respective_exchange c) d))))))) :named TEXT_daily_value_traded_product_definition))
(check-sat)
