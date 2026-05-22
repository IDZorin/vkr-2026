# A4V3 IR Translation Prompt, Public Baseline v1

You are translating a source fragment into A4V3, a typed intermediate
representation for traceable rule formalization.

## Inputs

You will receive:

- `source.md`: the source fragment to translate.
- Optional `normalized.md`: a normalized but source-faithful rendering.
- Optional prelude or existing local examples.

Use only the provided source and explicitly provided context. Do not invent
facts, dates, parties, numeric values, or cross-section identities.

## Output Files

Produce:

- `main_ir.a4v3`: the A4V3 translation.
- `provenance.yaml`: claim-level grounding and back-translation.
- Optional `translator_notes.md`: design decisions, ambiguity notes, and
  source-faithfulness disclaimers.

## A4V3 Drafting Rules

1. Declare all local sorts, entities, relations, and functions used by the
   fragment unless they are explicitly supplied by the prelude.
2. Keep cross-section references local-first. If a source phrase clearly names
   an existing canonical entity, direct reference is allowed, but document it in
   notes.
3. Encode source modality explicitly:
   - use `obligation` for source obligations such as "shall" or "must";
   - use `permission` for source permissions such as "may" when agentive;
   - use `prohibition` for explicit bans;
   - use facts or constraints for descriptive claims.
4. Do not hide logical negation only in names such as `NoFee` or
   `not_provide_information`. When contradiction detection matters, introduce a
   positive carrier predicate and use explicit `not`.
5. Prefer low-arity relations. Arity above 2 requires clear role semantics or a
   translator note. Arity above 5 should be avoided unless there is a strong
   reason.
6. Avoid relation or variable names that read like whole English sentences.
   Prefer compact predicates with typed arguments.
7. Do not make an open illustrative list exhaustive unless the source states
   that it is exhaustive. Mark non-exhaustive lists explicitly when relevant.
8. Avoid global bare universals over broad sorts when the source is local to one
   section, index, document, or policy. Add an antecedent or a local subtype.
9. Use qualitative anchors such as `VagueTerm` for legally vague source phrases
   when preserving the phrase matters.

## Provenance Rules

For every material IR claim, add a provenance claim with:

- `source_quote`: short source phrase or sentence supporting the claim.
- `ir_refs`: names of the IR declarations or facts implementing the claim.
- `back_translation`: source-style English, not IR identifier prose.
- `vocabulary_basis`: one of `source_only`, `mixed`, or `ir_only`.
- `status`: usually `human_approved` once reviewed.

Back-translations should use source vocabulary. Avoid leaking CamelCase IR
identifiers such as `MethodologyChangeNeed` into natural language. Write
"methodology change need" or the exact source phrase instead.

## Validation Expectation

After drafting, run the deterministic checks for the entry, for example:

```bash
python tools/check_entry.py path/to/entry
```

If a source token is intentionally not represented in IR, add a human-approved
waiver with a concise reason. If a checker reports semantic drift, prefer
improving the IR or provenance before adding a waiver.

