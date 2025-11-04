# LLMMetadata


## Fields

| Field                                                         | Type                                                          | Required                                                      | Description                                                   |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| `vendor`                                                      | *str*                                                         | :heavy_check_mark:                                            | The vendor of the event.                                      |
| `model`                                                       | *str*                                                         | :heavy_check_mark:                                            | The model used for the event.                                 |
| `prompt`                                                      | *OptionalNullable[str]*                                       | :heavy_minus_sign:                                            | The LLM prompt used for the event.                            |
| `response`                                                    | *OptionalNullable[str]*                                       | :heavy_minus_sign:                                            | The LLM response used for the event.                          |
| `input_tokens`                                                | *int*                                                         | :heavy_check_mark:                                            | The number of LLM input tokens used for the event.            |
| `cached_input_tokens`                                         | *Optional[int]*                                               | :heavy_minus_sign:                                            | The number of LLM cached tokens that were used for the event. |
| `output_tokens`                                               | *int*                                                         | :heavy_check_mark:                                            | The number of LLM output tokens used for the event.           |
| `total_tokens`                                                | *int*                                                         | :heavy_check_mark:                                            | The total number of LLM tokens used for the event.            |