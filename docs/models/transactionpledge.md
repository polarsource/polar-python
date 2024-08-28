# TransactionPledge


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `created_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Creation timestamp of the object.                                    |
| `modified_at`                                                        | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Last modification timestamp of the object.                           |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `state`                                                              | [models.PledgeState](../models/pledgestate.md)                       | :heavy_check_mark:                                                   | N/A                                                                  |
| `issue`                                                              | [models.TransactionIssue](../models/transactionissue.md)             | :heavy_check_mark:                                                   | N/A                                                                  |