# WebhookOrganizationUpdatedPayload

Sent when a organization is updated.

**Discord & Slack support:** Basic


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `type`                                                               | *Literal["organization.updated"]*                                    | :heavy_check_mark:                                                   | N/A                                                                  | organization.updated                                                 |
| `timestamp`                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |                                                                      |
| `data`                                                               | [models.Organization](../models/organization.md)                     | :heavy_check_mark:                                                   | N/A                                                                  |                                                                      |