# PolarAdvertisements
(*users.advertisements*)

## Overview

### Available Operations

* [list](#list) - List Advertisements
* [create](#create) - Create Advertisement
* [retrieve](#retrieve) - Get Advertisement
* [delete](#delete) - Delete Advertisement
* [update](#update) - Update Advertisement
* [enable](#enable) - Enable Advertisement

## list

List advertisement campaigns.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.users.advertisements.list(security=polar_sh.UsersAdvertisementsListSecurity(
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

| Parameter                                                                                                                                                               | Type                                                                                                                                                                    | Required                                                                                                                                                                | Description                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                                              | [models.UsersAdvertisementsListSecurity](../../models/usersadvertisementslistsecurity.md)                                                                               | :heavy_check_mark:                                                                                                                                                      | N/A                                                                                                                                                                     |
| `page`                                                                                                                                                                  | *Optional[int]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | Page number, defaults to 1.                                                                                                                                             |
| `limit`                                                                                                                                                                 | *Optional[int]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | Size of a page, defaults to 10. Maximum is 100.                                                                                                                         |
| `sorting`                                                                                                                                                               | List[[models.UserAdvertisementSortProperty](../../models/useradvertisementsortproperty.md)]                                                                             | :heavy_minus_sign:                                                                                                                                                      | Sorting criterion. Several criteria can be used simultaneously and will be applied in order. Add a minus sign `-` before the criteria name to sort by descending order. |
| `retries`                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                        | :heavy_minus_sign:                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                     |

### Response

**[models.UsersAdvertisementsListResponse](../../models/usersadvertisementslistresponse.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## create

Create an advertisement campaign.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.users.advertisements.create(security=polar_sh.UsersAdvertisementsCreateSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), request={
    "image_url": "http://limp-pastry.org",
    "text": "<value>",
    "link_url": "http://flashy-cartload.net",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `request`                                                                                 | [models.UserAdvertisementCampaignCreate](../../models/useradvertisementcampaigncreate.md) | :heavy_check_mark:                                                                        | The request object to use for the request.                                                |
| `security`                                                                                | [models.UsersAdvertisementsCreateSecurity](../../usersadvertisementscreatesecurity.md)    | :heavy_check_mark:                                                                        | The security requirements to use for the request.                                         |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |

### Response

**[models.UserAdvertisementCampaign](../../models/useradvertisementcampaign.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## retrieve

Get an advertisement campaign by ID.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.users.advertisements.retrieve(security=polar_sh.UsersAdvertisementsGetSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `security`                                                                              | [models.UsersAdvertisementsGetSecurity](../../models/usersadvertisementsgetsecurity.md) | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `id`                                                                                    | *str*                                                                                   | :heavy_check_mark:                                                                      | The advertisement campaign ID.                                                          |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[models.UserAdvertisementCampaign](../../models/useradvertisementcampaign.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## delete

Delete an advertisement campaign.

It'll be automatically disabled on all granted benefits.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.users.advertisements.delete(security=polar_sh.UsersAdvertisementsDeleteSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `security`                                                                                    | [models.UsersAdvertisementsDeleteSecurity](../../models/usersadvertisementsdeletesecurity.md) | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `id`                                                                                          | *str*                                                                                         | :heavy_check_mark:                                                                            | The advertisement campaign ID.                                                                |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |

### Response

**[Any](../../models/.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## update

Update an advertisement campaign.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.users.advertisements.update(security=polar_sh.UsersAdvertisementsUpdateSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>", user_advertisement_campaign_update={})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `security`                                                                                    | [models.UsersAdvertisementsUpdateSecurity](../../models/usersadvertisementsupdatesecurity.md) | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `id`                                                                                          | *str*                                                                                         | :heavy_check_mark:                                                                            | The advertisement campaign ID.                                                                |
| `user_advertisement_campaign_update`                                                          | [models.UserAdvertisementCampaignUpdate](../../models/useradvertisementcampaignupdate.md)     | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |

### Response

**[models.UserAdvertisementCampaign](../../models/useradvertisementcampaign.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## enable

Enable an advertisement campaign on a granted benefit.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


s.users.advertisements.enable(security=polar_sh.UsersAdvertisementsEnableSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>", user_advertisement_campaign_enable={
    "benefit_id": "<value>",
})

# Use the SDK ...

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `security`                                                                                    | [models.UsersAdvertisementsEnableSecurity](../../models/usersadvertisementsenablesecurity.md) | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `id`                                                                                          | *str*                                                                                         | :heavy_check_mark:                                                                            | The advertisement campaign ID.                                                                |
| `user_advertisement_campaign_enable`                                                          | [models.UserAdvertisementCampaignEnable](../../models/useradvertisementcampaignenable.md)     | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |
