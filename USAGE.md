<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.users.benefits.list(security=polar_sh.UsersBenefitsListSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
))

if res is not None:
    while True:
        # handle items

        res = res.Next()
        if res is None:
            break

```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
import polar_sh
from polar_sh import Polar

async def main():
    s = Polar()
    res = await s.users.benefits.list_async(security=polar_sh.UsersBenefitsListSecurity(
        open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
    ))
    if res is not None:
        while True:
            # handle items
    
            res = res.Next()
            if res is None:
                break

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->