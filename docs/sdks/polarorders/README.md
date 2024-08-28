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
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.users.orders.list(security=polar_sh.UsersOrdersListSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
))

if res is not None:
    while True:
        # handle items

        res = res.Next()
        if res is None:
            break


```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `request`                                                               | [models.UsersOrdersListRequest](../../models/usersorderslistrequest.md) | :heavy_check_mark:                                                      | The request object to use for the request.                              |
| `security`                                                              | [models.UsersOrdersListSecurity](../../usersorderslistsecurity.md)      | :heavy_check_mark:                                                      | The security requirements to use for the request.                       |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

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
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.users.orders.retrieve(security=polar_sh.UsersOrdersGetSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `security`                                                              | [models.UsersOrdersGetSecurity](../../models/usersordersgetsecurity.md) | :heavy_check_mark:                                                      | N/A                                                                     |
| `id`                                                                    | *str*                                                                   | :heavy_check_mark:                                                      | The order ID.                                                           |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

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
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.users.orders.invoice(security=polar_sh.UsersOrdersInvoiceSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `security`                                                                      | [models.UsersOrdersInvoiceSecurity](../../models/usersordersinvoicesecurity.md) | :heavy_check_mark:                                                              | N/A                                                                             |
| `id`                                                                            | *str*                                                                           | :heavy_check_mark:                                                              | The order ID.                                                                   |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[models.UserOrderInvoice](../../models/userorderinvoice.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |
