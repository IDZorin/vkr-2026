(set-logic ALL)
(set-option :produce-unsat-cores true)

(declare-sort DefinedTerm 0)
(declare-sort DocumentPart 0)

(declare-const IndexComponentRequirementsTerm DefinedTerm)
(declare-const Section2_2 DocumentPart)

(declare-fun term_shall_have_meaning_defined_in_section (DefinedTerm DocumentPart) Bool)

(assert (! (term_shall_have_meaning_defined_in_section IndexComponentRequirementsTerm Section2_2) :named TEXT_index_component_requirements_meaning_defined_in_section_2_2))
(check-sat)
