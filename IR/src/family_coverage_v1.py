"""family_coverage_v1.py

Det-метрика: какие из 35 a4v3 families использует каждая entry, и какие
families *ожидались* судя по детерминированным сигналам в source.

Family taxonomy — из `thoughts/IR_schema/a4v3_full_48.md` (35 families,
12 INNF top-level).

IR-side detection (regex по a4v3-тексту):
  - TypeDecl       (#1 opaque sort, #2 enum, #3 subtype, #10 record)
  - SymbolDecl     (#4 entity, #5 const, #6 body-less, #7 rel, #8 rel-incl,
                    #9 fun, #12 property, #23 event, #25 var)
  - AssertDecl     (#13 key, #14 disjoint, #15 fact/constraint, #27 init)
  - PathDecl       (#11)
  - ActionDecl     (#26)
  - TemporalDecl   (#29 always/eventually/once/next, #30 fairness)
  - DeonticDecl    (#31 obligation, #32 permission, #33 prohibition)
  - ValidationDecl, ProbabilisticDecl, GameDecl, GraphDecl, TheoremDecl

Source-side signal detection (regex по source.md):
  - modality   → expect DeonticDecl (some obligation-only cases are advisory)
  - temporal   → expect TemporalDecl (plain `until` can be advisory)
  - action     → expect ActionDecl
  - enum       → expect TypeDecl(enum)
  - subtype    → expect TypeDecl(subtype)
  - cardinality→ expect Term.count
  - key        → expect AssertDecl(key)
  - probabilistic → expect ProbabilisticDecl
  - theorem    → expect TheoremDecl

Domain-agnostic — только generic English markers, никаких финансовых терминов.

Saves: metrics_family_coverage_v1.json per entry.
Plus corpus-level family_coverage_corpus_report_v1.{json,md} at run root.

CLI:
    python family_coverage_v1.py [entry_dir|run_root]
"""
from __future__ import annotations
import json
import pathlib
import re
import sys
from collections import Counter, defaultdict

ROOT = pathlib.Path(__file__).resolve().parents[2]


# ─────────────────────────────────────────────────────────────────────────
# IR-side family detectors
# ─────────────────────────────────────────────────────────────────────────

IR_FAMILY_PATTERNS: list[tuple[str, str, re.Pattern]] = [
    # (innf_family, fine_family_id_or_kind, regex)
    ("TypeDecl", "sort_opaque",
     re.compile(r"^\s*sort\s+([A-Za-z_][A-Za-z0-9_]*)\s*$", re.MULTILINE)),
    ("TypeDecl", "sort_enum",
     re.compile(r"^\s*sort\s+([A-Za-z_][A-Za-z0-9_]*)\s*=\s*[A-Za-z]", re.MULTILINE)),
    ("TypeDecl", "sort_subtype",
     re.compile(r"^\s*sort\s+([A-Za-z_][A-Za-z0-9_]*)\s+extends\s+", re.MULTILINE)),
    ("TypeDecl", "struct_record",
     re.compile(r"^\s*struct\s+([A-Za-z_][A-Za-z0-9_]*)", re.MULTILINE)),
    ("SymbolDecl", "entity",
     re.compile(r"^\s*entity\s+([A-Za-z_][A-Za-z0-9_]*)\s*:", re.MULTILINE)),
    ("SymbolDecl", "const_val",
     re.compile(r"^\s*val\s+([A-Za-z_][A-Za-z0-9_]*)\s*:", re.MULTILINE)),
    ("SymbolDecl", "body_less",
     re.compile(r"^\s*(?:opaque|abstract|declare)\s+([A-Za-z_][A-Za-z0-9_]*)\s*:", re.MULTILINE)),
    ("SymbolDecl", "rel",
     re.compile(r"^\s*rel\s+([A-Za-z_][A-Za-z0-9_]*)\s*:", re.MULTILINE)),
    ("SymbolDecl", "rel_inclusion",
     re.compile(r"^\s*rel\s+([A-Za-z_][A-Za-z0-9_]*)\s+extends\s+", re.MULTILINE)),
    ("SymbolDecl", "fun",
     re.compile(r"^\s*fun(?:\[[^\]]+\])?\s+([A-Za-z_][A-Za-z0-9_]*)\s*:", re.MULTILINE)),
    ("SymbolDecl", "property",
     re.compile(r"^\s*property\s+([A-Za-z_][A-Za-z0-9_]*)\s*:", re.MULTILINE)),
    ("SymbolDecl", "event",
     re.compile(r"^\s*event\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(", re.MULTILINE)),
    ("SymbolDecl", "var",
     re.compile(r"^\s*var\s+([A-Za-z_][A-Za-z0-9_]*)\s*:", re.MULTILINE)),
    ("AssertDecl", "key_identity",
     re.compile(r"^\s*key\[(?:identity|validation)\]\s+", re.MULTILINE)),
    ("AssertDecl", "disjoint",
     re.compile(r"^\s*disjoint\s+", re.MULTILINE)),
    ("AssertDecl", "fact",
     re.compile(r"^\s*fact\s+([A-Za-z_][A-Za-z0-9_]*)\s*:", re.MULTILINE)),
    ("AssertDecl", "constraint",
     re.compile(r"^\s*constraint\s+([A-Za-z_][A-Za-z0-9_]*)\s*:", re.MULTILINE)),
    ("AssertDecl", "axiom",
     re.compile(r"^\s*axiom\s+([A-Za-z_][A-Za-z0-9_]*)\s*:", re.MULTILINE)),
    ("AssertDecl", "init",
     re.compile(r"^\s*init\s*\{", re.MULTILINE)),
    ("PathDecl", "path",
     re.compile(r"^\s*path\s+([A-Za-z_][A-Za-z0-9_]*)\s*=", re.MULTILINE)),
    ("ActionDecl", "action",
     re.compile(r"^\s*action\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(", re.MULTILINE)),
    ("TemporalDecl", "prop",
     re.compile(r"^\s*prop\s+([A-Za-z_][A-Za-z0-9_]*)\s*:", re.MULTILINE)),
    ("TemporalDecl", "fairness",
     re.compile(r"^\s*fairness\s+([A-Za-z_][A-Za-z0-9_]*)\s*:", re.MULTILINE)),
    ("DeonticDecl", "obligation",
     re.compile(r"^\s*obligation\s+([A-Za-z_][A-Za-z0-9_]*)(?:\s*\(|\s*:)", re.MULTILINE)),
    ("DeonticDecl", "permission",
     re.compile(r"^\s*permission\s+([A-Za-z_][A-Za-z0-9_]*)(?:\s*\(|\s*:)", re.MULTILINE)),
    ("DeonticDecl", "prohibition",
     re.compile(r"^\s*prohibition\s+([A-Za-z_][A-Za-z0-9_]*)(?:\s*\(|\s*:)", re.MULTILINE)),
    ("ValidationDecl", "target",
     re.compile(r"^\s*target\s+([A-Za-z_][A-Za-z0-9_]*)\s*:", re.MULTILINE)),
    ("ValidationDecl", "closed",
     re.compile(r"^\s*closed\s+", re.MULTILINE)),
    ("ProbabilisticDecl", "dist",
     re.compile(r"^\s*(?:dist|distribution)\s+", re.MULTILINE)),
    ("ProbabilisticDecl", "reward",
     re.compile(r"^\s*reward\s+", re.MULTILINE)),
    ("ProbabilisticDecl", "objective",
     re.compile(r"^\s*objective\s+(?:maximize|minimize)\s+", re.MULTILINE)),
    ("GameDecl", "obs",
     re.compile(r"^\s*obs\s*:", re.MULTILINE)),
    ("GameDecl", "indist",
     re.compile(r"^\s*fact\s+\w+\s*:\s*indist", re.MULTILINE)),
    ("GraphDecl", "dataset",
     re.compile(r"^\s*dataset\s+", re.MULTILINE)),
    ("GraphDecl", "reify",
     re.compile(r"^\s*reify\s+", re.MULTILINE)),
    ("TheoremDecl", "theorem",
     re.compile(r"^\s*theorem\s+([A-Za-z_][A-Za-z0-9_]*)\s*:", re.MULTILINE)),
    ("TheoremDecl", "checked",
     re.compile(r"^\s*checked\s+([A-Za-z_][A-Za-z0-9_]*)", re.MULTILINE)),
]


# Expression-grammar markers inside constraint/fact bodies
IR_EXPR_PATTERNS = {
    "forall": re.compile(r"\bforall\b"),
    "exists": re.compile(r"\bexists\b"),
    "implies": re.compile(r"\bimplies\b"),
    "iff": re.compile(r"\biff\b"),
    "ite": re.compile(r"\bite\s*\("),
    "count": re.compile(r"\bcount\s*\("),
    "set_comp": re.compile(r"\{[^}]*\bin\b[^}]*\bwhere\b[^}]*\}"),
    "always": re.compile(r"\balways\s*\("),
    "eventually": re.compile(r"\beventually\s*\("),
    "once": re.compile(r"\bonce\s*\("),
    "next": re.compile(r"\bnext\s*\("),
    # Static temporal-order coverage: source phrases such as "prior to the
    # Live Date" often mean a date/period ordering relation, not an LTL trace
    # property. Count only explicit relation/function calls in formula bodies;
    # declarations or long assertion names are not enough.
    "temporal_order_static_relation_call": re.compile(
        r"\b(?:"
        r"day_before|period_prior_to|prior_to|before|after|"
        r"subsequent_to|previous(?:_day|_calculation_day)?(?:_of)?"
        r")\s*\("
        r"|\b[A-Za-z_][A-Za-z0-9_]*_(?:before|after)\s*\("
    ),
}


# ─────────────────────────────────────────────────────────────────────────
# Source-side signal detectors
# ─────────────────────────────────────────────────────────────────────────

# Signals whose expected family is only advisory under the minimal-IR policy:
# a source marker is present, but a simpler local lowering may still be
# acceptable if the source does not make the richer family first-class.
ADVISORY_EXPECTATION_SIGNALS = {
    "modality_obligation",
    "temporal_always",
    "temporal_until",
    "action_transition",
}


# Generic English markers — domain-agnostic.
SOURCE_SIGNALS: list[tuple[str, str, re.Pattern]] = [
    # (signal_class, expected_family_id, regex pattern with capture for evidence)

    # Modality → DeonticDecl
    # `shall` and `must` get a negative lookahead to skip legalese definitional
    # binding ("X shall have the meaning ...", "X shall be defined as ...",
    # "X shall mean Y", "X shall refer to Y", "X shall be construed as Y").
    # Those are declarative legal style, not deontic obligations on an actor.
    ("modality_obligation", "DeonticDecl",
     re.compile(
         r"\b(?:"
         r"shall\s+(?!have\s+the\s+meaning|be\s+defined|mean\b|refer\s+to|be\s+construed|be\s+understood|have\s+the\s+same)"
         r"|must(?!\s+(?:not|have\s+the\s+meaning|be\s+defined|mean\b|refer\s+to|be\s+construed))"
         r"|is\s+required\s+to|are\s+required\s+to"
         r"|is\s+obligated|are\s+obligated|has\s+to|have\s+to"
         r"|endeavors?\s+to|undertakes?\s+to"
         r")\b", re.IGNORECASE)),
    ("modality_permission", "DeonticDecl",
     re.compile(r"\b(?:may\s+(?:have|include|use|elect|choose)|"
                r"may\s+be\s+(?:issued|made|used|applied|provided|published|"
                r"announced|granted|exercised|indicated|submitted|amended|"
                r"changed|calculated|selected)|"
                r"is\s+permitted|are\s+permitted|"
                r"is\s+allowed|are\s+allowed|"
                r"can\s+(?:elect|choose|opt))\b", re.IGNORECASE)),
    ("modality_prohibition", "DeonticDecl",
     re.compile(r"\b(?:shall\s+not|must\s+not|"
                r"cannot(?!\s+be\s+(?:completely\s+)?(?:ruled\s+out|excluded))|"
                r"may\s+not|"
                r"is\s+prohibited|are\s+prohibited|"
                r"is\s+forbidden|are\s+forbidden|"
                r"is\s+not\s+permitted|are\s+not\s+permitted)\b", re.IGNORECASE)),

    # Temporal → TemporalDecl
    ("temporal_eventually", "TemporalDecl",
     re.compile(r"\b(?:eventually|sooner\s+or\s+later|at\s+some\s+point|"
                r"will\s+ultimately|in\s+the\s+long\s+run)\b", re.IGNORECASE)),
    ("temporal_always", "TemporalDecl",
     re.compile(r"\b(?:always|at\s+all\s+times|continuously|"
                r"throughout|invariantly)\b", re.IGNORECASE)),
    # Plain `until` often describes procedure termination. Under the
    # minimal-IR policy this is advisory rather than hard-required unless
    # the source also makes trace/state structure explicit.
    ("temporal_until", "TemporalDecl",
     re.compile(r"\buntil\b", re.IGNORECASE)),
    ("temporal_order", "TemporalDecl",
     re.compile(r"\b(?:before|after|prior\s+to|subsequent\s+to|"
                r"thereafter|previously|once\b)\b", re.IGNORECASE)),

    # Enum → TypeDecl(enum)
    ("enum_one_of", "TypeDecl_enum",
     re.compile(r"\b(?:is\s+(?:one|any)\s+of|must\s+be\s+(?:one|any)\s+of|"
                r"can\s+be\s+(?:one|any)\s+of|takes?\s+values?\s+(?:in|from))\b",
                re.IGNORECASE)),
    ("enum_either_or", "TypeDecl_enum",
     re.compile(r"\beither\s+\w+\s+or\s+\w+(?:\s+or\s+\w+)*\b", re.IGNORECASE)),

    # Subtype → TypeDecl(subtype)
    ("subtype_is_a", "TypeDecl_subtype",
     re.compile(r"\b(?:is\s+a\s+kind\s+of|is\s+a\s+type\s+of|"
                r"is\s+a\s+subclass\s+of|extends|specializes|"
                r"is\s+a\s+special\s+case\s+of)\b", re.IGNORECASE)),

    # Cardinality → Term.count
    # Exclude percentages like `exactly 50%`: those are usually numeric
    # equality/threshold constraints, not discrete-object count claims.
    ("cardinality_exactly", "AssertDecl_count",
     re.compile(r"\b(?:exactly\s+one|exactly\s+\d+(?!\s*(?:%|percent\b)))\b",
                re.IGNORECASE)),
    ("cardinality_at_least", "AssertDecl_count",
     re.compile(r"\b(?:at\s+least\s+\d+(?!\s*(?:%|percent\b))|"
                r"no\s+fewer\s+than\s+\d+(?!\s*(?:%|percent\b))|"
                r"a\s+minimum\s+of\s+\d+(?!\s*(?:%|percent\b)))\b",
                re.IGNORECASE)),
    ("cardinality_at_most", "AssertDecl_count",
     re.compile(r"\b(?:at\s+most\s+\d+(?!\s*(?:%|percent\b))|"
                r"no\s+more\s+than\s+\d+(?!\s*(?:%|percent\b))|"
                r"a\s+maximum\s+of\s+\d+(?!\s*(?:%|percent\b)))\b",
                re.IGNORECASE)),

    # Key/uniqueness → AssertDecl(key)
    ("key_uniquely", "AssertDecl_key",
     re.compile(r"\b(?:uniquely\s+identif|primary\s+key|"
                r"distinct(?:ly)?\s+identif|no\s+two\s+\w+\s+(?:can|may)\s+have\s+the\s+same)\b",
                re.IGNORECASE)),

    # Conditional → ite or implies
    ("conditional_if_then_else", "Term_ite",
     re.compile(r"\bif\s+[^.]+?\s+then\s+[^.]+?\s+else\b", re.IGNORECASE)),
    ("conditional_if_then", "Formula_implies",
     re.compile(r"\bif\s+[^.]+?\s+then\b", re.IGNORECASE)),

    # Quantifiers → forall / exists
    ("quantifier_universal", "Formula_forall",
     re.compile(r"\b(?:every|each|for\s+all|for\s+any|all\s+\w+|any\s+\w+)\b",
                re.IGNORECASE)),
    ("quantifier_existential", "Formula_exists",
     re.compile(r"\b(?:there\s+exists?|there\s+is\s+(?:a|an|some)|"
                r"some\s+\w+|at\s+least\s+one)\b", re.IGNORECASE)),

    # Probabilistic → ProbabilisticDecl
    ("probabilistic", "ProbabilisticDecl",
     re.compile(r"\b(?:probability\s+of|with\s+probability|expected\s+value|"
                r"on\s+average|stochastic|random(?:ly|ized)?)\b", re.IGNORECASE)),

    # Action → ActionDecl
    # This is advisory: a phrase can name an action-like scenario without
    # making action execution/transition semantics first-class.
    ("action_transition", "ActionDecl",
     re.compile(r"\b(?:transitions?\s+(?:to|from)|state\s+changes?|"
                r"upon\s+\w+ing|after\s+\w+ing)\b", re.IGNORECASE)),

    # Theorem → TheoremDecl
    ("theorem_claim", "TheoremDecl",
     re.compile(r"\b(?:theorem|lemma|claim\s+that|it\s+(?:must|can)\s+be\s+(?:proved|shown))\b",
                re.IGNORECASE)),
]


# ─────────────────────────────────────────────────────────────────────────
# Detection & analysis
# ─────────────────────────────────────────────────────────────────────────

def _strip_comments(text: str) -> str:
    return "\n".join(
        line for line in text.splitlines() if not line.lstrip().startswith("#")
    )


def detect_ir_families(a4v3_text: str) -> dict:
    """Returns {(innf, fine): count} and {expr_marker: count}."""
    text = _strip_comments(a4v3_text)
    used: dict[tuple[str, str], int] = defaultdict(int)
    for innf, fine, pat in IR_FAMILY_PATTERNS:
        n = len(pat.findall(text))
        if n:
            used[(innf, fine)] = n
    expr: dict[str, int] = {}
    for marker, pat in IR_EXPR_PATTERNS.items():
        n = len(pat.findall(text))
        if n:
            expr[marker] = n
    return {"families": dict(used), "expr_markers": expr}


_VAGUE_TERM_DECL_RE = re.compile(
    r"^\s*(?:entity\s+[A-Za-z_][A-Za-z0-9_]*\s*:\s*VagueTerm|"
    r"sort\s+[A-Za-z_][A-Za-z0-9_]*\s+extends\s+VagueTerm)\b",
    re.MULTILINE,
)


def _has_vague_temporal_treatment(a4v3_text: str, translator_notes_text: str) -> bool:
    """Accept a temporal-order source signal without TemporalDecl when the IR
    explicitly models the phrase as a VagueTerm and translator notes explain
    that the phrase is vague/static timing, not trace-temporal semantics.

    This is intentionally general: the checker should not special-case
    section_3_1 or "sufficient notice before". It only recognizes the pattern
    when both artifacts are present:
    - an actual VagueTerm declaration in the IR;
    - a human-readable translator note mentioning vague timing/temporal
      treatment and explicitly distinguishing it from TemporalDecl/trace
      semantics.
    """
    if not _VAGUE_TERM_DECL_RE.search(a4v3_text or ""):
        return False
    notes = (translator_notes_text or "").lower()
    if "vague" not in notes:
        return False
    if not any(term in notes for term in ("timing", "temporal", "deadline", "notice")):
        return False
    return any(term in notes for term in (
        "temporaldecl",
        "trace-temporal",
        "trace temporal",
        "trace semantics",
        "static timing",
        "static temporal",
        "not trace",
    ))


# Counting / arithmetic phrasings that contain `before/after/prior to/...`
# but encode date arithmetic, not temporal modality. Removed before
# `temporal_order` regex runs.
_COUNTING_TEMPORAL_RE = re.compile(
    r"\b\d+\s+(?:business|calendar|trading|working)?\s*"
    r"(?:days?|weeks?|months?|years?)\s+"
    r"(?:before|after|prior\s+to|subsequent\s+to)\b",
    re.IGNORECASE,
)
# Phrases like "after close of business", "before the opening" — describe
# time-of-day boundary, not temporal modality.
_TIME_OF_DAY_BOUNDARY_RE = re.compile(
    r"\b(?:before|after)\s+"
    r"(?:close\s+of\s+business|the\s+(?:close|opening)\s+of\s+(?:business|trading))\b",
    re.IGNORECASE,
)
# Comparative baselines such as "as accurately, reliably and appropriately
# as before" use `before` as a reference-quality baseline, not as an ordering
# relation over dates/events. They should not require TemporalDecl coverage.
_COMPARATIVE_AS_BEFORE_RE = re.compile(
    r"\bas\b[^.?!;\n]{0,180}\bas\s+before\b",
    re.IGNORECASE,
)


def detect_source_signals(source_text: str) -> dict:
    """Returns {signal_class: list[evidence]}."""
    out: dict[str, dict] = {}
    text = source_text or ""
    # strip markdown headers
    text_no_h = "\n".join(line for line in text.splitlines()
                          if not line.lstrip().startswith("#"))
    # Build a counting-stripped text for temporal_order specifically.
    text_for_temporal = _TIME_OF_DAY_BOUNDARY_RE.sub(" ", text_no_h)
    text_for_temporal = _COUNTING_TEMPORAL_RE.sub(" ", text_for_temporal)
    text_for_temporal = _COMPARATIVE_AS_BEFORE_RE.sub(" ", text_for_temporal)
    for sig, expected, pat in SOURCE_SIGNALS:
        target_text = text_for_temporal if sig == "temporal_order" else text_no_h
        matches = pat.findall(target_text)
        if matches:
            ev = list({m if isinstance(m, str) else m[0] for m in matches})[:8]
            out.setdefault(sig, {
                "expected_family": expected,
                "expectation_mode": (
                    "advisory" if sig in ADVISORY_EXPECTATION_SIGNALS
                    else "required"
                ),
                "matches": [],
            })
            out[sig]["matches"].extend(ev)
    # dedup
    for sig in out:
        out[sig]["matches"] = sorted(set(out[sig]["matches"]))
    return out


def _strip_innf_suffix(family: str) -> str:
    return family.split("_")[0]


def compute_gaps(
    ir_used: dict,
    source_signals: dict,
    *,
    a4v3_text: str = "",
    translator_notes_text: str = "",
) -> dict:
    """For each source signal class, decide whether the expected family is
    represented in IR. Returns gap report."""
    used_innfs = {innf for (innf, _) in ir_used["families"].keys()}
    used_fines = {f"{innf}_{fine}" for (innf, fine) in ir_used["families"].keys()}
    used_expr = set(ir_used["expr_markers"].keys())

    gaps: list[dict] = []
    required_gaps: list[dict] = []
    advisory_gaps: list[dict] = []
    matches: list[dict] = []
    for sig, info in source_signals.items():
        expected = info["expected_family"]
        expectation_mode = info.get("expectation_mode", "required")
        ev = info["matches"]
        # expected can be:
        #   - INNF family name (e.g. "DeonticDecl", "TemporalDecl", "ActionDecl")
        #   - INNF_subfine (e.g. "TypeDecl_enum")
        #   - Formula_... or Term_... (expression markers)
        satisfied = False
        if expected.startswith("Formula_") or expected.startswith("Term_"):
            marker = expected.split("_", 1)[1]
            satisfied = marker in used_expr
        elif "_" in expected and expected.split("_")[0].endswith("Decl"):
            innf, fine = expected.split("_", 1)
            satisfied = (
                f"{innf}_{fine}" in used_fines
                or any((u_innf, u_fine) in ir_used["families"]
                       and u_innf == innf and fine in u_fine
                       for (u_innf, u_fine) in ir_used["families"])
            )
        else:
            satisfied = expected in used_innfs

        if (
            not satisfied
            and sig == "temporal_order"
            and expected == "TemporalDecl"
            and "temporal_order_static_relation_call" in used_expr
        ):
            satisfied = True
            satisfied_by = "static_temporal_relation_call"
        elif (
            not satisfied
            and sig == "temporal_order"
            and expected == "TemporalDecl"
            and _has_vague_temporal_treatment(a4v3_text, translator_notes_text)
        ):
            satisfied = True
            satisfied_by = "vague_temporal_translator_note"
        else:
            satisfied_by = None

        rec = {
            "signal": sig,
            "expected_family": expected,
            "expectation_mode": expectation_mode,
            "evidence": ev,
            "satisfied": satisfied,
        }
        if satisfied_by:
            rec["satisfied_by"] = satisfied_by
        if satisfied:
            matches.append(rec)
        else:
            gaps.append(rec)
            if expectation_mode == "advisory":
                advisory_gaps.append(rec)
            else:
                required_gaps.append(rec)
    return {
        "gaps": gaps,
        "required_gaps": required_gaps,
        "advisory_gaps": advisory_gaps,
        "matches": matches,
    }


def analyze_entry(entry_dir: pathlib.Path) -> dict:
    src_p = entry_dir / "source.md"
    a4v3_p = entry_dir / "main_ir.a4v3"
    if not a4v3_p.exists():
        return {"entry_id": entry_dir.name, "skipped": True, "reason": "no a4v3"}
    source = src_p.read_text(encoding="utf-8") if src_p.exists() else ""
    a4v3 = a4v3_p.read_text(encoding="utf-8")
    notes_p = entry_dir / "translator_notes.md"
    translator_notes = notes_p.read_text(encoding="utf-8") if notes_p.exists() else ""

    ir_used = detect_ir_families(a4v3)
    source_signals = detect_source_signals(source)
    gap_report = compute_gaps(
        ir_used,
        source_signals,
        a4v3_text=a4v3,
        translator_notes_text=translator_notes,
    )

    # Family-set view: which INNFs and fine families
    used_innfs = sorted({innf for (innf, _) in ir_used["families"].keys()})
    used_fines_full = sorted({
        f"{innf}.{fine}" for (innf, fine) in ir_used["families"].keys()
    })

    return {
        "entry_id": entry_dir.name,
        "skipped": False,
        "ir_innf_families_used": used_innfs,
        "ir_fine_families_used": used_fines_full,
        "ir_family_counts": {
            f"{innf}.{fine}": cnt for (innf, fine), cnt in ir_used["families"].items()
        },
        "ir_expr_markers": ir_used["expr_markers"],
        "source_signals": source_signals,
        "gaps": gap_report["gaps"],
        "required_gaps": gap_report["required_gaps"],
        "advisory_gaps": gap_report["advisory_gaps"],
        "matches": gap_report["matches"],
        "n_gaps": len(gap_report["gaps"]),
        "n_required_gaps": len(gap_report["required_gaps"]),
        "n_advisory_gaps": len(gap_report["advisory_gaps"]),
        "n_matches": len(gap_report["matches"]),
    }


def _save(entry_dir: pathlib.Path, result: dict) -> pathlib.Path:
    out = entry_dir / "metrics_family_coverage_v1.json"
    out.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n",
                   encoding="utf-8")
    return out


def aggregate(run_root: pathlib.Path) -> dict:
    entries: list[dict] = []
    for d in sorted(run_root.rglob("main_ir.a4v3")):
        entry_dir = d.parent
        if entry_dir.name.startswith("_"):
            continue
        entries.append(analyze_entry(entry_dir))

    n = sum(1 for e in entries if not e.get("skipped"))

    # INNF family usage corpus-wide
    innf_usage: Counter = Counter()
    fine_usage: Counter = Counter()
    expr_usage: Counter = Counter()
    for e in entries:
        if e.get("skipped"):
            continue
        for f in e["ir_innf_families_used"]:
            innf_usage[f] += 1
        for f in e["ir_fine_families_used"]:
            fine_usage[f] += 1
        for m in e["ir_expr_markers"]:
            expr_usage[m] += 1

    # Gap signal aggregation
    gap_by_signal: Counter = Counter()
    gap_entries: dict[str, set] = defaultdict(set)
    gap_examples: dict[str, list] = defaultdict(list)
    for e in entries:
        if e.get("skipped"):
            continue
        for g in e["gaps"]:
            gap_by_signal[g["signal"]] += 1
            gap_entries[g["signal"]].add(e["entry_id"])
            if len(gap_examples[g["signal"]]) < 6:
                gap_examples[g["signal"]].append({
                    "entry": e["entry_id"],
                    "expected_family": g["expected_family"],
                    "evidence": g["evidence"],
                })

    # Match (positive) signal aggregation
    match_by_signal: Counter = Counter()
    for e in entries:
        if e.get("skipped"):
            continue
        for m in e["matches"]:
            match_by_signal[m["signal"]] += 1

    # 12-family wishlist: which a4v3 families NEVER used in corpus?
    # Sourced from canonical spec via a4v3_grammar.families().
    from a4v3_grammar import families as _grammar_families  # noqa: E402
    all_known_innfs = set(_grammar_families())
    never_used_innfs = sorted(all_known_innfs - set(innf_usage))

    return {
        "run": run_root.name,
        "n_entries": n,
        "innf_family_usage": dict(innf_usage.most_common()),
        "fine_family_usage": dict(fine_usage.most_common()),
        "expr_marker_usage": dict(expr_usage.most_common()),
        "innf_families_never_used": never_used_innfs,
        "gap_signals": {
            "counts": dict(gap_by_signal.most_common()),
            "entries_per_signal": {k: sorted(v) for k, v in gap_entries.items()},
            "examples_per_signal": {k: v for k, v in gap_examples.items()},
        },
        "match_signals": dict(match_by_signal.most_common()),
        "entries": entries,
    }


def _md_corpus_report(agg: dict) -> str:
    lines: list[str] = []
    lines.append(f"# Family coverage — {agg['run']}")
    lines.append("")
    lines.append(f"- entries: **{agg['n_entries']}**")
    lines.append("")

    lines.append("## INNF families actually used in IR")
    lines.append("")
    lines.append("a4v3 has 12 INNF top-level families. Used in this corpus:")
    lines.append("")
    lines.append("| INNF family | entries using it |")
    lines.append("|---|---:|")
    for k, v in agg["innf_family_usage"].items():
        lines.append(f"| `{k}` | {v} / {agg['n_entries']} |")
    lines.append("")
    lines.append(f"### NEVER used in corpus")
    lines.append("")
    if agg["innf_families_never_used"]:
        for f in agg["innf_families_never_used"]:
            lines.append(f"- `{f}`")
    else:
        lines.append("_(все 12 families использованы)_")
    lines.append("")

    lines.append("## Fine family usage (canonical-family granularity)")
    lines.append("")
    lines.append("| family.kind | entries |")
    lines.append("|---|---:|")
    for k, v in agg["fine_family_usage"].items():
        lines.append(f"| `{k}` | {v} |")
    lines.append("")

    lines.append("## Expression-grammar markers in IR")
    lines.append("")
    lines.append("Inside constraint/fact/fun bodies (forall, exists, implies, ite, count, ...):")
    lines.append("")
    lines.append("| marker | entries |")
    lines.append("|---|---:|")
    for k, v in agg["expr_marker_usage"].items():
        lines.append(f"| `{k}` | {v} |")
    lines.append("")

    lines.append("## Gap signals — source has X, IR doesn't use the family")
    lines.append("")
    lines.append("Det-detector в source.md ловит сигнал → expected a4v3 family. "
                 "Если соответствующая family не использована в IR — это gap.")
    lines.append("")
    lines.append("| source signal | expected family | entries with gap |")
    lines.append("|---|---|---:|")
    gc = agg["gap_signals"]["counts"]
    eps = agg["gap_signals"]["examples_per_signal"]
    for sig, cnt in gc.items():
        ex = eps.get(sig, [])
        expected = ex[0]["expected_family"] if ex else "?"
        lines.append(f"| `{sig}` | `{expected}` | {cnt} |")
    lines.append("")

    lines.append("### Examples per gap signal")
    lines.append("")
    for sig in gc:
        if not eps.get(sig):
            continue
        lines.append(f"#### `{sig}` → expected `{eps[sig][0]['expected_family']}`")
        lines.append("")
        for ex in eps[sig][:5]:
            ev = ", ".join(f"`{e}`" for e in ex["evidence"][:5])
            lines.append(f"- `{ex['entry']}`: {ev}")
        lines.append("")

    return "\n".join(lines)


def main():
    args = sys.argv[1:]
    target = pathlib.Path(args[0]) if args else (
        ROOT / "IR/outputs/runs/unified_methodology_v1")

    if (target / "main_ir.a4v3").exists():
        result = analyze_entry(target)
        out = _save(target, result)
        print(f"Wrote {out}")
        if not result.get("skipped"):
            print(f"  INNFs used: {result['ir_innf_families_used']}")
            print(f"  expr markers: {result['ir_expr_markers']}")
            print(f"  gaps: {result['n_gaps']}, matches: {result['n_matches']}")
        return

    # corpus mode
    n = 0
    for d in sorted(target.rglob("main_ir.a4v3")):
        entry_dir = d.parent
        if entry_dir.name.startswith("_"):
            continue
        result = analyze_entry(entry_dir)
        _save(entry_dir, result)
        n += 1

    agg = aggregate(target)
    json_p = target / "family_coverage_corpus_report_v1.json"
    md_p = target / "family_coverage_corpus_report_v1.md"
    json_p.write_text(json.dumps(agg, indent=2, ensure_ascii=False, default=str) + "\n",
                      encoding="utf-8")
    md_p.write_text(_md_corpus_report(agg), encoding="utf-8")
    print(f"Wrote {json_p.relative_to(ROOT)}")
    print(f"Wrote {md_p.relative_to(ROOT)}")
    print()
    print(f"Per-entry metrics written: {n}")
    print(f"INNFs never used in corpus: {agg['innf_families_never_used']}")
    print(f"Top gap signals:")
    for sig, cnt in list(agg['gap_signals']['counts'].items())[:8]:
        print(f"  {sig}: {cnt} entries")


if __name__ == "__main__":
    main()
