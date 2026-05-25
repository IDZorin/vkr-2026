"""smt_probe_runner_v1.py

Sidecar SMT probe/witness layer for financial methodology local IR fragments.

The runner extracts probe candidates from existing ``main_ir.a4v3`` files,
emits SMT-LIB2 files for candidates supported by the shallow v1 compiler, and
optionally runs a local ``z3`` binary when available. Local IR files are never
rewritten.

CLI:
    python IR/src/smt_probe_runner_v1.py --run-root case_studies/financial_methodology
    python IR/src/smt_probe_runner_v1.py --run-root case_studies/financial_methodology --plan-only
    python IR/src/smt_probe_runner_v1.py --run-root case_studies/financial_methodology --smt-mode hybrid
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any

THIS_DIR = Path(__file__).resolve().parent
if str(THIS_DIR) not in sys.path:
    sys.path.insert(0, str(THIS_DIR))

from a4v3_parser_v1 import parse  # noqa: E402


ENTRY_GROUPS = (
    ("sections", "section"),
    ("definitions", "definition"),
    ("appendix", "appendix"),
)

BUILTIN_SORTS = {
    "Nat": "Int",
    "Int": "Int",
    "Integer": "Int",
    "Real": "Real",
    "Decimal": "Real",
    "Number": "Real",
    "Bool": "Bool",
    "String": "String",
}

SUPPORTED_EXPR_KINDS = {
    "ref",
    "call",
    "forall",
    "exists",
    "and",
    "or",
    "not",
    "implies",
    "iff",
    "isa",
    "eq",
    "lte",
    "gte",
    "lt",
    "gt",
    "add",
    "sub",
    "mul",
    "div",
}

UNSUPPORTED_EXPR_KINDS = {"count", "set_comp", "ite"}


class UnsupportedSmt(RuntimeError):
    pass


def _smt_ident(name: str) -> str:
    if re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", name):
        return name
    return "|" + name.replace("\\", "\\\\").replace("|", "\\|") + "|"


def _is_number_ref(name: str) -> bool:
    return bool(re.fullmatch(r"\d+(?:\.\d+)?%?", name))


def _number_to_smt(name: str) -> str:
    if name.endswith("%"):
        raw = name[:-1]
        if "." in raw:
            return f"(/ {raw} 100.0)"
        return f"(/ {raw} 100)"
    return name


def _discover_entries(run_root: Path) -> list[dict[str, Any]]:
    entries: list[dict[str, Any]] = []
    for group_dir_name, entry_kind in ENTRY_GROUPS:
        group_dir = run_root / group_dir_name
        if not group_dir.exists():
            continue
        for entry_dir in sorted(group_dir.iterdir(), key=lambda p: p.name.lower()):
            if not entry_dir.is_dir() or entry_dir.name.startswith("agent_run"):
                continue
            main_ir = entry_dir / "main_ir.a4v3"
            if not main_ir.exists() or main_ir.stat().st_size == 0:
                continue
            entries.append(
                {
                    "entry_id": entry_dir.name,
                    "entry_kind": entry_kind,
                    "entry_dir": entry_dir,
                    "relative_dir": str(entry_dir.relative_to(run_root)),
                }
            )
    return entries


def _expr_to_text(expr: dict[str, Any] | None) -> str:
    if not expr:
        return ""
    kind = expr.get("kind")
    if kind == "ref":
        return expr.get("name", "")
    if kind == "call":
        args = ", ".join(_expr_to_text(arg) for arg in expr.get("args", []))
        return f"{expr.get('callee')}({args})"
    if kind in {"forall", "exists"}:
        vars_text = ", ".join(f"{v['name']}: {v['sort']}" for v in expr.get("vars", []))
        return f"{kind} {vars_text}, {_expr_to_text(expr.get('body'))}"
    if kind in {"and", "or"}:
        return f" {kind} ".join(_wrap_text_arg(arg) for arg in expr.get("args", []))
    if kind == "not":
        return f"not {_wrap_text_arg(expr.get('arg'))}"
    if kind in {"implies", "iff"}:
        return f"{_wrap_text_arg(expr.get('left'))} {kind} {_wrap_text_arg(expr.get('right'))}"
    if kind in {"eq", "lte", "gte", "lt", "gt", "add", "sub", "mul", "div"}:
        op = {
            "eq": "=",
            "lte": "<=",
            "gte": ">=",
            "lt": "<",
            "gt": ">",
            "add": "+",
            "sub": "-",
            "mul": "*",
            "div": "/",
        }[kind]
        return f"{_wrap_text_arg(expr.get('left'))} {op} {_wrap_text_arg(expr.get('right'))}"
    if kind == "isa":
        return f"{_wrap_text_arg(expr.get('expr'))} isa {expr.get('sort', '')}"
    return f"<unsupported:{kind}>"


def _wrap_text_arg(expr: dict[str, Any] | None) -> str:
    if not expr:
        return ""
    if expr.get("kind") in {"ref", "call"}:
        return _expr_to_text(expr)
    return f"({_expr_to_text(expr)})"


def _wrap_exists(vars_: list[dict[str, str]], expr: dict[str, Any]) -> dict[str, Any]:
    dedup: list[dict[str, str]] = []
    seen: set[str] = set()
    for var in vars_:
        name = var.get("name")
        if name and name not in seen:
            seen.add(name)
            dedup.append({"name": name, "sort": var.get("sort", "")})
    if not dedup:
        return expr
    return {"kind": "exists", "vars": dedup, "body": expr}


def _contains_unsupported_expr(expr: dict[str, Any] | None) -> str | None:
    if not expr:
        return "missing expression"
    kind = expr.get("kind")
    if kind in UNSUPPORTED_EXPR_KINDS:
        return f"unsupported expression kind {kind}"
    if kind not in SUPPORTED_EXPR_KINDS:
        return f"unknown expression kind {kind}"
    for key in ("body", "left", "right", "arg", "expr", "cond", "then", "else", "predicate"):
        child = expr.get(key)
        if isinstance(child, dict):
            reason = _contains_unsupported_expr(child)
            if reason:
                return reason
    for key in ("args",):
        for child in expr.get(key, []) or []:
            if isinstance(child, dict):
                reason = _contains_unsupported_expr(child)
                if reason:
                    return reason
    return None


def _probe_id(entry_id: str, assertion_name: str, probe_type: str, index: int) -> str:
    raw = f"{entry_id}__{assertion_name}__{probe_type}__{index:03d}"
    return re.sub(r"[^A-Za-z0-9_]+", "_", raw)


def _extract_probes_from_expr(
    *,
    entry_id: str,
    entry_kind: str,
    relative_dir: str,
    assertion: dict[str, Any],
) -> list[dict[str, Any]]:
    expr = assertion.get("expr")
    if not expr:
        return []
    probes: list[dict[str, Any]] = []
    counter = 0

    def add_probe(probe_type: str, candidate: dict[str, Any], scope: list[dict[str, str]], origin: str) -> None:
        nonlocal counter
        counter += 1
        probe_expr = _wrap_exists(scope, candidate)
        reason = _contains_unsupported_expr(probe_expr)
        probes.append(
            {
                "schema": "smt_probe_spec_v1",
                "probe_id": _probe_id(entry_id, assertion.get("name", "assertion"), probe_type, counter),
                "entry_id": entry_id,
                "entry_kind": entry_kind,
                "relative_dir": relative_dir,
                "assertion": assertion.get("name"),
                "assertion_kind": assertion.get("kind"),
                "assertion_line_no": assertion.get("line_no"),
                "probe_type": probe_type,
                "origin": origin,
                "outer_vars": scope,
                "candidate_expr": candidate,
                "probe_expr": probe_expr,
                "candidate_expr_text": _expr_to_text(candidate),
                "probe_expr_text": _expr_to_text(probe_expr),
                "must_be_satisfiable": False,
                "compile_status": "candidate",
                "unsupported_reason": reason,
            }
        )

    def visit(node: dict[str, Any], scope: list[dict[str, str]], origin: str) -> None:
        kind = node.get("kind")
        if kind in {"forall", "exists"}:
            next_scope = scope + [{"name": v.get("name", ""), "sort": v.get("sort", "")} for v in node.get("vars", [])]
            if kind == "exists":
                add_probe("existential_witness", node, scope, f"{origin}/exists")
            body = node.get("body")
            if isinstance(body, dict):
                visit(body, next_scope, f"{origin}/{kind}")
            return
        if kind == "implies":
            left = node.get("left")
            right = node.get("right")
            if isinstance(left, dict):
                add_probe("non_vacuity_guard", left, scope, f"{origin}/implies_left")
                visit(left, scope, f"{origin}/implies_left")
            if isinstance(right, dict):
                visit(right, scope, f"{origin}/implies_right")
            return
        if kind == "iff":
            left = node.get("left")
            right = node.get("right")
            if isinstance(left, dict):
                add_probe("iff_lhs_witness", left, scope, f"{origin}/iff_left")
                visit(left, scope, f"{origin}/iff_left")
            if isinstance(right, dict):
                add_probe("iff_rhs_witness", right, scope, f"{origin}/iff_right")
                visit(right, scope, f"{origin}/iff_right")
            return
        if kind == "or":
            for idx, arg in enumerate(node.get("args", []) or [], start=1):
                if isinstance(arg, dict):
                    add_probe("or_branch_witness", arg, scope, f"{origin}/or_branch_{idx}")
                    visit(arg, scope, f"{origin}/or_branch_{idx}")
            return
        if kind == "not":
            arg = node.get("arg")
            add_probe("negative_condition_witness", node, scope, f"{origin}/not")
            if isinstance(arg, dict):
                visit(arg, scope, f"{origin}/not_arg")
            return
        for key in ("body", "left", "right", "arg"):
            child = node.get(key)
            if isinstance(child, dict):
                visit(child, scope, f"{origin}/{key}")
        for idx, child in enumerate(node.get("args", []) or [], start=1):
            if isinstance(child, dict):
                visit(child, scope, f"{origin}/arg_{idx}")

    visit(expr, [], assertion.get("name", "assertion"))
    return probes


@dataclass
class SymbolDecl:
    kind: str
    name: str
    args: list[str]
    result_sort: str | None = None


class SmtCompiler:
    def __init__(self, ast: dict[str, Any]) -> None:
        self.ast = ast
        self.sorts: dict[str, dict[str, Any]] = {}
        self.entities: dict[str, str] = {}
        self.symbols: dict[str, SymbolDecl] = {}
        self.unsupported_base_assertions: list[dict[str, Any]] = []
        self._collect_declarations()

    def _collect_declarations(self) -> None:
        for decl in self.ast.get("declarations", []) or []:
            family = decl.get("family")
            kind = decl.get("kind")
            if family == "TypeDecl":
                if kind == "subtype":
                    self.sorts[decl["name"]] = {"kind": "subtype", "parent": decl.get("parent")}
                    self._ensure_sort(decl.get("parent"))
                elif kind == "enum":
                    self.sorts[decl["name"]] = {"kind": "enum", "members": decl.get("enum_members", [])}
                    for member in decl.get("enum_members", []) or []:
                        self.entities[member] = decl["name"]
                elif kind in {"opaque", "sort"}:
                    self.sorts[decl["name"]] = {"kind": "opaque"}
            elif family == "SymbolDecl":
                if kind == "entity":
                    self.entities[decl["name"]] = decl.get("sort")
                    self._ensure_sort(decl.get("sort"))
                elif kind == "rel":
                    args = list(decl.get("args", []) or [])
                    self.symbols[decl["name"]] = SymbolDecl(kind="rel", name=decl["name"], args=args)
                    for sort in args:
                        self._ensure_sort(sort)
                elif kind == "fun":
                    args = list(decl.get("args", []) or [])
                    result_sort = decl.get("result_sort")
                    self.symbols[decl["name"]] = SymbolDecl(kind="fun", name=decl["name"], args=args, result_sort=result_sort)
                    for sort in args + ([result_sort] if result_sort else []):
                        self._ensure_sort(sort)
        for sort in list(self.sorts):
            parent = self.sorts[sort].get("parent")
            if parent:
                self._ensure_sort(parent)

    def _ensure_sort(self, sort: str | None) -> None:
        if not sort:
            return
        if sort in BUILTIN_SORTS:
            return
        self.sorts.setdefault(sort, {"kind": "opaque"})

    def root_sort(self, sort: str | None) -> str:
        if not sort:
            raise UnsupportedSmt("missing sort")
        seen: set[str] = set()
        current = sort
        while True:
            if current in BUILTIN_SORTS:
                return BUILTIN_SORTS[current]
            if current in seen:
                raise UnsupportedSmt(f"cyclic sort parent chain at {sort}")
            seen.add(current)
            info = self.sorts.get(current)
            if not info:
                return _smt_ident(current)
            parent = info.get("parent")
            if not parent:
                return _smt_ident(current)
            current = parent

    def needs_sort_predicate(self, sort: str | None) -> bool:
        if not sort:
            return False
        return self.sorts.get(sort, {}).get("kind") == "subtype"

    def _sort_guard(self, var_name: str, sort: str | None) -> str | None:
        return self._sort_guard_expr(_smt_ident(var_name), sort)

    def _sort_guard_expr(self, term: str, sort: str | None) -> str | None:
        if self.needs_sort_predicate(sort):
            return f"({_smt_ident(sort or '')} {term})"
        return None

    def prelude(self) -> list[str]:
        lines: list[str] = []
        root_sorts = sorted({self.root_sort(s) for s in self.sorts if self.root_sort(s) not in {"Int", "Real", "Bool"}})
        for root in root_sorts:
            lines.append(f"(declare-sort {root} 0)")
        lines.append("")
        for sort, info in sorted(self.sorts.items()):
            if self.needs_sort_predicate(sort):
                lines.append(f"(declare-fun {_smt_ident(sort)} ({self.root_sort(sort)}) Bool)")
        if any(self.needs_sort_predicate(s) for s in self.sorts):
            lines.append("")
        for sort, info in sorted(self.sorts.items()):
            if info.get("kind") == "subtype" and self.needs_sort_predicate(info.get("parent")):
                root = self.root_sort(sort)
                x = f"x_{_smt_ident(sort)}"
                lines.append(
                    f"(assert (! (forall (({x} {root})) "
                    f"(=> ({_smt_ident(sort)} {x}) ({_smt_ident(info.get('parent'))} {x}))) "
                    f":named TYPE_{_smt_ident(sort)}_extends_{_smt_ident(info.get('parent'))}))"
                )
        if lines and lines[-1] != "":
            lines.append("")
        for name, sort in sorted(self.entities.items()):
            lines.append(f"(declare-const {_smt_ident(name)} {self.root_sort(sort)})")
        if self.entities:
            lines.append("")
        for name, sort in sorted(self.entities.items()):
            guard = self._sort_guard(name, sort)
            if guard:
                lines.append(f"(assert (! {guard} :named TYPE_entity_{_smt_ident(name)}))")
        for sort, info in sorted(self.sorts.items()):
            if info.get("kind") == "enum":
                members = [m for m in info.get("members", []) or [] if m in self.entities]
                if len(members) > 1:
                    args = " ".join(_smt_ident(m) for m in members)
                    lines.append(f"(assert (! (distinct {args}) :named TYPE_enum_distinct_{_smt_ident(sort)}))")
        if lines and lines[-1] != "":
            lines.append("")
        for symbol in sorted(self.symbols.values(), key=lambda s: s.name):
            if symbol.kind == "rel":
                args = " ".join(self.root_sort(s) for s in symbol.args)
                lines.append(f"(declare-fun {_smt_ident(symbol.name)} ({args}) Bool)")
            elif symbol.kind == "fun":
                args = " ".join(self.root_sort(s) for s in symbol.args)
                result = self.root_sort(symbol.result_sort)
                lines.append(f"(declare-fun {_smt_ident(symbol.name)} ({args}) {result})")
        if self.symbols:
            lines.append("")
        lines.extend(self._typing_axioms())
        if lines and lines[-1] != "":
            lines.append("")
        return lines

    def _typing_axioms(self) -> list[str]:
        lines: list[str] = []
        for symbol in sorted(self.symbols.values(), key=lambda s: s.name):
            var_decls: list[str] = []
            vars_: list[str] = []
            guards: list[str] = []
            for idx, sort in enumerate(symbol.args):
                var = f"{_smt_ident(symbol.name)}_arg{idx}"
                vars_.append(var)
                var_decls.append(f"({var} {self.root_sort(sort)})")
                guard = self._sort_guard(var, sort)
                if guard:
                    guards.append(guard)
            call = f"({_smt_ident(symbol.name)} {' '.join(vars_)})" if vars_ else f"({_smt_ident(symbol.name)})"
            consequences: list[str] = []
            if symbol.kind == "rel":
                consequences.extend(guards)
            if symbol.kind == "fun" and self.needs_sort_predicate(symbol.result_sort):
                consequences.append(f"({_smt_ident(symbol.result_sort or '')} {call})")
            if not consequences or not var_decls:
                continue
            consequent = consequences[0] if len(consequences) == 1 else f"(and {' '.join(consequences)})"
            if symbol.kind == "rel":
                body = f"(=> {call} {consequent})"
            else:
                body = consequent
            lines.append(
                f"(assert (! (forall ({' '.join(var_decls)}) {body}) "
                f":named TYPE_symbol_{_smt_ident(symbol.name)}))"
            )
        return lines

    def compile_assertions(self) -> tuple[list[str], list[dict[str, Any]]]:
        lines: list[str] = []
        unsupported: list[dict[str, Any]] = []
        for assertion in self.ast.get("assertions", []) or []:
            expr = assertion.get("expr")
            if not expr:
                unsupported.append({"assertion": assertion.get("name"), "reason": assertion.get("expr_error") or "missing expression"})
                continue
            reason = _contains_unsupported_expr(expr)
            if reason:
                unsupported.append({"assertion": assertion.get("name"), "reason": reason})
                continue
            try:
                smt_expr = self.compile_expr(expr, {})
            except UnsupportedSmt as exc:
                unsupported.append({"assertion": assertion.get("name"), "reason": str(exc)})
                continue
            lines.append(f"(assert (! {smt_expr} :named TEXT_{_smt_ident(assertion.get('name', 'assertion'))}))")
        self.unsupported_base_assertions = unsupported
        return lines, unsupported

    def compile_expr(self, expr: dict[str, Any], env: dict[str, str]) -> str:
        kind = expr.get("kind")
        if kind == "ref":
            name = expr.get("name", "")
            if name == "true":
                return "true"
            if name == "false":
                return "false"
            if _is_number_ref(name):
                return _number_to_smt(name)
            if name in env or name in self.entities:
                return _smt_ident(name)
            raise UnsupportedSmt(f"unknown reference {name}")
        if kind == "call":
            callee = expr.get("callee")
            if callee == "sum":
                raise UnsupportedSmt("sum aggregate is not supported by SMT v1")
            if callee not in self.symbols:
                raise UnsupportedSmt(f"unknown call target {callee}")
            args = [self.compile_expr(arg, env) for arg in expr.get("args", []) or []]
            return f"({_smt_ident(callee)} {' '.join(args)})" if args else f"({_smt_ident(callee)})"
        if kind == "isa":
            sort = expr.get("sort")
            if not sort:
                raise UnsupportedSmt("isa expression missing sort")
            return self._sort_guard_expr(self.compile_expr(expr.get("expr"), env), sort) or "true"
        if kind in {"and", "or"}:
            args = [self.compile_expr(arg, env) for arg in expr.get("args", []) or []]
            if not args:
                return "true" if kind == "and" else "false"
            if len(args) == 1:
                return args[0]
            return f"({kind} {' '.join(args)})"
        if kind == "not":
            return f"(not {self.compile_expr(expr.get('arg'), env)})"
        if kind == "implies":
            return f"(=> {self.compile_expr(expr.get('left'), env)} {self.compile_expr(expr.get('right'), env)})"
        if kind == "iff":
            return f"(= {self.compile_expr(expr.get('left'), env)} {self.compile_expr(expr.get('right'), env)})"
        if kind in {"eq", "lte", "gte", "lt", "gt"}:
            op = {"eq": "=", "lte": "<=", "gte": ">=", "lt": "<", "gt": ">"}[kind]
            return f"({op} {self.compile_expr(expr.get('left'), env)} {self.compile_expr(expr.get('right'), env)})"
        if kind in {"add", "sub", "mul", "div"}:
            op = {"add": "+", "sub": "-", "mul": "*", "div": "/"}[kind]
            return f"({op} {self.compile_expr(expr.get('left'), env)} {self.compile_expr(expr.get('right'), env)})"
        if kind in {"forall", "exists"}:
            vars_ = expr.get("vars", []) or []
            local_env = dict(env)
            decls: list[str] = []
            guards: list[str] = []
            for var in vars_:
                name = var.get("name")
                sort = var.get("sort")
                if not name or not sort:
                    raise UnsupportedSmt("quantifier variable missing name or sort")
                local_env[name] = sort
                decls.append(f"({_smt_ident(name)} {self.root_sort(sort)})")
                guard = self._sort_guard(name, sort)
                if guard:
                    guards.append(guard)
            body = self.compile_expr(expr.get("body"), local_env)
            if kind == "forall" and guards:
                guard_expr = guards[0] if len(guards) == 1 else f"(and {' '.join(guards)})"
                body = f"(=> {guard_expr} {body})"
            if kind == "exists" and guards:
                body = f"(and {' '.join(guards)} {body})"
            return f"({kind} ({' '.join(decls)}) {body})"
        if kind in UNSUPPORTED_EXPR_KINDS:
            raise UnsupportedSmt(f"unsupported expression kind {kind}")
        raise UnsupportedSmt(f"unknown expression kind {kind}")

    def compile_probe(self, probe: dict[str, Any]) -> tuple[str | None, str | None]:
        reason = _contains_unsupported_expr(probe.get("probe_expr"))
        if reason:
            return None, reason
        if self.unsupported_base_assertions:
            return None, "base theory has unsupported assertions"
        try:
            return self.compile_expr(probe["probe_expr"], {}), None
        except UnsupportedSmt as exc:
            return None, str(exc)

    def smt_base_text(self) -> tuple[str, list[dict[str, Any]]]:
        assertions, unsupported = self.compile_assertions()
        lines = ["(set-logic ALL)", "(set-option :produce-unsat-cores true)", ""]
        lines.extend(self.prelude())
        lines.extend(assertions)
        if lines and lines[-1] != "":
            lines.append("")
        return "\n".join(lines), unsupported


class BoundedWitnessSmtCompiler(SmtCompiler):
    """Quantifier-free witness lowering for fast SMT smoke checks.

    This compiler is deliberately not a replacement for full first-order SMT.
    It instantiates quantified variables with stable witness constants per
    ``(variable-name, sort)`` inside one generated SMT file. That lets a base
    assertion such as ``forall d. A(d) implies B(d)`` constrain a probe such as
    ``exists d. A(d)`` without asking Z3 to reason over open quantifiers.
    """

    def __init__(self, ast: dict[str, Any]) -> None:
        super().__init__(ast)
        self._witnesses: dict[tuple[str, str], str] = {}
        self._witness_sorts: dict[str, str] = {}

    def _reset_witnesses(self) -> None:
        self._witnesses = {}
        self._witness_sorts = {}

    def _witness_const(self, var_name: str, sort: str) -> str:
        key = (var_name, sort)
        if key in self._witnesses:
            return self._witnesses[key]
        raw = f"W_{var_name}_{sort}"
        const = re.sub(r"[^A-Za-z0-9_]+", "_", raw).strip("_") or "W"
        while const in self.entities or const in self._witness_sorts:
            const = f"{const}_w"
        self._witnesses[key] = const
        self._witness_sorts[const] = sort
        return const

    def prelude_bounded(self) -> list[str]:
        lines: list[str] = []
        sort_sources = list(self.sorts) + list(self.entities.values()) + list(self._witness_sorts.values())
        root_sorts = sorted({self.root_sort(s) for s in sort_sources if self.root_sort(s) not in {"Int", "Real", "Bool"}})
        for root in root_sorts:
            lines.append(f"(declare-sort {root} 0)")
        lines.append("")
        for sort in sorted(self.sorts):
            if self.needs_sort_predicate(sort):
                lines.append(f"(declare-fun {_smt_ident(sort)} ({self.root_sort(sort)}) Bool)")
        if any(self.needs_sort_predicate(s) for s in self.sorts):
            lines.append("")
        for name, sort in sorted(self.entities.items()):
            lines.append(f"(declare-const {_smt_ident(name)} {self.root_sort(sort)})")
        for name, sort in sorted(self._witness_sorts.items()):
            lines.append(f"(declare-const {_smt_ident(name)} {self.root_sort(sort)})")
        if self.entities or self._witness_sorts:
            lines.append("")
        for name, sort in sorted(self.entities.items()):
            guard = self._sort_guard(name, sort)
            if guard:
                lines.append(f"(assert (! {guard} :named TYPE_entity_{_smt_ident(name)}))")
        for name, sort in sorted(self._witness_sorts.items()):
            guard = self._sort_guard(name, sort)
            if guard:
                lines.append(f"(assert (! {guard} :named TYPE_witness_{_smt_ident(name)}))")
        for sort, info in sorted(self.sorts.items()):
            if info.get("kind") == "enum":
                members = [m for m in info.get("members", []) or [] if m in self.entities]
                if len(members) > 1:
                    args = " ".join(_smt_ident(m) for m in members)
                    lines.append(f"(assert (! (distinct {args}) :named TYPE_enum_distinct_{_smt_ident(sort)}))")
        if lines and lines[-1] != "":
            lines.append("")
        for symbol in sorted(self.symbols.values(), key=lambda s: s.name):
            if symbol.kind == "rel":
                args = " ".join(self.root_sort(s) for s in symbol.args)
                lines.append(f"(declare-fun {_smt_ident(symbol.name)} ({args}) Bool)")
            elif symbol.kind == "fun":
                args = " ".join(self.root_sort(s) for s in symbol.args)
                result = self.root_sort(symbol.result_sort)
                lines.append(f"(declare-fun {_smt_ident(symbol.name)} ({args}) {result})")
        if self.symbols:
            lines.append("")
        return lines

    def compile_assertions_bounded(self) -> tuple[list[str], list[dict[str, Any]]]:
        lines: list[str] = []
        unsupported: list[dict[str, Any]] = []
        for assertion in self.ast.get("assertions", []) or []:
            expr = assertion.get("expr")
            if not expr:
                unsupported.append({"assertion": assertion.get("name"), "reason": assertion.get("expr_error") or "missing expression"})
                continue
            reason = _contains_unsupported_expr(expr)
            if reason:
                unsupported.append({"assertion": assertion.get("name"), "reason": reason})
                continue
            try:
                smt_expr = self.compile_expr_bounded(expr, {})
            except UnsupportedSmt as exc:
                unsupported.append({"assertion": assertion.get("name"), "reason": str(exc)})
                continue
            lines.append(f"(assert (! {smt_expr} :named BOUNDED_TEXT_{_smt_ident(assertion.get('name', 'assertion'))}))")
        self.unsupported_base_assertions = unsupported
        return lines, unsupported

    def compile_expr_bounded(self, expr: dict[str, Any], env: dict[str, str]) -> str:
        kind = expr.get("kind")
        if kind == "ref":
            name = expr.get("name", "")
            if name == "true":
                return "true"
            if name == "false":
                return "false"
            if _is_number_ref(name):
                return _number_to_smt(name)
            if name in env:
                return _smt_ident(env[name])
            if name in self.entities:
                return _smt_ident(name)
            raise UnsupportedSmt(f"unknown reference {name}")
        if kind == "call":
            callee = expr.get("callee")
            if callee == "sum":
                raise UnsupportedSmt("sum aggregate is not supported by SMT v1")
            if callee not in self.symbols:
                raise UnsupportedSmt(f"unknown call target {callee}")
            args = [self.compile_expr_bounded(arg, env) for arg in expr.get("args", []) or []]
            return f"({_smt_ident(callee)} {' '.join(args)})" if args else f"({_smt_ident(callee)})"
        if kind == "isa":
            sort = expr.get("sort")
            if not sort:
                raise UnsupportedSmt("isa expression missing sort")
            return self._sort_guard_expr(self.compile_expr_bounded(expr.get("expr"), env), sort) or "true"
        if kind in {"and", "or"}:
            args = [self.compile_expr_bounded(arg, env) for arg in expr.get("args", []) or []]
            if not args:
                return "true" if kind == "and" else "false"
            if len(args) == 1:
                return args[0]
            return f"({kind} {' '.join(args)})"
        if kind == "not":
            return f"(not {self.compile_expr_bounded(expr.get('arg'), env)})"
        if kind == "implies":
            return f"(=> {self.compile_expr_bounded(expr.get('left'), env)} {self.compile_expr_bounded(expr.get('right'), env)})"
        if kind == "iff":
            return f"(= {self.compile_expr_bounded(expr.get('left'), env)} {self.compile_expr_bounded(expr.get('right'), env)})"
        if kind in {"eq", "lte", "gte", "lt", "gt"}:
            op = {"eq": "=", "lte": "<=", "gte": ">=", "lt": "<", "gt": ">"}[kind]
            return f"({op} {self.compile_expr_bounded(expr.get('left'), env)} {self.compile_expr_bounded(expr.get('right'), env)})"
        if kind in {"add", "sub", "mul", "div"}:
            op = {"add": "+", "sub": "-", "mul": "*", "div": "/"}[kind]
            return f"({op} {self.compile_expr_bounded(expr.get('left'), env)} {self.compile_expr_bounded(expr.get('right'), env)})"
        if kind in {"forall", "exists"}:
            local_env = dict(env)
            guards: list[str] = []
            for var in expr.get("vars", []) or []:
                name = var.get("name")
                sort = var.get("sort")
                if not name or not sort:
                    raise UnsupportedSmt("quantifier variable missing name or sort")
                const = self._witness_const(name, sort)
                local_env[name] = const
                guard = self._sort_guard(const, sort)
                if guard:
                    guards.append(guard)
            body = self.compile_expr_bounded(expr.get("body"), local_env)
            if guards:
                return f"(and {' '.join(guards)} {body})"
            return body
        if kind in UNSUPPORTED_EXPR_KINDS:
            raise UnsupportedSmt(f"unsupported expression kind {kind}")
        raise UnsupportedSmt(f"unknown expression kind {kind}")

    def smt_bounded_base_text(self) -> tuple[str, list[dict[str, Any]]]:
        self._reset_witnesses()
        assertions, unsupported = self.compile_assertions_bounded()
        lines = ["(set-logic ALL)", "(set-option :produce-unsat-cores true)", ""]
        lines.extend(self.prelude_bounded())
        lines.extend(assertions)
        if lines and lines[-1] != "":
            lines.append("")
        return "\n".join(lines), unsupported

    def smt_bounded_probe_text(self, probe: dict[str, Any]) -> tuple[str | None, str | None]:
        reason = _contains_unsupported_expr(probe.get("probe_expr"))
        if reason:
            return None, reason
        self._reset_witnesses()
        assertions, unsupported = self.compile_assertions_bounded()
        if unsupported:
            return None, "base theory has unsupported assertions"
        try:
            probe_smt = self.compile_expr_bounded(probe["probe_expr"], {})
        except UnsupportedSmt as exc:
            return None, str(exc)
        lines = ["(set-logic ALL)", "(set-option :produce-unsat-cores true)", ""]
        lines.extend(self.prelude_bounded())
        lines.extend(assertions)
        if lines and lines[-1] != "":
            lines.append("")
        lines.append("(check-sat)")
        lines.append("(push 1)")
        lines.append(f"(assert (! {probe_smt} :named BOUNDED_PROBE_{_smt_ident(probe['probe_id'])}))")
        lines.append("(check-sat)")
        lines.append("(pop 1)")
        return "\n".join(lines) + "\n", None


def _write_probe_smt(path: Path, base_text: str, probe: dict[str, Any], probe_smt: str) -> None:
    text = (
        base_text
        + f"; Probe {probe['probe_id']}: {probe['probe_type']}\n"
        + "(check-sat)\n"
        + "(push 1)\n"
        + f"(assert (! {probe_smt} :named PROBE_{_smt_ident(probe['probe_id'])}))\n"
        + "(check-sat)\n"
        + "(pop 1)\n"
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _write_base_smt(path: Path, base_text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(base_text + "(check-sat)\n", encoding="utf-8")


def _run_z3_file(z3_path: str, smt_path: Path, extra_commands: str = "") -> dict[str, Any]:
    if extra_commands:
        with tempfile.NamedTemporaryFile("w", suffix=".smt2", encoding="utf-8", delete=False) as tmp:
            tmp.write(smt_path.read_text(encoding="utf-8"))
            tmp.write("\n")
            tmp.write(extra_commands)
            tmp_path = Path(tmp.name)
        run_path = tmp_path
    else:
        tmp_path = None
        run_path = smt_path
    try:
        proc = subprocess.run(
            [z3_path, "-T:10", "-smt2", str(run_path)],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=15,
            check=False,
        )
    except subprocess.TimeoutExpired as exc:
        return {
            "returncode": None,
            "status": "timeout",
            "stdout": (exc.stdout or "")[-5000:] if isinstance(exc.stdout, str) else "",
            "stderr": (exc.stderr or "")[-5000:] if isinstance(exc.stderr, str) else "",
            "timeout_s": 15,
        }
    finally:
        if tmp_path:
            tmp_path.unlink(missing_ok=True)
    stdout = proc.stdout.strip()
    lines = [line.strip() for line in stdout.splitlines() if line.strip()]
    status = next((line for line in lines if line in {"sat", "unsat", "unknown", "timeout"}), None)
    return {
        "returncode": proc.returncode,
        "status": status or "no_status",
        "stdout": proc.stdout[-5000:],
        "stderr": proc.stderr[-5000:],
    }


def _find_z3(run_root: Path) -> str | None:
    """Find a local Z3 executable.

    Windows project environments created by `uv` may expose `z3.exe` under
    `.venv/bin` even when it is not on PATH. Prefer PATH, then probe likely
    repository-local virtualenv locations.
    """
    if path := shutil.which("z3"):
        return path
    candidates: list[Path] = []
    resolved = run_root.resolve()
    for base in [resolved, *resolved.parents]:
        candidates.extend(
            [
                base / ".venv" / "bin" / "z3.exe",
                base / ".venv" / "Scripts" / "z3.exe",
                base / ".venv" / "bin" / "z3",
            ]
        )
    for candidate in candidates:
        if candidate.exists():
            return str(candidate)
    return None


def _z3_statuses(run: dict[str, Any]) -> list[str]:
    return [line.strip() for line in run.get("stdout", "").splitlines() if line.strip() in {"sat", "unsat", "unknown"}]


def _needs_bounded_fallback(result: dict[str, Any]) -> bool:
    status = result.get("probe_solver_status") or result.get("status") or result.get("solver_status")
    return status in {"timeout", "unknown", "no_status"}


def _bounded_severity(status: str | None, *, must_be_satisfiable: bool = False, is_base: bool = False) -> str:
    if status == "unsat":
        return "hard" if (must_be_satisfiable or is_base) else "soft"
    if status in {"unknown", "timeout", "no_status"}:
        return "soft"
    if status == "sat":
        return "advisory"
    return "advisory"


def _fixture_smt_text() -> str:
    return """(set-logic ALL)
(set-option :produce-unsat-cores true)

(declare-sort Event 0)
(declare-sort Day 0)

(declare-fun ThirdFriday (Event) Day)
(declare-fun TradingDay (Day) Bool)
(declare-fun NextTradingDay (Day) Day)
(declare-fun RebalanceDay (Event) Day)

(assert (! (forall ((e Event))
  (= (RebalanceDay e) (ThirdFriday e)))
  :named TEXT_S1))

(assert (! (forall ((e Event))
  (=> (not (TradingDay (ThirdFriday e)))
      (= (RebalanceDay e) (NextTradingDay (ThirdFriday e)))))
  :named TEXT_S2))

(assert (! (forall ((e Event))
  (=> (not (TradingDay (ThirdFriday e)))
      (and (= (RebalanceDay e) (ThirdFriday e))
           (not (= (RebalanceDay e) (NextTradingDay (ThirdFriday e)))))))
  :named TEXT_S3))

(check-sat)
(push 1)
(assert (! (exists ((e Event))
  (not (TradingDay (ThirdFriday e))))
  :named PROBE_non_trading_third_friday))
(check-sat)
(get-unsat-core)
(pop 1)
"""


def _analyze_entry(
    entry: dict[str, Any],
    smt_dir: Path,
    bounded_smt_dir: Path,
    plan_only: bool,
    z3_path: str | None,
    smt_mode: str,
) -> dict[str, Any]:
    entry_dir: Path = entry["entry_dir"]
    entry_id = entry["entry_id"]
    ast = parse((entry_dir / "main_ir.a4v3").read_text(encoding="utf-8"), strict=False)
    probes: list[dict[str, Any]] = []
    for assertion in ast.get("assertions", []) or []:
        probes.extend(
            _extract_probes_from_expr(
                entry_id=entry_id,
                entry_kind=entry["entry_kind"],
                relative_dir=entry["relative_dir"],
                assertion=assertion,
            )
        )

    compiler = SmtCompiler(ast)
    bounded_compiler = BoundedWitnessSmtCompiler(ast)
    base_text, unsupported_base = compiler.smt_base_text()
    base_compile_status = "unsupported" if unsupported_base else "executable"
    entry_smt_dir = smt_dir / entry_id
    entry_bounded_dir = bounded_smt_dir / entry_id
    base_smt_path = entry_smt_dir / "base_check.smt2"
    bounded_base_smt_path = entry_bounded_dir / "base_check.bounded.smt2"
    if not plan_only:
        _write_base_smt(base_smt_path, base_text)

    base_result: dict[str, Any] = {
        "compile_status": base_compile_status,
        "unsupported_assertions": unsupported_base,
        "smt_mode": smt_mode,
        "solver_status": "not_run_plan_only" if plan_only else ("solver_unavailable" if not z3_path else "not_run"),
        "smt_path": str(base_smt_path) if not plan_only else None,
        "bounded_compile_status": "not_run",
        "bounded_solver_status": "not_run_plan_only" if plan_only else ("solver_unavailable" if not z3_path else "not_run"),
        "bounded_smt_path": str(bounded_base_smt_path) if not plan_only else None,
    }
    run_full_base = smt_mode in {"full", "hybrid"}
    run_bounded_base = smt_mode == "bounded-witness"
    if not plan_only and z3_path and not unsupported_base and run_full_base:
        base_result.update(_run_z3_file(z3_path, base_smt_path))
    elif smt_mode == "bounded-witness":
        base_result["solver_status"] = "not_run_bounded_witness_mode"

    if smt_mode == "hybrid" and _needs_bounded_fallback(base_result):
        run_bounded_base = True
        base_result["bounded_reason"] = "full_solver_fallback"
    if run_bounded_base:
        bounded_base_text, bounded_unsupported_base = bounded_compiler.smt_bounded_base_text()
        base_result["bounded_compile_status"] = "unsupported" if bounded_unsupported_base else "executable"
        base_result["bounded_unsupported_assertions"] = bounded_unsupported_base
        if not plan_only:
            _write_base_smt(bounded_base_smt_path, bounded_base_text)
            if z3_path and not bounded_unsupported_base:
                bounded_run = _run_z3_file(z3_path, bounded_base_smt_path)
                base_result["bounded_solver_status"] = bounded_run.get("status")
                base_result["bounded_run"] = bounded_run
            elif bounded_unsupported_base:
                base_result["bounded_solver_status"] = "not_applicable_unsupported"

    probe_results: list[dict[str, Any]] = []
    for probe in probes:
        probe_smt, reason = compiler.compile_probe(probe)
        solver_status = "not_applicable_unsupported" if reason else (
            "not_run_plan_only" if plan_only else ("solver_unavailable" if not z3_path else "not_run")
        )
        if smt_mode == "bounded-witness" and not reason:
            solver_status = "not_run_bounded_witness_mode"
        result = {
            "probe_id": probe["probe_id"],
            "probe_type": probe["probe_type"],
            "assertion": probe["assertion"],
            "compile_status": "unsupported" if reason else "executable",
            "unsupported_reason": reason,
            "smt_mode": smt_mode,
            "solver_status": solver_status,
            "severity": "advisory" if (reason or solver_status == "solver_unavailable") else "not_evaluated",
            "smt_path": None,
            "bounded_compile_status": "not_run",
            "bounded_solver_status": "not_run_plan_only" if plan_only else ("solver_unavailable" if not z3_path else "not_run"),
            "bounded_smt_path": None,
        }
        if not reason and probe_smt:
            probe_path = entry_smt_dir / f"{probe['probe_id']}.smt2"
            probe["compile_status"] = "executable"
            probe["unsupported_reason"] = None
            probe["smt_path"] = str(probe_path)
            result["smt_path"] = str(probe_path)
            if not plan_only:
                _write_probe_smt(probe_path, base_text, probe, probe_smt)
                if z3_path and run_full_base:
                    run = _run_z3_file(z3_path, probe_path)
                    result.update(run)
                    # The probe file performs base check then probe check.
                    statuses = _z3_statuses(run)
                    if len(statuses) >= 2:
                        result["base_solver_status"] = statuses[0]
                        result["probe_solver_status"] = statuses[1]
                        if statuses[1] == "unsat":
                            result["severity"] = "hard" if probe.get("must_be_satisfiable") else "soft"
                        elif statuses[1] == "unknown":
                            result["severity"] = "soft"
                        else:
                            result["severity"] = "advisory"
                    elif run.get("status") == "unknown":
                        result["severity"] = "soft"
                    elif run.get("status") == "timeout":
                        result["probe_solver_status"] = "timeout"
                        result["severity"] = "soft"
                    elif run.get("status") == "no_status":
                        result["probe_solver_status"] = "no_status"
                        result["severity"] = "soft"
                    else:
                        result["severity"] = "advisory"
        else:
            probe["compile_status"] = "unsupported"
            probe["unsupported_reason"] = reason
            probe["smt_path"] = None

        run_bounded_probe = False
        if not reason and smt_mode == "bounded-witness":
            run_bounded_probe = True
            result["bounded_reason"] = "bounded_witness_mode"
        elif not reason and smt_mode == "hybrid" and _needs_bounded_fallback(result):
            run_bounded_probe = True
            result["bounded_reason"] = "full_solver_fallback"
        if run_bounded_probe:
            bounded_probe_text, bounded_reason = bounded_compiler.smt_bounded_probe_text(probe)
            result["bounded_compile_status"] = "unsupported" if bounded_reason else "executable"
            result["bounded_unsupported_reason"] = bounded_reason
            if bounded_reason:
                result["bounded_solver_status"] = "not_applicable_unsupported"
            elif bounded_probe_text:
                bounded_probe_path = entry_bounded_dir / f"{probe['probe_id']}.bounded.smt2"
                result["bounded_smt_path"] = str(bounded_probe_path)
                probe["bounded_smt_path"] = str(bounded_probe_path)
                if not plan_only:
                    bounded_probe_path.parent.mkdir(parents=True, exist_ok=True)
                    bounded_probe_path.write_text(bounded_probe_text, encoding="utf-8")
                    if z3_path:
                        bounded_run = _run_z3_file(z3_path, bounded_probe_path)
                        statuses = _z3_statuses(bounded_run)
                        result["bounded_run"] = bounded_run
                        result["bounded_solver_status"] = statuses[1] if len(statuses) >= 2 else bounded_run.get("status")
                        result["bounded_base_solver_status"] = statuses[0] if statuses else bounded_run.get("status")
                        result["bounded_severity"] = _bounded_severity(
                            result.get("bounded_solver_status"),
                            must_be_satisfiable=bool(probe.get("must_be_satisfiable")),
                        )
                        if smt_mode == "bounded-witness":
                            result["severity"] = result["bounded_severity"]
        probe_results.append(result)

    counts = Counter(r["compile_status"] for r in probe_results)
    solver_counts = Counter(r.get("probe_solver_status", r.get("solver_status")) for r in probe_results)
    bounded_counts = Counter(r.get("bounded_compile_status") for r in probe_results)
    bounded_solver_counts = Counter(r.get("bounded_solver_status") for r in probe_results)
    severity_counts = Counter(r.get("severity") for r in probe_results if r.get("severity") != "not_evaluated")
    return {
        "entry_id": entry_id,
        "entry_kind": entry["entry_kind"],
        "relative_dir": entry["relative_dir"],
        "assertion_count": len(ast.get("assertions", []) or []),
        "probe_count": len(probes),
        "probe_compile_counts": dict(counts),
        "probe_solver_counts": dict(solver_counts),
        "bounded_probe_compile_counts": dict(bounded_counts),
        "bounded_probe_solver_counts": dict(bounded_solver_counts),
        "probe_severity_counts": dict(severity_counts),
        "base_result": base_result,
        "probes": probes,
        "probe_results": probe_results,
    }


def analyze(run_root: Path, plan_only: bool = False, smt_mode: str = "hybrid") -> dict[str, Any]:
    out_dir = run_root / "reasoning"
    smt_dir = out_dir / "smt_probes"
    bounded_smt_dir = out_dir / "smt_probes_bounded"
    entries = _discover_entries(run_root)
    z3_path = _find_z3(run_root)

    entry_reports = [_analyze_entry(entry, smt_dir, bounded_smt_dir, plan_only, z3_path, smt_mode) for entry in entries]
    all_specs = [probe for entry in entry_reports for probe in entry["probes"]]
    all_results = [result for entry in entry_reports for result in entry["probe_results"]]

    # Regression fixture from thoughts/rebalance_day.
    fixture_path = smt_dir / "fixture_rebalance_day" / "fixture_non_trading_third_friday.smt2"
    fixture_result: dict[str, Any] = {
        "fixture_id": "fixture_rebalance_day_non_trading_third_friday",
        "smt_path": None if plan_only else str(fixture_path),
        "expected_base_status": "sat",
        "expected_probe_status": "unsat",
        "solver_status": "not_run_plan_only" if plan_only else ("solver_unavailable" if not z3_path else "not_run"),
    }
    if not plan_only:
        fixture_path.parent.mkdir(parents=True, exist_ok=True)
        fixture_path.write_text(_fixture_smt_text(), encoding="utf-8")
        if z3_path:
            run = _run_z3_file(z3_path, fixture_path)
            fixture_result.update(run)
            fixture_result["solver_status"] = run.get("status")
            statuses = [line.strip() for line in run.get("stdout", "").splitlines() if line.strip() in {"sat", "unsat", "unknown"}]
            fixture_result["observed_statuses"] = statuses
            fixture_result["passed"] = len(statuses) >= 2 and statuses[0] == "sat" and statuses[1] == "unsat"

    compile_counts = Counter(probe.get("compile_status") for probe in all_specs)
    solver_counts = Counter(result.get("probe_solver_status", result.get("solver_status")) for result in all_results)
    bounded_compile_counts = Counter(result.get("bounded_compile_status") for result in all_results)
    bounded_solver_counts = Counter(result.get("bounded_solver_status") for result in all_results)
    severity_counts = Counter(result.get("severity") for result in all_results if result.get("severity") not in {None, "not_evaluated"})
    base_counts = Counter(entry["base_result"].get("compile_status") for entry in entry_reports)
    base_solver_counts = Counter(entry["base_result"].get("status", entry["base_result"].get("solver_status")) for entry in entry_reports)
    bounded_base_counts = Counter(entry["base_result"].get("bounded_compile_status") for entry in entry_reports)
    bounded_base_solver_counts = Counter(entry["base_result"].get("bounded_solver_status") for entry in entry_reports)

    hard = 0
    soft = 0
    advisory = 0
    if not plan_only:
        for entry in entry_reports:
            base = entry["base_result"]
            if base.get("status") == "unsat":
                hard += 1
            elif base.get("status") in {"unknown", "timeout", "no_status"}:
                soft += 1
        for result in all_results:
            if result.get("severity") == "hard":
                hard += 1
            elif result.get("severity") == "soft":
                soft += 1
            elif result.get("severity") == "advisory":
                advisory += 1
        for entry in entry_reports:
            base = entry["base_result"]
            if base.get("bounded_solver_status") == "unsat":
                hard += 1
        for result in all_results:
            if result.get("bounded_severity") == "hard":
                hard += 1
            elif result.get("bounded_severity") == "soft" and result.get("severity") != "soft":
                soft += 1
            elif result.get("bounded_severity") == "advisory" and result.get("severity") not in {"soft", "hard"}:
                advisory += 1
    else:
        advisory = compile_counts.get("unsupported", 0)

    status = "blocked" if hard else "passed_with_review_items"
    if not (hard or soft or advisory):
        status = "passed"

    return {
        "schema": "smt_probe_results_v1",
        "run_root": str(run_root),
        "plan_only": plan_only,
        "smt_mode": smt_mode,
        "z3_path": z3_path,
        "solver_available": bool(z3_path),
        "entry_count": len(entries),
        "probe_count": len(all_specs),
        "base_compile_counts": dict(base_counts),
        "base_solver_counts": dict(base_solver_counts),
        "bounded_base_compile_counts": dict(bounded_base_counts),
        "bounded_base_solver_counts": dict(bounded_base_solver_counts),
        "probe_compile_counts": dict(compile_counts),
        "probe_solver_counts": dict(solver_counts),
        "bounded_probe_compile_counts": dict(bounded_compile_counts),
        "bounded_probe_solver_counts": dict(bounded_solver_counts),
        "hard_findings": hard,
        "soft_findings": soft,
        "advisory_findings": advisory,
        "status": status,
        "entries": entry_reports,
        "probe_specs": all_specs,
        "probe_results": all_results,
        "fixture": fixture_result,
    }


def _write_specs_markdown(report: dict[str, Any], out_path: Path) -> None:
    lines = ["# SMT Probe Specs v1", ""]
    lines.append(f"SMT mode: `{report.get('smt_mode')}`")
    lines.append(f"Entries: `{report['entry_count']}`")
    lines.append(f"Probe specs: `{report['probe_count']}`")
    lines.append(f"Probe compile counts: `{json.dumps(report['probe_compile_counts'], ensure_ascii=False)}`")
    lines.append("")
    lines.append("| Entry | Probes | Executable | Unsupported |")
    lines.append("| --- | ---: | ---: | ---: |")
    for entry in report["entries"]:
        counts = Counter(p.get("compile_status") for p in entry["probes"])
        lines.append(
            f"| `{entry['entry_id']}` | {entry['probe_count']} | "
            f"{counts.get('executable', 0)} | {counts.get('unsupported', 0)} |"
        )
    lines.append("")
    lines.append("## Probe Type Counts")
    lines.append("")
    for probe_type, count in sorted(Counter(p["probe_type"] for p in report["probe_specs"]).items()):
        lines.append(f"- `{probe_type}`: {count}")
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _write_results_markdown(report: dict[str, Any], out_path: Path) -> None:
    lines = ["# SMT Probe Results v1", ""]
    lines.append(f"Status: `{report['status']}`")
    lines.append(f"SMT mode: `{report.get('smt_mode')}`")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    for key in [
        "entry_count",
        "probe_count",
        "solver_available",
        "base_compile_counts",
        "base_solver_counts",
        "bounded_base_compile_counts",
        "bounded_base_solver_counts",
        "probe_compile_counts",
        "probe_solver_counts",
        "bounded_probe_compile_counts",
        "bounded_probe_solver_counts",
        "hard_findings",
        "soft_findings",
        "advisory_findings",
    ]:
        lines.append(f"- `{key}`: `{json.dumps(report.get(key), ensure_ascii=False)}`")
    lines.append("")
    lines.append("## Fixture")
    lines.append("")
    lines.append(f"- `fixture_id`: `{report['fixture'].get('fixture_id')}`")
    lines.append(f"- `solver_status`: `{report['fixture'].get('solver_status')}`")
    if "observed_statuses" in report["fixture"]:
        lines.append(f"- `observed_statuses`: `{report['fixture'].get('observed_statuses')}`")
        lines.append(f"- `passed`: `{report['fixture'].get('passed')}`")
    lines.append("")
    lines.append("## Entry Table")
    lines.append("")
    lines.append("| Entry | Probes | Executable | Unsupported | SAT | UNSAT | UNKNOWN | Timeout | Bounded SAT | Bounded UNSAT | Bounded Timeout |")
    lines.append("| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |")
    for entry in report["entries"]:
        compile_counts = Counter(r.get("compile_status") for r in entry["probe_results"])
        solver_counts = Counter(r.get("probe_solver_status", r.get("solver_status")) for r in entry["probe_results"])
        bounded_solver_counts = Counter(r.get("bounded_solver_status") for r in entry["probe_results"])
        lines.append(
            f"| `{entry['entry_id']}` | {entry['probe_count']} | "
            f"{compile_counts.get('executable', 0)} | {compile_counts.get('unsupported', 0)} | "
            f"{solver_counts.get('sat', 0)} | {solver_counts.get('unsat', 0)} | "
            f"{solver_counts.get('unknown', 0)} | {solver_counts.get('timeout', 0)} | "
            f"{bounded_solver_counts.get('sat', 0)} | {bounded_solver_counts.get('unsat', 0)} | "
            f"{bounded_solver_counts.get('timeout', 0)} |"
        )
    lines.append("")
    lines.append("## Interpretation")
    lines.append("")
    lines.append(
        "Executable probes have an SMT-LIB sidecar file. Unsupported probes are "
        "kept as explicit candidates for later compiler expansion. In `hybrid` "
        "mode, full SMT is attempted first and bounded-witness SMT is used only "
        "when full SMT times out or returns an unresolved status. Bounded witness "
        "results are smoke checks, not replacements for full first-order proofs."
    )
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _write_inventory(out_path: Path) -> None:
    out_path.write_text(
        """# SMT Probe Inventory v1

This sidecar layer generates SMT probe/witness candidates from existing local
seed methodology `main_ir.a4v3` files. It does not modify local IR.

## Probe Types

- `non_vacuity_guard`: checks that an `implies` antecedent can be realized.
- `iff_lhs_witness`: checks that the left side of an `iff` can be realized.
- `iff_rhs_witness`: checks that the right side of an `iff` can be realized.
- `or_branch_witness`: checks that each explicit `or` branch can be realized.
- `existential_witness`: checks that explicit existential scenarios can be realized.
- `negative_condition_witness`: checks that explicit `not ...` conditions can be realized.

## SMT v1 Scope

The v1 compiler is intentionally shallow. It supports relational skeletons,
subtype predicates, quantifiers, Boolean connectives, equality, numeric
comparisons, arithmetic, relation calls, and function calls. Aggregates such as
`count` and `sum` are marked unsupported instead of guessed.

## SMT Modes

- `full`: emit and solve the direct first-order SMT lowering.
- `bounded-witness`: replace quantified variables with stable witness constants
  per variable-name/sort inside each generated SMT file. This is a fast
  vacuity/conflict smoke check and deliberately avoids unbounded `forall`.
- `hybrid`: run `full` first; if Z3 times out or returns an unresolved status,
  generate and run the bounded-witness fallback for that base/probe.

## Severity

UNSAT base theories are hard findings. UNSAT non-mandatory probes are soft
review signals. Unsupported probe candidates are advisory and document where
future SMT coverage can grow.
""",
        encoding="utf-8",
    )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-root", default="case_studies/financial_methodology")
    ap.add_argument("--out-dir", default=None)
    ap.add_argument("--plan-only", action="store_true")
    ap.add_argument(
        "--smt-mode",
        choices=["full", "bounded-witness", "hybrid"],
        default="hybrid",
        help="full first-order SMT, bounded witness smoke checks, or full-with-bounded-fallback",
    )
    args = ap.parse_args()

    run_root = Path(args.run_root)
    out_dir = Path(args.out_dir) if args.out_dir else run_root / "reasoning"
    out_dir.mkdir(parents=True, exist_ok=True)

    report = analyze(run_root, plan_only=args.plan_only, smt_mode=args.smt_mode)
    specs_report = {
        "schema": "smt_probe_specs_v1",
        "run_root": report["run_root"],
        "smt_mode": report["smt_mode"],
        "entry_count": report["entry_count"],
        "probe_count": report["probe_count"],
        "probe_compile_counts": report["probe_compile_counts"],
        "entries": report["entries"],
        "probe_specs": report["probe_specs"],
    }

    (out_dir / "smt_probe_specs_v1.json").write_text(
        json.dumps(specs_report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    (out_dir / "smt_probe_results_v1.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    _write_specs_markdown(report, out_dir / "smt_probe_specs_v1.md")
    _write_results_markdown(report, out_dir / "smt_probe_results_v1.md")
    _write_inventory(out_dir / "smt_probe_inventory_v1.md")

    print(
        json.dumps(
            {
                "status": report["status"],
                "solver_available": report["solver_available"],
                "smt_mode": report["smt_mode"],
                "entry_count": report["entry_count"],
                "probe_count": report["probe_count"],
                "probe_compile_counts": report["probe_compile_counts"],
                "bounded_probe_compile_counts": report["bounded_probe_compile_counts"],
                "bounded_probe_solver_counts": report["bounded_probe_solver_counts"],
                "hard_findings": report["hard_findings"],
                "soft_findings": report["soft_findings"],
                "advisory_findings": report["advisory_findings"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
