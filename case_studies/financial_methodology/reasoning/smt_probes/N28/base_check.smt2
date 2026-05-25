(set-logic ALL)
(set-option :produce-unsat-cores true)

(declare-sort DefinedTerm 0)
(declare-sort DocumentPart 0)

(declare-const IntroductionSection DocumentPart)
(declare-const SolactiveTerm DefinedTerm)

(declare-fun term_shall_have_meaning_defined_in_section (DefinedTerm DocumentPart) Bool)

(assert (! (term_shall_have_meaning_defined_in_section SolactiveTerm IntroductionSection) :named TEXT_solactive_meaning_defined_in_introduction))
(check-sat)
