# Wallets
(*customer_portal.wallets*)

## Overview

### Available Operations

* [list](#list) - List Wallets
* [get](#get) - Get Wallet

## list

List wallets of the authenticated customer.

### Example Usage

<!-- UsageSnippet language="python" operationID="customer_portal:wallets:list" method="get" path="/v1/customer-portal/wallets/" -->
```python
import polar_sdk
from polar_sdk import Polar


with Polar() as polar:

    res = polar.customer_portal.wallets.list(security=polar_sdk.CustomerPortalWalletsListSecurity(
        customer_session="<YOUR_BEARER_TOKEN_HERE>",
    ), page=1, limit=10)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                               | Type                                                                                                                                                                    | Required                                                                                                                                                                | Description                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                                              | [models.CustomerPortalWalletsListSecurity](../../models/customerportalwalletslistsecurity.md)                                                                           | :heavy_check_mark:                                                                                                                                                      | N/A                                                                                                                                                                     |
| `page`                                                                                                                                                                  | *Optional[int]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | Page number, defaults to 1.                                                                                                                                             |
| `limit`                                                                                                                                                                 | *Optional[int]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | Size of a page, defaults to 10. Maximum is 100.                                                                                                                         |
| `sorting`                                                                                                                                                               | List[[models.CustomerWalletSortProperty](../../models/customerwalletsortproperty.md)]                                                                                   | :heavy_minus_sign:                                                                                                                                                      | Sorting criterion. Several criteria can be used simultaneously and will be applied in order. Add a minus sign `-` before the criteria name to sort by descending order. |
| `retries`                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                        | :heavy_minus_sign:                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                     |

### Response

**[models.CustomerPortalWalletsListResponse](../../models/customerportalwalletslistresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get

Get a wallet by ID for the authenticated customer.

### Example Usage

<!-- UsageSnippet language="python" operationID="customer_portal:wallets:get" method="get" path="/v1/customer-portal/wallets/{id}" -->
```python
import polar_sdk
from polar_sdk import Polar


with Polar() as polar:

    res = polar.customer_portal.wallets.get(security=polar_sdk.CustomerPortalWalletsGetSecurity(
        customer_session="<YOUR_BEARER_TOKEN_HERE>",
    ), id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `security`                                                                                  | [models.CustomerPortalWalletsGetSecurity](../../models/customerportalwalletsgetsecurity.md) | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `id`                                                                                        | *str*                                                                                       | :heavy_check_mark:                                                                          | The wallet ID.                                                                              |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |

### Response

**[models.CustomerWallet](../../models/customerwallet.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |