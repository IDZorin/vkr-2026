(set-logic ALL)
(set-option :produce-unsat-cores true)

(declare-sort FinancialInstrument 0)
(declare-sort Index 0)

(declare-fun Security (FinancialInstrument) Bool)

(declare-const TheIndex Index)

(declare-fun index_component (FinancialInstrument Index) Bool)
(declare-fun security_reflected_in_index (FinancialInstrument Index) Bool)

(assert (! (forall ((index_component_arg0 FinancialInstrument) (index_component_arg1 Index)) (=> (index_component index_component_arg0 index_component_arg1) (Security index_component_arg0))) :named TYPE_symbol_index_component))
(assert (! (forall ((security_reflected_in_index_arg0 FinancialInstrument) (security_reflected_in_index_arg1 Index)) (=> (security_reflected_in_index security_reflected_in_index_arg0 security_reflected_in_index_arg1) (Security security_reflected_in_index_arg0))) :named TYPE_symbol_security_reflected_in_index))

(assert (! (forall ((s FinancialInstrument)) (=> (Security s) (= (index_component s TheIndex) (security_reflected_in_index s TheIndex)))) :named TEXT_index_component_definition))
; Probe N19__index_component_definition__iff_rhs_witness__002: iff_rhs_witness
(check-sat)
(push 1)
(assert (! (exists ((s FinancialInstrument)) (and (Security s) (security_reflected_in_index s TheIndex))) :named PROBE_N19__index_component_definition__iff_rhs_witness__002))
(check-sat)
(pop 1)
