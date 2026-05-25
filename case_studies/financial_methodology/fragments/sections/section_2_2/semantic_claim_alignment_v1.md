# Semantic Claim Alignment: section_2_2

This ledger maps source claims to candidate IR blocks. It is a review surface, not a proof.

## Summary

- claim_count: `9`
- strong_candidate_count: `6`
- partial_candidate_count: `2`
- weak_or_missing_candidate_count: `1`
- reviewed_count: `0`
- approved_count: `0`
- needs_revision_count: `0`
- average_top3_token_coverage: `0.796`
- all_claims_review_approved: `False`

## Review Status Values

- `approved`: source claim is faithfully represented by the approved IR block(s).
- `needs_ir_revision`: source claim is missing, distorted, or only present in names.
- `source_ambiguous`: source itself needs interpretation before judging IR.
- `not_formalized_by_design`: claim is intentionally left as metadata/waiver/support text.

## Claims

### C01 `strong_candidate`

> ### 2.2 Selection of the Index Components

- top3 token coverage: `1.0`
- review status: `unreviewed`
- uncovered by top3: none

Candidate IR blocks:
- `declaration:opaque:SelectionOfIndexComponents` line `18` score `0.914`, recall `1.0`
  `sort SelectionOfIndexComponents`
- `declaration:rel:index_component` line `31` score `0.867`, recall `1.0`
  `rel index_component : SelectionDay, Security`
- `declaration:fun:selection_of_index_components` line `24` score `0.857`, recall `1.0`
  `fun[required] selection_of_index_components : SelectionDay -> SelectionOfIndexComponents`
- `declaration:rel:fully_rule_based` line `35` score `0.853`, recall `1.0`
  `rel fully_rule_based : SelectionOfIndexComponents`
- `declaration:prohibition:index_administrator_discretionary_decision` line `96` score `0.85`, recall `1.0`
  `prohibition index_administrator_discretionary_decision( agent: IndexAdministrator, selection: SelectionOfIndexComponents, decision: DiscretionaryDecision ) action: make_discretionary_decision target: decision scope: selection`

### C02 `strong_candidate`

> Based on the Index Universe, the initial composition of the Index as well as any selection for an ordinary rebalance is determined on the Selection Day in accordance with the following rules (the "Index Component Requirements"):

- top3 token coverage: `0.8`
- review status: `unreviewed`
- uncovered by top3: `universe` (Universe), `accordance` (accordance), `follow` (following)

Candidate IR blocks:
- `assertion:constraint:ordinary_rebalance_selection_determined_by_index_component_requirements` line `81` score `0.511`, recall `0.533`
  `constraint ordinary_rebalance_selection_determined_by_index_component_requirements : forall d: SelectionDay, forall s: Security, ordinary_rebalance_selection(d, s) iff selected_for_index_inclusion(d, s)`
- `assertion:constraint:initial_composition_determined_by_index_component_requirements` line `77` score `0.507`, recall `0.533`
  `constraint initial_composition_determined_by_index_component_requirements : forall d: SelectionDay, forall s: Security, initial_composition(d, s) iff selected_for_index_inclusion(d, s)`
- `assertion:constraint:selection_fully_rule_based` line `92` score `0.384`, recall `0.4`
  `constraint selection_fully_rule_based : forall d: SelectionDay, fully_rule_based(selection_of_index_components(d))`
- `declaration:rel:fully_rule_based` line `35` score `0.347`, recall `0.333`
  `rel fully_rule_based : SelectionOfIndexComponents`
- `assertion:constraint:eligible_based_on_index_universe` line `37` score `0.33`, recall `0.333`
  `constraint eligible_based_on_index_universe : forall d: SelectionDay, forall s: Security, eligible(d, s) implies index_universe(d, s)`

### C03 `partial_candidate`

> Each security is classified into one of the two regions
   1.

- top3 token coverage: `0.667`
- review status: `unreviewed`
- uncovered by top3: `one` (one), `two` (two)

Candidate IR blocks:
- `assertion:constraint:europe_country_assignment_classification` line `47` score `0.43`, recall `0.5`
  `constraint europe_country_assignment_classification : forall d: SelectionDay, forall s: Security, eligible(d, s) and gbs_country_assignment(d, s) = Europe implies region(d, s) = EuropeRegion`
- `assertion:constraint:descending_order_by_free_float_market_capizatlization` line `53` score `0.425`, recall `0.5`
  `constraint descending_order_by_free_float_market_capizatlization : forall d: SelectionDay, forall r: Region, forall s1: Security, forall s2: Security, eligible(d, s1) and eligible(d, s2) and region(d, s1) = r and region(d, s2) = r and free_float_market_capizatlization(d, s1) > free_float_market_capizatlization(d, s2) implies rank(d, r, s1) < rank(d, r, s2)`
- `assertion:constraint:americas_country_assignment_classification` line `41` score `0.422`, recall `0.5`
  `constraint americas_country_assignment_classification : forall d: SelectionDay, forall s: Security, eligible(d, s) and (gbs_country_assignment(d, s) = Canada or gbs_country_assignment(d, s) = UnitedStates) implies region(d, s) = Americas`
- `declaration:fun:region` line `26` score `0.333`, recall `0.333`
  `fun[required] region : SelectionDay, Security -> Region`
- `declaration:opaque:Region` line `3` score `0.333`, recall `0.167`
  `sort Region`

### C04 `partial_candidate`

> Americas if the Country Assignment is Canada or United States under the Gbs Index Universe framework
   2.

- top3 token coverage: `0.583`
- review status: `unreviewed`
- uncovered by top3: `under` (under), `index` (Index), `universe` (Universe), `framework` (framework), `2` (2)

Candidate IR blocks:
- `assertion:constraint:americas_country_assignment_classification` line `41` score `0.533`, recall `0.583`
  `constraint americas_country_assignment_classification : forall d: SelectionDay, forall s: Security, eligible(d, s) and (gbs_country_assignment(d, s) = Canada or gbs_country_assignment(d, s) = UnitedStates) implies region(d, s) = Americas`
- `declaration:entity:UnitedStates` line `11` score `0.39`, recall `0.333`
  `entity UnitedStates : CountryAssignment`
- `declaration:entity:Canada` line `10` score `0.333`, recall `0.25`
  `entity Canada : CountryAssignment`
- `declaration:opaque:CountryAssignment` line `8` score `0.283`, recall `0.167`
  `sort CountryAssignment`
- `declaration:fun:gbs_country_assignment` line `25` score `0.257`, recall `0.25`
  `fun[required] gbs_country_assignment : SelectionDay, Security -> CountryAssignment`

### C05 `weak_or_missing_candidate`

> Europe if the Country Assignment is Europe under the Gbs Index Universe framework
2.

- top3 token coverage: `0.444`
- review status: `unreviewed`
- uncovered by top3: `under` (under), `index` (Index), `universe` (Universe), `framework` (framework), `2` (2)

Candidate IR blocks:
- `declaration:entity:Europe` line `12` score `0.4`, recall `0.333`
  `entity Europe : CountryAssignment`
- `assertion:constraint:europe_country_assignment_classification` line `47` score `0.393`, recall `0.444`
  `constraint europe_country_assignment_classification : forall d: SelectionDay, forall s: Security, eligible(d, s) and gbs_country_assignment(d, s) = Europe implies region(d, s) = EuropeRegion`
- `declaration:opaque:CountryAssignment` line `8` score `0.328`, recall `0.222`
  `sort CountryAssignment`
- `declaration:fun:gbs_country_assignment` line `25` score `0.324`, recall `0.333`
  `fun[required] gbs_country_assignment : SelectionDay, Security -> CountryAssignment`
- `assertion:constraint:americas_country_assignment_classification` line `41` score `0.289`, recall `0.333`
  `constraint americas_country_assignment_classification : forall d: SelectionDay, forall s: Security, eligible(d, s) and (gbs_country_assignment(d, s) = Canada or gbs_country_assignment(d, s) = UnitedStates) implies region(d, s) = Americas`

### C06 `strong_candidate`

> Each security is ranked in a descending order by its Free Float Market Capizatlization.

- top3 token coverage: `1.0`
- review status: `unreviewed`
- uncovered by top3: none

Candidate IR blocks:
- `assertion:constraint:descending_order_by_free_float_market_capizatlization` line `53` score `0.869`, recall `1.0`
  `constraint descending_order_by_free_float_market_capizatlization : forall d: SelectionDay, forall r: Region, forall s1: Security, forall s2: Security, eligible(d, s1) and eligible(d, s2) and region(d, s1) = r and region(d, s2) = r and free_float_market_capizatlization(d, s1) > free_float_market_capizatlization(d, s2) implies rank(d, r, s1) < rank(d, r, s2)`
- `declaration:fun:free_float_market_capizatlization` line `27` score `0.582`, recall `0.625`
  `fun[required] free_float_market_capizatlization : SelectionDay, Security -> FreeFloatMarketCapizatlization`
- `declaration:opaque:FreeFloatMarketCapizatlization` line `14` score `0.543`, recall `0.5`
  `sort FreeFloatMarketCapizatlization`
- `declaration:opaque:Rank` line `15` score `0.3`, recall `0.125`
  `sort Rank`
- `declaration:fun:rank` line `28` score `0.26`, recall `0.25`
  `fun[required] rank : SelectionDay, Region, Security -> Rank`

### C07 `strong_candidate`

> The top 20 securities for each region are selected for Index inclusion.

- top3 token coverage: `1.0`
- review status: `unreviewed`
- uncovered by top3: none

Candidate IR blocks:
- `assertion:constraint:selected_top_20_for_each_region` line `62` score `0.886`, recall `1.0`
  `constraint selected_top_20_for_each_region : forall d: SelectionDay, forall s: Security, selected_for_index_inclusion(d, s) iff eligible(d, s) and rank(d, region(d, s), s) <= 20`
- `assertion:constraint:at_most_20_selected_per_region` line `69` score `0.758`, recall `0.857`
  `constraint at_most_20_selected_per_region : forall d: SelectionDay, forall r: Region, count(s in Security where selected_for_index_inclusion(d, s) and region(d, s) = r) <= 20`
- `declaration:rel:selected_for_index_inclusion` line `30` score `0.557`, recall `0.571`
  `rel selected_for_index_inclusion : SelectionDay, Security`
- `assertion:constraint:index_components_selected_for_index_inclusion` line `73` score `0.524`, recall `0.571`
  `constraint index_components_selected_for_index_inclusion : forall d: SelectionDay, forall s: Security, index_component(d, s) iff selected_for_index_inclusion(d, s)`
- `assertion:constraint:initial_composition_determined_by_index_component_requirements` line `77` score `0.505`, recall `0.571`
  `constraint initial_composition_determined_by_index_component_requirements : forall d: SelectionDay, forall s: Security, initial_composition(d, s) iff selected_for_index_inclusion(d, s)`

### C08 `strong_candidate`

> In case less than 20 securities per region are eligible, the Index contains less than 40 Index Components in total.

- top3 token coverage: `0.769`
- review status: `unreviewed`
- uncovered by top3: `case` (case), `contain` (contains), `total` (total)

Candidate IR blocks:
- `assertion:constraint:less_than_20_per_region_less_than_40_index_components` line `85` score `0.704`, recall `0.769`
  `constraint less_than_20_per_region_less_than_40_index_components : forall d: SelectionDay, (exists r: Region, count(s in Security where eligible(d, s) and region(d, s) = r) < 20) implies count(s in Security where index_component(d, s)) < 40`
- `assertion:constraint:selected_top_20_for_each_region` line `62` score `0.365`, recall `0.385`
  `constraint selected_top_20_for_each_region : forall d: SelectionDay, forall s: Security, selected_for_index_inclusion(d, s) iff eligible(d, s) and rank(d, region(d, s), s) <= 20`
- `assertion:constraint:at_most_20_selected_per_region` line `69` score `0.362`, recall `0.385`
  `constraint at_most_20_selected_per_region : forall d: SelectionDay, forall r: Region, count(s in Security where selected_for_index_inclusion(d, s) and region(d, s) = r) <= 20`
- `declaration:rel:index_component` line `31` score `0.274`, recall `0.231`
  `rel index_component : SelectionDay, Security`
- `declaration:opaque:Region` line `3` score `0.262`, recall `0.077`
  `sort Region`

### C09 `strong_candidate`

> The selection of the Index Components is fully rule-based and the Index Administrator cannot make any discretionary decision.

- top3 token coverage: `0.9`
- review status: `unreviewed`
- uncovered by top3: `cannot` (cannot)

Candidate IR blocks:
- `declaration:prohibition:index_administrator_discretionary_decision` line `96` score `0.672`, recall `0.7`
  `prohibition index_administrator_discretionary_decision( agent: IndexAdministrator, selection: SelectionOfIndexComponents, decision: DiscretionaryDecision ) action: make_discretionary_decision target: decision scope: selection`
- `declaration:rel:fully_rule_based` line `35` score `0.52`, recall `0.5`
  `rel fully_rule_based : SelectionOfIndexComponents`
- `assertion:constraint:selection_fully_rule_based` line `92` score `0.482`, recall `0.5`
  `constraint selection_fully_rule_based : forall d: SelectionDay, fully_rule_based(selection_of_index_components(d))`
- `declaration:opaque:SelectionOfIndexComponents` line `18` score `0.354`, recall `0.3`
  `sort SelectionOfIndexComponents`
- `declaration:opaque:DiscretionaryDecision` line `19` score `0.31`, recall `0.2`
  `sort DiscretionaryDecision`
