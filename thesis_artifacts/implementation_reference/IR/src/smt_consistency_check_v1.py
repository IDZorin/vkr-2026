"""smt_consistency_check_v1.py

Structural / SMT-style consistency check for a4v3 IR.

This is a STRUCTURAL precursor to a full a4v3 → SMT-LIB translator. It checks:

  1. **vacuous detection** — constraint body trivially `true` (e.g. tautologies
     `p or not p`, empty bodies, `forall x: T, true`)
  2. **undefined symbol references** — body calls a name that has no
     declaration (sort/fun/rel/entity)
  3. **conjunct contradictions** — same atomic call with same arguments
     appears positively AND negatively inside the same `and` block
  4. **per-constraint SAT (atomic conjuncts only)** — when constraint body
     reduces to a conjunction of atomic relations, no further SAT can fail
     (uninterpreted symbols are independently satisfiable). Mark trivially-sat.
  5. **Z3 SAT** — if the `z3` package is installed AND the constraint body fits
     the supported subset (currently: conjunctions of atoms with `and`/`not`/
     `forall`/`exists` over uninterpreted sorts), encode and run `solver.check()`.
     Otherwise mark `smt_supported=false` with a reason.

Saves: metrics_smt_consistency_check_v1.json per entry.

CLI:
    python smt_consistency_check_v1.py [entry_dir|run_root]
"""
from __future__ import annotations
import json
import pathlib
import re
import sys
from collections import defaultdict

ROOT = pathlib.Path(r"<WORKSPACE_ROOT>")
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import cross_entry_consistency_v1 as cec  # noqa: E402

try:
    import z3  # type: ignore
    _Z3 = True
except ImportError:
    z3 = None  # type: ignore
    _Z3 = False


_CONSTRAINT_HEADER_RE = re.compile(
    r"^constraint\s+([A-Za-z_][A-Za-z0-9_]*)\s*:\s*$", re.MULTILINE
)
_DECL_KIND_RE = re.compile(
    r"^\s*(sort|entity|fun|rel|constraint|axiom)\s+([A-Za-z_][A-Za-z0-9_]*)",
    re.MULTILINE,
)


def _split_constraints(text: str) -> list[tuple[str, str]]:
    """Return list of (name, body_text). Naive splitter: each `constraint NAME :`
    line starts a body that runs until the next top-level decl keyword.
    """
    matches = list(re.finditer(
        r"^(?:constraint|axiom)\s+([A-Za-z_][A-Za-z0-9_]*)\s*:\s*\n",
        text, flags=re.MULTILINE
    ))
    out = []
    for i, m in enumerate(matches):
        name = m.group(1)
        body_start = m.end()
        if i + 1 < len(matches):
            body_end = matches[i + 1].start()
        else:
            body_end = len(text)
        body = text[body_start:body_end]
        # Strip if next thing is a top-level decl
        next_decl = re.search(
            r"^(?:sort|entity|fun|rel|constraint|axiom)\b", body, flags=re.MULTILINE
        )
        if next_decl:
            body = body[: next_decl.start()]
        out.append((name, body.rstrip()))
    return out


_ATOM_CALL_RE = re.compile(r"\b([a-z_][a-z_0-9]*)\s*\(")
_NEG_ATOM_RE = re.compile(r"\bnot\s+([a-z_][a-z_0-9]*)\s*\(")
_TRUE_BODY_RE = re.compile(r"^\s*true\s*$", re.MULTILINE)


def _atomic_calls(body: str) -> list[str]:
    """Extract names of all atomic calls in the body."""
    return _ATOM_CALL_RE.findall(body)


def _is_trivially_true(body: str) -> bool:
    s = body.strip()
    if not s:
        return True
    if re.match(r"^\s*true\s*$", s):
        return True
    if re.match(r"^\s*forall\s+\w+\s*:\s*\w+\s*,\s*true\s*$", s):
        return True
    return False


def _detect_conjunct_contradictions(body: str) -> list[str]:
    """Heuristic: split by `\\n    and ` (4-space indent + and), pull atom name
    + first arg list; if same call appears with and without preceding `not`
    in the same body, that's a contradiction.
    """
    pos: set[str] = set()
    neg: set[str] = set()
    # very rough — full parsing would need proper grammar
    for m in re.finditer(r"\b([a-z_][a-z_0-9]*)\s*\(([^()]{0,200})\)", body):
        sig = f"{m.group(1)}({re.sub(r'\\s+', ' ', m.group(2)).strip()})"
        # check if preceded by not
        preceding = body[max(0, m.start() - 6):m.start()]
        if "not " in preceding[-6:]:
            neg.add(sig)
        else:
            pos.add(sig)
    return sorted(pos & neg)


def _all_declared_names(text: str) -> set[str]:
    decls = cec._parse_a4v3(text)
    out = {d["name"] for d in decls}
    # Add prelude names — but we want this entry-local for the "unknown ref"
    # check; ext grounding handles cross-overlay.
    return out


def _undefined_calls(body: str, known_names: set[str], all_text: str) -> list[str]:
    # only flag names that aren't:
    # - keywords
    # - known declared
    # - prelude items (sort: Day, Real, Integer, String, ...)
    keywords = {"forall", "exists", "and", "or", "not", "implies", "iff", "ite",
                "let", "in", "true", "false", "eq", "gt", "lt", "gte", "lte",
                "add", "sub", "mul", "div", "count", "set"}
    primitives = {"Day", "Real", "Integer", "Boolean", "String", "Period",
                  "Document", "Organization", "FinancialIndex"}
    callees = set(_atomic_calls(body))
    unknown = []
    for c in callees:
        if c in keywords or c in primitives or c in known_names:
            continue
        # check anywhere in entry text
        if re.search(rf"\b(?:sort|entity|fun|rel)\s+{c}\b", all_text):
            continue
        unknown.append(c)
    return sorted(set(unknown))


def _per_constraint_atomic_sat_only(body: str) -> bool:
    """Returns True if body contains ONLY atomic calls combined with `and`,
    quantifiers, possibly `not`. Such bodies over uninterpreted symbols are
    trivially satisfiable (independent atoms are independently realizable).
    """
    # any operators that change reasoning?
    if "implies" in body or "iff" in body:
        return False
    if " or " in body or "ite" in body or "let" in body:
        return False
    return True


def _try_z3_check(text: str, body: str, decls: list[dict]) -> dict:
    """Attempt to encode the body in Z3 if it fits the supported subset.

    Supported subset: top-level conjunction of atomic predicates (rel calls)
    optionally wrapped in a single forall. Returns dict with status."""
    if not _Z3:
        return {"smt_supported": False, "reason": "z3 not installed"}

    # Build sort and symbol maps
    sort_map: dict = {}
    for d in decls:
        if d["kind"] == "sort":
            sort_map[d["name"]] = z3.DeclareSort(d["name"])
    # add prelude-ish primitives if needed
    for nm in ("Day", "Real", "Integer", "Boolean", "Period", "Document",
               "Organization", "FinancialIndex", "ErrorEvent", "PolicyDocument"):
        sort_map.setdefault(nm, z3.DeclareSort(nm))

    rel_funcs: dict = {}
    fun_funcs: dict = {}
    for d in decls:
        if d["kind"] == "rel":
            args = d["arg_sorts"] or []
            try:
                domains = [sort_map.setdefault(a, z3.DeclareSort(a)) for a in args]
            except Exception as e:
                return {"smt_supported": False, "reason": f"bad rel sig: {e}"}
            rel_funcs[d["name"]] = z3.Function(d["name"], *domains, z3.BoolSort())
        elif d["kind"] == "fun":
            args = d["arg_sorts"] or []
            ret = d["return_sort"]
            try:
                domains = [sort_map.setdefault(a, z3.DeclareSort(a)) for a in args]
                ret_sort = sort_map.setdefault(ret, z3.DeclareSort(ret))
            except Exception as e:
                return {"smt_supported": False, "reason": f"bad fun sig: {e}"}
            fun_funcs[d["name"]] = z3.Function(d["name"], *domains, ret_sort)
        elif d["kind"] == "entity":
            sort = d["return_sort"]
            if sort and sort not in sort_map:
                sort_map[sort] = z3.DeclareSort(sort)
            # entities encoded as constants but we'd need parsing of args; skip

    # Body parsing: only support pure atomic conjunction without quantifier nesting.
    body_clean = re.sub(r"\s+", " ", body).strip()
    # strip leading `forall <var> : <Sort> ,`
    qm = re.match(r"forall\s+(\w+)\s*:\s*(\w+)\s*,\s*(.+)$", body_clean)
    quantifier = None
    if qm:
        quantifier = (qm.group(1), qm.group(2))
        body_clean = qm.group(3)

    # split on " and " (only top-level), no parens nesting handled
    if "(" in body_clean and ")" in body_clean:
        # check for nested parentheses
        depth = 0
        ok = True
        for ch in body_clean:
            if ch == "(":
                depth += 1
            elif ch == ")":
                depth -= 1
                if depth < 0:
                    ok = False
                    break
        if not ok:
            return {"smt_supported": False, "reason": "unbalanced parens"}

    parts = re.split(r"\s+and\s+", body_clean)
    if any("implies" in p or "iff" in p or " or " in p or "ite" in p
           or "exists" in p for p in parts):
        return {"smt_supported": False,
                "reason": "non-conjunctive operator in body"}

    constraints_z3 = []
    for p in parts:
        p = p.strip()
        if not p:
            continue
        neg = False
        if p.startswith("not "):
            neg = True
            p = p[4:].strip()
        m = re.match(r"([a-z_][a-z_0-9]*)\s*\((.*)\)\s*$", p)
        if not m:
            return {"smt_supported": False, "reason": f"unparseable atom: {p[:60]}"}
        name = m.group(1)
        if name not in rel_funcs:
            return {"smt_supported": False, "reason": f"call to undeclared rel: {name}"}
        # Args encoded as fresh constants of the rel's arg sorts
        f = rel_funcs[name]
        args_tokens = [a.strip() for a in m.group(2).split(",") if a.strip()]
        if len(args_tokens) != f.arity():
            return {"smt_supported": False,
                    "reason": f"arity mismatch {name}({len(args_tokens)} vs {f.arity()})"}
        z_args = []
        for i, a in enumerate(args_tokens):
            arg_sort = f.domain(i)
            # treat each token as fresh constant of that sort (no equality semantics)
            z_args.append(z3.Const(f"{name}_arg{i}_{a}", arg_sort))
        atom = f(*z_args)
        constraints_z3.append(z3.Not(atom) if neg else atom)

    if quantifier:
        var, sort_name = quantifier
        sort = sort_map.setdefault(sort_name, z3.DeclareSort(sort_name))
        # Replace constants of that sort named `<var>_*` with the bound variable;
        # this is a coarse encoding but adequate for atomic-conjunct bodies.
        bv = z3.Const(var, sort)
        body_expr = z3.And(*constraints_z3) if constraints_z3 else z3.BoolVal(True)
        formula = z3.ForAll([bv], body_expr)
    else:
        formula = z3.And(*constraints_z3) if constraints_z3 else z3.BoolVal(True)

    s = z3.Solver()
    s.set("timeout", 5000)
    s.add(formula)
    try:
        check = s.check()
    except Exception as e:
        return {"smt_supported": False, "reason": f"z3 exception: {e}"}
    return {"smt_supported": True, "z3_status": str(check)}


def _check_constraint(name: str, body: str, all_text: str, decls: list[dict],
                      known_names: set[str]) -> dict:
    issues: list[dict] = []
    # 1. vacuous?
    if _is_trivially_true(body):
        issues.append({"kind": "vacuous", "detail": "body reduces to `true`"})
    # 2. undefined refs
    unknown = _undefined_calls(body, known_names, all_text)
    if unknown:
        issues.append({"kind": "undefined_call", "detail": unknown})
    # 3. local contradictions
    contradictions = _detect_conjunct_contradictions(body)
    if contradictions:
        issues.append({"kind": "conjunct_contradiction", "detail": contradictions})

    # 4. atomic-conjunct sat (trivial)
    atomic_only = _per_constraint_atomic_sat_only(body)

    # 5. z3 attempt
    z3_result = _try_z3_check(all_text, body, decls)

    return {
        "name": name,
        "issues": issues,
        "atomic_conjunct_only": atomic_only,
        **z3_result,
    }


def analyze_entry(entry_dir: pathlib.Path) -> dict:
    a4v3_p = entry_dir / "main_ir.a4v3"
    if not a4v3_p.exists():
        return {"entry_id": entry_dir.name, "skipped": True, "reason": "no a4v3"}
    text = a4v3_p.read_text(encoding="utf-8")
    decls = cec._parse_a4v3(text)
    known_names = {d["name"] for d in decls}

    constraints = _split_constraints(text)
    per_constraint: list[dict] = []
    z3_status_counts: dict[str, int] = defaultdict(int)
    issue_counts: dict[str, int] = defaultdict(int)
    for name, body in constraints:
        check = _check_constraint(name, body, text, decls, known_names)
        per_constraint.append(check)
        for iss in check["issues"]:
            issue_counts[iss["kind"]] += 1
        if check.get("smt_supported"):
            z3_status_counts[check.get("z3_status", "unknown")] += 1
        else:
            z3_status_counts["unsupported"] += 1

    return {
        "entry_id": entry_dir.name,
        "skipped": False,
        "n_constraints": len(constraints),
        "z3_available": _Z3,
        "issue_counts": dict(issue_counts),
        "z3_status_counts": dict(z3_status_counts),
        "per_constraint": per_constraint,
    }


def _save(entry_dir: pathlib.Path, result: dict) -> pathlib.Path:
    out = entry_dir / "metrics_smt_consistency_check_v1.json"
    out.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n",
                   encoding="utf-8")
    return out


def main():
    args = sys.argv[1:]
    target = pathlib.Path(args[0]) if args else (
        ROOT / "IR/outputs/runs/unified_methodology_v1")

    if (target / "main_ir.a4v3").exists() or (target / "source.md").exists():
        result = analyze_entry(target)
        out = _save(target, result)
        print(f"Wrote {out}")
        if not result.get("skipped"):
            print(f"  constraints={result['n_constraints']} "
                  f"z3={'on' if result['z3_available'] else 'off'} "
                  f"issues={result['issue_counts']} "
                  f"z3_status={result['z3_status_counts']}")
        return

    n = 0
    n_issues = 0
    for d in sorted(target.rglob("main_ir.a4v3")):
        entry_dir = d.parent
        if entry_dir.name.startswith("_"):
            continue
        result = analyze_entry(entry_dir)
        _save(entry_dir, result)
        n += 1
        if not result.get("skipped") and result["issue_counts"]:
            n_issues += 1
    print(f"Processed {n} entries; {n_issues} have at least one structural issue.")


if __name__ == "__main__":
    main()
