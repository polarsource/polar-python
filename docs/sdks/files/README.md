# Files
(*files*)

## Overview

### Available Operations

* [list](#list) - List Files
* [create](#create) - Create File
* [files_uploaded](#files_uploaded) - Complete File Upload
* [delete](#delete) - Delete File
* [update](#update) - Update File

## list

List files.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.files.list(security=polar_sh.FilesListSecurity(
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
| `security`                                                          | [models.FilesListSecurity](../../models/fileslistsecurity.md)       | :heavy_check_mark:                                                  | N/A                                                                 |
| `organization_id`                                                   | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `ids`                                                               | List[*str*]                                                         | :heavy_minus_sign:                                                  | List of file IDs to get.                                            |
| `page`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Page number, defaults to 1.                                         |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Size of a page, defaults to 10. Maximum is 100.                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.FilesListResponse](../../models/fileslistresponse.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## create

Create a file.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.files.create(security=polar_sh.FilesCreateSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), request={
    "name": "<value>",
    "mime_type": "<value>",
    "size": 489382,
    "upload": {
        "parts": [
            {
                "number": 638424,
                "chunk_start": 859213,
                "chunk_end": 417458,
            },
        ],
    },
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `request`                                                             | [models.FilesCreateFileCreate](../../models/filescreatefilecreate.md) | :heavy_check_mark:                                                    | The request object to use for the request.                            |
| `security`                                                            | [models.FilesCreateSecurity](../../filescreatesecurity.md)            | :heavy_check_mark:                                                    | The security requirements to use for the request.                     |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.FileUpload](../../models/fileupload.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## files_uploaded

Complete a file upload.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.files.files_uploaded(security=polar_sh.FilesUploadedSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>", file_upload_completed={
    "id": "<id>",
    "path": "/private/tmp",
    "parts": [
        {
            "number": 944087,
            "checksum_etag": "<value>",
            "checksum_sha256_base64": "<value>",
        },
    ],
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `security`                                                            | [models.FilesUploadedSecurity](../../models/filesuploadedsecurity.md) | :heavy_check_mark:                                                    | N/A                                                                   |
| `id`                                                                  | *str*                                                                 | :heavy_check_mark:                                                    | The file ID.                                                          |
| `file_upload_completed`                                               | [models.FileUploadCompleted](../../models/fileuploadcompleted.md)     | :heavy_check_mark:                                                    | N/A                                                                   |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.FilesUploadedResponseFilesUploaded](../../models/filesuploadedresponsefilesuploaded.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## delete

Delete a file.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


s.files.delete(security=polar_sh.FilesDeleteSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>")

# Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `security`                                                          | [models.FilesDeleteSecurity](../../models/filesdeletesecurity.md)   | :heavy_check_mark:                                                  | N/A                                                                 |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.NotPermitted        | 403                        | application/json           |
| models.FileNotFound        | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## update

Update a file.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.files.update(security=polar_sh.FilesUpdateSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>", file_patch={})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `security`                                                          | [models.FilesUpdateSecurity](../../models/filesupdatesecurity.md)   | :heavy_check_mark:                                                  | N/A                                                                 |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The file ID.                                                        |
| `file_patch`                                                        | [models.FilePatch](../../models/filepatch.md)                       | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.FilesUpdateResponseFilesUpdate](../../models/filesupdateresponsefilesupdate.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |
