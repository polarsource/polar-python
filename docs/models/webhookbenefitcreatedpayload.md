# WebhookBenefitCreatedPayload

Sent when a new benefit is created.

**Discord & Slack support:** Basic


## Fields

| Field                                  | Type                                   | Required                               | Description                            |
| -------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- |
| `data`                                 | [models.Benefit](../models/benefit.md) | :heavy_check_mark:                     | N/A                                    |
| `type`                                 | *Literal["benefit.created"]*           | :heavy_check_mark:                     | N/A                                    |