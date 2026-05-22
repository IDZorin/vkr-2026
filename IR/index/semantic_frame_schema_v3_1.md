# Semantic Frame Schema v3.1

Purpose: provide a stable intermediate layer between natural-language source
and A4V3 IR. Frames are a reviewable claim ledger — they make roles, polarity,
modality, scope, numbers, references, and exceptions explicit before comparing
source to IR. Frames are not a replacement for IR; they are a bridge to it.

## Changes from v2

| Area | v3.1 decision |
|---|---|
| Lifecycle vs coverage | `draft`, `aligned`, and `verified` are separated from `coverage`; draft frames may be expected-exact without IR links. |
| IR alignment | `predicate.ir_ref` and `ir_alignment` are required only for aligned/verified exact-or-weak frames. |
| Predicate shape | `predicate` is always `{name, source_span, ir_ref}`; `name` is an identifier, not prose. |
| Slot strictness | Structural slot objects are mandatory only after alignment/verification; draft extraction may still be less rigid. |
| References | URL references are first-class via `reference[].kind = "url"`. |
| Verification | `lifecycle = verified` is allowed only with `alignment_report.overall = "pass"`. |

---

## File Shape

```json
{
  "schema": "semantic_frames_v3_1",
  "entry_id": "section_5_4",
  "source_path": "source.md",
  "frames": []
}
```

---

## Frame Shape

```json
{
  "frame_id": "section_5_4.F01",
  "lifecycle": "draft",
  "source_span": "exact source phrase",
  "type": "assertion",
  "coverage": "exact",
  "polarity": "positive",
  "modality": "none",
  "subject": [],
  "predicate": {"name": "", "source_span": null, "ir_ref": null},
  "object": [],
  "condition": [],
  "consequent": [],
  "scope": [],
  "quantifier": "none",
  "connective": "none",
  "comparator": "none",
  "aggregate": "none",
  "temporal_operator": null,
  "value": null,
  "unit": null,
  "time": [],
  "reference": [],
  "exclusion": [],
  "qualifiers": [],
  "absorbed_into": null,
  "clarifies": null,
  "depends_on": [],
  "ir_alignment": [],
  "unsupported_reason": "",
  "notes": ""
}
```

---

## Fixed Enums

### `type`

Answers: **what does this frame assert?** Not how well it is covered, not how it
relates to other frames.

| Value | Use when |
|---|---|
| `declaration` | a symbol, sort, or entity is introduced |
| `definition` | a term is characterized or given meaning |
| `assertion` | an unconditional factual or constrained claim |
| `value_definition` | a numeric or categorical value is assigned |
| `value_dependency` | a value depends on another value or condition |
| `shared_condition` | a named, reused condition referenced by multiple frames (see anti-fragmentation rule) |
| `exception` | an exclusion, override, or fallback case |
| `procedure` | a named procedure is followed |
| `action_transition` | an explicit state transition with guard/effect |
| `temporal` | ordering, persistence, or trace semantics |
| `deontic` | obligation, permission, or prohibition |
| `validation` | shape, schema, or closed-world constraint |
| `probabilistic` | probability, reward, distribution, or objective |
| `graph` | dataset, reification, or triple-level semantics |
| `theorem` | a claim requiring proof or verification |
| `rule` | a general conditional formula or constraint involving multiple sub-claims |
| `reference` | document, URL, or section metadata |

### `type` decision tree

Use this tree when the boundary between similar values is unclear:

```
Source introduces a new symbol or category (no value/body given)?
  → declaration
  Example: "The Index has a Rebalance Day"

Source explains the meaning of a term?
  → definition
  Example: '"Trading Day" means a day on which the Exchange is open'

Source assigns a concrete value or computation rule to a term?
  → value_definition
  Example: "Rebalance Day is the third Friday in March, June, September, December"
  Note: even though it "defines" the term, it gives a specific rule for computing a date.

Source says a value depends on another value, but exact formula is absent?
  → value_dependency
  Example: "weight is based on Float Market Capitalization"
  Note: if an explicit formula is given (weight = FMC / totalFMC), use value_definition.

Source is a condition that is independently asserted and reused across multiple frames?
  → shared_condition  (see rule below)

Otherwise use the remaining types based on content:
  assertion / exception / procedure / action_transition / temporal /
  deontic / validation / probabilistic / graph / theorem / reference
```

### Rule for `type = shared_condition`

> **`type = shared_condition` is reserved for shared condition frames only.**

`type = shared_condition` is reserved for **shared condition frames** — conditions
that are explicitly stated in the source, cover a large span, and are
reused or clarified by multiple other frames.

Do NOT create a `shared_condition` frame for the antecedent of a single rule.
Put the condition in the `condition[]` slot of the `assertion` or
`action_transition` frame instead.

If a condition frame is genuinely shared, mark the frames that use it with
`depends_on: ["<condition_frame_id>"]`.

**Removed from v2**: `unsupported` → use `coverage: "unsupported"`. `vague` → use
`coverage: "ambiguous"`. `clarification` → use `clarifies: "<frame_id>"`.

### `coverage`

Answers: **how faithfully is this frame represented in IR?**

| coverage | `draft` meaning | `aligned` / `verified` meaning |
|---|---|---|
| `exact` | Expected to be fully formalizable without semantic loss | Fully represented in IR |
| `weak` | Expected to require approximation or partial formalization | Represented imprecisely or partially in IR |
| `metadata_only` | Expected to be preserved as provenance/metadata | Preserved as provenance/metadata; no logical formula |
| `absorbed` | Expected to be represented by another frame | Represented by another frame; `absorbed_into` set |
| `omitted_with_waiver` | Intentionally not modeled; `waiver_reason` set | Intentionally not modeled |
| `unsupported` | Expected to be unsupported by the target IR/backend | Unsupported by the target IR/backend; `unsupported_reason` set |
| `ambiguous` | Source meaning is ambiguous or unresolved | Source meaning remains ambiguous after alignment |

### `polarity`

`positive` · `negative` · `conditional` · `exception` · `counterfactual` · `mixed` · `unknown`

### `modality`

`none` · `must` · `may` · `cannot` · `should` · `responsible` · `intended` · `possible` · `defined_as` · `unknown`

### Semantic clue fields (replace `operator`)

These fields capture top-level semantic structure without building a full Formula AST.
The exact formula lives in A4V3/INNF, not in the frame.

| Field | Values |
|---|---|
| `quantifier` | `none` · `forall` · `exists` · `exactly_one` · `at_least` · `at_most` |
| `connective` | `none` · `and` · `or` · `implies` · `iff` · `not` |
| `comparator` | `none` · `=` · `!=` · `<` · `<=` · `>` · `>=` · `in` · `not_in` |
| `aggregate`  | `none` · `count` · `sum` · `min` · `max` |
| `temporal_operator` | `null` · `always` · `eventually` · `once` · `next` · `until` · `since` · `before` · `after` · `within` |

**Example**: "Each component weight is capped at 5%":
`quantifier=forall, comparator=<=, aggregate=none`

**Example**: "Each region must represent exactly 50%":
`quantifier=forall, comparator==, aggregate=sum`

**Example**: "redistributed until constraints are satisfied":
`type=temporal, temporal_operator=until`

---

## Slot Rules

### `reference`

Use for URLs, section references, document names, external policies, and
incorporated-by-reference relations.

Allowed `kind` values: `internal_section` · `external_source` · `url` ·
`regulation` · `standard` · `guideline` · `previous_version` · `methodology` · `policy`

```json
"reference": [
  {"kind": "url", "target": "https://example.com/methodology.pdf"},
  {"kind": "internal_section", "target": "Section 5.2 Methodology Review"}
]
```

### Slot object schema

All structural array slots accept either a plain string or a **slot object**.

```json
{
  "role": "agent",
  "value": "Pasha",
  "source_span": "Паша",
  "derived": false,
  "derivation_rule": null,
  "derivation_target": null,
  "derivation_source": null
}
```

**`derived` is required** (no implicit default). If absent, the validator rejects the slot.

**`role` enum:**
`agent` · `patient` · `object` · `subject` · `defined_term` · `value` · `basis` ·
`source_value` · `target_value` · `condition` · `exception` · `scope` · `time` ·
`threshold` · `unit` · `comparator` · `process` · `step` · `stop_condition` ·
`result` · `authority` · `beneficiary` · `unknown`

`unknown` is only allowed when `coverage = ambiguous`.

**Evidence rules** (enforced by schema):
- `derived = false` → `source_span` required (non-empty string).
- `derived = true` → `derivation_rule` required (non-null enum value).

**`derivation_rule` enum:**

| Value | When to use |
|---|---|
| `from_section_header` | value implied by enclosing section title |
| `from_table_header` | value implied by table column/row header |
| `from_list_context` | value implied by list structure |
| `from_domain_ontology` | value from external domain knowledge (FIBO etc.) |
| `from_defined_term` | value from a term defined earlier in same document |
| `from_implicit_quantification` | quantifier not stated but implied by context |
| `from_default_unit` | unit not stated; taken from document-wide default |
| `from_modeling_convention` | standard modeling assumption (e.g. open-world) |
| `from_coreference` | value resolved from a coreference (pronoun, ellipsis) |
| `from_abbreviation_expansion` | abbreviation expanded by lookup |
| `from_backend_requirement` | value required by specific backend lowering |

`derivation_target`: what entity/slot is being derived (e.g. `"SelectionDay"`).
`derivation_source`: frame_id or span where the derivation basis was found.

### Role-critical vs metadata slots

**Structural slots** (`subject`, `object`, `condition`, `consequent`):
when `lifecycle ∈ {aligned, verified}` and `coverage = exact` or `weak`,
these **must** use slot objects. Plain strings are rejected by the schema validator.
For `lifecycle = draft`, slot objects are strongly preferred, but the schema still
allows plain strings while the extractor is only drafting source claims.

**Metadata slots** (`scope`, `time`, `exclusion`, `qualifiers`):
plain strings are allowed even when an aligned/verified frame has `coverage = exact`
or `weak`. Use slot objects there when role traceability matters (e.g. a scope
that disambiguates an agent).


### Field evidence for derived scalar fields

Frame-level scalar fields (`quantifier`, `connective`, `comparator`, `aggregate`,
`temporal_operator`, `value`, `unit`, `modality`, `polarity`) may be semantically
derived from source wording rather than copied verbatim.

When a scalar field value is inferred rather than read directly, add an entry to
`field_evidence`:

```json
"comparator": "<=",
"field_evidence": [
  {
    "field": "comparator",
    "value": "<=",
    "source_span": "capped at",
    "derived": true,
    "derivation_rule": "from_modeling_convention"
  }
]
```

This preserves auditability without converting scalar fields into a second Formula AST.
`field_evidence` is optional; populate it whenever a scalar assignment would otherwise
be untraced.

### Scalar value vs threshold slot

When a number is the **main asserted bound** of a rule, use a slot object
with `role = threshold` plus `unit` at frame level:

```json
"object": [
  {
    "role": "threshold",
    "value": 5,
    "source_span": "5%",
    "derived": false,
    "derivation_rule": null,
    "derivation_target": null,
    "derivation_source": null
  }
],
"unit": "%"
```

When a number is the **only scalar value of the whole frame** (not a bound
within a relational claim), use `value` / `unit` directly:

```json
"value": 100,
"unit": null
```

Rule: "component weight is capped at 5%" → `object[role=threshold]`.
Rule: "Index level is 100" → `value = 100`.

## Predicate Field


`predicate` is always an object with three fields:

```json
{
  "name": "single_component_weight_cap",
  "source_span": "capped at",
  "ir_ref": "AssertDecl.single_component_weight_cap"
}
```

In `lifecycle = draft`: `predicate.ir_ref` may be `null`.

In `lifecycle = aligned` or `verified` with `coverage = exact` or `weak`:
`predicate.ir_ref` must be non-null and must match one of `ir_alignment[*].ir_ref`.
This cross-field equality is enforced by the custom consistency validator.

`ir_ref` format: `INNFFamily.camelCaseName` (e.g. `SymbolDecl.rebalanceDay`,
`AssertDecl.weightCap`). Validated by pattern in `$defs/ir_ref`.

---

## Frame-to-Frame Relations

These are first-class fields, not prose in `notes`.

| Field | Type | Meaning |
|---|---|---|
| `absorbed_into` | `string \| null` | frame_id this frame is merged into |
| `clarifies` | `string \| null` | frame_id this frame is an explanatory qualification of |
| `depends_on` | `string[]` | frame_ids whose claims this frame presupposes |

**Rules:**
- `coverage = absorbed` → `absorbed_into` must be non-null.
- `absorbed_into` must reference an existing `frame_id` in the same document.
- No absorption cycles: A absorbed_into B absorbed_into A is invalid.
- `depends_on` must not reference non-existent frame_ids.

**Implied rule**: `clarifies(X)` implies `depends_on(X)` automatically.
Annotators should set `clarifies` when applicable; validators/normalizers
add `X` to `depends_on` if not already present.
Do not manually duplicate: if `clarifies: "F01"`, add `"F01"` to `depends_on`
only to be explicit — the normalizer handles it otherwise.

---

## Schema Enforcement Rules

Enforced by `allOf/if/then` in the JSON Schema validator:

1. `lifecycle ∈ {aligned, verified}` and `coverage = exact/weak` → `ir_alignment` non-empty
2. `coverage = unsupported` → `unsupported_reason` non-empty
3. `coverage = absorbed` → `absorbed_into` non-null, non-empty string
4. `lifecycle ∈ {aligned, verified}` and `coverage = exact/weak` and `type ≠ declaration` → `predicate` must be aligned object with `ir_ref`
5. `lifecycle ∈ {aligned, verified}` and `coverage = exact/weak` → `subject`, `object`, `condition`, `consequent` must use slot objects
6. `role = unknown` only allowed when `coverage = ambiguous`
7. Slot object `derived` is required; `derived = false` → `source_span` required; `derived = true` → `derivation_rule` required (non-null)


### Consistency rules (enforced by external validator, not JSON Schema)

The following cannot be enforced inside JSON Schema 2020-12 but must be
checked by a separate consistency validator after schema validation:

- `predicate.ir_ref` must equal one of `ir_alignment[*].ir_ref`
- `absorbed_into` must reference an existing `frame_id` in same document
- `clarifies` must reference an existing `frame_id` in same document
- `depends_on[*]` must reference existing `frame_id` values
- No absorption cycles (absorbed_into chains must be acyclic)
- `derivation_rule = from_domain_ontology` → `derivation_source` must be set
- `clarifies(X)` → `X` must be present in `depends_on` (normalizer may add automatically)



---

## IR Reference Naming Convention

`ir_ref` has the form:

```
INNFFamily.ir_identifier
```

The first segment is the INNF family name in CamelCase:
`TypeDecl` · `SymbolDecl` · `AssertDecl` · `PathDecl` · `ActionDecl` ·
`TemporalDecl` · `DeonticDecl` · `ValidationDecl` · `ProbabilisticDecl` ·
`GameDecl` · `GraphDecl` · `TheoremDecl`

The second segment is the declared A4V3 identifier.

Recommended naming:
- Types, sorts, entities: `PascalCase` (e.g. `TypeDecl.SelectionDay`)
- Functions, relations, predicates, facts, constraints: `snake_case`

Examples:
```
TypeDecl.SelectionDay
SymbolDecl.weight
AssertDecl.single_component_weight_cap
TemporalDecl.redistribution_until_satisfied
```


---

## Anti-fragmentation Rule for Shared Conditions

> **`type = shared_condition` is reserved for shared condition frames only.**

Use `type = shared_condition` only when the condition is independently named,
reused, clarified, or referenced by multiple frames.

The antecedent of a single rule belongs in the `condition[]` slot of the parent
frame, not as its own frame.

**Default when unsure: do not create a shared_condition frame.**

---

## Custom Consistency Validator

JSON Schema validates local structure. The following checks require a second-pass validator.

### 1. IR reference consistency

For every frame where `predicate.ir_ref != null`:
`predicate.ir_ref` must be present in `ir_alignment[*].ir_ref`.

### 2. IR reference existence

Every `ir_alignment[*].ir_ref` must point to an existing A4V3/INNF declaration
in the target IR document.

### 3. Frame graph consistency

- `absorbed_into` must reference an existing `frame_id` in the same document.
- `clarifies` must reference an existing `frame_id`.
- Every entry in `depends_on` must reference an existing `frame_id`.
- `absorbed_into` chains must be acyclic.
- `depends_on` chains must be acyclic (except explicitly marked mutual-clarification groups).

### 4. Unknown role rule

`role = unknown` in any slot object is allowed only when `coverage = ambiguous`.

### 5. Verified lifecycle rule

A frame may have `lifecycle = verified` only if `alignment_report.overall = pass`.
The verifier (not the LLM) sets this field.

### 6. Clarifies implies depends_on

If `clarifies = X`, then `X` must appear in `depends_on`.
The normalizer may add this automatically; annotators should not duplicate manually.

---

## Role-Position Alignment Algorithm

This algorithm verifies that frame slots correctly map to IR argument positions.
It answers the "Паша кормил Машу vs Маша кормила Пашу" problem formally.

### Inputs
- A frame with `coverage = exact` or `weak`
- The IR block referenced by each `ir_alignment` entry

### Steps

**Step 1. Resolve IR signature.**
For each `ir_alignment` entry, find the referenced IR declaration (e.g.
`SymbolDecl.fed` with `rel fed : agent: Person, patient: Person`).
Extract the argument-role map: `{pos_0: "agent", pos_1: "patient"}`.

**Step 2. Map frame slots to IR positions.**
For each IR argument position, find the corresponding slot object in `subject`,
`object`, or named slot where `role` matches the IR argument role.

```
IR:    rel fed(agent: Person, patient: Person)
Frame: subject[0].role = "agent",  value = "Pasha"
       object[0].role  = "patient", value = "Masha"
Check: fed(Pasha, Masha)  ✓
```

**Step 3. Check polarity and direction.**
If the frame has `polarity = negative`, verify the IR block encodes `not`.
If the frame has `connective = implies`, verify the IR block uses an implication
or conditional form, not a bare assertion.

**Step 4. Check evidence completeness.**
For every slot object used in Step 2:
- If `derived = false`: verify `source_span` is a substring of the frame's `source_span`.
- If `derived = true`: verify `derivation_rule` is set and `derivation_target` or
  `derivation_source` explains the inference.

**Step 5. Check for extra IR claims.**
For each IR block in `ir_alignment`, verify that every IR argument either has a
matching slot object in the frame, or is documented as derived with a `derivation_rule`.
No IR argument should be silent (neither sourced nor derived).

**Step 6. Report.**
If all checks pass: alignment is `exact`.
If Steps 2–3 pass but Step 4 has weak evidence: downgrade to `weak`.
If Step 2 fails (role mismatch or direction reversal): flag as `misaligned`.

---

## Completeness Criteria

An entry is frame-complete when:

- every source claim is covered by at least one frame
- every frame has `type`, `coverage`, `polarity`, `modality`
- every frame with `lifecycle ∈ {aligned, verified}` and `coverage ∈ {exact, weak}` has non-empty `ir_alignment`
- frames with `lifecycle = draft` and `coverage = exact/weak` may have empty `ir_alignment`
- every frame with `lifecycle ∈ {aligned, verified}` and `coverage ∈ {exact, weak}` uses slot objects in structural slots
- every frame with `coverage = unsupported` has `unsupported_reason`
- every frame with `coverage = absorbed` has `absorbed_into`
- no slot object uses `role = unknown` unless `coverage = ambiguous`
- every slot object with `derived = false` has a non-null `source_span`
- every slot object with `derived = true` has a `derivation_rule`
- every `verified` frame has `alignment_report.overall = pass`
- no custom top-level keys

---

## A4V3 / INNF Coverage Mapping

| INNF family | Frame type | Required frame slots |
|---|---|---|
| TypeDecl | `declaration` | `subject`, `predicate` |
| SymbolDecl (entity) | `definition` | `subject`, `predicate` |
| SymbolDecl (rel/fun) | `definition` | `predicate`, `subject`, `object` |
| AssertDecl (fact) | `assertion` | `subject`, `predicate`, `object` |
| AssertDecl (constraint) | `assertion` | `condition`, `consequent`, `comparator` |
| PathDecl | `reference` | `subject`, `predicate`, `object` |
| ActionDecl | `action_transition` | `subject`, `predicate`, `condition`, `consequent` |
| TemporalDecl | `temporal` | `predicate`, `temporal_operator`, `time` |
| DeonticDecl | `deontic` | `subject`, `predicate`, `object`, `modality` |
| ValidationDecl | `validation` | `subject`, `predicate`, `condition` |
| ProbabilisticDecl | `probabilistic` | `subject`, `predicate`, `value` |
| GameDecl | `game` | `subject`, `predicate`, `object` |
| GraphDecl | `graph` | `subject`, `predicate`, `object` |
| TheoremDecl | `theorem` | `condition`, `consequent` |

---

## Example: Rebalance Day

```json
{
  "frame_id": "N42.F01",
  "source_span": "REBALANCE DAY is the third Friday in March, June, September and December",
  "type": "definition",
  "coverage": "exact",
  "polarity": "positive",
  "modality": "defined_as",
  "subject": [
    {
      "role": "defined_term",
      "value": "REBALANCE DAY",
      "source_span": "REBALANCE DAY",
      "derived": false,
      "derivation_rule": null,
      "derivation_target": null,
      "derivation_source": null
    }
  ],
  "predicate": {
    "name": "defined_as",
    "source_span": "is",
    "ir_ref": "SymbolDecl.rebalanceDay"
  },
  "object": [
    {
      "role": "value",
      "value": "third Friday",
      "source_span": "third Friday",
      "derived": false,
      "derivation_rule": null,
      "derivation_target": null,
      "derivation_source": null
    }
  ],
  "condition": [],
  "consequent": [],
  "scope": ["March", "June", "September", "December"],
  "quantifier": "none",
  "connective": "none",
  "comparator": "none",
  "aggregate": "none",
  "temporal_operator": null,
  "value": null,
  "unit": null,
  "time": [],
  "reference": [],
  "exclusion": [],
  "qualifiers": [],
  "absorbed_into": null,
  "clarifies": null,
  "depends_on": [],
  "ir_alignment": [
    {
      "kind": "fun",
      "name": "rebalanceDay",
      "role": "main_definition",
      "innf_family": "SymbolDecl"
    }
  ],
  "unsupported_reason": "",
  "notes": ""
}
```

```json
{
  "frame_id": "N42.F02",
  "source_span": "If that day is not a trading day, the REBALANCE DAY will be the immediately following trading day",
  "type": "exception",
  "coverage": "exact",
  "polarity": "conditional",
  "modality": "none",
  "subject": [
    {
      "role": "defined_term",
      "value": "REBALANCE DAY",
      "source_span": "REBALANCE DAY",
      "derived": false,
      "derivation_rule": null,
      "derivation_target": null,
      "derivation_source": null
    }
  ],
  "predicate": {
    "name": "adjusted_to",
    "source_span": "will be",
    "ir_ref": "AssertDecl.rebalanceDayAdjustmentRule"
  },
  "object": [
    {
      "role": "target_value",
      "value": "immediately following trading day",
      "source_span": "immediately following trading day",
      "derived": false,
      "derivation_rule": null,
      "derivation_target": null,
      "derivation_source": null
    }
  ],
  "condition": [
    {
      "role": "condition",
      "value": "day is not a trading day",
      "source_span": "that day is not a trading day",
      "derived": false,
      "derivation_rule": null,
      "derivation_target": null,
      "derivation_source": null
    }
  ],
  "consequent": [],
  "scope": [],
  "quantifier": "none",
  "connective": "none",
  "comparator": "none",
  "aggregate": "none",
  "temporal_operator": null,
  "value": null,
  "unit": null,
  "time": [],
  "reference": [],
  "exclusion": [],
  "qualifiers": [],
  "absorbed_into": null,
  "clarifies": "N42.F01",
  "depends_on": ["N42.F01"],
  "ir_alignment": [
    {
      "kind": "fun",
      "name": "rebalanceDay",
      "role": "fallback_branch",
      "innf_family": "SymbolDecl"
    },
    {
      "kind": "fact",
      "name": "rebalanceDayAdjustmentRule",
      "role": "conditional_formula",
      "innf_family": "AssertDecl"
    }
  ],
  "unsupported_reason": "",
  "notes": "ITE in SymbolDecl body: if isTradingDay(thirdFriday(e)) then thirdFriday(e) else nextTradingDay(thirdFriday(e))"
}
```

---


---

## Lifecycle vs Coverage

`coverage` and `lifecycle` are orthogonal axes. Do not conflate them.

| Field | Question answered |
|---|---|
| `coverage` | How faithfully is this frame represented in IR? |
| `lifecycle` | What pipeline stage has this frame reached? |

### Lifecycle values

| `lifecycle` | Meaning |
|---|---|
| `draft` | Extracted from source text. IR alignment may not exist yet. `predicate.ir_ref` may be null. `ir_alignment` may be empty. |
| `aligned` | Linked to A4V3/INNF via `predicate.ir_ref` and `ir_alignment`. For `coverage = exact/weak`, both must be non-null/non-empty. |
| `verified` | Passed role-position, source-evidence, and no-extra-claim checks. `alignment_report` must be attached and `overall = pass`. |

### Valid combinations

```
lifecycle=draft,    coverage=exact      → source is clear and expected to be exactly expressible;
                                           "exact" here means expected expressibility, not already represented; IR not linked yet
lifecycle=draft,    coverage=ambiguous  → unclear source, extraction in progress
lifecycle=aligned,  coverage=exact      → linked to IR, alignment not yet checked
lifecycle=aligned,  coverage=weak       → linked but mapping is approximate
lifecycle=verified, coverage=exact      → fully verified, clean alignment
lifecycle=verified, coverage=weak       → verified but weak mapping is documented
```

`lifecycle = verified` is set only by the validator after `alignment_report.overall = pass`.
It must **never** be set by the LLM extractor.

## Recommended Pipeline

1. **Source text segmentation**
   Split source into logical passages (one rule/definition per passage).

2. **Draft semantic frame extraction**
   Extract frames with `lifecycle = draft`.
   Source evidence required (`source_span`, slot `derived` fields).
   `predicate.ir_ref = null` and `ir_alignment = []` are acceptable.
   Set `coverage` based on expected IR expressibility.

3. **A4V3 authoring IR generation**
   Produce IR blocks from source using the ACG → INNF pipeline.

4. **INNF normalization**
   Lower authoring IR to INNF canonical form.

5. **Frame alignment**
   Fill `predicate.ir_ref` pointing to INNF block.
   Fill `ir_alignment` items with `ir_ref`, `kind`, `name`, `innf_family`, `role`.
   Set `lifecycle = aligned`.

6. **Consistency validation** (6 checks)
   a. JSON Schema validation against `semantic_frame_schema_v3_1.json`
   b. IR reference existence: every `ir_alignment[*].ir_ref` maps to a real INNF block
   c. Predicate consistency: `predicate.ir_ref ∈ ir_alignment[*].ir_ref`
   d. Frame graph: `absorbed_into`, `clarifies`, `depends_on` reference existing `frame_id` values; no absorption cycles
   e. Role-position alignment algorithm (see below)
   f. Source evidence check: every slot with `derived = false` has traceable `source_span`

7. **Verification finalization**
   Attach `alignment_report` with per-check pass/fail.
   Set `lifecycle = verified` only if `alignment_report.overall = pass`.
   Frames with `coverage = weak` or `ambiguous` require human review before `verified`.

---

## Example: Draft vs Aligned Frame

### Draft (lifecycle = draft)

```json
{
  "frame_id": "W.F03",
  "lifecycle": "draft",
  "type": "assertion",
  "coverage": "exact",
  "source_span": "The weight of any single Index Component is capped at 5%.",
  "polarity": "positive",
  "modality": "none",
  "predicate": {
    "name": "capped_at",
    "source_span": "capped at",
    "ir_ref": null
  },
  "subject": [
    {"role": "defined_term", "value": "weight", "source_span": "weight", "derived": false, "derivation_rule": null, "derivation_target": null, "derivation_source": null},
    {"role": "scope", "value": "any single Index Component", "source_span": "any single Index Component", "derived": false, "derivation_rule": null, "derivation_target": null, "derivation_source": null}
  ],
  "object": [
    {"role": "threshold", "value": "5%", "source_span": "5%", "derived": false, "derivation_rule": null, "derivation_target": null, "derivation_source": null}
  ],
  "condition": [], "consequent": [], "scope": [],
  "quantifier": "forall", "connective": "none", "comparator": "<=", "aggregate": "none",
  "temporal_operator": null, "value": null, "unit": "%",
  "time": [], "reference": [], "exclusion": [], "qualifiers": [],
  "absorbed_into": null, "clarifies": null, "depends_on": [],
  "ir_alignment": [],
  "unsupported_reason": "", "notes": ""
}
```

### Aligned (lifecycle = aligned)

```json
{
  "frame_id": "W.F03",
  "lifecycle": "aligned",
  "type": "assertion",
  "coverage": "exact",
  "source_span": "The weight of any single Index Component is capped at 5%.",
  "polarity": "positive",
  "modality": "none",
  "predicate": {
    "name": "single_component_weight_cap",
    "source_span": "capped at",
    "ir_ref": "AssertDecl.single_component_weight_cap"
  },
  "subject": [
    {"role": "defined_term", "value": "weight", "source_span": "weight", "derived": false, "derivation_rule": null, "derivation_target": null, "derivation_source": null},
    {"role": "scope", "value": "any single Index Component", "source_span": "any single Index Component", "derived": false, "derivation_rule": null, "derivation_target": null, "derivation_source": null}
  ],
  "object": [
    {"role": "threshold", "value": "5%", "source_span": "5%", "derived": false, "derivation_rule": null, "derivation_target": null, "derivation_source": null}
  ],
  "condition": [], "consequent": [], "scope": [],
  "quantifier": "forall", "connective": "none", "comparator": "<=", "aggregate": "none",
  "temporal_operator": null, "value": null, "unit": "%",
  "time": [], "reference": [], "exclusion": [], "qualifiers": [],
  "absorbed_into": null, "clarifies": null, "depends_on": [],
  "ir_alignment": [
    {
      "ir_ref": "AssertDecl.single_component_weight_cap",
      "kind": "constraint",
      "name": "single_component_weight_cap",
      "innf_family": "AssertDecl",
      "role": "main_formula"
    }
  ],
  "unsupported_reason": "", "notes": ""
}
```
