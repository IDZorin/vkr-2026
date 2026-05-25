# Financial Methodology Case Study

This package is a cleaned end-to-end artifact bundle for one financial index
methodology translated into A4V3 IR.

It is intended to show the complete methodology-scale pipeline:

- local fragment translation into `main_ir.a4v3`;
- claim-level provenance and translator notes;
- deterministic quality checks and diagnostic reports;
- bridge and merge layers;
- process and reasoning artifacts;
- RDF/OWL/SHACL/SMT-oriented backend projections.

## Contents

- `fragments/sections/` - 22 section-level local A4V3 packages.
- `fragments/definitions/` - 32 definition-level local A4V3 packages.
- `fragments/appendix/` - 1 appendix-level local A4V3 package.
- `bridge/` - cross-fragment bridge decisions and bridge lint reports.
- `merge/` - canonical merged ontology and merge readiness reports.
- `process/` - process-layer ontology and workflow artifacts.
- `reasoning/` - SMT probe specifications, generated SMT files, and probe reports.
- `backend_projection/` - RDF, OWL, SHACL, and resolved projection outputs.
- `FRAGMENT_INDEX.csv` - compact index of all 55 local packages.
- `MANIFEST.csv` - file-level manifest with SHA-256 hashes and omission notes.
- `LICENSE_NOTES.md` - redistribution notes for source text and generated artifacts.
- `reports/artifact_summary.md` - short package summary.

## Curation Policy

Included:

- final `main_ir.a4v3` files;
- provenance, translator notes, role annotations, waivers, and quality snapshots;
- deterministic check reports and generated backend artifacts;
- corpus-level bridge, merge, process, reasoning, and projection layers.

Excluded:

- `source.md` and `normalized.md`, because the original methodology text may be
  copyrighted and is not redistributed in this public package;
- draft copies such as `main_ir - Copy (*.a4v3)` and `main_ir copy *.a4v3`;
- agent run directories, exploratory transcripts, temporary judge workspaces,
  and intermediate LLM rendering/verdict files.

The excluded files are still represented in `MANIFEST.csv` with omission notes
so that the artifact boundary is explicit rather than implicit.

## Reproducibility Notes

This is a frozen artifact package, not a live regeneration script. The generated
files can be inspected directly. IR-only checks can be rerun on the included
`main_ir.a4v3` files.

Example:

```bash
python IR/src/a4v3_parser_v1.py case_studies/financial_methodology/fragments/sections/section_1_3/main_ir.a4v3 --strict
```

The full `tools/check_entry.py` runner also executes source-aware checks such as
token provenance and source phrase coverage. Those checks require the original
`source.md` / `normalized.md` files and should be rerun in a private workspace
where the methodology source text is available under its own terms.

For publication and review, use `FRAGMENT_INDEX.csv` for navigation and
`MANIFEST.csv` when exact file identity matters.
