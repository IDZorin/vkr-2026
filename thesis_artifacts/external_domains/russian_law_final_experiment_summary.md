# Russian Law (Русская правда): SMT Experiments — Final Summary

**Дата:** 2026-05-20

**Цель:** проверить применимость SMT-проверки на богатом нормативном
корпусе (средневековый правовой текст «Русская правда», 18 статей),
после успеха proof-of-concept на правилах шашек-64.

---

## 1. Корпус и IR

| | Значение |
|---|---|
| Источник | Русская правда, 18 артикулов о убийстве, ранениях, краже, долговых отношениях |
| Source size | 87 строк прозы |
| IR size | 1026 строк A4V3 (готов из предыдущего эксперимента) |
| Декларации | 335 (146 rel + 80 subtypes + 10 opaque + 6 enum + 93 fact-constraints) |
| Parser strict | 0 warnings ✓ |
| SmtCompiler base | 545 строк SMT-LIB, 0 unsupported после post-process |

Существенно богаче чем draughts (67 fact, 16 sorts) — 80 subtypes только
для иерархии субъектов права (Chelovek → Muzh / Rusin / Gridin / Kupets
/ Yabednik / Mechnik / Izgoy / Slovenin) плюс категории дел и вещей.

---

## 2. Эксперименты

Запущены 9 SMT-запросов через настоящий `SmtCompiler` (тот же что для
draughts) в трёх блоках:

| Блок | Запросы | Цель |
|---|---|---|
| **E1** Penalty lookup | 5 | Вывести штраф из условий ("если отсёк палец — 3 гривны") |
| **E2** Applicability | 3 | Подтвердить (не)применимость правила в позиции |
| **E3** Consistency | 1 | База — без противоречий (`(check-sat)` без extras) |

---

## 3. Результаты

### 3.1 Сначала через full `SmtCompiler` — провал

| Блок | Resolved | Timeouts |
|---|---|---|
| E1 (5) | 0 | 5 |
| E2 (3) | 0 | 3 |
| E3 (1) | 0 | **1** ← база сама timeout |
| **Итого** | **0** | **9** |

Все 9 запросов timeout за 120 секунд. Z3 не справляется с quantifier
instantiation на 93 constraint × forall × 80 subtypes.

### 3.2 Переключение на `BoundedWitnessSmtCompiler` — успех

| Блок | Resolved | Timeouts |
|---|---|---|
| E1 (5) | **5/5** | 0 |
| E2 (3) | **3/3** | 0 |
| E3 (1) | **1/1** | 0 |
| **Итого** | **9/9** | **0** |

`BoundedWitnessSmtCompiler` (уже существует в `smt_probe_runner_v1.py`)
инстанциирует `forall x : T . body` фиксированным witness constant
`W_x_T` — получается ground SMT-LIB без открытых квантификаторов.
Z3 решает за миллисекунды.

**Это именно та техника, что применяется в dz-корпусе.** Изначальный
выбор full SmtCompiler был ошибкой инструмента.

---

## 4. Природа провала — quantifier instantiation

Это **усугублённая версия** ограничения, обнаруженного на draughts
(см. `IR/docs/draughts_smt_bridge_design.md` §9.3):

- 93 constraint-а × forall-кванторы каждое
- 80 subtypes × predicate-based encoding в SMT
- Множество opaque sorts (Chelovek, Plata, Svideteley, Vorov…)

При попытке решить даже простой `(check-sat)` Z3 должен инстанциировать
каждый универсальный constraint для всех возможных значений переменных
во всех связанных subtypes/opaque доменах. Пространство поиска
**взрывается экспоненциально**.

Дополнительные стартовые барьеры:
- IR использует opaque sorts (`Plata`, `Svideteley`, `Dney`, `Vorov`,
  `Kolichestvo`, `Dosok`) для квантитативных понятий, тогда как
  constraints передают Int-литералы. Без post-process замены этих
  sorts на Int Z3 даже не компилирует base.
- Subtypes encoded as predicates over root sort — каждое
  `(Muzh x)`, `(Chelovek x)` требует Z3 проверить inheritance chain.

---

## 5. Что это даёт ВКР

**Сильное усиливающее подтверждение** того ограничения, которое было
впервые сформулировано на draughts:

| Корпус | base consistency check |
|---|---|
| Draughts (67 fact) | sat за <1 секунды |
| Russian Law (93 constraint + 80 subtypes) | **timeout 120s** |

Зависимость **прямая**: чем богаче нормативный текст (больше rules,
больше типов субъектов), тем быстрее упирается общий SMT-решатель.

Это **архитектурный фундаментальный предел** общих SMT-решателей для
quantifier-heavy normative texts — **не баг pipeline, не баг A4V3, не
баг Z3**. Это известное свойство first-order logic with quantifiers
(полу-разрешимость в общем случае).

---

## 6. Future work — те же 4 направления что для draughts

Из `IR/docs/draughts_smt_bridge_design.md` §9.5:

1. **Ground-instantiation pre-pass.** Под конкретную ситуацию ("X отсёк
   палец Y") подставить значения existential vars до отправки в Z3.
   Получим пропозициональную задачу — гарантированно завершается.
2. **Pattern hints в IR-фактах.** Авторские триггеры для E-matching.
3. **Stratified theories.** Сначала type-инстанциация (`Muzh x` →
   `Chelovek x` → `SubjektPrava x`), потом legality.
4. **Доменно-специфичный решатель.** Для юриспруденции — позиционный
   case-checker, либо инструменты типа Catala / Formality.

Для **production** применения A4V3 IR на legal corpora **необходим**
один из этих подходов. Generic SMT solver работает только на узких
fragments (например EPR — effectively propositional reasoning).

---

## 7. Что доказано

| Свойство | Подтверждено |
|---|---|
| Pipeline NL → A4V3 → SMT компилирует богатый legal IR в SMT-LIB | ✓ |
| 0 unsupported assertions после post-process opaque sorts → Int | ✓ |
| Архитектура pipeline domain-agnostic (тот же compiler, что draughts) | ✓ |
| Generic Z3 справляется с базой Russian Law | **✗** (timeout) |
| Generic Z3 справляется с derived-instance scenarios | **✗** (timeout) |
| Граница применимости SMT для quantifier-heavy normative IR | **зафиксирована** |

---

## 7.ter Полный NL→SMT pipeline с query-driven instantiator (ФИНАЛ)

После итерации по 7.bis реализован **query-driven rule instantiator**
(`scripts/query_driven_instantiator.py`, ~150 строк). Идея:
- LLM производит SMT-LIB фрагменты с пользовательскими константами
  (`d`, `x`, `y`, `boroda`).
- Driver проходит по каждому `forall`-constraint в IR и подставляет
  user-константы в позиции forall-переменных, генерируя
  ground-инстанциации.
- Только эти ground-инстанциации добавляются к bounded base — Z3
  получает пропозициональную задачу.

### Результаты с query-driven instantiator

| Класс | N | Резолвлено | Verdict совпадает с ожиданием |
|---|---|---|---|
| Questions ("какой штраф за X?") | 5 | **5/5** | CONSISTENT_WITH_LAW ✓ |
| Adversarial denials ("не накажут за X") | 4 | **4/4** | **CONTRADICTED_BY_LAW ✓** |
| Out-of-scope refusals | 2 | **2/2** | NOT_COVERED ✓ |
| **Итого** | **11** | **11/11** | **100%** |

### Технические параметры финального прогона

| | |
|---|---|
| LLM (перевод NL → SMT) | deepseek-v4-flash, temp=0, max_tokens=8000 |
| Compile-time IR → bounded SMT-LIB | ~1.2 секунды |
| Query-driven instantiations на запрос | ~80–200 ground assertions |
| Z3 wall time per query | <100 миллисекунд (max наблюдалось ~2 сек) |
| Z3 timeout limit | 60 секунд (не достигался) |
| Полный wall pipeline per query | ~3–4 сек (доминирует LLM call) |

### Что доказано

| Свойство | Подтверждено |
|---|---|
| LLM-перевод NL→SMT работает на legal-corpus | ✓ (11/11 valid JSON) |
| Все цитированные IR-имена существуют в IR | ✓ (validator pass) |
| Pipeline формально подтверждает согласие с законом | ✓ (Q1–Q5) |
| Pipeline формально доказывает противоречие с законом | ✓ (A1–A4) |
| Pipeline корректно отказывается на out-of-scope | ✓ (OOS1–OOS2) |
| Архитектура domain-agnostic | ✓ (тот же compiler + instantiator что для draughts) |

---

## 7.bis Промежуточный шаг (диагностика проблемы)

После hardcoded SMT-тестов (9/9 OK) дополнительно прогнан full pipeline
с LLM-переводом естественно-языковых запросов в SMT-LIB. Скрипт
`scripts/russian_law_nl_query.py`, 11 inputs:

| Класс | Кол-во | Результат |
|---|---|---|
| Questions ("какой штраф за X?") | 5 | **5/5 CONSISTENT_WITH_LAW** ✓ |
| Adversarial denials ("вырвать бороду — не накажут") | 4 | **0/4 NOT_FORCED_CONTRADICTION** ✗ |
| Out-of-scope ("курс гривны, мода") | 2 | **2/2 NOT_COVERED** ✓ |

LLM-перевод работает (11/11 valid JSON, цитаты корректные). SMT
разрешает positive consistency-queries. Но **adversarial detection
противоречий не сработал**: `BoundedWitnessSmtCompiler` инстанциирует
универсалы (`forall p : ChastCheloveka`) единым witness constant, и
Z3 свободно выбирает его ≠ `boroda` — правило rp_008 vacuously
satisfied, противоречие не возникает.

### Архитектурная развилка

| Compiler | Consistency-queries | Contradiction-detection |
|---|---|---|
| Full `SmtCompiler` | timeout на 545 lines × 93 constraints | работал бы (если бы не timeout) |
| `BoundedWitnessSmtCompiler` | ✓ работает | ✗ теряет universality |
| **Query-driven instantiation** (future work) | ✓ | ✓ |

Третий путь — **переписать `forall x : T . body` под user-specific
переменные из запроса** до отправки в Z3. Это превращает рулы в
ground impликации, применимые именно к user's x_user, y_user из
вопроса. Реализация ~100-150 строк python.

## 8. Артефакты

| Файл | Назначение |
|---|---|
| `IR/outputs/runs/russian_law/main_ir.a4v3` | Полный IR Русской правды (1026 строк, 93 constraints) |
| `IR/outputs/runs/russian_law/source.md` | Источник (87 строк прозы) |
| `scripts/russian_law_smt_experiments.py` | Hardcoded SMT test driver (9 запросов, 3 блока) |
| `scripts/russian_law_nl_query.py` | **Full NL → SMT pipeline** (11 inputs через LLM + Z3) |
| `scripts/query_driven_instantiator.py` | **Query-driven rule rewriter** (переиспользуемый instantiator) |
| `<TMP_DIR>/russian_law_smt/*.smt2` | Hardcoded SMT файлы |
| `<TMP_DIR>/russian_law_nl_query/*.smt2` | NL-pipeline SMT файлы (per-input) |
| `IR/outputs/runs/russian_law/smt_experiments_results.txt` | Hardcoded run results (9/9) |
| `IR/outputs/runs/russian_law/nl_query_results_v3.txt` | **Финальные результаты NL pipeline (11/11)** |
| `IR/outputs/runs/russian_law/FINAL_EXPERIMENT_SUMMARY.md` | **Этот документ** |

---

## 8.bis Ограничения текущего эксперимента

### Что покрыто
- Domain: 18 артикулов «Русской правды» (раздел о убийстве, ранениях,
  краже, долговых отношениях).
- Типы запросов: penalty lookup, applicability check, consistency
  check, adversarial denial, out-of-scope refusal.
- 11 inputs (5 questions + 4 adversarial + 2 OOS).

### Что не покрыто (scope limitations)

1. **Многошаговые правовые рассуждения** не тестировались. Каждый
   запрос — про одно действие (вырвал бороду, ударил мечом). Цепочки
   («Иван украл коня → возмещение → рассмотрение свода → передача
   поручителю → 5 дней») не проверялись.
2. **Применимость по подтипам субъекта** проверена ограниченно. Все
   тесты используют generic `Chelovek`; не тестировались специфические
   подтипы (Муж, Русин, Гридин, Изгой, Словенин).
3. **Numeric reasoning** через `Int` aliasing: 7 опаковых sorts
   (`Plata`, `Svideteley`, `Dney`, `Vorov`, `Kolichestvo`, `Dosok`,
   `Rasstoyanie`) post-process-заменены на `Int`. Если конкретный
   constraint полагается на структурные свойства этих sorts —
   замена их Int могла бы вызвать misбehaviour. Не наблюдалось в
   тестах, но возможный риск.
4. **Open-world семантика relations**. Например, `(shtraf d x grivna 3)`
   и `(shtraf d x grivna 100)` могут оба быть истинными в SMT
   (отношение не функциональное). Тесты «штраф = 3, не 100»
   возвращают sat (множественные значения возможны), что
   корректно по моделированию, но может удивить интуицию юриста.
5. **Performance scaling не тестировался**. 198 ground assertions для
   одного запроса — Z3 решает за миллисекунды. На корпусе в 1000+
   constraint-ов и при широком наборе user-констант комбинаторика
   instantiations может вырасти существенно. Не известно где лежит
   граница масштабируемости.
6. **Качество LLM-перевода не валидировано формально**. 11/11 valid
   JSON и all-cited names existed in IR — но семантическая корректность
   перевода («LLM правильно понял что означает "не накажут"»)
   проверялась только косвенно через Z3-verdict-совпадение.
7. **Один LLM** (deepseek-v4-flash). Cross-LLM согласие (например с
   gpt-4o-mini, claude-haiku) не измерялось.
8. **Один Z3 solver**. Альтернативные decisional procedures (CVC5,
   MathSAT) не тестировались.

### Архитектурные ограничения pipeline

1. **Bounded witness теряет универсальность** (см. 7.bis). Решено
   через query-driven instantiator, но это **per-query rewriting** —
   стоит дополнительный compile-step на каждый запрос.
2. **Instantiator не покрывает nested forall в `body`**.
   Если внутри body встречается ещё один `forall` (не как top-level
   wrapper), он не разворачивается. На текущей Русской правде это не
   проявилось, но возможный risk для более сложных IR.
3. **Type matching по имени sorta**. Например `forall x : Chelovek`
   ищет константы с predicate `(Chelovek x)`. Subtype rules
   (Муж → Chelovek → SubjektPrava) учитываются только частично —
   fallback на SubjektPrava для (Chelovek, Muzh, Rusin). Полная
   subtype-hierarchy traversal не реализована.

## 9. ВКР-ready текст

**Глава 4 (artefacts):**
> На корпусе «Русская правда» (87 строк прозы, 18 артикулов о убийстве,
> ранениях, краже, долговых отношениях) получен A4V3 IR из 1026 строк,
> содержащий 335 деклараций (146 отношений, 80 подтипов субъектов
> права, 93 constraint-факта). IR компилируется через универсальный
> SmtCompiler в 545 строк SMT-LIB без unsupported конструкций.

**Глава 5 (методология SMT):**
> Generic SMT (Z3 поверх full first-order компиляции) не справился ни
> с одним из 9 тестовых запросов за 120 секунд из-за комбинаторного
> взрыва quantifier instantiation на 93 универсальных constraint-фактов
> × 80 подтипов субъектов. **Переключение на `BoundedWitnessSmtCompiler`**
> (готовый компилятор в `smt_probe_runner_v1.py`, реализующий
> witness-based ground-instantiation `forall x : T . body` → `body[x := W_x_T]`)
> разрешило все 9 hardcoded запросов за миллисекунды, но потеряло
> universality (адверсариальные denials возвращали sat вместо
> ожидаемого unsat). **Добавление query-driven rule instantiator**
> (~150 строк python, переписывает forall-constraints с
> user-константами из запроса перед отправкой в Z3) обеспечило
> **11/11 правильных верификаций** на полном NL→SMT pipeline:
> 5/5 questions подтверждены consistent_with_law, 4/4 adversarial
> denials формально доказаны contradicted_by_law, 2/2 out-of-scope
> корректно reject-ятся LLM. Архитектурный стек **bounded base +
> query-driven instantiation** работает на legal corpus в режиме
> реального времени (<4 секунд wall-time на запрос, доминирует
> LLM-call).

**Глава 5 (limitations):**
> Эксперимент покрывает 11 inputs на одиночных правилах; цепочки
> правовых рассуждений, специфические подтипы субъектов (Муж, Русин,
> Гридин), open-world неоднозначности отношений (множественные
> значения штрафа), и cross-LLM/cross-solver согласие не валидировались.
> Type matching при instantiation работает по имени sorta с partial
> subtype-fallback; полная subtype-hierarchy traversal не реализована.
> Performance scaling за пределами Русской правды (1026 строк, 93
> constraint) не тестировался — на корпусах в 10× больше комбинаторика
> instantiation может вырасти существенно. См. полные ограничения в
> разделе 8.bis.
