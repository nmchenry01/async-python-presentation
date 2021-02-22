import asyncio

async def something_async() -> str:
    # Wait 3 seconds
    await asyncio.sleep(3)

    return "I'm async (sortof) now!"

def main():
    result = something_async()

    print(result)

main()