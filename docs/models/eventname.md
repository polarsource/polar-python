# EventName


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `name`                                                               | *str*                                                                | :heavy_check_mark:                                                   | The name of the event.                                               |
| `occurrences`                                                        | *int*                                                                | :heavy_check_mark:                                                   | Number of times the event has occurred.                              |
| `first_seen`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | The first time the event occurred.                                   |
| `last_seen`                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | The last time the event occurred.                                    |