# Corpus-Aware Multi Judge: section_1_5

- generated_at: `2026-05-10T22:25:42+02:00`
- skipped: `False`
- local_source_alignment_mode: `corresponds`
- corpus_alignment_mode: `corresponds`
- corpus_alignment_agreement: `1.0`
- needs_context_count: `1`
- mean_confidence: `0.954`

## Included Context

```json
{
  "entry": "section_1_5",
  "entry_dir": "D:\\OneDrive\\Documents\\Study\\MIPT\\VKR\\research_experiments\\2026-02_pipeline\\case_studies\\financial_methodology\\sections\\section_1_5",
  "global_bridge": true,
  "related_sections": [],
  "artifacts": {
    "source.md": true,
    "normalized.md": true,
    "main_ir.a4v3": true,
    "repair.a4v3": false,
    "provenance.yaml": true,
    "translator_notes.md": true,
    "waivers.yaml": false,
    "waivers_v1.yaml": false
  }
}
```

## Judges

### gpt-5.4-mini

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `provenance, translator_notes, bridge`
- confidence: `0.96`

Reason:

The IR captures the source’s licensing statement as a permission for Solactive to issue licenses to use the Index as underlying value, and it records the listed use categories and recipient categories. The class/issuance carriers and the instance-to-class bridge are explicitly documented in provenance and translator notes, and they do not contradict the source.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR is structurally reified and more explicit than the prose source, but this is a modeling choice rather than semantic drift.
- `SolactiveOrganization`, `LicenseClass`, and `LicenseIssuance` are local carrier types introduced for formalization.

### gpt-5.4

- local_source_alignment: `partially_corresponds`
- corpus_alignment: `corresponds`
- relation_type: `same_meaning_poor_wording`
- needs_context: `True`
- context_used: `provenance, translator_notes`
- confidence: `0.93`

Reason:

The local IR captures the sentence's core content: licenses concerning use of the Index as underlying value, the three use categories, the four recipient categories, and Solactive as issuer, with 'may be issued' rendered deontically. Source-only, the class/issuance reification and the universal instance-to-class bridge make the mapping less directly readable and can look like over-structuring rather than a plain restatement. The supplied provenance and translator notes explicitly document that this is an intentional class-level encoding to avoid falsely asserting existing issued licenses, which resolves the apparent mismatch.

Semantic differences:

- none

Context-resolved issues:

- The source phrase 'may be issued' could look mismatched against the local fact introducing `IndexUnderlyingValueLicenseIssuance`, but provenance clarifies this carrier is structural and the modality is represented by the `permission`, not by an existential issuance claim.
- The source speaks generically of licenses, while the IR splits this into a class carrier, an issuance carrier, and a concrete-license subtype; provenance and notes explicitly justify this as a non-committal encoding of availability rather than actual issuance.
- The universal fact `forall l: IndexUnderlyingValueLicense, license_instance_of_class(l, LicensesToUseIndexAsUnderlyingValue)` could look like an extra claim, but provenance marks it as an internal bridge needed to align the permission target with the class-level source-backed carrier, not as an added source assertion.
- The fact listing all recipient categories on one issuance carrier could look like one issuance simultaneously targeting all categories, but provenance explicitly states it is a class/programme-level encoding of the listed categories, not a claim about one concrete issued license.

Stylistic notes:

- `LicensesToUseIndexAsUnderlyingValue` is awkward but source-traceable naming for a class-level carrier.
- `IndexUnderlyingValueLicenseIssuance` is a structural reification of 'may be issued' rather than source wording.
- Use of enums for use categories and recipient categories is a modeling choice, not semantic drift.
- `SolactiveOrganization` is a typing convenience for the permission agent parameter; the source only names Solactive.

### claude-haiku-4-5

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `provenance, translator_notes`
- confidence: `0.98`

Reason:

The main_ir.a4v3 faithfully encodes the source sentence's core claims: (1) licenses to use the Index as underlying value exist as a class, (2) they cover three use categories (financial instruments, investment funds, financial contracts), (3) they are issued to four recipient categories (stock exchanges, banks, financial services providers, investment houses), and (4) Solactive is the issuer. The IR uses class-level and issuance-level carriers to avoid over-committing to a concrete issued license, which correctly interprets the source's generic plural and modal 'may be issued'. The provenance and translator notes document these design decisions explicitly and justify them against the source text.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR introduces intermediate sorts (LicenseClass, LicenseIssuance, LicenseUseCategory, LicenseRecipientCategory) and a permission declaration to make the source's modality and structure explicit. This is intentional reification, not drift.
- The source uses a single sentence with implicit scope; the IR distributes that scope across multiple relations (license_class_uses_index_as_underlying_value, license_class_use_category, issuance_to_recipient_category, issuance_by). This is a faithful structural unpacking, documented in provenance.
- The entity Solactive is typed as SolactiveOrganization (a subtype of Organization) rather than used directly as a parameter type in the permission. This follows a4v3 discipline: parameter types must be sorts, not entities. The provenance notes this design choice explicitly.

### deepseek-v4-pro

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `none`
- confidence: `0.95`

Reason:

The IR faithfully encodes the source sentence: it represents the licensing programme as a class of licenses (with enumerated use and recipient categories), an issuance carrier, and a permission for Solactive to issue such licenses. No semantic drift is present; the structure clarifies the source without contradicting it.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The IR reifies 'license class', 'issuance', and category enums, which are not explicit in the source but serve to structure the semantics without altering meaning.
- The permission uses the type SolactiveOrganization rather than the entity Solactive as parameter type, which is a syntactic compliance choice, not a semantic change.

### qwen/qwen3.6-plus

- local_source_alignment: `corresponds`
- corpus_alignment: `corresponds`
- relation_type: `exact_equivalence`
- needs_context: `False`
- context_used: `none`
- confidence: `0.95`

Reason:

The IR accurately captures the source's licensing availability statement by modeling the license type, permitted uses, eligible recipients, and issuing agent. The modal 'may be issued' is correctly represented as a permission rather than an existential fact, and the listed categories are explicitly enumerated. The structural reification (license class, issuance carrier, enums) preserves the source semantics without adding or omitting claims.

Semantic differences:

- none

Context-resolved issues:

- none

Stylistic notes:

- The translation employs significant structural reification (LicenseClass, LicenseIssuance carrier, and enum sorts) to model a single declarative sentence, which is consistent with A4V3 methodology but adds ontological depth not explicitly present in the source phrasing.
