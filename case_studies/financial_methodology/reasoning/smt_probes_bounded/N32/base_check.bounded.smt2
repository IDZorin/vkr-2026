(set-logic ALL)
(set-option :produce-unsat-cores true)

(declare-sort DefinedTerm 0)
(declare-sort DocumentPart 0)

(declare-const Section1_4 DocumentPart)
(declare-const WMRefinitivRateTerm DefinedTerm)

(declare-fun term_shall_have_meaning_defined_in_section (DefinedTerm DocumentPart) Bool)

(assert (! (term_shall_have_meaning_defined_in_section WMRefinitivRateTerm Section1_4) :named BOUNDED_TEXT_wm_refinitiv_rate_meaning_defined_in_section_1_4))
(check-sat)
