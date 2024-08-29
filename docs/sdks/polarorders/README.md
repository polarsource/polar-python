# PolarOrders
(*users.orders*)

## Overview

### Available Operations

* [list](#list) - List Orders
* [retrieve](#retrieve) - Get Order
* [invoice](#invoice) - Get Order Invoice

## list

List my orders.

### Example Usage

```python
from polar_sh import Polar

s = Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.users.orders.list()

if res is not None:
    while True:
        # handle items

        res = res.Next()
        if res is None:
            break


```

### Parameters

| Parameter                                                                                                                                                                             | Type                                                                                                                                                                                  | Required                                                                                                                                                                              | Description                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `organization_id`                                                                                                                                                                     | [OptionalNullable[models.QueryParamOrganizationIDFilter]](../../models/queryparamorganizationidfilter.md)                                                                             | :heavy_minus_sign:                                                                                                                                                                    | Filter by organization ID.                                                                                                                                                            |
| `product_id`                                                                                                                                                                          | [OptionalNullable[models.ProductIDFilter]](../../models/productidfilter.md)                                                                                                           | :heavy_minus_sign:                                                                                                                                                                    | Filter by product ID.                                                                                                                                                                 |
| `product_price_type`                                                                                                                                                                  | [OptionalNullable[models.ProductPriceTypeFilter]](../../models/productpricetypefilter.md)                                                                                             | :heavy_minus_sign:                                                                                                                                                                    | Filter by product price type. `recurring` will return orders corresponding to subscriptions creations or renewals. `one_time` will return orders corresponding to one-time purchases. |
| `subscription_id`                                                                                                                                                                     | [OptionalNullable[models.QueryParamSubscriptionIDFilter]](../../models/queryparamsubscriptionidfilter.md)                                                                             | :heavy_minus_sign:                                                                                                                                                                    | Filter by subscription ID.                                                                                                                                                            |
| `query`                                                                                                                                                                               | *OptionalNullable[str]*                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                    | Search by product or organization name.                                                                                                                                               |
| `page`                                                                                                                                                                                | *Optional[int]*                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                    | Page number, defaults to 1.                                                                                                                                                           |
| `limit`                                                                                                                                                                               | *Optional[int]*                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                    | Size of a page, defaults to 10. Maximum is 100.                                                                                                                                       |
| `sorting`                                                                                                                                                                             | List[[models.UserOrderSortProperty](../../models/userordersortproperty.md)]                                                                                                           | :heavy_minus_sign:                                                                                                                                                                    | Sorting criterion. Several criteria can be used simultaneously and will be applied in order. Add a minus sign `-` before the criteria name to sort by descending order.               |
| `retries`                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                   |

### Response

**[models.UsersOrdersListResponse](../../models/usersorderslistresponse.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## retrieve

Get an order by ID.

### Example Usage

```python
from polar_sh import Polar

s = Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.users.orders.retrieve(id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The order ID.                                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UserOrder](../../models/userorder.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## invoice

Get an order's invoice data.

### Example Usage

```python
from polar_sh import Polar

s = Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.users.orders.invoice(id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The order ID.                                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UserOrderInvoice](../../models/userorderinvoice.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |
