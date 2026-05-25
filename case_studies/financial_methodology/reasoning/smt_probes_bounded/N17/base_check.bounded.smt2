(set-logic ALL)
(set-option :produce-unsat-cores true)

(declare-sort DefinedTerm 0)
(declare-sort DocumentPart 0)

(declare-const IndexTerm DefinedTerm)
(declare-const IntroductionSection DocumentPart)

(declare-fun term_shall_have_meaning_defined_in_section (DefinedTerm DocumentPart) Bool)

(assert (! (term_shall_have_meaning_defined_in_section IndexTerm IntroductionSection) :named BOUNDED_TEXT_index_meaning_defined_in_introduction))
(check-sat)
