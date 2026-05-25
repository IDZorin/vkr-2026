(set-logic ALL)
(set-option :produce-unsat-cores true)

(declare-sort Day 0)
(declare-sort FinancialInstrument 0)
(declare-sort Period 0)

(declare-fun AverageDailyValueTraded (Real) Bool)
(declare-fun DailyValueTraded (Real) Bool)
(declare-fun IndexComponent (FinancialInstrument) Bool)
(declare-fun SpecifiedPeriod (Period) Bool)
(declare-fun TradingDay (Day) Bool)
(declare-fun TradingDayCount (Int) Bool)

(declare-fun average_daily_value_traded (FinancialInstrument Period) Real)
(declare-fun daily_value_traded (FinancialInstrument Day) Real)
(declare-fun daily_value_traded_sum_over_period (FinancialInstrument Period) Real)
(declare-fun trading_day_count_in_period (Period) Int)
(declare-fun trading_day_falls_in_period (Day Period) Bool)

(assert (! (forall ((average_daily_value_traded_arg0 FinancialInstrument) (average_daily_value_traded_arg1 Period)) (AverageDailyValueTraded (average_daily_value_traded average_daily_value_traded_arg0 average_daily_value_traded_arg1))) :named TYPE_symbol_average_daily_value_traded))
(assert (! (forall ((daily_value_traded_arg0 FinancialInstrument) (daily_value_traded_arg1 Day)) (DailyValueTraded (daily_value_traded daily_value_traded_arg0 daily_value_traded_arg1))) :named TYPE_symbol_daily_value_traded))
(assert (! (forall ((daily_value_traded_sum_over_period_arg0 FinancialInstrument) (daily_value_traded_sum_over_period_arg1 Period)) (DailyValueTraded (daily_value_traded_sum_over_period daily_value_traded_sum_over_period_arg0 daily_value_traded_sum_over_period_arg1))) :named TYPE_symbol_daily_value_traded_sum_over_period))
(assert (! (forall ((trading_day_count_in_period_arg0 Period)) (TradingDayCount (trading_day_count_in_period trading_day_count_in_period_arg0))) :named TYPE_symbol_trading_day_count_in_period))
(assert (! (forall ((trading_day_falls_in_period_arg0 Day) (trading_day_falls_in_period_arg1 Period)) (=> (trading_day_falls_in_period trading_day_falls_in_period_arg0 trading_day_falls_in_period_arg1) (and (TradingDay trading_day_falls_in_period_arg0) (SpecifiedPeriod trading_day_falls_in_period_arg1)))) :named TYPE_symbol_trading_day_falls_in_period))

(assert (! (forall ((c FinancialInstrument)) (=> (IndexComponent c) (forall ((p Period)) (=> (SpecifiedPeriod p) (= (average_daily_value_traded c p) (/ (daily_value_traded_sum_over_period c p) (trading_day_count_in_period p))))))) :named TEXT_average_daily_value_traded_divided_by_trading_day_count_definition))
(check-sat)
