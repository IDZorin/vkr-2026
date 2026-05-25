# Corpus-Aware Multi Judge: section_4_7

- generated_at: `2026-05-11T13:18:26+02:00`
- skipped: `False`
- local_source_alignment_mode: `corresponds`
- corpus_alignment_mode: `corresponds`
- corpus_alignment_agreement: `0.8`
- needs_context_count: `1`
- mean_confidence: `0.946`

## Included Context

```json
{
  "entry": "section_4_7",
  "entry_dir": "D:\\OneDrive\\Documents\\Study\\MIPT\\VKR\\research_experiments\\2026-02_pipeline\\case_studies\\financial_methodology\\sections\\section_4_7",
  "global_bridge": true,
  "related_sections": [],
  "artifacts": {
    "source.md": true,
    "normalized.md": true,
    "main_ir.a4v3": true,
    "repair.a4v3": false,
    "provenance.yaml": true,
    "translator_notes.md": true,
    "waivers.yaml": false,
    "waivers_v1.yaml": false
  }
}
```

## Judges

### gpt-5.4-mini

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `provenance, translator_notes, bridge`
- confidence: `0.97`

Reason:

The IR captures all three source claims: market stress triggers predefined/exhaustive arrangements described in the Disruption Policy available on the Solactive website; market stress can arise for a variety of reasons and generally leads to inaccurate or delayed prices for one or more Index Components; and the Index may be limited or impaired during illiquid/fragmented markets and market stress. The corpus context confirms the intended local scope and the directed incorporation relation, but no repair is needed to make the translation fit the source.

Semantic differences:

- none

Context-resolved issues:

- The singular phrase "the Index" is treated as a local Solactive index scope carrier, consistent with provenance.
- "Incorporated by reference" is modeled as a directed relation into ThisGuideline, matching the documented translation decision.

Stylistic notes:

- Several source phrases are represented by vague-term carriers rather than literal wording, which is acceptable here.
- The IR uses explicit carriers for modality and cardinality-like phrases such as "generally" and "one or more Index Components".

### gpt-5.4

- local_source_alignment: `partially_corresponds`
- corpus_alignment: `corresponds`
- relation_type: `same_meaning_poor_wording`
- needs_context: `True`
- context_used: `provenance, translator_notes`
- confidence: `0.93`

Reason:

The IR captures all substantive source claims: calculation during market stress follows predefined/exhaustive arrangements described in the disruption policy; the policy is incorporated by reference and available on the Solactive website; market stress can arise for various reasons and generally yields inaccurate or delayed prices for one or more index components; and index determination may be limited or impaired during illiquid, fragmented, or stressed markets. Source-only, the main concern is the locally introduced scope link between singular "the Index" and plural "its indices," plus some carrier-style wording that can look over-engineered. Provenance and notes explicitly document these as translation choices rather than semantic additions, resolving the concern.

Semantic differences:

- none

Context-resolved issues:

- The fact index_of(TheIndex, Solactive) is not stated verbatim in the source, but provenance explicitly records it as a local scope bridge connecting source phrases "its indices" and "the Index" for this section's internal coherence.
- The use of possibility and vague-term carriers (e.g., DeterminationConditionPossibility, Generally, VarietyOfReasons, OneOrMoreIndexComponents) may look indirect source-only, but translator notes and provenance show they are deliberate devices to preserve modality and hedging rather than strengthen the claims.
- The directed incorporation relation into ThisGuideline is confirmed by provenance and translator notes as the intended reading of "incorporated by reference."

Stylistic notes:

- The IR uses named carrier entities such as SolactiveDisruptionArrangements and SolactiveDisruptionPolicy instead of repeating noun phrases inline.
- "AtTimesOfMarketDisruption" is a somewhat loose label because the source separately mentions illiquid markets, fragmented markets, and market stress; however this is used only as a qualifier tag, not as an added substantive condition.
- The relation name price_outcome_inaccurate_or_delayed bundles two alternatives in one predicate name, but the enum values keep the disjunction explicit.

### claude-haiku-4-5

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `provenance, translator_notes`
- confidence: `0.98`

Reason:

The main_ir.a4v3 faithfully translates all explicit claims in the source text. Every source sentence maps to at least one IR declaration (fact or constraint), with proper use of VagueTerm carriers for hedges and modality markers. The provenance ledger and translator notes document all major design decisions (e.g., possibility carriers for 'may be', enum carriers for disjunctions, vague-term carriers for 'generally' and 'variety of reasons'). No contradiction exists between source and IR; the IR is conservative and source-grounded throughout.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR uses formal relation names (e.g., `calculates_index_following_arrangement`, `incorporated_by_reference_into`) that are more explicit than the source's natural language, but this is standard A4V3 practice and does not constitute semantic drift.
- VagueTerm carriers (`Generally`, `VarietyOfReasons`, `OneOrMoreIndexComponents`, `MayBeLimitedOrImpaired`, `AtTimesOfMarketDisruption`) preserve source hedges and modality without reducing them to numeric or boolean claims, which is appropriate for a methodology document.
- The use of `DeterminationConditionPossibility` instead of direct `limited`/`impaired` facts correctly captures the source's modal 'may be' rather than asserting actual limitation or impairment.

### deepseek-v4-pro

- local_source_alignment: `partially_corresponds`
- corpus_alignment: `partially_corresponds`
- relation_type: `partial_overlap`
- needs_context: `False`
- context_used: `provenance, translator_notes`
- confidence: `0.9`

Reason:

The IR formalizes most source claims faithfully, but two constraints overstate the source's modal strength: 'can arise' is interpreted as a universal implication, and 'generally results' is also universally quantified despite a 'Generally' qualifier. The provenance and notes acknowledge the hedge carriers but do not alter the logical force.

Semantic differences:

- Constraint 'market_stress_can_arise_due_to_variety_of_reasons' asserts that every market stress in a market-stress period arises due to a variety of reasons, while the source only claims it can arise (possibility, not universality).
- Constraint 'market_stress_generally_results_in_price_conditions' asserts that every market-stress period has a price outcome with a 'Generally' qualifier, but the source's 'generally results' indicates a typical but not universal relationship, and the universal quantification removes the intended hedge.

Context-resolved issues:

- none

Stylistic notes:

- The IR uses explicit VagueTerm carriers for hedges like 'variety of reasons', 'generally', 'one or more', and 'may be', which is a stylistic choice consistent with the translator notes.
- The introduction of a MarketDisruption hierarchy (MarketStress, IlliquidMarket, FragmentedMarket) is a reasonable extrapolation from source phrases.

### qwen/qwen3.6-plus

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `provenance, translator_notes`
- confidence: `0.95`

Reason:

The IR faithfully captures all three source sentences using explicit A4V3 carriers for modality, vague terms, and disjunctive conditions. Constraints correctly scope calculations to Solactive indices during market stress periods, and the possibility carrier accurately models the epistemic 'may be limited or impaired' without asserting actual impairment. Provenance and translator notes confirm these design choices are intentional and align with the source semantics.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR uses explicit VagueTerm and Possibility carriers for hedges and modals ('generally', 'variety of reasons', 'may be'), which is a deliberate A4V3 convention to preserve epistemic nuance without over-committing to factual assertions.
- The disjunction in 'illiquid or fragmented markets and market stress' is correctly formalized as a disjunctive antecedent in the determination constraint.
