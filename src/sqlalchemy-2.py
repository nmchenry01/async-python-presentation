from sqlalchemy import create_engine, text
from pprint import pprint

# Using the synchronous MySQL driver pymysql
CONNECTION_STRING = "mysql+pymysql://root:example@localhost/exampledb"

# Creating a synchronous engine
mysql_engine = create_engine(
        CONNECTION_STRING,
        pool_recycle=3600,
        pool_size=5,
        echo=False
    )

sql_statement = "SELECT * from exampledb.`todo` limit 3;"

# Connect, execute SQL, and print results
# NOTE: The "with" statment here is a context manager. It handles close the connection automatically when it falls out of scope
with mysql_engine.begin() as connection:
    results = connection.execute(text(sql_statement)).fetchall()
    
    pprint(results)
