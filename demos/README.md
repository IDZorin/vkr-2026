# Public Demos

This directory contains public demonstrations that can be shown without exposing
the private methodology corpus.

The demos are intentionally separated from the core toolkit:

- `russian_law/` shows a historical-law fragment translated into A4V3 and used
  for recorded NL-to-SMT query checks.
- `draughts_64/` shows a formal game-rules fragment with board geometry,
  legality predicates, and recorded query checks.
- `common/` contains small experimental helpers shared by the demos.

The default demo mode is offline and reproducible. It replays recorded expected
results instead of requiring an API key or a live LLM call.

Run:

```bash
python demos/run_recorded_demo.py
```

The live LLM query drivers from the research workspace are deliberately not
included in this first public bundle. They depend on provider credentials and
domain-specific prompts; adding them later should be done as an optional layer,
not as the default reproducibility path.

