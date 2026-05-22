"""provenance_backtranslation_metrics_v1.py

Advisory metrics for DZ provenance back-translations.

The check compares each provenance.yaml claim's source_quotes against its
back_translation. It is intentionally not a gate: source text can be longer,
more legalistic, or split across support facts, while a good back_translation
may be more structural. The goal is to make suspicious back-translations easy
to inspect, not to auto-reject IR.

Outputs:
  <entry>/provenance_backtranslation_metrics_v1.json
  <entry>/provenance_backtranslation_metrics_v1.md

CLI:
  python provenance_backtranslation_metrics_v1.py [entry_dir|run_root]
  python provenance_backtranslation_metrics_v1.py [entry_dir] --semantic
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import statistics
import sys
from collections import Counter
from datetime import datetime
from typing import Any

import yaml


ROOT = pathlib.Path(__file__).resolve().parents[2]
TOKEN_RE = re.compile(r"[A-Za-z0-9]+(?:[._:/%-][A-Za-z0-9]+)*")
URL_RE = re.compile(r"https?://[^\s)>\]\"']+")
NUMBER_RE = re.compile(r"\b\d{1,3}(?:,\d{3})+(?:\.\d+)?%?\b|\b\d+(?:[.,]\d+)?%?\b")

STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "been", "being", "by",
    "for", "from", "has", "have", "in", "into", "is", "it", "its", "of",
    "on", "or", "that", "the", "then", "there", "this", "to", "was",
    "were", "which", "with",
}

MODAL_FAMILIES = {
    "obligation": {
        "shall", "must", "obliged", "obligated", "required", "requirement",
        "will",
    },
    "permission": {"may", "permitted", "allowed", "can"},
    "prohibition": {"cannot", "prohibited", "forbidden", "not_permitted"},
    "possibility": {"may", "possible", "potential", "can"},
}
NEGATION_TOKENS = {"not", "no", "non", "never", "cannot", "without", "excluding"}


def _read_text(path: pathlib.Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="replace")


def _load_yaml(path: pathlib.Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        return data if isinstance(data, dict) else {"_load_error": "top-level YAML is not a mapping"}
    except Exception as exc:
        return {"_load_error": f"{type(exc).__name__}: {exc}"}


def _entry_dirs(target: pathlib.Path) -> list[pathlib.Path]:
    target = target.resolve()
    if (target / "provenance.yaml").exists() or (target / "main_ir.a4v3").exists():
        return [target]
    return [
        p.parent
        for p in sorted(target.rglob("provenance.yaml"))
        if (p.parent / "main_ir.a4v3").exists()
        and not p.parent.name.startswith("_")
    ]


def _tokens(text: str) -> list[str]:
    return [
        tok.lower()
        for tok in TOKEN_RE.findall(text or "")
        if tok and tok.lower() not in STOPWORDS
    ]


def _unique_tokens(text: str) -> set[str]:
    return set(_tokens(text))


def _urls(text: str) -> set[str]:
    return {u.rstrip(".,;:") for u in URL_RE.findall(text or "")}


def _numbers(text: str) -> set[str]:
    return {n.replace(",", "") for n in NUMBER_RE.findall(text or "")}


def _preservation_ratio(source_items: set[str], back_items: set[str]) -> float | None:
    if not source_items:
        return None
    return round(len(source_items & back_items) / len(source_items), 3)


def _extract_modal_families(text: str) -> set[str]:
    toks = set(_tokens(text))
    out: set[str] = set()
    for family, markers in MODAL_FAMILIES.items():
        if toks & markers:
            out.add(family)
    return out


def _metric_mean(values: list[float | None]) -> float | None:
    nums = [float(v) for v in values if isinstance(v, int | float)]
    if not nums:
        return None
    return round(statistics.mean(nums), 3)


def _semantic_scores(source_text: str, back_translation: str) -> dict[str, Any]:
    try:
        sys.path.insert(0, str(ROOT / "IR/src/legacy_metrics"))
        import compute_translation_metrics_v1 as legacy  # type: ignore

        bert = legacy._safe_bertscore(back_translation, source_text)
        bt_to_src = legacy._nli_scores(back_translation, source_text)
        src_to_bt = legacy._nli_scores(source_text, back_translation)
        contradictions = [
            v for v in (
                bt_to_src.get("contradiction"),
                src_to_bt.get("contradiction"),
            )
            if isinstance(v, int | float)
        ]
        return {
            "available": True,
            "bertscore": bert,
            "nli_back_translation_implies_source": bt_to_src,
            "nli_source_implies_back_translation": src_to_bt,
            "bidirectional_entailment_min": (
                None
                if not isinstance(bt_to_src.get("entailment"), int | float)
                or not isinstance(src_to_bt.get("entailment"), int | float)
                else round(min(float(bt_to_src["entailment"]), float(src_to_bt["entailment"])), 3)
            ),
            "max_contradiction": round(max(contradictions), 3) if contradictions else None,
        }
    except Exception as exc:
        return {
            "available": False,
            "error": f"{type(exc).__name__}: {exc}",
        }


def _score_claim(
    claim_id: str,
    claim: dict[str, Any],
    *,
    semantic: bool,
) -> dict[str, Any]:
    source_quotes = claim.get("source_quotes")
    if not isinstance(source_quotes, list):
        source_quotes = []
    source_text = " ".join(str(q).strip() for q in source_quotes if str(q).strip())
    back_translation = str(claim.get("back_translation") or "").strip()

    source_toks = _unique_tokens(source_text)
    back_toks = _unique_tokens(back_translation)
    common = source_toks & back_toks
    recall = round(len(common) / len(source_toks), 3) if source_toks else None
    precision = round(len(common) / len(back_toks), 3) if back_toks else None
    jaccard = round(len(common) / len(source_toks | back_toks), 3) if (source_toks or back_toks) else None

    source_nums = _numbers(source_text)
    back_nums = _numbers(back_translation)
    source_urls = _urls(source_text)
    back_urls = _urls(back_translation)
    source_modals = _extract_modal_families(source_text)
    back_modals = _extract_modal_families(back_translation)
    source_neg = set(_tokens(source_text)) & NEGATION_TOKENS
    back_neg = set(_tokens(back_translation)) & NEGATION_TOKENS

    number_preservation = _preservation_ratio(source_nums, back_nums)
    url_preservation = _preservation_ratio(source_urls, back_urls)
    modal_preservation = _preservation_ratio(source_modals, back_modals)
    negation_preservation = _preservation_ratio(source_neg, back_neg)

    deterministic_score_parts = [
        recall,
        precision,
        jaccard,
        1.0 if number_preservation is None else number_preservation,
        1.0 if url_preservation is None else url_preservation,
        1.0 if modal_preservation is None else modal_preservation,
        1.0 if negation_preservation is None else negation_preservation,
    ]
    deterministic_score = _metric_mean(deterministic_score_parts)

    warnings: list[str] = []
    if recall is not None and recall < 0.35:
        warnings.append("low_source_token_recall")
    if precision is not None and precision < 0.25:
        warnings.append("low_back_translation_token_precision")
    if number_preservation is not None and number_preservation < 1.0:
        warnings.append("number_not_preserved")
    if url_preservation is not None and url_preservation < 1.0:
        warnings.append("url_not_preserved")
    if modal_preservation is not None and modal_preservation < 1.0:
        warnings.append("modal_family_not_preserved")
    if negation_preservation is not None and negation_preservation < 1.0:
        warnings.append("negation_not_preserved")
    if not back_translation:
        warnings.append("missing_back_translation")
    if not source_text:
        warnings.append("missing_source_quotes")

    result: dict[str, Any] = {
        "claim_id": claim_id,
        "kind": claim.get("kind"),
        "claim_origin": claim.get("claim_origin"),
        "status": claim.get("status"),
        "source_quote_count": len(source_quotes),
        "source_char_len": len(source_text),
        "back_translation_char_len": len(back_translation),
        "source_token_count": len(source_toks),
        "back_translation_token_count": len(back_toks),
        "source_token_recall": recall,
        "back_translation_token_precision": precision,
        "token_jaccard": jaccard,
        "number_preservation": number_preservation,
        "url_preservation": url_preservation,
        "modal_family_preservation": modal_preservation,
        "negation_preservation": negation_preservation,
        "deterministic_meaningfulness_score": deterministic_score,
        "warnings": warnings,
    }
    if semantic:
        result["semantic"] = _semantic_scores(source_text, back_translation)
    return result


def analyze_entry(entry_dir: pathlib.Path, *, semantic: bool = False) -> dict[str, Any]:
    data = _load_yaml(entry_dir / "provenance.yaml")
    if not (entry_dir / "provenance.yaml").exists():
        return {
            "schema": "provenance_backtranslation_metrics_v1",
            "entry_id": entry_dir.name,
            "generated_at": datetime.now().isoformat(timespec="seconds"),
            "status": "missing_provenance",
            "semantic_requested": semantic,
            "summary": {},
            "claims": [],
        }
    if data.get("_load_error"):
        return {
            "schema": "provenance_backtranslation_metrics_v1",
            "entry_id": entry_dir.name,
            "generated_at": datetime.now().isoformat(timespec="seconds"),
            "status": "yaml_parse_error",
            "error": data["_load_error"],
            "semantic_requested": semantic,
            "summary": {},
            "claims": [],
        }
    claims = data.get("claims")
    if not isinstance(claims, dict):
        claims = {}
    claim_rows = [
        _score_claim(str(claim_id), claim, semantic=semantic)
        for claim_id, claim in claims.items()
        if isinstance(claim, dict)
    ]
    source_claims = [c for c in claim_rows if c.get("claim_origin") == "source_claim"]
    warning_counts = Counter(w for c in claim_rows for w in c.get("warnings", []))

    summary = {
        "claim_count": len(claim_rows),
        "source_claim_count": len(source_claims),
        "claims_with_warnings": sum(1 for c in claim_rows if c.get("warnings")),
        "source_claims_with_warnings": sum(1 for c in source_claims if c.get("warnings")),
        "mean_deterministic_meaningfulness_score": _metric_mean([
            c.get("deterministic_meaningfulness_score") for c in claim_rows
        ]),
        "mean_source_claim_deterministic_meaningfulness_score": _metric_mean([
            c.get("deterministic_meaningfulness_score") for c in source_claims
        ]),
        "mean_source_token_recall": _metric_mean([c.get("source_token_recall") for c in claim_rows]),
        "mean_back_translation_token_precision": _metric_mean([
            c.get("back_translation_token_precision") for c in claim_rows
        ]),
        "warning_counts": dict(sorted(warning_counts.items())),
    }
    if semantic:
        semantic_claims = [
            c.get("semantic", {}) for c in claim_rows
            if isinstance(c.get("semantic"), dict) and c.get("semantic", {}).get("available")
        ]
        summary["semantic_available_claim_count"] = len(semantic_claims)
        summary["mean_bertscore_f1"] = _metric_mean([
            s.get("bertscore", {}).get("f1") for s in semantic_claims
        ])
        summary["mean_bidirectional_entailment_min"] = _metric_mean([
            s.get("bidirectional_entailment_min") for s in semantic_claims
        ])
        summary["max_contradiction"] = (
            max(
                float(s["max_contradiction"])
                for s in semantic_claims
                if isinstance(s.get("max_contradiction"), int | float)
            )
            if any(isinstance(s.get("max_contradiction"), int | float) for s in semantic_claims)
            else None
        )

    return {
        "schema": "provenance_backtranslation_metrics_v1",
        "entry_id": entry_dir.name,
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "status": "ok",
        "semantic_requested": semantic,
        "summary": summary,
        "claims": claim_rows,
    }


def write_report(entry_dir: pathlib.Path, report: dict[str, Any]) -> None:
    json_p = entry_dir / "provenance_backtranslation_metrics_v1.json"
    md_p = entry_dir / "provenance_backtranslation_metrics_v1.md"
    json_p.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    summary = report.get("summary", {}) if isinstance(report.get("summary"), dict) else {}
    claims = report.get("claims", []) if isinstance(report.get("claims"), list) else []
    lines = [
        f"# Provenance Back-Translation Metrics: {report.get('entry_id')}",
        "",
        f"- status: `{report.get('status')}`",
        f"- semantic_requested: `{report.get('semantic_requested')}`",
        f"- claim_count/source_claim_count: `{summary.get('claim_count')}` / `{summary.get('source_claim_count')}`",
        f"- claims_with_warnings/source_claims_with_warnings: `{summary.get('claims_with_warnings')}` / `{summary.get('source_claims_with_warnings')}`",
        f"- mean deterministic score: `{summary.get('mean_deterministic_meaningfulness_score')}`",
        f"- mean source-claim deterministic score: `{summary.get('mean_source_claim_deterministic_meaningfulness_score')}`",
        f"- mean source token recall: `{summary.get('mean_source_token_recall')}`",
        f"- mean back-translation token precision: `{summary.get('mean_back_translation_token_precision')}`",
        f"- warning_counts: `{json.dumps(summary.get('warning_counts', {}), ensure_ascii=False)}`",
    ]
    if report.get("semantic_requested"):
        lines.extend([
            f"- semantic_available_claim_count: `{summary.get('semantic_available_claim_count')}`",
            f"- mean BERTScore F1: `{summary.get('mean_bertscore_f1')}`",
            f"- mean bidirectional entailment min: `{summary.get('mean_bidirectional_entailment_min')}`",
            f"- max contradiction: `{summary.get('max_contradiction')}`",
        ])
    lines.extend(["", "## Lowest Deterministic Scores", ""])
    ranked = sorted(
        claims,
        key=lambda c: (
            1.0 if c.get("deterministic_meaningfulness_score") is None
            else float(c.get("deterministic_meaningfulness_score")),
            str(c.get("claim_id")),
        ),
    )
    lines.append("| claim | origin | score | recall | precision | warnings |")
    lines.append("| --- | --- | ---: | ---: | ---: | --- |")
    for claim in ranked[:12]:
        warnings = ", ".join(f"`{w}`" for w in claim.get("warnings", [])) or "-"
        lines.append(
            f"| `{claim.get('claim_id')}` | `{claim.get('claim_origin')}` | "
            f"`{claim.get('deterministic_meaningfulness_score')}` | "
            f"`{claim.get('source_token_recall')}` | "
            f"`{claim.get('back_translation_token_precision')}` | {warnings} |"
        )
    md_p.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("target", type=pathlib.Path)
    ap.add_argument("--semantic", action="store_true", help="Also compute BERTScore/NLI if local models are available.")
    args = ap.parse_args(argv)

    entries = _entry_dirs(args.target)
    if not entries:
        raise SystemExit(f"No entries found under {args.target}")
    for entry in entries:
        report = analyze_entry(entry, semantic=args.semantic)
        write_report(entry, report)
        summary = report.get("summary", {}) if isinstance(report.get("summary"), dict) else {}
        print(
            f"{entry.name}: status={report.get('status')} "
            f"claims={summary.get('claim_count')} "
            f"score={summary.get('mean_deterministic_meaningfulness_score')}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
