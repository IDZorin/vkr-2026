# Draughts-64 Demo

This demo uses 64-square draughts rules as a public formal-rules domain. It is
included to show that A4V3 can model non-legal rule systems with explicit board
geometry, game pieces, move legality predicates, and an operational legality
layer.

Included artifacts:

- `data/source.md` - source rule fragment.
- `data/main_ir.a4v3` - final A4V3 IR with board geometry and operational
  legality bridges.
- `data/provenance.yaml` - source grounding and back-translations.
- `data/translator_notes.md` - modeling notes.
- `expected_results.json` - recorded query outcomes.

Run from the repository root:

```bash
python demos/run_recorded_demo.py draughts_64
```

Important limitation: the recorded demo is the reproducible publication path.
The research workspace also tested live SMT and LLM query drivers, but those
experiments exposed known performance limits for quantifier-heavy SAT cases.
They are not enabled as the default public demo.

Source note: if redistributing official federation rule text, verify the current
publication and attribution terms.

