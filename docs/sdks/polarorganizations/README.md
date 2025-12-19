# PolarOrganizations
(*customer_portal.organizations*)

## Overview

### Available Operations

* [get](#get) - Get Organization

## get

Get a customer portal's organization by slug.

### Example Usage

<!-- UsageSnippet language="python" operationID="customer_portal:organizations:get" method="get" path="/v1/customer-portal/organizations/{slug}" -->
```python
from polar_sdk import Polar


with Polar() as polar:

    res = polar.customer_portal.organizations.get(slug="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `slug`                                                              | *str*                                                               | :heavy_check_mark:                                                  | The organization slug.                                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CustomerOrganizationData](../../models/customerorganizationdata.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |