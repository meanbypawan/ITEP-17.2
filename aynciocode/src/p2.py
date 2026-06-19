import asyncio

print("At the start.....") # Synchronous Main-Thread
async def eating_pizza(): # event loop
    print("Eating pizza....")
    await asyncio.sleep(2)
    print("Pizza done....")

async def servicing_car(): # event loop
    print("Servicing car....")
    await asyncio.sleep(3)
    print("Servicing done....")

async def meeting_with_friends(): # event loop
    print("Meeting with friends....")
    await asyncio.sleep(1)
    print("Meeting done....")

async def main():
    await asyncio.gather(eating_pizza(), servicing_car(), meeting_with_friends())

asyncio.run(main()) # event loop

print("At the end.......") # Main-Thread