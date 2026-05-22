# Russian Law Demo

This demo uses a public historical legal text fragment ("Russkaya Pravda") as a
non-private domain for A4V3 translation and recorded NL-to-SMT checks.

Included artifacts:

- `data/source.md` - source fragment.
- `data/main_ir.a4v3` - final A4V3 IR.
- `data/provenance.yaml` - source grounding and back-translations.
- `data/translator_notes.md` - modeling notes.
- `expected_results.json` - recorded query outcomes.

The recorded demo covers 11 inputs:

- 5 law-consistent penalty/applicability questions;
- 4 adversarial denials contradicted by the formalized rules;
- 2 out-of-scope refusals.

Run from the repository root:

```bash
python demos/run_recorded_demo.py russian_law
```

Source note: the legal content is historical. If publishing a specific modern
edition or transcription, verify and cite the edition/source used.

