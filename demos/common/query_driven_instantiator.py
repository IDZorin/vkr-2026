"""Query-driven rule instantiator for demo SMT queries.

For each A4V3 forall-rule and each combination of user-declared constants of
matching sort, this helper emits a ground SMT-LIB assertion. Combined with a
bounded-witness base, this gives fast consistency checks and useful
contradiction detection for recorded demo queries.
"""
from __future__ import annotations

import re
import sys
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "IR" / "src"))

import a4v3_parser_v1 as parser  # noqa: E402
from smt_probe_runner_v1 import SmtCompiler  # noqa: E402


def extract_user_consts(
    smt_declarations: list[str],
    smt_facts: list[str],
) -> dict[str, list[str]]:
    """Return a mapping from sort or subtype predicate to user constants."""
    consts_by_sort: dict[str, list[str]] = {}
    declared: dict[str, str] = {}

    for line in smt_declarations:
        match = re.match(r"\(declare-const\s+(\w+)\s+(\w+)\s*\)", line.strip())
        if match:
            name, sort = match.group(1), match.group(2)
            declared[name] = sort
            consts_by_sort.setdefault(sort, []).append(name)

    for fact in smt_facts:
        text = fact.strip()
        if text.startswith("(assert "):
            text = text[len("(assert ") : -1].strip()
        match = re.match(r"\(([A-Z]\w+)\s+(\w+)\)\s*$", text)
        if match:
            pred, name = match.group(1), match.group(2)
            if name in declared:
                consts_by_sort.setdefault(pred, []).append(name)

    return {sort: sorted(set(names)) for sort, names in consts_by_sort.items()}


def _substitute_refs(expr: dict, mapping: dict[str, str]):
    if not isinstance(expr, dict):
        return expr
    kind = expr.get("kind")
    if kind == "ref":
        name = expr.get("name")
        if name in mapping:
            return {"kind": "ref", "name": mapping[name]}
        return expr

    new = dict(expr)
    if kind in {"forall", "exists"}:
        bound = {v.get("name") for v in expr.get("vars", []) or []}
        inner_map = {key: value for key, value in mapping.items() if key not in bound}
        new["body"] = _substitute_refs(expr.get("body"), inner_map)
        return new

    for field in ("body", "left", "right", "arg"):
        if field in expr:
            new[field] = _substitute_refs(expr[field], mapping)
    if "args" in expr:
        new["args"] = [_substitute_refs(arg, mapping) for arg in expr["args"]]
    return new


def _build_substituted_smt(
    compiler: SmtCompiler,
    body: dict,
    mapping: dict[str, str],
    user_const_sorts: dict[str, str],
) -> str | None:
    substituted = _substitute_refs(body, mapping)
    try:
        return compiler.compile_expr(substituted, dict(user_const_sorts))
    except Exception:
        return None


def instantiate_constraints(
    ir_path: Path,
    consts_by_sort: dict[str, list[str]],
    user_const_sorts: dict[str, str] | None = None,
) -> list[str]:
    """Instantiate top-level forall constraints over user constants."""
    ast = parser.parse(ir_path.read_text(encoding="utf-8"))
    compiler = SmtCompiler(ast)
    results: list[str] = []

    consts_by_sort = dict(consts_by_sort)
    for ent_name, ent_sort in compiler.entities.items():
        consts_by_sort.setdefault(ent_sort, []).append(ent_name)
    consts_by_sort = {sort: sorted(set(names)) for sort, names in consts_by_sort.items()}

    if user_const_sorts is None:
        user_const_sorts = {}
        for sort, names in consts_by_sort.items():
            for name in names:
                user_const_sorts.setdefault(name, sort)

    def flatten_foralls(expr: dict) -> tuple[list, dict]:
        vars_: list = []
        current = expr
        while isinstance(current, dict) and current.get("kind") == "forall":
            vars_.extend(current.get("vars") or [])
            current = current.get("body")
        return vars_, current

    for assertion in ast.get("assertions", []) or []:
        expr = assertion.get("expr")
        if not expr or expr.get("kind") != "forall":
            continue
        forall_vars, body = flatten_foralls(expr)

        compatible_lists: list[list[tuple[str, str]]] = []
        for var in forall_vars:
            vsort = var.get("sort")
            vname = var.get("name")
            candidates = consts_by_sort.get(vsort, [])
            if not candidates and vsort in {"Chelovek", "Muzh", "Rusin"}:
                candidates = consts_by_sort.get("SubjektPrava", [])
            if not candidates:
                compatible_lists = []
                break
            compatible_lists.append([(vname, candidate) for candidate in candidates])

        if not compatible_lists:
            continue

        name = assertion.get("name", "unnamed")
        for combo in product(*compatible_lists):
            mapping = dict(combo)
            smt = _build_substituted_smt(compiler, body, mapping, user_const_sorts)
            if smt:
                inst_name = name + "__inst_" + "_".join(candidate for _, candidate in combo)
                results.append(f"(assert (! {smt} :named INST_{inst_name}))")

    return results


def build_query_smt(
    base_text: str,
    ir_path: Path,
    smt_declarations: list[str],
    smt_facts: list[str],
    smt_goal: str,
) -> str:
    """Combine base SMT, query-driven instantiations, user facts, and goal."""
    filtered_decls = [
        decl for decl in smt_declarations if decl.strip().startswith("(declare-const ")
    ]
    consts = extract_user_consts(filtered_decls, smt_facts)
    instantiated = instantiate_constraints(ir_path, consts)

    def ensure_asserted(text: str) -> str:
        text = text.strip()
        if text.startswith("(assert ") and text.endswith(")"):
            return text
        return f"(assert {text})"

    lines = [base_text, "; --- user declarations ---"]
    lines.extend(filtered_decls)
    lines.append("; --- query-driven instantiations ---")
    lines.extend(instantiated)
    lines.append("; --- user facts ---")
    lines.extend(ensure_asserted(fact) for fact in smt_facts)
    lines.append("; --- goal ---")
    lines.append(ensure_asserted(smt_goal))
    lines.append("(check-sat)")
    return "\n".join(lines)

