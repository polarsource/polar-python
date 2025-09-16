# WebhookCustomerStateChangedPayload

Sent when a customer state has changed.

It's triggered when:

* Customer is created, updated or deleted.
* A subscription is created or updated.
* A benefit is granted or revoked.

**Discord & Slack support:** Basic


## Fields

| Field                                                                                                          | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    | Example                                                                                                        |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `type`                                                                                                         | *Literal["customer.state_changed"]*                                                                            | :heavy_check_mark:                                                                                             | N/A                                                                                                            | customer.state_changed                                                                                         |
| `timestamp`                                                                                                    | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                           | :heavy_check_mark:                                                                                             | N/A                                                                                                            |                                                                                                                |
| `data`                                                                                                         | [models.CustomerState](../models/customerstate.md)                                                             | :heavy_check_mark:                                                                                             | A customer along with additional state information:<br/><br/>* Active subscriptions<br/>* Granted benefits<br/>* Active meters |                                                                                                                |