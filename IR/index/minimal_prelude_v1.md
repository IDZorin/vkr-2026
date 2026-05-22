# Minimal Prelude v1

This file defines the minimal shared ontology that the translation pipeline may use across methodologies.

## Purpose

Prelude symbols are allowed in IR without methodology-local redefinition.

They are:
- cross-methodology
- minimal
- read-only
- not a place for methodology-specific terms

Short rule:
- `IR = A4V3 + Prelude + original methodology text`

## Included Sorts

- `Day`
- `Month`
- `Weekday`
- `FinancialInstrument`
- `Event`
- `Organization`
- `Document`
- `DocumentPart`
- `DocumentLocator`
- `Period`
- `LookbackWindow`
- `WebResource`
- `Url`
- `VagueTerm`

All of these carry a non-empty witness policy.

## Included Calendar Entities

Weekdays:
- `Monday`
- `Tuesday`
- `Wednesday`
- `Thursday`
- `Friday`
- `Saturday`
- `Sunday`

Months:
- `January`
- `February`
- `March`
- `April`
- `May`
- `June`
- `July`
- `August`
- `September`
- `October`
- `November`
- `December`

## Included Functions

- `MonthOf : Day -> Month`
- `WeekdayOf : Day -> Weekday`

## Included Relations

- `occurs_on : Event, Day`
- `day_before : Day, Day`
- `has_url : WebResource, Url`
- `document_url : Document, Url`
- `part_of_document : DocumentPart, Document`
- `document_part_locator : DocumentPart, DocumentLocator`
- `document_part_url : DocumentPart, Url`

`Event` is only a generic carrier for dated occurrences. Methodology-specific event types should be introduced locally or in an alignment overlay, not directly in Prelude.

`Period` is the generic temporal duration/range carrier.
`LookbackWindow` is the shared carrier for backward-looking windows anchored by a methodology-local date or event.
Local entries should still define source-specific windows such as one-month or six-month lookbacks locally.

`DocumentPart` and `DocumentLocator` are generic provenance carriers for sections, paragraphs, clauses, tables, appendices, and URL fragments.
Concrete document titles, paragraph numbers, section names, and URL values should still be introduced locally or kept in provenance/waiver files.

`WebResource` and `Url` are generic reference carriers.
Concrete sites, documents, and URL values from a methodology should be local entities or provenance/waiver entries, not Prelude entities.

`VagueTerm` is the shared carrier for source terms that matter semantically but are not fully defined by the text.
Concrete vague terms such as a missing threshold, undefined qualitative standard, or unspecified predicate should be introduced locally.

## Excluded On Purpose

These do not belong in Prelude because they are methodology-specific:
- `TradingDay`
- `RebalanceDay`
- `SelectionDay`
- `RebalanceEvent`
- `SelectionEvent`
- `ExtraordinaryRebalanceEvent`
- `IndexUniverse`
- `FreeFloat`

## Witness Policy

Prelude sorts are not meant to be empty decorative types.

Standing rule:
- the type of case should not be empty
- its instance should be possible / admissible / existent in some scenario

This does not force every methodology-specific definition to inline an existential claim.
It means the shared base ontology is intended to be inhabited.
