# Accounts
(*accounts*)

## Overview

### Available Operations

* [accounts_search](#accounts_search) - Search
* [accounts_get](#accounts_get) - Get
* [accounts_onboarding_link](#accounts_onboarding_link) - Onboarding Link
* [accounts_dashboard_link](#accounts_dashboard_link) - Dashboard Link
* [accounts_create](#accounts_create) - Create

## accounts_search

Search

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.accounts.accounts_search(security=polar_sh.AccountsSearchSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `security`                                                              | [models.AccountsSearchSecurity](../../models/accountssearchsecurity.md) | :heavy_check_mark:                                                      | N/A                                                                     |
| `page`                                                                  | *Optional[int]*                                                         | :heavy_minus_sign:                                                      | Page number, defaults to 1.                                             |
| `limit`                                                                 | *Optional[int]*                                                         | :heavy_minus_sign:                                                      | Size of a page, defaults to 10. Maximum is 100.                         |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.ListResourceAccount](../../models/listresourceaccount.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## accounts_get

Get

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.accounts.accounts_get(security=polar_sh.AccountsGetSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="8667bc00-c75e-4358-bb21-152053ea44ad")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `security`                                                          | [models.AccountsGetSecurity](../../models/accountsgetsecurity.md)   | :heavy_check_mark:                                                  | N/A                                                                 |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Account](../../models/account.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## accounts_onboarding_link

Onboarding Link

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.accounts.accounts_onboarding_link(security=polar_sh.AccountsOnboardingLinkSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="3cb83ede-051b-4b7e-aa50-13dd4f0b0a48", return_path="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `security`                                                                              | [models.AccountsOnboardingLinkSecurity](../../models/accountsonboardinglinksecurity.md) | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `id`                                                                                    | *str*                                                                                   | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `return_path`                                                                           | *str*                                                                                   | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[models.AccountLink](../../models/accountlink.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## accounts_dashboard_link

Dashboard Link

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.accounts.accounts_dashboard_link(security=polar_sh.AccountsDashboardLinkSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="39a56e91-fc66-421b-b82f-12d1c0a09a32")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `security`                                                                            | [models.AccountsDashboardLinkSecurity](../../models/accountsdashboardlinksecurity.md) | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `id`                                                                                  | *str*                                                                                 | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.AccountLink](../../models/accountlink.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## accounts_create

Create

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.accounts.accounts_create(security=polar_sh.AccountsCreateSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), request={
    "account_type": polar_sh.AccountType.STRIPE,
    "country": "Angola",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.AccountCreate](../../models/accountcreate.md)               | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `security`                                                          | [models.AccountsCreateSecurity](../../accountscreatesecurity.md)    | :heavy_check_mark:                                                  | The security requirements to use for the request.                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Account](../../models/account.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |
