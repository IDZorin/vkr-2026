# Role Annotation Judge: section_4_1

- status: `ok`
- model: `gpt-5.4-mini`
- verdict: `consistent`
- frame_alignment: `correct`
- confidence: `0.95`

## Reason

The role annotations preserve the semantic direction and argument roles of the annotated IR relations, including scope, subject, component, basis, source/target, and time ordering. The displayed adjusted-return formula is correctly framed as applying to SOLTCA50 per the translator notes, and the ex-date/effective-date equality is consistent with the source wording. No material role reversals or unsupported semantic additions appear in the annotated items.

## Issues

- none

## Suggestions

- Keep the current role labels for the formula-factor relations; if future normalization is needed, add carrier entities rather than changing the existing semantic roles.
- If desired, add an explicit role annotation for `formula_applies_to_index` in a future pass, but it is not required for consistency here.
