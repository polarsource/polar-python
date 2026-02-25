# WebhookMemberDeletedPayload

Sent when a member is deleted.

This event is triggered when a member is removed from a customer.
Any active seats assigned to the member will be automatically revoked.

**Discord & Slack support:** Basic


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `type`                                                               | *Literal["member.deleted"]*                                          | :heavy_check_mark:                                                   | N/A                                                                  | member.deleted                                                       |
| `timestamp`                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |                                                                      |
| `data`                                                               | [models.Member](../models/member.md)                                 | :heavy_check_mark:                                                   | A member of a customer.                                              |                                                                      |