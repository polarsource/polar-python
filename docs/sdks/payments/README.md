# Payments
(*payments*)

## Overview

### Available Operations

* [list](#list) - List Payments
* [get](#get) - Get Payment

## list

List payments.

**Scopes**: `payments:read`

### Example Usage

```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.payments.list(organization_id=[
        "1dbfc517-0bbf-4301-9ba8-555ca42b9737",
    ])

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                               | Type                                                                                                                                                                    | Required                                                                                                                                                                | Description                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `organization_id`                                                                                                                                                       | [OptionalNullable[models.PaymentsListQueryParamOrganizationIDFilter]](../../models/paymentslistqueryparamorganizationidfilter.md)                                       | :heavy_minus_sign:                                                                                                                                                      | Filter by organization ID.                                                                                                                                              |
| `checkout_id`                                                                                                                                                           | [OptionalNullable[models.PaymentsListQueryParamCheckoutIDFilter]](../../models/paymentslistqueryparamcheckoutidfilter.md)                                               | :heavy_minus_sign:                                                                                                                                                      | Filter by checkout ID.                                                                                                                                                  |
| `order_id`                                                                                                                                                              | [OptionalNullable[models.PaymentsListQueryParamOrderIDFilter]](../../models/paymentslistqueryparamorderidfilter.md)                                                     | :heavy_minus_sign:                                                                                                                                                      | Filter by order ID.                                                                                                                                                     |
| `status`                                                                                                                                                                | [OptionalNullable[models.QueryParamStatusFilter]](../../models/queryparamstatusfilter.md)                                                                               | :heavy_minus_sign:                                                                                                                                                      | Filter by payment status.                                                                                                                                               |
| `method`                                                                                                                                                                | [OptionalNullable[models.MethodFilter]](../../models/methodfilter.md)                                                                                                   | :heavy_minus_sign:                                                                                                                                                      | Filter by payment method.                                                                                                                                               |
| `customer_email`                                                                                                                                                        | [OptionalNullable[models.CustomerEmailFilter]](../../models/customeremailfilter.md)                                                                                     | :heavy_minus_sign:                                                                                                                                                      | Filter by customer email.                                                                                                                                               |
| `page`                                                                                                                                                                  | *Optional[int]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | Page number, defaults to 1.                                                                                                                                             |
| `limit`                                                                                                                                                                 | *Optional[int]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | Size of a page, defaults to 10. Maximum is 100.                                                                                                                         |
| `sorting`                                                                                                                                                               | List[[models.PaymentSortProperty](../../models/paymentsortproperty.md)]                                                                                                 | :heavy_minus_sign:                                                                                                                                                      | Sorting criterion. Several criteria can be used simultaneously and will be applied in order. Add a minus sign `-` before the criteria name to sort by descending order. |
| `retries`                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                        | :heavy_minus_sign:                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                     |

### Response

**[models.PaymentsListResponse](../../models/paymentslistresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get

Get a payment by ID.

**Scopes**: `payments:read`

### Example Usage

```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.payments.get(id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The payment ID.                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Payment](../../models/payment.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |