# Refunds
(*refunds*)

## Overview

### Available Operations

* [list](#list) - List Refunds
* [create](#create) - Create Refund

## list

List products.

### Example Usage

```python
from polar_sdk import Polar

with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.refunds.list(page=1, limit=10)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                               | Type                                                                                                                                                                    | Required                                                                                                                                                                | Description                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                    | [OptionalNullable[models.RefundIDFilter]](../../models/refundidfilter.md)                                                                                               | :heavy_minus_sign:                                                                                                                                                      | Filter by refund ID.                                                                                                                                                    |
| `organization_id`                                                                                                                                                       | [OptionalNullable[models.RefundsListQueryParamOrganizationIDFilter]](../../models/refundslistqueryparamorganizationidfilter.md)                                         | :heavy_minus_sign:                                                                                                                                                      | Filter by organization ID.                                                                                                                                              |
| `order_id`                                                                                                                                                              | [OptionalNullable[models.OrderIDFilter]](../../models/orderidfilter.md)                                                                                                 | :heavy_minus_sign:                                                                                                                                                      | Filter by order ID.                                                                                                                                                     |
| `subscription_id`                                                                                                                                                       | [OptionalNullable[models.SubscriptionIDFilter]](../../models/subscriptionidfilter.md)                                                                                   | :heavy_minus_sign:                                                                                                                                                      | Filter by subscription ID.                                                                                                                                              |
| `customer_id`                                                                                                                                                           | [OptionalNullable[models.RefundsListQueryParamCustomerIDFilter]](../../models/refundslistqueryparamcustomeridfilter.md)                                                 | :heavy_minus_sign:                                                                                                                                                      | Filter by customer ID.                                                                                                                                                  |
| `succeeded`                                                                                                                                                             | *OptionalNullable[bool]*                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                      | Filter by `succeeded`.                                                                                                                                                  |
| `page`                                                                                                                                                                  | *Optional[int]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | Page number, defaults to 1.                                                                                                                                             |
| `limit`                                                                                                                                                                 | *Optional[int]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | Size of a page, defaults to 10. Maximum is 100.                                                                                                                         |
| `sorting`                                                                                                                                                               | List[[models.RefundSortProperty](../../models/refundsortproperty.md)]                                                                                                   | :heavy_minus_sign:                                                                                                                                                      | Sorting criterion. Several criteria can be used simultaneously and will be applied in order. Add a minus sign `-` before the criteria name to sort by descending order. |
| `retries`                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                        | :heavy_minus_sign:                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                     |

### Response

**[models.RefundsListResponse](../../models/refundslistresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## create

Create a refund.

### Example Usage

```python
import polar_sdk
from polar_sdk import Polar

with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.refunds.create(request={
        "order_id": "<value>",
        "reason": polar_sdk.RefundReason.CUSTOMER_REQUEST,
        "amount": 638424,
        "revoke_benefits": False,
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.RefundCreate](../../models/refundcreate.md)                 | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Refund](../../models/refund.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.RefundAmountTooHigh | 400                        | application/json           |
| models.RefundedAlready     | 403                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |