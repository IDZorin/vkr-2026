# A4V3 IR Toolkit

This repository is a curated public bundle of the A4V3 intermediate
representation tooling used in a research pipeline for formalizing natural
language rules into typed, traceable IR artifacts.

## What Is Included

- `IR/src/` - public deterministic A4V3 tooling:
  - parser and AST adapter;
  - semantic lint;
  - provenance and token-coverage checks;
  - family and source-phrase coverage checks;
  - lowering audit;
  - SMT helper/probe code for the supported fragment.
- `IR/rules/` - diagnostic rule catalogs and lexicons.
- `IR/index/` - public prelude and metric/schema documentation.
- `prompts/` - publication-safe, provider-neutral prompt templates for
  drafting A4V3 entries.
- `demos/` - public-domain/public-rules demos for Russian historical law and
  Draughts-64, with recorded offline results.
- `docs/thesis_artifact_mapping.md` - thesis-to-repository artifact map.
- `thesis_artifacts/` - sanitized evidence bundle used by the thesis mapping:
  diagnostic-rule audits, agent-run example, implementation references,
  pilot/mutation reports, and workflow summaries.
- `examples/section_2_3_weighting/` - a compact checked example showing source,
  A4V3 IR, provenance, and a quality snapshot.
- `tools/check_entry.py` - a small deterministic check runner for one local IR
  entry.

## Quick Start

Requires Python 3.10+.

```bash
python -m venv .venv
.venv/Scripts/python -m pip install -e .
.venv/Scripts/python tools/check_entry.py examples/section_2_3_weighting
.venv/Scripts/python tools/check_entry.py demos/russian_law/data
.venv/Scripts/python tools/check_entry.py demos/draughts_64/data
.venv/Scripts/python demos/run_recorded_demo.py
```

On Linux/macOS, replace `.venv/Scripts/python` with `.venv/bin/python`.

You can also run individual tools directly:

```bash
python IR/src/a4v3_parser_v1.py examples/section_2_3_weighting/main_ir.a4v3 --strict
python IR/src/a4v3_semantic_lint_v1.py examples/section_2_3_weighting
python IR/src/token_provenance_v1.py examples/section_2_3_weighting
```

## Repository Layout

The repository is structured as a small monorepo:

- the reusable toolkit lives in `IR/src/`, `IR/rules/`, `IR/index/`, and
  `tools/`;
- reproducible public demos live in `demos/`;
- the compact methodology example lives in `examples/`.

The demos use recorded outputs by default. This keeps the public repository
reproducible without API keys, model availability, or live LLM variance.

Thesis-facing artifact references are centralized in
`docs/thesis_artifact_mapping.md`. Use that file as the stable bridge between
the written thesis and this repository.

## A4V3 Entry Layout

A local checked entry usually contains:

- `source.md` - source text fragment;
- `main_ir.a4v3` - A4V3 translation;
- `provenance.yaml` - claim-level source grounding and back-translation;
- optional `waiver_token_absorption_v1.json` - human-approved token waivers;
- generated check artifacts such as `metrics_token_provenance_v1.json`,
  `a4v3_semantic_lint_v1.json`, and `quality_snapshot_v1.json`.

## Scope

The SMT and backend tooling covers a supported fragment. The project does not
claim a complete executable semantics for every A4V3 construct. Deontic,
temporal, probabilistic, and action semantics may require an additional domain
profile or a specialized operational layer.

## License

The code, prompts, documentation, and repository-native artifacts are licensed
under the Apache License 2.0. Third-party source texts and quoted materials in
the examples and demos remain under their respective original terms. See
`THIRD_PARTY_NOTICES.md`.


Add a repository license if you intend others to reuse the code.
