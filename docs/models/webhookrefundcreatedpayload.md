# WebhookRefundCreatedPayload

Sent when a refund is created regardless of status.

**Discord & Slack support:** Full


## Fields

| Field                                | Type                                 | Required                             | Description                          |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `data`                               | [models.Refund](../models/refund.md) | :heavy_check_mark:                   | N/A                                  |
| `type`                               | *Literal["refund.created"]*          | :heavy_check_mark:                   | N/A                                  |