(set-logic ALL)
(set-option :produce-unsat-cores true)

(declare-sort DefinedTerm 0)
(declare-sort DocumentPart 0)

(declare-const OversightCommitteeTerm DefinedTerm)
(declare-const Section5_5 DocumentPart)

(declare-fun term_shall_have_meaning_defined_in_section (DefinedTerm DocumentPart) Bool)

(assert (! (term_shall_have_meaning_defined_in_section OversightCommitteeTerm Section5_5) :named BOUNDED_TEXT_oversight_committee_meaning_defined_in_section_5_5))
(check-sat)
