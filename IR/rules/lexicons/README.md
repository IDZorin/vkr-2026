# Lexicons — закрытые списки в одном месте

Сюда вынесены все хардкоженные списки, которые иначе сидели бы в коде или
inline-bullet'ами в policy-документах. Каждый файл — YAML, явно описанный,
правится без правки логики.

## Важное деление: что показываем LLM, что — нет

| Видимость | Что это | Где использовать |
|---|---|---|
| **LLM-facing** | Авторитетный список разрешённых токенов / структур / источников | можно вставлять в промпты, в context window, в системные сообщения |
| **detector-only** | Internal списки для post-processing (lint, метрики, диагностика) | **никогда** не включать в промпт; иначе LLM выучит их как «можно лепить» |

Каждый lexicon-файл явно отмечает свой режим в заголовке.

## Что лежит

### LLM-facing

| Файл | Что | Кто потребитель |
|---|---|---|
| `anchor_sources.yaml` | 5 источников лицензии для токенов (methodology / ontology / overlay / user_clarification / waiver). Это категории «где взять имя», их можно показывать в промпте оператора/агента | будущий `identifier_structural_anchor_gap` лайнтер + промпт переводчика |

Авторитетный prelude (5 sorts + 19 entities + 2 functions + 1 relation) живёт **отдельным spec-файлом**: [`../../index/minimal_prelude_v1.json`](../../index/minimal_prelude_v1.json). Он намеренно **минимальный** (см. notes в файле): `Day`, `Month`, `Weekday`, `FinancialInstrument`, `Event`. Methodology-specific типы (`Price`, `Currency`, `Exchange`, `Security`, `IndexComponent`, `TradingDay`, ...) в prelude **НЕ входят** и не должны туда добавляться.

### detector-only (никогда не в LLM)

| Файл | Что | Кто потребитель |
|---|---|---|
| `clause_shape_triggers.yaml` | Триггер-слова английского языка для лайнтера длинных имён (negation/condition/authority/compliance/fallback/buried_carrier) | будущий `identifier_structural_anchor_gap` лайнтер |
| `generic_primitive_tokens.yaml` | Generic слова шкал и счётчиков (`value`, `count`, `ratio`, ...) — для подавления false-positives в lint'е | `canonical_subterm_reuse_gap`, `composite_identifier_crosslink_gap` |

### Конфигурация diagnostic-генератора

| Файл | Что | Кто потребитель |
|---|---|---|
| `severity_kinds.yaml` | 5 видов severity для метрик и чеков | `IR/src/build_diagnostics_v1.py` |
| `metric_alarm_rules.yaml` | Правила «когда метрика alarming» + список бинарных метрик где 1=ok | `IR/src/build_diagnostics_v1.py` |
| `name_stem_suffixes.yaml` | Суффиксы имён метрик для извлечения stem (`_count`, `_mass`, ...) | `IR/src/build_diagnostics_v1.py` |
| `metrics_json_skip_keys.yaml` | Метаданные top-level в `metrics.json` (не метрики) | `IR/src/build_diagnostics_v1.py` |

## Принцип

Список идёт сюда, если выполнено хотя бы одно:

1. Список **читается кодом** (а не только описан в спеке) — иначе MD-bullet остаётся источником истины.
2. Список **может расширяться** без правки логики (новый триггер, новый source).
3. Список **языковой/конфигурационный**, а не доменный (нет специфики «финансовые методики»).

И ещё одно правило, особенно важное для detector-only списков:

4. **Не давать LLM списки, которые он может выучить как «можно изобретать».** Generic primitives (`value`, `count`, ...) и trigger-слова (`not`, `if`, ...) — это ровно те слова, которые LLM может начать лепить, если мы покажем их в промпте. Используем их **только** для post-processing.

Списки, которые **не нужно** сюда тащить:
- enumerations концепций в policy-документах (issue taxonomy, merge actions, definition archetypes) — они описывают спец и живут в `index/`/`outputs/runs/.../04_policies_and_rules/` как авторитетные narrative-документы; дублирование в YAML создаёт drift.
- Структурные части метрик (имена групп, поля) — они описаны в `translation_metrics_catalog_v1.md`.

## Как добавить новый

1. Создать `IR/rules/lexicons/<name>.yaml`
2. В заголовке: краткое описание + источник + потребитель
3. Добавить строку в эту таблицу
4. Если список читается кодом — обновить код (`IR/src/...`) на чтение этого файла
