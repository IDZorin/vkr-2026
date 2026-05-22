"""DZ-wide backend projection pass for A4V3 artifacts.

This pass is intentionally sidecar-only: it reads existing DZ ``*.a4v3`` files
and emits structural RDF, OWL/RDF, and SHACL artifacts without rewriting the
source-of-truth IR.

The AtomVex backend package already contains OWL/SHACL/SMT emitters for the
expanded authoring frontend. DZ files use the repository-local A4V3 parser and
allow constructs that frontend does not currently accept, such as multiline
enum declarations and unary relations. This pass therefore lowers directly from
``a4v3_parser_v1`` ASTs and links to the SMT probe report instead of forcing DZ
IR through the incompatible frontend.

CLI:
    python IR/src/dz_backend_projection_pass_v1.py --dz-root IR/outputs/runs/dz
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from collections import Counter
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

DATA_RANGES = {
    "Bool": "xsd:boolean",
    "Boolean": "xsd:boolean",
    "Int": "xsd:integer",
    "Integer": "xsd:integer",
    "Nat": "xsd:integer",
    "Natural": "xsd:integer",
    "Real": "xsd:decimal",
    "Decimal": "xsd:decimal",
    "Number": "xsd:decimal",
    "Percent": "xsd:decimal",
    "String": "xsd:string",
    "Text": "xsd:string",
}

PREFIXES = """@prefix ex: <http://example.org/a4v3#> .
@prefix a4: <http://example.org/a4v3/meta#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

"""


@dataclass(frozen=True)
class ProjectionTarget:
    target_id: str
    target_kind: str
    source_path: Path
    relative_path: str
    output_dir: Path


def _s(name: str | None) -> str:
    """Return a safe local Turtle name."""
    raw = str(name or "unknown")
    safe = re.sub(r"[^A-Za-z0-9_]+", "_", raw)
    if not safe or safe[0].isdigit():
        safe = f"N_{safe}"
    return safe


def _iri(name: str | None) -> str:
    return f"ex:{_s(name)}"


def _lit(value: Any) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int):
        return f'"{value}"^^xsd:integer'
    if isinstance(value, float):
        return f'"{value}"^^xsd:decimal'
    return json.dumps("" if value is None else str(value), ensure_ascii=False)


def _range(sort: str | None) -> str:
    return DATA_RANGES.get(str(sort or ""), _iri(sort))


def _is_data_sort(sort: str | None) -> bool:
    return str(sort or "") in DATA_RANGES


def _is_number_string(value: str | None) -> bool:
    return bool(re.fullmatch(r"-?\d+(?:\.\d+)?%?", str(value or "")))


def _number_literal(value: str) -> str:
    if value.endswith("%"):
        raw = value[:-1]
        return f'"{raw}"^^xsd:decimal'
    datatype = "xsd:decimal" if "." in value else "xsd:integer"
    return f'"{value}"^^{datatype}'


def _known_individuals(ast: dict[str, Any]) -> set[str]:
    names = {d.get("name") for d in _symbol_decls(ast) if d.get("kind") == "entity"}
    for decl in _type_decls(ast):
        if decl.get("kind") == "enum":
            names.update(decl.get("enum_members", []) or [])
    return {str(name) for name in names if name}


def _symbol_map(ast: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {str(d.get("name")): d for d in _symbol_decls(ast) if d.get("name")}


def _flatten_and(expr: dict[str, Any] | None) -> list[dict[str, Any]]:
    if not expr:
        return []
    if expr.get("kind") == "and":
        out: list[dict[str, Any]] = []
        for arg in expr.get("args", []) or []:
            out.extend(_flatten_and(arg))
        return out
    return [expr]


def _term(expr: dict[str, Any] | None, ast: dict[str, Any]) -> str | None:
    if not expr:
        return None
    if expr.get("kind") != "ref":
        return None
    name = str(expr.get("name") or "")
    if name in {"true", "false"}:
        return name
    if _is_number_string(name):
        return _number_literal(name)
    return _iri(name)


def _emit_nary_owl_pattern(name: str, args: list[str], result_sort: str | None, lines: list[str]) -> None:
    lines.append(f"{_iri(name)} a owl:Class, a4:NaryRelationClass .")
    for idx, sort in enumerate(args):
        prop = _iri(f"{name}_arg_{idx}")
        prop_type = "owl:DatatypeProperty" if _is_data_sort(sort) else "owl:ObjectProperty"
        lines.append(f"{prop} a {prop_type} ;")
        lines.append(f"  rdfs:domain {_iri(name)} ;")
        lines.append(f"  rdfs:range {_range(sort)} .")
    if result_sort:
        prop = _iri(f"{name}_result")
        prop_type = "owl:DatatypeProperty" if _is_data_sort(result_sort) else "owl:ObjectProperty"
        lines.append(f"{prop} a {prop_type}, owl:FunctionalProperty ;")
        lines.append(f"  rdfs:domain {_iri(name)} ;")
        lines.append(f"  rdfs:range {_range(result_sort)} .")


def _emit_nary_shacl_pattern(name: str, args: list[str], result_sort: str | None, lines: list[str]) -> None:
    lines.append(f"{_iri(name)} a rdfs:Class .")
    lines.append(f"{_iri(name + 'Shape')} a sh:NodeShape ; sh:targetClass {_iri(name)} .")
    for idx, sort in enumerate(args):
        prop = _iri(f"{name}_arg_{idx}")
        range_line = f"sh:datatype {_range(sort)}" if _is_data_sort(sort) else f"sh:class {_iri(sort)}"
        lines.append(f"{_iri(name + 'Shape')} sh:property [ sh:path {prop} ; {range_line} ; sh:minCount 1 ; sh:maxCount 1 ] .")
    if result_sort:
        prop = _iri(f"{name}_result")
        range_line = f"sh:datatype {_range(result_sort)}" if _is_data_sort(result_sort) else f"sh:class {_iri(result_sort)}"
        lines.append(f"{_iri(name + 'Shape')} sh:property [ sh:path {prop} ; {range_line} ; sh:minCount 1 ; sh:maxCount 1 ] .")


def _emit_ground_atom(
    atom: dict[str, Any],
    ast: dict[str, Any],
    lines: list[str],
    *,
    assertion_name: str,
    atom_index: int,
    mode: str,
) -> bool:
    symbols = _symbol_map(ast)
    if atom.get("kind") == "call":
        callee = str(atom.get("callee") or "")
        decl = symbols.get(callee)
        if not decl or decl.get("kind") != "rel":
            return False
        args = atom.get("args", []) or []
        terms = [_term(arg, ast) for arg in args]
        if any(term is None for term in terms):
            return False
        if len(terms) == 1:
            lines.append(f"{terms[0]} a {_iri(callee)} .")
            return True
        if len(terms) == 2:
            lines.append(f"{terms[0]} {_iri(callee)} {terms[1]} .")
            return True
        event = _iri(f"FACT_{assertion_name}_{callee}_{atom_index}")
        lines.append(f"{event} a {_iri(callee)} .")
        for idx, term in enumerate(terms):
            lines.append(f"{event} {_iri(f'{callee}_arg_{idx}')} {term} .")
        return True

    if atom.get("kind") == "eq":
        left = atom.get("left")
        right = atom.get("right")
        if isinstance(left, dict) and left.get("kind") == "call":
            callee = str(left.get("callee") or "")
            decl = symbols.get(callee)
            if not decl or decl.get("kind") != "fun":
                return False
            args = left.get("args", []) or []
            terms = [_term(arg, ast) for arg in args]
            result = _term(right, ast)
            if any(term is None for term in terms) or result is None:
                return False
            if len(terms) == 1:
                lines.append(f"{terms[0]} {_iri(callee)} {result} .")
                return True
            event = _iri(f"FACT_{assertion_name}_{callee}_{atom_index}")
            lines.append(f"{event} a {_iri(callee)} .")
            for idx, term in enumerate(terms):
                lines.append(f"{event} {_iri(f'{callee}_arg_{idx}')} {term} .")
            lines.append(f"{event} {_iri(f'{callee}_result')} {result} .")
            return True
        if isinstance(left, dict) and left.get("kind") == "ref":
            left_term = _term(left, ast)
            right_term = _term(right, ast)
            if left_term and right_term and mode == "owl":
                lines.append(f"{left_term} owl:sameAs {right_term} .")
                return True
    return False


def _emit_ground_assertion(assertion: dict[str, Any], ast: dict[str, Any], lines: list[str], *, mode: str) -> bool:
    if assertion.get("kind") != "fact":
        return False
    atoms = _flatten_and(assertion.get("expr"))
    if not atoms:
        return False
    lowered = []
    for idx, atom in enumerate(atoms):
        lowered.append(
            _emit_ground_atom(
                atom,
                ast,
                lines,
                assertion_name=str(assertion.get("name") or "assertion"),
                atom_index=idx,
                mode=mode,
            )
        )
    return all(lowered)


def _expr_text(expr: dict[str, Any] | None) -> str:
    if not expr:
        return ""
    kind = expr.get("kind")
    if kind == "ref":
        return str(expr.get("name", ""))
    if kind == "call":
        return f"{expr.get('callee')}({', '.join(_expr_text(arg) for arg in expr.get('args', []) or [])})"
    if kind in {"forall", "exists"}:
        vars_text = ", ".join(f"{v.get('name')}: {v.get('sort')}" for v in expr.get("vars", []) or [])
        return f"{kind} {vars_text}, {_expr_text(expr.get('body'))}"
    if kind in {"and", "or"}:
        return f" {kind} ".join(f"({_expr_text(arg)})" for arg in expr.get("args", []) or [])
    if kind == "not":
        return f"not ({_expr_text(expr.get('arg'))})"
    if kind in {"implies", "iff"}:
        return f"({_expr_text(expr.get('left'))}) {kind} ({_expr_text(expr.get('right'))})"
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
        return f"({_expr_text(expr.get('left'))}) {op} ({_expr_text(expr.get('right'))})"
    return f"<{kind}>"


def _discover_targets(dz_root: Path, out_root: Path) -> list[ProjectionTarget]:
    targets: list[ProjectionTarget] = []
    for group_dir_name, target_kind in ENTRY_GROUPS:
        group_dir = dz_root / group_dir_name
        if not group_dir.exists():
            continue
        for entry_dir in sorted(group_dir.iterdir(), key=lambda p: p.name.lower()):
            if not entry_dir.is_dir() or entry_dir.name.startswith("agent_run"):
                continue
            main_ir = entry_dir / "main_ir.a4v3"
            if not main_ir.exists() or main_ir.stat().st_size == 0:
                continue
            rel = main_ir.relative_to(dz_root).as_posix()
            targets.append(
                ProjectionTarget(
                    target_id=entry_dir.name,
                    target_kind=target_kind,
                    source_path=main_ir,
                    relative_path=rel,
                    output_dir=out_root / group_dir_name / entry_dir.name,
                )
            )

    supplemental = [
        ("bridge_main_bridge", "bridge", dz_root / "bridge" / "main_bridge.a4v3"),
        ("bridge_resolved_bridge_decisions_v1", "bridge", dz_root / "bridge" / "resolved_bridge_decisions_v1.a4v3"),
        ("merge_canonical_ontology_v1", "merge", dz_root / "merge" / "canonical_ontology_v1.a4v3"),
        ("process_ontology_v1", "process", dz_root / "process" / "process_ontology_v1.a4v3"),
        ("ordinary_rebalance_workflow_v1", "process", dz_root / "process" / "ordinary_rebalance_workflow_v1.a4v3"),
        ("exception_overlays_v1", "process", dz_root / "process" / "exception_overlays_v1.a4v3"),
    ]
    for target_id, target_kind, path in supplemental:
        if path.exists() and path.stat().st_size > 0:
            targets.append(
                ProjectionTarget(
                    target_id=target_id,
                    target_kind=target_kind,
                    source_path=path,
                    relative_path=path.relative_to(dz_root).as_posix(),
                    output_dir=out_root / target_kind / target_id,
                )
            )
    return targets


def _type_decls(ast: dict[str, Any]) -> list[dict[str, Any]]:
    return [d for d in ast.get("declarations", []) or [] if d.get("family") == "TypeDecl"]


def _symbol_decls(ast: dict[str, Any]) -> list[dict[str, Any]]:
    return [d for d in ast.get("declarations", []) or [] if d.get("family") == "SymbolDecl"]


def emit_rdf(ast: dict[str, Any], target: ProjectionTarget) -> tuple[str, list[dict[str, Any]]]:
    lines = [PREFIXES.rstrip(), "", f"{_iri(target.target_id)} a a4:ProjectionTarget ;", f"  a4:relativePath {_lit(target.relative_path)} ;", f"  a4:targetKind {_lit(target.target_kind)} .", ""]
    diagnostics: list[dict[str, Any]] = []

    for decl in _type_decls(ast):
        name = decl.get("name")
        kind = decl.get("kind")
        lines.append(f"{_iri(name)} a rdfs:Class, a4:Sort ;")
        lines.append(f"  a4:declKind {_lit(kind)} .")
        if kind == "subtype":
            lines.append(f"{_iri(name)} rdfs:subClassOf {_iri(decl.get('parent'))} .")
        if kind == "enum":
            for member in decl.get("enum_members", []) or []:
                lines.append(f"{_iri(member)} a {_iri(name)}, a4:EnumMember, owl:NamedIndividual .")
                lines.append(f"{_iri(name)} a4:enumMember {_iri(member)} .")
    if _type_decls(ast):
        lines.append("")

    for decl in _symbol_decls(ast):
        name = decl.get("name")
        kind = decl.get("kind")
        if kind == "entity":
            lines.append(f"{_iri(name)} a {_iri(decl.get('sort'))}, owl:NamedIndividual .")
            continue
        if kind in {"rel", "fun"}:
            args = decl.get("args", []) or []
            lines.append(f"{_iri(name)} a rdf:Property, a4:{kind.capitalize()}Symbol ;")
            lines.append(f"  a4:arity {_lit(len(args))} .")
            for idx, sort in enumerate(args):
                arg_node = _iri(f"{name}_arg_{idx}")
                lines.append(f"{arg_node} a a4:Argument ; a4:position {_lit(idx)} ; a4:sort {_iri(sort)} .")
                lines.append(f"{_iri(name)} a4:argument {arg_node} .")
            if kind == "fun":
                lines.append(f"{_iri(name)} a4:resultSort {_range(decl.get('result_sort'))} .")
                if decl.get("flags"):
                    lines.append(f"{_iri(name)} a4:functionFlag {_lit(decl.get('flags'))} .")
            continue
        diagnostics.append({"severity": "advisory", "code": "symbol_preserved_as_artifact", "symbol": name, "kind": kind})
        lines.append(f"{_iri(name)} a a4:SymbolArtifact ; a4:declKind {_lit(kind)} .")
    if _symbol_decls(ast):
        lines.append("")

    for assertion in ast.get("assertions", []) or []:
        node = _iri(f"ASSERT_{assertion.get('name')}")
        lines.append(f"{node} a a4:Assertion ;")
        lines.append(f"  a4:assertionKind {_lit(assertion.get('kind'))} ;")
        lines.append(f"  a4:lineNo {_lit(assertion.get('line_no'))} ;")
        lines.append(f"  a4:exprText {_lit(_expr_text(assertion.get('expr')) or assertion.get('body_text', ''))} ;")
        lines.append(f"  a4:sourceText {_lit(assertion.get('raw', ''))} .")
    return "\n".join(lines).strip() + "\n", diagnostics


def emit_owl(ast: dict[str, Any], target: ProjectionTarget) -> tuple[str, list[dict[str, Any]]]:
    lines = [PREFIXES.rstrip(), "", f"{_iri(target.target_id)} a owl:Ontology .", ""]
    diagnostics: list[dict[str, Any]] = []

    for decl in _type_decls(ast):
        name = decl.get("name")
        kind = decl.get("kind")
        if kind == "enum":
            members = decl.get("enum_members", []) or []
            if members:
                one_of = " ".join(_iri(member) for member in members)
                lines.append(f"{_iri(name)} a owl:Class ; owl:oneOf ( {one_of} ) .")
            else:
                lines.append(f"{_iri(name)} a owl:Class .")
            for member in members:
                lines.append(f"{_iri(member)} a {_iri(name)}, owl:NamedIndividual .")
        else:
            lines.append(f"{_iri(name)} a owl:Class .")
        if kind == "subtype":
            lines.append(f"{_iri(name)} rdfs:subClassOf {_iri(decl.get('parent'))} .")
    if _type_decls(ast):
        lines.append("")

    for decl in _symbol_decls(ast):
        name = decl.get("name")
        kind = decl.get("kind")
        if kind == "entity":
            lines.append(f"{_iri(name)} a {_iri(decl.get('sort'))}, owl:NamedIndividual .")
            continue
        if kind == "rel":
            args = decl.get("args", []) or []
            if len(args) == 1:
                lines.append(f"{_iri(name)} a owl:Class ; rdfs:subClassOf {_iri(args[0])} .")
            elif len(args) == 2:
                prop_type = "owl:DatatypeProperty" if _is_data_sort(args[1]) else "owl:ObjectProperty"
                lines.append(f"{_iri(name)} a {prop_type} ;")
                lines.append(f"  rdfs:domain {_iri(args[0])} ;")
                lines.append(f"  rdfs:range {_range(args[1])} .")
            else:
                diagnostics.append({"severity": "advisory", "code": "nary_relation_reified", "symbol": name, "arity": len(args)})
                _emit_nary_owl_pattern(str(name), args, None, lines)
            continue
        if kind == "fun":
            args = decl.get("args", []) or []
            result_sort = decl.get("result_sort")
            if len(args) == 1:
                prop_type = "owl:DatatypeProperty" if _is_data_sort(result_sort) else "owl:ObjectProperty"
                lines.append(f"{_iri(name)} a {prop_type}, owl:FunctionalProperty ;")
                lines.append(f"  rdfs:domain {_iri(args[0])} ;")
                lines.append(f"  rdfs:range {_range(result_sort)} .")
            else:
                diagnostics.append({"severity": "advisory", "code": "nary_function_reified", "symbol": name, "arity": len(args)})
                _emit_nary_owl_pattern(str(name), args, result_sort, lines)
            continue
        diagnostics.append({"severity": "advisory", "code": "symbol_preserved_as_artifact", "symbol": name, "kind": kind})
        lines.append(f"{_iri(name)} a a4:SymbolArtifact ; a4:declKind {_lit(kind)} .")

    if ast.get("assertions"):
        lines.append("")
        for assertion in ast.get("assertions", []) or []:
            if _emit_ground_assertion(assertion, ast, lines, mode="owl"):
                continue
            diagnostics.append({"severity": "advisory", "code": "formula_preserved_as_artifact", "assertion": assertion.get("name")})
            lines.append(f"{_iri('ASSERT_' + str(assertion.get('name')))} a a4:AssertionArtifact ;")
            lines.append(f"  a4:assertionKind {_lit(assertion.get('kind'))} ;")
            lines.append(f"  a4:exprText {_lit(_expr_text(assertion.get('expr')) or assertion.get('body_text', ''))} .")
    return "\n".join(lines).strip() + "\n", diagnostics


def emit_shacl(ast: dict[str, Any], target: ProjectionTarget) -> tuple[str, list[dict[str, Any]]]:
    lines = [PREFIXES.rstrip(), "", f"{_iri(target.target_id)} a a4:ShaclProjectionTarget .", ""]
    diagnostics: list[dict[str, Any]] = []

    for decl in _type_decls(ast):
        name = decl.get("name")
        lines.append(f"{_iri(name)} a rdfs:Class .")
        if decl.get("kind") == "subtype":
            lines.append(f"{_iri(name)} rdfs:subClassOf {_iri(decl.get('parent'))} .")
        lines.append(f"{_iri(name + 'Shape')} a sh:NodeShape ; sh:targetClass {_iri(name)} .")
        if decl.get("kind") == "enum":
            for member in decl.get("enum_members", []) or []:
                lines.append(f"{_iri(member)} a {_iri(name)} .")
    if _type_decls(ast):
        lines.append("")

    for decl in _symbol_decls(ast):
        name = decl.get("name")
        kind = decl.get("kind")
        if kind == "entity":
            lines.append(f"{_iri(name)} a {_iri(decl.get('sort'))} .")
            continue
        if kind == "rel":
            args = decl.get("args", []) or []
            if len(args) == 1:
                lines.append(f"{_iri(name)} a rdfs:Class ; rdfs:subClassOf {_iri(args[0])} .")
            elif len(args) == 2:
                lines.append(f"{_iri(name)} a rdf:Property .")
                range_line = f"sh:datatype {_range(args[1])}" if _is_data_sort(args[1]) else f"sh:class {_iri(args[1])}"
                lines.append(f"{_iri(args[0] + 'Shape')} sh:property [ sh:path {_iri(name)} ; {range_line} ] .")
            else:
                diagnostics.append({"severity": "advisory", "code": "nary_relation_reified_shape", "symbol": name, "arity": len(args)})
                _emit_nary_shacl_pattern(str(name), args, None, lines)
            continue
        if kind == "fun":
            args = decl.get("args", []) or []
            result_sort = decl.get("result_sort")
            if len(args) == 1:
                lines.append(f"{_iri(name)} a rdf:Property .")
                range_line = f"sh:datatype {_range(result_sort)}" if _is_data_sort(result_sort) else f"sh:class {_iri(result_sort)}"
                counts = " ; sh:maxCount 1"
                if "required" in str(decl.get("flags") or ""):
                    counts = " ; sh:minCount 1 ; sh:maxCount 1"
                lines.append(f"{_iri(args[0] + 'Shape')} sh:property [ sh:path {_iri(name)} ; {range_line}{counts} ] .")
            else:
                diagnostics.append({"severity": "advisory", "code": "nary_function_reified_shape", "symbol": name, "arity": len(args)})
                _emit_nary_shacl_pattern(str(name), args, result_sort, lines)
            continue
        diagnostics.append({"severity": "advisory", "code": "symbol_preserved_as_artifact", "symbol": name, "kind": kind})
        lines.append(f"# symbol {name} kind={kind} preserved as artifact")
    if ast.get("assertions"):
        lines.append("")
        for assertion in ast.get("assertions", []) or []:
            _emit_ground_assertion(assertion, ast, lines, mode="shacl")
    return "\n".join(lines).strip() + "\n", diagnostics


def _check_turtle(text: str, *, kind: str) -> dict[str, Any]:
    if importlib.util.find_spec("rdflib") is None:
        return {"backend": kind, "status": "unavailable", "message": "rdflib is not installed"}
    try:
        from rdflib import Graph

        graph = Graph()
        graph.parse(data=text, format="turtle")
        return {"backend": kind, "status": "ok", "triple_count": len(graph), "message": "Turtle parsed"}
    except Exception as exc:
        return {"backend": kind, "status": "error", "message": str(exc)}


def _check_owl(text: str) -> dict[str, Any]:
    base = _check_turtle(text, kind="owl")
    if base.get("status") != "ok":
        return base
    if importlib.util.find_spec("owlrl") is None:
        base.update({"status": "partial", "message": "Turtle parsed; owlrl is not installed"})
        return base
    try:
        from rdflib import Graph
        from owlrl import DeductiveClosure, OWLRL_Semantics

        graph = Graph()
        graph.parse(data=text, format="turtle")
        before = len(graph)
        DeductiveClosure(OWLRL_Semantics).expand(graph)
        base.update({"status": "ok", "triple_count_before": before, "triple_count_after": len(graph), "message": "OWL RL closure completed"})
        return base
    except Exception as exc:
        return {"backend": "owl", "status": "error", "message": f"OWL RL reasoning failed: {exc}"}


def _check_shacl(text: str) -> dict[str, Any]:
    base = _check_turtle(text, kind="shacl")
    if base.get("status") != "ok":
        return base
    if importlib.util.find_spec("pyshacl") is None:
        base.update({"status": "partial", "message": "Turtle parsed; pyshacl is not installed"})
        return base
    try:
        from rdflib import Graph
        from pyshacl import validate

        graph = Graph()
        graph.parse(data=text, format="turtle")
        conforms, _, report_text = validate(graph, shacl_graph=graph, inference="rdfs", advanced=True)
        base.update({"status": "ok", "conforms": bool(conforms), "message": f"pySHACL conforms={conforms}", "report_text": str(report_text)[-5000:]})
        return base
    except Exception as exc:
        return {"backend": "shacl", "status": "error", "message": f"pySHACL validation failed: {exc}"}


def _write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _project_target(target: ProjectionTarget) -> dict[str, Any]:
    text = target.source_path.read_text(encoding="utf-8")
    ast = parse(text, strict=False)
    target.output_dir.mkdir(parents=True, exist_ok=True)

    parse_report = {
        "warning_count": len(ast.get("warnings", []) or []),
        "warnings": ast.get("warnings", []) or [],
        "declaration_count": len(ast.get("declarations", []) or []),
        "assertion_count": len(ast.get("assertions", []) or []),
    }

    backend_reports: dict[str, Any] = {}
    for backend, emitter, checker, artifact_name in [
        ("rdf", emit_rdf, lambda t: _check_turtle(t, kind="rdf"), "rdf.ttl"),
        ("owl", emit_owl, _check_owl, "owl.ttl"),
        ("shacl", emit_shacl, _check_shacl, "shacl_shapes.ttl"),
    ]:
        artifact_text, diagnostics = emitter(ast, target)
        artifact_path = target.output_dir / artifact_name
        _write_text(artifact_path, artifact_text)
        emission = {
            "backend": backend,
            "artifact": str(artifact_path),
            "diagnostic_count": len(diagnostics),
            "diagnostics": diagnostics,
            "partial": any(d.get("severity") in {"advisory", "soft"} for d in diagnostics),
        }
        check = checker(artifact_text)
        _write_json(target.output_dir / f"{backend}.emission.json", emission)
        _write_json(target.output_dir / f"{backend}.check.json", check)
        backend_reports[backend] = {"emission": emission, "check": check}

    return {
        "target_id": target.target_id,
        "target_kind": target.target_kind,
        "relative_path": target.relative_path,
        "output_dir": str(target.output_dir),
        "parse": parse_report,
        "backends": backend_reports,
    }


def run_pass(dz_root: Path, out_root: Path) -> dict[str, Any]:
    targets = _discover_targets(dz_root, out_root)
    target_reports = [_project_target(target) for target in targets]
    union_report = _write_owl_union(out_root, target_reports)
    resolved_report = _write_resolved_owl_union(dz_root, out_root, union_report)
    check_status_counts: Counter[str] = Counter()
    emission_diag_counts: Counter[str] = Counter()
    for report in target_reports:
        for backend, payload in report["backends"].items():
            check_status_counts[f"{backend}:{payload['check'].get('status')}"] += 1
            emission_diag_counts[backend] += int(payload["emission"].get("diagnostic_count", 0))

    smt_report_path = dz_root / "reasoning" / "smt_probe_results_v1.json"
    smt_summary = None
    if smt_report_path.exists():
        try:
            smt_report = json.loads(smt_report_path.read_text(encoding="utf-8"))
            smt_summary = {
                "path": str(smt_report_path),
                "status": smt_report.get("status"),
                "smt_mode": smt_report.get("smt_mode"),
                "probe_count": smt_report.get("probe_count"),
                "hard_findings": smt_report.get("hard_findings"),
                "soft_findings": smt_report.get("soft_findings"),
                "advisory_findings": smt_report.get("advisory_findings"),
            }
        except Exception as exc:
            smt_summary = {"path": str(smt_report_path), "status": "error", "message": str(exc)}

    hard = sum(1 for report in target_reports for payload in report["backends"].values() if payload["check"].get("status") == "error")
    if resolved_report.get("check", {}).get("status") == "error":
        hard += 1
    soft = sum(1 for report in target_reports for payload in report["backends"].values() if payload["check"].get("status") in {"partial", "timeout"})
    if resolved_report.get("check", {}).get("status") in {"partial", "timeout"}:
        soft += 1
    advisory = sum(int(report["parse"]["warning_count"]) for report in target_reports) + sum(emission_diag_counts.values())
    advisory += int(resolved_report.get("review_item_count", 0)) + int(resolved_report.get("unresolved_symbol_count", 0))
    status = "blocked" if hard else ("passed_with_review_items" if (soft or advisory) else "passed")

    return {
        "schema": "dz_backend_projection_report_v1",
        "dz_root": str(dz_root),
        "out_root": str(out_root),
        "target_count": len(target_reports),
        "target_count_by_kind": dict(Counter(r["target_kind"] for r in target_reports)),
        "backend_check_status_counts": dict(check_status_counts),
        "backend_emission_diagnostic_counts": dict(emission_diag_counts),
        "hard_findings": hard,
        "soft_findings": soft,
        "advisory_findings": advisory,
        "status": status,
        "smt_probe_summary": smt_summary,
        "owl_union": union_report,
        "owl_resolved": resolved_report,
        "targets": target_reports,
    }


def _rewrite_prefixes_for_union(text: str, graph_name: str) -> str:
    lines: list[str] = []
    for line in text.splitlines():
        if line.startswith("@prefix "):
            continue
        if line.strip().startswith("ex:") or " ex:" in line or "( ex:" in line:
            line = line.replace("ex:", f"{graph_name}:")
        lines.append(line)
    return "\n".join(lines).strip()


def _write_owl_union(out_root: Path, target_reports: list[dict[str, Any]]) -> dict[str, Any]:
    union_dir = out_root / "all"
    union_dir.mkdir(parents=True, exist_ok=True)
    union_path = union_dir / "dz_owl_union.ttl"
    manifest_path = union_dir / "dz_owl_union_manifest.json"
    check_path = union_dir / "dz_owl_union.check.json"

    prefix_lines = [
        "@prefix a4: <http://example.org/a4v3/meta#> .",
        "@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .",
        "@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .",
        "@prefix owl: <http://www.w3.org/2002/07/owl#> .",
        "@prefix sh: <http://www.w3.org/ns/shacl#> .",
        "@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .",
        "",
    ]
    manifest_entries: list[dict[str, Any]] = []
    body_parts: list[str] = []
    for idx, report in enumerate(target_reports, start=1):
        owl_artifact = Path(report["backends"]["owl"]["emission"]["artifact"])
        graph_name = f"g{idx:03d}"
        namespace = f"http://example.org/a4v3/{_s(report['target_kind'])}/{_s(report['target_id'])}#"
        prefix_lines.append(f"@prefix {graph_name}: <{namespace}> .")
        text = owl_artifact.read_text(encoding="utf-8")
        rewritten = _rewrite_prefixes_for_union(text, graph_name)
        body_parts.append(f"\n# --- {report['target_kind']} / {report['target_id']} / {report['relative_path']} ---\n{rewritten}\n")
        manifest_entries.append(
            {
                "prefix": graph_name,
                "namespace": namespace,
                "target_id": report["target_id"],
                "target_kind": report["target_kind"],
                "relative_path": report["relative_path"],
                "source_owl": str(owl_artifact),
            }
        )

    union_text = "\n".join(prefix_lines) + "\n" + "\n".join(body_parts).strip() + "\n"
    union_path.write_text(union_text, encoding="utf-8")
    manifest = {
        "schema": "dz_owl_union_manifest_v1",
        "target_count": len(target_reports),
        "union_path": str(union_path),
        "entries": manifest_entries,
    }
    _write_json(manifest_path, manifest)

    check = _check_owl(union_text)
    _write_json(check_path, check)
    return {
        "union_path": str(union_path),
        "manifest_path": str(manifest_path),
        "check_path": str(check_path),
        "target_count": len(target_reports),
        "check": check,
    }


def _iter_calls(expr: dict[str, Any] | None) -> list[dict[str, Any]]:
    if not isinstance(expr, dict):
        return []
    calls: list[dict[str, Any]] = []
    if expr.get("kind") == "call":
        calls.append(expr)
    for value in expr.values():
        if isinstance(value, dict):
            calls.extend(_iter_calls(value))
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    calls.extend(_iter_calls(item))
    return calls


def _ref_name(expr: dict[str, Any] | None) -> str | None:
    if isinstance(expr, dict) and expr.get("kind") == "ref":
        return str(expr.get("name") or "")
    return None


def _entry_target_id(entry_name: str) -> str | None:
    if m := re.fullmatch(r"Section(\d+)_(\d+)", entry_name):
        return f"section_{m.group(1)}_{m.group(2)}"
    if m := re.fullmatch(r"Appendix(\d+)_(\d+)", entry_name):
        return f"appendix_{m.group(1)}_{m.group(2)}"
    if m := re.fullmatch(r"Definition(N\d+)", entry_name):
        return m.group(1)
    return None


def _bridge_prefix_for_entry(entry_name: str) -> str | None:
    if re.fullmatch(r"Section\d+_\d+", entry_name):
        return entry_name
    if re.fullmatch(r"Appendix\d+_\d+", entry_name):
        return entry_name
    if m := re.fullmatch(r"Definition(N\d+)", entry_name):
        return m.group(1)
    return None


def _bridge_symbol_iri(
    symbol_name: str,
    *,
    symbol_entries: dict[str, list[str]],
    target_namespaces: dict[str, str],
) -> str | None:
    entries = symbol_entries.get(symbol_name) or []
    for entry in entries:
        target_id = _entry_target_id(entry)
        bridge_prefix = _bridge_prefix_for_entry(entry)
        namespace = target_namespaces.get(target_id or "")
        if not namespace or not bridge_prefix:
            continue
        prefix = f"{bridge_prefix}_"
        if symbol_name.startswith(prefix):
            return f"<{namespace}{_s(symbol_name[len(prefix):])}>"

    # Fallback for bridge symbols that are not explicitly located through
    # bridge_declared_in. Keep this conservative and deterministic.
    candidate_prefixes: list[tuple[str, str]] = []
    for target_id, namespace in target_namespaces.items():
        if m := re.fullmatch(r"section_(\d+)_(\d+)", target_id):
            candidate_prefixes.append((f"Section{m.group(1)}_{m.group(2)}", namespace))
        elif m := re.fullmatch(r"appendix_(\d+)_(\d+)", target_id):
            candidate_prefixes.append((f"Appendix{m.group(1)}_{m.group(2)}", namespace))
        elif re.fullmatch(r"N\d+", target_id):
            candidate_prefixes.append((target_id, namespace))
    for bridge_prefix, namespace in sorted(candidate_prefixes, key=lambda item: len(item[0]), reverse=True):
        prefix = f"{bridge_prefix}_"
        if symbol_name.startswith(prefix):
            return f"<{namespace}{_s(symbol_name[len(prefix):])}>"
    return None


def _resolution_node(left: str, right: str) -> str:
    return f"<http://example.org/a4v3/resolution#{_s(left)}__{_s(right)}>"


def _bridge_resolution_data(dz_root: Path) -> dict[str, Any]:
    bridge_path = dz_root / "bridge" / "main_bridge.a4v3"
    if not bridge_path.exists():
        return {"available": False, "message": "bridge/main_bridge.a4v3 not found"}

    ast = parse(bridge_path.read_text(encoding="utf-8"), strict=False)
    symbol_kinds: dict[str, str] = {}
    for decl in _symbol_decls(ast):
        if decl.get("kind") == "entity" and decl.get("name"):
            symbol_kinds[str(decl["name"])] = str(decl.get("sort") or "")

    calls: list[dict[str, Any]] = []
    for assertion in ast.get("assertions", []) or []:
        calls.extend(_iter_calls(assertion.get("expr")))

    pairs: dict[str, set[tuple[str, str]]] = {
        "same_index": set(),
        "same_sort": set(),
        "same_entity": set(),
        "same_relation": set(),
    }
    link_types: dict[tuple[str, str], str] = {}
    argument_orders: dict[tuple[str, str], str] = {}
    confidences: dict[tuple[str, str], str] = {}
    symbol_entries: dict[str, list[str]] = {}
    family_members: dict[str, list[str]] = {}
    family_link_types: dict[str, str] = {}
    family_confidences: dict[str, str] = {}

    for call in calls:
        callee = str(call.get("callee") or "")
        args = [_ref_name(arg) for arg in call.get("args", []) or []]
        if any(arg is None for arg in args):
            continue
        clean_args = [str(arg) for arg in args if arg is not None]
        if callee in pairs and len(clean_args) >= 2:
            pairs[callee].add((clean_args[0], clean_args[1]))
        elif callee == "bridge_link_type" and len(clean_args) >= 3:
            link_types[(clean_args[0], clean_args[1])] = clean_args[2]
        elif callee == "bridge_argument_order" and len(clean_args) >= 3:
            argument_orders[(clean_args[0], clean_args[1])] = clean_args[2]
        elif callee == "bridge_confidence" and len(clean_args) >= 3:
            confidences[(clean_args[0], clean_args[1])] = clean_args[2]
        elif callee == "bridge_declared_in" and len(clean_args) >= 2:
            symbol_entries.setdefault(clean_args[0], []).append(clean_args[1])
        elif callee == "bridge_family_member" and len(clean_args) >= 2:
            family_members.setdefault(clean_args[0], []).append(clean_args[1])
        elif callee == "bridge_family_link_type" and len(clean_args) >= 2:
            family_link_types[clean_args[0]] = clean_args[1]
        elif callee == "bridge_family_confidence" and len(clean_args) >= 2:
            family_confidences[clean_args[0]] = clean_args[1]

    return {
        "available": True,
        "bridge_path": str(bridge_path),
        "parse_warning_count": len(ast.get("warnings", []) or []),
        "symbol_kinds": symbol_kinds,
        "pairs": {key: sorted(value) for key, value in pairs.items()},
        "link_types": {f"{left}||{right}": value for (left, right), value in link_types.items()},
        "argument_orders": {f"{left}||{right}": value for (left, right), value in argument_orders.items()},
        "confidences": {f"{left}||{right}": value for (left, right), value in confidences.items()},
        "symbol_entries": symbol_entries,
        "family_members": family_members,
        "family_link_types": family_link_types,
        "family_confidences": family_confidences,
    }


def _review_attention(policy: str, reason: str, family: str | None) -> str:
    high_markers = (
        "IndexUniverse",
        "IndexAdjustment",
        "IndexComponent",
        "SecurityReflected",
        "RegionFunction",
        "IndexQuality",
        "AverageDailyValueTraded",
    )
    if policy == "not_equivalent_property":
        return "high"
    if family and any(marker in family for marker in high_markers):
        return "high"
    if policy == "family_relation_review_only":
        return "medium"
    if "non-identity link type" in reason:
        return "medium"
    return "low"


def _promotion_criteria(policy: str, link_type: str | None, order: str | None) -> str:
    if policy == "not_equivalent_property" and order == "ReversedArgumentOrder":
        return "Keep as adapter/inverse mapping, or add an explicit inverse-property/projection rule; do not use owl:equivalentProperty."
    if policy == "not_equivalent_property" and order and order.startswith("ScopedExtra"):
        return "Keep as scoped projection adapter, or reify the relation frame; do not use owl:equivalentProperty while arity differs."
    if policy == "family_relation_review_only":
        return "Promote only after adding pairwise same_relation plus bridge_argument_order(SameArgumentOrder), or an explicit adapter for scoped/reversed cases."
    if policy == "family_review_only" and link_type == "RelatedConcept":
        return "Promote only after a domain decision changes the bridge link type from RelatedConcept to a concrete alias/identity."
    if policy == "family_review_only" and link_type == "UnresolvedDrift":
        return "Promote only after resolving the drift and recording the chosen alias, adapter, or do-not-merge decision."
    return "Requires a bridge policy update with explicit identity, alias, or adapter evidence."


def _decision_attention(policy: str, family: str | None) -> str:
    if policy in {"resolved_as_inverse_adapter", "resolved_as_scoped_projection_adapter"}:
        return "high"
    if family and any(marker in family for marker in ("IndexComponent", "IndexUniverse", "IndexAdjustment", "AverageDailyValueTraded")):
        return "high"
    return "medium"


def _decision_criteria(policy: str) -> str:
    if policy == "resolved_as_inverse_adapter":
        return "Closed by owl:inverseOf because the bridge records ReversedArgumentOrder and both sides are binary relations."
    if policy == "resolved_as_scoped_projection_adapter":
        return "Closed by explicit adapter metadata because the target relation/function has an extra scope argument."
    if policy == "resolved_as_pairwise_signature_equivalence":
        return "Closed by owl:equivalentProperty because local declarations have identical relation/function signatures."
    if policy == "resolved_as_family_split":
        return "Closed as non-identity: this bridge family is an infrastructure cluster, not a complete graph of pairwise equivalent properties."
    if policy == "resolved_as_projection_family":
        return "Closed as a projection/frame mapping, not an OWL identity relation."
    if policy == "resolved_as_domain_specialized_relation":
        return "Closed as domain-specialized relation reuse: same surface predicate, different domain carrier, no owl:equivalentProperty."
    if policy == "resolved_as_non_identity_related_concept":
        return "Closed as related-but-not-identical; promotion would require changing the bridge link type to an explicit alias/identity."
    return "Closed by explicit resolved-layer policy."


def _write_resolved_review_reports(
    *,
    review_items_path: Path,
    review_summary_path: Path,
    review_items: list[dict[str, Any]],
    resolved_decisions: list[dict[str, Any]],
    counts: Counter[str],
    identity_axiom_count: int,
) -> None:
    by_policy = Counter(str(item.get("policy")) for item in review_items)
    by_attention = Counter(str(item.get("attention")) for item in review_items)
    decision_by_policy = Counter(str(item.get("policy")) for item in resolved_decisions)
    decision_by_attention = Counter(str(item.get("attention")) for item in resolved_decisions)
    by_family: dict[str, list[dict[str, Any]]] = {}
    for item in review_items:
        family = str(item.get("family") or "(direct pair)")
        by_family.setdefault(family, []).append(item)
    decisions_by_family: dict[str, list[dict[str, Any]]] = {}
    for item in resolved_decisions:
        family = str(item.get("family") or "(direct pair)")
        decisions_by_family.setdefault(family, []).append(item)

    family_rows: list[dict[str, Any]] = []
    for family, items in sorted(by_family.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        members = sorted({str(item["left"]) for item in items} | {str(item["right"]) for item in items})
        family_rows.append(
            {
                "family": family,
                "item_count": len(items),
                "policy_counts": dict(Counter(str(item.get("policy")) for item in items)),
                "attention_counts": dict(Counter(str(item.get("attention")) for item in items)),
                "link_types": sorted({str(item.get("link_type") or "unspecified") for item in items}),
                "argument_orders": sorted({str(item.get("argument_order") or "unspecified") for item in items}),
                "member_count": len(members),
                "sample_members": members[:8],
                "sample_pairs": [
                    {
                        "left": item["left"],
                        "right": item["right"],
                        "policy": item["policy"],
                        "attention": item["attention"],
                    }
                    for item in items[:6]
                ],
                "justification": items[0].get("reason"),
                "promotion_criteria": items[0].get("promotion_criteria"),
            }
        )

    payload = {
        "schema": "dz_owl_resolved_review_items_v1",
        "review_item_count": len(review_items),
        "resolved_decision_count": len(resolved_decisions),
        "identity_axiom_count": identity_axiom_count,
        "policy_counts": dict(by_policy),
        "attention_counts": dict(by_attention),
        "resolved_decision_policy_counts": dict(decision_by_policy),
        "resolved_decision_attention_counts": dict(decision_by_attention),
        "resolution_counts": dict(counts),
        "families": family_rows,
        "resolved_decisions": resolved_decisions,
        "items": review_items,
    }
    _write_json(review_items_path, payload)

    lines = [
        "# DZ OWL Resolved Review Items v1",
        "",
        "This report explains why the remaining bridge links were not promoted to strong OWL identity/equivalence axioms.",
        "It is not a waiver dump: each item is either an adapter case, a relation-family case without pairwise argument-order evidence, or a related-concept family that is intentionally weaker than identity.",
        "",
        "## Summary",
        "",
        f"- Strong identity/equivalence axioms emitted: `{identity_axiom_count}`",
        f"- Adapter / non-identity decisions closed: `{len(resolved_decisions)}`",
        f"- Review items: `{len(review_items)}`",
        f"- Resolved decision policy counts: `{json.dumps(dict(decision_by_policy), ensure_ascii=False)}`",
        f"- Resolved decision attention counts: `{json.dumps(dict(decision_by_attention), ensure_ascii=False)}`",
        f"- Open review policy counts: `{json.dumps(dict(by_policy), ensure_ascii=False)}`",
        f"- Open review attention counts: `{json.dumps(dict(by_attention), ensure_ascii=False)}`",
        "",
        "## Resolution Policy",
        "",
        "- `not_equivalent_property`: the bridge has a relation alias, but OWL property equivalence would be dishonest because argument order or arity differs.",
        "- `family_relation_review_only`: the bridge groups relations into a family, but the family does not provide pairwise argument-order evidence for every pair.",
        "- `family_review_only`: the bridge explicitly says `RelatedConcept` or another non-identity link type, so the resolved graph keeps it as a review/related link.",
        "",
        "## Closed Adapter / Non-Identity Decisions",
        "",
        "| Family | Decisions | Attention | Policies | Why Closed | Samples |",
        "| --- | ---: | --- | --- | --- | --- |",
    ]
    for family, items in sorted(decisions_by_family.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        attention = ", ".join(f"{k}:{v}" for k, v in Counter(str(item.get("attention")) for item in items).items())
        policies = ", ".join(f"{k}:{v}" for k, v in Counter(str(item.get("policy")) for item in items).items())
        samples = "; ".join(f"{item['left']} ↔ {item['right']}" for item in items[:3])
        reasons = sorted({str(item.get("reason") or "") for item in items})
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{family}`",
                    str(len(items)),
                    f"`{attention}`",
                    f"`{policies}`",
                    str(reasons[0] if reasons else ""),
                    f"`{samples}`",
                ]
            )
            + " |"
        )

    lines.extend(["", "## Open Review Items", ""])
    if not family_rows:
        lines.append("No open review items remain after adapter/projection/non-identity resolution.")
    else:
        lines.extend(
            [
                "| Family | Items | Attention | Link Types | Argument Orders | Why Not Strong OWL | Promotion Criteria | Samples |",
                "| --- | ---: | --- | --- | --- | --- | --- | --- |",
            ]
        )
    for row in family_rows:
        attention = ", ".join(f"{k}:{v}" for k, v in row["attention_counts"].items())
        samples = "; ".join(f"{p['left']} ↔ {p['right']}" for p in row["sample_pairs"][:3])
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{row['family']}`",
                    str(row["item_count"]),
                    f"`{attention}`",
                    f"`{', '.join(row['link_types'])}`",
                    f"`{', '.join(row['argument_orders'])}`",
                    str(row["justification"] or ""),
                    str(row["promotion_criteria"] or ""),
                    f"`{samples}`",
                ]
            )
            + " |"
        )

    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "A review item is not an uncovered token and not a hidden merge failure.",
            "It is a recorded refusal to make a stronger OWL claim than the bridge evidence supports.",
            "High-attention items are the ones worth reading first before a final thesis/report claim that all semantic merge decisions are closed.",
        ]
    )
    _write_text(review_summary_path, "\n".join(lines) + "\n")


def _write_resolved_owl_union(dz_root: Path, out_root: Path, union_report: dict[str, Any]) -> dict[str, Any]:
    union_path = Path(union_report["union_path"])
    manifest_path = Path(union_report["manifest_path"])
    union_dir = union_path.parent
    resolved_path = union_dir / "dz_owl_resolved.ttl"
    resolved_manifest_path = union_dir / "dz_owl_resolved_manifest.json"
    resolved_check_path = union_dir / "dz_owl_resolved.check.json"
    review_items_path = union_dir / "dz_owl_resolved_review_items_v1.json"
    review_summary_path = union_dir / "dz_owl_resolved_review_items_summary.md"

    if not union_path.exists() or not manifest_path.exists():
        return {"status": "error", "message": "OWL union or manifest is missing"}

    union_text = union_path.read_text(encoding="utf-8")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    target_namespaces = {entry["target_id"]: entry["namespace"] for entry in manifest.get("entries", [])}
    target_paths = {entry["target_id"]: dz_root / entry["relative_path"] for entry in manifest.get("entries", [])}
    bridge = _bridge_resolution_data(dz_root)

    if not bridge.get("available"):
        resolved_text = union_text + "\n# Resolved bridge layer skipped: bridge unavailable.\n"
        _write_text(resolved_path, resolved_text)
        check = _check_owl(resolved_text)
        _write_json(resolved_check_path, check)
        result = {
            "schema": "dz_owl_resolved_manifest_v1",
            "status": "skipped",
            "message": bridge.get("message"),
            "resolved_path": str(resolved_path),
            "check_path": str(resolved_check_path),
            "check": check,
        }
        _write_json(resolved_manifest_path, result)
        return result

    symbol_entries = bridge["symbol_entries"]
    symbol_kinds = bridge["symbol_kinds"]

    def symbol_iri(symbol: str) -> str | None:
        return _bridge_symbol_iri(symbol, symbol_entries=symbol_entries, target_namespaces=target_namespaces)

    decl_cache: dict[Path, dict[str, dict[str, Any]]] = {}

    def local_decl(symbol: str) -> dict[str, Any] | None:
        for entry in symbol_entries.get(symbol, []) or []:
            target_id = _entry_target_id(entry)
            bridge_prefix = _bridge_prefix_for_entry(entry)
            path = target_paths.get(target_id or "")
            if not path or not path.exists() or not bridge_prefix:
                continue
            prefix = f"{bridge_prefix}_"
            if not symbol.startswith(prefix):
                continue
            local_name = symbol[len(prefix):]
            if path not in decl_cache:
                ast = parse(path.read_text(encoding="utf-8"), strict=False)
                decl_cache[path] = {str(d.get("name")): d for d in ast.get("declarations", []) or [] if d.get("name")}
            decl = decl_cache[path].get(local_name)
            if decl:
                return decl
        return None

    def pairwise_signature_equivalent(left: str, right: str) -> bool:
        left_decl = local_decl(left)
        right_decl = local_decl(right)
        if not left_decl or not right_decl:
            return False
        if left_decl.get("family") != "SymbolDecl" or right_decl.get("family") != "SymbolDecl":
            return False
        if left_decl.get("kind") != right_decl.get("kind"):
            return False
        if left_decl.get("kind") not in {"rel", "fun"}:
            return False
        if left_decl.get("name") != right_decl.get("name"):
            return False
        if (left_decl.get("args") or []) != (right_decl.get("args") or []):
            return False
        if left_decl.get("kind") == "fun" and left_decl.get("result_sort") != right_decl.get("result_sort"):
            return False
        return True

    def binary_relation_pair(left: str, right: str) -> bool:
        left_decl = local_decl(left)
        right_decl = local_decl(right)
        return bool(
            left_decl
            and right_decl
            and left_decl.get("family") == "SymbolDecl"
            and right_decl.get("family") == "SymbolDecl"
            and left_decl.get("kind") == "rel"
            and right_decl.get("kind") == "rel"
            and len(left_decl.get("args") or []) == 2
            and len(right_decl.get("args") or []) == 2
        )

    def pair_meta(left: str, right: str) -> tuple[str | None, str | None, str | None]:
        key = f"{left}||{right}"
        rev = f"{right}||{left}"
        return (
            bridge["link_types"].get(key) or bridge["link_types"].get(rev),
            bridge["argument_orders"].get(key) or bridge["argument_orders"].get(rev),
            bridge["confidences"].get(key) or bridge["confidences"].get(rev),
        )

    safe_sort_links = {"SortAlias", "CrossSectionIdentity", "SourceAlias", "TickerAlias"}
    safe_entity_links = {"EntityAlias", "CrossSectionIdentity", "SourceAlias", "TickerAlias"}
    safe_relation_links = {"RelationAlias", "CrossSectionIdentity", "SourceAlias", "TickerAlias"}
    blocked_links = {"RelatedConcept", "UnresolvedDrift", "ScopedRelationAlias"}

    triples: set[str] = set()
    annotation_lines: list[str] = []
    review_items: list[dict[str, Any]] = []
    resolved_decisions: list[dict[str, Any]] = []
    decision_lines: list[str] = []
    unresolved_symbols: Counter[str] = Counter()
    counts: Counter[str] = Counter()

    def add_decision(
        left: str,
        right: str,
        *,
        policy: str,
        reason: str,
        link_type: str | None,
        confidence: str | None,
        order: str | None = None,
        family: str | None = None,
        adapter_kind: str | None = None,
    ) -> None:
        node = _resolution_node(f"{policy}_{left}", right)
        left_iri = symbol_iri(left)
        right_iri = symbol_iri(right)
        attention = _decision_attention(policy, family)
        criteria = _decision_criteria(policy)
        resolved_decisions.append(
            {
                "left": left,
                "right": right,
                "family": family,
                "policy": policy,
                "reason": reason,
                "link_type": link_type or "unspecified",
                "confidence": confidence or "unspecified",
                "argument_order": order or "unspecified",
                "adapter_kind": adapter_kind or "none",
                "attention": attention,
                "evidence": criteria,
            }
        )
        decision_lines.extend(
            [
                f"{node} a a4:BridgeResolutionDecision ;",
                f"  a4:leftBridgeSymbol {_lit(left)} ;",
                f"  a4:rightBridgeSymbol {_lit(right)} ;",
                f"  a4:bridgeFamily {_lit(family or 'direct_pair')} ;",
                f"  a4:resolutionPolicy {_lit(policy)} ;",
                f"  a4:resolutionReason {_lit(reason)} ;",
                f"  a4:resolutionAttention {_lit(attention)} ;",
                f"  a4:promotionCriteria {_lit(criteria)} ;",
                f"  a4:bridgeLinkType {_lit(link_type or 'unspecified')} ;",
                f"  a4:bridgeConfidence {_lit(confidence or 'unspecified')} ;",
                f"  a4:bridgeArgumentOrder {_lit(order or 'unspecified')} ;",
                f"  a4:adapterKind {_lit(adapter_kind or 'none')} .",
            ]
        )
        if left_iri and right_iri:
            decision_lines.append(f"{node} a4:sourceResource {left_iri} ; a4:targetResource {right_iri} .")
        counts[f"decision:{policy}"] += 1

    def add_annotation(
        left: str,
        right: str,
        *,
        policy: str,
        reason: str,
        link_type: str | None,
        confidence: str | None,
        order: str | None = None,
        family: str | None = None,
    ) -> None:
        node = _resolution_node(left, right)
        attention = _review_attention(policy, reason, family)
        criteria = _promotion_criteria(policy, link_type, order)
        review_items.append(
            {
                "left": left,
                "right": right,
                "family": family,
                "policy": policy,
                "reason": reason,
                "link_type": link_type or "unspecified",
                "confidence": confidence or "unspecified",
                "argument_order": order or "unspecified",
                "attention": attention,
                "promotion_criteria": criteria,
            }
        )
        annotation_lines.extend(
            [
                f"{node} a a4:BridgeResolutionReviewItem ;",
                f"  a4:leftBridgeSymbol {_lit(left)} ;",
                f"  a4:rightBridgeSymbol {_lit(right)} ;",
                f"  a4:bridgeFamily {_lit(family or 'direct_pair')} ;",
                f"  a4:resolutionPolicy {_lit(policy)} ;",
                f"  a4:resolutionReason {_lit(reason)} ;",
                f"  a4:resolutionAttention {_lit(attention)} ;",
                f"  a4:promotionCriteria {_lit(criteria)} ;",
                f"  a4:bridgeLinkType {_lit(link_type or 'unspecified')} ;",
                f"  a4:bridgeConfidence {_lit(confidence or 'unspecified')} ;",
                f"  a4:bridgeArgumentOrder {_lit(order or 'unspecified')} .",
            ]
        )
        counts[f"annotation:{policy}"] += 1

    def add_direct(left: str, right: str, predicate: str, *, source: str, link_type: str | None, confidence: str | None) -> None:
        left_iri = symbol_iri(left)
        right_iri = symbol_iri(right)
        if not left_iri:
            unresolved_symbols[left] += 1
        if not right_iri:
            unresolved_symbols[right] += 1
        if not left_iri or not right_iri or left_iri == right_iri:
            if not left_iri or not right_iri:
                add_annotation(left, right, policy="unresolved_symbol", reason=f"{source} could not map both bridge symbols to union IRIs", link_type=link_type, confidence=confidence)
            return
        triples.add(f"{left_iri} {predicate} {right_iri} .")
        triples.add(f"{left_iri} a4:resolvedWithBridgeSymbol {_lit(left)} .")
        triples.add(f"{right_iri} a4:resolvedWithBridgeSymbol {_lit(right)} .")
        counts[f"axiom:{predicate}:{source}"] += 1

    for left, right in bridge["pairs"].get("same_sort", []):
        link_type, order, confidence = pair_meta(left, right)
        if (link_type in safe_sort_links) or link_type is None:
            add_direct(left, right, "owl:equivalentClass", source="same_sort", link_type=link_type, confidence=confidence)
        else:
            add_annotation(left, right, policy="not_equivalent_class", reason="bridge link type is not a safe sort identity", link_type=link_type, confidence=confidence, order=order)

    for rel_name in ("same_entity", "same_index"):
        for left, right in bridge["pairs"].get(rel_name, []):
            link_type, order, confidence = pair_meta(left, right)
            if (link_type in safe_entity_links) or link_type is None:
                add_direct(left, right, "owl:sameAs", source=rel_name, link_type=link_type, confidence=confidence)
            else:
                add_annotation(left, right, policy="not_same_as", reason="bridge link type is not a safe entity identity", link_type=link_type, confidence=confidence, order=order)

    for left, right in bridge["pairs"].get("same_relation", []):
        link_type, order, confidence = pair_meta(left, right)
        if ((link_type in safe_relation_links) or link_type is None) and order == "SameArgumentOrder":
            add_direct(left, right, "owl:equivalentProperty", source="same_relation", link_type=link_type, confidence=confidence)
        elif order == "ReversedArgumentOrder" and binary_relation_pair(left, right):
            left_iri = symbol_iri(left)
            right_iri = symbol_iri(right)
            if left_iri and right_iri:
                triples.add(f"{left_iri} owl:inverseOf {right_iri} .")
                counts["axiom:owl:inverseOf:reversed_relation_adapter"] += 1
            add_decision(
                left,
                right,
                policy="resolved_as_inverse_adapter",
                reason="bridge records ReversedArgumentOrder for binary relations",
                link_type=link_type,
                confidence=confidence,
                order=order,
                adapter_kind="inverse_property",
            )
        elif order and order.startswith("ScopedExtra"):
            add_decision(
                left,
                right,
                policy="resolved_as_scoped_projection_adapter",
                reason="bridge records a scoped alias with an extra context argument",
                link_type=link_type,
                confidence=confidence,
                order=order,
                adapter_kind="scoped_projection",
            )
        else:
            add_annotation(
                left,
                right,
                policy="not_equivalent_property",
                reason="relation aliases require SameArgumentOrder; scoped or reversed aliases are preserved as review links",
                link_type=link_type,
                confidence=confidence,
                order=order,
            )

    for family, members in sorted(bridge["family_members"].items()):
        link_type = bridge["family_link_types"].get(family)
        confidence = bridge["family_confidences"].get(family)
        unique_members = sorted(set(members))
        if len(unique_members) < 2:
            continue
        if link_type in blocked_links:
            for idx, left in enumerate(unique_members):
                for right in unique_members[idx + 1 :]:
                    family_policy = "resolved_as_projection_family" if family in {
                        "AverageDailyValueTradedFamily",
                        "CanonicalIndexComponentRelationFamily",
                        "CanonicalIndexUniverseRelationFamily",
                        "IndexAdjustmentRelationReviewFamily",
                        "RegionFunctionFamily",
                    } else "resolved_as_non_identity_related_concept"
                    add_decision(
                        left,
                        right,
                        policy=family_policy,
                        reason=f"{family} has non-identity link type and is resolved below OWL equality",
                        link_type=link_type,
                        confidence=confidence,
                        family=family,
                        adapter_kind="projection_or_related_cluster",
                    )
            continue
        for idx, left in enumerate(unique_members):
            for right in unique_members[idx + 1 :]:
                left_kind = symbol_kinds.get(left)
                right_kind = symbol_kinds.get(right)
                if left_kind != right_kind:
                    add_annotation(left, right, policy="family_mixed_symbol_kinds", reason=f"{family} contains mixed bridge symbol sorts", link_type=link_type, confidence=confidence, family=family)
                    continue
                if left_kind == "BridgeSort" and link_type in safe_sort_links:
                    add_direct(left, right, "owl:equivalentClass", source=f"family:{family}", link_type=link_type, confidence=confidence)
                elif left_kind in {"BridgeEntity", "BridgeIndex"} and link_type in safe_entity_links:
                    add_direct(left, right, "owl:sameAs", source=f"family:{family}", link_type=link_type, confidence=confidence)
                elif left_kind == "BridgeRelation":
                    if link_type in safe_relation_links and pairwise_signature_equivalent(left, right):
                        add_direct(left, right, "owl:equivalentProperty", source=f"family_signature:{family}", link_type=link_type, confidence=confidence)
                        add_decision(
                            left,
                            right,
                            policy="resolved_as_pairwise_signature_equivalence",
                            reason="family relation pair has matching local name and exact local signature",
                            link_type=link_type,
                            confidence=confidence,
                            family=family,
                            adapter_kind="signature_equivalence",
                        )
                    elif family == "GenericDocumentAvailabilityRelationFamily":
                        add_decision(
                            left,
                            right,
                            policy="resolved_as_family_split",
                            reason="generic document availability family is an infrastructure cluster, not a complete pairwise property equivalence class",
                            link_type=link_type,
                            confidence=confidence,
                            family=family,
                            adapter_kind="family_split",
                        )
                    elif family in {"AnnouncementOnRelationFamily", "FullyRuleBasedRelationFamily"}:
                        add_decision(
                            left,
                            right,
                            policy="resolved_as_domain_specialized_relation",
                            reason=f"{family} reuses the same predicate wording over different domain carriers",
                            link_type=link_type,
                            confidence=confidence,
                            family=family,
                            adapter_kind="domain_specialization",
                        )
                    else:
                        add_annotation(
                            left,
                            right,
                            policy="family_relation_review_only",
                            reason="relation families do not carry pairwise argument-order evidence",
                            link_type=link_type,
                            confidence=confidence,
                            family=family,
                        )
                else:
                    add_annotation(left, right, policy="family_unresolved_policy", reason=f"no safe OWL resolution policy for {family}", link_type=link_type, confidence=confidence, family=family)

    resolution_block = [
        "",
        "# --- resolved bridge layer ---",
        "# Safe identity/alias decisions from bridge/main_bridge.a4v3.",
        "# RelatedConcept, UnresolvedDrift, scoped aliases, and reversed relation aliases are review annotations, not OWL equality.",
        "",
    ]
    resolution_block.extend(sorted(triples))
    if decision_lines:
        resolution_block.extend(["", "# --- bridge adapter / non-identity resolution decisions ---"])
        resolution_block.extend(decision_lines)
    if annotation_lines:
        resolution_block.extend(["", "# --- bridge review annotations ---"])
        resolution_block.extend(annotation_lines)

    resolved_text = union_text.rstrip() + "\n" + "\n".join(resolution_block).rstrip() + "\n"
    _write_text(resolved_path, resolved_text)
    check = _check_owl(resolved_text)
    _write_json(resolved_check_path, check)

    identity_axiom_count = sum(value for key, value in counts.items() if key.startswith("axiom:"))
    review_item_count = sum(value for key, value in counts.items() if key.startswith("annotation:"))
    _write_resolved_review_reports(
        review_items_path=review_items_path,
        review_summary_path=review_summary_path,
        review_items=review_items,
        resolved_decisions=resolved_decisions,
        counts=counts,
        identity_axiom_count=identity_axiom_count,
    )

    result = {
        "schema": "dz_owl_resolved_manifest_v1",
        "status": "ok" if check.get("status") == "ok" else "check_failed",
        "union_path": str(union_path),
        "resolved_path": str(resolved_path),
        "manifest_path": str(resolved_manifest_path),
        "check_path": str(resolved_check_path),
        "review_items_path": str(review_items_path),
        "review_summary_path": str(review_summary_path),
        "bridge_path": bridge.get("bridge_path"),
        "bridge_parse_warning_count": bridge.get("parse_warning_count"),
        "resolution_counts": dict(counts),
        "identity_axiom_count": identity_axiom_count,
        "resolved_triple_count": len(triples),
        "resolved_decision_count": len(resolved_decisions),
        "review_item_count": review_item_count,
        "review_annotation_line_count": len(annotation_lines),
        "unresolved_symbol_count": sum(unresolved_symbols.values()),
        "unresolved_symbols": dict(unresolved_symbols),
        "check": check,
    }
    _write_json(resolved_manifest_path, result)
    return result


def _write_markdown(report: dict[str, Any], out_path: Path) -> None:
    lines = ["# DZ Backend Projection Report v1", ""]
    lines.append(f"Status: `{report['status']}`")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    for key in [
        "target_count",
        "target_count_by_kind",
        "backend_check_status_counts",
        "backend_emission_diagnostic_counts",
        "hard_findings",
        "soft_findings",
        "advisory_findings",
    ]:
        lines.append(f"- `{key}`: `{json.dumps(report.get(key), ensure_ascii=False)}`")
    if report.get("smt_probe_summary"):
        lines.append(f"- `smt_probe_summary`: `{json.dumps(report['smt_probe_summary'], ensure_ascii=False)}`")
    if report.get("owl_union"):
        lines.append(f"- `owl_union`: `{json.dumps(report['owl_union'], ensure_ascii=False)}`")
    if report.get("owl_resolved"):
        lines.append(f"- `owl_resolved`: `{json.dumps(report['owl_resolved'], ensure_ascii=False)}`")
    lines.append("")
    lines.append("## Backend Meaning")
    lines.append("")
    lines.append("- `rdf.ttl`: structural graph projection of A4V3 declarations and assertions.")
    lines.append("- `owl.ttl`: OWL/RDF ontology-style projection of sorts, entities, and simple properties.")
    lines.append("- `shacl_shapes.ttl`: SHACL structural validation shapes for supported unary/binary symbols.")
    lines.append("- SMT is linked through the dedicated `smt_probe_runner_v1` report instead of duplicated here.")
    lines.append("")
    lines.append("## Targets")
    lines.append("")
    lines.append("| Target | Kind | RDF | OWL | SHACL | Diagnostics |")
    lines.append("| --- | --- | --- | --- | --- | ---: |")
    for target in report["targets"]:
        backends = target["backends"]
        diag_count = sum(int(payload["emission"].get("diagnostic_count", 0)) for payload in backends.values())
        lines.append(
            f"| `{target['target_id']}` | `{target['target_kind']}` | "
            f"`{backends['rdf']['check'].get('status')}` | "
            f"`{backends['owl']['check'].get('status')}` | "
            f"`{backends['shacl']['check'].get('status')}` | {diag_count} |"
        )
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dz-root", default="IR/outputs/runs/dz")
    parser.add_argument("--out-root", default=None)
    args = parser.parse_args()

    dz_root = Path(args.dz_root)
    out_root = Path(args.out_root) if args.out_root else dz_root / "backend_projection"
    report = run_pass(dz_root, out_root)
    _write_json(out_root / "backend_projection_report_v1.json", report)
    _write_markdown(report, out_root / "backend_projection_report_v1.md")
    print(
        json.dumps(
            {
                "status": report["status"],
                "target_count": report["target_count"],
                "target_count_by_kind": report["target_count_by_kind"],
                "backend_check_status_counts": report["backend_check_status_counts"],
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
