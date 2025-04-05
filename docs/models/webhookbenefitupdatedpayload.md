# WebhookBenefitUpdatedPayload

Sent when a benefit is updated.

**Discord & Slack support:** Basic


## Fields

| Field                                  | Type                                   | Required                               | Description                            | Example                                |
| -------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- |
| `type`                                 | *Literal["benefit.updated"]*           | :heavy_check_mark:                     | N/A                                    | benefit.updated                        |
| `data`                                 | [models.Benefit](../models/benefit.md) | :heavy_check_mark:                     | N/A                                    |                                        |