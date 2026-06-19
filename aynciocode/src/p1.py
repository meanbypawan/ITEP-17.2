import time
import asyncio
print("At the start......")

async def eating_pizza():
    print("Eating Pizza in progress....")
    await asyncio.sleep(2)
    print("Pizza done...")

asyncio.run(eating_pizza())
print("At the end..............")
