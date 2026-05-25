# Corpus-Aware Multi Judge: section_4_4

- generated_at: `2026-05-11T17:19:00+02:00`
- skipped: `False`
- local_source_alignment_mode: `corresponds`
- corpus_alignment_mode: `corresponds`
- corpus_alignment_agreement: `0.8`
- needs_context_count: `0`
- mean_confidence: `0.956`

## Included Context

```json
{
  "entry": "section_4_4",
  "entry_dir": "D:\\OneDrive\\Documents\\Study\\MIPT\\VKR\\research_experiments\\2026-02_pipeline\\case_studies\\financial_methodology\\sections\\section_4_4",
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
- context_used: `none`
- confidence: `0.96`

Reason:

The IR captures the source’s two claims: an index adjustment may be necessary between regular rebalance days under certain circumstances, and if a corporate action in relation to an index component occurs, Solactive announces the adjustment with at least two trading days’ notice and implements it on the notice’s effective day. The local vocabulary and scoped obligations match the source without needing bridge context.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR uses carrier sorts and deontic obligations to model modal wording, which is a translation style choice rather than a semantic difference.
- "Announcements" is modeled as a document part, matching the source’s section reference in a structural way.

### gpt-5.4

- local_source_alignment: `partially_corresponds`
- corpus_alignment: `partially_corresponds`
- relation_type: `partial_overlap`
- needs_context: `False`
- context_used: `provenance, translator_notes`
- confidence: `0.89`

Reason:

The IR captures most of the section faithfully: possible necessity of an index adjustment between regular rebalance days, the corporate-action trigger, compliance with the Solactive Equity Index Methodology, announcement on the Solactive website under Announcements, at least two Trading Days' notice, and implementation on the notice's effective day. However, one local formula overstates the source by asserting that every required adjustment has at least one of the listed effect types, whereas the source says such adjustment may have to be done in relation to a component and/or may also affect number and/or weighting, which is permissive rather than universally mandatory.

Semantic differences:

- The constraint `required_adjustment_effect_scope` makes every `RequiredIndexAdjustment` satisfy at least one listed effect relation. The source presents these as possible ways an adjustment may have to be done or may also affect components/number/weighting, not as a universal requirement that each required adjustment instantiate one of those modeled effects.

Context-resolved issues:

- The use of an `IndexAdjustmentPossibility` carrier for 'may be necessary' correctly preserves possibility rather than asserting an actual adjustment.
- Splitting 'has to be made' into a trigger constraint plus a deontic obligation is an explicit documented translation choice and avoids collapsing normativity into factual existence alone.
- Scoping announcement, notice-period, and implementation rules to `RequiredIndexAdjustment` is explained by the anaphoric reading of 'the Index adjustment' and is consistent with the source.
- The interval-order constraint for 'between two regular Rebalance Days' is documented as a bridge-style structural unpacking of 'between', not an added business rule.
- Modeling the Announcements location as a `DocumentPart` of the Solactive website, without inventing a URL, matches the source wording.

Stylistic notes:

- The source says 'giving a notice period of at least two Trading Days'; the IR realizes this through a `Notice` plus `NoticePeriod` structure, which is more formal but not inherently drift.
- Using `ThisGuideline` as the target of incorporation is a naming choice inferred from the local document context.
- The effect labels `ComponentRelationEffect`, `ComponentNumberEffect`, and `ComponentWeightingEffect` are reasonable ontology names rather than source phrases.

### claude-haiku-4-5

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `provenance, translator_notes`
- confidence: `0.98`

Reason:

The main_ir.a4v3 faithfully translates the source text of Section 4.4. Every source claim is covered by at least one IR element (fact, constraint, obligation, or relation), and every IR element traces back to explicit source phrases documented in the provenance ledger. The translator notes explain key design decisions (e.g., possibility carriers, required-adjustment subtypes, section-reference antecedents) that are consistent with the source wording and the a4v3 specification. No semantic drift is detected between source and IR, and no cross-section reasoning is required to validate the local translation.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR uses formal carrier sorts (IndexAdjustmentPossibility, RequiredIndexAdjustment, NoticePeriod, EffectiveDay) to represent source concepts that are expressed informally or modally in the source text. This is consistent with a4v3 methodology and does not constitute semantic drift.
- The IR introduces VagueTerm entities (CertainCircumstances, MayBeNecessary, MayHaveToBeDone, CertainIndexComponents) to preserve source qualifiers and modal language without making closed-world assumptions. This is a deliberate design choice documented in translator notes and provenance.
- The IR uses directed relations (e.g., incorporated_by_reference_into, announced_by, announced_on) to make implicit source structure explicit. All relation directions are justified by source phrasing and documented in provenance.
- The constraint rebalance_interval_order makes the word 'between' in 'between two regular Rebalance Days' explicit as a temporal ordering. This is a bridge constraint documented in provenance as a vocabulary clarification, not a new business rule.

### deepseek-v4-pro

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `provenance, translator_notes`
- confidence: `0.95`

Reason:

The IR faithfully captures all propositions in the source text: the possibility of an index adjustment between regular rebalance days, the required adjustment triggered by a corporate action, compliance with the Solactive Equity Index Methodology, announcement with at least two trading days' notice, and implementation on the notice's effective day. Vague phrasing ('certain circumstances', 'may be necessary') is represented with explicit possibility carriers and vague term entities without adding unjustified content. Corpus context only reinforces that every IR element is a deliberate translation of a source phrase.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR structures the source's vague and modal language using explicit encoding patterns such as IndexAdjustmentPossibility, VagueTerm entities, and an interval constraint for 'between'. These choices add precision without altering meaning.
- The division of 'has to be made' into a trigger constraint and an obligation is a deliberate scoping technique documented in translator notes.

### qwen/qwen3.6-plus

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `provenance, translator_notes`
- confidence: `1.0`

Reason:

The IR faithfully captures all source claims, accurately modeling modalities ('may be necessary' as a possibility carrier, 'has to be made' as an obligation scoped to a triggered required adjustment), temporal constraints (notice period of at least two trading days, implementation on the effective day), and document references (methodology incorporation, announcement section). Provenance and translator notes explicitly justify the structural choices, confirming exact alignment without semantic drift.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The separation of the corporate-action trigger into a constraint creating a RequiredIndexAdjustment and a separate obligation to make it is a deliberate deontic modeling choice that preserves the source's conditional necessity without over-constraining the logic.
