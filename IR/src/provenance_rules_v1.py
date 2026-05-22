"""provenance_rules_v1.py — canonical PROVENANCE RULES block.

This is a HARD RULE that must appear in EVERY LLM prompt that produces,
evaluates, renders, or otherwise touches IR or text derived from IR.

Rule layers:
  - IR formulas (constraint, fact, axiom, prop, theorem bodies):
      ONLY a4v3 spec + prelude/overlay + THIS section's source text.
      NO cross-section reasoning, NO domain-knowledge inference,
      NO user-hint-based content.
  - IR ontology (sort, entity, fun, rel declarations):
      may additionally use methodology context + general world-knowledge
      + human-comment hints, when grounded.
  - Cross-section links (e.g. "X defined elsewhere implies Y here"):
      belong to merge/bridge phase, NOT to this section's IR.

Usage:
    from provenance_rules_v1 import format_for_prompt
    SYSTEM = format_for_prompt() + "\\n\\n... task-specific instructions ..."

Or to embed inside an existing prompt:
    SYSTEM = "... " + format_for_prompt() + "\\n... rest ..."
"""
from __future__ import annotations


_PROVENANCE_RULES_TEXT = """═════════════════════════════════════════════════════════════════════════
PROVENANCE RULES (HARD — apply whenever you produce, evaluate, render,
or otherwise touch this section's IR or any text derived from it):
═════════════════════════════════════════════════════════════════════════

LAYER 1 — IR FORMULAS (bodies of `constraint`, `fact`, `axiom`, `prop`,
`theorem`, and any other a4v3 declaration whose payload is a formula):
  may contain ONLY content derivable from:
    (a) the a4v3 specification,
    (b) the prelude/overlay sorts and entities,
    (c) THIS section's source text.
  NO cross-section reasoning. NO domain-knowledge inference.
  NO user-hint-based content. NO encoding of background explanations.

LAYER 2 — IR ONTOLOGY (top-level `sort`, `entity`, `val`, `fun`, `rel`,
`event`, `var`, `property` declarations — the symbol catalog):
  may additionally use:
    (d) general methodology context (companion sections of the same
        document, when explicitly named in the source as defined terms),
    (e) general world-knowledge that a competent reader brings to the
        domain,
    (f) human-comment hints provided alongside the source.
  Even at this layer, every introduced sort/symbol must trace back to a
  source noun-phrase, prelude name, or explicit user instruction.

LAYER 3 — CROSS-SECTION LINKS (relationships that depend on definitions
from OTHER sections of the same methodology, or on temporal/causal
chains across sections):
  do NOT belong to this section's IR.
  They are the responsibility of a later merge/bridge phase that
  explicitly stitches sections together.

What this means for each role:
  - When GENERATING IR: do not write formula content that violates
    LAYER 1. Do not stretch LAYER 2 beyond what the source/prelude/
    user-hint actually justifies.
  - When EVALUATING IR (judging, critiquing, scoring): do not flag a
    claim as drift if it complies with these rules. A formula whose
    every term traces to a4v3+prelude+local-source is faithful, even
    if the source phrasing is informal.
  - When RENDERING IR back to natural language: paraphrase only what
    the IR claims. Do not invent additional NL claims that have no
    matching IR declaration.
  - When PROBING IR: only probe claims that the IR actually makes.
    Do not derive expected behaviors from cross-section reasoning.

═════════════════════════════════════════════════════════════════════════"""


def format_for_prompt() -> str:
    """Return the canonical PROVENANCE RULES block as a single string,
    ready to embed in any LLM prompt.
    """
    return _PROVENANCE_RULES_TEXT


def format_compact() -> str:
    """One-paragraph compact version, for prompts where space is tight."""
    return (
        "PROVENANCE RULES (HARD): IR formulas (constraint/fact/axiom/prop/"
        "theorem bodies) may contain ONLY content from a4v3 spec + prelude/"
        "overlay + this section's source text. IR ontology (sorts/entities/"
        "symbols) may additionally use methodology context, world-knowledge, "
        "or human hints — but every name must trace to source noun-phrase, "
        "prelude, or explicit instruction. Cross-section relationships "
        "(e.g. 'X defined elsewhere implies Y here') do NOT belong here — "
        "they go to a later merge/bridge phase. When generating IR: stay "
        "within these rules. When evaluating IR: do not flag claims that "
        "comply. When rendering IR to NL: paraphrase only what IR claims, "
        "do not invent extra claims."
    )


if __name__ == "__main__":
    print(format_for_prompt())
    print()
    print("=== COMPACT VERSION ===")
    print(format_compact())
