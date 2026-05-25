(set-logic ALL)
(set-option :produce-unsat-cores true)

(declare-sort DocumentPart 0)
(declare-sort FinancialInstrument 0)
(declare-sort GbsIndex 0)

(declare-fun Security (FinancialInstrument) Bool)

(declare-const GbsIndexSpecifiedInSection2_1 GbsIndex)
(declare-const Section2_1 DocumentPart)
(declare-const W_s_Security FinancialInstrument)

(assert (! (Security W_s_Security) :named TYPE_witness_W_s_Security))

(declare-fun gbs_index_component (FinancialInstrument GbsIndex) Bool)
(declare-fun gbs_index_specified_in_section (GbsIndex DocumentPart) Bool)
(declare-fun security_reflected_in_gbs_index (FinancialInstrument GbsIndex) Bool)

(assert (! (gbs_index_specified_in_section GbsIndexSpecifiedInSection2_1 Section2_1) :named BOUNDED_TEXT_gbs_index_specified_in_section_2_1))
(assert (! (and (Security W_s_Security) (= (gbs_index_component W_s_Security GbsIndexSpecifiedInSection2_1) (security_reflected_in_gbs_index W_s_Security GbsIndexSpecifiedInSection2_1))) :named BOUNDED_TEXT_gbs_index_component_definition))

(check-sat)
(push 1)
(assert (! (and (Security W_s_Security) (security_reflected_in_gbs_index W_s_Security GbsIndexSpecifiedInSection2_1)) :named BOUNDED_PROBE_N15__gbs_index_component_definition__iff_rhs_witness__002))
(check-sat)
(pop 1)
