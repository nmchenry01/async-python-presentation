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

I find the following definition a little more pragmatic

> Asynchronous programming is a form of parallel programming that allows a unit of work to run separately from the primary application thread

A little better, but what is "parallel programming"? Let's explore some key definitions we'll need to talk meaningfully about asynchronous programming

## Key Concepts

### Threads

Depending on whether you're talking about hardware or software, there are a couple different types of "threads". At a high level, we can generalize a thread as something on your computer that can do a unit of computational work

- **Hardware Thread** - In theory, this is based off of the number of CPUs on your computer (IE, 4 CPUs = 4 hardware threads, or the ability for your computer to do 4 things at once). However, modern CPUs use something called "hyperthreading" so in practice the number of hardware threads is higher than the number of CPUs (this is outside the scope of this talk)

- **Software/OS Thread** - Your operating system (OS) has it's own abstraction of a "thread". Your OS dispatches "work" to these threads, which in turn are run on hardware threads (the hardware thread can be thought of like the "engine" that the software thread runs on)

<p align="center">
  <img width="500" height="340" src="assets/threads.png">
</p>

### Parallelism

This is the idea of performing multiple operations at the same time. Your computer has multiple CPUs and hardware threads, therefore theoretically it can (and does) do multiple things at the same time

The more precise term for spreading work over a computers CPUs is **`Multiprocessing`**. This type of parallelism is very good in the case where you have a **`CPU bound`** task, or a task where the time to complete it is mainly derived from the speed at which CPU(s) can process it

Many machine learning algorithms and other mathematically intensive computations fall in to this category

### Concurrency

Concurrency is very similar to parallelism, but with one important distinction. It suggests that tasks _can_ run at the same time (but don't necessarily have to)

Parallelism is concurrency, but not vice versa.

Many modern programming languages embrace concurrency, and it is particularly useful for addressing the inefficiences of **`I/O bound`** tasks. An I/O (input/output) bound task is one in which the time to complete it is mainly derived from the time spent waiting for some I/O operation to complete. Examples of these are reading from the local file system, making an HTTP request, or waiting on data from a database

Below is a visualization that always helps me differentiate parallelism and concurrency

<p align="center">
  <img width="500" height="340" src="assets/concurrency-vs-parallelism.jpg">
</p>

# Asynchronous Programming in Python

Moving forward, we'll talk a little more about concurrency and asynchronous programming in the context of Python

NOTE: In the interest of time, we'll skip the history and evolution of concurrency in Python. Though if you're interested, you should 100% watch this [Youtube video](https://www.youtube.com/watch?v=MCs5OvhV9S4&ab_channel=PyCon2015)

---

## So How Does Python (Conceptually) Do Concurrency?

To cut to the chase, the top half of the below diagram illustrates (at a high level) how Python does concurrency

<p align="center">
  <img width="500" height="340" src="assets/python-concurrency.jpg">
</p>

For every Python process, only one thing can be running at any given time. This is due to the fact that Python has a construct called the **`GIL`**, or _Global Interpreter Lock_

The reasoning around the existence of the GIL is outside the scope of this talk, but it's contributed both to Python's success and to some of it's current limititations

But what controls what gets to run at any particular time?

Enter the **`event loop`**. The event loop can be thought of as a constantly running "while" loop that waits for asynchronous operations to return a result and the schedules them to be run by the Python interpreter.

<p align="center">
  <img width="500" height="340" src="assets/event-loop.png">
</p>

## Applied Python Concurrency

We'll now get in to how to write concurrent code in Python. The first construct, which is at the heart of Python concurrency, is the **`coroutine`**

If you're familiar with modern JavaScript, a _coroutine_ is a lot like a _promise_ (or a _future_ in Scala, a _task_ in C#, etc). For the purposes of this presentation, we'll consider it as an object that will give us a result some time in the future

As a side note, a coroutine is actually a specialized generator function in Python, but this is also outside the scope of this presentation

We'll start off by simply creating a coroutine

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

The takeaway here is that any function we denote as **`async`** will return a coroutine, even if nothing asynchronous is actually happening

Let's try simulating something asynchronous now

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

Well, we get back the same coroutine object we got before, which isn't really what we want (we want the `str` return value from the `something_async` function).

The way we get around this is by adding the **`await`** keyword like so

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

- We're using the `asyncio` library (Python's native async library)

- We're using `await` to wait on the results of several coroutines (`asyncio.sleep` also returns a coroutine under the hood)

- We're using `asyncio.run` to run our top level asynchronous function (this may be deprecated in the future for a top level `await`)

<!-- Cover Event Loop


Applied Python Concurrency

Get down in to the nitty gritty, this is where code examples start

* Cover coroutines
* asyncio library
* async/await

This is due to the fact that, in Python, only one thread can hold the control of the Python interpreter at a time

The process that controls this is referred to as the GIL, or `Python Global Interpreter Lock`

NOTE: We won't cover legacy asynchronous programming in Python, in the interest of time

- Async/await syntax (native coroutines)

- Coroutine function vs coroutine object

- Will skip generator based coroutines

- Coroutine is a generator, but a generator is not a coroutine -->
