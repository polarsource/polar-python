<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from polar_sdk import Polar

with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as s:
    res = s.users.benefits.list()

    if res is not None:
        while True:
            # handle items

            res = res.next()
            if res is None:
                break
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
    ) as s:
        res = await s.users.benefits.list_async()

        if res is not None:
            while True:
                # handle items

                res = res.next()
                if res is None:
                    break

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->