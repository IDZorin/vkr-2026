"""a4v3_smt_solve_v1.py

Small executable SMT solve backend for arithmetic A4V3 facts.

This is intentionally separate from `smt_consistency_check_v1.py`.
The consistency checker is a structural/SAT precursor; this module lowers
supported arithmetic `fact`/`constraint`/`axiom` expression ASTs to Z3 Reals
and extracts `answer_value(...)` / `quantity_value(...)` query values.

Supported v1 expression subset:
  - top-level `and`
  - comparisons: `=`, `<`, `<=`, `>`, `>=`
  - arithmetic: `+`, `-`, `*`, `/`
  - numeric literals parsed by the canonical ExprParser
  - value calls: `quantity_value(Entity)`, `answer_value(Entity)`

Non-arithmetic relation calls are ignored but reported. Unsupported expression
shapes are reported and never silently treated as solved.

CLI:
    python a4v3_smt_solve_v1.py <entry_dir|run_root> [--query auto|all|answer_value(X)|quantity_value(X)]
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys
from dataclasses import dataclass
from fractions import Fraction
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(pathlib.Path(__file__).parent))

import a4v3_parser_v1 as parser  # noqa: E402

try:
    import z3  # type: ignore
    _Z3_AVAILABLE = True
except ImportError:
    z3 = None  # type: ignore
    _Z3_AVAILABLE = False


VALUE_CALLEES = {"quantity_value", "answer_value"}
ASSERTION_KINDS = {"fact", "constraint", "axiom"}
NUMERIC_RE = re.compile(r"^-?\d+(?:\.\d+)?%?$")
QUERY_RE = re.compile(r"^(answer_value|quantity_value)\(([A-Za-z_][A-Za-z0-9_]*)\)$")


@dataclass(frozen=True)
class UnsupportedExpr:
    assertion: str
    kind: str
    reason: str
    expr: str
    line_no: int | None = None


class ArithmeticLowerer:
    def __init__(self) -> None:
        if not _Z3_AVAILABLE:
            raise RuntimeError("z3 is not installed")
        self.solver = z3.Solver()
        self.solver.set("timeout", 5000)
        self.vars: dict[tuple[str, str], Any] = {}
        self.asserted_constraints: list[dict[str, Any]] = []
        self.ignored_non_arithmetic: list[dict[str, Any]] = []
        self.unsupported: list[UnsupportedExpr] = []
        self.answer_quantity_links: list[tuple[str, str, str, int | None]] = []

    def lower_assertion(self, decl: dict[str, Any]) -> None:
        expr = decl.get("expr")
        if expr is None:
            self.unsupported.append(UnsupportedExpr(
                assertion=str(decl.get("name")),
                kind=str(decl.get("kind")),
                reason=decl.get("expr_error") or "missing parsed expression",
                expr=str(decl.get("body_text") or ""),
                line_no=decl.get("line_no"),
            ))
            return
        self._lower_bool(expr, decl)

    def _lower_bool(self, expr: dict[str, Any], decl: dict[str, Any]) -> Any | None:
        kind = expr.get("kind")
        if kind == "and":
            parts = []
            for item in expr.get("args") or []:
                lowered = self._lower_bool(item, decl)
                if lowered is not None:
                    parts.append(lowered)
            return z3.And(*parts) if parts else None

        if kind in {"eq", "lt", "lte", "gt", "gte"}:
            try:
                left = self._lower_arith(expr["left"], decl)
                right = self._lower_arith(expr["right"], decl)
            except ValueError as e:
                self._unsupported(decl, expr, str(e))
                return None
            if kind == "eq":
                constraint = left == right
            elif kind == "lt":
                constraint = left < right
            elif kind == "lte":
                constraint = left <= right
            elif kind == "gt":
                constraint = left > right
            else:
                constraint = left >= right
            self.solver.add(constraint)
            self.asserted_constraints.append({
                "assertion": decl.get("name"),
                "assertion_kind": decl.get("kind"),
                "line_no": decl.get("line_no"),
                "operator": kind,
                "expr": _expr_to_text(expr),
            })
            return constraint

        if kind == "call":
            self._record_relation_call(expr, decl)
            return None

        if kind == "not":
            arg = expr.get("arg")
            if isinstance(arg, dict) and arg.get("kind") == "call":
                self._record_relation_call(arg, decl, negated=True)
                return None
            self._unsupported(decl, expr, "`not` is only ignorable for non-arithmetic relation calls in v1")
            return None

        self._unsupported(decl, expr, f"unsupported boolean expression kind `{kind}`")
        return None

    def _lower_arith(self, expr: dict[str, Any], decl: dict[str, Any]) -> Any:
        kind = expr.get("kind")
        if kind == "ref":
            name = str(expr.get("name") or "")
            if NUMERIC_RE.match(name):
                return _z3_number(name)
            raise ValueError(f"bare non-numeric ref `{name}` cannot be lowered as arithmetic")

        if kind == "call":
            callee = str(expr.get("callee") or "")
            args = expr.get("args") or []
            if callee in VALUE_CALLEES and len(args) == 1 and isinstance(args[0], dict) and args[0].get("kind") == "ref":
                return self._value_var(callee, str(args[0].get("name") or ""))
            raise ValueError(f"call `{_expr_to_text(expr)}` is not a supported numeric value call")

        if kind in {"add", "sub", "mul", "div"}:
            left = self._lower_arith(expr["left"], decl)
            right = self._lower_arith(expr["right"], decl)
            if kind == "add":
                return left + right
            if kind == "sub":
                return left - right
            if kind == "mul":
                return left * right
            return left / right

        raise ValueError(f"expression kind `{kind}` cannot be lowered as arithmetic")

    def _value_var(self, callee: str, entity: str) -> Any:
        key = (callee, entity)
        if key not in self.vars:
            self.vars[key] = z3.Real(_var_name(callee, entity))
        return self.vars[key]

    def _record_relation_call(self, expr: dict[str, Any], decl: dict[str, Any],
                              *, negated: bool = False) -> None:
        callee = str(expr.get("callee") or "")
        args = [_expr_to_text(a) for a in (expr.get("args") or [])]
        if callee == "answer_quantity" and len(args) == 2:
            self.answer_quantity_links.append((args[0], args[1], str(decl.get("name")), decl.get("line_no")))
        self.ignored_non_arithmetic.append({
            "assertion": decl.get("name"),
            "assertion_kind": decl.get("kind"),
            "line_no": decl.get("line_no"),
            "call": f"{'not ' if negated else ''}{callee}({', '.join(args)})",
            "reason": "non-arithmetic relation fact is preserved as context but not asserted into the numeric SMT solver",
        })

    def _unsupported(self, decl: dict[str, Any], expr: dict[str, Any], reason: str) -> None:
        self.unsupported.append(UnsupportedExpr(
            assertion=str(decl.get("name")),
            kind=str(decl.get("kind")),
            reason=reason,
            expr=_expr_to_text(expr),
            line_no=decl.get("line_no"),
        ))


def analyze_entry(entry_dir: pathlib.Path, *, query: str = "auto") -> dict[str, Any]:
    a4v3_p = entry_dir / "main_ir.a4v3"
    if not a4v3_p.exists():
        return {
            "schema": "a4v3_smt_solve_v1",
            "entry_id": entry_dir.name,
            "status": "skipped",
            "reason": "no main_ir.a4v3",
        }

    if not _Z3_AVAILABLE:
        return {
            "schema": "a4v3_smt_solve_v1",
            "entry_id": entry_dir.name,
            "status": "z3_unavailable",
            "z3_available": False,
            "reason": "z3 package is not installed",
        }

    text = a4v3_p.read_text(encoding="utf-8")
    try:
        ast = parser.parse(text, strict=True)
    except Exception as e:
        return {
            "schema": "a4v3_smt_solve_v1",
            "entry_id": entry_dir.name,
            "status": "parse_error",
            "z3_available": True,
            "reason": str(e),
        }

    lowerer = ArithmeticLowerer()
    assertions = [d for d in ast.get("assertions", []) if d.get("kind") in ASSERTION_KINDS]
    for decl in assertions:
        lowerer.lower_assertion(decl)

    check = lowerer.solver.check()
    result: dict[str, Any] = {
        "schema": "a4v3_smt_solve_v1",
        "entry_id": entry_dir.name,
        "status": str(check),
        "z3_available": True,
        "query_mode": query,
        "assertions_total": len(assertions),
        "asserted_numeric_constraints_count": len(lowerer.asserted_constraints),
        "asserted_numeric_constraints": lowerer.asserted_constraints,
        "ignored_non_arithmetic_count": len(lowerer.ignored_non_arithmetic),
        "ignored_non_arithmetic": lowerer.ignored_non_arithmetic,
        "unsupported_assertions_count": len(lowerer.unsupported),
        "unsupported_assertions": [u.__dict__ for u in lowerer.unsupported],
        "answer_quantity_links": [
            {"answer": a, "quantity": q, "assertion": decl, "line_no": line}
            for a, q, decl, line in lowerer.answer_quantity_links
        ],
        "queries": [],
    }

    if check != z3.sat:
        return result

    query_specs = _select_queries(lowerer, query)
    if not query_specs:
        result["status"] = "no_query_found"
        result["reason"] = "No answer_value(...) query or answer_quantity(...) fallback was found."
        return result

    model = lowerer.solver.model()
    result["queries"] = [
        _evaluate_query(lowerer, model, qkind, entity, source)
        for qkind, entity, source in query_specs
    ]
    if lowerer.unsupported:
        result["status"] = "sat_partial"
    return result


def _select_queries(lowerer: ArithmeticLowerer, query: str) -> list[tuple[str, str, str]]:
    if query == "auto":
        answer_entities = sorted(entity for callee, entity in lowerer.vars if callee == "answer_value")
        if answer_entities:
            return [("answer_value", e, "explicit_answer_value") for e in answer_entities]
        seen: set[str] = set()
        out = []
        for answer, quantity, _, _ in lowerer.answer_quantity_links:
            if quantity in seen:
                continue
            seen.add(quantity)
            lowerer._value_var("quantity_value", quantity)
            out.append(("quantity_value", quantity, f"answer_quantity({answer}, {quantity})"))
        return out

    if query == "all":
        return [(callee, entity, "all") for callee, entity in sorted(lowerer.vars)]

    if m := QUERY_RE.match(query):
        callee, entity = m.group(1), m.group(2)
        lowerer._value_var(callee, entity)
        return [(callee, entity, "explicit_cli_query")]

    raise ValueError(f"Unsupported query syntax: {query}")


def _evaluate_query(lowerer: ArithmeticLowerer, model: Any, callee: str,
                    entity: str, source: str) -> dict[str, Any]:
    var = lowerer._value_var(callee, entity)
    value = model.eval(var, model_completion=True)
    uniqueness = _check_unique(lowerer, var, value)
    unique = bool(uniqueness["unique"])
    return {
        "query": f"{callee}({entity})",
        "source": source,
        "status": "unique" if unique else "underdetermined",
        "value_rational": _z3_value_rational(value) if unique else None,
        "value_decimal": _z3_value_decimal(value) if unique else None,
        "sample_value_rational": _z3_value_rational(value),
        "sample_value_decimal": _z3_value_decimal(value),
        "unique": unique,
        "uniqueness_status": uniqueness["status"],
    }


def _check_unique(lowerer: ArithmeticLowerer, var: Any, value: Any) -> dict[str, Any]:
    s = z3.Solver()
    s.set("timeout", 5000)
    for assertion in lowerer.solver.assertions():
        s.add(assertion)
    s.add(var != value)
    status = s.check()
    return {"status": str(status), "unique": status == z3.unsat}


def _z3_number(text: str) -> Any:
    if text.endswith("%"):
        frac = Fraction(text[:-1]) / 100
    else:
        frac = Fraction(text)
    if frac.denominator == 1:
        return z3.RealVal(str(frac.numerator))
    return z3.RealVal(f"{frac.numerator}/{frac.denominator}")


def _z3_value_rational(value: Any) -> str:
    if hasattr(value, "numerator_as_long") and hasattr(value, "denominator_as_long"):
        num = value.numerator_as_long()
        den = value.denominator_as_long()
        return str(num) if den == 1 else f"{num}/{den}"
    return str(value)


def _z3_value_decimal(value: Any) -> float | str:
    rat = _z3_value_rational(value)
    try:
        return float(Fraction(rat))
    except Exception:
        if hasattr(value, "as_decimal"):
            return value.as_decimal(20)
        return str(value)


def _var_name(callee: str, entity: str) -> str:
    return f"{callee}__{entity}"


def _expr_to_text(expr: Any) -> str:
    if not isinstance(expr, dict):
        return str(expr)
    kind = expr.get("kind")
    if kind == "ref":
        return str(expr.get("name") or "")
    if kind == "call":
        args = ", ".join(_expr_to_text(a) for a in expr.get("args") or [])
        return f"{expr.get('callee')}({args})"
    if kind in {"add", "sub", "mul", "div", "eq", "lt", "lte", "gt", "gte"}:
        op = {
            "add": "+", "sub": "-", "mul": "*", "div": "/",
            "eq": "=", "lt": "<", "lte": "<=", "gt": ">", "gte": ">=",
        }[kind]
        return f"({_expr_to_text(expr.get('left'))} {op} {_expr_to_text(expr.get('right'))})"
    if kind == "and":
        return " and ".join(_expr_to_text(a) for a in expr.get("args") or [])
    if kind == "not":
        return f"not {_expr_to_text(expr.get('arg'))}"
    return json.dumps(expr, ensure_ascii=False, sort_keys=True)


def _write_entry(entry_dir: pathlib.Path, result: dict[str, Any]) -> pathlib.Path:
    json_p = entry_dir / "metrics_smt_solve_v1.json"
    md_p = entry_dir / "metrics_smt_solve_v1.md"
    json_p.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    md_p.write_text(_render_md(result), encoding="utf-8")
    return json_p


def _render_md(result: dict[str, Any]) -> str:
    lines = [
        f"# SMT Solve v1 - {result.get('entry_id', '?')}",
        "",
        f"- status: `{result.get('status')}`",
        f"- z3_available: `{result.get('z3_available')}`",
        f"- query_mode: `{result.get('query_mode', '')}`",
        f"- asserted_numeric_constraints_count: `{result.get('asserted_numeric_constraints_count', 0)}`",
        f"- ignored_non_arithmetic_count: `{result.get('ignored_non_arithmetic_count', 0)}`",
        f"- unsupported_assertions_count: `{result.get('unsupported_assertions_count', 0)}`",
        "",
        "## Queries",
        "",
    ]
    queries = result.get("queries") or []
    if queries:
        lines.append("| query | value | decimal | unique |")
        lines.append("|---|---:|---:|---|")
        for q in queries:
            lines.append(
                f"| `{q.get('query')}` | `{q.get('value_rational')}` | "
                f"`{q.get('value_decimal')}` | `{q.get('unique')}` |"
            )
    else:
        lines.append("- none")
    lines.append("")
    if result.get("unsupported_assertions"):
        lines.extend(["## Unsupported Assertions", ""])
        for item in result["unsupported_assertions"]:
            lines.append(f"- `{item.get('assertion')}` line `{item.get('line_no')}`: {item.get('reason')} — `{item.get('expr')}`")
        lines.append("")
    return "\n".join(lines)


def _print_summary(result: dict[str, Any]) -> None:
    print(
        f"  status={result.get('status')} "
        f"constraints={result.get('asserted_numeric_constraints_count', 0)} "
        f"queries={len(result.get('queries') or [])} "
        f"unsupported={result.get('unsupported_assertions_count', 0)}"
    )
    for q in result.get("queries") or []:
        print(
            f"    {q['query']} = {q['value_rational']} "
            f"({q['value_decimal']}) status={q['status']} unique={q['unique']}"
        )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("target", nargs="?", default=str(ROOT / "IR/outputs/runs/unified_methodology_v1"))
    ap.add_argument("--query", default="auto",
                    help="auto, all, answer_value(Name), or quantity_value(Name)")
    args = ap.parse_args()

    target = pathlib.Path(args.target)
    if (target / "main_ir.a4v3").exists() or (target / "source.md").exists():
        result = analyze_entry(target, query=args.query)
        out = _write_entry(target, result)
        print(f"Wrote {out}")
        _print_summary(result)
        return

    n = 0
    solved = 0
    for ir in sorted(target.rglob("main_ir.a4v3")):
        entry_dir = ir.parent
        if entry_dir.name.startswith("_"):
            continue
        result = analyze_entry(entry_dir, query=args.query)
        _write_entry(entry_dir, result)
        n += 1
        if result.get("queries"):
            solved += 1
    print(f"Processed {n} entries; {solved} produced at least one query value.")


if __name__ == "__main__":
    main()
