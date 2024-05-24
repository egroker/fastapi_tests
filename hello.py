import asyncio

async def custom_coroutine():
    asyncio.sleep(1)
    print("Hello World")

asyncio.run(custom_coroutine())