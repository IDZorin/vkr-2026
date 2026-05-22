# Translation Metrics Catalog v1

## Purpose

This document defines a full metrics catalog for evaluating the `normalized_clauses -> IR` translation stage.

The goal is not to collapse quality into one magic score. The goal is to expose:

- technical validity
- grounding and invention risk
- clause and token coverage
- semantic preservation
- render-back equivalence
- committee and search behavior
- runtime cost
- optional gold-gap diagnostics

Each metric below states:

- `kind`: `hard_fail`, `hard_warning`, `continuous`, `comparative`, or `gold_only`
- `what it counts`
- `how to compute it`

## Metric Kinds

- `hard_fail`: if this metric fails, the translation should not be accepted as a valid IR result.
- `hard_warning`: the IR can still exist as an artifact, but the run should be marked semantically unsafe or incomplete.
- `continuous`: a numeric score or ratio for comparison across runs.
- `comparative`: a metric intended for comparing several IR variants or several runs.
- `gold_only`: only meaningful when a hand-authored gold artifact exists.

## Base Units

The metrics below reuse the following units.

- `normalized clause`: one item in `normalized_clauses`
- `formula-bearing item`: one top-level IR assertion or other IR item that carries substantive rule semantics
- `content token`: a non-stopword lexical token of semantic interest
- `significant token`: a content token that survives stopword removal and focus-term removal
- `grounded symbol`: a symbol whose name is licensed by source text, normalized text, advisory, Prelude, or explicit built-in A4V3 vocabulary
- `prose-only fragment`: a semantic fragment that appears only in notes, residuals, strengths, or other prose fields, not in executable IR

## Recommended Result Shape

Each entry should eventually emit one machine-readable metrics object with this high-level structure:

```json
{
  "validity": {},
  "grounding": {},
  "coverage": {},
  "semantic_preservation": {},
  "compression": {},
  "identifier_glue": {},
  "source_vs_normalized": {},
  "normalized_relative": {},
  "render_back": {},
  "variants": {},
  "efficiency": {},
  "gold_comparison": {}
}
```

## 1. Validity Metrics

These metrics answer: does the artifact even qualify as a legal IR draft?

### `ast_valid`

- kind: `hard_fail`
- what it counts: whether the emitted payload satisfies the canonical AST contract.
- how to compute: `1` if `_validate_canonical_drafter_payload(payload)` returns zero errors, else `0`.

### `ast_error_count`

- kind: `continuous`
- what it counts: total number of canonical AST validation errors.
- how to compute: the length of `_validate_canonical_drafter_payload(payload)`.

### `declaration_shape_error_count`

- kind: `continuous`
- what it counts: AST errors specifically attached to declaration nodes.
- how to compute: count validation errors whose path begins with `ir_ast.declarations`.

### `assertion_shape_error_count`

- kind: `continuous`
- what it counts: AST errors specifically attached to assertion nodes.
- how to compute: count validation errors whose path begins with `ir_ast.assertions`.

### `expr_shape_error_count`

- kind: `continuous`
- what it counts: AST errors specifically attached to expression nodes.
- how to compute: count validation errors whose path contains `.expr`, `.left`, `.right`, `.args`, `.body`, `.cond`, `.then`, or `.else`.

### `rendering_ok`

- kind: `hard_fail`
- what it counts: whether the renderer produced IR text from the AST without renderer failure.
- how to compute: `1` if `rendering_status == "rendered_from_ast"`, else `0`.

### `combined_validation_ok`

- kind: `hard_fail`
- what it counts: whether the draft validates when combined with the current section IR or section theory.
- how to compute: `1` if combined parse/validation succeeds, else `0`.

### `legacy_surface_token_count`

- kind: `hard_warning`
- what it counts: presence of legacy pre-canonical surface tokens in the AST payload.
- how to compute: count tokens such as `forall`, `implies`, `call`, `var`, `params`, `return_sort`, `totality` when they appear in forbidden legacy surface form rather than canonical node shape.

### `schema_repair_round_count`

- kind: `continuous`
- what it counts: how many times the drafter needed repair prompts to satisfy schema requirements.
- how to compute: count repair iterations triggered by AST or schema validation failure.

### `parse_retry_count`

- kind: `continuous`
- what it counts: how many times parsing or JSON extraction had to be retried.
- how to compute: count parser/JSON-extraction retries before a valid candidate was accepted.

## 2. Grounding and Invention Metrics

These metrics answer: is the IR text-grounded, or is it inventing local machinery?

### `ungrounded_symbol_count`

- kind: `hard_fail`
- what it counts: symbols declared in IR that are not grounded in source, advisory, Prelude, or built-in A4V3 vocabulary.
- how to compute: count `symbol` declaration errors emitted by `_validate_symbol_origins(...)`.

### `ungrounded_sort_count`

- kind: `hard_fail`
- what it counts: sort names that are neither Prelude, built-in, locally declared, nor text/advisory grounded.
- how to compute: count sort-origin validation failures.

### `ungrounded_ref_count`

- kind: `hard_fail`
- what it counts: expression references that are not locally bound, declared, or grounded.
- how to compute: count ref-origin failures from `_validate_expr_symbol_origins(...)`.

### `ungrounded_callee_count`

- kind: `hard_fail`
- what it counts: callee names used in calls that are not declared, Prelude, or whitelisted A4V3 builtins.
- how to compute: count callee-origin failures from `_validate_expr_symbol_origins(...)`.

### `prelude_redeclaration_count`

- kind: `hard_fail`
- what it counts: attempts to redeclare Prelude sorts, entities, or functions.
- how to compute: count redeclaration errors raised by `_validate_symbol_origins(...)`.

### `new_formula_token_count_vs_text_only`

- kind: `continuous`
- what it counts: all new formula tokens relative to source plus normalized text only, without forgiving Prelude.
- how to compute: tokenize rendered formula surface; subtract token set from source excerpt, source term, normalized clauses, and A4V3 syntax; count the residue.

### `new_formula_content_token_count_vs_text_only`

- kind: `hard_warning`
- what it counts: semantically meaningful new formula tokens relative to source plus normalized text only.
- how to compute: same as above, but remove stopwords and syntax-only tokens before counting.

### `new_full_surface_token_count_vs_text_only`

- kind: `continuous`
- what it counts: all new tokens in rendered IR plus prose fields relative to source plus normalized text only.
- how to compute: tokenize formula plus prose fields; subtract token set from source excerpt, source term, normalized clauses, and A4V3 syntax; count the residue.

### `new_full_surface_content_token_count_vs_text_only`

- kind: `hard_warning`
- what it counts: semantically meaningful new tokens in rendered IR plus prose fields relative to source plus normalized text only.
- how to compute: same as above, but remove stopwords and syntax-only tokens before counting.

### `invented_helper_symbol_count`

- kind: `hard_warning`
- what it counts: helper symbols introduced by the IR that are technically grounded by token overlap but are not justified as minimal abstractions.
- how to compute: count declared non-focus symbols that are not in source term inventory, not in Prelude, and not referenced in clause-to-IR mapping as necessary support symbols.

### `invented_helper_sort_count`

- kind: `hard_warning`
- what it counts: helper sorts introduced without strong textual license.
- how to compute: count newly declared sorts that are not direct concept names from source/advisory and are not Prelude or built-in sorts.

### `new_surface_token_count`

- kind: `continuous`
- what it counts: all lexical tokens appearing in rendered IR or structured prose fields that do not belong to the union of source text, normalized text, advisory text, Prelude, and whitelisted A4V3 syntax.
- how to compute: tokenize rendered IR plus prose fields; subtract token sets from source, advisory, Prelude, and A4V3 whitelist; count the residue.

### `new_surface_content_token_count`

- kind: `hard_warning`
- what it counts: semantically meaningful new tokens, excluding syntax and stopwords.
- how to compute: same as `new_surface_token_count`, but after removing stopwords and A4V3 syntax tokens.

### `advisory_only_symbol_count`

- kind: `hard_warning`
- what it counts: symbols whose only license comes from advisory prose rather than source text or normalized clauses.
- how to compute: count symbols found in advisory names but not in source-term inventory or normalized token inventory.

### `text_licensed_symbol_ratio`

- kind: `continuous`
- what it counts: share of declared local symbols that can be grounded directly in source or normalized text.
- how to compute: `text-grounded local symbol count / total local symbol count`.

### `prelude_symbol_ratio`

- kind: `continuous`
- what it counts: share of used symbols coming from Prelude or explicit built-ins.
- how to compute: `Prelude or built-in symbol usage count / total symbol usage count`.

## 3. Clause Coverage Metrics

These metrics answer: did every normalized clause survive somewhere in the IR?

### `normalized_clause_count`

- kind: `continuous`
- what it counts: number of normalized clauses presented to IR drafting.
- how to compute: `len(normalized_clauses)`.

### `formula_bearing_item_count`

- kind: `continuous`
- what it counts: number of top-level IR items that carry executable rule semantics.
- how to compute: count assertions and any other formula-bearing IR nodes considered semantically substantive.

### `clause_coverage_ratio`

- kind: `continuous`
- what it counts: fraction of normalized clauses that are represented somewhere in IR or explicit accepted annotation nodes.
- how to compute: `covered_clause_count / normalized_clause_count`.

### `uncovered_clause_count`

- kind: `hard_warning`
- what it counts: normalized clauses that are not represented in formula, annotation, or accepted residual structure.
- how to compute: `normalized_clause_count - covered_clause_count`.

### `multi_clause_merge_count`

- kind: `hard_warning`
- what it counts: cases where multiple normalized clauses are collapsed into a single formula-bearing item without explicit traceability.
- how to compute: for each formula-bearing item, count how many clauses map to it; sum all excess over `1`.

### `support_only_clause_count`

- kind: `continuous`
- what it counts: number of clauses explicitly marked support-only.
- how to compute: count normalized clauses whose role is classified as support-only or whose coverage record says they are intentionally non-formula-bearing.

### `support_only_clause_ratio`

- kind: `continuous`
- what it counts: share of all normalized clauses treated as support-only.
- how to compute: `support_only_clause_count / normalized_clause_count`.

### `covered_only_in_notes_count`

- kind: `hard_warning`
- what it counts: semantic fragments that appear only in notes or residual prose, not in formula or structured annotation.
- how to compute: count coverage-audit items with status `covered_only_in_notes`.

### `missing_fragment_count`

- kind: `hard_warning`
- what it counts: semantic fragments absent from both formula and prose.
- how to compute: count coverage-audit items with status `missing`.

### `prose_leak_count`

- kind: `hard_warning`
- what it counts: clause-sized semantic fragments left only in prose after stopword filtering.
- how to compute: count `covered_only_in_notes` or `missing` fragments whose significant-token count exceeds the chosen threshold.

## 4. Lexical and Content Coverage Metrics

These metrics answer: how much source content survives lexically or near-lexically?

### `content_token_recall`

- kind: `continuous`
- what it counts: how much of the source content-token inventory appears in IR.
- how to compute: `matched source content tokens / total source content tokens`.

### `content_token_precision`

- kind: `continuous`
- what it counts: how much of the IR content-token inventory is source-licensed.
- how to compute: `matched IR content tokens / total IR content tokens`.

### `content_token_jaccard`

- kind: `continuous`
- what it counts: overlap between source content tokens and IR content tokens.
- how to compute: `|intersection| / |union|`.

### `content_token_multiset_recall`

- kind: `continuous`
- what it counts: recall with repeated token occurrences taken seriously.
- how to compute: multiset overlap count divided by total source content-token multiplicity.

### `content_token_multiset_precision`

- kind: `continuous`
- what it counts: precision with repeated token occurrences taken seriously.
- how to compute: multiset overlap count divided by total IR content-token multiplicity.

### `source_content_token_mass`

- kind: `continuous`
- what it counts: total multiplicity of content tokens in the source text, not just distinct token types.
- how to compute: tokenize normalized text into content tokens and count all occurrences.

### `formula_content_token_mass`

- kind: `continuous`
- what it counts: total multiplicity of content tokens in formal IR surface.
- how to compute: tokenize rendered IR into content tokens and count all occurrences.

### `full_surface_content_token_mass`

- kind: `continuous`
- what it counts: total multiplicity of content tokens across formal IR and prose fields together.
- how to compute: tokenize rendered IR plus prose fields and count all occurrences.

### `formula_repeat_overuse_token_count`

- kind: `hard_warning`
- what it counts: how many source-licensed content tokens are repeated more often in formal IR than in the source.
- how to compute: compare content-token counters for source and formula surface, then count tokens where `formula_count > source_count`.

### `formula_repeat_overuse_mass`

- kind: `hard_warning`
- what it counts: total excess repetition mass in formal IR.
- how to compute: sum `max(0, formula_count - source_count)` over all source-licensed content tokens.

### `formula_repeat_underuse_token_count`

- kind: `continuous`
- what it counts: how many source content tokens appear fewer times in formal IR than in the source.
- how to compute: count tokens where `formula_count < source_count`.

### `formula_repeat_underuse_mass`

- kind: `continuous`
- what it counts: total missing repetition mass in formal IR.
- how to compute: sum `max(0, source_count - formula_count)` over all source content tokens.

### `formula_repeat_overuse_examples`

- kind: `comparative`
- what it counts: the most obviously overused content tokens in formal IR.
- how to compute: rank tokens by `formula_count - source_count` and keep the top examples.

### `full_surface_repeat_overuse_token_count`

- kind: `hard_warning`
- what it counts: how many content tokens are repeated more often in IR plus notes than in the source.
- how to compute: compare source token counter with the combined counter over rendered IR and prose fields.

### `full_surface_repeat_overuse_mass`

- kind: `hard_warning`
- what it counts: total excess repetition mass across IR plus prose.
- how to compute: sum `max(0, full_surface_count - source_count)` over all content tokens.

### `full_surface_repeat_overuse_examples`

- kind: `comparative`
- what it counts: the strongest repetition-inflation examples anywhere in the artifact.
- how to compute: rank tokens by `full_surface_count - source_count` and keep the top examples.

### `focus_term_explicitly_modeled`

- kind: `hard_fail`
- what it counts: whether the defined term is explicit in IR rather than hidden behind helpers.
- how to compute: `1` if the focus term appears as a top-level declaration or clearly in formula body, else `0`.

### `focus_term_in_top_level_decl`

- kind: `continuous`
- what it counts: whether the focus term appears as a top-level sort/entity/symbol declaration.
- how to compute: boolean flag over declaration names.

### `focus_term_in_formula_body`

- kind: `continuous`
- what it counts: whether the focus term appears in the semantic body of assertions, not only as a declaration.
- how to compute: boolean flag over expression references and calls.

### `source_to_ir_token_gap_count`

- kind: `continuous`
- what it counts: source-side content tokens missing from IR surface.
- how to compute: count source content tokens absent from rendered IR and accepted annotation nodes.

### `ir_to_source_token_gap_count`

- kind: `continuous`
- what it counts: IR-side content tokens without source, advisory, Prelude, or A4V3 support.
- how to compute: count IR content tokens missing from the allowed vocabulary pool.

## 4A. Source-to-Normalized Metrics

These metrics answer: what changed before IR even started, when raw source text was rewritten into normalized clauses?

### `source_excerpt_content_token_count`

- kind: `continuous`
- what it counts: distinct source-side content tokens in the original source excerpt.
- how to compute: tokenize source excerpt into content tokens and count unique types.

### `source_excerpt_content_token_mass`

- kind: `continuous`
- what it counts: total multiplicity of content tokens in the original source excerpt.
- how to compute: tokenize source excerpt into content tokens and count all occurrences.

### `normalized_content_token_count`

- kind: `continuous`
- what it counts: distinct content tokens in normalized clauses.
- how to compute: tokenize concatenated normalized clauses into content tokens and count unique types.

### `normalized_content_token_mass`

- kind: `continuous`
- what it counts: total multiplicity of content tokens in normalized clauses.
- how to compute: tokenize concatenated normalized clauses into content tokens and count all occurrences.

### `normalized_content_token_recall_from_source`

- kind: `continuous`
- what it counts: how much of the original source token inventory survives into normalization.
- how to compute: `matched normalized/source content token types / source content token types`.

### `normalized_content_token_precision_to_source`

- kind: `continuous`
- what it counts: how source-grounded the normalized token inventory is.
- how to compute: `matched normalized/source content token types / normalized content token types`.

### `normalized_content_token_jaccard`

- kind: `continuous`
- what it counts: set-overlap between source content tokens and normalized content tokens.
- how to compute: `|intersection| / |union|`.

### `normalized_content_token_multiset_recall_from_source`

- kind: `continuous`
- what it counts: how much of the source token mass survives into normalization.
- how to compute: multiset overlap between normalized and source token counters divided by source token mass.

### `normalized_content_token_multiset_precision_to_source`

- kind: `continuous`
- what it counts: how much of normalized token mass is licensed directly by source wording.
- how to compute: multiset overlap between normalized and source token counters divided by normalized token mass.

### `source_to_normalized_token_gap_count`

- kind: `hard_warning`
- what it counts: distinct source content tokens that normalization dropped completely.
- how to compute: count `source_token_set - normalized_token_set`.

### `normalized_to_source_new_token_count`

- kind: `hard_warning`
- what it counts: distinct content tokens introduced by normalization that were not present in source.
- how to compute: count `normalized_token_set - source_token_set`.

### `normalized_repeat_overuse_token_count`

- kind: `hard_warning`
- what it counts: number of source-licensed content tokens repeated more often in normalization than in source.
- how to compute: compare normalized token counter with source token counter and count tokens where `normalized_count > source_count`.

### `normalized_repeat_overuse_mass`

- kind: `hard_warning`
- what it counts: total excess repetition introduced by normalization.
- how to compute: sum `max(0, normalized_count - source_count)` over all content tokens.

### `normalized_repeat_overuse_examples`

- kind: `comparative`
- what it counts: top examples of normalization inflating token repetition.
- how to compute: rank tokens by `normalized_count - source_count` and keep top examples.

### `normalized_length_ratio_vs_source_mass`

- kind: `continuous`
- what it counts: how much normalization expands or compresses source token mass.
- how to compute: `normalized_content_token_mass / source_excerpt_content_token_mass`.

### `normalized_content_mass_per_clause`

- kind: `continuous`
- what it counts: average content-token mass per normalized clause.
- how to compute: `normalized_content_token_mass / normalized_clause_count`.

### `source_normalized_bertscore_f1`

- kind: `continuous`
- what it counts: semantic similarity between original source excerpt and normalized clauses.
- how to compute: BERTScore F1 between concatenated normalized clauses and source excerpt.

### `normalized_implies_source_entailment`

- kind: `continuous`
- what it counts: whether normalization semantically entails the source.
- how to compute: NLI entailment score with `premise = normalized`, `hypothesis = source`.

### `source_implies_normalized_entailment`

- kind: `continuous`
- what it counts: whether the source semantically entails the normalization.
- how to compute: NLI entailment score with `premise = source`, `hypothesis = normalized`.

### `source_vs_normalized_contradiction_score`

- kind: `hard_warning`
- what it counts: contradiction risk between source and normalization.
- how to compute: take the max contradiction score from the two NLI directions.

## 5. Link and Ontology Preservation Metrics

These metrics answer: did the IR keep the right actors and links, not just plausible names?

### `explicit_link_violation_count`

- kind: `hard_warning`
- what it counts: cases where a symbol name embeds another concept that the formula body never links explicitly.
- how to compute: count checklist violations of `keep_links_explicit`.

### `embedded_concept_without_formula_link_count`

- kind: `hard_warning`
- what it counts: symbol names with compositional tokens such as `ExchangeOf`, `IndexUniverseRequirements`, or similar that never appear as explicit linked concepts in formula.
- how to compute: inspect multi-token symbol names and count cases where one embedded concept is absent from the expression graph.

### `carrier_choice_stability`

- kind: `comparative`
- what it counts: whether different runs choose the same carrier family, for example function vs relation or exchange-level vs component-level predicate.
- how to compute: compare chosen carrier signatures across variants or reruns; report agreement ratio.

### `arg_arity_stability`

- kind: `comparative`
- what it counts: whether different variants agree on argument count.
- how to compute: compare top-level focus symbol arity across variants; report agreement ratio.

### `sort_choice_stability`

- kind: `comparative`
- what it counts: whether different variants agree on sorts for the same argument positions.
- how to compute: compare argument-sort tuples across variants; report agreement ratio.

### `dependency_link_count`

- kind: `continuous`
- what it counts: number of explicit dependency symbols or cross-entry concepts actually used in formula.
- how to compute: count distinct dependency symbols referenced in declarations or assertions.

### `dependency_link_recall`

- kind: `continuous`
- what it counts: share of expected dependency concepts that are explicitly linked in formula.
- how to compute: `explicitly linked dependency count / expected dependency count`.

### `cross_reference_usage_count`

- kind: `continuous`
- what it counts: number of related entries or cross-referenced concepts actually used in final IR.
- how to compute: count cross-reference ids from advisory that survive into formula or accepted annotation.

### `cross_reference_dropout_count`

- kind: `hard_warning`
- what it counts: cross-referenced concepts discussed upstream but omitted from final IR.
- how to compute: `expected cross-reference count - used cross-reference count`.

## 6. Scope, Negation, and Exception Metrics

These metrics answer: did the rule keep its boundaries and carve-outs?

### `scope_visibility_violation_count`

- kind: `hard_warning`
- what it counts: scope restrictions that are lost, blurred, or pushed into symbol names only.
- how to compute: count checklist or coverage findings where scope text is not visible in formula or accepted annotation nodes.

### `exception_visibility_violation_count`

- kind: `hard_warning`
- what it counts: exceptions or exclusions that disappear or are blurred into opaque helpers.
- how to compute: count checklist violations of `preserve_negation_scope_and_exceptions`.

### `negation_loss_count`

- kind: `hard_warning`
- what it counts: lost negative operators such as `not`, `excluding`, `unless not`, and analogous semantics.
- how to compute: compare negation-bearing source fragments against IR and count missing negation semantics.

### `quantifier_loss_count`

- kind: `hard_warning`
- what it counts: lost universal or existential force.
- how to compute: compare quantification cues like `each`, `every`, `all`, `exists`, `for any` against quantifier structure in IR.

### `guard_loss_count`

- kind: `hard_warning`
- what it counts: lost guard conditions or antecedents.
- how to compute: compare conditional source fragments against IR implication, guard predicates, or `ite` conditions.

### `temporal_link_loss_count`

- kind: `hard_warning`
- what it counts: lost temporal relations such as `immediately following`, `preceding`, `after`, `before`.
- how to compute: count temporal source fragments not mapped into explicit temporal predicates, functions, or annotations.

### `counterfactual_loss_count`

- kind: `hard_warning`
- what it counts: lost counterfactual semantics such as `would have been ... if ... had not occurred`.
- how to compute: count counterfactual fragments lacking explicit counterfactual predicate or equivalent guarded representation.

### `clarification_loss_count`

- kind: `hard_warning`
- what it counts: clarification clauses that disappear or survive only as unstructured notes.
- how to compute: count clarification fragments not present in formula or explicit clarification annotation nodes.

### `responsibility_loss_count`

- kind: `hard_warning`
- what it counts: responsibility, governance, or authority clauses omitted entirely when the modeling policy expects them to remain visible.
- how to compute: count responsibility fragments absent from IR or structured annotation layer.

### `procedural_note_leak_count`

- kind: `continuous`
- what it counts: procedural or governance material left as plain prose rather than structured residual annotations.
- how to compute: count responsibility or governance fragments whose only representation is free prose.

## 7. Definition Quality Metrics

These metrics answer: is the entry really modeled as a definition, not a hollow shell?

### `declaration_only_downgrade_flag`

- kind: `hard_warning`
- what it counts: whether a definitional clause was reduced to a bare declaration with no meaningful body.
- how to compute: `1` when the source is definitional but the IR contains only declarations and no definitional assertion or equation.

### `definition_body_present`

- kind: `continuous`
- what it counts: whether the definition includes a semantic body, not just a carrier.
- how to compute: boolean flag based on presence of definitional assertions or body-bearing constructs.

### `definitional_equation_present`

- kind: `continuous`
- what it counts: whether a value-like definition is expressed as an equation.
- how to compute: boolean flag when the focus term appears on one side of an equality-like definition.

### `biconditional_present_when_expected`

- kind: `continuous`
- what it counts: whether predicate-like definitions are encoded with `iff` or semantically equivalent bidirectional structure when appropriate.
- how to compute: boolean flag comparing focus-term kind to expression structure.

### `vacuous_constraint_flag`

- kind: `hard_warning`
- what it counts: whether a constraint is tautological or semantically empty.
- how to compute: `1` for reflexive equalities such as `Exchange(x) = Exchange(x)` or other trivially true shells.

### `reflexive_equality_count`

- kind: `hard_warning`
- what it counts: number of equality assertions whose left and right normalized forms are identical.
- how to compute: count equality nodes whose rendered operands match modulo whitespace and trivial renaming.

### `opaque_support_symbol_count`

- kind: `continuous`
- what it counts: number of intentionally opaque support symbols used to preserve semantics.
- how to compute: count helper symbols explicitly marked or inferable as support abstractions rather than primary focus symbols.

### `opaque_support_symbol_ratio`

- kind: `continuous`
- what it counts: share of support abstractions among all local declared symbols.
- how to compute: `opaque_support_symbol_count / local_declared_symbol_count`.

### `helper_explosion_count`

- kind: `hard_warning`
- what it counts: excessive proliferation of helper symbols relative to source complexity.
- how to compute: `max(0, helper_symbol_count - expected_helper_budget)` where the budget depends on clause count and role complexity.

### `core_term_centeredness_score`

- kind: `continuous`
- what it counts: how central the focus term is in the final IR.
- how to compute: weighted score from top-level declaration presence, assertion-body appearance, and dependency centrality; for example a normalized score in `[0,1]`.

## 8. Compression and Readability Metrics

These metrics answer: did the IR compress too aggressively or become unreadably bloated?

### `formula_to_clause_compression_ratio`

- kind: `continuous`
- what it counts: how many normalized clauses are carried per formula-bearing IR item.
- how to compute: `normalized_clause_count / max(1, formula_bearing_item_count)`.

### `mean_significant_tokens_per_formula_item`

- kind: `continuous`
- what it counts: average semantic density per formula-bearing item.
- how to compute: total significant source tokens represented formally divided by formula-bearing item count.

### `max_clause_collapse_size`

- kind: `hard_warning`
- what it counts: the largest number of normalized clauses collapsed into one formula-bearing item.
- how to compute: maximum clause-to-formula fan-in over the clause-to-IR map.

### `named_exclusion_count`

- kind: `continuous`
- what it counts: number of exclusions represented as explicit distinct predicates or conjuncts.
- how to compute: count exclusion-bearing constructs mapped from exclusion clauses.

### `named_scope_predicate_count`

- kind: `continuous`
- what it counts: number of explicit scope predicates or guards.
- how to compute: count distinct scope-bearing predicates, guard expressions, or annotation nodes.

### `annotation_node_count`

- kind: `continuous`
- what it counts: number of explicit non-formula semantic annotation nodes used to preserve clarification, responsibility, or provenance.
- how to compute: count accepted annotation structures beyond bare notes.

### `notes_token_count`

- kind: `continuous`
- what it counts: total token count in prose-only fields such as rendering notes and residual risks.
- how to compute: tokenize prose fields and count all tokens.

### `notes_content_token_count`

- kind: `hard_warning`
- what it counts: content-token mass left in prose rather than formal IR or explicit annotation nodes.
- how to compute: tokenize prose fields, remove stopwords and syntax, and count the residue.

### `notes_to_formula_content_ratio`

- kind: `continuous`
- what it counts: how much semantic content lives in notes relative to formula.
- how to compute: `notes_content_token_count / max(1, formula_content_token_count)`.

## 8A. Identifier Glue Metrics

These metrics answer: are names staying compositional, or are whole clauses getting fused into giant helper identifiers?

The goal is not to punish every multiword name. The goal is to distinguish:

- reasonable compositional names like `RelevantExchange`
- text-grounded long names like `WouldHaveBeenOpenButForDisruption`
- suspicious over-glued names that compress too much logic into one symbol

### `identifier_count`

- kind: `continuous`
- what it counts: number of unique IR identifiers inspected by the glue analysis.
- how to compute: collect unique declaration names, assertion names, and named references/callees from the AST.

### `compound_identifier_count_raw`

- kind: `hard_warning`
- what it counts: identifiers whose raw split length is already large.
- how to compute: split each identifier at camel/snake boundaries and count those with at least 4 raw pieces.

### `compound_identifier_count_content`

- kind: `hard_warning`
- what it counts: identifiers with at least 3 non-stopword content pieces.
- how to compute: split each identifier, remove stopwords/syntax pieces, then count identifiers with at least 3 remaining pieces.

### `compound_identifier_rate_raw`

- kind: `continuous`
- what it counts: how large the raw glued-name population is relative to the whole identifier inventory.
- how to compute: `compound_identifier_count_raw / identifier_count`.

### `compound_identifier_rate_content`

- kind: `continuous`
- what it counts: how large the content-level glued-name population is relative to the whole identifier inventory.
- how to compute: `compound_identifier_count_content / identifier_count`.

### `max_identifier_piece_count_raw`

- kind: `continuous`
- what it counts: worst-case raw identifier length.
- how to compute: maximum raw split-piece count across identifiers.

### `max_identifier_piece_count_content`

- kind: `continuous`
- what it counts: worst-case content-piece identifier length.
- how to compute: maximum non-stopword content-piece count across identifiers.

### `mean_identifier_piece_count_raw`

- kind: `continuous`
- what it counts: average raw identifier length.
- how to compute: mean raw split-piece count across identifiers.

### `mean_identifier_piece_count_content`

- kind: `continuous`
- what it counts: average content-piece identifier length.
- how to compute: mean non-stopword content-piece count across identifiers.

### `identifier_glue_excess_mass_raw`

- kind: `continuous`
- what it counts: total raw over-glue mass.
- how to compute: for each identifier, compute `max(0, raw_piece_count - 3)` and sum over identifiers.

### `identifier_glue_excess_mass_content`

- kind: `continuous`
- what it counts: total content-level over-glue mass.
- how to compute: for each identifier, compute `max(0, content_piece_count - 2)` and sum over identifiers.

### `identifier_glue_excess_rate_raw`

- kind: `continuous`
- what it counts: average raw over-glue burden per identifier.
- how to compute: `identifier_glue_excess_mass_raw / identifier_count`.

### `identifier_glue_excess_rate_content`

- kind: `continuous`
- what it counts: average content-level over-glue burden per identifier.
- how to compute: `identifier_glue_excess_mass_content / identifier_count`.

### `source_grounded_content_piece_ratio_mean`

- kind: `continuous`
- what it counts: how grounded identifier pieces are in source text, normalized text, and Prelude vocabulary.
- how to compute: for each identifier, compute the share of content pieces found in the source-side lexicon; then average across identifiers.

### `advisory_grounded_content_piece_ratio_mean`

- kind: `continuous`
- what it counts: how grounded identifier pieces are if advisory vocabulary is also counted as a license source.
- how to compute: same as above, but expand the lexicon with advisory text.

### `low_source_grounded_glued_identifier_count`

- kind: `hard_warning`
- what it counts: suspicious identifiers that are both long and weakly grounded in the source.
- how to compute: count identifiers with at least 3 content pieces and source-grounded content-piece ratio below `0.67`.

### `low_source_grounded_glued_identifier_rate`

- kind: `continuous`
- what it counts: how much of the identifier inventory is simultaneously glued and weakly source-grounded.
- how to compute: `low_source_grounded_glued_identifier_count / identifier_count`.

### `top_glued_identifiers`

- kind: `comparative`
- what it counts: the most over-glued identifiers in the artifact.
- how to compute: rank identifiers by content glue excess, then raw glue excess, then low source-groundedness.

### `lowest_source_grounded_identifiers`

- kind: `comparative`
- what it counts: identifiers whose pieces are least grounded in the source.
- how to compute: rank identifiers by source-grounded content-piece ratio ascending, then by content-piece count descending.

## 8B. Assertion Complexity Metrics

These metrics answer: is the definition expressed as a reasonably decomposed set of logic blocks, or is too much logic crammed into one giant assertion?

### `assertion_count`

- kind: `continuous`
- what it counts: number of top-level assertion blocks in the IR.
- how to compute: count AST assertions.

### `mean_assertion_node_count`

- kind: `continuous`
- what it counts: average expression-tree size per assertion.
- how to compute: recursively count expression nodes inside each assertion and average.

### `max_assertion_node_count`

- kind: `hard_warning`
- what it counts: size of the single most complex assertion.
- how to compute: recursively count expression nodes inside each assertion and take the maximum.

### `total_assertion_node_count`

- kind: `continuous`
- what it counts: total logic mass across all assertions.
- how to compute: sum expression-node counts over assertions.

### `mean_assertion_depth`

- kind: `continuous`
- what it counts: average nesting depth of assertion expressions.
- how to compute: recursively compute expression depth per assertion and average.

### `max_assertion_depth`

- kind: `hard_warning`
- what it counts: nesting depth of the deepest assertion.
- how to compute: recursively compute expression depth and take the maximum.

### `total_ite_count`

- kind: `hard_warning`
- what it counts: total number of explicit `ite` branches in the IR.
- how to compute: recursively count `ite` nodes across assertions.

### `max_ite_count_per_assertion`

- kind: `hard_warning`
- what it counts: largest number of `ite` branches inside a single assertion.
- how to compute: recursively count `ite` nodes per assertion and take the maximum.

### `total_quantifier_count`

- kind: `continuous`
- what it counts: total number of quantifier nodes in assertions.
- how to compute: recursively count `forall` and `exists` nodes.

### `total_connective_count`

- kind: `continuous`
- what it counts: total number of logical connectives such as `and`, `or`, `not`, `implies`, `iff`.
- how to compute: recursively count logical connective nodes across assertions.

### `total_branching_point_count`

- kind: `continuous`
- what it counts: total branching burden in the logic.
- how to compute: sum branch contributions from `and/or` fanout, `ite`, and multi-variable quantifier binders.

### `max_branching_point_count_per_assertion`

- kind: `hard_warning`
- what it counts: worst single-assertion branching burden.
- how to compute: compute branching-point count per assertion and take the maximum.

### `single_assertion_logic_share`

- kind: `continuous`
- what it counts: how much of all assertion logic mass lives in the largest single assertion.
- how to compute: `max_assertion_node_count / total_assertion_node_count`.

### `overcompressed_single_assertion_flag`

- kind: `hard_warning`
- what it counts: whether a multi-clause definition appears packed into one overly large assertion.
- how to compute: fire when `normalized_clause_count >= 3`, `assertion_count == 1`, and the lone assertion is large/deep/branchy or uses `ite`.

### `top_complex_assertions`

- kind: `comparative`
- what it counts: the most structurally complex assertions in the artifact.
- how to compute: rank assertions by node count, depth, then branching-point count.

## 8C. Normalized Alignment Metrics

These metrics answer: does the IR decompose the definition at a scale that is at least directionally compatible with the normalized text?

### `logic_block_count`

- kind: `continuous`
- what it counts: number of top-level IR logic blocks.
- how to compute: count AST assertions.

### `clause_to_logic_block_ratio`

- kind: `continuous`
- what it counts: how many normalized clauses are being carried, on average, by one logic block.
- how to compute: `normalized_clause_count / max(1, logic_block_count)`.

### `logic_block_to_clause_ratio`

- kind: `continuous`
- what it counts: how densely the IR logic-block count tracks normalized clause count.
- how to compute: `logic_block_count / max(1, normalized_clause_count)`.

### `clause_underdecomposition_mass`

- kind: `hard_warning`
- what it counts: how many normalized clauses have no corresponding top-level logic block if we compare counts naively.
- how to compute: `max(0, normalized_clause_count - logic_block_count)`.

### `clause_overdecomposition_mass`

- kind: `continuous`
- what it counts: how many extra logic blocks were introduced beyond normalized clause count.
- how to compute: `max(0, logic_block_count - normalized_clause_count)`.

### `underdecomposed_logic_flag`

- kind: `hard_warning`
- what it counts: whether a multi-clause normalized definition has been collapsed into too few logic blocks and one dominant assertion.
- how to compute: fire when `normalized_clause_count >= 3`, `logic_block_count <= 1`, and `overcompressed_single_assertion_flag = 1`.

## 9. Render-Back and Semantic Equivalence Metrics

These metrics answer: if we verbalize the IR back into English, does it still say the same thing?

### `render_back_available`

- kind: `continuous`
- what it counts: whether a verbalized natural-language rendering of the IR exists.
- how to compute: boolean flag set when the render-back stage succeeds.

### `render_back_clause_count`

- kind: `continuous`
- what it counts: number of natural-language blocks in the render-back.
- how to compute: count render-back sentences or blocks aligned to IR assertions and annotations.

### `render_content_token_recall`

- kind: `continuous`
- what it counts: how many normalized-text content tokens reappear in IR render-back.
- how to compute: token overlap between render-back and normalized clauses.

### `render_content_token_precision`

- kind: `continuous`
- what it counts: how much of the render-back’s content-token mass is licensed by normalized text.
- how to compute: overlap between render-back content tokens and normalized content tokens divided by total render-back content tokens.

### `render_bertscore_f1_to_normalized`

- kind: `continuous`
- what it counts: semantic similarity between render-back text and normalized clauses.
- how to compute: BERTScore F1 between concatenated render-back and concatenated normalized clauses.

### `render_bertscore_f1_to_source`

- kind: `continuous`
- what it counts: semantic similarity between render-back text and original source excerpt.
- how to compute: BERTScore F1 between render-back and source excerpt.

### `render_nli_ir_implies_text`

- kind: `continuous`
- what it counts: whether the render-back semantically entails the normalized text.
- how to compute: NLI model score for `premise = render-back`, `hypothesis = normalized text`.

### `render_nli_text_implies_ir`

- kind: `continuous`
- what it counts: whether the normalized text semantically entails the render-back.
- how to compute: NLI model score for `premise = normalized text`, `hypothesis = render-back`.

### `render_contradiction_score`

- kind: `hard_warning`
- what it counts: probability or score that render-back contradicts normalized text.
- how to compute: contradiction output from NLI model.

### `render_similarity_threshold_pass`

- kind: `hard_warning`
- what it counts: whether render-back similarity passes the configured threshold.
- how to compute: boolean over chosen threshold on BERTScore, NLI, or hybrid render-alignment score.

## 10. Targeted Probe Metrics

These metrics answer: did specific fragile semantic features survive?

### `probe_scope_preserved`

- kind: `hard_warning`
- what it counts: whether scope semantics survive targeted probing.
- how to compute: ask a targeted classifier or rule-based probe whether the scope condition in normalized text is present in IR or render-back.

### `probe_exception_preserved`

- kind: `hard_warning`
- what it counts: whether exclusion clauses survive targeted probing.
- how to compute: targeted probe over exclusion fragments.

### `probe_negation_preserved`

- kind: `hard_warning`
- what it counts: whether negative force survives targeted probing.
- how to compute: targeted probe over negation-bearing fragments.

### `probe_counterfactual_preserved`

- kind: `hard_warning`
- what it counts: whether counterfactual semantics survive targeted probing.
- how to compute: targeted probe over counterfactual fragments such as `would have been ... if ... had not occurred`.

### `probe_clarification_preserved`

- kind: `hard_warning`
- what it counts: whether clarification semantics remain visible in formula or explicit annotation.
- how to compute: targeted probe over clarification fragments.

### `probe_responsibility_preserved`

- kind: `hard_warning`
- what it counts: whether responsibility or authority semantics remain visible where required.
- how to compute: targeted probe over responsibility fragments.

### `probe_reference_preserved`

- kind: `hard_warning`
- what it counts: whether external reference semantics such as `as defined in Section X` survive.
- how to compute: targeted probe over reference-bearing fragments.

### `probe_temporal_order_preserved`

- kind: `hard_warning`
- what it counts: whether temporal ordering survives, for example `immediately following`, `preceding`, `after`.
- how to compute: targeted probe over temporal-order fragments.

### `probe_value_source_preserved`

- kind: `hard_warning`
- what it counts: whether value-source semantics such as `most recent published price` or `as sourced from data vendors` survive where intended.
- how to compute: targeted probe over value-source fragments.

## 11. Variant and Committee Metrics

These metrics answer: how much search happened, and how much real diversity did it buy us?

### `candidate_reading_count`

- kind: `continuous`
- what it counts: number of advisory candidate readings proposed.
- how to compute: `len(candidate_readings)`.

### `draft_variant_count`

- kind: `continuous`
- what it counts: number of concrete IR variants drafted.
- how to compute: `len(drafter_variants)`.

### `unique_ir_variant_count`

- kind: `comparative`
- what it counts: number of materially distinct IR variants.
- how to compute: cluster variants by normalized carrier, focus symbol signature, and formula skeleton; count clusters.

### `variant_diversity_score`

- kind: `comparative`
- what it counts: how different the variants really are.
- how to compute: average pairwise structural distance across variants.

### `critic_confidence`

- kind: `comparative`
- what it counts: confidence reported by the critic for the selected variant.
- how to compute: normalized critic confidence field or calibrated mapping from critic output.

### `critic_margin`

- kind: `comparative`
- what it counts: gap between best and second-best variant according to critic ranking.
- how to compute: if critic provides scores, subtract rank-2 score from rank-1 score; otherwise derive an ordinal margin from ranking evidence.

### `consensus_sample_count`

- kind: `continuous`
- what it counts: number of advisory samples or committee votes used.
- how to compute: count sampled advisory runs.

### `consensus_margin`

- kind: `comparative`
- what it counts: how strongly majority or plurality favored the selected advisory reading.
- how to compute: `winning_vote_count - runner_up_vote_count`.

### `critic_merge_recommended`

- kind: `comparative`
- what it counts: whether the critic thinks no single variant is fully adequate.
- how to compute: boolean flag from critic output.

### `semantic_coverage_retry_count`

- kind: `continuous`
- what it counts: how many times semantic coverage hints forced a retry.
- how to compute: count semantic-coverage-triggered repair rounds.

## 12. Efficiency and Runtime Metrics

These metrics answer: how expensive the translation was.

### `llm_call_count`

- kind: `continuous`
- what it counts: total number of model completions in the run.
- how to compute: count assistant/completion turns emitted by the runtime.

### `successful_llm_call_count`

- kind: `continuous`
- what it counts: successful model completions.
- how to compute: count completion calls that returned valid responses.

### `failed_llm_call_count`

- kind: `continuous`
- what it counts: failed model completions.
- how to compute: `llm_call_count - successful_llm_call_count`.

### `timeout_count`

- kind: `continuous`
- what it counts: number of model or network calls that failed by timeout.
- how to compute: count logged timeout exceptions.

### `wall_clock_seconds`

- kind: `continuous`
- what it counts: end-to-end runtime for the entry.
- how to compute: run end time minus run start time.

### `avg_call_latency_s`

- kind: `continuous`
- what it counts: average latency of one successful model completion.
- how to compute: mean of per-call durations.

### `max_call_latency_s`

- kind: `continuous`
- what it counts: slowest successful model completion.
- how to compute: maximum of per-call durations.

### `repair_calls_count`

- kind: `continuous`
- what it counts: number of completions spent on repair rather than first-pass generation.
- how to compute: count completion calls tied to validator or critic repair prompts.

### `cost_estimate_tokens_in`

- kind: `continuous`
- what it counts: approximate prompt-token budget consumed.
- how to compute: sum prompt-token counts from logged completions when available.

### `cost_estimate_tokens_out`

- kind: `continuous`
- what it counts: approximate completion-token budget consumed.
- how to compute: sum completion-token counts from logged completions when available.

## 13. Gold-Only Metrics

These metrics answer: how close the result is to a hand-authored gold target.

### `gold_clause_alignment`

- kind: `gold_only`
- what it counts: fraction of gold semantic blocks aligned by the candidate IR.
- how to compute: align candidate clause coverage map against gold clause inventory.

### `gold_scope_recall`

- kind: `gold_only`
- what it counts: share of gold scope semantics preserved.
- how to compute: `matched gold scope fragments / total gold scope fragments`.

### `gold_exception_recall`

- kind: `gold_only`
- what it counts: share of gold exclusion semantics preserved.
- how to compute: `matched gold exception fragments / total gold exception fragments`.

### `gold_counterfactual_recall`

- kind: `gold_only`
- what it counts: share of gold counterfactual semantics preserved.
- how to compute: `matched gold counterfactual fragments / total gold counterfactual fragments`.

### `gold_dependency_recall`

- kind: `gold_only`
- what it counts: share of explicit concept links in gold that are preserved in the candidate.
- how to compute: `matched gold dependency links / total gold dependency links`.

### `gold_structure_similarity`

- kind: `gold_only`
- what it counts: structural similarity modulo renaming between candidate IR and gold IR.
- how to compute: compare declaration graph, assertion skeleton, and operator shapes after normalization of names.

### `gold_render_similarity`

- kind: `gold_only`
- what it counts: semantic similarity between candidate render-back and gold render-back.
- how to compute: BERTScore, NLI, or clause-aligned similarity on verbalized forms.

### `gold_modulo_renaming_match`

- kind: `gold_only`
- what it counts: whether candidate and gold are equivalent up to safe renaming and trivial formatting differences.
- how to compute: canonicalize names and compare normalized structure.

### `gold_helper_overuse_delta`

- kind: `gold_only`
- what it counts: how much more helper machinery the candidate introduces than the gold.
- how to compute: `candidate helper count - gold helper count`.

## 14. Variability and Stability Metrics

These metrics answer: if we rerun the same stage or the same full pipeline, how much does the artifact move?

### `usable_variant_count`

- kind: `comparative`
- what it counts: number of drafted variants that are actually usable for comparison.
- how to compute: count variants with `status = ok`, canonical AST, and non-empty rendered IR.

### `unique_variant_signature_count`

- kind: `comparative`
- what it counts: how many materially distinct IR outputs appear inside one run.
- how to compute: normalize rendered IR strings and count distinct values, or cluster by structural signature.

### `focus_signature_unique_count`

- kind: `comparative`
- what it counts: how many different focus-symbol signatures appear across variants or reruns.
- how to compute: extract the declared signature of the focus term, for example `rel(IndexComponent,Day)` vs `rel(Day,Exchange)`, and count unique values.

### `focus_signature_mode_share`

- kind: `comparative`
- what it counts: how dominant the most common focus-symbol signature is.
- how to compute: `max(signature frequency) / usable_variant_count`.

### `pairwise_structure_similarity_mean`

- kind: `comparative`
- what it counts: mean structural similarity between all pairs of variants or reruns.
- how to compute: compare declaration mix, logical-operator mix, and arity profile pairwise; average the pairwise cosine similarities.

### `pairwise_structure_distance_mean`

- kind: `comparative`
- what it counts: mean structural drift between all pairs of variants or reruns.
- how to compute: `1 - pairwise_structure_similarity_mean`.

### `pairwise_token_jaccard_mean`

- kind: `comparative`
- what it counts: average lexical overlap between rendered IR artifacts.
- how to compute: compute content-token Jaccard for every pair, then average.

### `artifact_signature_entropy`

- kind: `comparative`
- what it counts: how evenly the artifact space is spread across distinct signatures rather than collapsing to one dominant form.
- how to compute: Shannon entropy over normalized artifact signatures or focus signatures.

### `same_parameter_mass_different_structure_pair_count`

- kind: `comparative`
- what it counts: how often two artifacts have the same total parameter mass but different structure.
- how to compute: among all pairs, count those with equal `total_parameter_slot_mass` but non-identical structural signature.

### `same_parameter_mass_different_structure_pair_ratio`

- kind: `comparative`
- what it counts: rate of decomposition drift after controlling for parameter mass.
- how to compute: `same_parameter_mass_different_structure_pair_count / total_pair_count`.

### `avg_structure_similarity_to_other_successful_runs`

- kind: `comparative`
- what it counts: how close the current artifact is to the rest of the successful cohort.
- how to compute: for the chosen artifact, compute mean structure similarity to every other successful artifact in the cohort.

## 15. Parameterization and Factorization Metrics

These metrics answer: how much argument structure the artifact uses, regardless of how that structure is factorized.

### `callable_symbol_count`

- kind: `continuous`
- what it counts: number of declared callable local symbols.
- how to compute: count local `fun` and `rel` declarations.

### `callable_symbol_with_args_count`

- kind: `continuous`
- what it counts: number of callable local symbols that actually take arguments.
- how to compute: count local `fun` and `rel` declarations whose arity is greater than zero.

### `top_level_parameter_slot_count`

- kind: `continuous`
- what it counts: total argument slots declared at symbol level.
- how to compute: sum the arities of all local `fun` and `rel` declarations.

### `quantifier_parameter_slot_count`

- kind: `continuous`
- what it counts: total bound-variable slots introduced by quantifiers.
- how to compute: recursively count variables introduced by `forall` and `exists` nodes in assertions.

### `total_parameter_slot_mass`

- kind: `continuous`
- what it counts: total parameter burden of the artifact, independent of how it is factorized.
- how to compute: `top_level_parameter_slot_count + quantifier_parameter_slot_count`.

### `factorization_count`

- kind: `continuous`
- what it counts: how many separate callable factors carry argument structure.
- how to compute: count local callable symbols whose arity is greater than zero.

### `parameter_slots_per_factor`

- kind: `continuous`
- what it counts: average argument mass per factor.
- how to compute: `top_level_parameter_slot_count / max(1, factorization_count)`.

### `factorization_index`

- kind: `continuous`
- what it counts: how fragmented the argument structure is.
- how to compute: `factorization_count / max(1, top_level_parameter_slot_count)`.

### `focus_symbol_signature`

- kind: `comparative`
- what it counts: the effective carrier signature chosen for the focus term.
- how to compute: inspect the declaration for the focus term and serialize it as a normalized signature, for example `rel(IndexComponent,Day)` or `fun(IndexComponent)->Exchange`.

### `focus_symbol_arity`

- kind: `comparative`
- what it counts: the arity chosen for the focus term itself.
- how to compute: read the declared argument count of the focus symbol.

## 16. Normalized-Relative Density Metrics

These metrics answer: how expensive the IR became relative to the size of the normalized input.

### `new_formula_content_token_rate_vs_reference_mass`

- kind: `continuous`
- what it counts: density of newly introduced content tokens in formal IR relative to normalized token mass.
- how to compute: `new_formula_content_token_count / normalized_content_token_mass`.

### `new_full_surface_content_token_rate_vs_reference_mass`

- kind: `continuous`
- what it counts: density of newly introduced content tokens across IR plus prose relative to normalized token mass.
- how to compute: `new_full_surface_content_token_count / normalized_content_token_mass`.

### `formula_repeat_overuse_rate`

- kind: `hard_warning`
- what it counts: repetition inflation in formal IR relative to normalized token mass.
- how to compute: `formula_repeat_overuse_mass / normalized_content_token_mass`.

### `full_surface_repeat_overuse_rate`

- kind: `hard_warning`
- what it counts: repetition inflation across IR plus prose relative to normalized token mass.
- how to compute: `full_surface_repeat_overuse_mass / normalized_content_token_mass`.

### `parameter_slot_mass_per_clause`

- kind: `continuous`
- what it counts: how much parameter structure the IR spends per normalized clause.
- how to compute: `total_parameter_slot_mass / normalized_clause_count`.

### `parameter_slot_mass_per_reference_token`

- kind: `continuous`
- what it counts: how much parameter structure the IR spends per normalized content token.
- how to compute: `total_parameter_slot_mass / normalized_content_token_mass`.

### `factorization_per_clause`

- kind: `continuous`
- what it counts: how fragmented the callable structure is per normalized clause.
- how to compute: `factorization_count / normalized_clause_count`.

### `factorization_per_reference_token`

- kind: `continuous`
- what it counts: how fragmented the callable structure is relative to normalized token mass.
- how to compute: `factorization_count / normalized_content_token_mass`.

### `notes_content_token_rate_vs_reference_mass`

- kind: `hard_warning`
- what it counts: how much content mass is parked in notes relative to normalized input size.
- how to compute: `notes_content_token_count / normalized_content_token_mass`.

## 17. Tradeoff Metrics

These metrics answer: how much semantic fidelity or stability we get per unit of structural cost.

### `render_bertscore_f1_to_normalized_per_parameter_slot_mass`

- kind: `comparative`
- what it counts: normalized-text similarity divided by parameter mass.
- how to compute: `render_bertscore_f1_to_normalized / total_parameter_slot_mass`.

### `render_nli_ir_implies_text_per_parameter_slot_mass`

- kind: `comparative`
- what it counts: entailment from IR render-back to normalized text per unit of parameter mass.
- how to compute: `render_nli_ir_implies_text / total_parameter_slot_mass`.

### `render_nli_text_implies_ir_per_parameter_slot_mass`

- kind: `comparative`
- what it counts: entailment from normalized text back to IR render-back per unit of parameter mass.
- how to compute: `render_nli_text_implies_ir / total_parameter_slot_mass`.

### `render_bertscore_f1_to_normalized_per_formula_repeat_overuse_mass`

- kind: `comparative`
- what it counts: normalized-text similarity per unit of repetition inflation inside formal IR.
- how to compute: `render_bertscore_f1_to_normalized / formula_repeat_overuse_mass`.

### `render_nli_text_implies_ir_per_formula_repeat_overuse_mass`

- kind: `comparative`
- what it counts: semantic adequacy per unit of formal repetition inflation.
- how to compute: `render_nli_text_implies_ir / formula_repeat_overuse_mass`.

### `render_nli_text_implies_ir_per_full_surface_repeat_overuse_mass`

- kind: `comparative`
- what it counts: semantic adequacy per unit of repetition inflation across IR plus prose.
- how to compute: `render_nli_text_implies_ir / full_surface_repeat_overuse_mass`.

### `pairwise_structure_similarity_mean_per_parameter_slot_mass`

- kind: `comparative`
- what it counts: structural stability bought per unit of parameter mass.
- how to compute: `pairwise_structure_similarity_mean / total_parameter_slot_mass`.

### `focus_signature_mode_share_per_parameter_slot_mass`

- kind: `comparative`
- what it counts: carrier-stability bought per unit of parameter mass.
- how to compute: `focus_signature_mode_share / total_parameter_slot_mass`.

## Minimal Recommended Scoreboard

If only a first version is implemented, the recommended minimum scoreboard is:

- `ast_valid`
- `combined_validation_ok`
- `ungrounded_symbol_count`
- `new_surface_content_token_count`
- `normalized_clause_count`
- `formula_bearing_item_count`
- `clause_coverage_ratio`
- `covered_only_in_notes_count`
- `prose_leak_count`
- `explicit_link_violation_count`
- `scope_visibility_violation_count`
- `exception_visibility_violation_count`
- `counterfactual_loss_count`
- `declaration_only_downgrade_flag`
- `vacuous_constraint_flag`
- `render_content_token_recall`
- `render_nli_ir_implies_text`
- `render_nli_text_implies_ir`
- `unique_ir_variant_count`
- `pairwise_structure_distance_mean`
- `total_parameter_slot_mass`
- `factorization_count`
- `same_parameter_mass_different_structure_pair_ratio`
- `critic_confidence`
- `llm_call_count`
- `wall_clock_seconds`

## Recommended Implementation Order

### Phase 1

Implement immediately because most of the ingredients already exist in the current pipeline.

- validity metrics
- grounding metrics
- clause coverage metrics
- prose leak metrics
- basic variant metrics
- runtime metrics

### Phase 2

Implement next because they directly address current failure modes in `N10`, `N30`, and `N31`.

- `new_surface_content_token_count`
- `explicit_link_violation_count`
- `scope_visibility_violation_count`
- `exception_visibility_violation_count`
- `counterfactual_loss_count`
- `vacuous_constraint_flag`
- `declaration_only_downgrade_flag`

### Phase 3

Implement once render-back infrastructure exists.

- BERTScore-based render metrics
- NLI-based entailment and contradiction metrics
- targeted semantic probes

### Phase 4

Implement only for benchmark mode.

- full gold-comparison family

## Notes

- No single metric should decide semantic quality alone.
- `hard_fail` metrics protect validity and grounding.
- `hard_warning` metrics expose semantic drift and prose leakage.
- `continuous` metrics make it possible to compare runs, models, and pipeline variants over time.
- `gold_only` metrics should never be used to guide generation in cleanroom mode.
