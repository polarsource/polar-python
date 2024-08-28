# WebhookEvent

A webhook event.

An event represent something that happened in the system
that should be sent to the webhook endpoint.

It can be delivered multiple times until it's marked as succeeded,
each one creating a new delivery.


## Fields

| Field                                                                                                            | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `created_at`                                                                                                     | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                             | :heavy_check_mark:                                                                                               | Creation timestamp of the object.                                                                                |
| `modified_at`                                                                                                    | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                             | :heavy_check_mark:                                                                                               | Last modification timestamp of the object.                                                                       |
| `id`                                                                                                             | *str*                                                                                                            | :heavy_check_mark:                                                                                               | The webhook event ID.                                                                                            |
| `payload`                                                                                                        | *str*                                                                                                            | :heavy_check_mark:                                                                                               | The payload of the webhook event.                                                                                |
| `last_http_code`                                                                                                 | *OptionalNullable[int]*                                                                                          | :heavy_minus_sign:                                                                                               | Last HTTP code returned by the URL. `null` if no delviery has been attempted or if the endpoint was unreachable. |
| `succeeded`                                                                                                      | *OptionalNullable[bool]*                                                                                         | :heavy_minus_sign:                                                                                               | Whether this event was successfully delivered. `null` if no delivery has been attempted.                         |