# Oauth2
(*oauth2*)

## Overview

### Available Operations

* [authorize](#authorize) - Authorize
* [token](#token) - Request Token
* [revoke](#revoke) - Revoke Token
* [introspect](#introspect) - Introspect Token
* [userinfo](#userinfo) - Get User Info

## authorize

Authorize

### Example Usage

```python
from polar_sdk import Polar

with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:
    res = polar.oauth2.authorize()

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Oauth2AuthorizeResponseOauth2Authorize](../../models/oauth2authorizeresponseoauth2authorize.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## token

Request an access token using a valid grant.

### Example Usage

```python
import polar_sdk
from polar_sdk import Polar

with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:
    res = polar.oauth2.token(request={
        "client_id": "<id>",
        "client_secret": "<value>",
        "code": "<value>",
        "redirect_uri": "https://old-fort.name",
        "grant_type": polar_sdk.GrantType.AUTHORIZATION_CODE,
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

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## revoke

Revoke an access token or a refresh token.

### Example Usage

```python
from polar_sdk import Polar

with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:
    res = polar.oauth2.revoke(request={
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

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## introspect

Get information about an access token.

### Example Usage

```python
from polar_sdk import Polar

with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:
    res = polar.oauth2.introspect(request={
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

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## userinfo

Get information about the authenticated user.

### Example Usage

```python
from polar_sdk import Polar

with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:
    res = polar.oauth2.userinfo()

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

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |