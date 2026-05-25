# Merge Readiness Audit v1

Status: `passed`

## Summary

- `entry_count`: 55
- `declaration_count`: 1530
- `rule_bearing_declaration_count`: 1329
- `bridged_rule_bearing_declaration_count`: 351
- `bridge_family_count`: 68
- `bridge_symbol_count`: 442
- `hard_findings`: 0
- `soft_findings`: 0
- `advisory_findings`: 0

## Candidate Audit Snapshot

- `parse_warning_count`: 0
- `unbridged_repeated_exact_count`: 0
- `same_name_different_signature_count`: 27
- `same_name_different_signature_uncovered_count`: 0
- `lexical_candidate_count`: 53
- `lexical_uncovered_by_bridge_symbol_guess_count`: 0
- `source_phrase_candidate_count`: 28
- `source_phrase_uncovered_count`: 0
- `assertion_external_identifier_count`: 0

## Findings

No findings.

## Interpretation

Hard findings block merge. Soft findings require an explicit merge decision. Advisory findings are review prompts, especially for type-gap risks where a post-merge contradiction may fail only because a membership edge is missing.
