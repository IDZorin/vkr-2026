"""extended_grounding_check_v1.py

Расширенная проверка grounding'а sorts/symbols относительно НЕ только
strict-источников (Prelude + source + advisory), но и corpus-level
canonical overlay.

Strict-метрика `ungrounded_sort_count` / `ungrounded_symbol_count` /
`ungrounded_ref_count` срабатывает на любой локально-объявленный символ,
не встречающийся в source.md или Prelude. По `merge_alignment_policy_v1`
overlay-слой (L1 exact / L2 ontology) — валидный источник grounding'а.

Этот модуль:
  1. парсит a4v3 entry → declared sorts/symbols
  2. строит набор grounding sources:
     - prelude (minimal_prelude_v1.json)
     - corpus canonical overlay (canonical_symbol_overlay_v3)
     - source.md content tokens
  3. для каждого declared item: grounded или нет
  4. возвращает extended counts

Не редактирует strict-метрики в `main_ir_metrics_v1.json` —
только поверх для diagnostic_summary.
"""
from __future__ import annotations
import json, pathlib, re
import yaml

ROOT = pathlib.Path(__file__).resolve().parents[2]
PRELUDE_PATH = ROOT / "IR/index/minimal_prelude_v1.json"
DOMAIN_PRELUDE_DIR = ROOT / "IR/index"
OVERLAY_PATH = ROOT / "IR/outputs/runs/unified_methodology_v1/02_alignment_and_canonicalization/definitions/canonical_symbol_overlay_v3.json"
GENERIC_PRIMITIVES_PATH = ROOT / "IR/rules/lexicons/generic_primitive_tokens.yaml"

# Regex'ы для парсинга a4v3
_SORT_RE = re.compile(r"^\s*sort\s+([A-Za-z_][A-Za-z0-9_]*)")
_ENTITY_RE = re.compile(r"^\s*entity\s+([A-Za-z_][A-Za-z0-9_]*)")
# fun/rel: имя символа после ключевого слова
_FUN_RE = re.compile(r"^\s*fun(?:\[[^\]]+\])?\s+([A-Za-z_][A-Za-z0-9_]*)")
_REL_RE = re.compile(r"^\s*rel\s+([A-Za-z_][A-Za-z0-9_]*)")
# First-class a4v3 families (per `thoughts/IR_schema/a4v3_full_48.md`)
_OBLIGATION_RE = re.compile(r"^\s*obligation\s+([A-Za-z_][A-Za-z0-9_]*)")
_PERMISSION_RE = re.compile(r"^\s*permission\s+([A-Za-z_][A-Za-z0-9_]*)")
_PROHIBITION_RE = re.compile(r"^\s*prohibition\s+([A-Za-z_][A-Za-z0-9_]*)")
_PROP_RE = re.compile(r"^\s*prop\s+([A-Za-z_][A-Za-z0-9_]*)")
_FAIRNESS_RE = re.compile(r"^\s*fairness\s+([A-Za-z_][A-Za-z0-9_]*)")
_ACTION_RE = re.compile(r"^\s*action\s+([A-Za-z_][A-Za-z0-9_]*)")
_THEOREM_RE = re.compile(r"^\s*theorem\s+([A-Za-z_][A-Za-z0-9_]*)")
_PATH_RE = re.compile(r"^\s*path\s+([A-Za-z_][A-Za-z0-9_]*)")
_VAL_RE = re.compile(r"^\s*val\s+([A-Za-z_][A-Za-z0-9_]*)")
_EVENT_RE = re.compile(r"^\s*event\s+([A-Za-z_][A-Za-z0-9_]*)")
_VAR_RE = re.compile(r"^\s*var\s+([A-Za-z_][A-Za-z0-9_]*)")

# Keywords that should NOT be flagged as ungrounded refs/callees when they
# appear inside expressions. Sourced from the canonical a4v3 spec via
# `a4v3_grammar.expression_keywords()` (operators/binders/field names).
def _load_a4v3_keywords() -> set[str]:
    from a4v3_grammar import expression_keywords  # noqa: E402
    return set(expression_keywords())


_A4V3_KEYWORDS: set[str] = _load_a4v3_keywords()


def _stem(token: str) -> str:
    """Простой rule-based stemmer (без библиотек).

    Отрезает регулярные английские суффиксы для кросс-формовой сверки:
      `representation` → `represent`
      `securities`    → `security`     (-ies → -y)
      `participants`  → `participant`
      `holders`       → `holder`
      `classified`    → `classifi` ↔ `classification` тоже → `classifi`
      `running`       → `running`     (короткое -ing не трогаем по консервативности)
    Цель — поднять recall матчинга, не идеальная точность.
    """
    t = token.lower()
    if len(t) <= 4:
        return t
    # most specific first
    for suf, repl in (
        ("ization", "ize"),
        ("isation", "ise"),
        ("ational", "ate"),
        ("ication", "ifi"),  # classification → classifi
        ("ation",   "ate"),
        ("ities",   "ity"),  # entities → entity
        ("ied",     "y"),    # carried → carry
        ("ies",     "y"),    # securities → security
        ("ing",     ""),     # running → runn (rough but OK for recall)
        ("ed",      ""),     # represented → represent
        ("ers",     "er"),
        ("ors",     "or"),
        ("es",      ""),     # holders is -ers; addresses -es
        ("s",       ""),     # holders → holder
    ):
        if t.endswith(suf) and len(t) - len(suf) >= 3:
            return t[: -len(suf)] + repl
    return t


def _content_tokens(text: str) -> set[str]:
    """Lowercased + stemmed word tokens from text.

    Возвращаем И raw lowercased форму, И stem — чтобы матч работал в обе
    стороны (`security` matched both ways).
    """
    raw = {t.lower() for t in re.findall(r"[A-Za-z][A-Za-z_0-9]*", text)}
    stems = {_stem(t) for t in raw}
    return raw | stems


def _normalize_name(name: str) -> set[str]:
    """Normalize an identifier for token-level matching.

    `FinancialIndex` → {`financialindex`, `financial`, `index`} + stems
    `trading_price` → {`trading_price`, `trading`, `price`} + stems
    """
    pieces: set[str] = {name.lower()}
    # camelCase split
    parts = re.findall(r"[A-Z][a-z]*|[a-z]+|[0-9]+", name)
    pieces.update(p.lower() for p in parts if p)
    # snake_case split
    pieces.update(p.lower() for p in name.split("_") if p)
    # stems
    pieces.update(_stem(p) for p in list(pieces))
    return pieces


_PRELUDE_CACHE: dict | None = None
_DOMAIN_PRELUDES_CACHE: list[dict] | None = None
_OVERLAY_CACHE: dict | None = None
_GENERIC_PRIMITIVES_CACHE: set[str] | None = None


def _load_prelude() -> dict:
    global _PRELUDE_CACHE
    if _PRELUDE_CACHE is None:
        _PRELUDE_CACHE = json.loads(PRELUDE_PATH.read_text(encoding="utf-8"))
    return _PRELUDE_CACHE


def _load_domain_preludes() -> list[dict]:
    global _DOMAIN_PRELUDES_CACHE
    if _DOMAIN_PRELUDES_CACHE is None:
        out: list[dict] = []
        for path in sorted(DOMAIN_PRELUDE_DIR.glob("domain_prelude_*_v*.json")):
            try:
                out.append(json.loads(path.read_text(encoding="utf-8")))
            except Exception:
                continue
        _DOMAIN_PRELUDES_CACHE = out
    return _DOMAIN_PRELUDES_CACHE


def _load_overlay() -> dict:
    global _OVERLAY_CACHE
    if _OVERLAY_CACHE is None:
        _OVERLAY_CACHE = json.loads(OVERLAY_PATH.read_text(encoding="utf-8"))
    return _OVERLAY_CACHE


def _load_generic_primitives() -> set[str]:
    global _GENERIC_PRIMITIVES_CACHE
    if _GENERIC_PRIMITIVES_CACHE is None:
        try:
            data = yaml.safe_load(GENERIC_PRIMITIVES_PATH.read_text(encoding="utf-8"))
            _GENERIC_PRIMITIVES_CACHE = set(data.get("primitives", []) or [])
        except Exception:
            _GENERIC_PRIMITIVES_CACHE = set()
    return _GENERIC_PRIMITIVES_CACHE


def _provenance_vocabulary_names(provenance_text: str = "") -> set[str]:
    """Identifiers explicitly documented in provenance vocabulary_notes.

    methodology provenance is the human-readable ledger for section-local vocabulary
    choices. If an otherwise compact A4V3 name is listed there, extended
    grounding may treat it as intentionally source-grounded. Provenance lint
    separately guards against leaking these identifiers into back-translations.
    """
    if not provenance_text.strip():
        return set()
    try:
        data = yaml.safe_load(provenance_text) or {}
    except Exception:
        return set()
    notes = data.get("vocabulary_notes") if isinstance(data, dict) else {}
    if not isinstance(notes, dict):
        return set()
    return {str(k) for k in notes.keys() if str(k).strip()}


def build_grounding_sources(
    source_text: str = "",
    normalized_text: str = "",
    provenance_text: str = "",
) -> dict:
    """Собирает все валидные источники grounding'а в один набор."""
    pre = _load_prelude()
    domain_preludes = _load_domain_preludes()
    overlay = _load_overlay()
    generic_primitives = _load_generic_primitives()

    prelude_sort_names = {s["name"] for s in pre.get("sorts", [])}
    prelude_entity_names = {e["name"] for e in pre.get("entities", [])}
    prelude_func_names = {f["name"] for f in pre.get("functions", [])}
    prelude_rel_names = {r["name"] for r in pre.get("relations", [])}

    domain_sort_names = {
        s["name"]
        for dp in domain_preludes
        for s in dp.get("sorts", []) or []
        if isinstance(s, dict) and s.get("name")
    }
    domain_entity_names = {
        e["name"]
        for dp in domain_preludes
        for e in dp.get("entities", []) or []
        if isinstance(e, dict) and e.get("name")
    }
    domain_func_names = {
        f["name"]
        for dp in domain_preludes
        for f in dp.get("functions", []) or []
        if isinstance(f, dict) and f.get("name")
    }
    domain_rel_names = {
        r["name"]
        for dp in domain_preludes
        for r in dp.get("relations", []) or []
        if isinstance(r, dict) and r.get("name")
    }

    overlay_canonical_sorts: set[str] = set()
    overlay_canonical_symbols: set[str] = set()
    for it in overlay.get("exact_overlay", []) or []:
        if not isinstance(it, dict):
            continue
        label = it.get("canonical_label", "")
        # mappings tells us per-entry kind (sort vs symbol)
        mappings = it.get("mappings", []) or []
        kinds = {m.get("kind") for m in mappings if isinstance(m, dict)}
        if "sort" in kinds:
            overlay_canonical_sorts.add(label)
        if {"fun", "rel", "symbol"} & kinds:
            overlay_canonical_symbols.add(label)
    for it in overlay.get("ontology_overlay", []) or []:
        if not isinstance(it, dict):
            continue
        lab = it.get("canonical_label") or it.get("name")
        if not lab:
            continue
        # decide bucket by mappings.kind, fallback symbols
        mappings = it.get("mappings", []) or []
        kinds = {m.get("kind") for m in mappings if isinstance(m, dict)}
        if "sort" in kinds:
            overlay_canonical_sorts.add(lab)
        else:
            overlay_canonical_symbols.add(lab)

    src_tokens = _content_tokens(source_text + " " + normalized_text)
    provenance_vocabulary_names = _provenance_vocabulary_names(provenance_text)

    return {
        "prelude_sort_names": prelude_sort_names,
        "prelude_entity_names": prelude_entity_names,
        "prelude_func_names": prelude_func_names,
        "prelude_rel_names": prelude_rel_names,
        "domain_sort_names": domain_sort_names,
        "domain_entity_names": domain_entity_names,
        "domain_func_names": domain_func_names,
        "domain_rel_names": domain_rel_names,
        "overlay_canonical_sorts": overlay_canonical_sorts,
        "overlay_canonical_symbols": overlay_canonical_symbols,
        "source_tokens": src_tokens,
        "generic_primitives": generic_primitives,
        "provenance_vocabulary_names": provenance_vocabulary_names,
    }


def is_name_grounded_extended(name: str, kind: str, sources: dict) -> tuple[bool, str]:
    """Returns (is_grounded, reason).

    kind: 'sort' | 'entity' | 'symbol' (fun/rel)
    """
    if kind == "sort":
        if name in sources["prelude_sort_names"]:
            return True, "prelude"
        if name in sources["domain_sort_names"]:
            return True, "domain_prelude"
        if name in sources["overlay_canonical_sorts"]:
            return True, "corpus_canonical_overlay"
    elif kind == "entity":
        if name in sources["prelude_entity_names"]:
            return True, "prelude"
        if name in sources["domain_entity_names"]:
            return True, "domain_prelude"
    elif kind == "symbol":
        if name in sources["prelude_func_names"] or name in sources["prelude_rel_names"]:
            return True, "prelude"
        if name in sources["domain_func_names"] or name in sources["domain_rel_names"]:
            return True, "domain_prelude"
        if name in sources["overlay_canonical_symbols"]:
            return True, "corpus_canonical_overlay"
        # Generic primitives (`ratio`, `count`, `value`, ...) — internal allowlist,
        # see `IR/rules/lexicons/generic_primitive_tokens.yaml`. Never shown to LLM.
        if name.lower() in sources["generic_primitives"]:
            return True, "generic_primitive"

    if name in sources.get("provenance_vocabulary_names", set()):
        return True, "provenance_vocabulary_notes"

    # Source-text grounding.
    # Любой content piece имени, найденный в source/normalized тексте,
    # считаем достаточным основанием — это копирует логику strict-метрики.
    # Атомарность user'овской заботы про `day_before` решается тем, что
    # prelude exact-match ВЫШЕ ловит `day_before` целиком, не доходя сюда.
    pieces = _normalize_name(name)
    matched = pieces & sources["source_tokens"]
    if matched:
        return True, f"source_text:{','.join(sorted(matched))[:60]}"

    return False, "ungrounded"


def parse_a4v3_declarations(text: str) -> dict:
    """Парсит a4v3 текст, возвращает declared sorts/entities/symbols.

    Распознаёт все 12 INNF families per `thoughts/IR_schema/a4v3_full_48.md`:
    sort/entity/fun/rel/val/event/var (Type+Symbol), obligation/permission/
    prohibition (Deontic), prop/fairness (Temporal), action (Action),
    theorem (Theorem), path (Path).

    Имена из всех families попадают в `declared_names` для grounding'а.
    """
    sorts: list[str] = []
    entities: list[str] = []
    fns: list[str] = []
    rels: list[str] = []
    deontic: list[str] = []
    temporal: list[str] = []
    actions: list[str] = []
    theorems: list[str] = []
    paths: list[str] = []
    vals: list[str] = []
    events: list[str] = []
    vars_: list[str] = []
    for line in text.splitlines():
        line = line.split("--", 1)[0]
        if line.lstrip().startswith("#"):
            continue
        if m := _SORT_RE.match(line):
            sorts.append(m.group(1))
        elif m := _ENTITY_RE.match(line):
            entities.append(m.group(1))
        elif m := _FUN_RE.match(line):
            fns.append(m.group(1))
        elif m := _REL_RE.match(line):
            rels.append(m.group(1))
        elif m := _OBLIGATION_RE.match(line):
            deontic.append(m.group(1))
        elif m := _PERMISSION_RE.match(line):
            deontic.append(m.group(1))
        elif m := _PROHIBITION_RE.match(line):
            deontic.append(m.group(1))
        elif m := _PROP_RE.match(line):
            temporal.append(m.group(1))
        elif m := _FAIRNESS_RE.match(line):
            temporal.append(m.group(1))
        elif m := _ACTION_RE.match(line):
            actions.append(m.group(1))
        elif m := _THEOREM_RE.match(line):
            theorems.append(m.group(1))
        elif m := _PATH_RE.match(line):
            paths.append(m.group(1))
        elif m := _VAL_RE.match(line):
            vals.append(m.group(1))
        elif m := _EVENT_RE.match(line):
            events.append(m.group(1))
        elif m := _VAR_RE.match(line):
            vars_.append(m.group(1))
    return {
        "sorts": sorts,
        "entities": entities,
        "functions": fns,
        "relations": rels,
        "deontic": deontic,
        "temporal": temporal,
        "actions": actions,
        "theorems": theorems,
        "paths": paths,
        "vals": vals,
        "events": events,
        "vars": vars_,
    }


def collect_refs_and_callees(ir_ast: dict) -> tuple[list[str], list[str]]:
    """Walk artifact ir_ast и собирает все ref-имена и callee-имена.

    `{kind: "ref", name: X}` → ref name X
    `{kind: "call", callee: Y, args: [...]}` → callee Y
    Quantifier var bindings (`forall x: Sort`) учтены через _walk(bound).
    """
    refs: list[str] = []
    callees: list[str] = []
    bound_stack: list[set[str]] = [set()]

    def _walk(node):
        if isinstance(node, dict):
            kind = node.get("kind")
            if kind == "ref":
                name = node.get("name", "")
                # пропускаем bound vars из текущего scope
                # пропускаем numeric strings: drafter иногда кодирует литералы
                # типа `{kind: "ref", name: "1000.0"}` вместо `{kind: "literal"}`.
                # Такие — не ungrounded, а просто плохо закодированные литералы.
                if name and not any(name in s for s in bound_stack):
                    s = str(name).strip()
                    is_numeric = bool(re.match(r"^-?\d+(\.\d+)?$", s))
                    if not is_numeric:
                        refs.append(name)
                return
            if kind == "call":
                callee = node.get("callee", "")
                if callee:
                    callees.append(callee)
                for arg in node.get("args", []) or []:
                    _walk(arg)
                return
            if kind in ("forall", "exists"):
                # bind vars
                new_scope = set(bound_stack[-1])
                for v in node.get("vars", []) or []:
                    if isinstance(v, dict) and v.get("name"):
                        new_scope.add(v["name"])
                bound_stack.append(new_scope)
                _walk(node.get("body"))
                bound_stack.pop()
                return
            if kind == "let":
                new_scope = set(bound_stack[-1])
                for b in node.get("bindings", []) or []:
                    if isinstance(b, dict):
                        if b.get("name"):
                            new_scope.add(b["name"])
                        _walk(b.get("value"))
                bound_stack.append(new_scope)
                _walk(node.get("body"))
                bound_stack.pop()
                return
            if kind == "set_comp" or kind == "count":
                binder = node.get("binder")
                new_scope = set(bound_stack[-1])
                if isinstance(binder, dict) and binder.get("name"):
                    new_scope.add(binder["name"])
                bound_stack.append(new_scope)
                _walk(node.get("predicate"))
                bound_stack.pop()
                return
            # generic recurse
            for v in node.values():
                _walk(v)
        elif isinstance(node, list):
            for v in node:
                _walk(v)

    for assertion in ir_ast.get("assertions", []) or []:
        if isinstance(assertion, dict):
            _walk(assertion.get("expr"))
    return refs, callees


def check_ungrounded_refs(artifact: dict, sources: dict, declared_names: set[str]) -> dict:
    """Returns {ungrounded_refs: [...], ungrounded_callees: [...]} after
    walking the artifact's ir_ast and resolving each ref/callee against
    grounding sources + locally-declared names.
    """
    ir_stage = artifact.get("ir_stage") or {}
    drafter = ir_stage.get("drafter") or {}
    result = drafter.get("result") or {}
    ir_ast = result.get("ir_ast") or {}
    if not isinstance(ir_ast, dict):
        return {"ungrounded_refs": [], "ungrounded_callees": []}

    refs, callees = collect_refs_and_callees(ir_ast)

    # Allowed names = locally declared + prelude sorts/entities/funcs/rels +
    # overlay canonicals + generic primitives.
    allowed = set(declared_names)
    allowed |= sources["prelude_sort_names"]
    allowed |= sources["prelude_entity_names"]
    allowed |= sources["prelude_func_names"]
    allowed |= sources["prelude_rel_names"]
    allowed |= sources["domain_sort_names"]
    allowed |= sources["domain_entity_names"]
    allowed |= sources["domain_func_names"]
    allowed |= sources["domain_rel_names"]
    allowed |= sources["overlay_canonical_sorts"]
    allowed |= sources["overlay_canonical_symbols"]
    allowed |= sources.get("provenance_vocabulary_names", set())
    allowed_lower = {a.lower() for a in allowed}
    allowed_lower |= sources["generic_primitives"]

    src_tokens = sources["source_tokens"]

    def is_grounded(n: str) -> bool:
        if n in allowed:
            return True
        if n.lower() in allowed_lower:
            return True
        if re.fullmatch(r"\d+(?:\.\d+)?%", n):
            return True
        # piece/source-text fallback
        pieces = _normalize_name(n)
        if pieces & src_tokens:
            return True
        return False

    ungrounded_refs = sorted({r for r in refs if not is_grounded(r)})
    ungrounded_callees = sorted({c for c in callees if not is_grounded(c)})
    return {"ungrounded_refs": ungrounded_refs, "ungrounded_callees": ungrounded_callees}


def check_entry(entry_dir: pathlib.Path) -> dict:
    a4v3 = entry_dir / "main_ir.a4v3"
    if not a4v3.exists():
        return {"entry": entry_dir.name, "status": "no_a4v3"}
    text = a4v3.read_text(encoding="utf-8")
    declared = parse_a4v3_declarations(text)

    src = entry_dir / "source.md"
    norm = entry_dir / "normalized.md"
    prov = entry_dir / "provenance.yaml"
    sources = build_grounding_sources(
        source_text=src.read_text(encoding="utf-8") if src.exists() else "",
        normalized_text=norm.read_text(encoding="utf-8") if norm.exists() else "",
        provenance_text=prov.read_text(encoding="utf-8") if prov.exists() else "",
    )

    ungrounded = {"sorts": [], "entities": [], "symbols": [],
                  "deontic": [], "temporal": [], "actions": []}
    grounded_via_overlay = {"sorts": [], "symbols": []}
    for s in declared["sorts"]:
        ok, reason = is_name_grounded_extended(s, "sort", sources)
        if not ok:
            ungrounded["sorts"].append(s)
        elif reason == "corpus_canonical_overlay":
            grounded_via_overlay["sorts"].append(s)
    for e in declared["entities"]:
        ok, _ = is_name_grounded_extended(e, "entity", sources)
        if not ok:
            ungrounded["entities"].append(e)
    for sym in declared["functions"] + declared["relations"] + declared.get("vals", []):
        ok, reason = is_name_grounded_extended(sym, "symbol", sources)
        if not ok:
            ungrounded["symbols"].append(sym)
        elif reason == "corpus_canonical_overlay":
            grounded_via_overlay["symbols"].append(sym)
    # First-class family declarations: grounded if name-pieces appear in source.
    # Strict prelude/overlay match unlikely (these are local norms / temporal
    # props), source-text match is the primary signal.
    for d in declared.get("deontic", []):
        ok, _ = is_name_grounded_extended(d, "symbol", sources)
        if not ok:
            ungrounded["deontic"].append(d)
    for t in declared.get("temporal", []):
        ok, _ = is_name_grounded_extended(t, "symbol", sources)
        if not ok:
            ungrounded["temporal"].append(t)
    for a in declared.get("actions", []):
        ok, _ = is_name_grounded_extended(a, "symbol", sources)
        if not ok:
            ungrounded["actions"].append(a)

    # Walk artifact ir_ast to find ungrounded refs / callees.
    artifacts = list(entry_dir.glob("*_manual_section_workspace_artifact_current_v1.json")) \
              + list(entry_dir.glob("*_manual_ir_workspace_artifact_current_v1.json"))
    ungrounded_refs: list[str] = []
    ungrounded_callees: list[str] = []
    if artifacts:
        try:
            art = json.loads(artifacts[0].read_text(encoding="utf-8"))
            declared_names = (
                set(declared["sorts"])
                | set(declared["entities"])
                | set(declared["functions"])
                | set(declared["relations"])
                | set(declared.get("deontic", []))
                | set(declared.get("temporal", []))
                | set(declared.get("actions", []))
                | set(declared.get("vals", []))
                | set(declared.get("events", []))
                | set(declared.get("vars", []))
                | set(declared.get("paths", []))
                | set(declared.get("theorems", []))
                | _A4V3_KEYWORDS
            )
            ref_check = check_ungrounded_refs(art, sources, declared_names)
            ungrounded_refs = ref_check["ungrounded_refs"]
            ungrounded_callees = ref_check["ungrounded_callees"]
        except Exception:
            pass

    return {
        "entry": entry_dir.name,
        "ungrounded_sort_count_extended": len(ungrounded["sorts"]),
        "ungrounded_symbol_count_extended": len(ungrounded["symbols"]),
        "ungrounded_entity_count_extended": len(ungrounded["entities"]),
        "ungrounded_ref_count_extended": len(ungrounded_refs),
        "ungrounded_callee_count_extended": len(ungrounded_callees),
        "ungrounded": ungrounded,
        "ungrounded_refs": ungrounded_refs,
        "ungrounded_callees": ungrounded_callees,
        "grounded_via_overlay": grounded_via_overlay,
    }


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        for p in sys.argv[1:]:
            r = check_entry(pathlib.Path(p))
            print(f"=== {r['entry']} ===")
            print(f"  ungrounded sorts:    {r['ungrounded']['sorts']}")
            print(f"  ungrounded symbols:  {r['ungrounded']['symbols']}")
            print(f"  grounded via overlay: sorts={r['grounded_via_overlay']['sorts']}, "
                  f"symbols={r['grounded_via_overlay']['symbols'][:8]}")
