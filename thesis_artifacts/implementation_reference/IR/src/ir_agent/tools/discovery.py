"""Discovery / retrieval tools: read corpus, search, schema lookup, curator."""
from __future__ import annotations

import json
import pathlib
import re
import sys
from typing import Any

from ir_agent.config import ROOT, SRC
from ir_agent.env import ToolEnv
from ir_agent.helpers import _entry_dir, _read_text, _strip_code_fence, _truncate
from ir_agent.prompts.curator import _CURATOR_SYSTEM


def _authoritative_status(section_dir: pathlib.Path) -> dict[str, Any]:
    """Tell agent how trustworthy this section's IR is.

    - 'manual_gold': main_ir.a4v3 exists at section level AND no agent_run mark
    - 'agent_accept_candidate': there's at least one agent_run with that
      decision in agent_triage.json
    - 'agent_accept_with_dissent': accept_with_dissent decision
    - 'partial_or_unverified': only needs_human_review or unset runs
    - 'unknown': no signals
    """
    main_ir = section_dir / "main_ir.a4v3"
    if not main_ir.exists() or main_ir.stat().st_size == 0:
        return {"status": "unknown", "reason": "main_ir.a4v3 missing/empty"}

    accept = []
    accept_with_dissent = []
    for run_dir in section_dir.glob("agent_run_*"):
        triage = run_dir / "agent_triage.json"
        if not triage.exists():
            continue
        try:
            t = json.loads(triage.read_text(encoding="utf-8"))
            decision = t.get("decision")
            if decision == "agent_accept_candidate":
                accept.append(run_dir.name)
            elif decision == "agent_accept_candidate_with_dissent":
                accept_with_dissent.append(run_dir.name)
        except Exception:
            pass

    if accept:
        return {"status": "agent_accept_candidate",
                "evidence": f"{len(accept)} agent_run(s) accepted",
                "use_with_caution": False}
    if accept_with_dissent:
        return {"status": "agent_accept_candidate_with_dissent",
                "evidence": f"{len(accept_with_dissent)} agent_run(s) accept_with_dissent",
                "use_with_caution": False}
    if main_ir.stat().st_size > 500:
        return {"status": "manual_gold",
                "evidence": f"section-level main_ir.a4v3 ({main_ir.stat().st_size} bytes)",
                "use_with_caution": False,
                "note": "Likely human-curated reference. Patterns here are authoritative for similar source phrases."}
    return {"status": "partial_or_unverified",
            "evidence": "no accepted agent run, small main_ir",
            "use_with_caution": True}


def tool_read_section(env: ToolEnv, *, section_id: str,
                      include: list[str] | None = None) -> dict[str, Any]:
    include = include or ["source"]
    d = _entry_dir(section_id,
                    sections_root=env.corpus_paths.sections_root,
                    definitions_root=env.corpus_paths.definitions_root)
    if d is None:
        return {"error": f"section not found: {section_id}",
                "hint": "use list_sections to see available IDs"}
    # Path display: prefer relative-to-corpus-run-dir so corpora that
    # live outside this repo's root still render cleanly. Falls back to
    # repo-relative, then absolute, depending on which works.
    try:
        path_display = str(d.relative_to(env.corpus_paths.run_dir))
    except ValueError:
        try:
            path_display = str(d.relative_to(ROOT))
        except ValueError:
            path_display = str(d)
    out: dict[str, Any] = {"section_id": section_id, "path": path_display}

    is_own = (section_id == env.original_entry_id)
    safe_for_own = {"source", "normalized"}
    file_map = {"source": "source.md", "normalized": "normalized.md",
                "ir": "main_ir.a4v3", "provenance": "provenance.yaml",
                "notes": "translator_notes.md",
                "waivers": "waiver_token_absorption_v1.json"}
    # EXPERIMENTAL escape hatch: --allow-own-canonical-ir bypasses
    # anti-leak for own canonical artifacts. Used ONLY for research
    # experiments to measure whether the agent literal-copies the gold
    # IR vs. abstracts a pattern. NEVER set in production runs.
    allow_own = bool(getattr(env, "allow_own_canonical_ir", False))

    blocked: list[str] = []
    for key in include:
        fname = file_map.get(key)
        if not fname:
            out[key] = {"error": f"unknown include key: {key}"}
            continue
        if is_own and key not in safe_for_own and not allow_own:
            blocked.append(key)
            out[key] = {"error": "anti-leak: cannot read own section's "
                                  f"{key!r} (would copy canonical / prior agent "
                                  "output). Allowed for own section: source, "
                                  "normalized."}
            continue
        text = _read_text(d / fname, max_chars=12000)
        if is_own and key not in safe_for_own and allow_own:
            # Tag with explicit research-mode warning so we can find the
            # access in the transcript and so the LLM sees it's a leak.
            out[key] = (
                "**EXPERIMENTAL_OWN_CANONICAL_LEAK**: this is your OWN "
                "section's canonical artifact, normally blocked by "
                "anti-leak. The flag --allow-own-canonical-ir was set. "
                "Use ONLY to abstract patterns; DO NOT copy verbatim "
                "(your IR will be diff'd against this canonical and "
                "literal-copying invalidates the experiment).\n\n"
                + (text or "[file missing or empty]")
            )
        else:
            out[key] = text or "[file missing or empty]"

    if not is_own and ("ir" in include or "provenance" in include):
        out["authoritative_status"] = _authoritative_status(d)
    if blocked:
        out["_anti_leak_blocked"] = blocked
    return out


def tool_list_sections(env: ToolEnv) -> dict[str, Any]:
    sroot = env.corpus_paths.sections_root
    droot = env.corpus_paths.definitions_root
    sections = sorted(p.name for p in sroot.iterdir()
                      if p.is_dir() and (p / "source.md").exists()) if sroot and sroot.exists() else []
    definitions = sorted(p.name for p in droot.iterdir() if p.is_dir()) \
        if droot and droot.exists() else []
    return {
        "sections": sections,
        "definitions": definitions,
        "translated_sections": sorted([s for s in sections
                                        if (sroot / s / "main_ir.a4v3").exists()
                                        and (sroot / s / "main_ir.a4v3").stat().st_size > 0]),
        "current_section": env.original_entry_id,
    }


def _scope_paths(env: ToolEnv, scope: str) -> list[pathlib.Path]:
    """Per-corpus scope expansion. Reads paths from env.corpus_paths so
    the agent stays corpus-agnostic — no hardcoded `dz` anywhere."""
    cp = env.corpus_paths
    if scope == "sections" and cp.sections_root and cp.sections_root.exists():
        return [d / fname for d in sorted(cp.sections_root.iterdir()) if d.is_dir()
                for fname in ["source.md", "main_ir.a4v3", "provenance.yaml",
                              "translator_notes.md", "repair.a4v3"]
                if (d / fname).exists()]
    if scope == "definitions" and cp.definitions_root and cp.definitions_root.exists():
        return [d / fname for d in sorted(cp.definitions_root.iterdir()) if d.is_dir()
                for fname in ["source.md", "main_ir.a4v3", "provenance.yaml",
                              "translator_notes.md"]
                if (d / fname).exists()]
    if scope == "bridge" and cp.bridge_dir and cp.bridge_dir.exists():
        return [cp.bridge_dir / fname
                for fname in ["main_bridge.a4v3", "provenance.yaml", "translator_notes.md"]
                if (cp.bridge_dir / fname).exists()]
    if scope == "policy":
        candidates: list[pathlib.Path] = [cp.run_dir / "manual_gold_process_v1.md"]
        if cp.prelude_dir and cp.prelude_dir.exists():
            # Glob the full prelude stack: minimal (base ontology) +
            # domain (methodology-family layers). Hard-coded filenames
            # would miss new prelude files added per corpus.
            candidates.extend(sorted(cp.prelude_dir.glob("minimal_prelude_*.md")))
            candidates.extend(sorted(cp.prelude_dir.glob("domain_prelude_*.md")))
        return [p for p in candidates if p.exists()]
    if scope == "appendix" and cp.appendix_root and cp.appendix_root.exists():
        return [d / fname for d in sorted(cp.appendix_root.iterdir()) if d.is_dir()
                for fname in ["source.md", "main_ir.a4v3", "provenance.yaml",
                              "translator_notes.md"]
                if (d / fname).exists()]
    if scope == "user_hints":
        out: list[pathlib.Path] = []
        for p in [cp.run_dir / "user_hints" / "active.yaml",
                  cp.run_dir / "user_hints" / "archive.yaml"]:
            if p.exists():
                out.append(p)
        if cp.sections_root and cp.sections_root.exists():
            out.extend(d / "user_hints" / "active.yaml"
                       for d in sorted(cp.sections_root.iterdir())
                       if d.is_dir() and (d / "user_hints" / "active.yaml").exists())
        if cp.definitions_root and cp.definitions_root.exists():
            out.extend(d / "user_hints" / "active.yaml"
                       for d in sorted(cp.definitions_root.iterdir())
                       if d.is_dir() and (d / "user_hints" / "active.yaml").exists())
        return out
    return []


DEFAULT_SEARCH_SCOPES = ["sections", "definitions", "bridge", "policy"]


def tool_search_corpus(env: ToolEnv, *, query: str,
                       max_matches: int = 10,
                       scopes: list[str] | None = None) -> dict[str, Any]:
    """Grep across seed methodology corpus (sections+definitions+bridge+policy by default).
    Failed agent_run_* are NOT searched here — use search_failures for that."""
    if not query.strip():
        return {"error": "empty query"}
    use_scopes = scopes if scopes is not None else DEFAULT_SEARCH_SCOPES
    paths_to_search: list[pathlib.Path] = []
    used_scopes: list[str] = []
    for s in use_scopes:
        try:
            scope_paths = _scope_paths(env, s)
        except Exception:
            scope_paths = []
        if scope_paths:
            paths_to_search.extend(scope_paths)
            used_scopes.append(s)

    pat = re.compile(re.escape(query), re.IGNORECASE)
    results: list[dict[str, Any]] = []
    blocked_own_section_paths = 0
    for p in paths_to_search:
        if len(results) >= max_matches:
            break
        if p.parent.name == env.original_entry_id and p.name != "source.md" \
                and p.name != "normalized.md":
            blocked_own_section_paths += 1
            continue
        try:
            lines = p.read_text(encoding="utf-8", errors="replace").splitlines()
        except Exception:
            continue
        try:
            rel = str(p.relative_to(env.corpus_paths.run_dir)).replace("\\", "/")
        except ValueError:
            try:
                rel = str(p.relative_to(ROOT)).replace("\\", "/")
            except ValueError:
                rel = str(p)
        for i, line in enumerate(lines, start=1):
            if pat.search(line):
                results.append({
                    "scope_path": rel,
                    "section": p.parent.name,
                    "file": p.name,
                    "line": i,
                    "context": line.strip()[:280],
                })
                if len(results) >= max_matches:
                    break
    out = {"query": query, "match_count": len(results),
           "scopes_searched": used_scopes, "matches": results,
           "truncated": len(results) >= max_matches}
    if blocked_own_section_paths:
        out["_anti_leak_blocked_own_section_files"] = blocked_own_section_paths
    return out


def _grep_catalog(catalog_path: pathlib.Path, query: str,
                  max_matches: int = 8,
                  exclude_section_id: str | None = None) -> dict[str, Any]:
    """Grep entries in a markdown catalog. Each entry is delimited by
    `## section_X / agent_run_v2_*` headers. Returns full entries that
    contain a match."""
    if not catalog_path.exists():
        return {"query": query, "match_count": 0,
                "matches": [],
                "note": f"catalog {catalog_path.name} does not exist yet — "
                        f"no past runs of this kind"}
    text = catalog_path.read_text(encoding="utf-8", errors="replace")
    entries = re.split(r"(?m)^## ", text)
    if entries and not entries[0].strip().startswith("section_") \
            and not entries[0].strip().startswith("definitions/"):
        entries = entries[1:]
    pat = re.compile(re.escape(query), re.IGNORECASE)
    results = []
    blocked_own = 0
    for entry in entries:
        if exclude_section_id:
            first_line = entry.split("\n", 1)[0]
            if first_line.startswith(exclude_section_id + " "):
                blocked_own += 1
                continue
        if pat.search(entry):
            snippet = "## " + entry.strip()
            if len(snippet) > 4000:
                snippet = snippet[:4000] + "\n[entry truncated]"
            results.append(snippet)
            if len(results) >= max_matches:
                break
    out = {"query": query, "match_count": len(results),
           "catalog": catalog_path.name,
           "matches": results,
           "truncated": len(results) >= max_matches}
    if blocked_own:
        out["_anti_leak_skipped_own_section_entries"] = blocked_own
    return out


def tool_search_successes(env: ToolEnv, *, query: str,
                          max_matches: int = 5) -> dict[str, Any]:
    cat = env.corpus_paths.success_catalog_path
    if cat is None:
        return {"query": query, "match_count": 0, "matches": [],
                "note": "no prelude_dir in corpus_profile — success catalog disabled"}
    return _grep_catalog(cat, query, max_matches=max_matches,
                         exclude_section_id=env.original_entry_id)


def tool_search_failures(env: ToolEnv, *, query: str,
                         max_matches: int = 5) -> dict[str, Any]:
    cat = env.corpus_paths.failure_catalog_path
    if cat is None:
        return {"query": query, "match_count": 0, "matches": [],
                "note": "no prelude_dir in corpus_profile — failure catalog disabled"}
    return _grep_catalog(cat, query, max_matches=max_matches,
                         exclude_section_id=env.original_entry_id)


def tool_semantic_search(env: ToolEnv, *, query: str, top_k: int = 5,
                          kinds: list[str] | None = None,
                          exclude_current_section: bool = True
                          ) -> dict[str, Any]:
    """Semantic (embedding-based) search over the seed methodology corpus index. Returns
    top-K most semantically similar chunks (sections / IRs / provenance
    claims / translator notes / policy)."""
    sys.path.insert(0, str(SRC))
    try:
        import embedding_index_v1
        results = embedding_index_v1.semantic_search(
            query, top_k=top_k, kinds=kinds,
            exclude_section=env.original_entry_id if exclude_current_section else None,
            corpus_run_dir=env.corpus_paths.run_dir,
        )
    except Exception as exc:
        return {"error": f"{type(exc).__name__}: {exc}",
                "hint": (f"embedding index may not be built for this corpus — "
                         f"run 'python IR/src/embedding_index_v1.py build "
                         f"--corpus-run-dir {env.corpus_paths.run_dir}' first")}
    return {"query": query, "top_k": top_k,
            "kinds_filter": kinds,
            "exclude_section": env.original_entry_id if exclude_current_section else None,
            "corpus_run_dir": str(env.corpus_paths.run_dir),
            "matches": results}


def tool_curate_starter_pack(env: ToolEnv, *,
                              focus_query: str | None = None
                              ) -> dict[str, Any]:
    """Run a retrieval sub-agent that curates a starter pack of best
    precedents for the current section."""
    if env.client is None:
        return {"error": "intra-tool LLM client not configured"}
    source = _read_text(env.section_dir / "source.md")
    if not source.strip():
        return {"error": "source.md missing"}

    sys.path.insert(0, str(SRC))
    try:
        import embedding_index_v1
    except Exception as exc:
        return {"error": f"embedding_index_v1 unavailable: {exc}"}

    query_for_semantic = focus_query or source[:1000]
    crd = env.corpus_paths.run_dir
    candidates: dict[str, Any] = {
        "by_full_source": embedding_index_v1.semantic_search(
            query_for_semantic, top_k=8,
            exclude_section=env.original_entry_id,
            corpus_run_dir=crd),
        "by_ir_pattern": embedding_index_v1.semantic_search(
            f"A4V3 IR for: {source[:500]}", top_k=5,
            kinds=["main_ir"], exclude_section=env.original_entry_id,
            corpus_run_dir=crd),
        "by_provenance_intent": embedding_index_v1.semantic_search(
            f"provenance claim for: {source[:500]}", top_k=5,
            kinds=["provenance_claim"], exclude_section=env.original_entry_id,
            corpus_run_dir=crd),
        "by_translator_notes": embedding_index_v1.semantic_search(
            f"translator notes about: {source[:500]}", top_k=4,
            kinds=["translator_notes"], exclude_section=env.original_entry_id,
            corpus_run_dir=crd),
    }

    user = (
        f"## SECTION SOURCE\n\n{source}\n\n"
        f"## RAW SEARCH RESULTS (multi-angle)\n\n"
        f"```json\n{json.dumps(candidates, indent=2, ensure_ascii=False)[:14000]}\n```\n\n"
        f"Curate the starter pack per the schema."
    )
    try:
        result = env.client.complete(
            [], raw_messages=[
                {"role": "system", "content": _CURATOR_SYSTEM},
                {"role": "user", "content": user},
            ],
            max_tokens=4096, extra_body=env.extra_body, seed=env.seed,
        )
    except Exception as exc:
        return {"error": f"{type(exc).__name__}: {exc}",
                "raw_candidates": candidates}
    raw = _strip_code_fence(result.text or "")
    try:
        pack = json.loads(raw)
    except Exception as exc:
        return {"error": f"curator returned non-JSON: {exc}",
                "raw_excerpt": raw[:600],
                "raw_candidates": candidates}

    out_path = env.discovery_dir / "curated_starter_pack.json"
    out_path.write_text(json.dumps(pack, indent=2, ensure_ascii=False) + "\n",
                        encoding="utf-8")
    pack["_persisted_to"] = str(out_path.relative_to(env.agent_run_dir))
    return pack


def tool_get_a4v3_family(env: ToolEnv, *, family_name: str) -> dict[str, Any]:
    """Extract schema lines mentioning a specific family (DeonticDecl, etc.)."""
    if env.corpus_paths.prelude_dir is None:
        return {"error": "no prelude_dir in corpus_profile — schema lookup disabled"}
    schema_path = env.corpus_paths.prelude_dir / "a4v3_full (50).md"
    if not schema_path.exists():
        return {"error": f"schema file missing at {schema_path}"}
    text = schema_path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    pat = re.compile(re.escape(family_name), re.IGNORECASE)
    relevant_blocks: list[str] = []
    for i, line in enumerate(lines):
        if pat.search(line):
            start = max(0, i - 1)
            end = min(len(lines), i + 2)
            block = "\n".join(lines[start:end])
            relevant_blocks.append(f"--- line {i+1} ---\n{block}")
            if len(relevant_blocks) >= 12:
                break
    return {"family_name": family_name,
            "found_blocks": len(relevant_blocks),
            "excerpts": _truncate("\n\n".join(relevant_blocks), 6000)}


def tool_list_a4v3_families(env: ToolEnv) -> dict[str, Any]:
    return {"families": [
        "TypeDecl", "SymbolDecl", "AssertDecl", "PathDecl", "ActionDecl",
        "TemporalDecl", "DeonticDecl", "ValidationDecl", "ProbabilisticDecl",
        "GameDecl", "GraphDecl", "TheoremDecl",
    ], "common_constructs": [
        "sort", "entity", "rel", "fun", "fact", "constraint",
        "permission", "obligation", "prohibition",
    ]}
