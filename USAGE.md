<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from polar_sdk import Polar

with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.external_organizations.list()

    while res is not None:
        # Handle items

        res = res.next()
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from polar_sdk import Polar

async def main():
    async with Polar(
        access_token="<YOUR_BEARER_TOKEN_HERE>",
    ) as polar:

        res = await polar.external_organizations.list_async()

        while res is not None:
            # Handle items

            res = res.next()

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->