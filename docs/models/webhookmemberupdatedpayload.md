# WebhookMemberUpdatedPayload

Sent when a member is updated.

This event is triggered when member details are updated,
such as their name or role within the customer.

**Discord & Slack support:** Basic


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `type`                                                               | *Literal["member.updated"]*                                          | :heavy_check_mark:                                                   | N/A                                                                  | member.updated                                                       |
| `timestamp`                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |                                                                      |
| `data`                                                               | [models.Member](../models/member.md)                                 | :heavy_check_mark:                                                   | A member of a customer.                                              |                                                                      |