# Diagnostic Rules Coverage

Правила в `IR/rules/` отфильтрованы под то, что реально появляется в
артефактах прогона `IR/outputs/runs/unified_methodology_v1/`. Полный
каталог из 689 placements хранится в исходнике
`thoughts/IR_schema/unified_methodology_mini_project_v1/`.

| Module | Metrics | Checks | Rules | JSON | Markdown |
| --- | ---: | ---: | ---: | --- | --- |
| `source_normalization` | 26 | 11 | 37 | `../rules/source_normalization/diagnostic_rules.json` | `../rules/source_normalization/diagnostic_rules.md` |
| `ontology_planning` | 44 | 20 | 64 | `../rules/ontology_planning/diagnostic_rules.json` | `../rules/ontology_planning/diagnostic_rules.md` |
| `formula_ir_drafting` | 173 | 15 | 188 | `../rules/formula_ir_drafting/diagnostic_rules.json` | `../rules/formula_ir_drafting/diagnostic_rules.md` |
| `quality_evaluation` | 243 | 46 | 289 | `../rules/quality_evaluation/diagnostic_rules.json` | `../rules/quality_evaluation/diagnostic_rules.md` |
| `merge_canonicalization` | 63 | 15 | 78 | `../rules/merge_canonicalization/diagnostic_rules.json` | `../rules/merge_canonicalization/diagnostic_rules.md` |
| `user_hints_provenance` | 0 | 0 | 0 | `../rules/user_hints_provenance/diagnostic_rules.json` | `../rules/user_hints_provenance/diagnostic_rules.md` |

Total metric placements: 549
Total check placements: 107
Total diagnostic rules: 656

## Что отброшено и почему

Из исходных 689 placements 33 уникальных правила не появляются в этом
прогоне (manual single-variant без orchestrator/hints). Они закономерно
относятся к функциональностям, которых здесь не было:

- **6 user-hints чеков** — в прогоне не было user hints
- **5 acceptance-gate чеков** — manual прогон без agent orchestrator
- **9 backtest/merge-rewrite чеков** — без локальных rewrite после alignment
- **10 policy чеков** (ontology/shape гайдлайны) — поведенческие принципы, не записываются как named JSON keys
- **3 meta/aux** (`best_*`, `identifier_glue_metrics`, `render_threshold`)

Полный список — в `_dropped.txt` в исходном каталоге (см. провенанс ниже)
или восстановим по diff с
`thoughts/IR_schema/unified_methodology_mini_project_v1/`.
