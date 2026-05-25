(set-logic ALL)
(set-option :produce-unsat-cores true)

(declare-sort Exchange 0)
(declare-sort FinancialInstrument 0)
(declare-sort Index 0)
(declare-sort Listing 0)
(declare-sort Rules 0)

(declare-fun IndexComponent (FinancialInstrument) Bool)

(declare-const Section2Rules Rules)
(declare-const TheIndex Index)

(declare-fun listing_component (Listing FinancialInstrument) Bool)
(declare-fun listing_determined_in_accordance_with_rules (Listing Rules) Bool)
(declare-fun listing_exchange (Listing Exchange) Bool)
(declare-fun respective_exchange_for_index_component (Index FinancialInstrument) Exchange)

(assert (! (forall ((listing_component_arg0 Listing) (listing_component_arg1 FinancialInstrument)) (=> (listing_component listing_component_arg0 listing_component_arg1) (IndexComponent listing_component_arg1))) :named TYPE_symbol_listing_component))

(assert (! (forall ((c FinancialInstrument)) (=> (IndexComponent c) (exists ((l Listing)) (and (listing_component l c) (listing_determined_in_accordance_with_rules l Section2Rules) (= (respective_exchange_for_index_component TheIndex c) (listing_exchange l)))))) :named TEXT_exchange_definition))
; Probe N10__exchange_definition__existential_witness__001: existential_witness
(check-sat)
(push 1)
(assert (! (exists ((c FinancialInstrument)) (and (IndexComponent c) (exists ((l Listing)) (and (listing_component l c) (listing_determined_in_accordance_with_rules l Section2Rules) (= (respective_exchange_for_index_component TheIndex c) (listing_exchange l)))))) :named PROBE_N10__exchange_definition__existential_witness__001))
(check-sat)
(pop 1)
