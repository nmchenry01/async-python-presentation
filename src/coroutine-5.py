import asyncio
import time

async def me_first() -> str:
    await asyncio.sleep(1)

    return "I'm first!"

async def me_second() -> str:
    await asyncio.sleep(1)

    return "Then me!"

async def me_third() -> str:
    await asyncio.sleep(1)

    return "And finally me!"

async def main():
    start = time.perf_counter()

    # Init all coroutines
    first_coroutine = me_first()
    second_coroutine = me_second()
    third_coroutine = me_third()
    
    # Schedule all coroutines to run concurrently and wait on all to return
    result = await asyncio.gather(*[first_coroutine, second_coroutine, third_coroutine])

    end = time.perf_counter()

    print(f"It took {end - start} seconds to complete all operations\n")
    
    print(result)


asyncio.run(main())