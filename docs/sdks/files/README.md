# Files
(*files*)

## Overview

### Available Operations

* [list](#list) - List Files
* [create](#create) - Create File
* [uploaded](#uploaded) - Complete File Upload
* [update](#update) - Update File
* [delete](#delete) - Delete File

## list

List files.

**Scopes**: `files:read` `files:write`

### Example Usage

```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.files.list(organization_id="1dbfc517-0bbf-4301-9ba8-555ca42b9737")

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                   | Type                                                                                                                        | Required                                                                                                                    | Description                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `organization_id`                                                                                                           | [OptionalNullable[models.FilesListQueryParamOrganizationIDFilter]](../../models/fileslistqueryparamorganizationidfilter.md) | :heavy_minus_sign:                                                                                                          | Filter by organization ID.                                                                                                  |
| `ids`                                                                                                                       | [OptionalNullable[models.FileIDFilter]](../../models/fileidfilter.md)                                                       | :heavy_minus_sign:                                                                                                          | Filter by file ID.                                                                                                          |
| `page`                                                                                                                      | *Optional[int]*                                                                                                             | :heavy_minus_sign:                                                                                                          | Page number, defaults to 1.                                                                                                 |
| `limit`                                                                                                                     | *Optional[int]*                                                                                                             | :heavy_minus_sign:                                                                                                          | Size of a page, defaults to 10. Maximum is 100.                                                                             |
| `retries`                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                            | :heavy_minus_sign:                                                                                                          | Configuration to override the default retry behavior of the client.                                                         |

### Response

**[models.FilesListResponse](../../models/fileslistresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## create

Create a file.

**Scopes**: `files:write`

### Example Usage

```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.files.create(request={
        "name": "<value>",
        "mime_type": "<value>",
        "size": 612128,
        "upload": {
            "parts": [],
        },
        "service": "downloadable",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.FileCreate](../../models/filecreate.md)                     | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.FileUpload](../../models/fileupload.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## uploaded

Complete a file upload.

**Scopes**: `files:write`

### Example Usage

```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.files.uploaded(id="<value>", file_upload_completed={
        "id": "<id>",
        "path": "/boot",
        "parts": [
            {
                "number": 979613,
                "checksum_etag": "<value>",
                "checksum_sha256_base64": "<value>",
            },
            {
                "number": 979613,
                "checksum_etag": "<value>",
                "checksum_sha256_base64": "<value>",
            },
            {
                "number": 979613,
                "checksum_etag": "<value>",
                "checksum_sha256_base64": "<value>",
            },
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The file ID.                                                        |
| `file_upload_completed`                                             | [models.FileUploadCompleted](../../models/fileuploadcompleted.md)   | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.FilesUploadedResponseFilesUploaded](../../models/filesuploadedresponsefilesuploaded.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotPermitted        | 403                        | application/json           |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## update

Update a file.

**Scopes**: `files:write`

### Example Usage

```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.files.update(id="<value>", file_patch={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The file ID.                                                        |
| `file_patch`                                                        | [models.FilePatch](../../models/filepatch.md)                       | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.FilesUpdateResponseFilesUpdate](../../models/filesupdateresponsefilesupdate.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotPermitted        | 403                        | application/json           |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## delete

Delete a file.

**Scopes**: `files:write`

### Example Usage

```python
from polar_sdk import Polar


with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    polar.files.delete(id="<value>")

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
| models.NotPermitted        | 403                        | application/json           |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |