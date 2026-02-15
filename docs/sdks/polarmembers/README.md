# PolarMembers
(*customer_portal.members*)

## Overview

### Available Operations

* [list_members](#list_members) - List Members
* [add_member](#add_member) - Add Member
* [update_member](#update_member) - Update Member
* [remove_member](#remove_member) - Remove Member

## list_members

List all members of the customer's team.

Only available to owners and billing managers of team customers.

### Example Usage

<!-- UsageSnippet language="python" operationID="customer_portal:members:list_members" method="get" path="/v1/customer-portal/members" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.customer_portal.members.list_members()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.CustomerPortalMember]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## add_member

Add a new member to the customer's team.

Only available to owners and billing managers of team customers.

Rules:
- Cannot add a member with the owner role (there must be exactly one owner)
- If a member with this email already exists, the existing member is returned

### Example Usage

<!-- UsageSnippet language="python" operationID="customer_portal:members:add_member" method="post" path="/v1/customer-portal/members" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.customer_portal.members.add_member(request={
        "email": "Domenica.Schamberger@yahoo.com",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `request`                                                                       | [models.CustomerPortalMemberCreate](../../models/customerportalmembercreate.md) | :heavy_check_mark:                                                              | The request object to use for the request.                                      |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[models.CustomerPortalMember](../../models/customerportalmember.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## update_member

Update a member's role.

Only available to owners and billing managers of team customers.

Rules:
- Cannot modify your own role (to prevent self-demotion)
- Customer must have exactly one owner at all times

### Example Usage

<!-- UsageSnippet language="python" operationID="customer_portal:members:update_member" method="patch" path="/v1/customer-portal/members/{id}" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.customer_portal.members.update_member(id="8319ae11-ed5f-4642-81e4-4b40731df195", customer_portal_member_update={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `id`                                                                            | *str*                                                                           | :heavy_check_mark:                                                              | N/A                                                                             |
| `customer_portal_member_update`                                                 | [models.CustomerPortalMemberUpdate](../../models/customerportalmemberupdate.md) | :heavy_check_mark:                                                              | N/A                                                                             |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[models.CustomerPortalMember](../../models/customerportalmember.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## remove_member

Remove a member from the team.

Only available to owners and billing managers of team customers.

Rules:
- Cannot remove yourself
- Cannot remove the only owner

### Example Usage

<!-- UsageSnippet language="python" operationID="customer_portal:members:remove_member" method="delete" path="/v1/customer-portal/members/{id}" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    polar.customer_portal.members.remove_member(id="b61c5e87-cda5-4b14-93ee-71a695f42d9d")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |