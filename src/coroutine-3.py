import asyncio

async def something_async() -> str:
    # Wait 3 seconds
    await asyncio.sleep(3)

    return "Now we're cooking with fire!"

async def main():
    result = await something_async()
    
    print(result)

asyncio.run(main())