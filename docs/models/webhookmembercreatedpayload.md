# WebhookMemberCreatedPayload

Sent when a new member is created.

A member represents an individual within a customer (team).
This event is triggered when a member is added to a customer,
either programmatically via the API or when an owner is automatically
created for a new customer.

**Discord & Slack support:** Basic


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `type`                                                               | *Literal["member.created"]*                                          | :heavy_check_mark:                                                   | N/A                                                                  | member.created                                                       |
| `timestamp`                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |                                                                      |
| `data`                                                               | [models.Member](../models/member.md)                                 | :heavy_check_mark:                                                   | A member of a customer.                                              |                                                                      |