# Articles
(*articles*)

## Overview

### Available Operations

* [list](#list) - List Articles
* [create](#create) - Create Article
* [retrieve](#retrieve) - Get Article
* [delete](#delete) - Delete Article
* [update](#update) - Update Article
* [receivers](#receivers) - Get Article Receivers Count
* [preview](#preview) - Send Article Preview
* [send](#send) - Send Article

## list

List articles.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.articles.list(security=polar_sh.ArticlesListSecurity(
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

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.ArticlesListRequest](../../models/articleslistrequest.md)   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `security`                                                          | [models.ArticlesListSecurity](../../articleslistsecurity.md)        | :heavy_check_mark:                                                  | The security requirements to use for the request.                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ArticlesListResponse](../../models/articleslistresponse.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## create

Create an article.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.articles.create(security=polar_sh.ArticlesCreateSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), request={
    "title": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.ArticleCreate](../../models/articlecreate.md)               | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `security`                                                          | [models.ArticlesCreateSecurity](../../articlescreatesecurity.md)    | :heavy_check_mark:                                                  | The security requirements to use for the request.                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Article](../../models/article.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## retrieve

Get an article by ID.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.articles.retrieve(security=polar_sh.ArticlesGetSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `security`                                                          | [models.ArticlesGetSecurity](../../models/articlesgetsecurity.md)   | :heavy_check_mark:                                                  | N/A                                                                 |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Article](../../models/article.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## delete

Delete an article.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


s.articles.delete(security=polar_sh.ArticlesDeleteSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>")

# Use the SDK ...

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `security`                                                              | [models.ArticlesDeleteSecurity](../../models/articlesdeletesecurity.md) | :heavy_check_mark:                                                      | N/A                                                                     |
| `id`                                                                    | *str*                                                                   | :heavy_check_mark:                                                      | N/A                                                                     |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotPermitted        | 403                        | application/json           |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## update

Update an article.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.articles.update(security=polar_sh.ArticlesUpdateSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>", article_update={})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `security`                                                              | [models.ArticlesUpdateSecurity](../../models/articlesupdatesecurity.md) | :heavy_check_mark:                                                      | N/A                                                                     |
| `id`                                                                    | *str*                                                                   | :heavy_check_mark:                                                      | N/A                                                                     |
| `article_update`                                                        | [models.ArticleUpdate](../../models/articleupdate.md)                   | :heavy_check_mark:                                                      | N/A                                                                     |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.Article](../../models/article.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotPermitted        | 403                        | application/json           |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## receivers

Get number of potential receivers for an article.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.articles.receivers(security=polar_sh.ArticlesReceiversSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `security`                                                                    | [models.ArticlesReceiversSecurity](../../models/articlesreceiverssecurity.md) | :heavy_check_mark:                                                            | N/A                                                                           |
| `id`                                                                          | *str*                                                                         | :heavy_check_mark:                                                            | N/A                                                                           |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[models.ArticleReceivers](../../models/articlereceivers.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## preview

Send an article preview by email.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.articles.preview(security=polar_sh.ArticlesPreviewSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>", article_preview={
    "email": "Eileen56@yahoo.com",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `security`                                                                | [models.ArticlesPreviewSecurity](../../models/articlespreviewsecurity.md) | :heavy_check_mark:                                                        | N/A                                                                       |
| `id`                                                                      | *str*                                                                     | :heavy_check_mark:                                                        | N/A                                                                       |
| `article_preview`                                                         | [models.ArticlePreview](../../models/articlepreview.md)                   | :heavy_check_mark:                                                        | N/A                                                                       |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[Any](../../models/.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotPermitted        | 403                        | application/json           |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## send

Send an article by email to all subscribers.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.articles.send(security=polar_sh.ArticlesSendSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `security`                                                          | [models.ArticlesSendSecurity](../../models/articlessendsecurity.md) | :heavy_check_mark:                                                  | N/A                                                                 |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Any](../../models/.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotPermitted        | 403                        | application/json           |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |
