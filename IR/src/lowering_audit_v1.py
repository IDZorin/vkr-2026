"""lowering_audit_v1.py

IR-driven scanner: ищет в именах rel/fun/entity модальные/временные/
деонтические/action токены. Если такие есть — это lowering smell:
семантика, которая в a4v3 имеет first-class family (DeonticDecl,
TemporalDecl, ActionDecl), зашита в имя обычного `rel`.

Подход: tokenize symbol name по `_` и camelCase, сравнить токены с
доменно-агностическими английскими модальными/временными лексиконами.
Plus multi-token phrase patterns ("may_not", "shall_not", ...).

Domain-agnostic: только generic English markers.

Output:
  - per-entry: lowering_audit_v1.json (per a4v3 file)
  - corpus: lowering_audit_corpus_report_v1.{json,md}

CLI:
    python lowering_audit_v1.py [entry_dir|run_root]
"""
from __future__ import annotations
import json
import pathlib
import re
import sys
from collections import Counter, defaultdict

ROOT = pathlib.Path(__file__).resolve().parents[2]


# ─────────────────────────────────────────────────────────────────────────
# Lexicons of modal/temporal/action tokens — generic English, NOT domain
# ─────────────────────────────────────────────────────────────────────────

DEONTIC_OBLIGATION = {
    "shall", "must", "required", "obligated", "endeavors", "endeavor",
    "strives", "strive", "undertakes", "undertake", "responsible",
}
DEONTIC_PERMISSION = {
    "may", "permitted", "allowed",
}
DEONTIC_PROHIBITION = {
    "cannot", "forbidden", "prohibited",
}

# Multi-token phrases that compose into deontic semantics — only when adjacent
DEONTIC_PROHIBITION_PHRASES = [
    "may_not", "must_not", "shall_not",
    "not_permitted", "not_allowed",
]

# ── Epistemic possibility (≠ deontic permission) ──
# When `may` combines with a state-of-affairs verb expressing uncertainty about
# whether something WILL happen (not whether someone IS PERMITTED), the right
# lowering is expression-grammar: existential or `prop eventually(...)`,
# NOT DeonticDecl.permission.
EPISTEMIC_POSSIBILITY_PHRASES = [
    # Stative / passive — almost never agentive permission, true epistemic.
    "may_occur", "may_arise", "may_appear", "may_exist", "may_become",
    "may_be_needed", "may_be_necessary",
    # Note: `may_affect`, `may_cause`, `may_change`, `may_prevent`, `may_have`
    # are intentionally NOT here — they're often agentive (`may change X`,
    # `may prevent X` = permission). Let them fall through to standalone
    # `may` token detection as DeonticDecl.permission. The user must
    # disambiguate per-entry.
]

# Conditional obligation: pattern `may_be_required` — "if condition, then required"
# Same surface trigger but distinct semantics from epistemic_possibility.
CONDITIONAL_OBLIGATION_PHRASES = [
    "may_be_required",
]

# ── Drop patterns: names where triggers are NOT modalities ──
# These names match triggers but are domain-agnostic structural predicates
# (binary day relations, numeric/comparative bounds, parametric temporal
# helpers). We don't want false positives on them.
DROP_NAME_PATTERNS = [
    re.compile(r"^(?:before|after|during|until|since)$"),
    re.compile(r"^business_days_(?:before|after)$"),
    re.compile(r"^calendar_days_(?:before|after)$"),
    re.compile(r"^trading_days_(?:before|after)$"),
    # comparative "as ... as before"
    re.compile(r"_as_before$"),
    # numeric/range "within ... limit/range/bound/tolerance/threshold"
    re.compile(r"within_[A-Za-z_]+_(?:limit|range|bound|tolerance|threshold|cap|ceiling|floor)$"),
    re.compile(r"^within_(?:limit|range|bound|tolerance|threshold|cap|ceiling|floor)"),
    # Well-known abstract sequence relations between non-temporal carriers
    # (events, solution steps, calculation stages). The "before"/"after"
    # token here denotes ordering between domain objects, not a temporal
    # claim — so they should not be flagged as TemporalDecl candidates.
    re.compile(r"^(?:step|event|stage|phase|round)_(?:before|after|precedes|follows)$"),
]

TEMPORAL_TOKENS = {
    "before", "after", "until", "always", "eventually", "once",
    "previously", "subsequently", "thereafter", "during",
    "within",  # within X period — deadline-ish, often DeonticDecl.deadline
}
TEMPORAL_PHRASES = [
    "prior_to", "subsequent_to", "at_all_times", "as_of",
]

ACTION_TOKENS = {
    "transitions", "becomes", "upon",
}

# Map (token → (family, sub-kind, spec_family_no))
_LEXICON: list[tuple[set[str], str, str, str]] = [
    (DEONTIC_OBLIGATION, "DeonticDecl", "obligation", "#31"),
    (DEONTIC_PERMISSION, "DeonticDecl", "permission", "#32"),
    (DEONTIC_PROHIBITION, "DeonticDecl", "prohibition", "#33"),
    (TEMPORAL_TOKENS, "TemporalDecl", "temporal_marker", "#29"),
    (ACTION_TOKENS, "ActionDecl", "transition", "#26"),
]

_PHRASE_LEXICON: list[tuple[list[str], str, str, str]] = [
    *((p.split("_"), "DeonticDecl", "prohibition", "#33") for p in DEONTIC_PROHIBITION_PHRASES),
    *((p.split("_"), "TemporalDecl", "temporal_marker", "#29") for p in TEMPORAL_PHRASES),
    # Epistemic possibility: not Deontic — should be expression-grammar level
    *((p.split("_"), "ExpressionGrammar", "epistemic_possibility", "expr#exists/eventually")
      for p in EPISTEMIC_POSSIBILITY_PHRASES),
    # Conditional obligation: matches phrase pattern, candidate is DeonticDecl#31
    # with a guard. We mark it distinctly to keep the conditional flavor.
    *((p.split("_"), "DeonticDecl", "conditional_obligation", "#31+guard")
      for p in CONDITIONAL_OBLIGATION_PHRASES),
]


# ─────────────────────────────────────────────────────────────────────────
# Tokenization
# ─────────────────────────────────────────────────────────────────────────

_CAMEL_RE = re.compile(r"[A-Z][a-z]*|[a-z]+|[0-9]+")


def _tokenize_name(name: str) -> list[str]:
    """Split symbol name into lowercased tokens.

    `not_completely_ruled_out` → [not, completely, ruled, out]
    `IndexComponent` → [index, component]
    `MarketCap2_v3` → [market, cap, 2, v, 3]
    """
    parts: list[str] = []
    for chunk in name.split("_"):
        for m in _CAMEL_RE.findall(chunk):
            parts.append(m.lower())
    return parts


def _check_phrases(tokens: list[str]) -> list[dict]:
    """Find multi-token phrases inside the token sequence."""
    hits: list[dict] = []
    n = len(tokens)
    for phrase_tokens, family, kind, spec in _PHRASE_LEXICON:
        plen = len(phrase_tokens)
        for i in range(n - plen + 1):
            if tokens[i:i + plen] == phrase_tokens:
                hits.append({
                    "matched": "_".join(phrase_tokens),
                    "family": family,
                    "kind": kind,
                    "spec_ref": spec,
                    "match_kind": "phrase",
                })
    return hits


def _check_single_tokens(tokens: list[str]) -> list[dict]:
    hits: list[dict] = []
    for tok in tokens:
        for token_set, family, kind, spec in _LEXICON:
            if tok in token_set:
                hits.append({
                    "matched": tok,
                    "family": family,
                    "kind": kind,
                    "spec_ref": spec,
                    "match_kind": "token",
                })
    return hits


def audit_symbol(name: str) -> list[dict]:
    """Returns list of all lowering smells found in this symbol name.

    Drop-pattern check first: names whose triggers are structural predicates
    (`before` literally, comparative `*_as_before`, numeric `within_*_limit`)
    return [].

    Phrase matches take precedence over single-token matches that fall INSIDE
    the phrase. We dedupe by deleting single hits that are subsumed by phrase
    hits — this avoids "may_occur" being also flagged as standalone "may".
    """
    # Drop-pattern check: skip whole symbol if it matches a structural pattern
    for pat in DROP_NAME_PATTERNS:
        if pat.search(name):
            return []

    tokens = _tokenize_name(name)
    phrase_hits = _check_phrases(tokens)
    token_hits = _check_single_tokens(tokens)

    # If we matched a phrase, drop the standalone token hits whose tokens are
    # consumed by ANY phrase match. This unifies "may_occur" → epistemic_possibility
    # (not also DeonticDecl.permission via standalone "may").
    phrase_tokens_consumed: set[str] = set()
    for ph in phrase_hits:
        for t in ph["matched"].split("_"):
            phrase_tokens_consumed.add(t)
    filtered_tokens = [
        h for h in token_hits if h["matched"] not in phrase_tokens_consumed
    ] if phrase_hits else token_hits

    return phrase_hits + filtered_tokens


# ─────────────────────────────────────────────────────────────────────────
# a4v3 declaration parser (reuse from cross_entry_consistency_v1)
# ─────────────────────────────────────────────────────────────────────────

_DECL_LINE_RE = re.compile(
    r"^\s*(sort|entity|fun|rel|axiom|constraint|fact|action|prop|"
    r"obligation|permission|prohibition|theorem|val)\s+([A-Za-z_][A-Za-z0-9_]*)"
    r"(?:\s*[:=]\s*(.*))?$",
    re.MULTILINE,
)


def _parse_decls(text: str) -> list[dict]:
    out: list[dict] = []
    for i, line in enumerate(text.splitlines(), start=1):
        if line.lstrip().startswith("#"):
            continue
        m = _DECL_LINE_RE.match(line)
        if not m:
            continue
        out.append({
            "kind": m.group(1),
            "name": m.group(2),
            "line_no": i,
            "raw": line.strip(),
        })
    return out


# ─────────────────────────────────────────────────────────────────────────
# Entry-level audit
# ─────────────────────────────────────────────────────────────────────────

# Arithmetic / quantity sorts — entities of these sorts don't carry temporal
# or deontic semantics in their values. Compound names like
# `CookiesAfterGiving : CountQuantity` use "after" as state-tracking suffix,
# not as a TemporalDecl marker. Skip name-level audit for entities whose
# sort is one of these to avoid false positives in math word problem and
# similar arithmetic-heavy corpora.
_ARITHMETIC_QUANTITY_SORTS = {
    # Arithmetic / quantity carriers
    "Quantity", "CountQuantity", "FractionQuantity",
    "MonetaryAmount", "Percent",
    "Real", "Integer", "Nat", "Number",
    "LengthQuantity", "PercentQuantity", "ConversionQuantity",
    # Abstract math-problem carriers — names of these (e.g. Add, Subtract,
    # RemainingAfter, TakeFractionOf) are abstract operation tags, not
    # temporal/action claims. Without this guard `entity RemainingAfter :
    # Operation` (a prelude operation tag) triggers TemporalDecl smell.
    "Operation", "ProblemEvent", "SolutionStep", "Equation",
    "ArithmeticExpression", "UnknownQuantity", "Answer",
    "ProblemActor", "ProblemObject", "MathProblem",
}


def audit_entry(entry_dir: pathlib.Path) -> dict:
    a4v3_p = entry_dir / "main_ir.a4v3"
    if not a4v3_p.exists():
        return {"entry_id": entry_dir.name, "skipped": True, "reason": "no a4v3"}
    text = a4v3_p.read_text(encoding="utf-8")
    decls = _parse_decls(text)

    smells: list[dict] = []
    for d in decls:
        # We only check name-level smells on rel / fun / entity / val / fact /
        # constraint — these are where "buried modality in name" is the bug.
        # If decl is already DeonticDecl/TemporalDecl/ActionDecl — skip
        # (correct lowering already in place).
        if d["kind"] in ("obligation", "permission", "prohibition",
                         "prop", "action", "theorem"):
            continue
        if d["kind"] in ("axiom", "constraint", "fact"):
            # Body of these may use modalities, but name itself usually plain.
            # We still check name to catch e.g. `constraint may_be_excluded_from_index : ...`
            pass
        # Skip entity decls whose sort is purely arithmetic — names like
        # `CookiesAfterGiving : CountQuantity` use "after" as state-tracking
        # suffix, not as a TemporalDecl marker. Same for `MoneyOwnedBefore`
        # etc. Without this guard the detector produces blocking false
        # positives on every arithmetic word problem.
        if d["kind"] == "entity":
            m = re.search(r":\s*([A-Za-z_]\w*)", d["raw"])
            if m and m.group(1) in _ARITHMETIC_QUANTITY_SORTS:
                continue
        hits = audit_symbol(d["name"])
        if not hits:
            continue
        for h in hits:
            smells.append({
                "entry_id": entry_dir.name,
                "decl_kind": d["kind"],
                "symbol": d["name"],
                "line_no": d["line_no"],
                "matched_token_or_phrase": h["matched"],
                "candidate_family": h["family"],
                "candidate_kind": h["kind"],
                "spec_ref": h["spec_ref"],
                "match_kind": h["match_kind"],
                "raw_decl": d["raw"][:120],
            })

    # Aggregate
    by_family: Counter = Counter()
    by_token: Counter = Counter()
    for s in smells:
        by_family[f"{s['candidate_family']}.{s['candidate_kind']}"] += 1
        by_token[s["matched_token_or_phrase"]] += 1

    return {
        "entry_id": entry_dir.name,
        "skipped": False,
        "n_decls": len(decls),
        "n_smells": len(smells),
        "by_candidate_family": dict(by_family),
        "by_matched": dict(by_token),
        "smells": smells,
    }


def _save_entry(entry_dir: pathlib.Path, result: dict) -> pathlib.Path:
    out = entry_dir / "lowering_audit_v1.json"
    out.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n",
                   encoding="utf-8")
    return out


def aggregate(run_root: pathlib.Path) -> dict:
    entries: list[dict] = []
    for d in sorted(run_root.rglob("main_ir.a4v3")):
        entry_dir = d.parent
        if entry_dir.name.startswith("_"):
            continue
        entries.append(audit_entry(entry_dir))

    n = sum(1 for e in entries if not e.get("skipped"))

    # corpus-wide aggregations
    by_family: Counter = Counter()
    by_token: Counter = Counter()
    by_symbol: dict[str, list] = defaultdict(list)  # symbol → entries
    n_entries_with_smells = 0
    for e in entries:
        if e.get("skipped"):
            continue
        if e["n_smells"] > 0:
            n_entries_with_smells += 1
        for f, c in e["by_candidate_family"].items():
            by_family[f] += c
        for t, c in e["by_matched"].items():
            by_token[t] += c
        for s in e["smells"]:
            by_symbol[s["symbol"]].append({
                "entry": s["entry_id"],
                "decl_kind": s["decl_kind"],
                "matched": s["matched_token_or_phrase"],
                "candidate_family": s["candidate_family"],
                "candidate_kind": s["candidate_kind"],
                "spec_ref": s["spec_ref"],
                "line_no": s["line_no"],
            })

    # Top smelly symbols (most frequent across corpus)
    top_symbols = sorted(by_symbol.items(),
                          key=lambda kv: (-len(kv[1]), kv[0]))

    return {
        "run": run_root.name,
        "n_entries": n,
        "n_entries_with_smells": n_entries_with_smells,
        "total_smells": sum(by_family.values()),
        "by_candidate_family": dict(by_family.most_common()),
        "by_matched_token": dict(by_token.most_common()),
        "by_symbol": {k: v for k, v in top_symbols},
        "top_smelly_symbols": [
            {"symbol": k, "occurrences": len(v), "entries": sorted({x["entry"] for x in v})}
            for k, v in top_symbols[:30]
        ],
    }


def _md_corpus_report(agg: dict) -> str:
    lines: list[str] = []
    lines.append(f"# Lowering audit — {agg['run']}")
    lines.append("")
    lines.append("Det-сканер по именам rel/fun/entity/val/constraint/fact: ищет ")
    lines.append("модальные/временные/деонтические токены, означающие что семантика ")
    lines.append("первого класса (DeonticDecl/TemporalDecl/ActionDecl) **зашита в имя** ")
    lines.append("вместо использования соответствующей a4v3 family.")
    lines.append("")
    lines.append(f"- entries: **{agg['n_entries']}**")
    lines.append(f"- entries with at least one smell: **{agg['n_entries_with_smells']}**")
    lines.append(f"- total smells: **{agg['total_smells']}**")
    lines.append("")

    lines.append("## By candidate target family")
    lines.append("")
    lines.append("«Если переписать smell правильно, какая family должна быть использована»:")
    lines.append("")
    lines.append("| candidate family | total occurrences |")
    lines.append("|---|---:|")
    for f, c in agg["by_candidate_family"].items():
        lines.append(f"| `{f}` | {c} |")
    lines.append("")

    lines.append("## By matched token / phrase")
    lines.append("")
    lines.append("| trigger | occurrences |")
    lines.append("|---|---:|")
    for t, c in agg["by_matched_token"].items():
        lines.append(f"| `{t}` | {c} |")
    lines.append("")

    lines.append("## Top smelly symbols (most repeated across corpus)")
    lines.append("")
    lines.append("| symbol | occurrences | entries |")
    lines.append("|---|---:|---|")
    for r in agg["top_smelly_symbols"]:
        ents = ", ".join(r["entries"][:6])
        if len(r["entries"]) > 6:
            ents += f" (+{len(r['entries']) - 6})"
        lines.append(f"| `{r['symbol']}` | {r['occurrences']} | {ents} |")
    lines.append("")

    lines.append("## Refactor cookbook (a4v3 spec ref → canonical lowering)")
    lines.append("")
    lines.append("```")
    lines.append("# Smell:")
    lines.append("rel must_be_published_by : Document, Organization")
    lines.append("# Refactor (DeonticDecl#31 obligation):")
    lines.append("obligation Publish(agent: Organization, target: Document)")
    lines.append("  action: publish")
    lines.append("  deadline: <if applicable>")
    lines.append("")
    lines.append("# Smell:")
    lines.append("rel may_be_excluded : IndexComponent")
    lines.append("# Refactor (DeonticDecl#32 permission):")
    lines.append("permission Exclude(agent: IndexProvider, target: IndexComponent)")
    lines.append("  action: exclude")
    lines.append("")
    lines.append("# Smell:")
    lines.append("rel cannot_be_changed : Document")
    lines.append("# Refactor (DeonticDecl#33 prohibition):")
    lines.append("prohibition Change(agent: AnyParty, target: Document)")
    lines.append("  action: change")
    lines.append("")
    lines.append("# Smell:")
    lines.append("rel published_before : Document, Day")
    lines.append("# Refactor (TemporalDecl#29 once / past-time):")
    lines.append("prop document_published_in_past : once(published(document))")
    lines.append("```")
    lines.append("")

    return "\n".join(lines)


def main():
    args = sys.argv[1:]
    target = pathlib.Path(args[0]) if args else (
        ROOT / "IR/outputs/runs/unified_methodology_v1")

    if (target / "main_ir.a4v3").exists():
        result = audit_entry(target)
        _save_entry(target, result)
        if not result.get("skipped"):
            print(f"Wrote {target / 'lowering_audit_v1.json'}")
            print(f"  smells: {result['n_smells']}")
            print(f"  by family: {result['by_candidate_family']}")
        return

    # corpus mode
    n = 0
    for d in sorted(target.rglob("main_ir.a4v3")):
        entry_dir = d.parent
        if entry_dir.name.startswith("_"):
            continue
        result = audit_entry(entry_dir)
        _save_entry(entry_dir, result)
        n += 1

    agg = aggregate(target)
    json_p = target / "lowering_audit_corpus_report_v1.json"
    md_p = target / "lowering_audit_corpus_report_v1.md"
    json_p.write_text(json.dumps(agg, indent=2, ensure_ascii=False, default=str) + "\n",
                      encoding="utf-8")
    md_p.write_text(_md_corpus_report(agg), encoding="utf-8")
    print(f"Wrote {json_p.relative_to(ROOT)}")
    print(f"Wrote {md_p.relative_to(ROOT)}")
    print()
    print(f"Per-entry written: {n}")
    print(f"Entries with smells: {agg['n_entries_with_smells']}/{agg['n_entries']}")
    print(f"Total smells: {agg['total_smells']}")
    print(f"By family: {agg['by_candidate_family']}")
    print(f"Top trigger tokens: {dict(list(agg['by_matched_token'].items())[:10])}")


if __name__ == "__main__":
    main()
