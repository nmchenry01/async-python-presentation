# Overview

---

<p align="center">
  <img width="500" height="340" src="assets/python-pseudo.jpg">
</p>

## Who is this for?

- Anyone (technical) working with Python and data!

## What will be covered?

- Asynchronous Programming and Key Concepts (5 minutes)

- Asynchronous Programming in Python (5-7 minutes)

- The SQLAlchemy ORM (5-7 minutes)

- Asynchronous SQLAlchemy (2-3 minutes)

## Why should I care about this?

- Asynchronous programming is becomming more and more popular in the Python programming language, given the need for increased performance and to compete with other languages/runtimes that embrace the concept natively (Go, Node.js, C#, etc)

- Whether you're a developer, data scientist, business analyst, etc, accessing data is a crucial part of creating impactful programs. If you use Python (and need to access data), you'll likely end up using SQLAlchemy given it's the most popular ORM (object-relational model) in the ecosystem. Did I mention the next major release of it is going async?

# Introduction to Asynchronous Programming

---

> **Asynchrony**, in computer programming, refers to the occurrence of events independent of the main program flow and ways to deal with such events
> These may be "outside" events such as the arrival of signals, or actions instigated by a program that take place concurrently with program execution, without the program blocking to wait for results. **-Wikipedia**

<p align="center">
  <img width="500" height="340" src="assets/maths.gif">
</p>

Well that definition is certainly a mouthful...

I find the following definition a little more pragmatic:

> Asynchronous programming is a form of parallel programming that allows a unit of work to run separately from the primary application thread

A little better, but what is "parallel programming"? Let's explore some key definitions we'll need to talk meaningfully about asynchronous programming.

## Key Concepts

### Threads

Depending on whether you're talking about hardware or software, there are a couple different types of "threads". At a high level, we can generalize a thread as something on your computer that can do a unit of computational work.

- **Hardware Thread** - In theory, this is based off of the number of CPUs on your computer (IE, 4 CPUs = 4 hardware threads, or the ability for your computer to do 4 things at once). However, modern CPUs use something called "hyperthreading" so in practice the number of hardware threads is higher than the number of CPUs

- **Software/OS Thread** - Your operating system (OS) has it's own abstraction of a "thread". Your OS dispatches "work" to these threads, which in turn are run on hardware threads (the hardware thread can be thought of like the "engine" that the software thread runs on)

<p align="center">
  <img width="500" height="340" src="assets/threads.png">
</p>

### Parallelism

This is the idea of performing multiple operations at the same time. Your computer has multiple CPUs and hardware threads, therefore theoretically it can (and does) do multiple things at the same time.

The more precise term for spreading work over a computers CPUs is **`Multiprocessing`**. This type of parallelism is very good in the case where you have a **`CPU bound`** task, or a task where the time to complete it is mainly derived from the speed at which CPU(s) can process it.

Many machine learning algorithms and other mathematically intensive computations fall in to this category.

### Concurrency

Concurrency is very similar to parallelism, but with one important distinction. It suggests that tasks _can_ run at the same time (but don't necessarily have to).

Parallelism is concurrency, but not vice versa.

Many modern programming languages embrace concurrency, and it is particularly useful for addressing the inefficiences of **`I/O bound`** tasks. An I/O (input/output) bound task is one in which the time to complete it is mainly derived from the time spent waiting for some I/O operation to complete. Examples of these are reading from the local file system, making an HTTP request, or waiting on data from a database.

Below is a visualization that always helps me differentiate parallelism and concurrency:

<p align="center">
  <img width="500" height="340" src="assets/concurrency-vs-parallelism.jpg">
</p>

# Asynchronous Programming in Python

Moving forward, we'll talk a little more about concurrency and asynchronous programming in the context of Python.

NOTE: In the interest of time, we'll skip the history and evolution of concurrency in Python. Though if you're interested, you should 100% watch this [Youtube video](https://www.youtube.com/watch?v=MCs5OvhV9S4&ab_channel=PyCon2015).

---

## So How Does Python (Conceptually) Do Concurrency?

To cut to the chase, the top half of the below diagram illustrates (at a high level) how Python does concurrency:

<p align="center">
  <img width="500" height="340" src="assets/python-concurrency.jpg">
</p>

For every Python process, only one thing can be running at any given time. This is due to the fact that Python has a construct called the **`GIL`**, or _Global Interpreter Lock_.

The reasoning around the existence of the GIL is outside the scope of this talk, but it's contributed both to Python's success and to some of it's current limititations.

But what controls what gets to run at any particular time?

Enter the **`event loop`**. The event loop can be thought of as a constantly running "while" loop that waits for asynchronous operations to return a result and the schedules them to be run by the Python interpreter.

<p align="center">
  <img width="500" height="340" src="assets/event-loop.png">
</p>

## Applied Python Concurrency

We'll now get in to how to write concurrent code in Python. The first construct, which is at the heart of Python concurrency, is the **`coroutine`**.

If you're familiar with modern JavaScript, a _coroutine_ is a lot like a _promise_ (or a _future_ in Scala, a _task_ in C#, etc). For the purposes of this presentation, we'll consider it as an object that will give us a result some time in the future.

As a side note, a coroutine is actually a specialized generator function in Python, but this is also outside the scope of this presentation.

We'll start off by simply creating a coroutine:

```python
from pprint import pprint

async def something_async() -> str:
    return "I'm not really async!"

def main():
    coroutine = something_async()

    print(f"{coroutine}\n")
    pprint(dir(coroutine))

main()
```

The takeaway here is that any function we denote as **`async`** will return a coroutine, even if nothing asynchronous is actually happening.

Let's try simulating some asynchronous operation now:

```python
import asyncio

async def something_async() -> str:
    # Wait 3 seconds
    await asyncio.sleep(3)

    return "I'm async (sortof) now!"

def main():
    result = something_async()

    print(result)

main()
```

Well, we get back the same coroutine object we got before, which isn't really what we want (we want the `str` return value from the `something_async` function). The program also exits before 3 seconds elapse, which isn't what we'd expect from reading the code.

The way we get around this is by adding the **`await`** keyword:

```python
import asyncio

async def something_async() -> str:
    # Wait 3 seconds
    await asyncio.sleep(3)

    return "Now we're cooking with fire!"

async def main():
    result = await something_async()

    print(result)

asyncio.run(main())
```

A couple new things are happening here:

- We're using the **`asyncio`** library (Python's native async library)

- We're using **`await`** to wait on the results of several coroutines (**`asyncio.sleep`** also returns a coroutine under the hood)

- We're using **`asyncio.run`** to run our top level asynchronous function (this may be deprecated in the future for a top level **`await`**). This bascially interfaces with the running event loop to make it so the program doesn't exist before all async work is done

Sweet, so now we have a general idea about some of Python's async constructs and how to get some basic code to run.

Now let's take it one step further and try to do multiple asynchronous operations:

```python
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

    first_result = await me_first()
    second_result = await me_second()
    third_result = await me_third()

    end = time.perf_counter()

    print(f"It took {end - start} seconds to complete all operations")

    print(first_result)
    print(second_result)
    print(third_result)


asyncio.run(main())
```

From a functionality perspective, we get the output we want here. The results of all three operations are printed to the console.

However, the downside is that the entire program takes about 3 seconds to run, which is basically the same as if we were writing it in the traditional, synchronous way.

We need to be able to _schedule_ the operations to run concurrently and then wait on them to return:

```python
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
```

Finally, we get what we're looking for! The overall program takes about 1 second to run, and we get the output from all of our async functions as expected.

The big takeaway here is that Python can _schedule_ operations concurrently, but can't actually run them concurrently given it's single-threaded.

You'll notice the program takes a couple thousandths of a second longer than a second to run. This comes from the overhead of the other parts of the program as well as the time it takes for the event loop to do it's thing. It's still way more performant than the synchronous version.

Notably, the Python asyncio includes a whole lot more with respect to working with concurrency.

If interested, check out the docs [here](https://docs.python.org/3/library/asyncio.html) and [here](https://docs.python.org/3/library/asyncio-task.html#coroutines-and-tasks). There's a lot more to concurrency in Python than what is covered here.

# SQLAlchemy

---

Now that we have a basis in applied Python concurrency, let's talk about how it relates to one of the most popular ORMs in the Python ecosystem, [SQLAlchemy](https://www.sqlalchemy.org/).

Notably, native coroutines and the async/await syntax are still in the relatively early phases of adoption in Python. Accordingly, not all libraries are asyncio-compatible.

SQLAlchemy is no exception to this trend. As of right now, the current stable release series of [1.3.x](https://www.sqlalchemy.org/download.html#current) does not have support for asyncio.

However, the current [beta release](https://www.sqlalchemy.org/download.html#beta) and the upcoming major [2.0 release](https://docs.sqlalchemy.org/en/14/changelog/migration_20.html) have/will have full asyncio support.

Today, we'll take a look at some of that preview functionality, after going over some basic example usage of the library.

## API Overview

The first thing we'll do is create an engine with which to interact with out locally running database (I'm using MySQL):

```python
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
```

In the above, we do the following things:

- Define a connection string with all the info needed to conect to the local MySQL database (we're currently using a synchronous MySQL driver called pymsql)

- Create an "engine" which represents a connection pool we can use to make database calls. This object only needs to be instantiated once in your application

- Test the connection to make sure it's active

Great, we're connected to our database!

From here, we have a couple choices about how to use SQLAlchemy. The two ways we'll cover are the ORM pattern and raw SQL.

Starting with raw SQL, we can simply pass a MySQL compatible SQL statement to a connection directly:

```python
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
# NOTE: The "with" statment here is a context manager. It handles closing the connection
with mysql_engine.begin() as connection:
    results = connection.execute(text(sql_statement)).fetchall()
    
    pprint(results)
```

So the above executes a simple SQL statement and returns the results. This style of SQLAlchemy usage is useful for applications where writing custom SQL is necessary, either due to the complexity of queries or other business rationales.

However, for most use cases, using the ORM style query API is more intuitive:

```python
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
```

## Asynchronous SQLAlchemy


<!-- Create engine

Create models

Read data

Raw SQL

Asyncio version -->
