# Donations
(*donations*)

## Overview

### Available Operations

* [donations_search_donations](#donations_search_donations) - Search Donations
* [donations_create_payment_intent](#donations_create_payment_intent) - Create Payment Intent
* [donations_update_payment_intent](#donations_update_payment_intent) - Update Payment Intent
* [donations_statistics](#donations_statistics) - Statistics
* [donations_donations_public_search](#donations_donations_public_search) - Donations Public Search

## donations_search_donations

Search Donations

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.donations.donations_search_donations(security=polar_sh.DonationsSearchDonationsSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), to_organization_id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                               | Type                                                                                                                                                                    | Required                                                                                                                                                                | Description                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                                              | [models.DonationsSearchDonationsSecurity](../../models/donationssearchdonationssecurity.md)                                                                             | :heavy_check_mark:                                                                                                                                                      | N/A                                                                                                                                                                     |
| `to_organization_id`                                                                                                                                                    | *str*                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                      | N/A                                                                                                                                                                     |
| `page`                                                                                                                                                                  | *Optional[int]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | Page number, defaults to 1.                                                                                                                                             |
| `limit`                                                                                                                                                                 | *Optional[int]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | Size of a page, defaults to 10. Maximum is 100.                                                                                                                         |
| `sorting`                                                                                                                                                               | [OptionalNullable[models.DonationsSearchDonationsQueryParamSorting]](../../models/donationssearchdonationsqueryparamsorting.md)                                         | :heavy_minus_sign:                                                                                                                                                      | Sorting criterion. Several criteria can be used simultaneously and will be applied in order. Add a minus sign `-` before the criteria name to sort by descending order. |
| `retries`                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                        | :heavy_minus_sign:                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                     |

### Response

**[models.ListResourceDonation](../../models/listresourcedonation.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## donations_create_payment_intent

Create Payment Intent

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.donations.donations_create_payment_intent(security=polar_sh.DonationsCreatePaymentIntentSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), request={
    "to_organization_id": "<value>",
    "email": "Laurianne.Kessler@yahoo.com",
    "amount": 853358,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `request`                                                                                     | [models.DonationCreateStripePaymentIntent](../../models/donationcreatestripepaymentintent.md) | :heavy_check_mark:                                                                            | The request object to use for the request.                                                    |
| `security`                                                                                    | [models.DonationsCreatePaymentIntentSecurity](../../donationscreatepaymentintentsecurity.md)  | :heavy_check_mark:                                                                            | The security requirements to use for the request.                                             |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |

### Response

**[models.DonationStripePaymentIntentMutationResponse](../../models/donationstripepaymentintentmutationresponse.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## donations_update_payment_intent

Update Payment Intent

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.donations.donations_update_payment_intent(security=polar_sh.DonationsUpdatePaymentIntentSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>", donation_update_stripe_payment_intent={
    "email": "Aniyah14@yahoo.com",
    "amount": 940900,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                           | Type                                                                                                | Required                                                                                            | Description                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `security`                                                                                          | [models.DonationsUpdatePaymentIntentSecurity](../../models/donationsupdatepaymentintentsecurity.md) | :heavy_check_mark:                                                                                  | N/A                                                                                                 |
| `id`                                                                                                | *str*                                                                                               | :heavy_check_mark:                                                                                  | N/A                                                                                                 |
| `donation_update_stripe_payment_intent`                                                             | [models.DonationUpdateStripePaymentIntent](../../models/donationupdatestripepaymentintent.md)       | :heavy_check_mark:                                                                                  | N/A                                                                                                 |
| `retries`                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                    | :heavy_minus_sign:                                                                                  | Configuration to override the default retry behavior of the client.                                 |

### Response

**[models.DonationStripePaymentIntentMutationResponse](../../models/donationstripepaymentintentmutationresponse.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## donations_statistics

Statistics

### Example Usage

```python
import dateutil.parser
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.donations.donations_statistics(security=polar_sh.DonationsStatisticsSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), to_organization_id="<value>", start_date=dateutil.parser.parse("2022-10-01").date(), end_date=dateutil.parser.parse("2023-01-01").date(), donations_interval=polar_sh.Donationsinterval.DAY)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `security`                                                                        | [models.DonationsStatisticsSecurity](../../models/donationsstatisticssecurity.md) | :heavy_check_mark:                                                                | N/A                                                                               |
| `to_organization_id`                                                              | *str*                                                                             | :heavy_check_mark:                                                                | N/A                                                                               |
| `start_date`                                                                      | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)      | :heavy_check_mark:                                                                | N/A                                                                               |
| `end_date`                                                                        | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)      | :heavy_check_mark:                                                                | N/A                                                                               |
| `donations_interval`                                                              | [models.Donationsinterval](../../models/donationsinterval.md)                     | :heavy_check_mark:                                                                | N/A                                                                               |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.DonationStatistics](../../models/donationstatistics.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## donations_donations_public_search

Donations Public Search

### Example Usage

```python
from polar_sh import Polar

s = Polar(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
)


res = s.donations.donations_donations_public_search(organization_id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                               | Type                                                                                                                                                                    | Required                                                                                                                                                                | Description                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `organization_id`                                                                                                                                                       | *str*                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                      | N/A                                                                                                                                                                     |
| `page`                                                                                                                                                                  | *Optional[int]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | Page number, defaults to 1.                                                                                                                                             |
| `limit`                                                                                                                                                                 | *Optional[int]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | Size of a page, defaults to 10. Maximum is 100.                                                                                                                         |
| `sorting`                                                                                                                                                               | [OptionalNullable[models.DonationsDonationsPublicSearchQueryParamSorting]](../../models/donationsdonationspublicsearchqueryparamsorting.md)                             | :heavy_minus_sign:                                                                                                                                                      | Sorting criterion. Several criteria can be used simultaneously and will be applied in order. Add a minus sign `-` before the criteria name to sort by descending order. |
| `retries`                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                        | :heavy_minus_sign:                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                     |

### Response

**[models.ListResourcePublicDonation](../../models/listresourcepublicdonation.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |
