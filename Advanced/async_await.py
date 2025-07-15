# Async/Await Example

import asyncio

async def greet():
    print("Hello ...")
    await asyncio.sleep(1)
    print("... World!")

asyncio.run(greet())
