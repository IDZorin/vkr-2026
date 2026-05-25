# Section 4.7 Translator Notes

This file records translator decisions for the current `main_ir.a4v3`.
It is review memory, not an additional source of methodology claims.

## Changelog

### 2026-05-11T13:20:00+02:00

Decision: synthesize the final IR from the three drafts instead of accepting
one draft as-is.

Accepted:

- Use the `MarketDisruption` hierarchy from Copy 3: `MarketStress`,
  `IlliquidMarket`, and `FragmentedMarket`.
- Use `SolactiveDisruptionArrangements` as a named arrangement carrier, with
  explicit `predefined`, `exhaustive`, and `described_in` facts.
- Use enums for disjunctive states: `PriceCondition = Inaccurate | Delayed`
  and `DeterminationCondition = Limited | Impaired`.
- Represent `generally` and `variety of reasons` as `VagueTerm` carriers,
  not as hidden wording in relation names or as a numeric multiplicity claim.
- Represent `one or more Index Components` explicitly via
  `OneOrMoreIndexComponents`, while the formula body still contains an
  existential component witness.
- Represent `may be limited or impaired` with a
  `DeterminationConditionPossibility` carrier. This keeps modality visible and
  avoids asserting that the Index determination is actually limited or
  impaired.
- Use directed incorporation:
  `incorporated_by_reference_into(SolactiveDisruptionPolicy, ThisGuideline)`.

Rejected / alternatives:

- Do not include a concrete disruption-policy URL in `main_ir.a4v3`; the
  section source only says the policy is available on the Solactive website.
- Do not use Copy 2's `=== FINAL_IR ===` header; it is not valid A4V3.
- Do not model `variety of reasons` as `exists r1, r2, r1 != r2`; the source
  phrase is a qualitative hedge, not a numeric lower bound.
- Do not model `may be limited or impaired` as actual `limited`/`impaired`
  relations over every market disruption.

Validation notes:

- `may be limited or impaired` is epistemic possibility, not deontic
  permission. The family coverage checker was updated so this phrase does not
  require a `permission` declaration.

### 2026-05-11T13:35:00+02:00

Decision: keep the accepted carrier-heavy encoding, and document why the
extra layers are intentional rather than accidental duplication.

Accepted:

- The phrase `may be limited or impaired` has three layers:
  `MayBeLimitedOrImpaired` keeps the surface modal phrase visible,
  `DeterminationConditionPossibility` carries the epistemic possibility
  semantics, and `DeterminationCondition = Limited | Impaired` keeps the two
  alternative states queryable. This is intentionally similar to the 4.6
  `ErrorPossibility` / description-carrier pattern.
- `one or more Index Components` is represented both by
  `OneOrMoreIndexComponents` and by an existential component witness. The
  existential gives the formal at-least-one semantics; the carrier preserves
  the source phrase for provenance and token-level auditability.
- The current period relations are asymmetric by design:
  `period_of_market_stress` is used for the source phrase "periods of market
  stress", while `period_of_market_disruption` handles the broader
  `MarketDisruption` subtypes for illiquid and fragmented market contexts.
  This may later be normalized in a merge/bridge layer, but it is not a local
  section error.
- `predefined` and `exhaustive` are kept as unary flags on the arrangement
  carrier. They are qualitative descriptions, but not vague hedges in the same
  sense as `generally` or `variety of reasons`; no `VagueTerm` carrier is
  needed for them.

Rejected / alternatives:

- Do not collapse the `may be limited or impaired` layers into only a relation
  name, because that would hide modality and make contradiction checks weaker.
- Do not remove the existential component witness for `one or more`; otherwise
  the source cardinality would survive only as a token carrier.
