"""source_phrase_coverage_v1.py

Det metric: which noun-ish phrases from source.md are referenced in IR?

Complements `ungrounded_*` (which checks IR -> source). This checks
source -> IR: recall side of phrase coverage.

Heuristic phrase extraction (no NLP library):
1. Capitalized multi-word phrases ("Closing Price", "Market Capitalization")
2. Hyphenated terms ("market-cap", "post-tax")
3. Quoted terms ("X" or 'X' or `X`)
4. Single capitalized non-stopword Title-Case words ("Solactive", "Recalculation")

For each candidate phrase:
- Tokenize lowercased + stemmed (using same stemmer as extended_grounding)
- Check whether ANY IR symbol/sort/entity has overlapping content tokens

Coverage rate = covered / total_phrases.

Saves: metrics_source_phrase_coverage_v1.json per entry.

CLI:
    python source_phrase_coverage_v1.py [entry_dir|run_root]
"""
from __future__ import annotations
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import extended_grounding_check_v1 as ext  # noqa: E402

# Common English stopwords + methodology fluff. Domain-agnostic.
_STOPWORDS = {
    "the", "a", "an", "of", "in", "on", "at", "for", "to", "from", "by",
    "and", "or", "but", "if", "with", "as", "is", "are", "was", "were",
    "be", "been", "being", "have", "has", "had", "this", "that", "these",
    "those", "it", "its", "they", "their", "them", "we", "our", "you",
    "your", "i", "me", "my", "he", "she", "his", "her", "him", "shall",
    "may", "must", "should", "will", "would", "can", "could", "might",
    "however", "therefore", "thus", "such", "than", "then", "when", "while",
    "between", "among", "any", "all", "no", "not", "each", "every", "some",
    "section", "chapter", "page", "above", "below", "following", "based",
    "respect", "case", "time", "value",  # too generic to be a "phrase"
}

_CAPITALIZED_PHRASE_RE = re.compile(
    r"(?<!\.)\b(?:[A-Z][a-z]+(?:[- ][A-Z][a-z]+)*)\b"
)
_HYPHENATED_RE = re.compile(r"\b[a-z]+(?:-[a-z]+)+\b")
_QUOTED_RE = re.compile(r"[\"“‘']([^\"”’']{2,80})[\"”’']")
_BACKTICK_RE = re.compile(r"`([^`]{2,80})`")


def _strip_md(text: str) -> str:
    return "\n".join(
        line for line in text.splitlines() if not line.lstrip().startswith("#")
    )


def _extract_phrases(source: str) -> list[str]:
    text = _strip_md(source or "")
    phrases: set[str] = set()
    for m in _CAPITALIZED_PHRASE_RE.finditer(text):
        ph = m.group(0).strip()
        # filter solo stopwords
        if ph.lower() in _STOPWORDS:
            continue
        if len(ph) < 3:
            continue
        phrases.add(ph)
    for m in _HYPHENATED_RE.finditer(text):
        phrases.add(m.group(0))
    for m in _QUOTED_RE.finditer(text):
        ph = m.group(1).strip()
        if 2 <= len(ph.split()) <= 6 or len(ph) >= 4:
            phrases.add(ph)
    for m in _BACKTICK_RE.finditer(text):
        phrases.add(m.group(1).strip())
    # Drop stopword-only phrases
    out = [p for p in phrases if any(
        w.lower() not in _STOPWORDS for w in re.findall(r"\w+", p)
    )]
    return sorted(out, key=lambda p: (-len(p), p))


def _phrase_tokens(phrase: str) -> set[str]:
    # split, lowercase, drop stopwords, stem
    parts = re.findall(r"[A-Za-z]+", phrase)
    raw = {p.lower() for p in parts if p.lower() not in _STOPWORDS and len(p) >= 3}
    stems = {ext._stem(p) for p in raw}
    return raw | stems


def _ir_token_universe(a4v3_text: str) -> set[str]:
    """All content tokens reachable from IR declarations + bodies."""
    tokens: set[str] = set()
    for line in a4v3_text.splitlines():
        if line.lstrip().startswith("#"):
            continue
        for w in re.findall(r"[A-Za-z][A-Za-z_0-9]*", line):
            tokens.update(ext._normalize_name(w))
    return tokens


def analyze_entry(entry_dir: pathlib.Path) -> dict:
    src_p = entry_dir / "source.md"
    a4v3_p = entry_dir / "main_ir.a4v3"
    source = src_p.read_text(encoding="utf-8") if src_p.exists() else ""
    a4v3 = a4v3_p.read_text(encoding="utf-8") if a4v3_p.exists() else ""

    phrases = _extract_phrases(source)
    ir_tokens = _ir_token_universe(a4v3)

    covered: list[dict] = []
    uncovered: list[dict] = []
    for ph in phrases:
        toks = _phrase_tokens(ph)
        if not toks:
            continue
        # phrase is "covered" if every meaningful token has at least one match
        # in the IR token universe (after stemming/casing normalization)
        matched = {t for t in toks if t in ir_tokens}
        coverage = len(matched) / max(1, len(toks))
        rec = {"phrase": ph, "tokens": sorted(toks), "matched": sorted(matched),
               "token_coverage": round(coverage, 3)}
        if coverage >= 0.5:
            covered.append(rec)
        else:
            uncovered.append(rec)

    n = len(covered) + len(uncovered)
    return {
        "entry_id": entry_dir.name,
        "phrase_count": n,
        "covered_count": len(covered),
        "uncovered_count": len(uncovered),
        "coverage_rate": round(len(covered) / n, 3) if n else None,
        "covered": covered,
        "uncovered": uncovered,
    }


def _save(entry_dir: pathlib.Path, result: dict) -> pathlib.Path:
    out = entry_dir / "metrics_source_phrase_coverage_v1.json"
    out.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n",
                   encoding="utf-8")
    return out


def main():
    if len(sys.argv) > 1:
        target = pathlib.Path(sys.argv[1])
    else:
        target = ROOT / "IR/outputs/runs/unified_methodology_v1"

    if (target / "main_ir.a4v3").exists() or (target / "source.md").exists():
        result = analyze_entry(target)
        out = _save(target, result)
        print(f"Wrote {out}")
        print(f"  phrases: {result['phrase_count']}, coverage: {result['coverage_rate']}")
        if result["uncovered"]:
            print(f"  uncovered: {[u['phrase'] for u in result['uncovered'][:8]]}")
        return

    n = 0
    low = 0
    for d in sorted(target.rglob("main_ir.a4v3")):
        entry_dir = d.parent
        if entry_dir.name.startswith("_"):
            continue
        result = analyze_entry(entry_dir)
        _save(entry_dir, result)
        n += 1
        if result["coverage_rate"] is not None and result["coverage_rate"] < 0.7:
            low += 1
    print(f"Processed {n} entries; {low} with coverage < 0.7.")


if __name__ == "__main__":
    main()
