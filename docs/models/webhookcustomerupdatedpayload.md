# WebhookCustomerUpdatedPayload

Sent when a customer is updated.

This event is fired when the customer details are updated.

If you want to be notified when a customer subscription or benefit state changes, you should listen to the `customer_state_changed` event.

**Discord & Slack support:** Basic


## Fields

| Field                                    | Type                                     | Required                                 | Description                              | Example                                  |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| `type`                                   | *Literal["customer.updated"]*            | :heavy_check_mark:                       | N/A                                      | customer.updated                         |
| `data`                                   | [models.Customer](../models/customer.md) | :heavy_check_mark:                       | A customer in an organization.           |                                          |