"""a4v3_semantic_lint_v1.py

Small deterministic lint checks for A4V3 drafts.

This module intentionally does not decide whether an IR is semantically
faithful to the source. It catches translator-workflow smells that repeatedly
showed up during manual financial methodology work:

- unused local declarations
- obligation scope that repeats an obligation parameter sort
- obligation names that read like completed events rather than actions
- likely double-coding of one deontic norm as both obligation and constraint
- ad-hoc temporal relations in deontic files
- vacuous responsibility implications
- bare universal predicate constraints that only assert a label
- fact-like universal constraints that should likely be facts
- non-numeric function return sorts used in numeric comparisons/aggregates
- named based-on constraints whose body does not link dependent value and basis
- repeated semantic tokens in predicate/function names without a structural carrier
- relation/function arity above the local-IR comfort threshold
- sentence-like string literals in formula bodies
- deontic parameters typed by entity names instead of sort names
- semantic contract gaps: strong IR usage that relies on hidden semantics not
  present in the main IR, prelude, repair overlay, or translator notes

Outputs:
  <entry>/a4v3_semantic_lint_v1.json
  <entry>/a4v3_semantic_lint_v1.md

CLI:
  python a4v3_semantic_lint_v1.py [entry_dir|run_root]
"""
from __future__ import annotations

import json
import pathlib
import re
import sys
from collections import Counter, defaultdict
from typing import Any


ROOT = pathlib.Path(__file__).resolve().parents[2]

TOP_LEVEL_KINDS = {
    "sort", "entity", "rel", "fun", "val", "fact", "constraint",
    "axiom", "prop", "action", "obligation", "permission",
    "prohibition", "theorem",
}

CLAIM_KINDS = {"fact", "constraint", "axiom", "prop", "theorem"}
SYMBOL_KINDS = {"rel", "fun", "sort", "entity", "val"}
TEMPORAL_REL_TOKENS = {
    "prior", "before", "after", "precede", "precedes", "preceded",
    "preceding", "subsequent", "since", "until",
}
NUMERIC_SORTS = {
    "Decimal", "Float", "Int", "Integer", "Nat", "Natural", "Number",
    "Numeric", "Percent", "Percentage", "Real", "Rational",
    "MonetaryAmount",
}
SEMANTIC_CONTRACT_TRIGGER_RE = re.compile(
    r"\b(?:top|first|highest|lowest|largest|smallest|best)\s+\d+\b",
    re.IGNORECASE,
)
RANK_CUT_RE = re.compile(
    r"\brank\s*\(.*\)\s*(?P<op><=|<)\s*(?P<bound>\d+)\b"
)
CHECK_CONTRACT_CLASS = {
    "numeric_operation_on_non_numeric_sort": "value_domain_contract",
    "basis_relation_without_value_link": "dependency_contract",
    "bare_universal_predicate_constraint": "process_contract",
    "fact_like_universal_constraint": "process_contract",
    "possible_double_coded_deontic_norm": "modality_contract",
    "temporal_rel_in_deontic_context": "modality_contract",
    "vacuous_responsibility_implication": "scope_contract",
    "self_referential_deontic_scope": "scope_contract",
    "shared_name_token_without_structural_carrier": "dependency_contract",
    "relation_or_function_arity_gt_2_without_role_explanation": "role_contract",
    "relation_or_function_arity_gt_5": "role_contract",
    "sentence_literal_in_formula": "value_domain_contract",
    "permission_source_asserts_concrete_event_instance": "modality_contract",
    "deontic_role_parameter_not_bound": "role_contract",
    "deontic_parameter_type_is_entity": "role_contract",
    "missing_instance_layer_for_referenceable_category": "structural_contract",
    "redundant_entity_shadowing_sort": "structural_contract",
}
GENERIC_RELATION_TOKENS = {
    "a", "an", "and", "are", "as", "at", "by", "for", "from", "has",
    "in", "is", "of", "on", "or", "rule", "rules", "the", "to", "with",
}
EVENT_LIKE_SORT_TOKENS = {
    "action", "adjustment", "amendment", "announcement", "application",
    "calculation", "cessation", "change", "classification", "decision",
    "determination", "deviation", "event", "exercise", "issuance",
    "modification", "notice", "publication", "rebalance", "review",
    "selection", "submission", "transition",
}
DEONTIC_ROLE_PARAM_NAMES = {
    "agent", "issuer", "recipient", "licensee", "scope", "context",
    "instrument", "target", "object", "beneficiary", "counterparty",
}
SHARED_NAME_TOKEN_STOPLIST = GENERIC_RELATION_TOKENS | {
    "adapt", "adapts", "anchor", "appli", "apply", "applied",
    "available", "case", "cases", "condition", "conditions", "constraint",
    "constraints", "change", "changes", "chang", "day", "days", "detail",
    "details", "document", "eligible", "event", "fact", "facts", "follow",
    "follows", "guideline", "guidelines", "highest", "identifi", "identify",
    "includ", "include", "includes", "current", "currently",
    "index", "indices", "inform", "informing", "consult", "consulting",
    "methodology", "methodologies", "object", "option", "options", "part",
    "policy", "policies", "procedure", "procedures", "process", "processes",
    "prior", "publish", "published", "relation", "relations", "scope",
    "section", "sections", "situation", "situations", "source", "target",
    "targets", "term", "terms", "time", "times", "transition", "terminate",
    "termination", "url", "use", "used", "using", "value", "values",
}
PAST_PARTICIPLE_IRREGULAR = {"made", "given", "done", "taken", "known"}
PAST_PARTICIPLE_SUFFIX_ALLOWLIST = {"open", "even"}

DECL_RE = re.compile(
    r"^(?P<kind>sort|entity|rel|fun|val|fact|constraint|axiom|prop|action|"
    r"obligation|permission|prohibition|theorem)(?:\[[^\]]+\])?\s+"
    r"(?P<name>[A-Za-z_][A-Za-z0-9_]*)(?P<rest>.*)$"
)
IDENT_RE = re.compile(r"\b[A-Za-z_][A-Za-z0-9_]*\b")
STRING_LITERAL_RE = re.compile(r'"([^"\\]*(?:\\.[^"\\]*)*)"')
WORD_RE = re.compile(r"\b[A-Za-z][A-Za-z0-9_-]*\b")


def _norm_explanation_text(text: str) -> str:
    return re.sub(r"[^a-z0-9_]+", " ", text.lower())


def _strip_comment(line: str) -> str:
    # A4V3 files in the workspace use both `--` and `//` comments.
    # The semantic lint is intentionally lightweight, but comments must not
    # leak into declaration signatures; otherwise role/arity checks count
    # prose words as argument sorts.
    line = line.split("--", 1)[0]
    line = line.split("//", 1)[0]
    return line.rstrip()


def _tokens(name: str) -> list[str]:
    out: list[str] = []
    for chunk in re.split(r"[_\W]+", name):
        if not chunk:
            continue
        out.extend(x.lower() for x in re.findall(r"[A-Z]?[a-z]+|[A-Z]+(?![a-z])|[0-9]+", chunk))
    return out


def _stem_token(tok: str) -> str:
    tok = tok.lower()
    if tok.endswith("ies") and len(tok) > 4:
        return tok[:-3] + "y"
    for suffix in ("ing", "ed", "es", "s"):
        if tok.endswith(suffix) and len(tok) > len(suffix) + 2:
            return tok[:-len(suffix)]
    return tok


def _action_terms(action: str) -> set[str]:
    terms = set(_tokens(action))
    stems = {_stem_token(t) for t in terms}
    terms |= stems
    expansions = {
        "submit": {"submit", "submitted", "submission"},
        "submitt": {"submit", "submitted", "submission"},
        "approve": {"approve", "approved", "approval"},
        "make": {"make", "made", "making"},
        "made": {"make", "made", "making"},
        "comply": {"comply", "compliance", "compliant"},
        "compliance": {"comply", "compliance", "compliant"},
        "return": {"return", "returned"},
        "take": {"take", "taken", "taking"},
    }
    for term in list(terms):
        terms |= expansions.get(term, set())
    # Action names often contain glue prepositions such as
    # `make_in_compliance_with`. These words are too broad for double-coding
    # detection: otherwise any constraint mentioning the same target and the
    # word "with" looks like a duplicated norm.
    action_stopwords = {"in", "with", "of", "to", "for", "from", "by", "on", "at", "as"}
    return {t for t in terms if t and t not in action_stopwords}


def _sort_parents(blocks: list[dict[str, Any]]) -> dict[str, str]:
    parents: dict[str, str] = {}
    for block in blocks:
        if block["kind"] != "sort":
            continue
        m = re.search(r"\bextends\s+([A-Za-z_][A-Za-z0-9_]*)", block["header"])
        if m:
            parents[block["name"]] = m.group(1)
    return parents


def _is_numeric_sort(sort_name: str, parents: dict[str, str] | None = None) -> bool:
    if sort_name in NUMERIC_SORTS or sort_name.lower().endswith(("percent", "percentage")):
        return True
    parents = parents or {}
    seen: set[str] = set()
    cur = sort_name
    while cur in parents and cur not in seen:
        seen.add(cur)
        cur = parents[cur]
        if cur in NUMERIC_SORTS or cur.lower().endswith(("percent", "percentage")):
            return True
    return False


def _parse_blocks(text: str) -> list[dict[str, Any]]:
    lines = text.splitlines()
    blocks: list[dict[str, Any]] = []
    current: dict[str, Any] | None = None

    for line_no, raw_line in enumerate(lines, start=1):
        line = _strip_comment(raw_line)
        if not line.strip():
            if current is not None:
                current["lines"].append(raw_line)
            continue
        if line.startswith((" ", "\t")):
            if current is not None:
                current["lines"].append(raw_line)
            continue
        m = DECL_RE.match(line.strip())
        if m and m.group("kind") in TOP_LEVEL_KINDS:
            if current is not None:
                blocks.append(current)
            current = {
                "kind": m.group("kind"),
                "name": m.group("name"),
                "rest": m.group("rest").strip(),
                "line_no": line_no,
                "header": line.strip(),
                "lines": [raw_line],
            }
        elif current is not None:
            current["lines"].append(raw_line)

    if current is not None:
        blocks.append(current)

    for block in blocks:
        block["text"] = "\n".join(block["lines"])
        block["body"] = "\n".join(block["lines"][1:])
    return blocks


def _extract_params(text: str) -> list[dict[str, str]]:
    normalized = re.sub(r"\s+", " ", text)
    m = re.search(r"\((.*?)\)", normalized)
    if not m:
        return []
    out: list[dict[str, str]] = []
    for part in m.group(1).split(","):
        pm = re.search(r"\b([A-Za-z_][A-Za-z0-9_]*)\s*:\s*([A-Za-z_][A-Za-z0-9_]*)", part)
        if pm:
            out.append({"name": pm.group(1), "sort": pm.group(2)})
    return out


def _extract_fields(block: dict[str, Any]) -> dict[str, str]:
    fields: dict[str, str] = {}
    for raw_line in block["lines"][1:]:
        line = _strip_comment(raw_line).strip()
        m = re.match(r"^(action|target|scope|deadline)\s*:\s*(.+?)\s*$", line)
        if m:
            fields[m.group(1)] = m.group(2).strip()
    return fields


def _declared_sort_refs(block: dict[str, Any]) -> set[str]:
    refs: set[str] = set()
    header = block["header"]
    decl_text = re.sub(
        r"\s+",
        " ",
        "\n".join(_strip_comment(line) for line in block["lines"]),
    )
    kind = block["kind"]
    if kind == "sort":
        m = re.search(r"\bextends\s+([A-Za-z_][A-Za-z0-9_]*)", header)
        if m:
            refs.add(m.group(1))
    elif kind == "entity":
        m = re.search(r":\s*([A-Za-z_][A-Za-z0-9_]*)", header)
        if m:
            refs.add(m.group(1))
    elif kind in {"rel", "fun", "val"}:
        if ":" in decl_text:
            sig = decl_text.split(":", 1)[1]
            refs |= set(IDENT_RE.findall(sig))
    elif kind in {"obligation", "permission", "prohibition"}:
        refs |= {p["sort"] for p in _extract_params(block["text"])}
        fields = _extract_fields(block)
        if fields.get("scope"):
            refs |= set(IDENT_RE.findall(fields["scope"]))
        if fields.get("target"):
            refs |= set(IDENT_RE.findall(fields["target"]))
    return refs


def _function_return_sorts(blocks: list[dict[str, Any]]) -> dict[str, str]:
    out: dict[str, str] = {}
    for block in blocks:
        if block["kind"] != "fun":
            continue
        decl_text = re.sub(r"\s+", " ", block["text"])
        m = re.search(r":\s*(.*?)\s*->\s*([A-Za-z_][A-Za-z0-9_]*)\b", decl_text)
        if m:
            out[block["name"]] = m.group(2)
    return out


def _signature_text(block: dict[str, Any]) -> str:
    """Return the declaration signature body after `:`.

    A4V3 relation/function signatures are often split across lines:

        rel foo :
          A, B

    The semantic lint only needs a lightweight tokenizer, so a normalized text
    slice is enough.
    """
    decl_text = re.sub(
        r"\s+",
        " ",
        "\n".join(_strip_comment(line) for line in block["lines"]),
    )
    if ":" not in decl_text:
        return ""
    return decl_text.split(":", 1)[1].strip()


def _signature_input_sorts(block: dict[str, Any]) -> list[str]:
    sig = _signature_text(block)
    if not sig:
        return []
    if block["kind"] == "fun":
        sig = sig.split("->", 1)[0].strip()
    else:
        sig = sig.rstrip(".")
    return [
        tok
        for tok in IDENT_RE.findall(sig)
        # Ignore optional annotations if they ever leak into the signature
        # slice; relation/function argument positions are type names.
        if tok not in {"required", "optional"}
    ]


def _arity_explanation_context(entry_dir: pathlib.Path) -> str:
    parts: list[str] = []
    for name in ("translator_notes.md", "provenance.yaml"):
        p = entry_dir / name
        if p.exists():
            parts.append(p.read_text(encoding="utf-8", errors="replace"))
    return _norm_explanation_text("\n".join(parts))


def _symbol_has_role_explanation(symbol: str, explanation_context: str) -> bool:
    if not explanation_context:
        return False
    symbol_norm = _norm_explanation_text(symbol).strip()
    if symbol_norm and symbol_norm in explanation_context:
        return True
    # Human notes often discuss arity/carriers without repeating every long
    # relation name. Accept a role/carrier discussion that mentions the major
    # non-generic tokens of the symbol.
    toks = [
        t
        for t in _tokens(symbol)
        if len(t) > 2 and t not in GENERIC_RELATION_TOKENS
    ]
    if not toks:
        return False
    hits = sum(1 for t in set(toks) if re.search(rf"\b{re.escape(t)}\b", explanation_context))
    has_role_words = any(
        word in explanation_context
        for word in (" role ", " roles ", " arity ", " carrier ", " reification ")
    )
    return has_role_words and hits >= min(2, len(set(toks)))


def _call_names(text: str) -> list[str]:
    return re.findall(r"\b([A-Za-z_][A-Za-z0-9_]*)\s*\(", text)


def _used_identifiers(blocks: list[dict[str, Any]]) -> set[str]:
    used: set[str] = set()
    for block in blocks:
        kind = block["kind"]
        if kind in CLAIM_KINDS:
            # Include the body after the declaration header. The declaration name
            # itself must not count as evidence of use.
            used |= set(IDENT_RE.findall(block["body"]))
            # Header decorators such as `[realizes: RuleObject]` are explicit
            # links and should keep the referenced rule object alive.
            used |= set(IDENT_RE.findall(block.get("rest") or ""))
        elif kind in {"obligation", "permission", "prohibition"}:
            fields = _extract_fields(block)
            for value in fields.values():
                used |= set(IDENT_RE.findall(value))
            body_without_comments = "\n".join(
                _strip_comment(line) for line in block["lines"][1:]
            )
            used |= set(IDENT_RE.findall(body_without_comments))
            used |= {p["sort"] for p in _extract_params(block["text"])}
        used |= _declared_sort_refs(block)
    return used


def _unused_declarations(blocks: list[dict[str, Any]]) -> list[dict[str, Any]]:
    declared = [b for b in blocks if b["kind"] in SYMBOL_KINDS]
    used = _used_identifiers(blocks)
    out: list[dict[str, Any]] = []
    for block in declared:
        if block["name"] in used:
            continue
        severity = "strong" if block["kind"] in {"rel", "fun"} else "soft"
        out.append({
            "check": "unused_declaration",
            "severity": severity,
            "decl_kind": block["kind"],
            "symbol": block["name"],
            "line_no": block["line_no"],
            "raw_decl": block["header"],
            "reason": (
                "Declaration is not referenced by any assertion body, deontic field, "
                "or another declaration signature."
            ),
        })
    return out


def _arity_findings(entry_dir: pathlib.Path, blocks: list[dict[str, Any]]) -> list[dict[str, Any]]:
    explanation_context = _arity_explanation_context(entry_dir)
    out: list[dict[str, Any]] = []
    for block in blocks:
        if block["kind"] not in {"rel", "fun"}:
            continue
        args = _signature_input_sorts(block)
        arity = len(args)
        if arity <= 2:
            continue
        if arity > 5:
            out.append({
                "check": "relation_or_function_arity_gt_5",
                "severity": "strong",
                "decl_kind": block["kind"],
                "symbol": block["name"],
                "line_no": block["line_no"],
                "arity": arity,
                "argument_sorts": args,
                "raw_decl": block["header"],
                "reason": (
                    "Relation/function arity is above 5. Reify the claim as a "
                    "carrier/event with explicit binary role relations."
                ),
            })
        elif not _symbol_has_role_explanation(block["name"], explanation_context):
            out.append({
                "check": "relation_or_function_arity_gt_2_without_role_explanation",
                "severity": "soft",
                "decl_kind": block["kind"],
                "symbol": block["name"],
                "line_no": block["line_no"],
                "arity": arity,
                "argument_sorts": args,
                "raw_decl": block["header"],
                "reason": (
                    "Relation/function arity is above 2. This is allowed for "
                    "local IR, but roles must be clearly explained in "
                    "translator_notes.md or provenance.yaml; otherwise prefer "
                    "a carrier plus binary role relations."
                ),
            })
    return out


def _sentence_literals_in_formula(blocks: list[dict[str, Any]]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for block in blocks:
        if block["kind"] not in CLAIM_KINDS:
            continue
        for raw_line in block["lines"][1:]:
            line = _strip_comment(raw_line)
            for m in STRING_LITERAL_RE.finditer(line):
                literal = m.group(1)
                words = WORD_RE.findall(literal)
                if len(words) < 4:
                    continue
                out.append({
                    "check": "sentence_literal_in_formula",
                    "severity": "strong",
                    "decl_kind": block["kind"],
                    "claim": block["name"],
                    "line_no": block["line_no"],
                    "literal": literal,
                    "word_count": len(words),
                    "reason": (
                        "Formula body contains a sentence-like string literal. "
                        "Do not encode a variable/concept as prose; introduce "
                        "a sort/entity/value carrier and explicit relations."
                    ),
                })
    return out


def _self_referential_scope(blocks: list[dict[str, Any]]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for block in blocks:
        if block["kind"] not in {"obligation", "permission", "prohibition"}:
            continue
        fields = _extract_fields(block)
        scope = fields.get("scope")
        if not scope:
            continue
        param_sorts = {p["sort"] for p in _extract_params(block["text"])}
        if scope in param_sorts:
            out.append({
                "check": "self_referential_deontic_scope",
                "severity": "strong",
                "decl_kind": block["kind"],
                "symbol": block["name"],
                "line_no": block["line_no"],
                "scope": scope,
                "parameter_sorts": sorted(param_sorts),
                "reason": "The deontic scope repeats a parameter sort instead of adding a context.",
            })
    return out


def _past_participle_obligation_names(blocks: list[dict[str, Any]]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for block in blocks:
        if block["kind"] != "obligation":
            continue
        toks = _tokens(block["name"])
        first = toks[0] if toks else ""
        if not first:
            continue
        looks_past = (
            first in PAST_PARTICIPLE_IRREGULAR
            or (
                (first.endswith("ed") or first.endswith("en"))
                and first not in PAST_PARTICIPLE_SUFFIX_ALLOWLIST
                and len(first) > 4
            )
        )
        if looks_past:
            out.append({
                "check": "past_participle_obligation_name",
                "severity": "style",
                "decl_kind": block["kind"],
                "symbol": block["name"],
                "line_no": block["line_no"],
                "first_token": first,
                "reason": "Obligation names should read as actions, not already-completed events.",
            })
    return out


def _double_coded_deontic_norms(blocks: list[dict[str, Any]]) -> list[dict[str, Any]]:
    obligations = [b for b in blocks if b["kind"] in {"obligation", "prohibition"}]
    constraints = [b for b in blocks if b["kind"] == "constraint"]
    out: list[dict[str, Any]] = []
    for obl in obligations:
        fields = _extract_fields(obl)
        action = fields.get("action", "")
        target = fields.get("target", "")
        if not action or not target:
            continue
        action_terms = _action_terms(action)
        target_terms = set(IDENT_RE.findall(target))
        for constraint in constraints:
            text = constraint["text"]
            text_tokens = set(_tokens(text))
            has_action = bool(action_terms & text_tokens)
            has_target = any(t in text for t in target_terms)
            if has_action and has_target:
                out.append({
                    "check": "possible_double_coded_deontic_norm",
                    "severity": "strong",
                    "deontic_decl": obl["name"],
                    "deontic_line_no": obl["line_no"],
                    "constraint": constraint["name"],
                    "constraint_line_no": constraint["line_no"],
                    "action": action,
                    "target": target,
                    "matched_action_terms": sorted(action_terms & text_tokens),
                    "reason": (
                        "A deontic norm may also be encoded as a hard constraint "
                        "with the same action/target."
                    ),
                })
    return out


def _temporal_rel_in_deontic_context(blocks: list[dict[str, Any]]) -> list[dict[str, Any]]:
    has_deontic = any(b["kind"] in {"obligation", "permission", "prohibition"} for b in blocks)
    if not has_deontic:
        return []
    declared_rels = [b for b in blocks if b["kind"] == "rel"]
    claim_text = "\n".join(b["text"] for b in blocks if b["kind"] in CLAIM_KINDS)
    out: list[dict[str, Any]] = []
    for rel in declared_rels:
        toks = set(_tokens(rel["name"]))
        if not (toks & TEMPORAL_REL_TOKENS):
            continue
        if not re.search(rf"\b{re.escape(rel['name'])}\s*\(", claim_text):
            continue
        out.append({
            "check": "temporal_rel_in_deontic_context",
            "severity": "advisory",
            "decl_kind": "rel",
            "symbol": rel["name"],
            "line_no": rel["line_no"],
            "matched_tokens": sorted(toks & TEMPORAL_REL_TOKENS),
            "reason": (
                "Temporal relation is used in assertion bodies while the file has "
                "deontic declarations; inspect whether temporal/deontic structure "
                "should be first-class instead."
            ),
        })
    return out


def _vacuous_responsibility_constraints(blocks: list[dict[str, Any]]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    forall_re = r"forall\s+([A-Za-z_][A-Za-z0-9_]*)\s*:\s*([A-Za-z_][A-Za-z0-9_]*)"
    for block in blocks:
        if block["kind"] != "constraint":
            continue
        body = re.sub(r"\s+", " ", block["body"])
        if "implies" not in body or "responsible_for" not in body or "exists" in body:
            continue
        qvars = re.findall(forall_re, body)
        if len(qvars) < 2:
            continue
        vars_only = [v for v, _sort in qvars]
        for d in vars_only:
            for a in vars_only:
                if d == a:
                    continue
                antecedent = re.search(
                    rf"\b([A-Za-z_][A-Za-z0-9_]*)\s*\(\s*{re.escape(d)}\s*,\s*{re.escape(a)}\s*\)\s*implies",
                    body,
                )
                consequent = re.search(
                    rf"responsible_for\s*\(\s*[^,]+,\s*{re.escape(d)}\s*\)",
                    body,
                )
                if antecedent and consequent:
                    out.append({
                        "check": "vacuous_responsibility_implication",
                        "severity": "strong",
                        "constraint": block["name"],
                        "line_no": block["line_no"],
                        "decision_var": d,
                        "subject_var": a,
                        "antecedent_rel": antecedent.group(1),
                        "reason": (
                            "Responsibility is guarded by existence of an external decision. "
                            "If the source requires a decision for every governed item, use "
                            "forall item, exists decision, rel(decision,item) and responsible_for(...)."
                        ),
                    })
    return out


def _bare_universal_predicate_constraints(blocks: list[dict[str, Any]]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    bare_re = re.compile(
        r"^(?P<quantifiers>(?:forall\s+[A-Za-z_][A-Za-z0-9_]*\s*:\s*"
        r"[A-Za-z_][A-Za-z0-9_]*\s*,\s*)+)"
        r"(?P<predicate>[A-Za-z_][A-Za-z0-9_]*)\s*\((?P<args>[^()]*)\)\s*$"
    )
    qvar_re = re.compile(r"forall\s+([A-Za-z_][A-Za-z0-9_]*)\s*:")
    for block in blocks:
        if block["kind"] != "constraint":
            continue
        body = " ".join(
            _strip_comment(line).strip()
            for line in block["body"].splitlines()
            if _strip_comment(line).strip()
        )
        m = bare_re.match(body)
        if not m:
            continue
        predicate = m.group("predicate")
        if predicate in {"true", "false"}:
            continue
        out.append({
            "check": "bare_universal_predicate_constraint",
            "severity": "strong",
            "constraint": block["name"],
            "line_no": block["line_no"],
            "predicate": predicate,
            "quantified_vars": qvar_re.findall(m.group("quantifiers")),
            "raw_body": body,
            "reason": (
                "Constraint universally asserts a single predicate with no equality, "
                "comparison, implication, aggregate, or value link. This often hides "
                "semantic load in the predicate name instead of the formula body."
            ),
        })
    return out


def _fact_like_universal_constraints(blocks: list[dict[str, Any]]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    quantifier_re = re.compile(
        r"^\s*(?:forall\s+[A-Za-z_][A-Za-z0-9_]*\s*:\s*"
        r"[A-Za-z_][A-Za-z0-9_]*\s*,\s*)+"
    )
    simple_bare_re = re.compile(
        r"^(?:forall\s+[A-Za-z_][A-Za-z0-9_]*\s*:\s*"
        r"[A-Za-z_][A-Za-z0-9_]*\s*,\s*)+"
        r"[A-Za-z_][A-Za-z0-9_]*\s*\([^()]*\)\s*$"
    )
    qvar_re = re.compile(r"forall\s+([A-Za-z_][A-Za-z0-9_]*)\s*:")
    atom_re = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*\s*\(.+\)$")
    constraint_keywords = {
        "implies", "iff", "exists", "sum", "count", "min", "max",
        "until", "since", "always", "eventually",
    }
    for block in blocks:
        if block["kind"] != "constraint":
            continue
        body = " ".join(
            _strip_comment(line).strip()
            for line in block["body"].splitlines()
            if _strip_comment(line).strip()
        )
        if not body:
            continue
        if simple_bare_re.match(body):
            # The stricter label-only check reports this as a stronger smell.
            continue
        qm = quantifier_re.match(body)
        if not qm:
            continue
        formula = body[qm.end():].strip()
        formula_l = formula.lower()
        if any(re.search(rf"\b{kw}\b", formula_l) for kw in constraint_keywords):
            continue
        if re.search(r"(<=|>=|<|>|=|\+|\*|/)", formula):
            continue
        conjuncts = [part.strip() for part in re.split(r"\band\b", formula) if part.strip()]
        if not conjuncts:
            continue
        if not all(atom_re.match(part) for part in conjuncts):
            continue
        out.append({
            "check": "fact_like_universal_constraint",
            "severity": "soft",
            "constraint": block["name"],
            "line_no": block["line_no"],
            "quantified_vars": qvar_re.findall(qm.group(0)),
            "raw_body": body,
            "reason": (
                "Constraint universally asserts descriptive/procedural atoms with no "
                "comparison, equality, implication, existential witness, aggregate, "
                "or temporal operator. If this is a source description rather than a "
                "hard admissibility condition, prefer fact."
            ),
        })
    return out


def _numeric_operation_on_non_numeric_sort(blocks: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return_sorts = _function_return_sorts(blocks)
    parents = _sort_parents(blocks)
    out: list[dict[str, Any]] = []
    seen: set[tuple[str, str, str]] = set()
    numeric_literal = r"[-+]?\d+(?:\.\d+)?%?"
    for block in blocks:
        if block["kind"] not in CLAIM_KINDS:
            continue
        body = re.sub(r"\s+", " ", block["body"])
        for fun_name, return_sort in return_sorts.items():
            if _is_numeric_sort(return_sort, parents):
                continue
            escaped = re.escape(fun_name)
            contexts: list[str] = []
            call = rf"{escaped}\s*\([^)]*\)"
            if re.search(rf"\b{call}\s*(?:<=|>=|<|>)\s*{numeric_literal}(?![A-Za-z0-9_])", body):
                contexts.append("comparison_to_numeric_literal")
            if re.search(rf"(?<![A-Za-z0-9_]){numeric_literal}\s*(?:<=|>=|<|>)\s*{call}", body):
                contexts.append("reverse_comparison_to_numeric_literal")
            if re.search(
                rf"\b{call}\s*(?:<=|>=|<|>)\s*[A-Za-z_][A-Za-z0-9_]*\s*\(",
                body,
            ):
                contexts.append("comparison_to_function_call")
            if re.search(
                rf"\b[A-Za-z_][A-Za-z0-9_]*\s*\([^)]*\)\s*(?:<=|>=|<|>)\s*{call}",
                body,
            ):
                contexts.append("reverse_comparison_to_function_call")
            if re.search(rf"\bsum\s*\(.+,\s*{escaped}\s*\(", body):
                contexts.append("sum_value_term")
            if not contexts:
                continue
            key = (block["name"], fun_name, return_sort)
            if key in seen:
                continue
            seen.add(key)
            out.append({
                "check": "numeric_operation_on_non_numeric_sort",
                "severity": "strong",
                "constraint": block["name"],
                "line_no": block["line_no"],
                "function": fun_name,
                "return_sort": return_sort,
                "contexts": contexts,
                "reason": (
                    "Function result is used in numeric comparison or aggregate, "
                    "but its declared return sort is not a known numeric/value sort."
                ),
            })
    return out


def _split_based_on_tokens(name: str) -> tuple[list[str], list[str]] | None:
    toks = _tokens(name)
    for i in range(len(toks) - 1):
        if toks[i] == "based" and toks[i + 1] == "on":
            return toks[:i], toks[i + 2:]
    if "basis" in toks:
        i = toks.index("basis")
        return toks[:i], toks[i + 1:]
    return None


def _specific_tokens(tokens: list[str]) -> set[str]:
    return {
        _stem_token(t)
        for t in tokens
        if t and t not in GENERIC_RELATION_TOKENS and t not in {"based", "basis"}
    }


def _shared_name_specific_tokens(name: str) -> set[str]:
    out: set[str] = set()
    for tok in _tokens(name):
        stem = _stem_token(tok)
        if not stem or stem in SHARED_NAME_TOKEN_STOPLIST:
            continue
        if stem.isdigit() or len(stem) < 4:
            continue
        out.add(stem)
    return out


def _structural_carrier_tokens(blocks: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    """Tokens that have a real structural carrier, not just a rel/fun name.

    Carriers are local sorts/entities/values and relation/function signature
    sorts. Relation/function names themselves are intentionally excluded.
    """
    carriers: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for block in blocks:
        if block["kind"] in {"sort", "entity", "val"}:
            for tok in _shared_name_specific_tokens(block["name"]):
                carriers[tok].append({
                    "kind": block["kind"],
                    "name": block["name"],
                    "line_no": block["line_no"],
                })
            continue
        if block["kind"] not in {"rel", "fun"}:
            continue
        decl_text = re.sub(r"\s+", " ", block["text"])
        if ":" not in decl_text:
            continue
        sig = decl_text.split(":", 1)[1]
        for ident in IDENT_RE.findall(sig):
            for tok in _shared_name_specific_tokens(ident):
                carriers[tok].append({
                    "kind": "signature_sort",
                    "name": ident,
                    "decl": block["name"],
                    "line_no": block["line_no"],
                })
    return carriers


def _claim_body_structural_tokens(block: dict[str, Any]) -> dict[str, list[str]]:
    """Tokens carried by arguments/sorts/entities inside a claim body.

    Call identifiers are excluded, because this check is specifically about
    not treating predicate names as structural links.
    """
    call_names = set(_call_names(block["body"]))
    reserved = {
        "and", "or", "not", "implies", "iff", "forall", "exists", "sum",
        "count", "where", "true", "false",
    }
    carriers: dict[str, list[str]] = defaultdict(list)
    for ident in IDENT_RE.findall(block["body"]):
        if ident in call_names or ident.lower() in reserved:
            continue
        for tok in _shared_name_specific_tokens(ident):
            carriers[tok].append(ident)
    return carriers


def _basis_relation_without_value_link(blocks: list[dict[str, Any]]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for block in blocks:
        if block["kind"] not in CLAIM_KINDS:
            continue
        split = _split_based_on_tokens(block["name"])
        if not split:
            continue
        left_tokens, right_tokens = split
        dependent_terms = _specific_tokens(left_tokens)
        basis_terms = _specific_tokens(right_tokens)
        if not dependent_terms or not basis_terms:
            continue
        semantic_calls: list[tuple[str, set[str]]] = []
        for call_name in _call_names(block["body"]):
            call_tokens = set(_stem_token(t) for t in _tokens(call_name))
            if call_tokens & {"based", "basis"}:
                continue
            if call_name in {"forall", "exists", "sum", "count"}:
                continue
            semantic_calls.append((call_name, call_tokens))
        dependent_hits = [
            call_name for call_name, toks in semantic_calls
            if toks & dependent_terms
        ]
        basis_hits = [
            call_name for call_name, toks in semantic_calls
            if toks & basis_terms
        ]
        missing: list[str] = []
        if not dependent_hits:
            missing.append("dependent_value")
        if not basis_hits:
            missing.append("basis_value")
        if not missing:
            continue
        out.append({
            "check": "basis_relation_without_value_link",
            "severity": "advisory",
            "constraint": block["name"],
            "line_no": block["line_no"],
            "dependent_terms": sorted(dependent_terms),
            "basis_terms": sorted(basis_terms),
            "semantic_calls": [name for name, _toks in semantic_calls],
            "missing": missing,
            "reason": (
                "The claim name says one value is based on another, but the body "
                "does not mention both the dependent value and the basis value as "
                "formula terms. This may be an intentionally weak provenance marker, "
                "or it may mean the semantic dependency is only in the name."
            ),
        })
    return out


def _shared_name_token_without_structural_carrier(blocks: list[dict[str, Any]]) -> list[dict[str, Any]]:
    declared_call_names = {b["name"] for b in blocks if b["kind"] in {"rel", "fun"}}
    global_carriers = _structural_carrier_tokens(blocks)
    out: list[dict[str, Any]] = []
    seen: set[tuple[str, str]] = set()
    for block in blocks:
        if block["kind"] not in CLAIM_KINDS:
            continue
        normalized_body = re.sub(r"\s+", " ", block.get("body", "")).lower()
        calls = [
            call for call in _call_names(block["body"])
            if call in declared_call_names
        ]
        if len(set(calls)) < 2:
            continue
        token_to_calls: dict[str, set[str]] = defaultdict(set)
        for call in calls:
            for tok in _shared_name_specific_tokens(call):
                token_to_calls[tok].add(call)
        body_carriers = _claim_body_structural_tokens(block)
        for tok, call_set in sorted(token_to_calls.items()):
            if len(call_set) < 2:
                continue
            # Polarity bridge pattern, e.g.:
            #   non_conclusive(l) iff not conclusive(l)
            # Here the repeated token is exactly the intended positive/negative
            # pairing, and the body contains explicit `not`, so the semantic
            # link is not merely hidden in names.
            has_positive = any(call == tok for call in call_set)
            has_negative_prefixed = any(call.startswith(f"non_{tok}") or call.startswith(f"not_{tok}") for call in call_set)
            if has_positive and has_negative_prefixed and " iff " in normalized_body and " not " in normalized_body:
                continue
            if global_carriers.get(tok) or body_carriers.get(tok):
                continue
            key = (block["name"], tok)
            if key in seen:
                continue
            seen.add(key)
            out.append({
                "check": "shared_name_token_without_structural_carrier",
                "severity": "soft",
                "claim_kind": block["kind"],
                "claim": block["name"],
                "line_no": block["line_no"],
                "shared_token": tok,
                "calls": sorted(call_set),
                "reason": (
                    "A non-generic semantic token is repeated across multiple "
                    "predicate/function names in one claim, but the token has no "
                    "structural carrier such as a sort, entity, signature argument, "
                    "or formula-body argument. The relation may live only in names."
                ),
            })
    return out


def _entry_side_text(entry_dir: pathlib.Path) -> str:
    chunks: list[str] = []
    for name in ("source.md", "normalized.md", "translator_notes.md"):
        p = entry_dir / name
        if p.exists():
            chunks.append(p.read_text(encoding="utf-8", errors="ignore"))
    return "\n\n".join(chunks)


def _source_has_permission_modal(entry_dir: pathlib.Path) -> bool:
    """Conservative source-side signal for permission/possibility.

    This is intentionally lexical. It does not prove that the whole section is
    deontic; it only enables lowering-smell checks when the IR also declares a
    permission. The goal is to catch the common bad lowering:

        source: "X may be issued ..."
        IR:     permission issue(...)
                fact concrete_issuance_1 : ...  # wrongly asserts occurrence
    """
    chunks: list[str] = []
    for name in ("source.md", "normalized.md"):
        p = entry_dir / name
        if p.exists():
            chunks.append(p.read_text(encoding="utf-8", errors="ignore"))
    text = " ".join(chunks).lower()
    return bool(re.search(r"\bmay\b|\bpermitted\b|\bretains?\s+the\s+right\b", text))


def _entities_by_sort(blocks: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    out: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for block in blocks:
        if block["kind"] != "entity":
            continue
        m = re.search(r":\s*([A-Za-z_][A-Za-z0-9_]*)", block["header"])
        if not m:
            continue
        out[m.group(1)].append(block)
    return out


def _event_like_sort_names(blocks: list[dict[str, Any]]) -> set[str]:
    out: set[str] = set()
    for block in blocks:
        if block["kind"] != "sort":
            continue
        stems = {_stem_token(t) for t in _tokens(block["name"])}
        if stems & EVENT_LIKE_SORT_TOKENS:
            out.add(block["name"])
    return out


def _generic_instance_name(entity_name: str, sort_name: str) -> bool:
    """Detect numbered placeholder instances such as LicenseIssuance1.

    Canonical seed methodology usually names source/program entities semantically
    (`IndexUnderlyingValueLicenseIssuance`). Numbered instances are a useful
    deterministic signal that a drafter may have materialized an event rather
    than modeling its authorized class/program.
    """
    if re.search(r"(?:^|_)(?:copy|draft)\d*$", entity_name.lower()):
        return True
    if re.search(r"\d+$", entity_name):
        return True
    return entity_name.lower() in {
        f"{sort_name.lower()}instance",
        f"{sort_name.lower()}entity",
    }


def _permission_source_asserts_concrete_event_instance(
    entry_dir: pathlib.Path,
    blocks: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    if not _source_has_permission_modal(entry_dir):
        return []
    if not any(block["kind"] == "permission" for block in blocks):
        return []

    event_sorts = _event_like_sort_names(blocks)
    if not event_sorts:
        return []
    entities = _entities_by_sort(blocks)
    out: list[dict[str, Any]] = []
    seen: set[tuple[str, str]] = set()

    for sort_name in sorted(event_sorts):
        for ent in entities.get(sort_name, []):
            if not _generic_instance_name(ent["name"], sort_name):
                continue
            ent_ref_re = re.compile(rf"\b{re.escape(ent['name'])}\b")
            for block in blocks:
                if block["kind"] != "fact":
                    continue
                if not ent_ref_re.search(block["body"]):
                    continue
                # Facts whose names are also generic/numbered are especially
                # likely to assert that the event instance exists.
                fact_stems = {_stem_token(t) for t in _tokens(block["name"])}
                sort_stems = {_stem_token(t) for t in _tokens(sort_name)}
                if not (fact_stems & sort_stems or _generic_instance_name(block["name"], sort_name)):
                    continue
                key = (ent["name"], block["name"])
                if key in seen:
                    continue
                seen.add(key)
                out.append({
                    "check": "permission_source_asserts_concrete_event_instance",
                    "severity": "strong",
                    "decl_kind": "fact",
                    "claim": block["name"],
                    "line_no": block["line_no"],
                    "entity": ent["name"],
                    "entity_sort": sort_name,
                    "entity_line_no": ent["line_no"],
                    "reason": (
                        "The source contains permissive/modal language and the IR "
                        "declares a permission, but a fact asserts a concrete "
                        "numbered event/carrier instance. For permission clauses, "
                        "use a class/program/scope carrier unless the source "
                        "explicitly says the event occurred."
                    ),
                })
    return out


def _deontic_role_parameter_not_bound(blocks: list[dict[str, Any]]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for block in blocks:
        if block["kind"] not in {"permission", "obligation", "prohibition"}:
            continue
        params = _extract_params(block["text"])
        if len(params) <= 1:
            continue
        fields = _extract_fields(block)
        field_text = " ".join(fields.values())
        for param in params:
            name = param["name"]
            lname = name.lower()
            if lname in {"agent", "target"}:
                # Agent/target parameters are often intentionally represented
                # by their parameter role rather than repeated in fields.
                continue
            if name in field_text:
                continue
            param_stems = {_stem_token(t) for t in _tokens(name)}
            role_like = bool(param_stems & DEONTIC_ROLE_PARAM_NAMES)
            if not role_like:
                continue
            out.append({
                "check": "deontic_role_parameter_not_bound",
                "severity": "strong",
                "decl_kind": block["kind"],
                "symbol": block["name"],
                "line_no": block["line_no"],
                "parameter": name,
                "parameter_sort": param["sort"],
                "fields": fields,
                "reason": (
                    "A deontic declaration has a role-like parameter that is "
                    "not referenced by action/target/scope. This makes the "
                    "role decorative rather than semantically binding. Either "
                    "bind it in target/scope or move the role to an explicit "
                    "carrier/program fact."
                ),
            })
    return out


def _redundant_entity_shadowing_sort(
    blocks: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Detect entity declarations whose name == their sort type. Pattern:

        entity X : X            # tautological — name same as sort
        entity Foo : Foo        # same problem regardless of context

    Two sub-cases, both reported:
      1. `X` is an enum-member sort (single-value sort produced by
         `sort Parent = X | Y | Z`). Declaring `entity X : X` shadows
         the enum-member name with a separate entity in a different
         namespace, leading to ambiguity in facts that reference `X`.
      2. `X` is a regular non-enum sort. The entity is tautological:
         `entity X` of type `X` adds no information vs just using `X`
         as the singleton sort directly, and creates a confusing
         `X` vs `X` shadow.

    Severity: soft. Doesn't break parsing or semantics, but produces a
    cluttered IR that judges and reviewers flag as low-quality
    scaffolding.
    """
    # Collect all sort names + enum members
    sort_names: set[str] = set()
    enum_members: set[str] = set()
    for block in blocks:
        if block["kind"] != "sort":
            continue
        sort_names.add(block["name"])
        # Enum case: `sort Parent = A | B | C ...` (with optional newlines)
        m = re.search(r"=\s*(.+)$", block["text"], flags=re.DOTALL)
        if m:
            rhs = m.group(1)
            # Members separated by `|`; strip whitespace + identifiers only
            for part in rhs.split("|"):
                part = part.strip().rstrip(";")
                # Match a leading identifier
                tok = re.match(r"^([A-Z][\w]*)", part)
                if tok:
                    enum_members.add(tok.group(1))
                    sort_names.add(tok.group(1))

    out: list[dict[str, Any]] = []
    for block in blocks:
        if block["kind"] != "entity":
            continue
        # Parse `entity X : Y`
        m = re.match(r"entity\s+([A-Z][\w]*)\s*:\s*([A-Z][\w]*)",
                      block["text"])
        if not m:
            continue
        ent_name = m.group(1)
        ent_type = m.group(2)
        if ent_name != ent_type:
            continue
        sub_case = ("enum_member" if ent_name in enum_members
                     else "non_enum_singleton")
        reason = (
            f"entity `{ent_name}` is declared with sort type `{ent_type}` "
            f"identical to its own name. "
        )
        if sub_case == "enum_member":
            reason += (
                f"`{ent_name}` is an enum member of a parent sort; "
                f"facts can reference `{ent_name}` directly as a value "
                f"of that enum without needing a separately-declared "
                f"entity. Declaring `entity {ent_name} : {ent_name}` "
                f"creates a confusing entity-vs-enum-member shadow in "
                f"different namespaces."
            )
        else:
            reason += (
                f"`{ent_name}` is a singleton sort — using the sort "
                f"name directly in facts is sufficient. The entity "
                f"declaration adds no semantic content and introduces "
                f"a redundant name shadow."
            )
        out.append({
            "check": "redundant_entity_shadowing_sort",
            "severity": "soft",
            "decl_kind": "entity",
            "symbol": ent_name,
            "line_no": block["line_no"],
            "sub_case": sub_case,
            "shadowed_sort": ent_type,
            "reason": reason,
        })
    return out


def _missing_instance_layer_for_referenceable_category(
    blocks: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Advisory: when permission/obligation/prohibition uses a sort ending in
    `Class` (or with `Class` suffix on a stem) as parameter target or scope,
    and no companion non-Class instance sort with the same stem exists,
    surface this as an advisory finding.

    Rationale: in the canonical three-layer pattern for referenceable
    object categories (licenses, notices, publications, amendments,
    certificates, ...) the IR should have BOTH:
      - a base/instance sort (e.g. `License`, `IndexUnderlyingValueLicense`)
      - a class entity sort (e.g. `LicenseClass`) with a singleton entity
    Collapsing into class-only loses cross-section handle for individual
    objects. This advisory does NOT block — semantic translations are
    still valid; it surfaces a structural divergence from canonical.
    """
    sort_names = {block["name"] for block in blocks if block["kind"] == "sort"}
    if not sort_names:
        return []

    # For each XxxClass sort, check whether some companion non-Class sort
    # exists with a related stem. We accept either the exact stem (X without
    # the Class suffix), or any sort that the XxxClass sort "extends" in
    # its declaration text.
    class_sorts: dict[str, str] = {}  # name -> stem
    for name in sort_names:
        if name.endswith("Class") and len(name) > 5:
            class_sorts[name] = name[: -len("Class")]
    if not class_sorts:
        return []

    out: list[dict[str, Any]] = []
    seen_pairs: set[tuple[str, str]] = set()
    for block in blocks:
        if block["kind"] not in {"permission", "obligation", "prohibition"}:
            continue
        # Sorts referenced by this declaration: parameter types + the
        # bare token after `scope:` (best-effort).
        referenced: list[tuple[str, str]] = []  # (kind, sort_name)
        for param in _extract_params(block["text"]):
            referenced.append(("param_target", param["sort"]))
        scope_match = re.search(
            r"^\s*scope\s*:\s*([A-Za-z_]\w*)\s*$",
            block["text"],
            flags=re.MULTILINE,
        )
        if scope_match:
            referenced.append(("scope", scope_match.group(1)))

        for ref_kind, ref_sort in referenced:
            if ref_sort not in class_sorts:
                continue
            stem = class_sorts[ref_sort]
            # Companion instance sort: either the bare stem `Stem`, or any
            # sort whose declaration mentions `extends Stem` (i.e. a
            # narrower instance type built on the base instance sort).
            has_companion = stem in sort_names
            if not has_companion:
                for b in blocks:
                    if b["kind"] != "sort":
                        continue
                    if re.search(
                        rf"\bextends\s+{re.escape(stem)}\b", b["text"]
                    ):
                        has_companion = True
                        break
            if has_companion:
                continue
            key = (block["name"], ref_sort)
            if key in seen_pairs:
                continue
            seen_pairs.add(key)
            out.append({
                "check": "missing_instance_layer_for_referenceable_category",
                "severity": "advisory",
                "decl_kind": block["kind"],
                "symbol": block["name"],
                "line_no": block["line_no"],
                "referenced_sort": ref_sort,
                "reference_kind": ref_kind,
                "expected_instance_sort_stem": stem,
                "reason": (
                    f"{block['kind']} `{block['name']}` references "
                    f"`{ref_sort}` (class-level sort) as its {ref_kind}, "
                    f"but no companion instance sort `{stem}` (or any "
                    f"`extends {stem}` narrowing) is declared. If the "
                    f"source describes a category of OBJECTS that can "
                    f"exist as individual reference-able instances "
                    f"(licenses, notices, publications, amendments, "
                    f"certificates, ...), the canonical IR shape uses "
                    f"three layers: base instance sort `{stem}` + "
                    f"source-specific narrowing if needed + class "
                    f"singleton entity. Permission parameter should "
                    f"usually be the instance sort. Class-only is "
                    f"acceptable ONLY when source truly talks about the "
                    f"class itself, never about future individual objects."
                ),
            })
    return out


def _deontic_parameter_type_is_entity(blocks: list[dict[str, Any]]) -> list[dict[str, Any]]:
    entity_lines = {
        block["name"]: block["line_no"]
        for block in blocks
        if block["kind"] == "entity"
    }
    if not entity_lines:
        return []

    out: list[dict[str, Any]] = []
    for block in blocks:
        if block["kind"] not in {"permission", "obligation", "prohibition"}:
            continue
        for param in _extract_params(block["text"]):
            param_type = param["sort"]
            if param_type not in entity_lines:
                continue
            out.append({
                "check": "deontic_parameter_type_is_entity",
                "severity": "strong",
                "decl_kind": block["kind"],
                "symbol": block["name"],
                "line_no": block["line_no"],
                "parameter": param["name"],
                "parameter_type": param_type,
                "entity_line_no": entity_lines[param_type],
                "reason": (
                    "A deontic parameter is typed by an entity name. "
                    "Parameters must be typed by sorts; if the source names a "
                    "specific singleton agent/object, introduce a singleton "
                    "subsort (for example `sort SolactiveOrganization extends "
                    "Organization; entity Solactive : SolactiveOrganization`) "
                    "and use that sort as the parameter type."
                ),
            })
    return out


def _source_contract_triggers(entry_dir: pathlib.Path, bound: str) -> list[str]:
    triggers: list[str] = []
    seen: set[str] = set()
    for name in ("source.md", "normalized.md"):
        p = entry_dir / name
        if not p.exists():
            continue
        text = p.read_text(encoding="utf-8", errors="ignore")
        parts = re.split(r"(?<=[.!?])\s+|\n+", text)
        for part in parts:
            cleaned = " ".join(part.strip().split())
            if not cleaned:
                continue
            has_generic_top_k = SEMANTIC_CONTRACT_TRIGGER_RE.search(cleaned)
            has_bound_top_k = re.search(
                rf"\b(?:top|first|highest|lowest|largest|smallest|best)\s+{re.escape(bound)}\b",
                cleaned,
                re.IGNORECASE,
            )
            if has_generic_top_k or has_bound_top_k:
                if cleaned in seen:
                    continue
                seen.add(cleaned)
                triggers.append(cleaned)
    return triggers[:5]


def _selected_predicate_from_iff(body: str) -> str | None:
    m = re.search(
        r"\b([A-Za-z_][A-Za-z0-9_]*)\s*\([^)]*\)\s+iff\b",
        body,
        flags=re.IGNORECASE,
    )
    if not m:
        return None
    pred = m.group(1)
    pred_tokens = {_stem_token(t) for t in _tokens(pred)}
    if pred_tokens & {"select", "chosen", "choose", "inclusion", "component"}:
        return pred
    return None


def _has_cardinality_contract(blocks: list[dict[str, Any]],
                              selected_predicate: str,
                              bound: str) -> list[str]:
    hits: list[str] = []
    for block in blocks:
        if block["kind"] not in CLAIM_KINDS:
            continue
        body = re.sub(r"\s+", " ", block["body"])
        if "count" not in body or selected_predicate not in body:
            continue
        if re.search(rf"(?:<=|<)\s*{re.escape(bound)}\b", body):
            hits.append(block["name"])
    return hits


def _has_rank_uniqueness_contract(blocks: list[dict[str, Any]]) -> list[str]:
    hits: list[str] = []
    explicit_name_tokens = {
        "unique", "uniqueness", "injective", "injectivity", "tie",
        "ties", "tiebreak", "tiebreaker", "tie-break", "strict_total",
        "total_order",
    }
    for block in blocks:
        if block["kind"] not in CLAIM_KINDS:
            continue
        name_l = block["name"].lower()
        name_tokens = set(_tokens(block["name"]))
        body = re.sub(r"\s+", " ", block["body"])
        if "rank" not in body.lower() and "rank" not in name_tokens:
            continue
        if explicit_name_tokens & name_tokens or any(tok in name_l for tok in explicit_name_tokens):
            hits.append(block["name"])
            continue
        # Conservative structural fallback: rank equality implying object equality.
        if (
            "implies" in body
            and len(re.findall(r"\brank\s*\(", body)) >= 2
            and re.search(r"\b[A-Za-z_][A-Za-z0-9_]*\s*=\s*[A-Za-z_][A-Za-z0-9_]*\b", body)
        ):
            hits.append(block["name"])
    return hits


def _semantic_contract_gaps(entry_dir: pathlib.Path,
                            blocks: list[dict[str, Any]],
                            repair_blocks: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Detect hidden semantic contracts used by main IR.

    This is intentionally a general contract-gap layer. The first implemented
    detector is rank-cut selection cardinality, but the output shape is generic:
    contract_class, usage pattern, source trigger, main contract status, and
    repair overlay status.
    """
    out: list[dict[str, Any]] = []
    side_text = _entry_side_text(entry_dir).lower()
    notes_acknowledge_weakness = any(
        marker in side_text
        for marker in (
            "semantic contract", "contract gap", "derived invariant",
            "repair candidate", "repair.a4v3", "weak/ambiguous",
            "intentionally weak", "ambiguous",
        )
    )

    for block in blocks:
        if block["kind"] not in CLAIM_KINDS:
            continue
        body = re.sub(r"\s+", " ", block["body"])
        if "iff" not in body.lower() or "rank" not in body.lower():
            continue
        selected_predicate = _selected_predicate_from_iff(body)
        if not selected_predicate:
            continue
        cut = RANK_CUT_RE.search(body)
        if not cut:
            continue
        bound = cut.group("bound")
        op = cut.group("op")

        main_cardinality = _has_cardinality_contract(blocks, selected_predicate, bound)
        main_uniqueness = _has_rank_uniqueness_contract(blocks)
        main_contracts = sorted(set(main_cardinality + main_uniqueness))
        if main_contracts:
            continue

        repair_cardinality = _has_cardinality_contract(repair_blocks, selected_predicate, bound)
        repair_uniqueness = _has_rank_uniqueness_contract(repair_blocks)
        repair_contracts = sorted(set(repair_cardinality + repair_uniqueness))
        has_repair = bool(repair_contracts)
        severity = "advisory" if has_repair else "strong"
        repair_status = "has_repair_candidate" if has_repair else "missing_repair_candidate"

        out.append({
            "check": "semantic_contract_gap",
            "severity": severity,
            "contract_class": "cardinality_contract",
            "usage_pattern": "rank_cut_selection",
            "claim_kind": block["kind"],
            "claim": block["name"],
            "line_no": block["line_no"],
            "symbol": selected_predicate,
            "usage": f"{selected_predicate}(...) iff ... rank(...) {op} {bound}",
            "source_triggers": _source_contract_triggers(entry_dir, bound),
            "missing_in_main": [
                "top-k cardinality guard",
                "rank uniqueness or tie-break contract",
            ],
            "main_contract_status": "missing",
            "repair_status": repair_status,
            "repair_candidates": repair_contracts,
            "notes_acknowledge_weakness": notes_acknowledge_weakness,
            "reason": (
                "The main IR selects by a rank cutoff, which relies on a hidden "
                "top-k/cardinality contract. Without a cardinality guard or rank "
                "uniqueness/tie-break contract, a backend can assign the same rank "
                "to many objects and still satisfy the rank cutoff."
            ),
        })
    return out


def _annotate_contract_classes(findings: list[dict[str, Any]]) -> None:
    """Attach general contract-class labels to semantic-smell findings.

    `semantic_contract_gap` findings set their own class at the usage detector.
    Older deterministic checks are kept as stable check names, but exposing the
    class lets reports group them under the same general contract-gap taxonomy.
    """
    for finding in findings:
        if finding.get("contract_class"):
            continue
        contract_class = CHECK_CONTRACT_CLASS.get(finding.get("check", ""))
        if contract_class:
            finding["contract_class"] = contract_class


def analyze_entry(entry_dir: pathlib.Path) -> dict[str, Any]:
    a4v3_p = entry_dir / "main_ir.a4v3"
    if not a4v3_p.exists():
        return {"entry_id": entry_dir.name, "skipped": True, "reason": "no main_ir.a4v3"}

    text = a4v3_p.read_text(encoding="utf-8")
    blocks = _parse_blocks(text)
    repair_p = entry_dir / "repair.a4v3"
    repair_blocks = _parse_blocks(repair_p.read_text(encoding="utf-8")) if repair_p.exists() else []
    findings: list[dict[str, Any]] = []
    findings.extend(_unused_declarations(blocks))
    findings.extend(_arity_findings(entry_dir, blocks))
    findings.extend(_sentence_literals_in_formula(blocks))
    findings.extend(_self_referential_scope(blocks))
    findings.extend(_past_participle_obligation_names(blocks))
    findings.extend(_double_coded_deontic_norms(blocks))
    findings.extend(_temporal_rel_in_deontic_context(blocks))
    findings.extend(_vacuous_responsibility_constraints(blocks))
    findings.extend(_bare_universal_predicate_constraints(blocks))
    findings.extend(_fact_like_universal_constraints(blocks))
    findings.extend(_numeric_operation_on_non_numeric_sort(blocks))
    findings.extend(_basis_relation_without_value_link(blocks))
    findings.extend(_shared_name_token_without_structural_carrier(blocks))
    findings.extend(_permission_source_asserts_concrete_event_instance(entry_dir, blocks))
    findings.extend(_deontic_role_parameter_not_bound(blocks))
    findings.extend(_deontic_parameter_type_is_entity(blocks))
    findings.extend(_missing_instance_layer_for_referenceable_category(blocks))
    findings.extend(_redundant_entity_shadowing_sort(blocks))
    findings.extend(_semantic_contract_gaps(entry_dir, blocks, repair_blocks))
    _annotate_contract_classes(findings)

    by_check = Counter(f["check"] for f in findings)
    by_severity = Counter(f["severity"] for f in findings)
    by_contract_class = Counter(
        f["contract_class"] for f in findings if f.get("contract_class")
    )
    unused_by_kind = Counter(f.get("decl_kind") for f in findings if f["check"] == "unused_declaration")

    return {
        "entry_id": entry_dir.name,
        "skipped": False,
        "schema": "a4v3_semantic_lint_v1",
        "summary": {
            "total_findings": len(findings),
            "strong_findings": by_severity.get("strong", 0),
            "soft_findings": by_severity.get("soft", 0),
            "style_findings": by_severity.get("style", 0),
            "advisory_findings": by_severity.get("advisory", 0),
            "unused_declaration_count": by_check.get("unused_declaration", 0),
            "arity_gt_5_count": by_check.get("relation_or_function_arity_gt_5", 0),
            "arity_gt_2_without_role_explanation_count": by_check.get(
                "relation_or_function_arity_gt_2_without_role_explanation", 0
            ),
            "sentence_literal_in_formula_count": by_check.get("sentence_literal_in_formula", 0),
            "permission_source_asserts_concrete_event_instance_count": by_check.get(
                "permission_source_asserts_concrete_event_instance", 0
            ),
            "deontic_role_parameter_not_bound_count": by_check.get(
                "deontic_role_parameter_not_bound", 0
            ),
            "deontic_parameter_type_is_entity_count": by_check.get(
                "deontic_parameter_type_is_entity", 0
            ),
            "missing_instance_layer_for_referenceable_category_count": by_check.get(
                "missing_instance_layer_for_referenceable_category", 0
            ),
            "redundant_entity_shadowing_sort_count": by_check.get(
                "redundant_entity_shadowing_sort", 0
            ),
            "unused_rel_fun_count": sum(
                1
                for f in findings
                if f["check"] == "unused_declaration" and f.get("decl_kind") in {"rel", "fun"}
            ),
            "unused_sort_entity_count": sum(
                1
                for f in findings
                if f["check"] == "unused_declaration" and f.get("decl_kind") in {"sort", "entity", "val"}
            ),
            "self_referential_scope_count": by_check.get("self_referential_deontic_scope", 0),
            "past_participle_obligation_name_count": by_check.get("past_participle_obligation_name", 0),
            "double_coded_deontic_norm_count": by_check.get("possible_double_coded_deontic_norm", 0),
            "temporal_rel_in_deontic_context_count": by_check.get("temporal_rel_in_deontic_context", 0),
            "vacuous_responsibility_implication_count": by_check.get("vacuous_responsibility_implication", 0),
            "bare_universal_predicate_constraint_count": by_check.get("bare_universal_predicate_constraint", 0),
            "fact_like_universal_constraint_count": by_check.get("fact_like_universal_constraint", 0),
            "numeric_operation_on_non_numeric_sort_count": by_check.get("numeric_operation_on_non_numeric_sort", 0),
            "basis_relation_without_value_link_count": by_check.get("basis_relation_without_value_link", 0),
            "shared_name_token_without_structural_carrier_count": by_check.get("shared_name_token_without_structural_carrier", 0),
            "semantic_contract_gap_count": by_check.get("semantic_contract_gap", 0),
            "semantic_contract_gap_strong_count": sum(
                1
                for f in findings
                if f["check"] == "semantic_contract_gap" and f.get("severity") == "strong"
            ),
            "repair_candidate_present_count": sum(
                1
                for f in findings
                if f["check"] == "semantic_contract_gap"
                and f.get("repair_status") == "has_repair_candidate"
            ),
            "top_k_contract_gap_count": sum(
                1
                for f in findings
                if f["check"] == "semantic_contract_gap"
                and f.get("usage_pattern") == "rank_cut_selection"
            ),
            "by_contract_class": dict(by_contract_class),
        },
        "by_check": dict(by_check),
        "by_severity": dict(by_severity),
        "by_contract_class": dict(by_contract_class),
        "unused_by_decl_kind": {k: v for k, v in unused_by_kind.items() if k},
        "findings": findings,
    }


def _md_entry(result: dict[str, Any]) -> str:
    if result.get("skipped"):
        return f"# A4V3 Semantic Lint: {result.get('entry_id')}\n\nSkipped: {result.get('reason')}\n"
    s = result["summary"]
    lines = [
        f"# A4V3 Semantic Lint: {result['entry_id']}",
        "",
        f"- total_findings: `{s['total_findings']}`",
        f"- strong/soft/style/advisory: `{s['strong_findings']}` / `{s['soft_findings']}` / `{s['style_findings']}` / `{s['advisory_findings']}`",
        f"- unused rel/fun: `{s['unused_rel_fun_count']}`",
        f"- arity > 5 hard findings: `{s.get('arity_gt_5_count', 0)}`",
        f"- arity > 2 without role explanation: `{s.get('arity_gt_2_without_role_explanation_count', 0)}`",
        f"- sentence-like literals in formula bodies: `{s.get('sentence_literal_in_formula_count', 0)}`",
        f"- permission source asserts concrete event instances: `{s.get('permission_source_asserts_concrete_event_instance_count', 0)}`",
        f"- unbound deontic role parameters: `{s.get('deontic_role_parameter_not_bound_count', 0)}`",
        f"- deontic parameters typed by entities: `{s.get('deontic_parameter_type_is_entity_count', 0)}`",
        f"- self-referential deontic scope: `{s['self_referential_scope_count']}`",
        f"- possible double-coded deontic norms: `{s['double_coded_deontic_norm_count']}`",
        f"- vacuous responsibility implications: `{s['vacuous_responsibility_implication_count']}`",
        f"- bare universal predicate constraints: `{s['bare_universal_predicate_constraint_count']}`",
        f"- fact-like universal constraints: `{s['fact_like_universal_constraint_count']}`",
        f"- numeric operations on non-numeric sorts: `{s['numeric_operation_on_non_numeric_sort_count']}`",
        f"- based-on claims without value link: `{s['basis_relation_without_value_link_count']}`",
        f"- shared name tokens without structural carrier: `{s['shared_name_token_without_structural_carrier_count']}`",
        f"- semantic contract gaps: `{s.get('semantic_contract_gap_count', 0)}` "
        f"(strong `{s.get('semantic_contract_gap_strong_count', 0)}`, "
        f"repair candidates `{s.get('repair_candidate_present_count', 0)}`)",
        f"- contract classes: `{json.dumps(s.get('by_contract_class', {}), ensure_ascii=False)}`",
        "",
    ]
    if not result["findings"]:
        lines.append("No semantic-lint findings.")
        lines.append("")
        return "\n".join(lines)

    lines.extend(["## Findings", ""])
    for f in result["findings"]:
        subject = f.get("symbol") or f.get("constraint") or f.get("deontic_decl") or f.get("claim") or "?"
        lines.append(f"### `{f['check']}` / `{subject}`")
        lines.append("")
        lines.append(f"- severity: `{f.get('severity')}`")
        if f.get("line_no"):
            lines.append(f"- line: `{f['line_no']}`")
        if f.get("reason"):
            lines.append(f"- reason: {f['reason']}")
        if f.get("contract_class"):
            lines.append(f"- contract_class: `{f['contract_class']}`")
        if f.get("usage"):
            lines.append(f"- usage: `{f['usage']}`")
        if f.get("repair_status"):
            lines.append(f"- repair_status: `{f['repair_status']}`")
        if f.get("repair_candidates"):
            lines.append(f"- repair_candidates: `{', '.join(f['repair_candidates'])}`")
        if f.get("source_triggers"):
            lines.append("- source_triggers:")
            for trigger in f["source_triggers"]:
                lines.append(f"  - {trigger}")
        if f.get("raw_decl"):
            lines.append(f"- raw: `{f['raw_decl']}`")
        lines.append("")
    return "\n".join(lines)


def _save_entry(entry_dir: pathlib.Path, result: dict[str, Any]) -> pathlib.Path:
    json_p = entry_dir / "a4v3_semantic_lint_v1.json"
    md_p = entry_dir / "a4v3_semantic_lint_v1.md"
    json_p.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    md_p.write_text(_md_entry(result), encoding="utf-8")
    return json_p


def aggregate(run_root: pathlib.Path) -> dict[str, Any]:
    entries: list[dict[str, Any]] = []
    for a4v3 in sorted(run_root.rglob("main_ir.a4v3")):
        if any(part.startswith("_") for part in a4v3.parts):
            continue
        entries.append(analyze_entry(a4v3.parent))

    by_check: Counter = Counter()
    by_contract_class: Counter = Counter()
    by_entry: dict[str, dict[str, Any]] = {}
    for result in entries:
        if result.get("skipped"):
            continue
        by_check.update(result.get("by_check") or {})
        by_contract_class.update(result.get("by_contract_class") or {})
        by_entry[result["entry_id"]] = result["summary"]

    return {
        "run": run_root.name,
        "schema": "a4v3_semantic_lint_corpus_v1",
        "n_entries": len([e for e in entries if not e.get("skipped")]),
        "total_findings": sum((e.get("summary") or {}).get("total_findings", 0) for e in entries),
        "by_check": dict(by_check),
        "by_contract_class": dict(by_contract_class),
        "entries": by_entry,
    }


def main() -> None:
    target = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "case_studies/financial_methodology"
    if (target / "main_ir.a4v3").exists():
        result = analyze_entry(target)
        out = _save_entry(target, result)
        print(f"Wrote {out}")
        if not result.get("skipped"):
            print(f"  findings: {result['summary']['total_findings']}")
            print(f"  by_check: {result['by_check']}")
        return

    n = 0
    for a4v3 in sorted(target.rglob("main_ir.a4v3")):
        if any(part.startswith("_") for part in a4v3.parts):
            continue
        result = analyze_entry(a4v3.parent)
        _save_entry(a4v3.parent, result)
        n += 1

    agg = aggregate(target)
    json_p = target / "a4v3_semantic_lint_corpus_report_v1.json"
    json_p.write_text(json.dumps(agg, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {json_p}")
    print(f"  entries: {n}")
    print(f"  total findings: {agg['total_findings']}")
    print(f"  by_check: {agg['by_check']}")


if __name__ == "__main__":
    main()
