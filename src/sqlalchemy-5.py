from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine
import asyncio
import time
from datetime import datetime


async def main():
    # Using the async MySQL driver aiomysql
    CONNECTION_STRING = "mysql+aiomysql://root:example@localhost/exampledb"

    # Creating an async engine
    async_mysql_engine = create_async_engine(
        CONNECTION_STRING,
        pool_recycle=3600,
        pool_size=10,
        echo=False
    )

    sql_statement = "SELECT * from exampledb.`todo`;"

    # Async version of big read operation
    async def some_big_read_operation():
        print(f"I started at {datetime.now()}\n")
        async with async_mysql_engine.connect() as connection:
            await connection.execute(text(sql_statement))

    # Now do it 10 times and time it
    coroutine_list = [some_big_read_operation() for _ in range(10)]
    
    start = time.perf_counter()
    await asyncio.gather(*coroutine_list)
    end = time.perf_counter()
    print(f"It took {end - start} seconds to read a boatload of data")


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
