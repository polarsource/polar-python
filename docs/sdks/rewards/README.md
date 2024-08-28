# Rewards
(*rewards*)

## Overview

### Available Operations

* [rewards_search](#rewards_search) - Search rewards
* [rewards_summary](#rewards_summary) - Get rewards summary

## rewards_search

Search rewards.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.rewards.rewards_search(security=polar_sh.RewardsSearchSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `security`                                                            | [models.RewardsSearchSecurity](../../models/rewardssearchsecurity.md) | :heavy_check_mark:                                                    | N/A                                                                   |
| `pledges_to_organization`                                             | *OptionalNullable[str]*                                               | :heavy_minus_sign:                                                    | Search rewards for pledges in this organization.                      |
| `rewards_to_user`                                                     | *OptionalNullable[str]*                                               | :heavy_minus_sign:                                                    | Search rewards to user.                                               |
| `rewards_to_org`                                                      | *OptionalNullable[str]*                                               | :heavy_minus_sign:                                                    | Search rewards to organization.                                       |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.ListResourceReward](../../models/listresourcereward.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## rewards_summary

Get summary of rewards for resource.

### Example Usage

```python
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.rewards.rewards_summary(security=polar_sh.RewardsSummarySecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
), issue_id="cb6043ae-c425-4d48-9684-ded68f9c39d6")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `security`                                                              | [models.RewardsSummarySecurity](../../models/rewardssummarysecurity.md) | :heavy_check_mark:                                                      | N/A                                                                     |
| `issue_id`                                                              | *str*                                                                   | :heavy_check_mark:                                                      | N/A                                                                     |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.RewardsSummary](../../models/rewardssummary.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |
