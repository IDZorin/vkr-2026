# Corpus-Aware Multi Judge: section_3_1

- generated_at: `2026-05-12T10:48:27+02:00`
- skipped: `False`
- local_source_alignment_mode: `corresponds`
- corpus_alignment_mode: `corresponds`
- corpus_alignment_agreement: `0.8`
- needs_context_count: `3`
- mean_confidence: `0.924`

## Included Context

```json
{
  "entry": "section_3_1",
  "entry_dir": "<PRIVATE_WORKSPACE>\\case_studies\\financial_methodology\\sections\\section_3_1",
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

- local_source_alignment: `partially_corresponds`
- corpus_alignment: `partially_corresponds`
- relation_type: `partial_overlap`
- needs_context: `True`
- context_used: `bridge, provenance, translator_notes`
- confidence: `0.86`

Reason:

The IR captures the main rebalance claims: adjustment on the Rebalance Day after Close of Business, implementation via shares determined on the Fixing Day based on Selection Day weights, and publication of changes with sufficient notice under Announcement. However, it also adds structural details not stated in the section, especially the explicit incorporation-by-reference target `ThisGuideline` and the obligation wrapper for publication, so the match is not exact. Corpus context explains some over-specific naming and the split between structural notice facts and the deontic publication obligation, but it does not eliminate the extra local claims.

Semantic differences:

- `incorporated_by_reference_into(SolactiveEquityIndexMethodology, ThisGuideline)` is not explicitly stated in the source; the target document is inferred from context rather than named in the section.
- `publish_index_component_change` turns 'Solactive will publish' into an obligation; this is a translation choice, not a direct source statement.
- The IR introduces `ordinary_rebalance_day` as a scoped unary predicate; this is a modeling device not present in the source text, though it is consistent with the section.
- `notice_for_rebalance_day` and `notice_described_by(SufficientNoticeBeforeRebalanceDay)` are structural encodings of the timing phrase rather than literal source wording.

Context-resolved issues:

- The use of `SufficientNoticeBeforeRebalanceDay : VagueTerm` is explicitly supported by translator notes as the intended treatment of 'sufficient notice before the Rebalance Day'.
- The split between a structural notice constraint and a separate publication obligation is explicitly documented in translator notes and provenance.
- The local naming of `SolactiveEquityIndexMethodology`, `OrdinaryRebalanceProcedure`, and `AnnouncementSection` is supported by provenance as source-phrase carriers.

Stylistic notes:

- `ThisGuideline` is a context-inferred document target rather than a source-named entity.
- `OrdinaryRebalanceProcedure` and `AnnouncementSection` are reasonable carrier names but slightly more formal than the source phrasing.
- `weight_on_selection_day` / `shares_on_fixing_day` are clear functional encodings of the prose.
- The IR is somewhat verbose but structurally faithful in its core event-day relations.

### gpt-5.4

- local_source_alignment: `partially_corresponds`
- corpus_alignment: `corresponds`
- relation_type: `same_meaning_poor_wording`
- needs_context: `True`
- context_used: `provenance, translator_notes`
- confidence: `0.88`

Reason:

The local IR covers the section's main content well: adjustment of the Index on Rebalance Day after Close of Business, implementation of shares determined on the Fixing Day based on weights calculated on the Selection Day, reference to the Equity Index Methodology, and publication of Index Component changes on the Announcement section of the Solactive website. Source-only, two items look overcommitted or awkwardly rendered: the methodology being incorporated by reference specifically into `ThisGuideline`, and the notice timing being represented via `notice_for_rebalance_day` plus a vague-term label rather than an explicit before-rebalance temporal relation. The provenance and translator notes explicitly document both as intentional translation choices preserving source meaning without adding a concrete timing threshold, so with corpus context the translation corresponds overall.

Semantic differences:

- none

Context-resolved issues:

- `incorporated_by_reference_into(SolactiveEquityIndexMethodology, ThisGuideline)` is not explicit in the sentence itself, but provenance documents this as the intended target-document inference pattern rather than a contradictory claim.
- The source phrase "with sufficient notice before the Rebalance Day" is not encoded as a strict temporal relation; translator notes and provenance explain that the timing is intentionally preserved as the vague term `SufficientNoticeBeforeRebalanceDay` plus linkage to the relevant Rebalance Day, avoiding an over-specific reading.
- The split of "Solactive will publish" into both an obligation and a structural notice constraint could look duplicative source-only, but provenance explicitly explains this as deontic-plus-structure decomposition rather than semantic drift.

Stylistic notes:

- `Weight extends Percent` relies on a sort not listed in the provided prelude inventory; this is a schema/plumbing issue rather than a source-semantic mismatch.
- Translator notes mention `notice_before_rebalance_day(n, rd)`, but the actual IR uses `notice_for_rebalance_day`; this is a wording/inventory inconsistency in notes, not a demonstrated contradiction in the IR.
- `ordinary_rebalance_day` as a unary flag and `Section3_1IndexComponentChange` as a scoped subtype are modeling devices for section scoping, not extra substantive claims from the prose.

### claude-haiku-4-5

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `provenance, translator_notes`
- confidence: `0.98`

Reason:

The main_ir.a4v3 file faithfully translates all claims in the source text. The provenance ledger and translator notes document every IR decision with explicit source quotes and back-translations. The IR correctly splits the publication modal into a deontic obligation and structural constraint, preserves the vague timing phrase as a VagueTerm rather than over-specifying it, and uses local entities (TheIndex, Solactive, etc.) without importing cross-section identities. All seven IR claims (five constraints, two facts, one obligation) trace directly to source phrases with no contradictions or unwarranted additions.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR uses camelCase for relation names (e.g., ordinary_rebalance_day, selection_day_of_rebalance) while the source uses natural English phrases; this is a4v3 naming convention, not semantic drift.
- The IR introduces subtypes (SelectionDay, FixingDay, RebalanceDay as Day subtypes; OrdinaryRebalance, CloseOfBusiness as Event subtypes) to structure the domain; these are justified by the source's repeated use of these named temporal/event concepts.
- The IR uses function notation (new_selection_for_rebalance(rd), shares_on_fixing_day(fd, c), weight_on_selection_day(sd, c)) to map days and components to their derived values; the source describes these as determinations and calculations, which the IR captures structurally.
- The IR introduces Section3_1IndexComponentChange as a subtype of IndexComponentChange to scope the publication obligation to this section's procedure; the provenance notes this is a plumbing decision parallel to section 4.4's RequiredIndexAdjustment pattern, justified by the source phrase 'any changes made to the Index Components' in the context of this section's rebalance procedure.

### deepseek-v4-pro

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `provenance, translator_notes`
- confidence: `0.95`

Reason:

The IR captures every substantive claim of the source text, including the rebalance adjustment, share implementation, cross-references to sections 2.1/2.2, the incorporation-by-reference of the Equity Index Methodology, the publication obligation with sufficient notice, and the announcement section URL. All structural and deontic elements are faithfully encoded.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The source phrase 'sufficient notice before the Rebalance Day' is encoded as the VagueTerm SufficientNoticeBeforeRebalanceDay, preserving the qualitative hedge.
- The publication sentence is split into a structural constraint and a separate deontic obligation, a documented translation choice.
- The target of 'incorporated by reference' is inferred as ThisGuideline, a reasonable contextual reading confirmed by provenance notes.

### qwen/qwen3.6-plus

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `True`
- context_used: `provenance, translator_notes`
- confidence: `0.95`

Reason:

The IR faithfully captures all four source claims: the index adjustment timing and purpose, the share implementation mechanics, the methodology reference, and the publication obligation. Corpus context explicitly documents intentional modeling choices such as splitting the publication sentence into a deontic obligation and structural constraint, using a VagueTerm for the notice threshold, and inferring the target document for incorporation by reference.

Semantic differences:

- none

Context-resolved issues:

- The split of 'will publish' into a deontic obligation and a structural constraint is clarified by translator notes.
- The inference of 'ThisGuideline' as the target of 'incorporated by reference' is justified in provenance.
- The use of a VagueTerm for 'sufficient notice before the Rebalance Day' instead of a concrete temporal relation is explained in translator notes.

Stylistic notes:

- The subtype Section3_1IndexComponentChange is introduced to scope the publication obligation specifically to this section's procedure.
- The purpose clause 'in order to reflect' is modeled as a structural relation reflects_new_selection rather than a modal operator.
