# Canonical AST Format Extensions v1

Документ фиксирует расхождения между **строгим валидатором** canonical AST
(`thoughts/IR_schema/scripts/run_advisor_drafter_experiment.py:_validate_canonical_drafter_payload`)
и **форматом, который реально эмитирует драфтер** при ручной трансляции.

Расширенный валидатор живёт в [../src/extended_canonical_validator_v1.py](../src/extended_canonical_validator_v1.py)
и принимает оба формата. Используется в `build_diagnostics_summary_v1.py`
для acceptance gate.

## Зачем расширение

Драфтер при сборке canonical AST из manual a4v3 эмитирует кейсы, которые
строгий валидатор отвергает. Однако:

- a4v3-исходник синтаксически корректен (парсится, рендерится обратно)
- LLM-судья даёт `corresponds`
- Семантически данные кейсы выразимы в каноническом наборе строгого
  валидатора через эквивалентные конструкции (например `gte` ≡
  бинарная сравнительная операция; `enum_members` ≡ серия `entity`-деклараций)

То есть это **format quirk**, не семантический баг. Расширенный валидатор
позволяет принимать оба представления.

## Что расширено

### 1. Comparison expression kinds: `gt`, `lt`, `gte`, `lte`

Строгий валидатор поддерживает в `_validate_canonical_expr` следующие
`kind`-значения для бинарных операций: `eq`, `add`, `sub`, `mul`, `div`,
`implies`, `iff`. Сравнения `>`, `<`, `>=`, `<=` через `kind`-значение
строгий валидатор не принимает.

Драфтер же эмитирует:

```json
{
  "kind": "gte",
  "left":  { "kind": "call", "callee": "average_daily_value_traded", "args": [...] },
  "right": { "kind": "literal", "value": 5000000.0 }
}
```

Расширение принимает форму `{"kind": "gt|lt|gte|lte", "left": <expr>, "right": <expr>}`
с теми же требованиями, что и `eq`.

### 2. `count` expression kind

Строгий валидатор поддерживает `set_comp` со схемой `{kind, binder, predicate}`
(построение множества по условию). Драфтер для cardinality (мощности
множества) эмитирует тот же шаблон под именем `count`:

```json
{
  "kind": "count",
  "binder": { "name": "other", "sort": "Security" },
  "predicate": { "kind": "call", "callee": "ahead_by_ffmc", "args": [...] }
}
```

Расширение принимает `count` с той же шаблоном, что и `set_comp`.

### 3. `enum_members` поле в sort declaration

Строгий валидатор принимает `sort` declarations только в форме `{"decl": "sort", "name": "X"}`.
Любое дополнительное поле отвергается как `unexpected keys`.

Драфтер для value families (например `sort GbsFrameworkAssignment = A | B | C`
в a4v3) эмитирует:

```json
{
  "decl": "sort",
  "name": "GbsFrameworkAssignment",
  "enum_members": ["DevelopedMarketsEurope", "Europe", "Canada", "UnitedStates", "OtherGbsFrameworkAssignment"]
}
```

Семантически это эквивалентно строгой канонической форме:

```json
{"decl": "sort", "name": "GbsFrameworkAssignment"}
{"decl": "entity", "name": "DevelopedMarketsEurope", "sort": "GbsFrameworkAssignment"}
{"decl": "entity", "name": "Europe", "sort": "GbsFrameworkAssignment"}
...
```

Расширение принимает `enum_members` (валидирует как непустой список
непустых строк, без дубликатов), не требуя ручного развёртывания.

## Эффект

| | strict | extended |
|---|---:|---:|
| Sections с `ast_valid = 0` | 12 | 0 |
| Definitions с `ast_valid = 0` | 0 | 0 |
| Appendix с `ast_valid = 0` | 1 | 0 |

Через расширенный валидатор все 55 entries `ast_valid = 1`. Метрика в
`main_ir_metrics_v1.json` остаётся как считал строгий
(не перезаписываем артефакт), но `diagnostics_summary` показывает
`ast_valid_extended` и использует его в acceptance gate.

## Когда применять расширения

- При оценке текущего корпуса unified_methodology — да, по умолчанию.
- При проектировании следующей версии canonical AST — пересмотреть:
  - либо **дополнить строгий валидатор** этими kinds/полем (синхронизировать
    drafter и validator под единое расширенное определение)
  - либо **обновить эмиттер драфтера** до строгого подмножества
    (расширить `enum_members` в множество entity-деклараций; завернуть
    `gte`/`lt`/etc. в `call` к prelude-функциям)

Текущий файл фиксирует промежуточное состояние совместимости.
