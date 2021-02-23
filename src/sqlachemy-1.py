from sqlalchemy import create_engine

# Using the synchronous MySQL driver pymysql
CONNECTION_STRING = "mysql+pymysql://root:example@localhost/exampledb"

# Creating a synchronous engine
mysql_engine = create_engine(
        CONNECTION_STRING,
        pool_recycle=3600,
        pool_size=5,
        echo=False
    )

# Test connection
connection = mysql_engine.connect()

print(connection)
connection.execute("Select 1")
print(connection.engine)

connection.close()