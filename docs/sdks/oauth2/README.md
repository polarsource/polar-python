# Oauth2
(*oauth2*)

## Overview

### Available Operations

* [oauth2_list_clients](#oauth2_list_clients) - List Clients
* [oauth2_oauth2_create_client](#oauth2_oauth2_create_client) - Create Client
* [oauth2_oauth2_get_client](#oauth2_oauth2_get_client) - Get Client
* [oauth2_oauth2_update_client](#oauth2_oauth2_update_client) - Update Client
* [oauth2_oauth2_delete_client](#oauth2_oauth2_delete_client) - Delete Client
* [oauth2_authorize](#oauth2_authorize) - Authorize
* [oauth2_request_token](#oauth2_request_token) - Request Token
* [oauth2_revoke_token](#oauth2_revoke_token) - Revoke Token
* [oauth2_introspect_token](#oauth2_introspect_token) - Introspect Token
* [oauth2_userinfo](#oauth2_userinfo) - Get User Info

## oauth2_list_clients

List OAuth2 clients.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.oauth2.oauth2_list_clients(security=polar_sh.Oauth2ListClientsSecurity(
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
| `security`                                                                    | [models.Oauth2ListClientsSecurity](../../models/oauth2listclientssecurity.md) | :heavy_check_mark:                                                            | N/A                                                                           |
| `page`                                                                        | *Optional[int]*                                                               | :heavy_minus_sign:                                                            | Page number, defaults to 1.                                                   |
| `limit`                                                                       | *Optional[int]*                                                               | :heavy_minus_sign:                                                            | Size of a page, defaults to 10. Maximum is 100.                               |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[models.Oauth2ListClientsResponse](../../models/oauth2listclientsresponse.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## oauth2_oauth2_create_client

Create an OAuth2 client.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.oauth2.oauth2_oauth2_create_client(security=polar_sh.Oauth2Oauth2CreateClientSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), request={
    "redirect_uris": [
        "https://showy-food.com",
    ],
    "client_name": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [models.OAuth2ClientConfiguration](../../models/oauth2clientconfiguration.md)        | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `security`                                                                           | [models.Oauth2Oauth2CreateClientSecurity](../../oauth2oauth2createclientsecurity.md) | :heavy_check_mark:                                                                   | The security requirements to use for the request.                                    |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[Any](../../models/.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## oauth2_oauth2_get_client

Get an OAuth2 client by Client ID.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.oauth2.oauth2_oauth2_get_client(security=polar_sh.Oauth2Oauth2GetClientSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), client_id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `security`                                                                            | [models.Oauth2Oauth2GetClientSecurity](../../models/oauth2oauth2getclientsecurity.md) | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `client_id`                                                                           | *str*                                                                                 | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[Any](../../models/.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## oauth2_oauth2_update_client

Update an OAuth2 client.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.oauth2.oauth2_oauth2_update_client(security=polar_sh.Oauth2Oauth2UpdateClientSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), client_id="<value>", o_auth2_client_configuration_update={
    "redirect_uris": [
        "http://assured-generosity.net",
    ],
    "client_name": "<value>",
    "client_id": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `security`                                                                                  | [models.Oauth2Oauth2UpdateClientSecurity](../../models/oauth2oauth2updateclientsecurity.md) | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `client_id`                                                                                 | *str*                                                                                       | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `o_auth2_client_configuration_update`                                                       | [models.OAuth2ClientConfigurationUpdate](../../models/oauth2clientconfigurationupdate.md)   | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |

### Response

**[Any](../../models/.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## oauth2_oauth2_delete_client

Delete an OAuth2 client.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.oauth2.oauth2_oauth2_delete_client(security=polar_sh.Oauth2Oauth2DeleteClientSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), client_id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `security`                                                                                  | [models.Oauth2Oauth2DeleteClientSecurity](../../models/oauth2oauth2deleteclientsecurity.md) | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `client_id`                                                                                 | *str*                                                                                       | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |

### Response

**[Any](../../models/.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## oauth2_authorize

Authorize

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.oauth2.oauth2_authorize(security=polar_sh.Oauth2AuthorizeSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `security`                                                          | [models.Oauth2AuthorizeSecurity](../../oauth2authorizesecurity.md)  | :heavy_check_mark:                                                  | The security requirements to use for the request.                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Oauth2AuthorizeResponseOauth2Authorize](../../models/oauth2authorizeresponseoauth2authorize.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |


## oauth2_request_token

Request an access token using a valid grant.

### Example Usage

```python
from polar_sh import Polar

s = Polar(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
)


res = s.oauth2.oauth2_request_token(request={
    "client_id": "<value>",
    "client_secret": "<value>",
    "refresh_token": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `request`                                                                             | [models.Oauth2RequestTokenRequestBody](../../models/oauth2requesttokenrequestbody.md) | :heavy_check_mark:                                                                    | The request object to use for the request.                                            |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.TokenResponse](../../models/tokenresponse.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |


## oauth2_revoke_token

Revoke an access token or a refresh token.

### Example Usage

```python
from polar_sh import Polar

s = Polar(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
)


res = s.oauth2.oauth2_revoke_token(request={
    "token": "<value>",
    "client_id": "<value>",
    "client_secret": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                         | Type                                                                                              | Required                                                                                          | Description                                                                                       |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `request`                                                                                         | [models.Oauth2RevokeTokenRevokeTokenRequest](../../models/oauth2revoketokenrevoketokenrequest.md) | :heavy_check_mark:                                                                                | The request object to use for the request.                                                        |
| `retries`                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                  | :heavy_minus_sign:                                                                                | Configuration to override the default retry behavior of the client.                               |

### Response

**[models.RevokeTokenResponse](../../models/revoketokenresponse.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |


## oauth2_introspect_token

Get information about an access token.

### Example Usage

```python
from polar_sh import Polar

s = Polar(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
)


res = s.oauth2.oauth2_introspect_token(request={
    "token": "<value>",
    "client_id": "<value>",
    "client_secret": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                         | Type                                                                                                              | Required                                                                                                          | Description                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                         | [models.Oauth2IntrospectTokenIntrospectTokenRequest](../../models/oauth2introspecttokenintrospecttokenrequest.md) | :heavy_check_mark:                                                                                                | The request object to use for the request.                                                                        |
| `retries`                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                  | :heavy_minus_sign:                                                                                                | Configuration to override the default retry behavior of the client.                                               |

### Response

**[models.IntrospectTokenResponse](../../models/introspecttokenresponse.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |


## oauth2_userinfo

Get information about the authenticated user.

### Example Usage

```python
from polar_sh import Polar

s = Polar(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
)


res = s.oauth2.oauth2_userinfo()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Oauth2UserinfoResponseOauth2Userinfo](../../models/oauth2userinforesponseoauth2userinfo.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
