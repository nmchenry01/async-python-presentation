from sqlalchemy import create_engine, text
import time
from datetime import datetime

# Using the synchronous MySQL driver pymysql
CONNECTION_STRING = "mysql+pymysql://root:example@localhost/exampledb"

# Creating a synchronous engine
mysql_engine = create_engine(
        CONNECTION_STRING,
        pool_recycle=3600,
        pool_size=5,
        echo=False
    )

sql_statement = "SELECT * from exampledb.`todo`;"

def some_big_read_operation():
    print(f"I started at {datetime.now()}\n")
    with mysql_engine.begin() as connection:
        connection.execute(text(sql_statement)).fetchall()

# Reading 20k rows each time
some_big_read_operation()

# Now do it 10 times and time it
start = time.perf_counter()
for _ in range(10):
    some_big_read_operation()
end = time.perf_counter()

print(f"It took {end - start} seconds to read a boatload of data")
