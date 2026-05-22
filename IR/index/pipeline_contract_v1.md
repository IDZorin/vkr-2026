# Pipeline Contract v1

Public release note: this document describes the broader research pipeline.
Some referenced private agent prompts and repair-orchestration policies are not
included in this public bundle. For a publication-safe baseline prompt, use
`../../prompts/a4v3_ir_translation_prompt_public_v1.md`.

This document organizes the existing rules, metrics, checks, and agent
instructions by transformation stage.

It does not replace the metric catalog or policy files. It is the routing
contract that says which existing material applies at each transition.

## Top-Level Pipeline

```text
Text
  -> Normalization
  -> IR
  -> Merge
```

Each transition has:

- input and output artifacts
- allowed transformations
- forbidden transformations
- deterministic metrics
- checklist or lint checks
- agent instructions
- user-hint handling

## Global Rule: User Hints

User hints may apply at any transition.

They must not be treated as hidden agent memory. They should be recorded
as plain text with provenance.

Recommended shape:

```text
hint_id: H001
scope: global | block:<id> | transition:text_to_normalization | transition:normalization_to_ir | transition:ir_to_merge
text: <user supplied hint>
status: active | superseded | rejected
used_in: <artifacts or decisions>
```

If a hint changes a local constraint, the artifact must show that the
change came from user clarification. If a hint only supplies ontology
support, it should usually live in declarations, notes, or overlay.

## Stage 1. Text -> Normalization

### Purpose

Rewrite source methodology text into normalized clauses while preserving
meaning and making later IR construction easier.

### Inputs

- raw methodology text
- `source.md`
- relevant user hints

### Outputs

- `normalized.md`
- `notes.md`
- optional correction notes
- optional previous version such as `normalized_old_vN.md`

### Source Files

- `normalization_rules_v1.md`
- `docs/translation_stage_checklists/normalization_checklist.md`
- `configs/translation_quality/translation_stage_checklists.yaml`
- `translation_agent_operating_prompt_v1.md`, Step 1

### Existing Instructions

From `normalization_rules_v1.md`:

1. Put the named term in subject position.
2. Normalize from general to specific.
3. Use repetition only to expose structure.
4. Keep one main logic burden per clause.
5. Split operationally different content.
6. Repair broken source syntax, but do not invent new substance.
7. Prefer explicit antecedents over vague pronouns when the IR will need them.
8. State abstract objects first for fractions, sets, or selected values.
9. Keep clarification clauses visibly non-core.
10. Preserve old normalization when changing it.

Working heuristic:

1. `NamedTerm is CoreDefinition.`
2. `This applies to ...`
3. `This also applies to ...`
4. `NamedTerm also includes / excludes ...`
5. `For clarification ...`
6. `Authority / governance ...`

### Allowed Transformations

- preserve the source wording where possible
- split text into clauses when it exposes structure
- repeat terms or scope only to preserve links between normalized clauses
- repair typos, casing, punctuation, or broken syntax when documented
- add minimal prelude/context only when required to keep a referent clear

### Forbidden Transformations

- delete an actor, condition, number, exception, obligation, or authority
- add a legal/domain condition not present in the source
- make vague text more certain than the source
- split clauses so that scope or exceptions become hidden
- repeat content as padding
- silently hide surface corrections

### Checklist Checks

From the normalization checklist:

- `preserve_meaning`: no actor, condition, number, exception, or obligation disappears or appears
- `make_edits_explicit`: typos, casing, and punctuation cleanups are recorded
- `keep_clause_boundaries_honest`: splitting does not hide logic
- `avoid_padding_or_repetition`: no filler or duplicated content
- `keep_unresolved_ambiguity_visible`: no invented certainty

### Validator Codes

From `translation_stage_checklists.yaml`:

- `silent_deletion`
- `silent_addition`
- `lexical_preservation_below_threshold`
- `invalid_surface_correction`
- `definition_role_alignment_failed`
- `normalization_duplicate_content_repetition`

### Metrics

Primary source-to-normalized metrics:

- `source_excerpt_content_token_count`
- `source_excerpt_content_token_mass`
- `normalized_content_token_count`
- `normalized_content_token_mass`
- `normalized_content_token_recall_from_source`
- `normalized_content_token_precision_to_source`
- `normalized_content_token_jaccard`
- `normalized_content_token_multiset_recall_from_source`
- `normalized_content_token_multiset_precision_to_source`
- `source_to_normalized_token_gap_count`
- `normalized_to_source_new_token_count`
- `normalized_repeat_overuse_token_count`
- `normalized_repeat_overuse_mass`
- `normalized_repeat_overuse_examples`
- `normalized_length_ratio_vs_source_mass`
- `normalized_content_mass_per_clause`
- `source_normalized_bertscore_f1`
- `normalized_implies_source_entailment`
- `source_implies_normalized_entailment`
- `source_vs_normalized_contradiction_score`

Checklist score fields:

- `content_token_recall`
- `content_token_precision`
- `content_token_multiset_recall`
- `content_token_multiset_precision`
- `threshold`
- `duplication_suspected`

## Stage 2. Normalization -> IR

This transition has two required substeps:

```text
Normalized
  -> Concepts / Ontology Plan
  -> Formula IR
```

The first substep is not optional. The formula should not be drafted
directly from prose without extracting carriers, value families,
relations, and ontology support.

## Stage 2A. Normalized -> Concepts / Ontology Plan

### Purpose

Identify the things the IR must talk about before writing formulas.

### Inputs

- `normalized.md`
- `source.md`
- relevant user hints
- existing local declarations
- available prelude / shared ontology

### Outputs

- candidate sorts
- candidate entities
- candidate enum/value families
- candidate functions
- candidate relations
- carriers
- authority/source objects
- fallback triggers
- ontology links
- unresolved questions

### Source Files

- `ontology_declaration_policy_v1.md`
- `semantic_shape_policy_v1.md`
- `definition_archetypes_v1.md`
- `identifier_shape_and_anchor_policy_v1.md`
- `translation_agent_operating_prompt_v1.md`, Steps 2 and 3

### Existing Instructions

From `ontology_declaration_policy_v1.md`:

- declarations may use general ontology and ordinary domain meaning
- constraints must stay source-faithful
- build the ontology skeleton first
- declare symbols at the ontology level
- write constraints strictly from the text
- keep plausible but not locally licensed mappings in overlay

From `semantic_shape_policy_v1.md`:

- choose shape before inventing helpers
- anchor the focus term directly
- prefer direct local shapes
- keep qualifications outside the focus name
- avoid over-reification
- keep carrier choice honest
- prefer explicit constraints over clever helper names

From `definition_archetypes_v1.md`, supported definition shapes:

- `carrier_predicate_definition`
- `qualified_value_definition`
- `fallback_value_definition`
- `role_bearer_definition`
- `reference_term_definition`
- `event_condition_definition`
- `mapping_or_value_family_definition`

### Allowed Transformations

- introduce sorts and declarations licensed by text, world ontology, prelude, or user hint
- separate value type, carrier, role, source, authority, and condition
- record ontology support before formula drafting
- keep local text claims separate from world-level bridges

### Forbidden Transformations

- turn ontology guesses into local constraints without source license
- introduce a helper only because it makes formula writing easier
- hide a concept link inside a long symbol name
- collapse different ontology levels into one symbol
- choose a carrier that loses the real local subject of the clause

### Checks

Ontology checklist:

- declarations use real-world ontology rather than accidental wording
- constraints remain literal and source-faithful
- important concept links are not buried only in symbol names
- editorial inconsistency is handled in declarations or overlay, not by distorting constraints

Identifier-anchor checks:

- important identifier tokens have a structural anchor
- accepted anchor source is `methodology`, `ontology`, `overlay`, `user_clarification`, or `waiver`
- clause-shaped identifiers are rejected or repaired
- compact noun/value-family identifiers are allowed when they do not hide conditions

Declaration / ontology lint checks:

- `same_symbol_different_codomains`
- `ontology_level_mixing`
- `overlay_consistency_drift`
- `numeric_window_fusion_forbidden`
- `semantic_load_in_name`
- `opaque_helper_predicates`
- `composite_identifier_crosslink_gap`
- `canonical_subterm_reuse_gap`
- `identifier_structural_anchor_gap`

### Metrics

Grounding and invention metrics:

- `ungrounded_symbol_count`
- `ungrounded_sort_count`
- `ungrounded_ref_count`
- `ungrounded_callee_count`
- `prelude_redeclaration_count`
- `new_formula_token_count_vs_text_only`
- `new_formula_content_token_count_vs_text_only`
- `new_full_surface_token_count_vs_text_only`
- `new_full_surface_content_token_count_vs_text_only`
- `invented_helper_symbol_count`
- `invented_helper_sort_count`
- `new_surface_token_count`
- `new_surface_content_token_count`
- `advisory_only_symbol_count`
- `text_licensed_symbol_ratio`
- `prelude_symbol_ratio`

Link and ontology preservation metrics:

- `explicit_link_violation_count`
- `embedded_concept_without_formula_link_count`
- `carrier_choice_stability`
- `arg_arity_stability`
- `sort_choice_stability`
- `dependency_link_count`
- `dependency_link_recall`
- `cross_reference_usage_count`
- `cross_reference_dropout_count`

Identifier glue metrics:

- `identifier_count`
- `compound_identifier_count_raw`
- `compound_identifier_count_content`
- `compound_identifier_rate_raw`
- `compound_identifier_rate_content`
- `max_identifier_piece_count_raw`
- `max_identifier_piece_count_content`
- `mean_identifier_piece_count_raw`
- `mean_identifier_piece_count_content`
- `identifier_glue_excess_mass_raw`
- `identifier_glue_excess_mass_content`
- `identifier_glue_excess_rate_raw`
- `identifier_glue_excess_rate_content`
- `source_grounded_content_piece_ratio_mean`
- `advisory_grounded_content_piece_ratio_mean`
- `low_source_grounded_glued_identifier_count`
- `low_source_grounded_glued_identifier_rate`
- `top_glued_identifiers`
- `lowest_source_grounded_identifiers`

## Stage 2B. Concepts / Ontology Plan -> Formula IR

### Purpose

Write local A4V3 formulas from the normalized text and the extracted
ontology plan.

### Inputs

- normalized clauses
- source text
- ontology plan
- user hints with provenance
- prelude

### Outputs

- `main_ir.a4v3`
- local declarations
- local source-faithful constraints
- local notes if needed

### Source Files

- `docs/translation_stage_checklists/ir_checklist.md`
- `semantic_shape_policy_v1.md`
- `definition_archetypes_v1.md`
- `identifier_shape_and_anchor_policy_v1.md`
- `translation_metrics_catalog_v1.md`
- `translation_agent_operating_prompt_v1.md`, Steps 4-7

### Existing Instructions

Formula construction must:

- write clear declarations
- write source-faithful constraints
- keep links explicit in formulas
- use the chosen archetype as binding for the first draft
- avoid hidden semantics only in names
- avoid abstract implementation-like reformulations
- avoid backend-shaped logic that no longer resembles the source

### Allowed Transformations

- use A4V3 syntax tokens
- use prelude tokens
- use normalized/source tokens
- use ontology tokens already justified in Stage 2A
- use user-hint tokens with provenance
- split one normalized sentence into several formula-bearing items when it has several logic burdens

### Forbidden Transformations

- introduce new semantic tokens without text, prelude, ontology, or user-hint support
- compress several logic burdens into one opaque helper
- hide fallback, exception, scope, authority, or compliance conditions in names
- represent important content only in comments or notes
- produce pseudo-IR prose that cannot parse or validate
- accept semantic judge success when deterministic hard failures remain

### Checklist Checks

From the IR checklist:

- `cover_every_normalized_block`: every normalized clause is represented
- `keep_links_explicit`: concept links are in formula structure, not only names
- `preserve_negation_scope_and_exceptions`: negation, scope, and exceptions are visible
- `keep_render_back_close_to_normalized_text`: render-back is semantically close
- `use_valid_ir_surface_forms`: IR parses and validates
- `keep_grounding_auditable`: important symbols have explicit support

### Validator Codes

From `translation_stage_checklists.yaml`:

- `formula_item_count_below_normalized_clause_count`
- `symbol_name_embeds_entity_without_explicit_link`
- `symbol_name_embeds_concept_without_explicit_link`
- `render_alignment_below_threshold`
- `missing_render_targets`
- `draft_ir_parse_failed`
- `draft_ir_validation_failed`

### Metrics

Validity metrics:

- `ast_valid`
- `ast_error_count`
- `declaration_shape_error_count`
- `assertion_shape_error_count`
- `expr_shape_error_count`
- `rendering_ok`
- `combined_validation_ok`
- `legacy_surface_token_count`
- `schema_repair_round_count`
- `parse_retry_count`

Clause coverage metrics:

- `normalized_clause_count`
- `formula_bearing_item_count`
- `clause_coverage_ratio`
- `uncovered_clause_count`
- `multi_clause_merge_count`
- `support_only_clause_count`
- `support_only_clause_ratio`
- `covered_only_in_notes_count`
- `missing_fragment_count`
- `prose_leak_count`

Lexical and content coverage metrics:

- `content_token_recall`
- `content_token_precision`
- `content_token_jaccard`
- `content_token_multiset_recall`
- `content_token_multiset_precision`
- `source_content_token_mass`
- `formula_content_token_mass`
- `full_surface_content_token_mass`
- `formula_repeat_overuse_token_count`
- `formula_repeat_overuse_mass`
- `formula_repeat_underuse_token_count`
- `formula_repeat_underuse_mass`
- `formula_repeat_overuse_examples`
- `full_surface_repeat_overuse_token_count`
- `full_surface_repeat_overuse_mass`
- `full_surface_repeat_overuse_examples`
- `focus_term_explicitly_modeled`
- `focus_term_in_top_level_decl`
- `focus_term_in_formula_body`
- `source_to_ir_token_gap_count`
- `ir_to_source_token_gap_count`

Scope, negation, and exception metrics:

- `scope_visibility_violation_count`
- `exception_visibility_violation_count`
- `negation_loss_count`
- `quantifier_loss_count`
- `guard_loss_count`
- `temporal_link_loss_count`
- `counterfactual_loss_count`
- `clarification_loss_count`
- `responsibility_loss_count`
- `procedural_note_leak_count`

Definition quality metrics:

- `declaration_only_downgrade_flag`
- `definition_body_present`
- `definitional_equation_present`
- `biconditional_present_when_expected`
- `vacuous_constraint_flag`
- `reflexive_equality_count`
- `opaque_support_symbol_count`
- `opaque_support_symbol_ratio`
- `helper_explosion_count`
- `core_term_centeredness_score`

Compression and readability metrics:

- `formula_to_clause_compression_ratio`
- `mean_significant_tokens_per_formula_item`
- `max_clause_collapse_size`
- `named_exclusion_count`
- `named_scope_predicate_count`
- `annotation_node_count`
- `notes_token_count`
- `notes_content_token_count`
- `notes_to_formula_content_ratio`

Assertion complexity metrics:

- `assertion_count`
- `mean_assertion_node_count`
- `max_assertion_node_count`
- `total_assertion_node_count`
- `mean_assertion_depth`
- `max_assertion_depth`
- `total_ite_count`
- `max_ite_count_per_assertion`
- `total_quantifier_count`
- `total_connective_count`
- `total_branching_point_count`
- `max_branching_point_count_per_assertion`
- `single_assertion_logic_share`
- `overcompressed_single_assertion_flag`
- `top_complex_assertions`

Normalized alignment metrics:

- `logic_block_count`
- `clause_to_logic_block_ratio`
- `logic_block_to_clause_ratio`
- `clause_underdecomposition_mass`
- `clause_overdecomposition_mass`
- `underdecomposed_logic_flag`

Render-back and semantic equivalence metrics:

- `render_back_available`
- `render_back_clause_count`
- `render_content_token_recall`
- `render_content_token_precision`
- `render_bertscore_f1_to_normalized`
- `render_bertscore_f1_to_source`
- `render_nli_ir_implies_text`
- `render_nli_text_implies_ir`
- `render_contradiction_score`
- `render_similarity_threshold_pass`

Targeted probe metrics:

- `probe_scope_preserved`
- `probe_exception_preserved`
- `probe_negation_preserved`
- `probe_counterfactual_preserved`
- `probe_clarification_preserved`
- `probe_responsibility_preserved`
- `probe_reference_preserved`
- `probe_temporal_order_preserved`
- `probe_value_source_preserved`

Normalized-relative density metrics:

- `new_formula_content_token_rate_vs_reference_mass`
- `new_full_surface_content_token_rate_vs_reference_mass`
- `formula_repeat_overuse_rate`
- `full_surface_repeat_overuse_rate`
- `parameter_slot_mass_per_clause`
- `parameter_slot_mass_per_reference_token`
- `factorization_per_clause`
- `factorization_per_reference_token`
- `notes_content_token_rate_vs_reference_mass`

## Stage 3. IR -> Merge

### Purpose

Preserve sentence-level/local IR provenance while building a shared
methodology-level ontology and canonical alignment layer.

### Inputs

- stable local IR blocks
- local metrics and local semantic judge results
- declaration lint reports
- existing overlays
- relevant user hints

### Outputs

- exact/shared alignment overlays
- ontology alignment overlays
- canonical symbol links
- bridge families
- role links
- conflict splits
- post-merge backtest reports

### Source Files

- `merge_alignment_policy_v1.md`
- `ontology_declaration_policy_v1.md`, Overlay Rule
- `translation_agent_operating_prompt_v1.md`, Step 8 and Section 6
- `translation_metrics_catalog_v1.md`

### Existing Layer Stack

From `merge_alignment_policy_v1.md`:

- `L0. Local clause IR`: local block remains judged on its own
- `L1. Exact/shared alignment overlay`: same name, kind, signature, meaning
- `L2. Ontology alignment overlay`: related meanings with separate local realization

### Merge Actions

- `exact_merge_overlay`: same symbol, kind, signature, and meaning
- `bridge_family`: same concept family with different carriers, codomains, or realizations
- `bridge_supertype`: different local sorts share a world-level supertype
- `role_link`: glossary/label term links to operational/domain role
- `keep_separate_with_link`: related meanings that should not be collapsed
- `conflict_split`: same surface symbol used at incompatible ontology levels

### Allowed Transformations

- record canonical aliases
- add overlay-only links
- create bridge relations
- propose symbol unification
- identify conflict splits
- use ordinary domain ontology at the merge layer
- rewrite local IR only after explicit proposal and successful backtest

### Forbidden Transformations

- silently rewrite local constraints to make ontology prettier
- collapse different ontology levels into one symbol
- force value mappings into local formulas when text does not license it
- accept local rewrites without backtest
- merge symbols only because names are similar
- lose sentence-level provenance

### Checks Before Merge

Hard declaration-layer checks:

- `same_symbol_different_codomains`
- `ontology_level_mixing`
- `overlay_consistency_drift`
- `numeric_window_fusion_forbidden`

Mapping/value-family checks:

- `enum_value_mapping_candidates`
- `codomain_split_value_families`

Soft structural warnings:

- `semantic_load_in_name`
- `opaque_helper_predicates`
- identifier-glue metrics
- `identifier_structural_anchor_gap`

### Checks After Merge

Overlay-only alignment acceptance:

- no new hard declaration-layer conflict
- no overlay drift
- ontology decision is recorded explicitly in overlay
- local formulas remain unchanged

Local rewrite after alignment acceptance:

- semantic verdict must not worsen
- relation type must not worsen
- higher-is-better metrics must not fall beyond tolerance
- lower-is-better metrics must not rise beyond tolerance

Current explicit backtest metrics:

- `semantic_verdict`
- `relation_type`
- `llm_bertscore`
- `llm_ir_to_text`
- `llm_text_to_ir`
- `llm_contradiction`
- deterministic proxies as fallback

### Metrics

Variant and committee metrics:

- `candidate_reading_count`
- `draft_variant_count`
- `unique_ir_variant_count`
- `variant_diversity_score`
- `critic_confidence`
- `critic_margin`
- `consensus_sample_count`
- `consensus_margin`
- `critic_merge_recommended`
- `semantic_coverage_retry_count`

Variability and stability metrics:

- `usable_variant_count`
- `unique_variant_signature_count`
- `focus_signature_unique_count`
- `focus_signature_mode_share`
- `pairwise_structure_similarity_mean`
- `pairwise_structure_distance_mean`
- `pairwise_token_jaccard_mean`
- `artifact_signature_entropy`
- `same_parameter_mass_different_structure_pair_count`
- `same_parameter_mass_different_structure_pair_ratio`
- `avg_structure_similarity_to_other_successful_runs`

Parameterization and factorization metrics:

- `callable_symbol_count`
- `callable_symbol_with_args_count`
- `top_level_parameter_slot_count`
- `quantifier_parameter_slot_count`
- `total_parameter_slot_mass`
- `factorization_count`
- `parameter_slots_per_factor`
- `factorization_index`
- `focus_symbol_signature`
- `focus_symbol_arity`

Gold-only metrics:

- `gold_clause_alignment`
- `gold_scope_recall`
- `gold_exception_recall`
- `gold_counterfactual_recall`
- `gold_dependency_recall`
- `gold_structure_similarity`
- `gold_render_similarity`
- `gold_modulo_renaming_match`
- `gold_helper_overuse_delta`

Tradeoff metrics:

- `render_bertscore_f1_to_normalized_per_parameter_slot_mass`
- `render_nli_ir_implies_text_per_parameter_slot_mass`
- `render_nli_text_implies_ir_per_parameter_slot_mass`
- `render_bertscore_f1_to_normalized_per_formula_repeat_overuse_mass`
- `render_nli_text_implies_ir_per_formula_repeat_overuse_mass`
- `render_nli_text_implies_ir_per_full_surface_repeat_overuse_mass`
- `pairwise_structure_similarity_mean_per_parameter_slot_mass`
- `focus_signature_mode_share_per_parameter_slot_mass`

## Cross-Cutting Agent Acceptance and Repair

### Source Files

- `agent_acceptance_policy_v1.md`
- `agent_issue_taxonomy_v1.md`
- `agent_repair_policy_v1.md`
- `agent_orchestrator_state_machine_v1.md`
- `translation_agent_contract_v1.md`
- `translation_agent_contract_v1.json`
- `translation_agent_operating_prompt_v1.md`

### Acceptance States

`accepted` requires:

- semantic verdict is `corresponds`
- `combined_validation_ok = 1`
- `hard_structural_issue_count = 0`
- `declaration_hard_issue_count = 0`
- `quality_issue_count = 0`

`soft_review` means:

- structurally usable
- semantic state is non-failing
- quality/modeling issues remain

`needs_review` means:

- any hard blocker remains
- semantic verdict is `does_not_correspond`
- combined validation fails

### Issue Taxonomy

Existing issue classes:

- `hard_structural`
- `declaration_conflict`
- `grounding`
- `carrier_modeling`
- `decomposition`
- `shape_mismatch`
- `quality_modeling`
- `semantic_mismatch`
- `judge_reliability`

### Repair Categories

From `agent_repair_policy_v1.md`:

- structural repairs
- quality repairs
- semantic repairs
- repair discipline

### Orchestrator States

From `agent_orchestrator_state_machine_v1.md`:

- run generation
- run deterministic checks
- run LLM checks
- classify issues
- repair if bounded limits allow
- accept, soft review, or manual escalation

## Cross-Cutting Efficiency Metrics

These apply to any automated transition.

- `llm_call_count`
- `successful_llm_call_count`
- `failed_llm_call_count`
- `timeout_count`
- `wall_clock_seconds`
- `avg_call_latency_s`
- `max_call_latency_s`
- `repair_calls_count`
- `cost_estimate_tokens_in`
- `cost_estimate_tokens_out`

## Minimal Scoreboard

From `translation_metrics_catalog_v1.md`, the minimum recommended
scoreboard is:

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

## Implementation Order

Existing catalog recommendation:

1. Phase 1: validity, grounding, clause coverage, prose leak, basic variant, runtime.
2. Phase 2: new surface content, explicit links, scope, exception, counterfactual, vacuous constraints, declaration-only downgrade.
3. Phase 3: render-back BERTScore, NLI entailment/contradiction, targeted semantic probes.
4. Phase 4: full gold-comparison family for benchmark mode.

## Current Organization Assessment

The existing repository already contains most of the rules and metrics,
but their organization is document-centered:

- normalization rules
- IR checklist
- ontology declaration policy
- semantic shape policy
- merge alignment policy
- metric catalog
- agent contract and repair policies

This contract makes the organization transition-centered:

- `Text -> Normalization`
- `Normalization -> Concepts / Ontology Plan`
- `Concepts / Ontology Plan -> Formula IR`
- `IR -> Merge`

The transition-centered view should be used by agents. The original
documents remain the source-of-truth references for detailed definitions.
