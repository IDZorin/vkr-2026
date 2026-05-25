(set-logic ALL)
(set-option :produce-unsat-cores true)

(declare-sort DocumentPart 0)
(declare-sort FinancialInstrument 0)
(declare-sort GbsIndex 0)

(declare-fun Security (FinancialInstrument) Bool)

(declare-const GbsIndexSpecifiedInSection2_1 GbsIndex)
(declare-const Section2_1 DocumentPart)

(declare-fun gbs_index_component (FinancialInstrument GbsIndex) Bool)
(declare-fun gbs_index_specified_in_section (GbsIndex DocumentPart) Bool)
(declare-fun security_reflected_in_gbs_index (FinancialInstrument GbsIndex) Bool)

(assert (! (forall ((gbs_index_component_arg0 FinancialInstrument) (gbs_index_component_arg1 GbsIndex)) (=> (gbs_index_component gbs_index_component_arg0 gbs_index_component_arg1) (Security gbs_index_component_arg0))) :named TYPE_symbol_gbs_index_component))
(assert (! (forall ((security_reflected_in_gbs_index_arg0 FinancialInstrument) (security_reflected_in_gbs_index_arg1 GbsIndex)) (=> (security_reflected_in_gbs_index security_reflected_in_gbs_index_arg0 security_reflected_in_gbs_index_arg1) (Security security_reflected_in_gbs_index_arg0))) :named TYPE_symbol_security_reflected_in_gbs_index))

(assert (! (gbs_index_specified_in_section GbsIndexSpecifiedInSection2_1 Section2_1) :named TEXT_gbs_index_specified_in_section_2_1))
(assert (! (forall ((s FinancialInstrument)) (=> (Security s) (= (gbs_index_component s GbsIndexSpecifiedInSection2_1) (security_reflected_in_gbs_index s GbsIndexSpecifiedInSection2_1)))) :named TEXT_gbs_index_component_definition))
; Probe N15__gbs_index_component_definition__iff_rhs_witness__002: iff_rhs_witness
(check-sat)
(push 1)
(assert (! (exists ((s FinancialInstrument)) (and (Security s) (security_reflected_in_gbs_index s GbsIndexSpecifiedInSection2_1))) :named PROBE_N15__gbs_index_component_definition__iff_rhs_witness__002))
(check-sat)
(pop 1)
