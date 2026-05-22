# User Hints — Contract

**Cross-cutting слой.** Подсказки от пользователя могут применяться на любом
переходе пайплайна и должны быть видимы агенту во время трансформации.

Контрактная часть (формат, scope, чеки) живёт здесь, в `index/`. Конкретные
hints конкретного прогона — это per-run input/output, см.
[../outputs/README.md](../outputs/README.md): они кладутся в
`outputs/runs/<run_id>/user_hints/active.yaml`.

## Идея в одном предложении

Подсказка — это **простой текст-комментарий с провенансом**, отправляемый
агенту, чтобы тот учёл его при любой трансформации. Это не «скрытая память»
агента: каждая подсказка явно записана, у каждой есть scope и status.

## Формат

Минимум:

```
hint_id: H001
scope: global
       | block:<id>
       | transition:text_to_normalization
       | transition:normalization_to_ir
       | transition:ir_to_merge
text: <текст подсказки на естественном языке>
status: active | superseded | rejected
used_in: <артефакты или решения, в которых hint реально применён>
```

Рекомендуется хранить активные подсказки в одном файле (например
`active.yaml`) и архив отозванных/перекрытых рядом.

## Разделение поведения

Если подсказка **меняет локальный constraint** — артефакт обязан показать,
что изменение пришло от user clarification (т.е. провенанс должен быть
виден в notes или declaration).

Если подсказка **только даёт онтологическую поддержку** (например,
«Exchange — это объект из мировой онтологии биржевых площадок»), она
обычно живёт в declaration / notes / overlay, а не правит constraint.

## Какие правила бьют

Модуль [../rules/user_hints_provenance/](../rules/user_hints_provenance/)
определяет **6 чеков** для подсказок пользователя (в текущем прогоне они
не применялись, поскольку user hints не было):

| Чек | Что проверяет |
|---|---|
| `hint_is_explicit` | подсказка записана как plain text, а не «висит в воздухе» |
| `hint_scope_is_clear` | у hint указан scope (global / block / transition) |
| `hint_override_or_conflict_is_identified` | конфликты между подсказками явно отмечены |
| `hint_used_stage_is_recorded` | где hint реально применён — записано в `used_in` |
| `hint_not_silently_absorbed` | если hint реально изменил constraint, это видно в артефакте |
| `waiver_does_not_hide_real_lint_finding` | hint-waiver не маскирует реальную проблему |

## Что делать при противоречивых подсказках

Не «угадывать» — это сигнал. Положить конфликт в `unresolved`, запросить
у пользователя дополнительное уточнение. Пайплайн (особенно `ir_to_merge`)
может явно сообщать: «не могу объединить, hint H003 противоречит H007».

## См. также

- [pipeline_contract_v1.md](pipeline_contract_v1.md), `Global Rule: User Hints`
- [../rules/user_hints_provenance/](../rules/user_hints_provenance/)
- [../outputs/README.md](../outputs/README.md) (где per-run hints живут на диске)
