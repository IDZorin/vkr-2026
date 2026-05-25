(set-logic ALL)
(set-option :produce-unsat-cores true)

(declare-sort DefinedTerm 0)
(declare-sort DocumentPart 0)

(declare-const Section1_3 DocumentPart)
(declare-const StartDateTerm DefinedTerm)

(declare-fun term_shall_have_meaning_defined_in_section (DefinedTerm DocumentPart) Bool)

(assert (! (term_shall_have_meaning_defined_in_section StartDateTerm Section1_3) :named TEXT_start_date_meaning_defined_in_section_1_3))
(check-sat)
