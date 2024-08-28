# WebhookDelivery

A webhook delivery for a webhook event.


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `created_at`                                                               | [date](https://docs.python.org/3/library/datetime.html#date-objects)       | :heavy_check_mark:                                                         | Creation timestamp of the object.                                          |
| `modified_at`                                                              | [date](https://docs.python.org/3/library/datetime.html#date-objects)       | :heavy_check_mark:                                                         | Last modification timestamp of the object.                                 |
| `id`                                                                       | *str*                                                                      | :heavy_check_mark:                                                         | The webhook delivery ID.                                                   |
| `succeeded`                                                                | *bool*                                                                     | :heavy_check_mark:                                                         | Whether the delivery was successful.                                       |
| `webhook_event`                                                            | [models.WebhookEvent](../models/webhookevent.md)                           | :heavy_check_mark:                                                         | The webhook event sent by this delivery.                                   |
| `http_code`                                                                | *OptionalNullable[int]*                                                    | :heavy_minus_sign:                                                         | The HTTP code returned by the URL. `null` if the endpoint was unreachable. |