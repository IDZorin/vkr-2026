"""semantic_claim_alignment_v1.py

Build a reviewable source-claim -> IR-block alignment ledger.

This is not a semantic proof and not a replacement for human/LLM judgment.
It creates the missing middle layer between token coverage and render-back:
each source claim gets candidate A4V3 declarations/assertions that appear to
carry it, plus explicit uncovered content tokens and review fields.

Outputs per entry:
  - semantic_claim_alignment_v1.json
  - semantic_claim_alignment_v1.md
  - semantic_claim_alignment_review_v1.json

CLI:
  python semantic_claim_alignment_v1.py <entry_dir|run_root>
"""
from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import re
import sys
from datetime import datetime
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(pathlib.Path(__file__).parent))

import a4v3_parser_v1 as parser  # noqa: E402
import token_provenance_v1 as token_provenance  # noqa: E402


_A4_KEYWORDS = {
    "sort", "entity", "rel", "fun", "fact", "constraint", "axiom", "key",
    "disjoint", "init", "forall", "exists", "and", "or", "not", "implies",
    "iff", "where", "count", "permission", "prohibition", "obligation",
    "action", "scope", "agent", "target", "extends",
}


def _read(path: pathlib.Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="replace")


def _load_json(path: pathlib.Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _strip_workspace_headers(text: str) -> str:
    lines = []
    for line in str(text or "").splitlines():
        clean = line.strip()
        if re.fullmatch(r"#?\s*Section\s+\d+(?:\.\d+)*\s+Source", clean, flags=re.IGNORECASE):
            continue
        lines.append(line)
    return "\n".join(lines).strip()


def _claim_units(source: str) -> list[dict[str, Any]]:
    """Split source into review-sized claim units.

    We keep this deliberately conservative: sentence-like units are primary,
    semicolon-separated long units are split, but coordinated lists remain
    intact so the reviewer can judge whether the IR decomposed them correctly.
    """
    text = _strip_workspace_headers(source)
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n+", text) if p.strip()]
    units: list[dict[str, Any]] = []
    for para in paragraphs:
        pieces = re.split(r"(?<!\d)(?<=[.!?])\s+(?!\d)", para)
        for piece in pieces:
            piece = piece.strip()
            if not piece:
                continue
            subpieces = [piece]
            if len(piece) > 420 and ";" in piece:
                subpieces = [s.strip() for s in piece.split(";") if s.strip()]
            for sub in subpieces:
                if len(re.findall(r"[A-Za-z0-9]", sub)) < 15:
                    continue
                units.append({
                    "claim_id": f"C{len(units) + 1:02d}",
                    "text": sub,
                    "hash": hashlib.sha1(sub.encode("utf-8")).hexdigest()[:12],
                })
    return units


def _content_token_groups(text: str) -> list[dict[str, Any]]:
    groups = []
    for item in token_provenance._source_tokens(text):
        if item.get("is_stopword"):
            continue
        token = str(item.get("token") or "")
        keys = set(item.get("keys") or [])
        if token:
            keys.add(token)
        keys = {k for k in keys if k and k not in _A4_KEYWORDS}
        if not keys:
            continue
        groups.append({
            "token": token,
            "surface_forms": item.get("surface_forms") or [],
            "keys": sorted(keys),
        })
    return groups


def _text_keys(text: str) -> set[str]:
    keys: set[str] = set()
    for match in re.finditer(r"[A-Za-z][A-Za-z0-9_]*|\d+(?:\.\d+)?%?", str(text or "")):
        keys.update(token_provenance._token_keys(match.group(0)))
    return {k for k in keys if k and k not in _A4_KEYWORDS}


def _extract_ir_blocks(ir_text: str) -> tuple[list[dict[str, Any]], str | None]:
    try:
        ast = parser.parse(ir_text)
    except Exception as exc:
        return [], f"{type(exc).__name__}: {exc}"

    blocks: list[dict[str, Any]] = []
    for decl in ast.get("declarations", []):
        if not isinstance(decl, dict):
            continue
        raw = str(decl.get("raw") or "")
        name = str(decl.get("name") or "")
        family = str(decl.get("family") or "")
        kind = str(decl.get("kind") or "")
        is_assertion = decl in (ast.get("assertions") or [])
        role = "assertion" if is_assertion else "declaration"
        block_id = f"{role}:{kind}:{name}" if name else f"{role}:{kind}:{decl.get('line_no')}"
        blocks.append({
            "block_id": block_id,
            "role": role,
            "family": family,
            "kind": kind,
            "name": name,
            "line": decl.get("line_no"),
            "raw": raw,
            "keys": sorted(_text_keys(raw)),
        })
    return blocks, None


def _candidate_alignment(claim: dict[str, Any], blocks: list[dict[str, Any]]) -> dict[str, Any]:
    groups = _content_token_groups(claim["text"])
    claim_keys_by_token = {g["token"]: set(g["keys"]) for g in groups}
    all_claim_keys = set().union(*claim_keys_by_token.values()) if claim_keys_by_token else set()

    candidates = []
    for block in blocks:
        block_keys = set(block.get("keys") or [])
        if not block_keys or not all_claim_keys:
            continue
        matched_groups = [
            token
            for token, keys in claim_keys_by_token.items()
            if keys & block_keys
        ]
        if not matched_groups:
            continue
        recall = len(matched_groups) / len(claim_keys_by_token)
        precision = len(set().union(*(claim_keys_by_token[t] for t in matched_groups)) & block_keys) / max(1, len(block_keys))
        score = (0.8 * recall) + (0.2 * precision)
        candidates.append({
            "block_id": block["block_id"],
            "role": block["role"],
            "family": block["family"],
            "kind": block["kind"],
            "name": block["name"],
            "line": block["line"],
            "token_recall": round(recall, 3),
            "token_precision": round(precision, 3),
            "score": round(score, 3),
            "matched_claim_tokens": sorted(matched_groups),
            "raw_excerpt": " ".join(block["raw"].split())[:500],
        })
    candidates.sort(key=lambda c: (c["score"], c["token_recall"]), reverse=True)
    top = candidates[:5]
    top_keys: set[str] = set()
    for cand in top[:3]:
        block = next((b for b in blocks if b["block_id"] == cand["block_id"]), None)
        if block:
            top_keys.update(block.get("keys") or [])
    covered_tokens = [
        token
        for token, keys in claim_keys_by_token.items()
        if keys & top_keys
    ]
    uncovered_tokens = [
        {
            "token": g["token"],
            "surface_forms": g["surface_forms"],
        }
        for g in groups
        if g["token"] not in covered_tokens
    ]
    coverage = len(covered_tokens) / max(1, len(groups))
    if coverage >= 0.75:
        auto_status = "strong_candidate"
    elif coverage >= 0.45:
        auto_status = "partial_candidate"
    else:
        auto_status = "weak_or_missing_candidate"
    return {
        "tokens": groups,
        "candidate_blocks": top,
        "candidate_count": len(candidates),
        "covered_claim_tokens_by_top3": sorted(covered_tokens),
        "uncovered_claim_tokens_by_top3": uncovered_tokens,
        "top3_token_coverage": round(coverage, 3),
        "auto_status": auto_status,
    }


def _review_map(entry_dir: pathlib.Path) -> dict[str, dict[str, Any]]:
    review = _load_json(entry_dir / "semantic_claim_alignment_review_v1.json")
    out: dict[str, dict[str, Any]] = {}
    for item in review.get("items") or []:
        if not isinstance(item, dict):
            continue
        key = str(item.get("claim_hash") or item.get("claim_id") or "")
        if key:
            out[key] = item
    return out


def analyze_entry(entry_dir: pathlib.Path) -> dict[str, Any]:
    source = _read(entry_dir / "source.md")
    ir_text = _read(entry_dir / "main_ir.a4v3")
    blocks, parse_error = _extract_ir_blocks(ir_text)
    existing_review = _review_map(entry_dir)

    claims = []
    for claim in _claim_units(source):
        alignment = _candidate_alignment(claim, blocks)
        old = existing_review.get(claim["hash"]) or existing_review.get(claim["claim_id"]) or {}
        claims.append({
            **claim,
            **alignment,
            "review": {
                "status": old.get("status") or "unreviewed",
                "reviewer": old.get("reviewer") or "",
                "comment": old.get("comment") or "",
                "approved_blocks": old.get("approved_blocks") or [],
            },
        })

    summary = {
        "claim_count": len(claims),
        "strong_candidate_count": sum(1 for c in claims if c["auto_status"] == "strong_candidate"),
        "partial_candidate_count": sum(1 for c in claims if c["auto_status"] == "partial_candidate"),
        "weak_or_missing_candidate_count": sum(1 for c in claims if c["auto_status"] == "weak_or_missing_candidate"),
        "reviewed_count": sum(1 for c in claims if c["review"]["status"] != "unreviewed"),
        "approved_count": sum(1 for c in claims if c["review"]["status"] == "approved"),
        "needs_revision_count": sum(1 for c in claims if c["review"]["status"] == "needs_ir_revision"),
        "average_top3_token_coverage": round(sum(c["top3_token_coverage"] for c in claims) / len(claims), 3) if claims else None,
    }
    summary["all_claims_review_approved"] = bool(claims) and summary["approved_count"] == len(claims)
    return {
        "entry_id": entry_dir.name,
        "schema": "semantic_claim_alignment_v1",
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "parse_error": parse_error,
        "summary": summary,
        "claims": claims,
    }


def _write_review_template(entry_dir: pathlib.Path, result: dict[str, Any]) -> None:
    path = entry_dir / "semantic_claim_alignment_review_v1.json"
    existing = _review_map(entry_dir)
    items = []
    for claim in result.get("claims") or []:
        old = existing.get(claim["hash"]) or existing.get(claim["claim_id"]) or {}
        items.append({
            "claim_id": claim["claim_id"],
            "claim_hash": claim["hash"],
            "claim_text": claim["text"],
            "status": old.get("status") or "unreviewed",
            "reviewer": old.get("reviewer") or "",
            "comment": old.get("comment") or "",
            "approved_blocks": old.get("approved_blocks") or [],
            "candidate_block_ids": [c["block_id"] for c in claim.get("candidate_blocks", [])],
        })
    payload = {
        "entry_id": result["entry_id"],
        "schema": "semantic_claim_alignment_review_v1",
        "allowed_status": [
            "unreviewed",
            "approved",
            "needs_ir_revision",
            "source_ambiguous",
            "not_formalized_by_design",
        ],
        "items": items,
    }
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def _write_md(entry_dir: pathlib.Path, result: dict[str, Any]) -> None:
    summary = result.get("summary") or {}
    lines = [
        f"# Semantic Claim Alignment: {result['entry_id']}",
        "",
        "This ledger maps source claims to candidate IR blocks. It is a review surface, not a proof.",
        "",
        "## Summary",
        "",
    ]
    for key, value in summary.items():
        lines.append(f"- {key}: `{value}`")
    if result.get("parse_error"):
        lines.extend(["", f"- parse_error: `{result['parse_error']}`"])
    lines.extend([
        "",
        "## Review Status Values",
        "",
        "- `approved`: source claim is faithfully represented by the approved IR block(s).",
        "- `needs_ir_revision`: source claim is missing, distorted, or only present in names.",
        "- `source_ambiguous`: source itself needs interpretation before judging IR.",
        "- `not_formalized_by_design`: claim is intentionally left as metadata/waiver/support text.",
        "",
        "## Claims",
        "",
    ])
    for claim in result.get("claims") or []:
        lines.append(f"### {claim['claim_id']} `{claim['auto_status']}`")
        lines.append("")
        lines.append(f"> {claim['text']}")
        lines.append("")
        lines.append(f"- top3 token coverage: `{claim['top3_token_coverage']}`")
        lines.append(f"- review status: `{claim['review']['status']}`")
        uncovered = claim.get("uncovered_claim_tokens_by_top3") or []
        if uncovered:
            forms = ", ".join(
                f"`{u['token']}` ({', '.join(u.get('surface_forms') or [])})"
                for u in uncovered
            )
            lines.append(f"- uncovered by top3: {forms}")
        else:
            lines.append("- uncovered by top3: none")
        lines.append("")
        lines.append("Candidate IR blocks:")
        candidates = claim.get("candidate_blocks") or []
        if not candidates:
            lines.append("- none")
        for cand in candidates:
            lines.append(
                f"- `{cand['block_id']}` line `{cand.get('line')}` "
                f"score `{cand['score']}`, recall `{cand['token_recall']}`"
            )
            lines.append(f"  `{cand['raw_excerpt']}`")
        lines.append("")
    (entry_dir / "semantic_claim_alignment_v1.md").write_text(
        "\n".join(lines).rstrip() + "\n",
        encoding="utf-8",
    )


def save_entry(entry_dir: pathlib.Path, result: dict[str, Any]) -> pathlib.Path:
    out = entry_dir / "semantic_claim_alignment_v1.json"
    out.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    _write_review_template(entry_dir, result)
    _write_md(entry_dir, result)
    return out


def process_entry(entry_dir: pathlib.Path) -> dict[str, Any]:
    result = analyze_entry(entry_dir)
    out = save_entry(entry_dir, result)
    return {
        "entry": entry_dir.name,
        "out": str(out),
        "summary": result.get("summary") or {},
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("target", nargs="?", default=str(ROOT / "case_studies/financial_methodology"))
    args = ap.parse_args()
    target = pathlib.Path(args.target)
    if (target / "main_ir.a4v3").exists() or (target / "source.md").exists():
        info = process_entry(target)
        s = info["summary"]
        print(f"Wrote {info['out']}")
        print(
            f"  claims: {s.get('claim_count')}, "
            f"strong/partial/weak: {s.get('strong_candidate_count')}/"
            f"{s.get('partial_candidate_count')}/{s.get('weak_or_missing_candidate_count')}"
        )
        return

    count = 0
    weak = 0
    for ir_path in sorted(target.rglob("main_ir.a4v3")):
        entry_dir = ir_path.parent
        if entry_dir.name.startswith("_"):
            continue
        if not _read(ir_path).strip():
            continue
        info = process_entry(entry_dir)
        count += 1
        weak += int(info["summary"].get("weak_or_missing_candidate_count") or 0)
    print(f"Processed {count} entries; weak/missing claim candidates: {weak}.")


if __name__ == "__main__":
    main()
