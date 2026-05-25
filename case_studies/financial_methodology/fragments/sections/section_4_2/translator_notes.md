# Section 4.2 Translator Notes

This file records translator decisions for the current `main_ir.a4v3`.
It is review memory, not an additional source of methodology claims.

## Changelog

### 2026-05-14T23:20:00+02:00

Decision: synthesize the final IR from the three drafts, using Copy 2 as the
base and applying the financial methodology patterns already used in adjacent sections.

Accepted:

- Use reified event carriers for `IndexCalculation`, `IndexTermination`, and
  `TerminationAnnouncement`, because the source ties termination and
  announcement to the event where the adjusted return Index is calculated as
  zero or below zero.
- Use `IndexLevel extends Real`, not `Int`, because Index levels may be
  decimal-valued and the source only requires comparison against zero.
- Use `AsSoonAsReasonablyPossible : VagueTerm` for the timing phrase instead
  of hiding the phrase in a unary predicate.
- Use `SolactiveOrganization extends Organization` and
  `entity Solactive : SolactiveOrganization` so the deontic permission has a
  typed agent parameter rather than `agent: Solactive`.
- Model the News area as `NewsSection : DocumentPart`, with
  `section_of_website(NewsSection, SolactiveWebsite)` and the source URL
  preserved through `document_part_url(...)`.
- Keep both website-level and section-level announcement placement:
  `announced_on(a, SolactiveWebsite)` and
  `announcement_under_section(a, NewsSection)`.
- Represent the clarification sentence as a permission for Solactive to
  terminate an Index for `OtherReasons : VagueTerm` under
  `SolactivePolicies`. The source phrase "other reasons" is an open-ended
  legal qualifier, not a defined taxonomy of termination reason kinds.
- Keep `termination_in_accordance_with_policy(...)` as an explicit relation for
  concrete termination events, not only as the deontic `scope` metadata.

Rejected / alternatives:

- Do not use Copy 3's direct `index_level(i) <= 0` pattern; it loses the source
  phrase "is calculated as zero or below zero" and weakens the temporal link to
  the announcement.
- Do not use `OtherReasons` as the deontic scope; the vague reason qualifier
  explains the permission, while the policy framework is the natural scope.
- Do not model `as soon as reasonably possible` as only a unary flag on an
  announcement; it is a vague timing qualifier.

Validation notes:

- Parser strict passes with zero warnings.
- Semantic lint has no strong findings and no numeric-sort findings.
- The soft `shared_name_token_without_structural_carrier` findings for
  `announc` and `calculat` are accepted as checker false positives for this
  file: the structural carriers are the typed variables
  `a: TerminationAnnouncement` and `c: IndexCalculation`.
- The advisory `temporal_rel_in_deontic_context` finding is expected because
  this section has both a deontic permission and a source-required temporal
  `after(a, c)` relation.
- Full clean gate remains `needs_review` until provenance/back-translation and
  token coverage are added.
