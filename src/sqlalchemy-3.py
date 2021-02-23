from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Using the synchronous MySQL driver pymysql
CONNECTION_STRING = "mysql+pymysql://root:example@localhost/exampledb"

# Creating a synchronous engine
mysql_engine = create_engine(
        CONNECTION_STRING,
        pool_recycle=3600,
        pool_size=5,
        echo=False
    )

# Generate sessions, which manage persistence for ORM-mapped objects
session_maker = sessionmaker(bind=mysql_engine)

# Create an object mapping to the database schema
Base = declarative_base()

class Todo(Base):
    __tablename__ = 'todo'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)

# Select 3 entities
with session_maker() as session:
    todos = session.query(Todo).limit(3).all()

    for todo in todos:
        print(f"A todo with id {todo.id} and priority {todo.priority}")

print("\n")

# Find the total number of entities in the DB
with session_maker() as session:
    number_of_todos = session.query(Todo).count()

    print(f"There are {number_of_todos} todo entities in the database")

