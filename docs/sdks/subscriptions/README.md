# Subscriptions
(*subscriptions*)

## Overview

### Available Operations

* [subscriptions_list](#subscriptions_list) - List Subscriptions
* [subscriptions_create](#subscriptions_create) - Create Free Subscription
* [subscriptions_import](#subscriptions_import) - Import Subscriptions
* [subscriptions_export](#subscriptions_export) - Export Subscriptions

## subscriptions_list

List subscriptions.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.subscriptions.subscriptions_list(security=polar_sh.SubscriptionsListSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `request`                                                                   | [models.SubscriptionsListRequest](../../models/subscriptionslistrequest.md) | :heavy_check_mark:                                                          | The request object to use for the request.                                  |
| `security`                                                                  | [models.SubscriptionsListSecurity](../../subscriptionslistsecurity.md)      | :heavy_check_mark:                                                          | The security requirements to use for the request.                           |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.ListResourceSubscription](../../models/listresourcesubscription.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## subscriptions_create

Create a subscription on the free tier for a given email.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.subscriptions.subscriptions_create(security=polar_sh.SubscriptionsCreateSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), request={
    "email": "Paxton_Schaden@hotmail.com",
    "product_id": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [models.SubscriptionCreateEmail](../../models/subscriptioncreateemail.md)  | :heavy_check_mark:                                                         | The request object to use for the request.                                 |
| `security`                                                                 | [models.SubscriptionsCreateSecurity](../../subscriptionscreatesecurity.md) | :heavy_check_mark:                                                         | The security requirements to use for the request.                          |
| `retries`                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)           | :heavy_minus_sign:                                                         | Configuration to override the default retry behavior of the client.        |

### Response

**[models.SubscriptionOutput](../../models/subscriptionoutput.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## subscriptions_import

Import subscriptions from a CSV file.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.subscriptions.subscriptions_import(security=polar_sh.SubscriptionsImportSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), request={
    "file": {
        "file_name": "your_file_here",
        "content": open("<file_path>", "rb"),
    },
    "organization_id": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [models.BodySubscriptionsImport](../../models/bodysubscriptionsimport.md)  | :heavy_check_mark:                                                         | The request object to use for the request.                                 |
| `security`                                                                 | [models.SubscriptionsImportSecurity](../../subscriptionsimportsecurity.md) | :heavy_check_mark:                                                         | The security requirements to use for the request.                          |
| `retries`                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)           | :heavy_minus_sign:                                                         | Configuration to override the default retry behavior of the client.        |

### Response

**[models.SubscriptionsImported](../../models/subscriptionsimported.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## subscriptions_export

Export subscriptions as a CSV file.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.subscriptions.subscriptions_export(security=polar_sh.SubscriptionsExportSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `security`                                                                        | [models.SubscriptionsExportSecurity](../../models/subscriptionsexportsecurity.md) | :heavy_check_mark:                                                                | N/A                                                                               |
| `organization_id`                                                                 | [OptionalNullable[models.OrganizationID]](../../models/organizationid.md)         | :heavy_minus_sign:                                                                | Filter by organization ID.                                                        |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[Any](../../models/.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |
