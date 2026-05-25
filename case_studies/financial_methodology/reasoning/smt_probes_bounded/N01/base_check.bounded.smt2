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

(declare-const W_c_IndexComponent FinancialInstrument)
(declare-const W_p_SpecifiedPeriod Period)

(assert (! (IndexComponent W_c_IndexComponent) :named TYPE_witness_W_c_IndexComponent))
(assert (! (SpecifiedPeriod W_p_SpecifiedPeriod) :named TYPE_witness_W_p_SpecifiedPeriod))

(declare-fun average_daily_value_traded (FinancialInstrument Period) Real)
(declare-fun daily_value_traded (FinancialInstrument Day) Real)
(declare-fun daily_value_traded_sum_over_period (FinancialInstrument Period) Real)
(declare-fun trading_day_count_in_period (Period) Int)
(declare-fun trading_day_falls_in_period (Day Period) Bool)

(assert (! (and (IndexComponent W_c_IndexComponent) (and (SpecifiedPeriod W_p_SpecifiedPeriod) (= (average_daily_value_traded W_c_IndexComponent W_p_SpecifiedPeriod) (/ (daily_value_traded_sum_over_period W_c_IndexComponent W_p_SpecifiedPeriod) (trading_day_count_in_period W_p_SpecifiedPeriod))))) :named BOUNDED_TEXT_average_daily_value_traded_divided_by_trading_day_count_definition))
(check-sat)
