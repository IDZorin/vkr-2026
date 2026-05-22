"""a4v3_grammar.py — single source of truth for a4v3 surface syntax.

Reads the bundled public syntax summary from `IR/index/a4v3_spec_public_v1.json`.
The full research repository keeps larger internal spec workbooks; this public
bundle intentionally ships the compact surface grammar needed by the parser,
lint, coverage, and lowering checks.

Replaces the previously-scattered hardcoded keyword lists in:
  - a4v3_parser_v1._BLOCK_KEYWORDS
  - extended_grounding_check_v1._A4V3_KEYWORDS
  - translator/L6_validate.valid_keywords
  - legacy_metrics/compute_translation_metrics_v1._IR_SYNTAX_TOKENS
  - any other place that hardcodes a4v3 syntax tokens

API:
  load_spec()                  → raw JSON dict
  families()                   → tuple of 12 family names
  kinds(family)                → tuple of allowed kinds (DERIVED FROM JSON)
  block_keywords()             → frozenset of top-level decl keywords
  expression_keywords()        → frozenset of in-expression operators / fields
  all_keywords()               → union of the above (for content_token exclusion)
  notation_reference_keywords() → 91-keyword surface lexicon from spec sheet
  spec_path()                  → path of the active spec file
  spec_version()               → version tag (e.g. "v50" from filename)

Override:
  Set `A4V3_SPEC_PATH=/abs/path/to/spec.json` to test another compatible
  syntax summary.
"""
from __future__ import annotations
import json
import os
import pathlib
import re
from functools import lru_cache

ROOT = pathlib.Path(__file__).resolve().parents[2]
SPEC_DIR = ROOT / "IR/index"


# Stable families (the 12 INNF top-level families) — these names are part
# of the a4v3 v3 contract. Adding a new family is a major spec change and
# requires updating both the JSON spec AND this constant.
FAMILIES: tuple[str, ...] = (
    "TypeDecl", "SymbolDecl", "AssertDecl", "PathDecl", "ActionDecl",
    "TemporalDecl", "DeonticDecl", "ValidationDecl", "ProbabilisticDecl",
    "GameDecl", "GraphDecl", "TheoremDecl",
)


# Family → top-level declaration keywords. These are stable (the surface
# keywords for each family are part of the v3 contract). Kinds within a
# family change more often (e.g. adding `until` to TemporalDecl) — those
# ARE derived from the JSON via kinds(family).
_FAMILY_TO_BLOCK_KW: dict[str, tuple[str, ...]] = {
    "TypeDecl":          ("sort", "struct"),
    "SymbolDecl":        ("entity", "val", "fun", "rel", "event", "var", "property"),
    "AssertDecl":        ("fact", "constraint", "axiom", "key", "disjoint", "init"),
    "PathDecl":          ("path",),
    "ActionDecl":        ("action",),
    "TemporalDecl":      ("prop", "fairness"),
    "DeonticDecl":       ("obligation", "permission", "prohibition"),
    "ValidationDecl":    ("target", "closed", "deactivated", "sparql_constraint"),
    "ProbabilisticDecl": ("dist", "distribution", "reward", "utility", "objective"),
    "GameDecl":          ("obs", "indist"),
    "GraphDecl":         ("dataset", "reify"),
    "TheoremDecl":       ("theorem", "checked"),
}

_BUILTIN_KINDS: dict[str, tuple[str, ...]] = {
    "TypeDecl": ("opaque", "enum", "inductive", "record"),
    "SymbolDecl": ("const", "rel", "fun", "pred"),
    "AssertDecl": ("plain", "key_identity", "key_validation", "init"),
    "PathDecl": ("compose", "inverse", "closure", "closure_star"),
    "ActionDecl": ("action", "guard", "effect", "frame", "legality", "update"),
    "TemporalDecl": ("always", "eventually", "once", "next", "until", "since", "fairness"),
    "DeonticDecl": ("permission", "obligation", "prohibition"),
    "ValidationDecl": ("target", "closed", "deactivated", "property_shape", "sparql_constraint"),
    "ProbabilisticDecl": ("distribution", "reward", "utility", "reachability", "objective"),
    "GameDecl": ("choice", "choice_kind", "information_set", "observation", "payoff"),
    "GraphDecl": ("dataset", "reification"),
    "TheoremDecl": ("open", "checked"),
}


# Expression-internal operators / binders / field names. Spans logical,
# arithmetic, comparison, set, temporal, action, and decl-field token
# categories. Stable across spec versions; new operators would require
# updating this constant alongside the JSON spec.
_EXPRESSION_KW: frozenset[str] = frozenset({
    # logical
    "forall", "exists", "and", "or", "not", "implies", "iff", "ite",
    "let", "in", "true", "false",
    # comparison
    "eq", "gt", "lt", "gte", "lte",
    # arithmetic
    "add", "sub", "mul", "div", "mod", "abs",
    # set / collection
    "count", "set_comp", "union", "inter", "diff", "minus", "member",
    "where", "exactly", "seq", "sequence", "list", "first", "second",
    "nil", "cons",
    # temporal — derived from TemporalDecl.kinds + LTL operator literals
    "always", "eventually", "once", "next", "until", "since", "fairness",
    # action update ops
    "assign", "map_set", "relation_add", "relation_del",
    "override", "identity", "unchanged",
    # decl field / role names
    "agent", "target", "action", "deadline", "scope", "exception",
    "priority", "guard", "effect", "frame", "params", "parameters",
    "kind", "purpose", "source", "key",
    # type modifiers
    "opaque", "abstract", "extends", "recursive", "reflexive",
    "transitive", "multiplicity", "constructors", "match", "rec",
    # extras
    "by", "arg", "cardinality", "init", "checked", "wf", "p_max",
    "prime", "state", "type", "only", "restrict", "statement",
    "maximize", "reward", "utility", "legal", "prob", "date",
})


def _extract_spec_version(path: pathlib.Path) -> int:
    """Pick numeric N from `a4v3_full (N).json`-style filename. -1 if absent."""
    m = re.search(r"\((\d+)\)", path.stem)
    return int(m.group(1)) if m else -1


@lru_cache(maxsize=1)
def spec_path() -> pathlib.Path:
    """Path of the active a4v3 spec file.

    Override with env var `A4V3_SPEC_PATH=/abs/path/to/spec.json`.
    Default: bundled `IR/index/a4v3_spec_public_v1.json`.
    """
    override = os.environ.get("A4V3_SPEC_PATH")
    if override:
        p = pathlib.Path(override)
        if not p.exists():
            raise RuntimeError(f"A4V3_SPEC_PATH={override!r} does not exist")
        return p
    candidates = list(SPEC_DIR.glob("a4v3_spec*.json")) + list(SPEC_DIR.glob("a4v3_full*.json"))
    if not candidates:
        raise RuntimeError(
            f"No a4v3_spec*.json or a4v3_full*.json found in {SPEC_DIR}. "
            f"Set A4V3_SPEC_PATH or place a spec file."
        )
    candidates.sort(key=_extract_spec_version, reverse=True)
    return candidates[0]


def spec_version() -> str:
    """Version tag for the active spec (e.g. 'v50' from 'a4v3_full (50).json')."""
    n = _extract_spec_version(spec_path())
    return f"v{n}" if n >= 0 else "unknown"


@lru_cache(maxsize=1)
def load_spec() -> dict:
    """Load and cache the JSON spec."""
    return json.loads(spec_path().read_text(encoding="utf-8"))


@lru_cache(maxsize=1)
def families() -> tuple[str, ...]:
    return FAMILIES


@lru_cache(maxsize=None)
def kinds(family: str) -> tuple[str, ...]:
    """Allowed kinds for a family, parsed from INNF v1 'Fields' column.

    Returns the kind set declared in the spec — e.g. for TemporalDecl in
    spec v50, returns `('always', 'eventually', 'once', 'next', 'until',
    'since', 'fairness')`.
    """
    spec = load_spec()
    for row in spec.get("INNF v1", []):
        if not row or len(row) < 3 or row[0] != family:
            continue
        fields_cell = str(row[2] or "")
        m = re.search(r"kind\s*∈\s*\{([^}]+)\}", fields_cell)
        if m:
            return tuple(k.strip() for k in m.group(1).split(","))
        return _BUILTIN_KINDS.get(family, tuple())
    return _BUILTIN_KINDS.get(family, tuple())


@lru_cache(maxsize=1)
def block_keywords() -> frozenset[str]:
    """Top-level declaration keywords (line-leading in a4v3 text).

    Union of all keywords across the 12 families' surface forms.
    """
    out: set[str] = set()
    for kws in _FAMILY_TO_BLOCK_KW.values():
        out.update(kws)
    return frozenset(out)


def family_block_keywords(family: str) -> tuple[str, ...]:
    """Top-level keywords for a specific family. Returns () for unknown family."""
    return _FAMILY_TO_BLOCK_KW.get(family, ())


@lru_cache(maxsize=1)
def expression_keywords() -> frozenset[str]:
    """Operators / binders / field names used inside expressions."""
    return _EXPRESSION_KW


@lru_cache(maxsize=1)
def all_keywords() -> frozenset[str]:
    """Union of block + expression keywords. Use for content-token exclusion
    in metrics that count 'content' words against source/normalized text.
    """
    return block_keywords() | expression_keywords()


@lru_cache(maxsize=1)
def notation_reference_keywords() -> frozenset[str]:
    """The 91-keyword surface lexicon parsed from spec's `Notation Reference`
    sheet. May include some extra-low-frequency tokens or alternate spellings;
    use `all_keywords()` for the canonical set instead unless you need every
    surface form mentioned in the spec."""
    spec = load_spec()
    rows = spec.get("Notation Reference", [])
    if not rows:
        return frozenset()
    header = rows[0]
    try:
        kw_col = next(i for i, h in enumerate(header)
                       if h and "keyword" in str(h).lower())
    except StopIteration:
        return frozenset()
    out: set[str] = set()
    for row in rows[1:]:
        if len(row) <= kw_col or not row[kw_col]:
            continue
        cell = str(row[kw_col])
        for tok in re.split(r"[\s,|/()<>=]+", cell):
            tok = tok.strip().lower()
            if tok and re.match(r"^[a-z_][a-z_]*$", tok) and len(tok) >= 2:
                out.add(tok)
    return frozenset(out)


def temporal_kinds() -> tuple[str, ...]:
    """Convenience: TemporalDecl kinds from spec."""
    return kinds("TemporalDecl")


def deontic_kinds() -> tuple[str, ...]:
    """Convenience: DeonticDecl kinds from spec."""
    return kinds("DeonticDecl")


def assert_consistency() -> None:
    """Sanity check: verify that key family kinds match the JSON spec.

    NOTE: block_keywords and expression_keywords legitimately OVERLAP on
    dual-use tokens (e.g. `action` is both a SymbolDecl/ActionDecl block
    keyword AND a DeonticDecl field name; `target` is both a
    ValidationDecl block keyword AND a DeonticDecl field; `init`, `key`,
    `reward`, `utility`, `fairness`, `checked` similar). Overlap is OK
    by design — both keyword roles are valid a4v3 surface tokens.
    """
    # TemporalDecl.kinds in the spec must include the LTL primaries.
    tk = set(temporal_kinds())
    required = {"always", "eventually", "next", "once"}
    if not required.issubset(tk):
        raise RuntimeError(
            f"a4v3_grammar: TemporalDecl.kinds in spec={tk} is missing "
            f"required LTL primaries {required - tk}. Spec file: {spec_path()}"
        )
    # All declared families must be present in the spec.
    spec = load_spec()
    spec_families = {row[0] for row in spec.get("INNF v1", [])
                     if row and row[0] in FAMILIES}
    missing = set(FAMILIES) - spec_families
    if missing:
        raise RuntimeError(
            f"a4v3_grammar: families {sorted(missing)} declared in code "
            f"but missing from spec INNF v1 sheet: {spec_path()}"
        )


if __name__ == "__main__":
    print(f"spec_path: {spec_path()}")
    print(f"spec_version: {spec_version()}")
    print(f"families: {families()}")
    for fam in FAMILIES:
        print(f"  {fam}.kinds: {kinds(fam)}")
    print(f"block_keywords ({len(block_keywords())}): "
           f"{sorted(block_keywords())}")
    print(f"expression_keywords ({len(expression_keywords())}): "
           f"{sorted(expression_keywords())}")
    print(f"all_keywords ({len(all_keywords())})")
    print(f"notation_reference_keywords ({len(notation_reference_keywords())})")
    assert_consistency()
    print("consistency check: OK")
