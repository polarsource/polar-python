# CustomerSeats
(*customer_seats*)

## Overview

### Available Operations

* [assign_seat](#assign_seat) - Assign Seat
* [list_seats](#list_seats) - List Seats
* [revoke_seat](#revoke_seat) - Revoke Seat
* [resend_invitation](#resend_invitation) - Resend Invitation
* [get_claim_info](#get_claim_info) - Get Claim Info
* [claim_seat](#claim_seat) - Claim Seat

## assign_seat

**Scopes**: `customer_seats:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="customer-seats:assign_seat" method="post" path="/v1/customer-seats" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.customer_seats.assign_seat(request={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.SeatAssign](../../models/seatassign.md)                     | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CustomerSeat](../../models/customerseat.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## list_seats

**Scopes**: `customer_seats:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="customer-seats:list_seats" method="get" path="/v1/customer-seats" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.customer_seats.list_seats()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `subscription_id`                                                   | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `order_id`                                                          | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SeatsList](../../models/seatslist.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## revoke_seat

**Scopes**: `customer_seats:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="customer-seats:revoke_seat" method="delete" path="/v1/customer-seats/{seat_id}" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.customer_seats.revoke_seat(seat_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `seat_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CustomerSeat](../../models/customerseat.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## resend_invitation

**Scopes**: `customer_seats:write`

### Example Usage

<!-- UsageSnippet language="python" operationID="customer-seats:resend_invitation" method="post" path="/v1/customer-seats/{seat_id}/resend" -->
```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.customer_seats.resend_invitation(seat_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `seat_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CustomerSeat](../../models/customerseat.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get_claim_info

Get Claim Info

### Example Usage

<!-- UsageSnippet language="python" operationID="customer-seats:get_claim_info" method="get" path="/v1/customer-seats/claim/{invitation_token}" -->
```python
from polar_sdk import Polar


with Polar() as polar:

    res = polar.customer_seats.get_claim_info(invitation_token="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `invitation_token`                                                  | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SeatClaimInfo](../../models/seatclaiminfo.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## claim_seat

Claim Seat

### Example Usage

<!-- UsageSnippet language="python" operationID="customer-seats:claim_seat" method="post" path="/v1/customer-seats/claim" -->
```python
from polar_sdk import Polar


with Polar() as polar:

    res = polar.customer_seats.claim_seat(request={
        "invitation_token": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.SeatClaim](../../models/seatclaim.md)                       | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CustomerSeatClaimResponse](../../models/customerseatclaimresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |