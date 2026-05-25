(set-logic ALL)
(set-option :produce-unsat-cores true)

(declare-sort DefinedTerm 0)
(declare-sort DocumentPart 0)

(declare-const IndexUniverseRequirementsTerm DefinedTerm)
(declare-const Section2_1 DocumentPart)

(declare-fun term_shall_have_meaning_defined_in_section (DefinedTerm DocumentPart) Bool)

(assert (! (term_shall_have_meaning_defined_in_section IndexUniverseRequirementsTerm Section2_1) :named BOUNDED_TEXT_index_universe_requirements_meaning_defined_in_section_2_1))
(check-sat)
