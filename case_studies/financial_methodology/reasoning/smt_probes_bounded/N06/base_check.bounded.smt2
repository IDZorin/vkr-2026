(set-logic ALL)
(set-option :produce-unsat-cores true)

(declare-sort CalculationTime 0)
(declare-sort DocumentPart 0)
(declare-sort Index 0)

(declare-const CloseOfBusiness CalculationTime)
(declare-const Section1_4 DocumentPart)
(declare-const TheIndex Index)

(declare-fun calculation_time_of_closing_level_of_index (CalculationTime Index) Bool)
(declare-fun outlined_in_section (CalculationTime DocumentPart) Bool)

(assert (! (and (calculation_time_of_closing_level_of_index CloseOfBusiness TheIndex) (outlined_in_section CloseOfBusiness Section1_4)) :named BOUNDED_TEXT_close_of_business_definition))
(check-sat)
