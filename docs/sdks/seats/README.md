# Seats
(*customer_portal.seats*)

## Overview

### Available Operations

* [list_seats](#list_seats) - List Seats
* [assign_seat](#assign_seat) - Assign Seat
* [revoke_seat](#revoke_seat) - Revoke Seat
* [resend_invitation](#resend_invitation) - Resend Invitation
* [list_claimed_subscriptions](#list_claimed_subscriptions) - List Claimed Subscriptions

## list_seats

**Scopes**: `customer_portal:read` `customer_portal:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="customer_portal:seats:list_seats" method="get" path="/v1/customer-portal/seats" -->
```python
import polar_sdk
from polar_sdk import Polar


with Polar() as polar:

    res = polar.customer_portal.seats.list_seats(security=polar_sdk.CustomerPortalSeatsListSeatsSecurity(
        customer_session="<YOUR_BEARER_TOKEN_HERE>",
    ), subscription_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                           | Type                                                                                                | Required                                                                                            | Description                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `security`                                                                                          | [models.CustomerPortalSeatsListSeatsSecurity](../../models/customerportalseatslistseatssecurity.md) | :heavy_check_mark:                                                                                  | N/A                                                                                                 |
| `subscription_id`                                                                                   | *OptionalNullable[str]*                                                                             | :heavy_minus_sign:                                                                                  | Subscription ID                                                                                     |
| `order_id`                                                                                          | *OptionalNullable[str]*                                                                             | :heavy_minus_sign:                                                                                  | Order ID                                                                                            |
| `retries`                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                    | :heavy_minus_sign:                                                                                  | Configuration to override the default retry behavior of the client.                                 |

### Response

**[models.SeatsList](../../models/seatslist.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## assign_seat

**Scopes**: `customer_portal:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="customer_portal:seats:assign_seat" method="post" path="/v1/customer-portal/seats" -->
```python
import polar_sdk
from polar_sdk import Polar


with Polar() as polar:

    res = polar.customer_portal.seats.assign_seat(security=polar_sdk.CustomerPortalSeatsAssignSeatSecurity(
        customer_session="<YOUR_BEARER_TOKEN_HERE>",
    ), request={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [models.SeatAssign](../../models/seatassign.md)                                                | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `security`                                                                                     | [models.CustomerPortalSeatsAssignSeatSecurity](../../customerportalseatsassignseatsecurity.md) | :heavy_check_mark:                                                                             | The security requirements to use for the request.                                              |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[models.CustomerSeat](../../models/customerseat.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## revoke_seat

**Scopes**: `customer_portal:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="customer_portal:seats:revoke_seat" method="delete" path="/v1/customer-portal/seats/{seat_id}" -->
```python
import polar_sdk
from polar_sdk import Polar


with Polar() as polar:

    res = polar.customer_portal.seats.revoke_seat(security=polar_sdk.CustomerPortalSeatsRevokeSeatSecurity(
        customer_session="<YOUR_BEARER_TOKEN_HERE>",
    ), seat_id="4b3d74b3-01ff-4aac-bd03-320535cd5ce4")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `security`                                                                                            | [models.CustomerPortalSeatsRevokeSeatSecurity](../../models/customerportalseatsrevokeseatsecurity.md) | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `seat_id`                                                                                             | *str*                                                                                                 | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |

### Response

**[models.CustomerSeat](../../models/customerseat.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## resend_invitation

**Scopes**: `customer_portal:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="customer_portal:seats:resend_invitation" method="post" path="/v1/customer-portal/seats/{seat_id}/resend" -->
```python
import polar_sdk
from polar_sdk import Polar


with Polar() as polar:

    res = polar.customer_portal.seats.resend_invitation(security=polar_sdk.CustomerPortalSeatsResendInvitationSecurity(
        customer_session="<YOUR_BEARER_TOKEN_HERE>",
    ), seat_id="e3817437-8d53-4578-88d2-1dc256825965")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                         | Type                                                                                                              | Required                                                                                                          | Description                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                        | [models.CustomerPortalSeatsResendInvitationSecurity](../../models/customerportalseatsresendinvitationsecurity.md) | :heavy_check_mark:                                                                                                | N/A                                                                                                               |
| `seat_id`                                                                                                         | *str*                                                                                                             | :heavy_check_mark:                                                                                                | N/A                                                                                                               |
| `retries`                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                  | :heavy_minus_sign:                                                                                                | Configuration to override the default retry behavior of the client.                                               |

### Response

**[models.CustomerSeat](../../models/customerseat.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## list_claimed_subscriptions

List all subscriptions where the authenticated customer has claimed a seat.

**Scopes**: `customer_portal:read` `customer_portal:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="customer_portal:seats:list_claimed_subscriptions" method="get" path="/v1/customer-portal/seats/subscriptions" -->
```python
import polar_sdk
from polar_sdk import Polar


with Polar() as polar:

    res = polar.customer_portal.seats.list_claimed_subscriptions(security=polar_sdk.CustomerPortalSeatsListClaimedSubscriptionsSecurity(
        customer_session="<YOUR_BEARER_TOKEN_HERE>",
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                 | [models.CustomerPortalSeatsListClaimedSubscriptionsSecurity](../../customerportalseatslistclaimedsubscriptionssecurity.md) | :heavy_check_mark:                                                                                                         | The security requirements to use for the request.                                                                          |
| `retries`                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                           | :heavy_minus_sign:                                                                                                         | Configuration to override the default retry behavior of the client.                                                        |

### Response

**[List[models.CustomerSubscription]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |