# IR pipeline — current implementation state

## seed methodology corpus update — 2026-05-19

The DZ methodology corpus has a newer end-to-end state snapshot:

- [full_pipeline_architecture_v1.md](full_pipeline_architecture_v1.md)
- [dz_end_to_end_corpus_state_v1.md](dz_end_to_end_corpus_state_v1.md)

Those documents are the current references for the high-level pipeline architecture and for how the DZ local IR, provenance/audit envelopes, bridge layer, resolved bridge decisions, canonical ontology, process/workflow files, SMT witness/probe sidecars, and RDF/OWL/SHACL backend projections are stored.

Short status:

- seed local corpus: 22 sections, 32 definitions, 1 appendix;
- backend projection targets: 61;
- RDF/OWL/SHACL backend checks: 61/61/61 `ok`;
- backend hard findings: 0;
- backend soft findings: 0;
- resolved OWL review items: 0;
- unresolved resolved-OWL symbols: 0;
- SMT hybrid probes: hard findings 0; N31 full-SMT timeouts are covered by bounded SAT fallback.

The rest of this file is the older 2026-04-27 implementation snapshot for the generic IR pipeline.

**Дата снимка:** 2026-04-27. Этот документ — точный снимок что РЕАЛЬНО реализовано в коде на эту дату, в отличие от концептуальных описаний в `IR/text_to_normalization/README.md` etc. Обновлять при каждом существенном изменении.

## Per-entry agent workflow (полный цикл)

```
INPUT: source.md (raw span, 1-3 предложения)
        ↓
Stage 1: NORMALIZE       → normalized.md
Stage 1.A: validate norm → metrics_normalization_v1.json + gate
        ↓
Stage 2: TRANSLATE L1-L8 → main_ir.a4v3
        ↓
Stage 3: METRICS         → 8+ metric files
        ↓
Stage 4: DIAGNOSTIC      → diagnostic_suite_v1.json (findings)
        ↓
Stage 4.B: GATE          → pass / continue
        ↓
Stage 5: REPAIR          → archive prev IR, write new IR
        ↓
goto Stage 3 (until pass / max_iter / no-improvement)
```

## Stage 1 — Normalization

**Реализация:** [IR/src/normalize_v1.py](../src/normalize_v1.py)

| компонент | детали |
|---|---|
| Механизм | один LLM-вызов через `llm_helper_v1.chat` |
| Default model | `gpt-5.4-mini` (через env `IR_DEFAULT_LLM_MODEL`) |
| Промпт | preserves every content token, expand acronyms, resolve anaphora, atomic clauses one-per-line |
| Retry с feedback | да — если gate fail, второй вызов получает explicit lost/added tokens |
| Max retries | 3 |
| Output | `normalized.md`, `normalize_v1_meta.json` |

**Что НЕ хардкожено в промпте:** конкретные термины методики, prelude sorts, domain-specific lists. См. `feedback_no_hardcoded_domain_strings`.

## Stage 1.A — Normalization metrics + gate

**Реализация:** [IR/src/normalization_metrics_v1.py](../src/normalization_metrics_v1.py)

| метрика | вычисление | используется в gate? |
|---|---|---|
| `tokens_lost_in_normalization` | set(src) − set(norm) — конкретный список | ✅ feedback для retry |
| `tokens_added_in_normalization` | set(norm) − set(src) | ✅ feedback для retry |
| `recall_norm_covers_source` | |overlap| / |src| | ✅ gate criterion |
| `precision_norm_to_source` | |overlap| / |norm| | ❌ analytical only |
| `jaccard` | |overlap| / |union| | ❌ analytical |
| `bertscore_f1` | BERT cos similarity | ❌ optional, not in gate |
| `nli_*` | NLI entailment + contradiction | ❌ optional |

**Gate (token-only по умолчанию):**
- `recall_norm_covers_source ≥ 0.95` — единственный обязательный критерий
- BERT/NLI убраны из gate (2026-04-27): они для render-back на Stage 4, не для нормализации
- BERT/NLI остаются доступны через `--semantic` флаг для аналитики

## Stage 2 — Translator L1-L8

**Реализация:** [IR/src/translator/orchestrator.py](../src/translator/orchestrator.py)

| layer | вход | механизм | выход |
|---|---|---|---|
| L1 segment | normalized text | det regex (sentence boundary, bullet strip) | list[Clause] |
| L2 bridge_classify | clauses | det signals (family_coverage_v1) + LLM | family + kind per clause |
| L3 sort_extract | clauses + classifications | LLM | TypeDecl list |
| L4 symbol_decl | sorts + clauses | LLM | SymbolDecl list (entity/fun/rel) |
| L5 body_assemble | sorts + symbols + clauses | LLM (главный creative шаг) | body_text per assertion |
| L6 validate | весь IR | det parser + grounding check | ValidationReport |
| L7 critic_loop | IR + validation | LLM | repair pass (max_retries=1) |
| L8 multi_judge | финальный IR | ансамбль LLM | multi_judge verdict |

**Внутри одной entry → batch processing.** Все clauses обрабатываются вместе, создаётся один IR с shared sorts/symbols. Per-clause + merge — отдельный экспериментальный путь, см. `IR/src/run_per_clause_v1.py` и `merge_irs_v1.py`.

**Известные проблемы (НЕ исправлены):**
- L3 имеет хардкод prelude-списка в SYSTEM-промпте, который **расходится** с canonical `IR/index/minimal_prelude_v1.json`
- L4, L5, L7, L8 не знают про prelude
- Normalize_v1 и Repair_v1 тоже не знают про prelude
- Это нарушение `feedback_no_hardcoded_domain_strings` — TODO исправить

## Stage 3 — Метрики per-entry

| генератор | output | механизм |
|---|---|---|
| `legacy_metrics_runner_v1` + `extended_legacy_metrics_v1` | `main_ir_metrics_v1.json` (25 секций, 134 extended ключа) | det |
| `family_coverage_v1` | `metrics_family_coverage_v1.json` | det |
| `source_phrase_coverage_v1` | `metrics_source_phrase_coverage_v1.json` | det |
| `modal_temporal_preservation_v1` | `metrics_modal_temporal_preservation_v1.json` | det |
| `lowering_audit_v1` | `lowering_audit_v1.json` | det |
| `a4v3_semantic_lint_v1` | `a4v3_semantic_lint_v1.json` | det translator-lint |
| `targeted_probes_v1` | `metrics_targeted_probes_v1.json` | LLM (9 проб) |
| `multi_judge_consensus_v1` | `metrics_multi_judge_consensus_v1.json` | LLM ensemble |
| `counterexample_probing_v1` | `metrics_counterexample_probing_v1.json` | LLM |
| `fact_extraction_compare_v1` | `metrics_fact_extraction_compare_v1.json` | LLM |
| `legacy_runner.generate_llm_stage_metrics` | `*_llm_render_metrics_*.json` + `*_llm_semantic_verdict_*.json` | LLM render-back + judge |
| `pipeline_telemetry_v1` | `pipeline_telemetry_v1.json` | агрегатор tokens/latency (НЕ quality) |

## Stage 4 — Diagnostic suite

**Реализация:** [IR/src/run_diagnostic_suite_v1.py](../src/run_diagnostic_suite_v1.py)

- **634 правила** в `IR/rules/<module>/diagnostic_rules.json` (6 модулей)
- `a4v3_semantic_lint` is an additional deterministic rule module registered in `IR/rules/a4v3_semantic_lint/diagnostic_rules.json` and auto-run by `run_diagnostic_suite_v1.py`; it includes dead declarations, deontic/name smells, label-only universal predicate constraints, numeric-sort smells, and weak `based_on` link checks.
- Покрытие: 91.4% правил resolve на каждой записи
- Каждое finding содержит self-contained пакет: `value`, `evidence_blocks`, `bad_value_means`, `repair_target`, `what_it_counts`, `how_to_compute`, `scope` (span/corpus)
- `audit_rules_v2.py` классифицирует правила по 4 осям: `where × what × why × scope`

## Stage 5 — Repair

**Реализация:** [IR/src/repair_v1.py](../src/repair_v1.py)

| функция | детали |
|---|---|
| `filter_actionable(findings)` | level∈{fail,warning} + scope=span + repair_target есть |
| Promt | "apply repair_target LITERALLY for each finding, output complete a4v3" |
| Архив | предыдущий IR → `main_ir_old_v{n}.a4v3` |
| Output | новый `main_ir.a4v3` + `repair_v1_meta_iter{n}.json` |

## Stage 5 (loop) — Agent loop

**Реализация:** [IR/src/agent_loop_v1.py](../src/agent_loop_v1.py)

| фаза | что |
|---|---|
| outer loop | до `max_iter=5` IR-итераций |
| stop conditions | gate_pass / no_improvement (2 итерации без снижения actionable) / max_iter |
| inner loop | до `max_norm_iter=3` нормализации с feedback |
| history | `_diagnostics_history/iter_NN/` snapshot per IR-итерация |
| итог | `agent_loop_v1.json` log |

## Merge (deferred — V0 покрывает 1 из 8 типов)

**Реализация:** [IR/src/merge_irs_v1.py](../src/merge_irs_v1.py) — **только L1 syntactic exact_merge**

⚠️ **ВАЖНО:** Это покрывает только 1 из 8 типов alignment (exact_merge). Реальный merge архитектурно описан в `IR/docs/merge_architecture_v1.md` и [thoughts/IR_schema/merge_alignment_policy_v1.md](../../thoughts/IR_schema/merge_alignment_policy_v1.md). Включает 3 слоя (L0 local / L1 exact / L2 ontology), 8 типов alignment proposals, embedding-based candidate finder, LLM proposal layer, world-knowledge LLM, backtest для local rewrites, user hints для ambiguous cases.

**Что в V0 есть:**
- Syntactic dedup: parse через `a4v3_parser_v1`, группировка по (family, name)
- TypeDecl/AssertDecl с одинаковым именем → keep first
- SymbolDecl с одинаковым именем но разным signature → conflict в `merge_meta.json`
- Generic interface — работает на любом уровне: clause / span / methodology / multi-methodology

**Что V0 НЕ делает (требует L2):**
- Семантическое слияние синонимов (`TradingPrice` vs `TradePrice`)
- bridge_family / bridge_supertype / role_link / subclass_of / keep_separate_with_link / conflict_split / ambiguous
- World-knowledge LLM gate
- Embedding-based candidate finding
- User hints для ambiguous
- Backtest для local rewrites

**См. подробно:** [IR/docs/merge_architecture_v1.md](merge_architecture_v1.md)

## Эксперимент C — per-clause IR (без merge)

**Реализация:** [IR/src/run_per_clause_v1.py](../src/run_per_clause_v1.py)

Цель: понять **изолированное качество** per-clause IR до того как делать merge.
Для каждой clause normalized.md создаётся отдельный mini-IR + per-clause метрики.

## Inter-run comparison

**Реализация:** [IR/src/inter_run_comparison_v1.py](../src/inter_run_comparison_v1.py)

Pairwise сравнение между ранами для `gold_*` метрик. CLI:
```
python inter_run_comparison_v1.py --base <run> --compare <run>
```

Generalize silver-baseline-comparison: любая пара ранов, не привязка к silver.

## Файловый контракт каждой entry

```
entry_dir/
├── source.md                 ← вход
├── normalized.md             ← Stage 1
├── normalize_v1_meta.json    ← Stage 1
├── metrics_normalization_v1.json  ← Stage 1.A
├── main_ir.a4v3    ← Stage 2 (финал)
├── main_ir_old_v{n}.a4v3   ← Stage 5 (архивы)
├── L1_segment.json … L8_multi_judge.json   ← Stage 2 чекпоинты
├── translation_state.json    ← Stage 2
├── main_ir_metrics_v1.json
├── metrics_*.json (8+)       ← Stage 3
├── *_llm_render_metrics_*.json + *_llm_semantic_verdict_*.json ← Stage 3 LLM
├── pipeline_telemetry_v1.json
├── lowering_audit_v1.json
├── a4v3_semantic_lint_v1.json + .md
├── diagnostic_suite_v1.json + .md  ← Stage 4
├── repair_v1_meta_iter{n}.json
├── inter_run_comparison_v1.json    ← optional cross-run
├── agent_loop_v1.json        ← полный лог loop
└── _diagnostics_history/     ← snapshot за каждую итерацию
```

## Что НЕ реализовано

- **Prelude inheritance в агентах** — все агенты должны читать canonical `IR/index/minimal_prelude_v1.json` (сейчас только L6 grounding check читает; L3 имеет хардкод; L4-L8, normalize, repair не знают)
- **User hints канал** — формат `hints.md` рядом с `source.md` для per-span подсказок (см. `feedback_no_hardcoded_domain_strings`)
- **Document-level merge (V5 layers 22-24)** — `det_wire_graph`, `llm_judge_relations`, `llm_check_completeness`. Merge V0 syntactic есть, но cross-entry нет
- **Семантический merge** — LLM-вызов "are these synonymous?" для слияния `TradingPrice` ↔ `TradePrice` etc.
- **Нормализатор-генератор V5 layers 16-18** — `det_normalize`, `llm_normalize`, `llm_judge_normalize`. Сейчас только `normalize_v1` (один LLM) — это упрощённая реализация только LLM-части
