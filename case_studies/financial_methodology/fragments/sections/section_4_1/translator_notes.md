# Section 4.1 Translator Notes

## 2026-05-09T20:10:00+02:00 — Scope of the displayed adjusted-return formula

Decision: the displayed formula in section 4.1 is modeled as the `SOLTCA50` / 50 AR formula, not as a generic formula for every adjusted-return index.

Accepted:

- `AdjustedReturnVersion` is the source-local name for the 5% per annum adjusted-return construction from the NTR Index version.
- `SOLTCA50` is the source-local name for the 50 index points per annum adjusted-return construction from the GTR Index version.
- The explicit displayed formula is attached to `SOLTCA50` in `soltca50_adjusted_return_index_formula`.
- The global bridge layer aligns `SOLTCA50` with the canonical section 1.2 entity `SolactiveTransatlanticCleanEnergyEURIndex50AR`.

Rejected:

- Do not attach the displayed formula to `AdjustedReturnVersion` merely because section 4.1 says "The adjusted return Index is calculated according to the following formula".
- Do not model the displayed formula as applying to all adjusted-return indices.

Rationale:

Read in isolation, the sentence "The adjusted return Index is calculated according to the following formula" could look generic. Read together with section 1.2, the scope is more specific. Section 1.2 lists two adjusted-return entries:

- `Solactive Transatlantic Clean Energy EUR Index 50 AR`, ticker `SOLTCA50`, type `AR**`;
- `Solactive Transatlantic Clean Energy EUR Index 5% AR`, ticker `SOLTCEA5`, type `AR*`.

The section 1.2 footnotes distinguish them:

- `AR*` means adjusted return as described in the Equity Index Methodology.
- `AR**` means adjusted return following the formula specified in Section 4.

Section 4.1 then states that `SOLTCA50` has a 50 index points per annum decrement from the GTR Index version, and the displayed formula defines `SD` as the Synthetic Dividend of 50 index points per annum. Therefore the displayed formula is the `SOLTCA50` / 50 AR formula. The 5% adjusted-return construction remains represented by `AdjustedReturnVersion` and its 5% decrement from the NTR Index version.

Validation:

- Parser strict and semantic lint pass for `section_4_1/main_ir.a4v3`.
- Multi-judge source-only review may still report this as partial because it does not read section 1.2 context by default. This note records that the decision is based on whole-methodology context, not only isolated section 4.1 wording.

## 2026-05-09T20:10:00+02:00 — Effective date and ex-date equivalence

Decision: keep `ex_date(p) = effective_date(p)` in the dividend/distribution reinvestment rule.

Accepted:

- The parenthetical source phrase "the effective date (the so called ex-date)" is treated as an appositive equivalence for this context.
- The IR keeps the equality instead of weakening it to an unrelated naming relation.

Rejected:

- Do not remove the equality merely because a source-only judge calls it "stronger"; the source explicitly presents the two labels as interchangeable in this clause.

Rationale:

The phrase does not say that ex-date is merely related to effective date; it says the effective date is the so-called ex-date. Therefore equality is an appropriate formalization in this local payment-date context.

## 2026-05-11T13:55:00+02:00 -- Arity-5 formula-factor relations

Decision: keep the current arity-5 formula-factor relations as an accepted
local compact encoding, but mark them as future carrier-reification candidates.

Affected relations:

- `formula_level_change_based_on_price_change`
- `formula_level_change_takes_weight`
- `formula_level_change_takes_currency_conversion`

Accepted:

- These relations are source-local formula-factor links for section 4.1.
- The five roles are formula, index, calculation day, index component, and the
  factor value used by the formula.
- The current encoding is readable enough for the local hand-authored IR and
  is already accepted by the deterministic and LLM checks.

Future improvement:

- Arity 5 is not ideal for merge, ontology construction, or contradiction
  detection because the roles are positional rather than explicit role edges.
- A future graph-normalized version should introduce a carrier such as
  `FormulaApplication` or `LevelChangeTerm` and split the roles into binary
  relations, for example formula/application, index, day, component, weight,
  price change, and currency conversion.

Rejected for now:

- Do not rewrite the accepted section immediately only to satisfy the new
  soft arity lint. The current relation arity is documented as a conscious
  local compactness tradeoff, not a semantic error.
