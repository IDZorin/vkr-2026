# Thesis Artifact Mapping

This file connects the thesis text to the public repository artifacts. It is a
neutral mapping layer: thesis-facing names avoid private corpus identifiers,
while the repository paths point to inspectable public files.

Status meanings:

- `included` - file or directory is included in this public bundle.
- `template` - the thesis uses a neutral path pattern; the public bundle
  contains a template or README instead of private corpus data.
- `reference` - code is included for inspection, but is not part of the default
  reproducible runtime.
- `private_source` - the original artifact exists in the research workspace but
  is not included because it may contain private methodology corpus material.

## 1. Local Fragment Package

| Thesis artifact name | Public mapping | Status | Notes |
|---|---|---:|---|
| `source.md` | `examples/section_2_3_weighting/source.md`; `examples/rebalance_day_source_conflict/source.md`; `demos/russian_law/data/source.md`; `demos/draughts_64/data/source.md` | included | Four public examples are provided. |
| `normalized.md` | `examples/rebalance_day_source_conflict/normalized.md`; `thesis_artifacts/agent_run_example_draughts_64/discovery/*` and public demo source packages | partial | Some public demos do not need a separate normalized file; the financial methodology package omits normalized source derivatives. |
| `main_ir.a4v3` | `examples/section_2_3_weighting/main_ir.a4v3`; `examples/rebalance_day_source_conflict/main_ir.a4v3`; `demos/*/data/main_ir.a4v3`; `case_studies/financial_methodology/fragments/**/main_ir.a4v3` | included | Final local A4V3 IR. The financial case study includes 55 clean local entries. |
| `provenance.yaml` | `examples/section_2_3_weighting/provenance.yaml`; `examples/rebalance_day_source_conflict/provenance.yaml`; `demos/*/data/provenance.yaml`; `case_studies/financial_methodology/fragments/**/provenance.yaml` | included | Claim-level grounding and back-translation. |
| `translator_notes.md` | `examples/rebalance_day_source_conflict/translator_notes.md`; `demos/*/data/translator_notes.md`; `case_studies/financial_methodology/fragments/**/translator_notes.md` | included | Modeling and ambiguity notes. |
| `waiver*.json` | `examples/section_2_3_weighting/waiver_token_absorption_v1.json`; `examples/rebalance_day_source_conflict/waiver_token_absorption_v1.json`; `demos/*/data/waiver_token_absorption_v1.json`; `case_studies/financial_methodology/fragments/**/waiver*.json` | included | Human-approved token waivers. |
| `role_annotations.yaml` | `case_studies/financial_methodology/fragments/**/role_annotations.yaml` | included | Role annotations for the full financial methodology case study. |
| `quality_snapshot_v1.*` | `examples/section_2_3_weighting/quality_snapshot_v1.md`; `examples/rebalance_day_source_conflict/quality_snapshot_v1.md`; `demos/*/data/quality_snapshot_v1.md`; `case_studies/financial_methodology/fragments/**/quality_snapshot_v1.*` | included | Public snapshot files are kept as compact Markdown/JSON. |
| `agent_triage.*` | `thesis_artifacts/agent_run_example_draughts_64/agent_triage.*` | included | Sanitized public agent-run example. |
| `*_v1.json`, `*_v1.md` reports | `IR/rules/**`; `thesis_artifacts/diagnostic_rules/`; `case_studies/financial_methodology/fragments/**/*.json`; `case_studies/financial_methodology/fragments/**/*.md` | included | The financial methodology case study includes generated per-entry reports. Deterministic tools can also regenerate checks. |

## 2. Agent Run

| Thesis artifact name | Public mapping | Status | Notes |
|---|---|---:|---|
| `agent_run_*` | `thesis_artifacts/agent_run_example_draughts_64/` | included | Public Draughts-64 run used as inspectable example. |
| `agent_metadata.json` | `thesis_artifacts/agent_run_example_draughts_64/agent_metadata.json` | included | Local absolute paths sanitized. |
| `agent_state.json` | `thesis_artifacts/agent_run_example_draughts_64/agent_state.json` | included | Sanitized. |
| `agent_transcript.json` | `thesis_artifacts/agent_run_example_draughts_64/agent_transcript.json` | included | Sanitized transcript; not used by default demo runner. |
| `iter_*`, `iter_meta.json` | `thesis_artifacts/agent_run_example_draughts_64/README.md` | template | Iteration snapshots are part of the agent-run contract; this public example keeps the compact final trace. |
| `verdict.json` | `thesis_artifacts/agent_run_example_draughts_64/critic_swarm_v1.json` | included | Critic/judge verdicts are represented by the critic swarm report. |
| `strategy_v*.md` | `thesis_artifacts/agent_run_example_draughts_64/discovery/strategy_v0.md` | included | Public strategy artifact. |
| `ir_vs_strategy_check_v*.json/md` | `thesis_artifacts/agent_run_example_draughts_64/ir_vs_strategy_check_v3.*` | included | Strategy-to-IR alignment report. |
| `critic_swarm_v1.json` | `thesis_artifacts/agent_run_example_draughts_64/critic_swarm_v1.json` | included | Public critic-swarm output. |
| `keep_drop_replace_v*.md` | agent-run contract; generated by package tools | template | Not present in the selected public run; covered by implementation reference. |
| `pre_rollback_*.a4v3`, `rollback_log.md` | agent-run contract; generated on rollback | template | Not present in the selected public run. |
| `provenance*.yaml`, `provenance_*_v1.*` | `thesis_artifacts/agent_run_example_draughts_64/provenance.yaml` | included | Public final provenance artifact. |

## 3. Implementation Modules

| Thesis path | Public mapping | Status |
|---|---|---:|
| `IR/src/ir_agent/loop.py` | `thesis_artifacts/implementation_reference/IR/src/ir_agent/loop.py` | reference |
| `IR/src/ir_agent/phases.py` | `thesis_artifacts/implementation_reference/IR/src/ir_agent/phases.py` | reference |
| `IR/src/ir_agent/env.py` | `thesis_artifacts/implementation_reference/IR/src/ir_agent/env.py` | reference |
| `IR/src/ir_agent/snapshots.py` | `thesis_artifacts/implementation_reference/IR/src/ir_agent/snapshots.py` | reference |
| `IR/src/ir_agent/tools/` | `thesis_artifacts/implementation_reference/IR/src/ir_agent/tools/` | reference |
| `IR/src/a4v3_parser_v1.py` | `IR/src/a4v3_parser_v1.py`; also mirrored in `thesis_artifacts/implementation_reference/IR/src/` | included |
| `IR/src/audit_rules_v1.py` | `thesis_artifacts/implementation_reference/IR/src/audit_rules_v1.py` | reference |
| `IR/src/audit_rules_v2.py` | `thesis_artifacts/implementation_reference/IR/src/audit_rules_v2.py` | reference |
| `IR/src/lowering_audit_v1.py` | `IR/src/lowering_audit_v1.py` | included |
| `IR/src/fragment_readiness_audit_v1.py` | `IR/src/fragment_readiness_audit_v1.py` | included |
| `IR/src/bridge_lint_v1.py` | `IR/src/bridge_lint_v1.py` | included |
| `IR/src/bridge_candidate_audit_v1.py` | `thesis_artifacts/implementation_reference/IR/src/bridge_candidate_audit_v1.py` | reference |
| `IR/src/merge_readiness_audit_v1.py` | `IR/src/merge_readiness_audit_v1.py` | included |
| `IR/src/extended_canonical_validator_v1.py` | `thesis_artifacts/implementation_reference/IR/src/extended_canonical_validator_v1.py` | reference |
| `IR/src/process_reasoning_audit_v1.py` | `IR/src/process_reasoning_audit_v1.py` | included |
| `IR/src/smt_probe_runner_v1.py` | `IR/src/smt_probe_runner_v1.py` | included |
| `IR/src/smt_consistency_check_v1.py` | `IR/src/smt_consistency_check_v1.py` | included |
| `IR/src/legacy_metrics/compute_translation_metrics_v1.py` | `thesis_artifacts/implementation_reference/IR/src/legacy_metrics/compute_translation_metrics_v1.py` | reference |

## 4. Base Vocabularies And Preludes

| Thesis path pattern | Public mapping | Status |
|---|---|---:|
| `IR/index/*prelude*_v1.*` | `IR/index/*prelude*_v1.*` | included |
| `IR/index/minimal_prelude_v1.*` | public demos include their local minimal preludes where needed; core prelude files are under `IR/index/` | included/template |
| `IR/index/domain_prelude_financial_values_v1.*` | `IR/index/domain_prelude_financial_values_v1.*` when present in public bundle | included/template |
| `IR/index/domain_prelude_index_methodology_v1.*` | `IR/index/domain_prelude_index_methodology_v1.*` | included |

## 5. Diagnostic Rule Catalog

| Thesis artifact name | Public mapping | Status |
|---|---|---:|
| `IR/rules/*/diagnostic_rules.json` | `IR/rules/*/diagnostic_rules.json` | included |
| `rules_audit_v2.json` | `thesis_artifacts/diagnostic_rules/rules_audit_v2.json` | included |
| `rules_audit_v2.md` | `thesis_artifacts/diagnostic_rules/rules_audit_v2.md` | included |
| `rules_audit_v2` | `thesis_artifacts/diagnostic_rules/` | included |

## 6. Full Run Slice Layers

| Thesis neutral path | Public mapping | Status | Notes |
|---|---|---:|---|
| `IR/outputs/runs/<run_id>/bridge/` | `case_studies/financial_methodology/bridge/` | included | Full financial methodology bridge layer. |
| `IR/outputs/runs/<run_id>/merge/canonical_ontology_v1.a4v3` | `case_studies/financial_methodology/merge/canonical_ontology_v1.a4v3` | included | Canonical merged ontology for the financial methodology case study. |
| `IR/outputs/runs/<run_id>/process/` | `case_studies/financial_methodology/process/` | included | Process-layer artifacts. |
| `IR/outputs/runs/<run_id>/reasoning/` | `case_studies/financial_methodology/reasoning/` | included | SMT probe specs, generated SMT files, and probe reports. |
| `IR/outputs/runs/<run_id>/backend_projection/` | `case_studies/financial_methodology/backend_projection/` | included | Projection artifact names are mapped below. |
| `*_owl_union.ttl`, `*_owl_resolved.ttl` | `case_studies/financial_methodology/backend_projection/all/` | included | Resolved and union OWL projections for the case study. |

## 7. Target Projections

| Thesis artifact name | Public mapping | Status |
|---|---|---:|
| `rdf.ttl`, `rdf.emission.json`, `rdf.check.json` | `case_studies/financial_methodology/backend_projection/**/rdf.*` | included |
| `owl.ttl`, `owl.emission.json`, `owl.check.json` | `case_studies/financial_methodology/backend_projection/**/owl.*` | included |
| `shacl_shapes.ttl`, `shacl.emission.json`, `shacl.check.json` | `case_studies/financial_methodology/backend_projection/**/shacl*` | included |
| `*.smt2` | `case_studies/financial_methodology/reasoning/smt_probes*/**/*.smt2` | included |
| `smt_probe_results_v1.json`, `smt_probe_results_v1.md` | `case_studies/financial_methodology/reasoning/smt_probe_results_v1.*`; public demo result summaries: `demos/*/expected_results.json` | included |

## 8. Mutation Benchmark

| Thesis neutral name | Public mapping | Status |
|---|---|---:|
| `mutation_benchmark_v2/reports/*.json` | `thesis_artifacts/mutation_benchmark_v2/reports/*.json` | included |
| `mutation_benchmark_v2/reports/*.csv` | `thesis_artifacts/mutation_benchmark_v2/reports/*.csv` | included |
| `mutation_benchmark_v2/reports/*.md` | `thesis_artifacts/mutation_benchmark_v2/reports/*.md` | included |
| `mutation_benchmark_v2/cases/<case_id>/source_original.md` | `thesis_artifacts/mutation_benchmark_v2/README.md` | private_source |
| `source.md`, `normalized.md`, `original_ir_reference.a4v3`, `manual_ir_working.a4v3`, `backend_surface_ir.a4v3`, `<case_id>.json`, `notes.md`, `manual_ir_working_metrics_v1.json`, `backend_results.json` | `thesis_artifacts/mutation_benchmark_v2/README.md` | private_source |

The public name is `mutation_benchmark_v2`; the original working directory name
is intentionally not used in thesis-facing references.

## 9. Pilot 40 Methodologies And H3

| Thesis artifact name | Public mapping | Status |
|---|---|---:|
| `pilot_40_methodologies_statistics_v1.md` | `thesis_artifacts/pilot_40/pilot_40_methodologies_statistics_v1.md` | included |
| `pilot_40_methodologies_results_v1.md` | `thesis_artifacts/pilot_40/pilot_40_full_machine_report_sanitized.md` | included/sanitized |
| Aggregated pilot reports | `thesis_artifacts/pilot_40/` | included |

The thesis should cite the clean statistics appendix and the neutral
`pilot_40_full_machine_report_sanitized.md`, not the raw working report name.

## 10. Models And External Working Reports

| Thesis artifact name | Public mapping | Status |
|---|---|---:|
| `IR/docs/current_state_v1.md` | `thesis_artifacts/workflow_reports/current_state_v1_sanitized.md` | included/sanitized |
| `IR/docs/agent_v2_workflow_v1.md` | `thesis_artifacts/workflow_reports/agent_v2_workflow_v1_sanitized.md` | included/sanitized |
| `IR/outputs/runs/russian_law/FINAL_EXPERIMENT_SUMMARY.md` | `thesis_artifacts/external_domains/russian_law_final_experiment_summary.md` | included/sanitized |

## 11. Figures

| Thesis figure path | Public mapping | Status |
|---|---|---:|
| `figures/chapter2_fit_matrix.png` | `figures/chapter2_fit_matrix.png` | included |
| `figures/chapter3_pipeline_overview.png` | `figures/chapter3_pipeline_overview.png` | included |
| `figures/chapter5_h1_quality_components.png` | `figures/chapter5_h1_quality_components.png` | included |
| `figures/chapter5_a4v3_family_counts.png` | `figures/chapter5_a4v3_family_counts.png` | included |
| `figures/chapter5_smt_statuses.png` | `figures/chapter5_smt_statuses.png` | included |
| `figures/chapter5_mutation_outcomes.png` | `figures/chapter5_mutation_outcomes.png` | included |
| `figures/chapter5_mutation_classes_stacked.png` | `figures/chapter5_mutation_classes_stacked.png` | included |
| `figures/chapter5_projection_signals.png` | `figures/chapter5_projection_signals.png` | included |
| `figures/chapter5_reuse_learning_curve.png` | `figures/chapter5_reuse_learning_curve.png` | included |
| `figures/chapter5_transferability_matrix.png` | `figures/chapter5_transferability_matrix.png` | included |

## Recommended Thesis Citation Pattern

Use this mapping document as the stable appendix pointer:

> The public repository contains a neutral artifact mapping in
> `docs/thesis_artifact_mapping.md`. The curated financial methodology case
> study is included under `case_studies/financial_methodology/` without
> redistributing the original source text; other private methodology-corpus
> workspaces are represented either by sanitized aggregate reports or by neutral
> templates. Public-domain/public-rules demonstrations are included under
> `demos/`.
