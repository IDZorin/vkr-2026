# Section 2.1 Translator Notes

This file records translator decisions for the current `main_ir.a4v3`.
It is review memory, not an additional source of methodology claims.

## Changelog

### 2026-05-17T00:45:00+02:00

Decision: expose lookback month counts as numeric arguments instead of encoding `one` and `six` in separate function names.

Accepted:

- Replaced `one_month_prior_including_selection_day` and `six_months_prior_including_selection_day` with `months_prior_including_selection_day(MonthCount, SelectionDay)`.
- Added `OneMonth = 1` and `SixMonths = 6` as explicit numeric facts.
- Kept the source distinction between the 1-month and 6-month windows by passing `OneMonth` and `SixMonths` as arguments where the windows are used.

Rationale:

- Numeric quantities that affect formula semantics should be machine-visible as values, not only recoverable from identifier spelling.
- This preserves the existing source semantics while making the model extensible if another lookback month count appears later.

### 2026-05-09T14:01:30+02:00

Decision: tighten two local modeling points after semantic-lint / reviewer feedback.

Accepted:

- `MonthCount` now extends `Nat`, because `months_over(...) = 1` and
  `months_over(...) = 6` use numeric literals. This follows the same convention
  as numeric `Rank` and monetary ADVT/FMC quantities in adjacent sections.
- Removed the bridge-only `gbs_index_universe_starting_list_definition` and its
  helper `starting_list_of_financial_instruments` / `security_in_starting_list_of_financial_instruments`
  declarations. The main eligibility rule now uses
  `part_component_of_gbs_index_universe(...)` directly, matching the source
  phrase "Part/ Component of the GBS Index Universe".

Rejected / deferred:

- The document-part URL / locator facts stay in `main_ir.a4v3` for now. They are
  already marked as `bridge` / `ir_internal_bridge` in `provenance.yaml`.
  We are not introducing a separate `infrastructure.a4v3` overlay in this pass;
  if that split is adopted later, those three facts are the first candidates to
  move.

Rationale:

- Numeric sorts should not remain opaque when they are compared with numeric
  literals.
- A bridge is useful only when it connects concepts that are both needed. Here
  the prelude "starting list" predicate was not used anywhere except to define
  the local source-faithful predicate, so it was extra indirection rather than
  semantic content.

### 2026-05-09T12:00:00+02:00

Decision: clarify the role of `AvoidFrequentChangesBetweenTwoShareClasses : VagueTerm` as an
intentional anchor without formula link.

Accepted:

- The entity is declared as a `VagueTerm` and intentionally does not appear in any
  constraint body. It is an unused-by-formula concept anchor by design, not by oversight.

Rationale:

- The source phrase `To avoid frequent changes between two share-classes` is the stated
  motivation for the buffer rules, not a separate computable claim. The word `frequent`
  is the same kind of qualitative qualifier as `significant`, `reasonable`,
  `material`, or `substantially` — we have no precise computational meaning for it
  beyond what the buffer rules already encode.
- The buffer rules themselves (`CurrentCompanyBufferRule`, `NotCurrentCompanyBufferRule`)
  are the operational realization of the anti-flapping intent. The `VagueTerm` anchor
  preserves source-phrase traceability without pretending we have an independent
  formal definition for `frequent`.
- This is the recommended pattern when the source provides motivation but no separate
  computable rule. The semantic-lint `unused_declaration` finding for this entity is
  expected and approved here.

Alternative considered:

- Linking the anchor to the buffer rules with `rel motivation_of : VagueTerm, IndexBufferRule`
  and a corresponding `fact buffer_rules_motivation`. Rejected for now because it would
  create a one-off relation just to satisfy the linter and overstate the formal status of
  the motivation. Reconsider if/when other sections need the same `motivation_of` pattern;
  then it can be promoted to a reusable prelude relation.

### 2026-05-08T11:16:40+02:00

Decision: mark `determination_of_index_universe_fully_rule_based` as `fact`, not `constraint`.

Accepted:

- `fully_rule_based(determination_of_index_universe(d))` remains explicit for every `SelectionDay`.
- The declaration is now a `fact` because the source states a descriptive governance property of the determination process, not a numeric eligibility condition or checkable admissibility constraint.

Rationale: this follows the same convention adopted for section 2.3: universal descriptive/procedural atoms are represented as `fact`; hard requirements such as eligibility biconditionals, counts, thresholds, and buffer rules remain `constraint`.

### 2026-05-06T17:27:25+02:00

Decision: represent the Index Universe Requirements as a biconditional eligibility rule with explicit reusable requirement components.

Accepted:

- The source phrase `Part/ Component of the GBS Index Universe... on a Selection Day` is represented through `StartingListOfFinancialInstruments`, not by a vague `InitialFinancialInstrumentUniverse`.
- The GBS Benchmark Series PDF URL and document-part provenance are preserved explicitly.
- Developed Markets Europe, Canada, and United States are modeled as allowed GBS universe classifications.
- ADVT threshold is represented as a `MonetaryAmount` with value `5`, currency `USD`, and scale `Million`.
- One- and six-month lookback windows are represented as functions anchored on `SelectionDay` and including the anchor day.
- The minimum ADVT over 1 and 6 months is represented as the min-like value constrained against both windows.
- Buffer rules are represented as first-class rule objects `CurrentCompanyBufferRule` and `NotCurrentCompanyBufferRule`, linked to formula-bearing constraints with `[realizes: ...]`.
- `AvoidFrequentChangesBetweenTwoShareClasses` is kept as a `VagueTerm`, because the source explains motivation but does not define a separate computable rule beyond the buffers.
- `eligible_for_index_universe_requirements` is the main biconditional: eligibility iff all listed requirements hold.
- `only_one_share_class_of_each_company` is explicit as a count constraint.
- No-discretion governance is represented as a `prohibition`, not just as a descriptive predicate.

Rejected / alternatives:

- Do not use `RuleRationale`; it was rejected because it is not a stable legal/A4V3 term in this local ontology.
- Do not add ad hoc `rel/fact` bridges only to connect rule entities unless formula linkage is needed; `[realizes: ...]` is the chosen explicit link.
- Do not leave rule entities dangling when their purpose is to name a first-class rule object.
- Do not model `comprised`, `fulfill`, `below`, or `following` as standalone domain relations; they are document/requirement framing words.

Rationale: section 2.1 contains several heterogeneous requirements. The chosen IR keeps the main membership rule readable while extracting reusable concepts for GBS source universe, market classification, ADVT threshold/windows, buffer rules, RBICS appendix membership, and no-discretion governance.

Waiver rationale:

- `comprised`, `fulfill`, `below`, `inclusion`, `applies`, and `following` are absorbed by the eligibility biconditional and explicit buffer constraints.
- `under` is absorbed by GBS framework provenance and classification functions.
- `will` is absorbed by deterministic eligibility in the current-company buffer rule.
- `see` is absorbed by the Appendix/RBICS cross-reference structure.

Validation:

- clean gate: accepted
- phrase coverage: 25/25
- token accounted coverage: 90/90
- exact URLs: 1/1
- waivers: 9/9
