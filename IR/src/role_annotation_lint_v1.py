"""role_annotation_lint_v1.py

Deterministic lint for optional financial methodology role/frame annotations.

This checker is intentionally dormant unless an entry contains
``role_annotations.yaml``. When the file exists, it validates that the
annotation layer is mechanically consistent with ``main_ir.a4v3``:

- annotated symbols exist in A4V3;
- declared symbol kind and arity match;
- roles come from the approved role vocabulary;
- high-arity relations and functions are covered;
- constraint frame annotations reference existing constraints and variables.

Outputs:
  <entry>/role_annotation_lint_v1.json
  <entry>/role_annotation_lint_v1.md

CLI:
  python role_annotation_lint_v1.py [entry_dir|run_root]
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
from collections import Counter
from datetime import datetime
from typing import Any

import yaml


ROLE_ANNOTATION_FILE = "role_annotations.yaml"

# Deliberately broad v1 role vocabulary. It is still finite and machine
# checkable, but permissive enough for current financial methodology relation/function patterns.
APPROVED_ROLES = {
    "actor",
    "affected",
    "agent",
    "amount",
    "attribute",
    "basis",
    "beneficiary",
    "candidate",
    "cause",
    "component",
    "condition",
    "container",
    "content",
    "context",
    "currency",
    "calculation_time",
    "day",
    "dependent",
    "destination",
    "effect",
    "earlier_time",
    "event",
    "evidence",
    "exchange",
    "definition",
    "dimension",
    "formula",
    "input",
    "instrument",
    "index_variable",
    "kind",
    "level",
    "location",
    "later_time",
    "object",
    "output",
    "owner",
    "part",
    "policy",
    "predicate",
    "price",
    "qualifier",
    "quality",
    "purpose",
    "rate",
    "reason",
    "recipient",
    "reference",
    "result",
    "return",
    "same_as_type",
    "scope",
    "selected",
    "source",
    "state",
    "subject",
    "target",
    "time",
    "time_of_day",
    "timezone",
    "topic",
    "value",
}

TOP_LEVEL_RE = re.compile(
    r"^\s*(sort|entity|rel|fun|fact|constraint|obligation|permission|"
    r"prohibition|val|enum)\b"
)
NAME_RE = re.compile(
    r"^\s*(?P<kind>sort|entity|rel|fun|fact|constraint|obligation|permission|"
    r"prohibition|val|enum)(?:\[[^\]]+\])?\s+"
    r"(?P<name>[A-Za-z_][A-Za-z0-9_]*)\b"
)
SORT_EXTENDS_RE = re.compile(
    r"^\s*sort\s+(?P<name>[A-Za-z_][A-Za-z0-9_]*)\s+extends\s+"
    r"(?P<parent>[A-Za-z_][A-Za-z0-9_]*)\b"
)
COMPLEX_FRAME_RE = re.compile(
    r"\b(forall|exists|implies|iff)\b|<=|>=|"
    r"(?<![-A-Za-z0-9_])<(?!=)|(?<![-A-Za-z0-9_])>(?!=)|"
    r"\b(based_on|derived_from|proportional|rank|top|before|after|"
    r"prior_to|until|selected|current|primary|unique|exactly|at_most|"
    r"at_least)\b|[+*/]"
)
QUANT_VAR_RE = re.compile(r"\b(?:forall|exists)\s+([A-Za-z_][A-Za-z0-9_]*)\s*:")
QUANT_VAR_WITH_KIND_RE = re.compile(
    r"\b(?P<kind>forall|exists)\s+(?P<var>[A-Za-z_][A-Za-z0-9_]*)\s*:"
    r"\s*(?P<type>[A-Za-z_][A-Za-z0-9_]*)"
)
CALL_RE = re.compile(r"\b([A-Za-z_][A-Za-z0-9_]*)\s*\(")
CAMEL_TOKEN_RE = re.compile(r"[A-Z]+(?=[A-Z][a-z]|$)|[A-Z]?[a-z]+|\d+")


BUILTIN_SORT_PARENTS = {
    "TradingDay": "Day",
    "CalculationDay": "Day",
    "BusinessDay": "Day",
    "SelectionDay": "Day",
    "FixingDay": "Day",
    "RebalanceDay": "Day",
    "RegularRebalanceDay": "RebalanceDay",
    "EffectiveDay": "Day",
    "DocumentPart": "Document",
    "Url": "WebResource",
    "Percent": "Real",
    "MonetaryAmount": "Real",
}

ROLE_BY_BASE_SORT = {
    "Day": "day",
    "Period": "time",
    "Event": "event",
    "Organization": "agent",
    "Document": "reference",
    "WebResource": "reference",
    "Real": "value",
    "Nat": "value",
    "Currency": "currency",
    "Exchange": "exchange",
    "VagueTerm": "qualifier",
    "Index": "subject",
    "FinancialInstrument": "instrument",
    "Security": "instrument",
    "Rate": "rate",
}

ROLE_TOKEN_PRIORITY = [
    ({"context"}, "context"),
    ({"possibility"}, "condition"),
    ({"period", "interval", "time"}, "time"),
    ({"kind", "classification", "category", "type", "subindustry", "industry", "sector", "class"}, "kind"),
    ({"definition"}, "definition"),
    ({"list"}, "container"),
    ({"attribute"}, "attribute"),
    ({"variable"}, "index_variable"),
    ({"component"}, "component"),
    ({"exchange"}, "exchange"),
    ({"currency"}, "currency"),
    ({"price"}, "price"),
    ({"rate", "fixing"}, "rate"),
    ({"level"}, "level"),
    ({"effect"}, "effect"),
    ({"quality"}, "quality"),
    ({"reason"}, "reason"),
    ({"basis", "assumption", "factor"}, "basis"),
    ({"purpose", "use"}, "purpose"),
    ({"document", "section", "policy", "guideline", "methodology", "website", "url", "table", "column", "appendix", "notice"}, "reference"),
    ({"administrator", "organization", "committee", "provider", "bank", "house"}, "agent"),
    ({"shares"}, "value"),
    ({"share", "security", "instrument", "listing", "license"}, "instrument"),
    ({"action", "adjustment", "deviation", "calculation", "termination", "announcement", "rebalance", "trade", "error", "review", "modification", "change", "determination", "endeavor"}, "event"),
    ({"amount", "capitalization", "value", "number", "count", "percent", "percentage", "weight", "level", "float", "fee"}, "value"),
    ({"index"}, "subject"),
]


def _read_text(path: pathlib.Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="replace")


def _load_yaml(path: pathlib.Path) -> tuple[dict[str, Any], str | None]:
    if not path.exists():
        return {}, None
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except Exception as exc:
        return {}, f"{type(exc).__name__}: {exc}"
    if not isinstance(data, dict):
        return {}, "top-level YAML value must be a mapping"
    return data, None


def _entry_dirs(target: pathlib.Path) -> list[pathlib.Path]:
    target = target.resolve()
    if (target / "main_ir.a4v3").exists() or (target / ROLE_ANNOTATION_FILE).exists():
        return [target]
    return [
        p.parent
        for p in sorted(target.rglob(ROLE_ANNOTATION_FILE))
        if (p.parent / "main_ir.a4v3").exists()
        and not p.parent.name.startswith("_")
    ]


def _strip_comments(text: str) -> str:
    return "\n".join(line.split("--", 1)[0] for line in text.splitlines())


def _blocks(a4v3_text: str) -> list[tuple[str, str, str]]:
    lines = a4v3_text.splitlines()
    out: list[tuple[str, str, str]] = []
    i = 0
    while i < len(lines):
        m = TOP_LEVEL_RE.match(lines[i])
        if not m:
            i += 1
            continue
        kind = m.group(1)
        j = i + 1
        while j < len(lines) and not TOP_LEVEL_RE.match(lines[j]):
            j += 1
        block = "\n".join(lines[i:j])
        nm = NAME_RE.match(block)
        name = nm.group("name") if nm else f"@line_{i + 1}"
        out.append((kind, name, block))
        i = j
    return out


def _split_signature_args(signature: str) -> list[str]:
    signature = _strip_comments(signature).replace("\n", " ")
    return [part.strip() for part in signature.split(",") if part.strip()]


def _parse_a4v3(a4v3_text: str) -> dict[str, Any]:
    symbols: dict[str, dict[str, Any]] = {}
    constraints: dict[str, str] = {}
    facts: dict[str, str] = {}
    deontics: dict[str, str] = {}
    sort_parents: dict[str, str] = dict(BUILTIN_SORT_PARENTS)
    for kind, name, block in _blocks(a4v3_text):
        if kind == "sort":
            m_ext = SORT_EXTENDS_RE.match(block)
            if m_ext:
                sort_parents[m_ext.group("name")] = m_ext.group("parent")
        if kind == "rel":
            sig = block.split(":", 1)[1] if ":" in block else ""
            args = _split_signature_args(sig)
            symbols[name] = {"kind": "rel", "arity": len(args), "args": args}
        elif kind == "fun":
            sig = block.split(":", 1)[1] if ":" in block else ""
            left, _, right = sig.partition("->")
            args = _split_signature_args(left)
            symbols[name] = {
                "kind": "fun",
                "arity": len(args),
                "args": args,
                "return": _strip_comments(right).strip(),
            }
        elif kind == "constraint":
            constraints[name] = block
        elif kind == "fact":
            facts[name] = block
        elif kind in {"obligation", "permission", "prohibition"}:
            deontics[name] = kind
        else:
            symbols.setdefault(name, {"kind": kind, "arity": None, "args": []})
    return {
        "symbols": symbols,
        "constraints": constraints,
        "facts": facts,
        "deontics": deontics,
        "sort_parents": sort_parents,
    }


def _identifier_tokens(text: str) -> set[str]:
    out: set[str] = set()
    for part in re.split(r"[^A-Za-z0-9]+", text or ""):
        if not part:
            continue
        out.update(token.lower() for token in CAMEL_TOKEN_RE.findall(part))
    return out


def _sort_ancestors(type_name: str, sort_parents: dict[str, str]) -> list[str]:
    out: list[str] = []
    seen: set[str] = set()
    cur = re.sub(r"[^A-Za-z0-9_].*$", "", (type_name or "").strip())
    while cur and cur not in seen:
        seen.add(cur)
        out.append(cur)
        cur = sort_parents.get(cur, "")
    return out


def _expected_role_for_type(type_name: str, sort_parents: dict[str, str]) -> str | None:
    ancestors = _sort_ancestors(type_name, sort_parents)
    ancestor_set = set(ancestors)

    if "Day" in ancestor_set:
        return "day"
    if "Period" in ancestor_set:
        return "time"
    if "Event" in ancestor_set:
        return "event"

    tokens: set[str] = set()
    for name in ancestors or [type_name]:
        tokens.update(_identifier_tokens(name))
    for trigger_tokens, role in ROLE_TOKEN_PRIORITY:
        if tokens & trigger_tokens:
            return role
    for base, role in ROLE_BY_BASE_SORT.items():
        if base in ancestor_set:
            return role
    return None


def _validate_type_role_alignment(
    *,
    role: str | None,
    type_name: str,
    location: str,
    findings: list[dict[str, Any]],
    sort_parents: dict[str, str],
) -> None:
    if not role:
        return
    expected = _expected_role_for_type(type_name, sort_parents)
    if not expected or role == expected:
        return
    findings.append({
        "check": "role_type_alignment_mismatch",
        "severity": "soft",
        "location": location,
        "role": role,
        "expected_role": expected,
        "type": type_name,
        "reason": "role annotation does not match the declared A4V3 type.",
    })


def _role_from_value(value: Any) -> str | None:
    if isinstance(value, str):
        return value
    if isinstance(value, dict):
        role = value.get("role")
        if isinstance(role, str):
            return role
    return None


def _normalize_arg_roles(raw: Any) -> list[dict[str, Any]]:
    if isinstance(raw, list):
        return [item if isinstance(item, dict) else {"role": item} for item in raw]
    if isinstance(raw, dict):
        items: list[tuple[int, Any]] = []
        for key, value in raw.items():
            try:
                index = int(key)
            except Exception:
                continue
            items.append((index, value))
        return [
            value if isinstance(value, dict) else {"role": value}
            for _, value in sorted(items)
        ]
    return []


def _collect_symbol_annotations(data: dict[str, Any]) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    symbols = data.get("symbols")
    if isinstance(symbols, dict):
        for name, spec in symbols.items():
            if isinstance(spec, dict):
                out[str(name)] = dict(spec)
    relations = data.get("relations")
    if isinstance(relations, dict):
        for name, spec in relations.items():
            if isinstance(spec, dict):
                item = dict(spec)
                item.setdefault("kind", "rel")
                out[str(name)] = item
    functions = data.get("functions")
    if isinstance(functions, dict):
        for name, spec in functions.items():
            if isinstance(spec, dict):
                item = dict(spec)
                item.setdefault("kind", "fun")
                out[str(name)] = item
    return out


def _collect_constraint_annotations(data: dict[str, Any]) -> dict[str, dict[str, Any]]:
    constraints = data.get("constraints")
    if not isinstance(constraints, dict):
        return {}
    return {
        str(name): spec
        for name, spec in constraints.items()
        if isinstance(spec, dict)
    }


def _collect_fact_annotations(data: dict[str, Any]) -> dict[str, dict[str, Any]]:
    facts = data.get("facts")
    if not isinstance(facts, dict):
        return {}
    return {
        str(name): spec
        for name, spec in facts.items()
        if isinstance(spec, dict)
    }


def _validate_role(
    *,
    role: str | None,
    location: str,
    findings: list[dict[str, Any]],
) -> None:
    if not role:
        findings.append({
            "check": "missing_role",
            "severity": "strong",
            "location": location,
            "reason": "role annotation item has no role value.",
        })
        return
    if role not in APPROVED_ROLES:
        findings.append({
            "check": "unknown_role_token",
            "severity": "strong",
            "location": location,
            "role": role,
            "reason": "role token is not in the approved role prelude vocabulary.",
        })


def _validate_variable_spec(
    *,
    formula_name: str,
    var_name: str,
    var_spec: Any,
    block: str,
    severity_for_unquantified: str,
    findings: list[dict[str, Any]],
    sort_parents: dict[str, str],
) -> None:
    quantified = set(QUANT_VAR_RE.findall(block))
    quantifier_by_var = {
        match.group("var"): match.group("kind")
        for match in QUANT_VAR_WITH_KIND_RE.finditer(block)
    }
    type_by_var = {
        match.group("var"): match.group("type")
        for match in QUANT_VAR_WITH_KIND_RE.finditer(block)
    }
    var_text = str(var_name)
    if var_text not in block:
        findings.append({
            "check": "formula_annotation_variable_not_in_formula",
            "severity": "strong",
            "formula": formula_name,
            "variable": var_text,
            "reason": "annotated variable does not occur in the formula body.",
        })
    elif quantified and var_text not in quantified:
        findings.append({
            "check": "formula_annotation_variable_not_quantified",
            "severity": severity_for_unquantified,
            "formula": formula_name,
            "variable": var_text,
            "reason": "annotated variable occurs but is not introduced by forall/exists.",
        })
    _validate_role(
        role=_role_from_value(var_spec),
        location=f"{formula_name}.variables.{var_name}",
        findings=findings,
    )
    if var_text in type_by_var:
        _validate_type_role_alignment(
            role=_role_from_value(var_spec),
            type_name=type_by_var[var_text],
            location=f"{formula_name}.variables.{var_name}",
            findings=findings,
            sort_parents=sort_parents,
        )
    if isinstance(var_spec, dict) and "quantifier" in var_spec:
        quantifier = str(var_spec.get("quantifier") or "")
        if quantifier not in {"forall", "exists"}:
            findings.append({
                "check": "unknown_variable_quantifier",
                "severity": "strong",
                "formula": formula_name,
                "variable": var_text,
                "quantifier": quantifier,
                "reason": "variable quantifier must be 'forall' or 'exists'.",
            })
        elif var_text in quantifier_by_var and quantifier != quantifier_by_var[var_text]:
            findings.append({
                "check": "formula_annotation_quantifier_mismatch",
                "severity": "strong",
                "formula": formula_name,
                "variable": var_text,
                "annotated_quantifier": quantifier,
                "actual_quantifier": quantifier_by_var[var_text],
                "reason": "annotated variable quantifier must match the A4V3 formula.",
            })


def _walk_formula_items(value: Any) -> list[str]:
    """Collect formula/call strings from flat or nested frame expressions.

    Supported annotation shapes include:

      effect:
        - rel(x)
      effect:
        all_of: [rel(x), {not: other(x)}]
      condition:
        any_of:
          - rel_a(x)
          - all_of: [rel_b(x), rel_c(x)]
      equivalence:
        left: a(x)
        right: {not: b(x)}

    The linter does not evaluate logic; it just validates referenced calls.
    """
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        out: list[str] = []
        for item in value:
            out.extend(_walk_formula_items(item))
        return out
    if isinstance(value, dict):
        out: list[str] = []
        for item in value.values():
            out.extend(_walk_formula_items(item))
        return out
    return []


def lint_entry(entry_dir: pathlib.Path) -> dict[str, Any]:
    ann_path = entry_dir / ROLE_ANNOTATION_FILE
    findings: list[dict[str, Any]] = []
    if not ann_path.exists():
        return {
            "schema": "role_annotation_lint_v1",
            "entry_id": entry_dir.name,
            "generated_at": datetime.now().isoformat(timespec="seconds"),
            "status": "skipped_missing_role_annotations",
            "role_annotation_file": ROLE_ANNOTATION_FILE,
            "summary": {
                "total_findings": 0,
                "strong_findings": 0,
                "soft_findings": 0,
                "advisory_findings": 0,
                "by_check": {},
            },
            "findings": [],
        }

    data, load_error = _load_yaml(ann_path)
    if load_error:
        findings.append({
            "check": "role_annotations_yaml_parse_error",
            "severity": "strong",
            "reason": load_error,
        })
        data = {}

    a4v3_text = _read_text(entry_dir / "main_ir.a4v3")
    parsed = _parse_a4v3(a4v3_text)
    symbols: dict[str, dict[str, Any]] = parsed["symbols"]
    constraints: dict[str, str] = parsed["constraints"]
    sort_parents: dict[str, str] = parsed["sort_parents"]
    all_declared = set(symbols) | set(constraints) | set(parsed["facts"]) | set(parsed["deontics"])
    calls_present_in_ir = set(CALL_RE.findall(a4v3_text))

    symbol_annotations = _collect_symbol_annotations(data)
    constraint_annotations = _collect_constraint_annotations(data)
    fact_annotations = _collect_fact_annotations(data)

    for name, spec in symbol_annotations.items():
        declared = symbols.get(name)
        if declared is None:
            findings.append({
                "check": "annotation_references_unknown_symbol",
                "severity": "strong",
                "symbol": name,
                "reason": "annotated symbol is not declared in main_ir.a4v3.",
            })
            continue
        expected_kind = declared.get("kind")
        annotated_kind = spec.get("kind")
        if annotated_kind and annotated_kind != expected_kind:
            findings.append({
                "check": "annotation_kind_mismatch",
                "severity": "strong",
                "symbol": name,
                "expected_kind": expected_kind,
                "annotated_kind": annotated_kind,
                "reason": "role annotation kind does not match A4V3 declaration kind.",
            })
        arg_roles = _normalize_arg_roles(spec.get("args"))
        if len(arg_roles) != int(declared.get("arity") or 0):
            findings.append({
                "check": "annotation_arity_mismatch",
                "severity": "strong",
                "symbol": name,
                "declared_arity": declared.get("arity"),
                "annotated_arity": len(arg_roles),
                "reason": "number of annotated argument roles must match A4V3 arity.",
            })
        for index, item in enumerate(arg_roles, start=1):
            _validate_role(
                role=_role_from_value(item),
                location=f"{name}.args[{index}]",
                findings=findings,
            )
            declared_args = declared.get("args") or []
            if index <= len(declared_args):
                _validate_type_role_alignment(
                    role=_role_from_value(item),
                    type_name=str(declared_args[index - 1]),
                    location=f"{name}.args[{index}]",
                    findings=findings,
                    sort_parents=sort_parents,
                )
        if expected_kind == "fun":
            returns = spec.get("returns")
            role = _role_from_value(returns)
            if returns is None:
                findings.append({
                    "check": "function_missing_return_role",
                    "severity": "strong",
                    "symbol": name,
                    "reason": "function annotations must include returns.role.",
                })
            else:
                _validate_role(
                    role=role,
                    location=f"{name}.returns",
                    findings=findings,
                )

    annotated_symbols = set(symbol_annotations)
    for name, declared in sorted(symbols.items()):
        if declared.get("kind") == "rel" and int(declared.get("arity") or 0) > 2:
            if name not in annotated_symbols:
                findings.append({
                    "check": "missing_annotation_for_high_arity_relation",
                    "severity": "strong",
                    "symbol": name,
                    "arity": declared.get("arity"),
                    "reason": "relations with arity > 2 require role annotations or carrier refactoring.",
                })
        if declared.get("kind") == "fun" and name not in annotated_symbols:
            findings.append({
                "check": "missing_annotation_for_function",
                "severity": "strong",
                "symbol": name,
                "arity": declared.get("arity"),
                "reason": "functions require argument roles and return role.",
            })

    def _validate_formula_annotation(
        *,
        name: str,
        spec: dict[str, Any],
        block: str | None,
        formula_kind: str,
    ) -> None:
        if block is None:
            findings.append({
                "check": f"annotation_references_unknown_{formula_kind}",
                "severity": "strong",
                formula_kind: name,
                "reason": f"annotated {formula_kind} is not declared in main_ir.a4v3.",
            })
            return
        variables = spec.get("variables")
        if isinstance(variables, dict):
            for var_name, var_spec in variables.items():
                _validate_variable_spec(
                    formula_name=name,
                    var_name=str(var_name),
                    var_spec=var_spec,
                    block=block,
                    severity_for_unquantified="soft",
                    findings=findings,
                    sort_parents=sort_parents,
                )
        scope = spec.get("scope")
        if isinstance(scope, dict) and "role" in scope:
            _validate_role(
                role=_role_from_value(scope),
                location=f"{name}.scope",
                findings=findings,
            )
        for section in ("trigger", "condition", "effect", "side_conditions", "equivalence"):
            for item in _walk_formula_items(spec.get(section)):
                for called in CALL_RE.findall(item):
                    if called in {"forall", "exists", "not"}:
                        continue
                    if called not in all_declared and called not in calls_present_in_ir:
                        findings.append({
                            "check": "formula_annotation_references_unknown_call",
                            "severity": "soft",
                            formula_kind: name,
                            "section": section,
                            "call": called,
                            "reason": "formula frame annotation references a call not declared in A4V3.",
                        })

    for name, spec in constraint_annotations.items():
        _validate_formula_annotation(
            name=name,
            spec=spec,
            block=constraints.get(name),
            formula_kind="constraint",
        )

    facts: dict[str, str] = parsed["facts"]
    for name, spec in fact_annotations.items():
        _validate_formula_annotation(
            name=name,
            spec=spec,
            block=facts.get(name),
            formula_kind="fact",
        )

    annotated_constraints = set(constraint_annotations)
    for name, block in sorted(constraints.items()):
        if name not in annotated_constraints and COMPLEX_FRAME_RE.search(block):
            findings.append({
                "check": "missing_annotation_for_complex_constraint",
                "severity": "soft",
                "constraint": name,
                "reason": "complex constraints should have frame annotations once the entry opts into role annotations.",
            })
    annotated_facts = set(fact_annotations)
    for name, block in sorted(facts.items()):
        if name not in annotated_facts and COMPLEX_FRAME_RE.search(block):
            findings.append({
                "check": "missing_annotation_for_complex_fact",
                "severity": "soft",
                "fact": name,
                "reason": "complex facts should have frame annotations once the entry opts into role annotations.",
            })

    counts = Counter(f["check"] for f in findings)
    summary = {
        "total_findings": len(findings),
        "strong_findings": sum(1 for f in findings if f.get("severity") == "strong"),
        "soft_findings": sum(1 for f in findings if f.get("severity") == "soft"),
        "advisory_findings": sum(1 for f in findings if f.get("severity") == "advisory"),
        "by_check": dict(sorted(counts.items())),
        "annotated_symbol_count": len(symbol_annotations),
        "annotated_constraint_count": len(constraint_annotations),
        "annotated_fact_count": len(fact_annotations),
    }
    return {
        "schema": "role_annotation_lint_v1",
        "entry_id": entry_dir.name,
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "status": "ok",
        "role_annotation_file": ROLE_ANNOTATION_FILE,
        "approved_roles": sorted(APPROVED_ROLES),
        "summary": summary,
        "findings": findings,
    }


def write_report(entry_dir: pathlib.Path, report: dict[str, Any]) -> None:
    json_p = entry_dir / "role_annotation_lint_v1.json"
    md_p = entry_dir / "role_annotation_lint_v1.md"
    json_p.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    summary = report.get("summary") or {}
    lines = [
        f"# Role Annotation Lint: {report.get('entry_id')}",
        "",
        f"- status: `{report.get('status')}`",
        f"- total_findings: `{summary.get('total_findings', 0)}`",
        f"- strong/soft/advisory: `{summary.get('strong_findings', 0)}` / "
        f"`{summary.get('soft_findings', 0)}` / `{summary.get('advisory_findings', 0)}`",
        f"- annotated symbols: `{summary.get('annotated_symbol_count', 0)}`",
        f"- annotated constraints: `{summary.get('annotated_constraint_count', 0)}`",
        f"- annotated facts: `{summary.get('annotated_fact_count', 0)}`",
        f"- by_check: `{summary.get('by_check', {})}`",
    ]
    findings = report.get("findings") or []
    if findings:
        lines.extend(["", "## Findings", ""])
        for finding in findings:
            label = (
                finding.get("symbol")
                or finding.get("constraint")
                or finding.get("location")
                or ""
            )
            lines.append(f"### `{finding.get('check')}` / `{label}`")
            lines.append("")
            lines.append(f"- severity: `{finding.get('severity')}`")
            lines.append(f"- reason: {finding.get('reason')}")
            for key in ("role", "arity", "declared_arity", "annotated_arity", "variable", "call"):
                if key in finding:
                    lines.append(f"- {key}: `{finding.get(key)}`")
            lines.append("")
    else:
        lines.extend(["", "No role-annotation lint findings.", ""])
    md_p.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("target", help="seed methodology entry dir or run root")
    args = ap.parse_args()
    target = pathlib.Path(args.target)
    entries = _entry_dirs(target)
    if not entries:
        raise SystemExit(f"No role annotation entries found under {target}")
    corpus = []
    for entry in entries:
        report = lint_entry(entry)
        write_report(entry, report)
        corpus.append(report)
    if len(corpus) > 1:
        out = {
            "schema": "role_annotation_lint_corpus_v1",
            "generated_at": datetime.now().isoformat(timespec="seconds"),
            "entry_count": len(corpus),
            "total_findings": sum(r.get("summary", {}).get("total_findings", 0) for r in corpus),
            "strong_findings": sum(r.get("summary", {}).get("strong_findings", 0) for r in corpus),
            "entries": [
                {
                    "entry_id": r.get("entry_id"),
                    "status": r.get("status"),
                    "total_findings": r.get("summary", {}).get("total_findings"),
                    "strong_findings": r.get("summary", {}).get("strong_findings"),
                }
                for r in corpus
            ],
        }
        (target / "role_annotation_lint_corpus_v1.json").write_text(
            json.dumps(out, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )


if __name__ == "__main__":
    main()
