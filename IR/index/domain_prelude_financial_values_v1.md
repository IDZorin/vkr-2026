# Domain Prelude: Financial Values v1

Reusable financial-value primitives for typed monetary amounts.

This is intentionally separate from `minimal_prelude_v1`: these symbols are useful for financial methodologies, but they are not universal cross-domain primitives.

## Included Sorts

- `MonetaryAmount`
- `Currency`
- `MonetaryAmountValue`
- `MonetaryAmountScale`
- `Percent`

## Included Entities

None. Concrete currencies and scales, such as `USD` or `Million`, should be local entities grounded in the source text.

## Included Functions

- `currency : MonetaryAmount -> Currency`
- `monetary_amount_value : MonetaryAmount -> MonetaryAmountValue`
- `monetary_amount_scale : MonetaryAmount -> MonetaryAmountScale`

`Percent` is the reusable value sort for percentage quantities such as `50%` or `5%`.
Concrete percentage literals should stay as literals in formulas; do not create entities
such as `FiftyPercent` or `FivePercent`.

## Naming Note

`Currency` and `currency` are different levels:

- `Currency` is the type of currency objects, such as a locally grounded `USD`.
- `MonetaryAmountScale` is the type of scale objects, such as a locally grounded `Million`.
- `currency(amount)` is the accessor returning the currency of a concrete `MonetaryAmount`.

Example pattern:

```a4v3
entity Threshold : MonetaryAmount

fact threshold_currency :
currency(Threshold) = USD

fact threshold_value :
monetary_amount_value(Threshold) = 5

fact threshold_scale :
monetary_amount_scale(Threshold) = Million
```

Do not use this prelude to invent monetary facts not warranted by the source.
