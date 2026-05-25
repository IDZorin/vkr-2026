# Corpus-Aware Multi Judge: section_4_5

- generated_at: `2026-05-10T18:49:35+02:00`
- skipped: `False`
- local_source_alignment_mode: `corresponds`
- corpus_alignment_mode: `corresponds`
- corpus_alignment_agreement: `0.8`
- needs_context_count: `0`
- mean_confidence: `0.948`

## Included Context

```json
{
  "entry": "section_4_5",
  "entry_dir": "D:\\OneDrive\\Documents\\Study\\MIPT\\VKR\\research_experiments\\2026-02_pipeline\\case_studies\\financial_methodology\\sections\\section_4_5",
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
- confidence: `0.97`

Reason:

The IR captures the source’s claims about corporate actions, their impact on the index, implementation window, compliance with the Equity Index Methodology, the non-conclusive list of examples, and Solactive’s limited deviation right. The corpus context mainly confirms intended readings and local naming choices, but no contradiction or unresolved omission remains in the main IR.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- Some source phrases are normalized into ontology-friendly names, e.g. 'Mergers & Acquisitions' and 'as possible'.
- The passive source clauses are represented as obligations without explicit agents, which matches the translator notes.

### gpt-5.4

- local_source_alignment: `partially_corresponds`
- corpus_alignment: `partially_corresponds`
- relation_type: `partial_overlap`
- needs_context: `False`
- context_used: `provenance, translator_notes`
- confidence: `0.84`

Reason:

The IR captures most of the section’s core content: considered corporate actions, their material impact, implementation from cum-day to ex-day, compliance with the Equity Index Methodology, Solactive’s deviation right, and the non-conclusive list of relevant corporate-action kinds. However, several formulas overstate or shift the source meaning: the methodology is asserted to cover each listed corporate-action kind, the document-level statement about definitions/adjustments is scoped only to covered kinds rather than plainly to each corporate action, and the deviation-condition constraint is written as a universal over permitted deviations rather than directly limiting the permission itself. Corpus notes explain some modeling choices, but they do not eliminate these semantic mismatches.

Semantic differences:

- The fact `relevant_corporate_action_list` adds that the Equity Index Methodology covers each of the 12 listed corporate-action kinds (`methodology_covers_corporate_action_kind`), which is stronger than the source text. The source says the methodology contains for each corporate action a brief definition and relevant adjustment information, but does not explicitly state coverage only or specifically for the listed set.
- The constraint `equity_index_methodology_material_for_covered_corporate_actions` is conditioned on `methodology_covers_corporate_action_kind`, so the source claim about 'for each corporate action' is represented only indirectly and only for kinds marked as covered in the IR. This changes the source’s direct scope structure.
- The permission `deviate_from_standard_procedures` is unconditional at declaration level, while the unusual/complex/preserve-comparability-and-representativeness conditions appear only in a separate universal over `PermittedCorporateActionDeviation`. This does not fully encode that the retained right is specifically for deviations in those cases.

Context-resolved issues:

- The use of `non_conclusive(RelevantCorporateActionList)` plus `non_conclusive_means_not_conclusive` is an acceptable explicit rendering of 'but not conclusive' rather than a semantic drift.
- Representing passive source clauses as agentless obligations is justified by the translator notes and does not itself contradict the source.
- Using a coincidence relation between the adjustment and the occurrence of the price effect, rather than stronger temporal equality, is a faithful conservative modeling choice.
- Keeping the corporate-action list open via `CorporateActionKind` and `ListedCorporateActionKind` matches the source’s non-exhaustive wording.

Stylistic notes:

- `IndexMaintenanceCorporateAction` is a modeling subtype used to scope universals; this is structural wording rather than semantic drift.
- `AsPossible` as a `VagueTerm` for 'as generic and transparent as possible' is a reasonable hedge-preserving device.
- `index_maintenance_scope` is plumbing/entity-binding rather than substantive added content.

### claude-haiku-4-5

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `provenance, translator_notes`
- confidence: `0.98`

Reason:

The main_ir.a4v3 faithfully translates all substantive claims in the source text. The IR ontology (sorts, entities, relations, constraints, obligations, permissions) traces directly to source noun-phrases and explicit statements. The provenance ledger and translator notes document all significant translation decisions (e.g., passive obligations without agent, non-conclusive list representation, deviation permission scope) and justify them by reference to source phrasing. No semantic divergence exists between source and IR; stylistic differences (e.g., 'will consider' → relation vs. obligation) are documented and justified.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- Source passive voice 'need to be accounted for' and 'will be made in compliance' are represented as obligations without explicit agent; translator notes justify this as preserving the source's passive form rather than inventing an agent.
- Source phrase 'will consider various events' is represented as a relation considers_for_index_maintenance rather than a standalone obligation; translator notes explain this reflects the source's process-scoping intent rather than a deontic claim.
- Source phrase 'as generic and transparent as possible' is encoded via methodology_quality paired with VagueTerm AsPossible rather than a bare boolean flag; this preserves the source's hedge without over-committing to an operational threshold.
- Source phrase 'coincides with the occurrence of the price effect' is represented as a direct relation adjustment_coincides_with_price_effect_occurrence rather than equality of day-valued functions; translator notes justify this as avoiding over-specification.
- Source list 'following, but not conclusive, list' is represented by non_conclusive(RelevantCorporateActionList) with an explicit constraint non_conclusive_means_not_conclusive; this preserves the source negation and keeps the parent sort CorporateActionKind open.

### deepseek-v4-pro

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `provenance, translator_notes`
- confidence: `1.0`

Reason:

The IR faithfully captures all source claims. Every source sentence maps to explicit facts, constraints, obligations, or permissions, with no missing or added content. Translation decisions (e.g., encoding 'will consider' as a relation, treating 'as possible' as a VagueTerm, separating deviation conditions) are well-motivated and do not distort meaning.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR uses detailed sort hierarchies and formal entity names, which is expected for a formal language.
- The 'non_conclusive_means_not_conclusive' constraint adds no new content; it serves as a logical bridge for contradiction detection.

### qwen/qwen3.6-plus

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `provenance, translator_notes`
- confidence: `0.95`

Reason:

The IR faithfully formalizes every descriptive, normative, and enumerative claim in the source text. Constraints capture the temporal and material impact conditions, obligations/permissions map directly to the source's passive modals and retained rights, and the corporate action list is preserved as open with an explicit non-conclusive marker. Provenance and translator notes confirm that structural choices (e.g., agent-less obligations, VagueTerm for hedges, defining-universal for deviation conditions) are intentional and do not introduce semantic drift.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- Passive normative claims are formalized as agent-less obligations, preserving the source's deliberate omission of a responsible agent.
- The hedge 'as possible' is encoded via a VagueTerm entity rather than committing to a hard operational threshold.
- The non-conclusive list is structurally preserved using an explicit non_conclusive flag and an open parent sort CorporateActionKind, preventing unintended closure of the universe of corporate actions.
