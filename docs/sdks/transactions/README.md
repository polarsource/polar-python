# Transactions
(*transactions*)

## Overview

### Available Operations

* [transactions_search_transactions](#transactions_search_transactions) - Search Transactions
* [transactions_lookup_transaction](#transactions_lookup_transaction) - Lookup Transaction
* [transactions_get_summary](#transactions_get_summary) - Get Summary
* [transactions_get_payout_estimate](#transactions_get_payout_estimate) - Get Payout Estimate
* [transactions_create_payout](#transactions_create_payout) - Create Payout
* [transactions_get_payout_csv](#transactions_get_payout_csv) - Get Payout Csv

## transactions_search_transactions

Search Transactions

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.transactions.transactions_search_transactions(security=polar_sh.TransactionsSearchTransactionsSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `request`                                                                                             | [models.TransactionsSearchTransactionsRequest](../../models/transactionssearchtransactionsrequest.md) | :heavy_check_mark:                                                                                    | The request object to use for the request.                                                            |
| `security`                                                                                            | [models.TransactionsSearchTransactionsSecurity](../../transactionssearchtransactionssecurity.md)      | :heavy_check_mark:                                                                                    | The security requirements to use for the request.                                                     |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |

### Response

**[models.ListResourceTransaction](../../models/listresourcetransaction.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## transactions_lookup_transaction

Lookup Transaction

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.transactions.transactions_lookup_transaction(security=polar_sh.TransactionsLookupTransactionSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), transaction_id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `security`                                                                                            | [models.TransactionsLookupTransactionSecurity](../../models/transactionslookuptransactionsecurity.md) | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `transaction_id`                                                                                      | *str*                                                                                                 | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |

### Response

**[models.TransactionDetails](../../models/transactiondetails.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## transactions_get_summary

Get Summary

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.transactions.transactions_get_summary(security=polar_sh.TransactionsGetSummarySecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), account_id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `security`                                                                              | [models.TransactionsGetSummarySecurity](../../models/transactionsgetsummarysecurity.md) | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `account_id`                                                                            | *str*                                                                                   | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[models.TransactionsSummary](../../models/transactionssummary.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## transactions_get_payout_estimate

Get Payout Estimate

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.transactions.transactions_get_payout_estimate(security=polar_sh.TransactionsGetPayoutEstimateSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), account_id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `security`                                                                                            | [models.TransactionsGetPayoutEstimateSecurity](../../models/transactionsgetpayoutestimatesecurity.md) | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `account_id`                                                                                          | *str*                                                                                                 | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |

### Response

**[models.PayoutEstimate](../../models/payoutestimate.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## transactions_create_payout

Create Payout

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.transactions.transactions_create_payout(security=polar_sh.TransactionsCreatePayoutSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), request={
    "account_id": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [models.PayoutCreate](../../models/payoutcreate.md)                                  | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `security`                                                                           | [models.TransactionsCreatePayoutSecurity](../../transactionscreatepayoutsecurity.md) | :heavy_check_mark:                                                                   | The security requirements to use for the request.                                    |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[models.Transaction](../../models/transaction.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## transactions_get_payout_csv

Get Payout Csv

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.transactions.transactions_get_payout_csv(security=polar_sh.TransactionsGetPayoutCsvSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `security`                                                                                  | [models.TransactionsGetPayoutCsvSecurity](../../models/transactionsgetpayoutcsvsecurity.md) | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `id`                                                                                        | *str*                                                                                       | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |

### Response

**[Any](../../models/.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |
