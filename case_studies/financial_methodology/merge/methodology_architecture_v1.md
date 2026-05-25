# Financial Methodology Architecture v1

This note records the intended high-level architecture for translating one
methodology document into auditable IR and executable validation artifacts.

## Краткая Схема

1. **Source fragments**

   `source.md` / `normalized.md`

2. **Local IR layer**

   `main_ir.a4v3`

   - локальная онтология;
   - локальные формулы;
   - local-only source-faithful перевод.

3. **Audit envelope for local IR**

   `provenance.yaml`, `translator_notes.md`, `waiver*.json`,
   `role_annotations.yaml`, deterministic checks, LLM / human review.

4. **Bridge layer**

   `bridge/main_bridge.a4v3`

   - связывает локальные symbols между фрагментами;
   - records exact same / alias / subtype-ish family / related / drift /
     do-not-merge;
   - не создаёт новую предметную методику.

5. **Canonical ontology layer**

   `merge/canonical_ontology_v1.a4v3`

   - общий словарь мира;
   - `IndexFamily`, `PublishedIndexVariant`, `Security`, `IndexComponent`,
     `TradingDay`, `Exchange`, `Price`, `CorporateAction`;
   - задаёт иерархии и общие роли.

6. **Resolved methodology theory**

   `local IR + bridge + canonical ontology`

   - не обязательно материализуется как новый `main_ir`;
   - это логическое представление, где ссылки разрешены через bridge;
   - source of truth всё ещё local IR + bridge + canonical ontology.

7. **Process/workflow layer**

   `process/*.a4v3`

   - Universe construction;
   - Component selection;
   - Weight calculation;
   - Fixing Day shares;
   - Rebalance execution;
   - Corporate action handling;
   - Disruption / correction / termination flows.

8. **Reasoning and validation layer**

   - consistency checks;
   - contradiction probes;
   - vacuity checks;
   - missing type-link checks;
   - variant-specific conflict checks.

9. **Operational lowering layer**

   SHACL / RDF / SMT / executable rules.

   - проверка конкретных расчётных данных;
   - generated artifacts, not source of truth.

## 1. Source Fragments

Files:

- `source.md`
- `normalized.md`

Purpose:

- Preserve the original document fragment.
- Keep normalized source text close to the original meaning.
- Provide the textual evidence for local IR and provenance.

## 2. Local IR Layer

Files:

- `main_ir.a4v3`

Purpose:

- Define the local ontology for one fragment.
- Define local formulas, constraints, deontics, exceptions, and facts.
- Remain source-faithful and local-only.

Important:

- Local IR is a source-of-truth layer.
- Local IR should not silently import cross-section concepts unless the local
  source supports them.

## 3. Audit Envelope For Local IR

Files:

- `provenance.yaml`
- `translator_notes.md`
- `waiver*.json`
- `role_annotations.yaml`
- deterministic check outputs
- LLM / human review outputs

Purpose:

- Explain why each important modeling decision is justified.
- Preserve evidence for non-literal or inferred links.
- Record waivers only when a source token or phrase is intentionally not
  formalized.
- Keep role annotations short and aligned with IR types.

Important:

- This is an audit/governance layer, not a new process layer in the methodology.
- Human approval belongs here as validation of modeling decisions.

## 4. Bridge Layer

Files:

- `bridge/main_bridge.a4v3`

Purpose:

- Link local symbols across fragments.
- Record exact identity, aliases, variant links, subtype-ish families, related
  concepts, unresolved drift, and do-not-merge decisions.

Examples:

- `same_index`
- `same_sort`
- `same_entity`
- `same_relation`
- `BridgeFamily`

Important:

- Bridge does not create a new domain methodology.
- Bridge is a cross-reference and identity layer.
- Bridge is not the same thing as merge.

## 5. Canonical Ontology Layer

Files:

- `merge/canonical_ontology_v1.a4v3`

Purpose:

- Define the shared world used by the resolved methodology theory.
- Provide canonical sorts, entities, roles, and hierarchy.

Examples:

- `IndexFamily`
- `PublishedIndexVariant`
- `Security`
- `IndexComponent`
- `TradingDay`
- `Exchange`
- `Price`
- `CorporateAction`

Important:

- Canonical ontology says what shared concepts exist.
- Bridge says how local symbols point to those concepts.

### Canonical Frames And Bridge Frames

Observation frames are intentionally visible in two layers:

- `CanonicalFrame` entities live in `merge/canonical_ontology_v1.a4v3` and
  describe the shared ontology that future OWL/RDF/SHACL lowering should use.
- `BridgeFrame` entities live in `bridge/main_bridge.a4v3` and act as projection
  targets for local functions and relations.

The names are deliberately coordinated. For example,
`ClosingPriceObservationFrame` in the bridge mirrors
`ClosingPriceObservationFrame` in the canonical ontology. This is not a second
domain concept; it is a bridge-local handle for the canonical frame.

This keeps the layers separate:

- canonical ontology defines the frame and its roles;
- bridge records how local arguments and return values map into those roles;
- resolved views combine both for inspection;
- operational lowering can then generate OWL/RDF-style binary properties from
  role-filled frames.

The same mechanism is used for lifecycle states, not only numeric values. For
example, local `index_component` relations project to membership frames:

- `GenericIndexComponentMembershipFrame`;
- `SelectionDayIndexComponentMembershipFrame`;
- `CalculationDayIndexComponentMembershipFrame`.

This records that component membership can be generic, selection-day scoped, or
calculation-day scoped. It is a bridge/merge state model, not a process
workflow by itself: workflow ordering still belongs in `process/*.a4v3`.

## 6. Resolved Methodology Theory

Inputs:

- local IR
- bridge
- canonical ontology

Purpose:

- Provide the logical view where local references are resolved through the
  bridge and canonical ontology.

Important:

- This layer does not need to be materialized as a new authoritative
  `main_ir.a4v3`.
- If flattened formulas are generated, they are derived artifacts, not source
  of truth.
- The source of truth remains local IR plus bridge plus canonical ontology.

## 7. Process / Workflow Layer

Files:

- `process/*.a4v3`

Purpose:

- Model document-level procedure and ordering.
- Recover the workflow that is spread across multiple sections.

Examples:

- Universe construction
- Component selection
- Weight calculation
- Fixing Day shares
- Rebalance execution
- Corporate action handling
- Disruption, correction, and termination flows

Important:

- Process ontology models how the methodology runs over time.
- It is not the same as bridge.
- It is not the same as operational SHACL lowering.

## 8. Reasoning And Validation Layer

Purpose:

- Check the resolved methodology theory.

Examples:

- Consistency checks
- Contradiction probes
- Vacuity checks
- Missing type-link checks
- Variant-specific conflict checks

Important:

- This layer should report possible missing type or membership links instead of
  silently declaring the theory consistent.
- This is the layer that catches "the rule did not fire because the entity was
  not connected to the right class" risks.

## 9. Operational Lowering Layer

Possible outputs:

- SHACL
- RDF
- SMT
- executable rules

Purpose:

- Validate concrete calculation data or backend-specific representations.

Important:

- Operational lowering can be generated from any valid A4V3 fragment if that
  fragment contains enough structure for the target backend.
- Document-level operational lowering requires the resolved methodology theory
  plus the process/workflow ontology.
- Lowered artifacts are generated artifacts, not source of truth.

## Compact Formula

```text
Local IR says what each fragment says.
Bridge says how fragments refer to the same things.
Canonical ontology says what the shared world is.
Process ontology says how the methodology runs over time.
Validators check the resolved theory and concrete data.
```

## Source Of Truth

```text
source fragments
+ local IR
+ audit envelope
+ bridge
+ canonical ontology
+ process ontology
```

Derived artifacts:

```text
resolved views
flattened merged formulas
SHACL
SMT
RDF validation graphs
executable checks
```
