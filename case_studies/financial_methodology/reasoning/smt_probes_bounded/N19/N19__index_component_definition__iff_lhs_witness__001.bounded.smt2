(set-logic ALL)
(set-option :produce-unsat-cores true)

(declare-sort FinancialInstrument 0)
(declare-sort Index 0)

(declare-fun Security (FinancialInstrument) Bool)

(declare-const TheIndex Index)
(declare-const W_s_Security FinancialInstrument)

(assert (! (Security W_s_Security) :named TYPE_witness_W_s_Security))

(declare-fun index_component (FinancialInstrument Index) Bool)
(declare-fun security_reflected_in_index (FinancialInstrument Index) Bool)

(assert (! (and (Security W_s_Security) (= (index_component W_s_Security TheIndex) (security_reflected_in_index W_s_Security TheIndex))) :named BOUNDED_TEXT_index_component_definition))

(check-sat)
(push 1)
(assert (! (and (Security W_s_Security) (index_component W_s_Security TheIndex)) :named BOUNDED_PROBE_N19__index_component_definition__iff_lhs_witness__001))
(check-sat)
(pop 1)
