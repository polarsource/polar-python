<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
import polar_sh
from polar_sh import Polar

s = Polar()


res = s.users.users_list_benefits(security=polar_sh.UsersListBenefitsSecurity(
    open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
))

if res is not None:
    # handle response
    pass
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
    res = await s.users.users_list_benefits_async(security=polar_sh.UsersListBenefitsSecurity(
        open_id_connect="<YOUR_OPEN_ID_CONNECT_HERE>",
    ))
    if res is not None:
        # handle response
        pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->