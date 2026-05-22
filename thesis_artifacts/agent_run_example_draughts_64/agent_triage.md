# Agent v2 triage — rules_core

- **Final decision: failed_after_meta** (agent proposed: failed_after_meta)
- Override reason: IR gate did not pass — see lint/family_coverage findings.
- Generated at: 2026-05-19T12:25:50Z
- Agent summary: Cannot proceed past IR_IN_FLUX phase due to 2 blocking lowering smells and 2 blocking family coverage gaps that persist despite multiple iterations. The IR (502 lines) comprehensively covers all rules from Sections 2-4 of the IDF Draughts-64 rules with 0 strong lint findings. The blocking issues are tool-level: (1) family coverage checker doesn't recognize permission/prohibition blocks as satisfying modality signals from source text, and (2) lowering audit reports 2 smells whose cause could not be isolated across 15+ IR variants. The IR itself is semantically valid and source-faithful.

- Agent notes: The IR covers: board geometry (2.1), piece setup (2.2), movement rules (3.1-3.13), capture rules (4.1-4.15), and Brazilian variant rules (4.16.1-4.16.3). Uses AssertDecl facts for definitions, DeonticDecl obligations for 'must'/'has to' rules, prohibitions for 'forbidden'/'cannot' rules, and permissions for 'may'/'choice' rules. All identifiers are source-traceable. The 3 soft lint findings (arity > 2 relations) are acceptable with provenance documentation. The 'announces' symbol is grounded by source phrase 'has to announce beforehand'. The lowering smells (n=2, blocking) could not be isolated despite systematic bisection testing across 15+ variants — they only appear in the full IR and not in any minimal reproduction, suggesting an interaction effect.

## Metrics

- ir_gate_passed: `False`
- lint_strong: `None`
- lint_soft: `None`
- clean_gate: `None`
- blocking_conditions: `[]`
- family_gaps_total: `5`
- family_gaps_blocking: `3`
- family_gaps_overridden_by_intent: `2`
- lowering_smells_total: `0`
- lowering_smells_blocking: `0`
- lowering_smells_overridden_by_intent: `0`
- corpus_alignment_mode: `None`
- corpus_alignment_agreement: `None`
- corpus_alignment_distribution: `{}`
- corpus_alignment_worst_verdict: `None`
- needs_context_count: `None`
- waivers_suggested: `0`
- parts_inventory_unsatisfied_required: `1`
- agent_steps_used: `67`
- agent_total_tokens: `5060963`
