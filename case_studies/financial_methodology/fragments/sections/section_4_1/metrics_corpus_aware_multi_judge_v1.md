# Corpus-Aware Multi Judge: section_4_1

- generated_at: `2026-05-09T21:33:19+02:00`
- skipped: `False`
- local_source_alignment_mode: `partially_corresponds`
- corpus_alignment_mode: `corresponds`
- corpus_alignment_agreement: `1.0`
- needs_context_count: `2`
- mean_confidence: `0.945`

## Included Context

```json
{
  "entry": "section_4_1",
  "entry_dir": "<PRIVATE_WORKSPACE>\\case_studies\\financial_methodology\\sections\\section_4_1",
  "global_bridge": true,
  "related_sections": [
    "section_1_2"
  ],
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
- corpus_alignment: `corresponds`
- relation_type: `same_meaning_poor_wording`
- needs_context: `True`
- context_used: `bridge, translator_notes, provenance, related_sections`
- confidence: `0.96`

Reason:

Locally, the IR captures the section’s main claims but over-scopes the displayed adjusted-return formula and uses source-local names that look incomplete in isolation. The documented corpus context explicitly says the displayed formula is intended for SOLTCA50, keeps the 5% AR construction separate, and places cross-section identity links in the bridge layer, which resolves the apparent mismatch. No actual contradiction remains after that context is applied.

Semantic differences:

- none

Context-resolved issues:

- The displayed adjusted-return formula is attached to SOLTCA50 rather than to every adjusted-return index.
- Source-local names such as AdjustedReturnVersion, NTRIndexVersion, and GTRIndexVersion are intentionally kept in the local section and aligned to canonical section 1.2 entities in the bridge layer.
- The 5% adjusted-return construction is represented separately from the SOLTCA50 / 50 AR formula.

Stylistic notes:

- Some entity names are source-local placeholders rather than canonical published names.
- The formula and index naming are intentionally split across local IR and bridge for corpus hygiene.

### gpt-5.4

- local_source_alignment: `partially_corresponds`
- corpus_alignment: `corresponds`
- relation_type: `one_way_implication`
- needs_context: `True`
- context_used: `bridge, provenance, translator_notes, related_sections`
- confidence: `0.93`

Reason:

The local IR covers nearly all explicit section 4.1 content faithfully, including the methodology reference, standard-formula basis, reinvestment rule, 5% adjusted-return construction, SOLTCA50 50-point decrement, day-count boundary semantics, and the displayed formula. The main source-only issue is scope: the sentence introducing the displayed formula reads locally like a generic adjusted-return formula, while the IR attaches it only to SOLTCA50. Corpus context explicitly documents and supports that narrower reading via section 1.2 and the bridge layer, so the corpus-level judgment is correspondence.

Semantic differences:

- none

Context-resolved issues:

- Source-only, the clause 'The adjusted return Index is calculated according to the following formula' could be read as applying to every adjusted-return index or at least to the generic AdjustedReturnVersion; translator notes plus related section 1.2 explicitly resolve that the displayed formula is the SOLTCA50 / 50 AR formula only.
- The use of source-local entities such as PriceReturnIndexVersion, NTRIndexVersion, GTRIndexVersion, AdjustedReturnVersion, and SOLTCA50 may look underidentified in isolation, but bridge provenance explicitly maps them to the canonical section 1.2 index entities without treating those identities as local source claims.
- The equality ex_date(p) = effective_date(p) may look stronger than a loose association on a source-only pass, but translator notes explicitly justify it from the parenthetical 'effective date (the so called ex-date)' as an appositive equivalence in this local context.

Stylistic notes:

- The IR introduces both AdjustedReturnVersion and SOLTCA50 as adjusted-return indices; this is semantically motivated but the naming could confuse readers because one is generic-sounding and the other ticker-specific.
- `equity_index_methodology_reference` mixes source claims with minor plumbing such as the Section 1.2 locator; provenance already marks that distinction.
- `standard_index_formula_basis` uses explicit component/day quantification and helper relations for price change, weight, and currency conversion; this is more formal than the prose but not semantic drift.
