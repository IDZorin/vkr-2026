"""Strategy composition + amendment tools."""
from __future__ import annotations

import json
import re
from typing import Any

from ir_agent.env import ToolEnv
from ir_agent.helpers import _load_json, _read_text, _strip_code_fence
from ir_agent.parts_inventory import (
    compact_inventory_for_prompt,
    ensure_parts_inventory,
    promote_accepted_kdr_cards,
    write_inventory,
)
from ir_agent.prompts.strategy import (
    _AMEND_STRATEGY_SYSTEM,
    _COMPOSE_STRATEGY_SYSTEM,
)
from ir_agent.strategy_io import _latest_strategy_path


# ──────────────────────────────────────────────────────────────────────
# role_frame → strategy contract enforcement
#
# Three gates checked AFTER LLM produces strategy text:
#   (1) role_frame_to_strategy_drift — every structural element prescribed
#       by role_frame.drafter_directives (sort/entity/relation names,
#       ownership triples) must appear in strategy OR be explicitly
#       superseded with a reason.
#   (2) role_ownership_map_present — strategy MUST contain a
#       `### Role Ownership Map` subsection with one entry per
#       role_frame.participant.
#   (3) name_only_role_capture — for each role in role_frame.participants,
#       strategy must ground it via formula/bridge/waiver, not merely by
#       embedding the role's name in a compound symbol.
# All three gates return concrete errors so the agent can re-call
# compose_strategy with a known fix target.
# ──────────────────────────────────────────────────────────────────────

# Match `relation_name(arg1, arg2[, ...])` — captures relation + first arg
_REL_CALL_RE = re.compile(
    r"\b([a-z_][a-z0-9_]*)\s*\(\s*([A-Za-z_][\w]*)\s*,\s*([A-Za-z_][\w]*)",
    flags=re.IGNORECASE,
)
# Match `sort SortName` or `sort SortName extends Parent`
_SORT_DECL_RE = re.compile(
    r"\bsort\s+([A-Z][\w]*)(?:\s+extends\s+([A-Z][\w]*))?",
    flags=re.IGNORECASE,
)
# Match `entity EntityName : SortName`
_ENTITY_DECL_RE = re.compile(
    r"\bentity\s+([A-Z][\w]*)\s*:\s*([A-Z][\w]*)",
    flags=re.IGNORECASE,
)
# Marker for explicit override of a role_frame directive
_SUPERSEDED_RE = re.compile(
    r"superseded(?:\s+directive)?\s*:\s*([A-Za-z_][\w]*)\s*[—\-]\s*because\s+",
    flags=re.IGNORECASE,
)

# Backtick-fenced fragments. Inline (`x`) and fenced (```...```). Only the
# CONTENT of these spans is scanned for structural commitments — bare prose
# in drafter_directives is ignored to prevent English parentheticals like
# "actions (bake, give, eat)" from being mis-parsed as `actions(bake, give)`
# relation calls (a real false positive we observed on GSM problem_3).
_FENCED_CODE_BLOCK_RE = re.compile(
    r"```(?:[a-zA-Z0-9_+-]*)\n([\s\S]*?)\n?```",
    flags=re.MULTILINE,
)
_INLINE_BACKTICK_RE = re.compile(r"`([^`\n]+)`")


def _extract_code_fragments(text: str) -> list[str]:
    """Return the content of every fenced or inline backtick span in `text`.
    These are the ONLY spans treated as A4V3 syntax for commitment extraction.
    To commit role_frame to a relation/sort, directive authors must put it
    in backticks (e.g. `license_class_use_category(LicenseClass, LicenseUseCategory)`)."""
    fragments: list[str] = []
    for m in _FENCED_CODE_BLOCK_RE.finditer(text or ""):
        fragments.append(m.group(1))
    for m in _INLINE_BACKTICK_RE.finditer(text or ""):
        fragments.append(m.group(1))
    return fragments


def _extract_structural_commitments(rf: dict[str, Any]) -> dict[str, set[str]]:
    """From role_frame.json (specifically drafter_directives + the
    participant.proposed_modeling fields), extract the structural
    elements the strategy must honor. Returns dict with three sets:
      - 'sorts': sort names role_frame committed to
      - 'entities': entity names role_frame committed to
      - 'relations': relation names role_frame committed to
    """
    sorts: set[str] = set()
    entities: set[str] = set()
    relations: set[str] = set()

    haystacks: list[str] = []
    for d in rf.get("drafter_directives") or []:
        if isinstance(d, str):
            haystacks.append(d)
    for p in rf.get("participants") or []:
        if isinstance(p, dict):
            pm = p.get("proposed_modeling") or ""
            if pm:
                haystacks.append(pm)
    # Normalize entries — LLM sometimes writes "Brother : ProblemActor" or
    # "License extends Document" in proposed_new_sorts/entities instead of
    # just the identifier. Extract leading identifier only so the validator's
    # literal-match check works against strategy text which uses just the
    # identifier (e.g. "Brother (ProblemActor)" or "entity Brother : ...").
    _ID_RE = re.compile(r"^[A-Z][\w]*")
    ob = rf.get("ontology_budget") or {}
    for s in ob.get("proposed_new_sorts") or []:
        if isinstance(s, str):
            m = _ID_RE.match(s.strip())
            if m:
                sorts.add(m.group(0))
    for e in ob.get("proposed_new_entities") or []:
        if isinstance(e, str):
            m = _ID_RE.match(e.strip())
            if m:
                entities.add(m.group(0))

    for text in haystacks:
        # Only scan backtick-fenced fragments. Bare prose in directives is
        # natural language with potential parentheticals that look like
        # function calls; treating them as A4V3 syntax causes false-positive
        # "drift" errors (e.g. "actions (bake, give, eat)" → bogus
        # required relation `actions`).
        for fragment in _extract_code_fragments(text):
            for m in _SORT_DECL_RE.finditer(fragment):
                sorts.add(m.group(1))
                if m.group(2):
                    sorts.add(m.group(2))
            for m in _ENTITY_DECL_RE.finditer(fragment):
                entities.add(m.group(1))
                sorts.add(m.group(2))
            for m in _REL_CALL_RE.finditer(fragment):
                relations.add(m.group(1).lower())

    return {"sorts": sorts, "entities": entities, "relations": relations}


def _validate_strategy_against_role_frame(role_frame: dict[str, Any],
                                           strategy_text: str
                                           ) -> dict[str, Any]:
    """Run the 3 gates. Returns {} when all pass; otherwise a dict with
    `errors` list and `actionable_hint` string for the LLM to re-target."""
    errors: list[str] = []

    commitments = _extract_structural_commitments(role_frame)
    txt = strategy_text
    lower_txt = txt.lower()

    # Find what strategy explicitly supersedes — these are exempted
    # from the drift check.
    superseded_names = {m.group(1) for m in _SUPERSEDED_RE.finditer(txt)}
    superseded_lower = {s.lower() for s in superseded_names}

    # ── Gate 1: role_frame_to_strategy_drift ──────────────────────────
    missing: list[dict[str, str]] = []
    for sort_name in sorted(commitments["sorts"]):
        if not sort_name or len(sort_name) < 2:
            continue
        # Strategy mentions the sort? (boundary match)
        if re.search(rf"\b{re.escape(sort_name)}\b", txt):
            continue
        if sort_name.lower() in superseded_lower:
            continue
        missing.append({"kind": "sort", "name": sort_name})

    for entity_name in sorted(commitments["entities"]):
        if not entity_name or len(entity_name) < 2:
            continue
        if re.search(rf"\b{re.escape(entity_name)}\b", txt):
            continue
        if entity_name.lower() in superseded_lower:
            continue
        missing.append({"kind": "entity", "name": entity_name})

    for rel_name in sorted(commitments["relations"]):
        if not rel_name or len(rel_name) < 2:
            continue
        if rel_name in lower_txt:
            continue
        if rel_name in superseded_lower:
            continue
        missing.append({"kind": "relation", "name": rel_name})

    if missing:
        bulleted = "\n".join(
            f"  - {m['kind']}: `{m['name']}`" for m in missing[:15]
        )
        errors.append(
            f"role_frame_to_strategy_drift: {len(missing)} structural "
            f"element(s) from role_frame.drafter_directives / "
            f"ontology_budget were NOT carried into strategy AND not "
            f"explicitly superseded. Each missing element below must "
            f"either appear verbatim in the strategy text OR be "
            f"justified with a `Superseded directive: <name> — because "
            f"<reason>` line:\n{bulleted}"
        )

    # ── Gate 2: Role Ownership Map subsection present ─────────────────
    if not re.search(r"^###\s+Role\s+Ownership\s+Map\b", txt,
                      flags=re.MULTILINE | re.IGNORECASE):
        errors.append(
            "role_ownership_map_missing: section 3 (Relationships) MUST "
            "contain a `### Role Ownership Map` subsection. Without it "
            "the strategy doesn't pin down which carrier owns each role "
            "from role_frame.participants — this is exactly the gap "
            "that causes downstream judge dissent about 'over-asserted "
            "issuance program' (recipient + use categories all dumped on "
            "one carrier instead of split between event and class)."
        )
    else:
        # Each role from role_frame.participants must appear in the
        # subsection — match by source_phrase fragment.
        ownership_section = txt[
            re.search(r"^###\s+Role\s+Ownership\s+Map\b", txt,
                       flags=re.MULTILINE | re.IGNORECASE).end():
        ]
        # Cut at next ### or ## heading
        next_heading = re.search(r"^##?#?\s+\S", ownership_section,
                                  flags=re.MULTILINE)
        if next_heading:
            ownership_section = ownership_section[:next_heading.start()]
        unmapped: list[str] = []
        for p in role_frame.get("participants") or []:
            if not isinstance(p, dict):
                continue
            sp = (p.get("source_phrase") or "").strip()
            if not sp:
                continue
            # Match by 4+ char fragment to tolerate paraphrase
            fragment = sp[: max(8, len(sp) // 2)].lower()
            if fragment and fragment not in ownership_section.lower():
                # Try shorter fragment as last resort
                if sp.lower() not in ownership_section.lower():
                    unmapped.append(f"{p.get('role','?')}: \"{sp[:80]}\"")
        if unmapped:
            errors.append(
                "role_ownership_map_incomplete: the following roles "
                f"from role_frame.participants are NOT mapped in the "
                f"Role Ownership Map subsection:\n"
                + "\n".join(f"  - {u}" for u in unmapped[:10])
            )

    # ── Gate 3: name-only role capture ban ────────────────────────────
    # For each role with proposed_modeling that uses a non-prelude sort,
    # require the role's SOURCE PHRASE to appear in strategy context
    # accompanied by one of: `rel ` declaration, `bridge`, or `waiver`.
    # If the role's name only shows up inside a compound symbol name,
    # reject.
    name_only: list[str] = []
    for p in role_frame.get("participants") or []:
        if not isinstance(p, dict):
            continue
        sp = (p.get("source_phrase") or "").strip()
        pm = (p.get("proposed_modeling") or "").strip()
        if not sp:
            continue
        # Extract candidate sort names from proposed_modeling — Capitalized
        # words that look like type identifiers.
        sort_candidates = set(re.findall(r"\b[A-Z][A-Za-z0-9]+\b", pm))
        if not sort_candidates:
            continue
        # For each candidate sort, check whether strategy has any of:
        #  - a `rel <name>( ..., <Sort>, ...)` call referencing the sort
        #  - the word "bridge" within 200 chars of the sort name
        #  - the word "waiver" within 200 chars of the sort name
        # If none, AND the sort only appears inside compound names
        # (longer identifiers), flag as name-only.
        grounded = False
        for sort in sort_candidates:
            # Standalone whole-word reference (boundary)
            if re.search(rf"\brel\s+\w+\s*:\s*[^\n]*\b{re.escape(sort)}\b",
                          txt, flags=re.IGNORECASE):
                grounded = True
                break
            if re.search(rf"\b{re.escape(sort)}\b[^.\n]{{0,200}}\b(bridge|waiver)\b|"
                          rf"\b(bridge|waiver)\b[^.\n]{{0,200}}\b{re.escape(sort)}\b",
                          txt, flags=re.IGNORECASE):
                grounded = True
                break
            # Whole-word appearance in any line not inside a longer name
            for m in re.finditer(rf"\b{re.escape(sort)}\b", txt):
                # Check the immediately-following char — if it's a word char
                # the match is inside a larger identifier (false hit).
                end = m.end()
                if end < len(txt) and txt[end].isalnum():
                    continue
                # Whole-word standalone — count as grounded
                grounded = True
                break
            if grounded:
                break
        if not grounded:
            name_only.append(
                f"role={p.get('role','?')}: \"{sp[:60]}\" — sorts "
                f"{sorted(sort_candidates)[:3]} appear only as part of "
                f"compound names without standalone formula/bridge/waiver "
                f"reference"
            )
    if name_only:
        errors.append(
            "name_only_role_capture: the following role(s) from "
            "role_frame.participants are captured ONLY by being embedded "
            "in compound symbol names — not by an explicit relation, "
            "bridge reference, or waiver. Each role must have at least "
            "one of those three forms of grounding in strategy:\n"
            + "\n".join(f"  - {n}" for n in name_only[:8])
        )

    if not errors:
        return {}
    return {
        "errors": errors,
        "actionable_hint": (
            "Re-call compose_strategy. Address each error above by "
            "EITHER adding the missing structural element to strategy "
            "verbatim OR adding a `Superseded directive: <name> — "
            "because <reason>` line. For the Role Ownership Map, write "
            "one entry per role_frame.participants (see the prompt's "
            "Role Ownership Map example for format)."
        ),
    }


def _validate_strategy_against_parts_inventory(inventory: dict[str, Any],
                                               strategy_text: str
                                               ) -> dict[str, Any]:
    """Inventory contract gate.

    The strategy may supersede cards, but it cannot silently lose a
    required role/formula card. Unknown-symbol cards must be resolved by
    an explicit local declaration, bridge, or waiver plan.
    """
    if not inventory:
        return {}
    errors: list[str] = []
    txt = strategy_text
    lower = txt.lower()
    superseded = {
        m.group(1).lower()
        for m in re.finditer(
            r"superseded\s+part\s*:\s*([A-Za-z0-9_:-]+)\s*[—\-]\s*because\s+",
            txt,
            flags=re.IGNORECASE,
        )
    }

    ownership_section = ""
    m = re.search(r"^###\s+Role\s+Ownership\s+Map\b", txt,
                  flags=re.MULTILINE | re.IGNORECASE)
    if m:
        ownership_section = txt[m.end():]
        next_heading = re.search(r"^##?#?\s+\S", ownership_section,
                                  flags=re.MULTILINE)
        if next_heading:
            ownership_section = ownership_section[:next_heading.start()]
    ownership_lower = ownership_section.lower()

    missing_roles: list[str] = []
    unresolved_unknowns: list[str] = []
    missing_formula_parts: list[str] = []

    for card in inventory.get("cards") or []:
        if not card.get("required") or card.get("status") == "superseded":
            continue
        # Skip inferred-relation cards (claim_ledger default carrier_*/c{N}_role_*
        # names that may not match the active prelude vocabulary). They are
        # advisory commitments, not contract commitments. Coverage check does
        # the same filtering on its side.
        if card.get("relation_origin") == "inferred":
            continue
        cid = str(card.get("id") or "")
        if cid.lower() in superseded:
            continue
        rel = str(card.get("relation") or "")
        owner = str(card.get("owner") or "")
        target = str(card.get("target") or "")
        source_phrase = str(card.get("source_phrase") or "")
        ptype = card.get("part_type")

        if ptype == "role_link":
            # Required role cards must appear in the Role Ownership Map by
            # relation OR owner/target pair OR the source phrase fragment.
            phrase_fragment = source_phrase[: max(8, len(source_phrase) // 2)].lower()
            grounded = (
                (rel and rel.lower() in ownership_lower)
                or (owner and target and owner.lower() in ownership_lower
                    and target.lower() in ownership_lower)
                or (cid and cid.lower() in ownership_lower)
                or (phrase_fragment and phrase_fragment in ownership_lower)
            )
            if not grounded:
                missing_roles.append(
                    f"{cid}: relation={rel or '?'} source=\"{source_phrase[:70]}\""
                )

        if ptype == "formula_claim":
            grounded = (
                (rel and rel.lower() in lower)
                or (cid and cid.lower() in lower)
                or any(str(t).lower() in lower
                       for t in (card.get("coverage_tokens") or []))
            )
            if not grounded:
                missing_formula_parts.append(
                    f"{cid}: source=\"{source_phrase[:70]}\""
                )

        if (card.get("symbol_origin") in {"unknown", "excluded_from_prelude"}
                and _card_claims_external_symbol(card)):
            # The strategy must explicitly decide what to do with the
            # unknown symbol; merely mentioning it is not enough.
            anchors = [
                x.lower() for x in [cid, rel, owner, target] if x
            ]
            mentions_card = any(a in lower for a in anchors)
            has_resolution = False
            for anchor in anchors:
                pos = lower.find(anchor)
                if pos < 0:
                    continue
                window = lower[max(0, pos - 160): pos + len(anchor) + 240]
                if re.search(r"\b(local|declare|bridge|waiver|repair|resolved)\b",
                             window):
                    has_resolution = True
                    break
            if not mentions_card or not has_resolution:
                unresolved_unknowns.append(
                    f"{cid}: symbol_origin={card.get('symbol_origin')}; choose local declaration, bridge, repair, or waiver"
                )

    if missing_roles:
        errors.append(
            "parts_inventory_role_map_incomplete: required role cards are "
            "not represented in the Role Ownership Map:\n"
            + "\n".join(f"  - {x}" for x in missing_roles[:12])
        )
    if missing_formula_parts:
        errors.append(
            "parts_inventory_formula_parts_missing: required formula/source "
            "cards are not carried into strategy section 4:\n"
            + "\n".join(f"  - {x}" for x in missing_formula_parts[:12])
        )
    if unresolved_unknowns:
        errors.append(
            "parts_inventory_unknown_symbols_unresolved: resolver could not "
            "prove these symbols come from prelude/sibling/bridge/local "
            "source phrase (or found them in an explicit prelude exclusion "
            "list), and strategy did not explicitly choose local/bridge/"
            "repair/waiver resolution:\n"
            + "\n".join(f"  - {x}" for x in unresolved_unknowns[:12])
        )

    if not errors:
        return {}
    return {
        "errors": errors,
        "actionable_hint": (
            "Re-call compose_strategy. Add each missing card to the Role "
            "Ownership Map or section 4, or write `Superseded part: <id> - "
            "because <reason>`. For unknown symbols, explicitly choose "
            "local declaration, bridge, repair, or waiver."
        ),
    }


def _card_claims_external_symbol(card: dict[str, Any]) -> bool:
    text = " ".join([
        str(card.get("origin") or ""),
        str(card.get("notes") or ""),
        str(card.get("symbol_origin") or ""),
    ]).lower()
    return any(w in text for w in [
        "prelude", "reuse", "sibling", "bridge", "existing", "canonical",
    ])


def _kdr_requires_role_frame_reanalysis(latest_kdr: dict[str, Any] | None,
                                        role_frame: dict[str, Any]
                                        ) -> dict[str, Any] | None:
    """Detect when KDR is asking for ontology the role_frame never saw.

    Strategy amendment can refine a plan, but if judges/KDR propose a new
    carrier/process sort absent from role_frame, the scout layer was wrong.
    Route back to re_analyze_role_frame so the inventory/strategy/draft all
    inherit the same corrected parts instead of fighting each other.
    """
    if not latest_kdr or not isinstance(latest_kdr, dict):
        return None
    chunks: list[str] = []
    for item in latest_kdr.get("replace") or []:
        if isinstance(item, dict):
            chunks.extend([
                str(item.get("from") or ""),
                str(item.get("to") or ""),
                str(item.get("rationale") or ""),
            ])
    for item in latest_kdr.get("unresolved") or []:
        chunks.append(str(item))
    text = "\n".join(chunks)
    proposed_sorts = set(re.findall(r"\bsort\s+([A-Z][A-Za-z0-9_]*)\b", text))
    if not proposed_sorts:
        return None
    commitments = _extract_structural_commitments(role_frame)
    known_sorts = set(commitments.get("sorts") or set())
    missing = sorted(s for s in proposed_sorts if s not in known_sorts)
    if not missing:
        return None
    lower = text.lower()
    concept_gap_signal = any(sig in lower for sig in [
        "missing", "not capture", "not formal", "formaliz", "omits",
        "lacks", "does not model", "doesn't model", "basis", "process",
        "carrier", "concept",
    ])
    if not concept_gap_signal:
        return None
    return {
        "missing_sorts": missing,
        "reason": (
            "KDR proposes new ontology sorts absent from role_frame; "
            "this is a SCOUT/role_frame gap, not a local strategy edit."
        ),
    }


def tool_compose_strategy(env: ToolEnv) -> dict[str, Any]:
    """Consolidate user hints + role_frame + text-intent classification
    into strategy_v0.md."""
    if env.client is None:
        return {"error": "intra-tool LLM client not configured"}

    role_frame = _load_json(env.discovery_dir / "role_frame.json")
    classification = _load_json(env.discovery_dir / "text_intent_classification.json")
    claim_ledger = _load_json(env.discovery_dir / "claim_ledger.json")
    if not role_frame:
        return {"error": "role_frame.json missing — call analyze_role_frame() first"}
    if not classification:
        return {"error": "text_intent_classification.json missing — call classify_text_intent() first"}
    if not claim_ledger:
        return {"error": (
            "claim_ledger.json missing — call extract_claim_ledger() before "
            "compose_strategy. The ledger pins down each claim's "
            "event_status (actual / possible_or_authorized / etc.) so the "
            "strategy and downstream IR cannot promote possibilities into "
            "asserted facts."
        )}

    parts_inventory = ensure_parts_inventory(env)
    if not parts_inventory:
        return {"error": (
            "parts_inventory.json missing and could not be built; call "
            "extract_claim_ledger() again before compose_strategy."
        )}

    hints_content = ""
    candidates = [
        env.section_dir / "user_hints" / "active.yaml",
        env.agent_run_dir / "user_hints" / "active.yaml",
        env.corpus_paths.run_dir / "user_hints" / "active.yaml",
    ]
    found = [p for p in candidates if p.exists()]
    if found:
        hints_content = "\n\n".join(
            f"# from {p.name} ({p.parent.name})\n{p.read_text(encoding='utf-8')}"
            for p in found)
    else:
        hints_content = "(no hints set in any expected location)"

    source = _read_text(env.section_dir / "source.md")

    rf_compact = {
        "event": role_frame.get("event"),
        "modality": role_frame.get("modality"),
        "participants": role_frame.get("participants"),
        "ontology_budget": role_frame.get("ontology_budget"),
        "drafter_directives": role_frame.get("drafter_directives"),
    }
    cls_compact = {
        "clauses": classification.get("clauses"),
        "global_summary": classification.get("global_summary"),
        "policy_implication": classification.get("policy_implication"),
    }

    user = (
        f"## SECTION SOURCE\n\n{source}\n\n"
        f"## USER HINTS (raw)\n\n{hints_content}\n\n"
        f"## ROLE_FRAME (compact)\n\n```json\n"
        f"{json.dumps(rf_compact, indent=2, ensure_ascii=False)[:5000]}\n```\n\n"
        f"## TEXT-INTENT CLASSIFICATION (compact)\n\n```json\n"
        f"{json.dumps(cls_compact, indent=2, ensure_ascii=False)[:4000]}\n```\n\n"
        f"## CLAIM LEDGER (source-truth, ground for IR)\n\n```json\n"
        f"{json.dumps(claim_ledger, indent=2, ensure_ascii=False)[:5000]}\n```\n\n"
        f"## PARTS INVENTORY (durable lego contract)\n\n```json\n"
        f"{json.dumps(compact_inventory_for_prompt(parts_inventory), indent=2, ensure_ascii=False)[:7000]}\n```\n\n"
        f"## YOUR TASK\n\n"
        f"Write strategy_v0.md per the schema. This becomes the single "
        f"source of truth for the drafter. Be concise (each section ≤ 1500 "
        f"chars). Do not invent content; consolidate from upstream "
        f"artifacts. Do not contradict role_frame.modality.absorption_decision. "
        f"For each claim in the ledger with event_status="
        f"'possible_or_authorized' or 'obligated', section 4's A4V3 sketch "
        f"MUST use the carrier as a CLASS or PROGRAM when the source "
        f"describes a program/class rather than an actual occurrence. "
        f"One singleton entity per class/program PLUS role-wiring facts "
        f"is EXPECTED when role_frame/parts_inventory calls for it. "
        f"is EXPECTED — these wire the class structure, not assert occurrence. "
        f"FORBIDDEN: multiple per-occurrence entities (`entity Issuance1 : "
        f"...`, `entity Issuance2 : ...`) with facts asserting each happened."
    )
    # Output budget needs to cover: full 6-section strategy markdown +
    # mandatory Role Ownership Map subsection (one entry per role_frame
    # participant) + per-clause sketches + drift contract supersedes.
    # 4000 truncates on problems with >5 participants (observed: GSM
    # problem_3 with 8 participants, output cut at section 2 entity #7).
    _client, _xb, _mt = env.strategic_or_main(8000)
    try:
        result = _client.complete(
            [],
            raw_messages=[{"role": "system", "content": _COMPOSE_STRATEGY_SYSTEM},
                          {"role": "user", "content": user}],
            max_tokens=_mt,
            extra_body=_xb,
            seed=env.seed,
        )
    except Exception as exc:
        return {"error": f"{type(exc).__name__}: {exc}"}

    md = result.text or ""
    md = _strip_code_fence(md.strip())
    if not md.strip():
        return {"error": "compose_strategy LLM returned empty document"}

    # HARD GATE: strategy MUST have all 6 `## N.` section headings.
    # Without them the document is just an IR sketch / template echo,
    # losing the rich entity descriptions and per-clause guidance the
    # drafter needs. Previously this was only a warning, leading to
    # downstream cascading failures (xhigh run #6 produced a 9-line
    # permission-only strategy_v0 → drafter improvised → rounds 1-3
    # all partially_corresponds). DO NOT save the malformed file —
    # force the agent to retry with explicit format hint.
    section_headings = re.findall(r"^##\s+\d+\.", md, flags=re.MULTILINE)
    if len(section_headings) < 5:
        return {
            "error": "strategy_format_violation: output has only "
                     f"{len(section_headings)}/6 required `## N.` section "
                     "headings. compose_strategy must produce a structured "
                     "markdown document, NOT an IR sketch or permission "
                     "template.",
            "expected_sections": [
                "## 1. User hints (verbatim)",
                "## 2. Entities and their methodology role",
                "## 3. Relationships",
                "## 4. Per-clause translation strategy",
                "## 5. Critic feedback",
                "## 6. Open questions and uncertainty",
            ],
            "actual_chars": len(md),
            "actual_excerpt": md[:300],
            "instruction": (
                "Re-call compose_strategy. The output MUST be a markdown "
                "document with ALL six `## N.` headings (1-6) populated "
                "from the upstream artifacts (role_frame, classification, "
                "claim_ledger, user_hints). Do NOT just echo the permission "
                "template from role_frame's drafter_directives — section 4 "
                "should DESCRIBE the per-clause approach including the "
                "permission, but sections 1-3 and 5-6 must also be filled. "
                "Each section ≤ 1500 chars; bullet form preferred."
            ),
        }

    # role_frame → strategy contract gates: drift, ownership map,
    # name-only ban. See _validate_strategy_against_role_frame.
    promoted_inventory = promote_accepted_kdr_cards(parts_inventory, md)
    if promoted_inventory != parts_inventory:
        parts_inventory = promoted_inventory
        write_inventory(env, parts_inventory)

    contract = _validate_strategy_against_role_frame(role_frame, md)
    if contract:
        return {
            "error": "role_frame_strategy_contract_violation",
            "violations": contract["errors"],
            "actionable_hint": contract["actionable_hint"],
            "strategy_excerpt": md[:600],
            "instruction": (
                "Re-call compose_strategy with strategy text that "
                "honors role_frame's structural commitments. Each "
                "violation above identifies a specific fix target. "
                "Strategy was NOT saved — fix and retry."
            ),
        }

    parts_contract = _validate_strategy_against_parts_inventory(parts_inventory, md)
    if parts_contract:
        return {
            "error": "parts_inventory_strategy_contract_violation",
            "violations": parts_contract["errors"],
            "actionable_hint": parts_contract["actionable_hint"],
            "strategy_excerpt": md[:600],
            "instruction": (
                "Re-call compose_strategy. Strategy was NOT saved because "
                "required parts_inventory cards would be lost or unresolved."
            ),
        }

    out_path = env.discovery_dir / "strategy_v0.md"
    out_path.write_text(md, encoding="utf-8")

    return {
        "version": 0,
        "path": str(out_path.relative_to(env.agent_run_dir)),
        "chars": len(md),
        "sections_detected": len(section_headings),
        "instruction": (
            "strategy_v0.md saved. The submit_ir_for_lint gate is now OPEN. "
            "The drafter MUST follow strategy_v0 — re-read it via "
            "read_my_notes('strategy_v0') at any time. If a VERIFY round "
            "fails and local IR fixes don't resolve dissent, call "
            "amend_strategy() — it creates strategy_v1.md and the drafter "
            "switches to the new version."
        ),
    }


def tool_amend_strategy(env: ToolEnv) -> dict[str, Any]:
    """Amend the strategy after a failed VERIFY round."""
    if env.client is None:
        return {"error": "intra-tool LLM client not configured"}

    prev_path = _latest_strategy_path(env.discovery_dir)
    if prev_path is None:
        return {"error": "no prior strategy_v*.md — call compose_strategy() first"}

    if not env.verify_history:
        check_paths = sorted(env.agent_run_dir.glob(
            "ir_vs_strategy_check_v*.json"))
        n_drift_checks = sum(
            1 for p in check_paths
            if (_load_json(p) or {}).get("n_missing_strong", 0) > 0)
        if n_drift_checks < 2:
            return {
                "error": (
                    "amend_strategy is normally only allowed after at least "
                    "one run_package_checks. Pre-verify amend is allowed "
                    "ONLY when persistent check_ir_vs_strategy drift is "
                    f"detected (currently {n_drift_checks} of 2 required "
                    "drift-checks). Re-submit_ir_for_lint with the missing "
                    "items first, then re-run check_ir_vs_strategy. If "
                    "drift persists after 2 checks, this gate opens."
                ),
                "n_drift_checks_so_far": n_drift_checks,
            }

    prev_strategy = prev_path.read_text(encoding="utf-8")
    prev_version = int(re.match(r"strategy_v(\d+)\.md$", prev_path.name).group(1))
    next_version = prev_version + 1

    last_verify = env.verify_history[-1] if env.verify_history else {
        "round": 0,
        "worst_verdict": None,
        "distribution": {},
        "judge_dissent": [],
        "_note": "pre-verify amend triggered by persistent check_ir_vs_strategy drift",
    }
    current_ir = _read_text(env.agent_run_dir / "main_ir.a4v3", max_chars=6000)
    role_frame = _load_json(env.discovery_dir / "role_frame.json") or {}
    claim_ledger = _load_json(env.discovery_dir / "claim_ledger.json") or {}
    parts_inventory = ensure_parts_inventory(env)
    kdr_files = sorted(env.agent_run_dir.glob("keep_drop_replace_v*.json"))
    latest_kdr = _load_json(kdr_files[-1]) if kdr_files else None
    role_frame_gap = _kdr_requires_role_frame_reanalysis(latest_kdr, role_frame)
    if role_frame_gap:
        return {
            "error": "role_frame_reanalysis_required",
            "missing_sorts": role_frame_gap["missing_sorts"],
            "reason": role_frame_gap["reason"],
            "instruction": (
                "Call re_analyze_role_frame() before amend_strategy. The "
                "latest KDR is proposing new ontology/carrier sorts that "
                "role_frame never captured, so amending strategy would build "
                "on an upstream inventory gap. After re_analyze_role_frame "
                "updates roles/carriers, call compose_strategy/amend_strategy "
                "again and draft from the corrected parts."
            ),
        }

    user = (
        f"## PREVIOUS STRATEGY (strategy_v{prev_version}.md)\n\n"
        f"```markdown\n{prev_strategy}\n```\n\n"
        f"## CURRENT IR (after the failed verify)\n\n"
        f"```\n{current_ir}\n```\n\n"
        f"## LAST VERIFY RESULT (compact)\n\n"
        f"```json\n{json.dumps(last_verify, indent=2, ensure_ascii=False)[:6000]}\n```\n\n"
        + (
            f"## KEEP/DROP/REPLACE MEMO (auto-generated from latest verify)\n\n"
            f"```json\n{json.dumps(latest_kdr, indent=2, ensure_ascii=False)[:4000]}\n```\n\n"
            f"**Honor this memo**: items in `keep` MUST stay in next "
            f"strategy/IR; items in `drop` MUST be removed; items in "
            f"`replace.from` get replaced by `replace.to`.\n\n"
            if latest_kdr else ""
        )
        + (
            f"## CLAIM LEDGER (source-truth)\n\n```json\n"
            f"{json.dumps(claim_ledger, indent=2, ensure_ascii=False)[:3000]}\n```\n\n"
            f"For each claim with event_status='possible_or_authorized' or "
            f"'obligated', the new strategy section 4 MUST keep carrier as "
            f"a CLASS or PROGRAM when the source describes a program/class "
            f"rather than an actual occurrence. Role-wiring facts are "
            f"EXPECTED when role_frame/parts_inventory calls for them. "
            f"FORBIDDEN: multiple per-"
            f"occurrence entities asserting specific events happened.\n\n"
            if claim_ledger else ""
        )
        + (
            f"## PARTS INVENTORY (durable lego contract)\n\n```json\n"
            f"{json.dumps(compact_inventory_for_prompt(parts_inventory), indent=2, ensure_ascii=False)[:7000]}\n"
            f"```\n\n"
            f"Carry forward every required card or write `Superseded part: "
            f"<id> - because <reason>`. KDR additions accepted into "
            f"strategy should become required inventory cards in the next "
            f"IR/check cycle.\n\n"
            if parts_inventory else ""
        )
        + f"## ROLE_FRAME modality field (must remain consistent unless you "
        f"document why it was wrong)\n\n"
        f"```json\n{json.dumps(role_frame.get('modality') or {}, indent=2, ensure_ascii=False)}\n```\n\n"
        f"## YOUR TASK\n\n"
        f"Write strategy_v{next_version}.md per the schema. **Sculptor "
        f"model**: carry forward sections 1-3 + 6 from previous strategy "
        f"unchanged UNLESS the KDR memo's `replace` items demand a change "
        f"there. ONLY sections 4 (clause sketch — apply replace items) "
        f"and 5 (critic feedback — populate from verify) get rewritten."
    )
    try:
        result = env.client.complete(
            [],
            raw_messages=[{"role": "system", "content": _AMEND_STRATEGY_SYSTEM},
                          {"role": "user", "content": user}],
            max_tokens=8000,
            extra_body=env.extra_body,
            seed=env.seed,
        )
    except Exception as exc:
        return {"error": f"{type(exc).__name__}: {exc}"}

    md = _strip_code_fence((result.text or "").strip())
    if not md.strip():
        return {"error": "amend_strategy LLM returned empty document"}

    # HARD GATE (mirror of compose_strategy): amended strategy MUST keep
    # the 6-section structure. Otherwise downstream drafter loses entity/
    # relationship guidance.
    section_headings = re.findall(r"^##\s+\d+\.", md, flags=re.MULTILINE)
    if len(section_headings) < 5:
        return {
            "error": "strategy_format_violation: amended output has only "
                     f"{len(section_headings)}/6 required `## N.` section "
                     "headings. Strategy MUST retain all six sections "
                     "(carry forward unchanged from previous version when "
                     "no amendment needed); do NOT collapse to an IR sketch.",
            "expected_sections": [
                "## 1. User hints", "## 2. Entities and methodology role",
                "## 3. Relationships", "## 4. Per-clause translation strategy",
                "## 5. Critic feedback", "## 6. Open questions",
            ],
            "actual_chars": len(md),
            "actual_excerpt": md[:300],
            "instruction": (
                f"Re-call amend_strategy. Carry forward sections 1, 2, 3, 6 "
                f"VERBATIM from strategy_v{prev_version}.md (already provided "
                f"in the prompt). Rewrite ONLY sections 4 (per-clause sketch "
                f"applying KDR replace items) and 5 (critic feedback from "
                f"verify history). Output must contain `## 1.` through "
                f"`## 6.` markers verbatim."
            ),
        }

    diff_chars = sum(1 for a, b in zip(md, prev_strategy) if a != b) + abs(
        len(md) - len(prev_strategy))
    if diff_chars < 200:
        return {
            "error": (
                f"amend_strategy_too_cosmetic: new draft for "
                f"strategy_v{next_version}.md differs from v{prev_version} by "
                f"only {diff_chars} chars (< 200). Cosmetic re-wording will "
                f"not move judges. Either produce a substantively different "
                f"approach, or call re_analyze_role_frame() to overwrite the "
                f"role_frame's family choice (which amend cannot change)."
            ),
            "diff_chars": diff_chars,
        }

    def _section4_family(text: str) -> str:
        m = re.search(r"^##\s+4\.[^\n]*\n(.*?)(?=^##\s+\d+\.|\Z)",
                      text, flags=re.MULTILINE | re.DOTALL)
        if not m:
            return ""
        s4 = m.group(1)
        fm = re.search(r"chosen family[^\n]*?(`?)([A-Za-z_]+)\1",
                       s4, flags=re.IGNORECASE)
        return fm.group(2) if fm else ""

    prev_fam_in_strategy = _section4_family(prev_strategy)
    new_fam_in_strategy = _section4_family(md)
    family_unchanged = (prev_fam_in_strategy and new_fam_in_strategy
                        and prev_fam_in_strategy == new_fam_in_strategy)
    if family_unchanged:
        env.amends_within_same_family += 1
    else:
        env.amends_within_same_family = 0

    promoted_inventory = promote_accepted_kdr_cards(parts_inventory, md)
    if promoted_inventory != parts_inventory:
        parts_inventory = promoted_inventory
        write_inventory(env, parts_inventory)

    parts_contract = _validate_strategy_against_parts_inventory(parts_inventory, md)
    if parts_contract:
        return {
            "error": "parts_inventory_strategy_contract_violation",
            "violations": parts_contract["errors"],
            "actionable_hint": parts_contract["actionable_hint"],
            "strategy_excerpt": md[:600],
            "instruction": (
                "Re-call amend_strategy. Amended strategy was NOT saved "
                "because required parts_inventory cards would be lost or "
                "unresolved."
            ),
        }

    out_path = env.discovery_dir / f"strategy_v{next_version}.md"
    out_path.write_text(md, encoding="utf-8")

    family_hint = None
    if family_unchanged and env.amends_within_same_family >= 2:
        family_hint = (
            f"family_stuck: this is amendment #{env.amends_within_same_family} "
            f"keeping family='{new_fam_in_strategy}'. If judges continue to "
            f"dissent on family-level grounds (e.g. 'modal mismatch', "
            f"'over-asserts existence'), call re_analyze_role_frame() to "
            f"force a family override — amend_strategy alone cannot change "
            f"family because role_frame.modality is its source of truth."
        )

    return {
        "prev_version": prev_version,
        "new_version": next_version,
        "path": str(out_path.relative_to(env.agent_run_dir)),
        "chars": len(md),
        "diff_chars": diff_chars,
        "family_in_strategy": new_fam_in_strategy,
        "amends_within_same_family": env.amends_within_same_family,
        "family_hint": family_hint,
        "instruction": (
            f"strategy_v{next_version}.md saved. The drafter now reads this "
            f"version (latest one wins). Re-submit IR via submit_ir_for_lint "
            f"following the new strategy. If you continue to fail after 2-3 "
            f"amendments without convergence, finalize as failed_after_meta."
        ),
    }
