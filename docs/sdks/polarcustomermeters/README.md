# PolarCustomerMeters
(*customer_portal.customer_meters*)

## Overview

### Available Operations

* [list](#list) - List Meters
* [get](#get) - Get Customer Meter

## list

List meters of the authenticated customer.

**Scopes**: `customer_portal:read` `customer_portal:write`

### Example Usage

```python
import polar_sdk
from polar_sdk import Polar


with Polar() as polar:

    res = polar.customer_portal.customer_meters.list(security=polar_sdk.CustomerPortalCustomerMetersListSecurity(
        customer_session="<YOUR_BEARER_TOKEN_HERE>",
    ))

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                               | Type                                                                                                                                                                    | Required                                                                                                                                                                | Description                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                                              | [models.CustomerPortalCustomerMetersListSecurity](../../models/customerportalcustomermeterslistsecurity.md)                                                             | :heavy_check_mark:                                                                                                                                                      | N/A                                                                                                                                                                     |
| `meter_id`                                                                                                                                                              | [OptionalNullable[models.MeterIDFilter]](../../models/meteridfilter.md)                                                                                                 | :heavy_minus_sign:                                                                                                                                                      | Filter by meter ID.                                                                                                                                                     |
| `query`                                                                                                                                                                 | *OptionalNullable[str]*                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                      | Filter by meter name.                                                                                                                                                   |
| `page`                                                                                                                                                                  | *Optional[int]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | Page number, defaults to 1.                                                                                                                                             |
| `limit`                                                                                                                                                                 | *Optional[int]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | Size of a page, defaults to 10. Maximum is 100.                                                                                                                         |
| `sorting`                                                                                                                                                               | List[[models.CustomerCustomerMeterSortProperty](../../models/customercustomermetersortproperty.md)]                                                                     | :heavy_minus_sign:                                                                                                                                                      | Sorting criterion. Several criteria can be used simultaneously and will be applied in order. Add a minus sign `-` before the criteria name to sort by descending order. |
| `retries`                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                        | :heavy_minus_sign:                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                     |

### Response

**[models.CustomerPortalCustomerMetersListResponse](../../models/customerportalcustomermeterslistresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get

Get a meter by ID for the authenticated customer.

**Scopes**: `customer_portal:read` `customer_portal:write`

### Example Usage

```python
import polar_sdk
from polar_sdk import Polar


with Polar() as polar:

    res = polar.customer_portal.customer_meters.get(security=polar_sdk.CustomerPortalCustomerMetersGetSecurity(
        customer_session="<YOUR_BEARER_TOKEN_HERE>",
    ), id="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                 | Type                                                                                                      | Required                                                                                                  | Description                                                                                               |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                | [models.CustomerPortalCustomerMetersGetSecurity](../../models/customerportalcustomermetersgetsecurity.md) | :heavy_check_mark:                                                                                        | N/A                                                                                                       |
| `id`                                                                                                      | *str*                                                                                                     | :heavy_check_mark:                                                                                        | The customer meter ID.                                                                                    |
| `retries`                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                          | :heavy_minus_sign:                                                                                        | Configuration to override the default retry behavior of the client.                                       |

### Response

**[models.CustomerCustomerMeter](../../models/customercustomermeter.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |