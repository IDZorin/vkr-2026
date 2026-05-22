"""Text-intent classification tool."""
from __future__ import annotations

import json
from typing import Any

from ir_agent.env import ToolEnv
from ir_agent.helpers import _read_text, _strip_code_fence
from ir_agent.modal_patterns import _collect_corpus_precedents_for_classifier
from ir_agent.prompts.classifier import _CLASSIFY_INTENT_SYSTEM


def tool_classify_text_intent(env: ToolEnv) -> dict[str, Any]:
    """Classify the section's text type to determine modal-handling policy.

    Now CORPUS-AWARE: before classification, finds top-K semantically similar
    sections and extracts their family usage signals. Classifier sees these
    precedents and CALIBRATES its decision. Persists to
    discovery/text_intent_classification.json.

    Cached: if `discovery/text_intent_classification.json` already exists
    and contains valid output (no error), reuse it without re-calling the
    LLM. Lets `--reuse-from <prior_run>` skip expensive xhigh re-runs."""
    cached_path = env.discovery_dir / "text_intent_classification.json"
    if cached_path.exists():
        from ir_agent.helpers import _load_json as _lj
        cached = _lj(cached_path)
        if cached and "error" not in cached and "_load_error" not in cached:
            cached["_reused_cached"] = True
            return cached
    if env.client is None:
        return {"error": "intra-tool LLM client not configured"}
    source = _read_text(env.section_dir / "source.md")
    if not source.strip():
        return {"error": "source.md missing or empty"}

    corpus_block = _collect_corpus_precedents_for_classifier(env, source)

    user = (
        f"## SECTION SOURCE\n\n{source}\n\n"
        f"## CORPUS PRECEDENTS (similar sections in DZ)\n\n{corpus_block}\n\n"
        f"Classify per the schema. Calibrate to corpus practice; flag any "
        f"conflict between abstract rules and corpus practice in "
        f"corpus_alignment field."
    )
    _client, _xb, _mt = env.strategic_or_main(2560)
    try:
        result = _client.complete(
            [],
            raw_messages=[{"role": "system", "content": _CLASSIFY_INTENT_SYSTEM},
                          {"role": "user", "content": user}],
            max_tokens=_mt,
            extra_body=_xb,
            seed=env.seed,
        )
    except Exception as exc:
        return {"error": f"{type(exc).__name__}: {exc}"}
    raw = _strip_code_fence(result.text or "")
    try:
        parsed = json.loads(raw)
    except Exception as exc:
        return {"error": f"classifier returned non-JSON: {exc}",
                "raw_excerpt": raw[:500]}

    parsed["_corpus_precedents_used"] = corpus_block[:2000]
    (env.discovery_dir / "text_intent_classification.json").write_text(
        json.dumps(parsed, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8")
    return parsed
