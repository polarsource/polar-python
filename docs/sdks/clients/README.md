# Clients
(*oauth2.clients*)

## Overview

### Available Operations

* [list](#list) - List Clients
* [create](#create) - Create Client
* [retrieve](#retrieve) - Get Client
* [update](#update) - Update Client
* [delete](#delete) - Delete Client

## list

List OAuth2 clients.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.oauth2.clients.list(security=polar_sh.Oauth2ClientsListSecurity(
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

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `security`                                                                    | [models.Oauth2ClientsListSecurity](../../models/oauth2clientslistsecurity.md) | :heavy_check_mark:                                                            | N/A                                                                           |
| `page`                                                                        | *Optional[int]*                                                               | :heavy_minus_sign:                                                            | Page number, defaults to 1.                                                   |
| `limit`                                                                       | *Optional[int]*                                                               | :heavy_minus_sign:                                                            | Size of a page, defaults to 10. Maximum is 100.                               |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[models.Oauth2ClientsListResponse](../../models/oauth2clientslistresponse.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## create

Create an OAuth2 client.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.oauth2.clients.create(security=polar_sh.Oauth2ClientsOauth2CreateClientSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), request={
    "redirect_uris": [
        "http://limp-pastry.org",
    ],
    "client_name": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [models.OAuth2ClientConfiguration](../../models/oauth2clientconfiguration.md)                      | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `security`                                                                                         | [models.Oauth2ClientsOauth2CreateClientSecurity](../../oauth2clientsoauth2createclientsecurity.md) | :heavy_check_mark:                                                                                 | The security requirements to use for the request.                                                  |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[Any](../../models/.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## retrieve

Get an OAuth2 client by Client ID.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.oauth2.clients.retrieve(security=polar_sh.Oauth2ClientsOauth2GetClientSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), client_id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                           | Type                                                                                                | Required                                                                                            | Description                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `security`                                                                                          | [models.Oauth2ClientsOauth2GetClientSecurity](../../models/oauth2clientsoauth2getclientsecurity.md) | :heavy_check_mark:                                                                                  | N/A                                                                                                 |
| `client_id`                                                                                         | *str*                                                                                               | :heavy_check_mark:                                                                                  | N/A                                                                                                 |
| `retries`                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                    | :heavy_minus_sign:                                                                                  | Configuration to override the default retry behavior of the client.                                 |

### Response

**[Any](../../models/.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## update

Update an OAuth2 client.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.oauth2.clients.update(security=polar_sh.Oauth2ClientsOauth2UpdateClientSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), client_id="<value>", o_auth2_client_configuration_update={
    "redirect_uris": [
        "https://alarming-nondisclosure.com",
    ],
    "client_name": "<value>",
    "client_id": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                 | Type                                                                                                      | Required                                                                                                  | Description                                                                                               |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                | [models.Oauth2ClientsOauth2UpdateClientSecurity](../../models/oauth2clientsoauth2updateclientsecurity.md) | :heavy_check_mark:                                                                                        | N/A                                                                                                       |
| `client_id`                                                                                               | *str*                                                                                                     | :heavy_check_mark:                                                                                        | N/A                                                                                                       |
| `o_auth2_client_configuration_update`                                                                     | [models.OAuth2ClientConfigurationUpdate](../../models/oauth2clientconfigurationupdate.md)                 | :heavy_check_mark:                                                                                        | N/A                                                                                                       |
| `retries`                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                          | :heavy_minus_sign:                                                                                        | Configuration to override the default retry behavior of the client.                                       |

### Response

**[Any](../../models/.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## delete

Delete an OAuth2 client.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.oauth2.clients.delete(security=polar_sh.Oauth2ClientsOauth2DeleteClientSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), client_id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                 | Type                                                                                                      | Required                                                                                                  | Description                                                                                               |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                | [models.Oauth2ClientsOauth2DeleteClientSecurity](../../models/oauth2clientsoauth2deleteclientsecurity.md) | :heavy_check_mark:                                                                                        | N/A                                                                                                       |
| `client_id`                                                                                               | *str*                                                                                                     | :heavy_check_mark:                                                                                        | N/A                                                                                                       |
| `retries`                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                          | :heavy_minus_sign:                                                                                        | Configuration to override the default retry behavior of the client.                                       |

### Response

**[Any](../../models/.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |
