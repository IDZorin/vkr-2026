# Fragment Readiness Audit Inventory v1

This layer audits local seed methodology fragments after their normal per-entry checks have
already been run. It does not rewrite `main_ir.a4v3`, does not replace
`provenance.yaml`, and does not regenerate the heavier LLM or embedding-based
reports.

## Scope

The audit covers local fragment entries under:

- `sections/*`
- `definitions/*`
- `appendix/*`

Each entry is treated as a source-faithful local translation unit. Cross-entry
identity, canonical ontology, and process/workflow reasoning are handled by
the bridge, canonical, and process reasoning layers.

## Audit Families

- Parse checks: every non-empty `main_ir.a4v3` must parse with zero parser
  warnings.
- Artifact envelope checks: each entry should have `source.md`,
  `main_ir.a4v3`, `provenance.yaml`, `role_annotations.yaml`, and
  `entry_checks_v1.json`.
- Provenance checks: `provenance_lint_v1.json` must have no strong findings;
  soft/advisory findings are review items.
- Role annotation checks: `role_annotation_lint_v1.json` must have no strong
  findings; soft/advisory findings are review items.
- Local semantic lint checks: strong semantic lint findings block readiness;
  soft findings are review items unless accepted by the clean-gate process.
- Coverage checks: token, family, source-phrase, and back-translation reports
  are summarized so uncovered items remain visible at corpus level.
- Lowering checks: lowering smells are review items for future backend
  lowering, not automatic local-IR failures.
- Freshness checks: reports older than their source artifacts are flagged, but
  freshness does not rewrite or rerun checks automatically.
- Quality-gate checks: `quality_snapshot_v1.json` is used as the primary
  per-entry clean-gate signal when present.

## Severity Policy

- `hard`: broken local IR, missing mandatory local envelope, parser warnings,
  failed per-entry check run, strong provenance/role/semantic findings, or a
  non-accepted quality snapshot with blocking conditions.
- `soft`: accepted-but-reviewable issues that may matter before merge, such as
  non-accepted clean gates without blocking conditions, soft lint findings,
  required family gaps, source-phrase gaps, or lowering smells.
- `advisory`: intentional deferrals, stale generated reports, uncovered tokens
  already handled by provenance/waivers, back-translation warnings, diagnostic
  warnings, and optional artifact absences.

## Interpretation

This audit answers: "Are the local fragments still clean enough to serve as
source-of-truth inputs for bridge/canonical/process reasoning?"

It does not answer:

- whether two local symbols should be merged;
- whether the canonical ontology is complete;
- whether a workflow edge is semantically correct;
- whether SHACL/RDF/SMT lowering is ready.

Those are covered by the bridge/canonical/process/operational layers.
