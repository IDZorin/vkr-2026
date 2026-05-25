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
(declare-const W_c_IndexComponent FinancialInstrument)
(declare-const W_l_Listing Listing)

(assert (! (IndexComponent W_c_IndexComponent) :named TYPE_witness_W_c_IndexComponent))

(declare-fun listing_component (Listing FinancialInstrument) Bool)
(declare-fun listing_determined_in_accordance_with_rules (Listing Rules) Bool)
(declare-fun listing_exchange (Listing Exchange) Bool)
(declare-fun respective_exchange_for_index_component (Index FinancialInstrument) Exchange)

(assert (! (and (IndexComponent W_c_IndexComponent) (and (listing_component W_l_Listing W_c_IndexComponent) (listing_determined_in_accordance_with_rules W_l_Listing Section2Rules) (= (respective_exchange_for_index_component TheIndex W_c_IndexComponent) (listing_exchange W_l_Listing)))) :named BOUNDED_TEXT_exchange_definition))
(check-sat)
