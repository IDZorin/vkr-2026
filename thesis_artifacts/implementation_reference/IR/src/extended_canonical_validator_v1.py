"""extended_canonical_validator_v1.py

Расширенный валидатор canonical AST поверх существующего
`run_advisor_drafter_experiment._validate_canonical_drafter_payload`.

Принимает дополнительно:
  - expression kinds: `gt`, `lt`, `gte`, `lte` со структурой `{kind, left, right}`
    (как `eq`/`add` в оригинале).
  - sort declarations с опциональным полем `enum_members: [str, ...]` (для
    value families вроде `GbsFrameworkAssignment = A | B | C`).

Реализован через monkey-patch модуля `run_advisor_drafter_experiment` на
время вызова. Сам файл валидатора в `thoughts/` не трогается.

Документ контракта: `IR/index/canonical_ast_format_extensions_v1.md`.
"""
from __future__ import annotations
import json, pathlib, sys
from contextlib import contextmanager

_SCRIPTS = pathlib.Path(r"<WORKSPACE_ROOT>/thoughts/IR_schema/scripts")
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

import run_advisor_drafter_experiment as _ir_stage  # noqa: E402

EXTENDED_COMPARISON_KINDS: frozenset[str] = frozenset({"gt", "lt", "gte", "lte"})
# `count` имеет ту же форму что `set_comp` (binder + predicate), но возвращает
# число вместо множества (cardinality). Принимаем тоже.
EXTENDED_BINDER_PREDICATE_KINDS: frozenset[str] = frozenset({"count"})


def _ext_validate_expr(expr, path, errors):
    """Extended expression validator — supports gt/lt/gte/lte and count plus original kinds."""
    if isinstance(expr, dict):
        kind = expr.get("kind")
        if isinstance(kind, str):
            kind = kind.strip()
            if kind in EXTENDED_COMPARISON_KINDS:
                _ir_stage._validate_exact_keys(expr, {"kind", "left", "right"}, path, errors)
                if "left" not in expr:
                    errors.append(f"{path}.left: missing")
                else:
                    _ext_validate_expr(expr.get("left"), f"{path}.left", errors)
                if "right" not in expr:
                    errors.append(f"{path}.right: missing")
                else:
                    _ext_validate_expr(expr.get("right"), f"{path}.right", errors)
                return
            if kind in EXTENDED_BINDER_PREDICATE_KINDS:
                _ir_stage._validate_exact_keys(expr, {"kind", "binder", "predicate"}, path, errors)
                _ir_stage._validate_canonical_var_decl(expr.get("binder"), f"{path}.binder", errors)
                if "predicate" not in expr:
                    errors.append(f"{path}.predicate: missing")
                else:
                    _ext_validate_expr(expr.get("predicate"), f"{path}.predicate", errors)
                return
    # Fall back to original (which recurses through module-level
    # `_validate_canonical_expr`, currently patched to point here).
    _orig_validate_expr(expr, path, errors)


def _ext_validate_declaration(payload, path, errors):
    """Extended declaration validator — supports enum_members and subtype parent on sort."""
    if isinstance(payload, dict) and payload.get("decl") == "sort" and "enum_members" in payload:
        _ir_stage._validate_exact_keys(payload, {"decl", "name", "enum_members"}, path, errors)
        _ir_stage._validate_nonempty_string(payload.get("name"), f"{path}.name", errors)
        members = payload.get("enum_members")
        if not isinstance(members, list) or not members:
            errors.append(f"{path}.enum_members: expected non-empty list")
        else:
            seen = set()
            for idx, m in enumerate(members):
                _ir_stage._validate_nonempty_string(m, f"{path}.enum_members[{idx}]", errors)
                if isinstance(m, str):
                    if m in seen:
                        errors.append(f"{path}.enum_members[{idx}]: duplicate `{m}`")
                    seen.add(m)
        return
    if isinstance(payload, dict) and payload.get("decl") == "sort" and "parent" in payload:
        _ir_stage._validate_exact_keys(payload, {"decl", "name", "parent"}, path, errors)
        _ir_stage._validate_nonempty_string(payload.get("name"), f"{path}.name", errors)
        _ir_stage._validate_nonempty_string(payload.get("parent"), f"{path}.parent", errors)
        return
    _orig_validate_declaration(payload, path, errors)


# Save originals for fallback
_orig_validate_expr = _ir_stage._validate_canonical_expr
_orig_validate_declaration = _ir_stage._validate_canonical_declaration


@contextmanager
def _patched_validators():
    """Temporarily replace module-level validators with extended versions."""
    _ir_stage._validate_canonical_expr = _ext_validate_expr
    _ir_stage._validate_canonical_declaration = _ext_validate_declaration
    try:
        yield
    finally:
        _ir_stage._validate_canonical_expr = _orig_validate_expr
        _ir_stage._validate_canonical_declaration = _orig_validate_declaration


def validate_extended(payload: dict) -> list[str]:
    """Validate canonical drafter payload with extensions accepted."""
    with _patched_validators():
        return _ir_stage._validate_canonical_drafter_payload(payload)


def validate_strict(payload: dict) -> list[str]:
    """Validate with original strict validator (for comparison)."""
    return _ir_stage._validate_canonical_drafter_payload(payload)


def build_canonical_payload_from_artifact(artifact: dict) -> dict:
    """Extract the drafter result from artifact JSON wrapper.

    `*_manual_section_workspace_artifact_current_v1.json` оборачивает в
    `ir_stage.drafter.result`; для определений это `ir_stage.drafter.result`
    того же.
    """
    drafter = (artifact.get("ir_stage") or {}).get("drafter") or {}
    result = drafter.get("result") or {}
    return {
        "schema_version": result.get("schema_version", ""),
        "focus_term": result.get("focus_term", ""),
        "ir_ast": result.get("ir_ast", {}),
        "rendering_notes": result.get("rendering_notes", []),
        "primitive_usage": result.get("primitive_usage", []),
        "strengths": result.get("strengths", []),
        "residual_risks": result.get("residual_risks", []),
    }


def validate_artifact_file(artifact_path: pathlib.Path) -> dict:
    """Load artifact JSON, run both validators, return summary."""
    art = json.loads(pathlib.Path(artifact_path).read_text(encoding="utf-8"))
    payload = build_canonical_payload_from_artifact(art)
    strict_errors = validate_strict(payload)
    ext_errors = validate_extended(payload)
    return {
        "artifact": str(artifact_path),
        "ast_valid_strict": int(not strict_errors),
        "ast_error_count_strict": len(strict_errors),
        "errors_strict": strict_errors,
        "ast_valid_extended": int(not ext_errors),
        "ast_error_count_extended": len(ext_errors),
        "errors_extended": ext_errors,
    }


def main() -> None:
    """CLI: print validation summary for each artifact passed as argv."""
    if len(sys.argv) <= 1:
        print("usage: extended_canonical_validator_v1.py <artifact.json> [more...]")
        sys.exit(2)
    for p in sys.argv[1:]:
        result = validate_artifact_file(pathlib.Path(p))
        print(f"=== {pathlib.Path(p).name} ===")
        print(f"  strict:   ast_valid={result['ast_valid_strict']}, errors={result['ast_error_count_strict']}")
        print(f"  extended: ast_valid={result['ast_valid_extended']}, errors={result['ast_error_count_extended']}")
        if result["errors_extended"]:
            print("  extended errors (real bugs, not format quirks):")
            for e in result["errors_extended"]:
                print(f"    - {e}")


if __name__ == "__main__":
    main()
