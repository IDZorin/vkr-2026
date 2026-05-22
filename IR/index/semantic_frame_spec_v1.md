# Semantic Frame Spec v1

Purpose: provide a stable intermediate layer between natural-language source
and A4V3 IR. Frames are not a replacement for IR. They are a reviewable claim
ledger that makes roles, polarity, modality, scope, numbers, references, and
exceptions explicit before comparing source to IR.

## Core Idea

One source passage is decomposed into atomic semantic frames.

Each frame must receive one review outcome:

- `represented`: the frame is formalized in A4V3 and aligned to one or more IR blocks.
- `metadata`: the frame is preserved as provenance/reference/context but does not lower to a logical formula.
- `absorbed`: the frame is intentionally absorbed into another formal frame.
- `unsupported`: the frame cannot currently be represented by supported A4V3/backend semantics.
- `ambiguous`: the source is not precise enough to decide the intended formal meaning.

The goal is not to create many frames. The goal is to make every source claim
accounted for.

## File Shape

```json
{
  "schema": "semantic_frames_v1",
  "entry_id": "section_5_4",
  "source_path": "source.md",
  "frames": []
}
```

## Frame Shape

Every frame uses the same top-level keys. Do not invent new top-level keys.
If a value does not fit a dedicated slot, put it in `qualifiers`, `reference`,
or `notes`.

```json
{
  "frame_id": "section_5_4.F01",
  "source_span": "exact source phrase or sentence fragment",
  "type": "rule",
  "status": "represented",
  "polarity": "positive",
  "modality": "none",
  "subject": [],
  "predicate": "",
  "object": [],
  "condition": [],
  "consequent": [],
  "scope": [],
  "quantification": [],
  "operator": null,
  "value": null,
  "unit": null,
  "time": [],
  "reference": [],
  "exclusion": [],
  "qualifiers": [],
  "ir_alignment": [],
  "unsupported_reason": "",
  "notes": ""
}
```

## Fixed Enums

### `type`

- `definition`: a term is defined or characterized.
- `fact`: an unconditional factual assertion.
- `rule`: a general formula, constraint, implication, equality, or bound.
- `condition`: a condition that participates in another rule.
- `exception`: an exclusion, exception, fallback, or override condition.
- `procedure`: a procedure exists or is followed, without necessarily modeling stepwise state.
- `action_transition`: an explicit action/state transition.
- `temporal`: persistence, ordering, until/eventually/always, or trace semantics.
- `deontic`: obligation, permission, prohibition, responsibility.
- `reference`: document, URL, section reference, incorporated-by-reference relation.
- `validation`: closed-world, target, shape, or schema validation semantics.
- `probabilistic`: probability, distribution, reward, utility, objective.
- `game`: observation, indistinguishability, player/strategy knowledge.
- `graph`: dataset/reification/triple-level semantics.
- `clarification`: explanatory material that clarifies another frame.
- `vague`: an underdefined term or threshold preserved as vague.
- `unsupported`: a source claim that current A4V3/backend support cannot represent faithfully.

### `status`

- `represented`
- `metadata`
- `absorbed`
- `unsupported`
- `ambiguous`

### `polarity`

- `positive`
- `negative`
- `conditional`
- `exception`
- `counterfactual`
- `mixed`
- `unknown`

### `modality`

- `none`
- `must`
- `may`
- `cannot`
- `should`
- `responsible`
- `intended`
- `possible`
- `defined_as`
- `unknown`

### `operator`

Use `null` unless the frame contains an explicit comparison or equality.

- `=`
- `!=`
- `<`
- `<=`
- `>`
- `>=`
- `in`
- `not_in`
- `count=`
- `count<`
- `count<=`
- `count>`
- `count>=`
- `sum=`
- `sum<=`
- `sum>=`
- `iff`
- `implies`

## Slot Rules

### `subject`, `object`, `condition`, `consequent`, `scope`, `time`, `exclusion`, `qualifiers`

These are arrays of strings or small objects. Prefer strings for simple cases.
Use objects only when a role must be preserved.

Example:

```json
"subject": ["Index Administrator"]
```

or:

```json
"condition": [
  {
    "subject": "Exchange",
    "predicate": "open for trading",
    "polarity": "positive"
  }
]
```

### `quantification`

Use this for "each", "any", "all", "at least N", "exactly N", etc.

```json
"quantification": [
  {"quantifier": "each", "variable": "region", "sort": "Region"}
]
```

### `reference`

Use this for URLs, section references, document names, external policies, and
incorporated-by-reference relations.

```json
"reference": [
  {"kind": "section", "target": "Section 5.2 Methodology Review"},
  {"kind": "url", "target": "https://www.solactive.com/documents/termination-policy/"}
]
```

### `ir_alignment`

Every `represented` frame must align to at least one IR block.

```json
"ir_alignment": [
  {
    "kind": "constraint",
    "name": "region_represents_exactly_50_percent",
    "role": "main_formula"
  }
]
```

Allowed `kind` values:

- `sort`
- `entity`
- `rel`
- `fun`
- `fact`
- `constraint`
- `axiom`
- `permission`
- `prohibition`
- `obligation`
- `action`
- `prop`
- `path`
- `target`
- `sparql_constraint`
- `graph`
- `theorem`
- `comment`

## Atomicity Rules

Split a source sentence into multiple frames when it contains:

- multiple independent conditions;
- multiple exclusions;
- one definition plus clarification;
- one rule plus document/reference metadata;
- actor/action/object plus separate responsibility;
- numeric bound plus separate fallback;
- temporal/process semantics plus final state.

Do not split when a phrase is only a modifier of a single claim, e.g. "clearly
defined and transparent procedure" can stay as one procedure frame with
`qualifiers`.

## Completeness Criteria

An entry is frame-complete when:

- every source claim is covered by at least one frame;
- every frame has a fixed `type`, `status`, `polarity`, and `modality`;
- every `represented` frame has `ir_alignment`;
- every `unsupported` frame has `unsupported_reason`;
- every `absorbed` frame explains the target frame in `notes`;
- no frame uses custom top-level keys.

## A4V3 Coverage Mapping

| A4V3 family | Frame type | Required frame slots |
| --- | --- | --- |
| TypeDecl | `definition` | `subject`, `predicate`, `object` |
| SymbolDecl entity | `fact` or `definition` | `subject`, `predicate` |
| SymbolDecl rel/fun | `definition` | `predicate`, `subject`, `object` |
| AssertDecl fact | `fact` | `subject`, `predicate`, `object`, `ir_alignment` |
| AssertDecl constraint/axiom | `rule` | `condition`, `consequent` or `operator/value`, `ir_alignment` |
| PathDecl | `reference` | `subject`, `predicate`, `object` |
| ActionDecl | `action_transition` | `subject`, `predicate`, `condition`, `consequent` |
| TemporalDecl | `temporal` | `predicate`, `condition`, `time` |
| DeonticDecl | `deontic` | `subject`, `predicate`, `object`, `modality` |
| ValidationDecl | `validation` | `subject`, `predicate`, `condition` |
| ProbabilisticDecl | `probabilistic` | `subject`, `predicate`, `value` |
| GameDecl | `game` | `subject`, `predicate`, `object` |
| GraphDecl | `graph` | `subject`, `predicate`, `object` |
| TheoremDecl | `rule` | `condition`, `consequent` |

## Example: Section 5.4

```json
{
  "frame_id": "section_5_4.F03",
  "source_span": "if no other options are available the orderly cessation of the Index may be indicated",
  "type": "rule",
  "status": "represented",
  "polarity": "conditional",
  "modality": "may",
  "subject": ["orderly cessation of the Index"],
  "predicate": "indicated",
  "object": [],
  "condition": ["no other options are available"],
  "consequent": ["orderly cessation of the Index is indicated"],
  "scope": ["Index"],
  "quantification": [],
  "operator": "implies",
  "value": null,
  "unit": null,
  "time": [],
  "reference": [],
  "exclusion": [],
  "qualifiers": ["orderly"],
  "ir_alignment": [
    {
      "kind": "constraint",
      "name": "orderly_cessation_indicated_if_no_options",
      "role": "main_formula"
    },
    {
      "kind": "permission",
      "name": "indicate_orderly_cessation",
      "role": "modality_carrier"
    }
  ],
  "unsupported_reason": "",
  "notes": ""
}
```

## Example: N30

```json
{
  "frame_id": "N30.F01",
  "source_span": "\"Trading Day\" is ... a day on which the relevant Exchange is open for trading",
  "type": "definition",
  "status": "represented",
  "polarity": "positive",
  "modality": "defined_as",
  "subject": ["Trading Day"],
  "predicate": "defined_as",
  "object": ["day on which the relevant Exchange is open for trading"],
  "condition": [
    {
      "subject": "relevant Exchange",
      "predicate": "open for trading",
      "polarity": "positive"
    }
  ],
  "consequent": [],
  "scope": [
    "with respect to an Index Component included in the Index at the Rebalance Day",
    "with respect to every Index Component included in the Index at the Calculation Day immediately following the Rebalance Day"
  ],
  "quantification": [],
  "operator": null,
  "value": null,
  "unit": null,
  "time": [],
  "reference": [],
  "exclusion": [
    "days on which trading may be ceased prior to scheduled Exchange closing time",
    "days on which the Exchange is open for a scheduled shortened period"
  ],
  "qualifiers": [],
  "ir_alignment": [],
  "unsupported_reason": "",
  "notes": "This complex definition should usually be split into definition, counterfactual inclusion, exclusions, clarification, and responsibility frames."
}
```

## Recommended Pipeline

1. Source passage -> `semantic_frames_source_v1.json`.
2. A4V3 IR -> `semantic_frames_ir_v1.json` or direct `ir_alignment`.
3. Validate schema and fixed enums.
4. Check frame completeness.
5. Compare source frames to IR frames for role, polarity, modality, numeric, scope, and reference agreement.
6. Human/LLM review only the unresolved or low-confidence frames.
