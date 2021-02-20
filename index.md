# Overview

---

<p align="center">
  <img width="500" height="340" src="assets/python-pseudo.jpg">
</p>

## Who is this for?

- Anyone (technical) working with Python and data!

## What will be covered?

- Asyncronous Programming and Key Concepts

- Asyncronous Programming in Python

- The SQLAlchemy ORM

- Asyncronous SQLAlchemy

## Why should I care about this?

- Asyncronous programming is becomming more and more popular in the Python programming language, given the need for increased performance and to compete with other languages/runtimes that embrace the concept natively (Go, Node.js, C#, etc)

- Whether you're a developer, data scientist, business analyst, etc, accessing data is a crucial part of creating impactful programs. If you use Python (and need to access data), you'll likely end up using SQLAlchemy given it's the most popular ORM (object-relational model) in the ecosystem. Did I mention the next major release of it is going async?

# Introduction to Asyncronous Programming

---

> **Asynchrony**, in computer programming, refers to the occurrence of events independent of the main program flow and ways to deal with such events
> These may be "outside" events such as the arrival of signals, or actions instigated by a program that take place concurrently with program execution, without the program blocking to wait for results. **-Wikipedia**

<p align="center">
  <img width="500" height="340" src="assets/maths.gif">
</p>

Well that definition is certainly a mouthful...

I find the following definition a little more pragmatic

> Asynchronous programming is a form of parallel programming that allows a unit of work to run separately from the primary application thread

A little better, but what is "parallel programming"? Let's explore some key definitions we'll need to talk meaningfully about asyncronous programming

## Key Concepts

### Parallelism

This is the idea of performing multiple operations at the same time. Your computer has multiple CPUs, therefore theoretically it can (and does) do multiple things at the same time

The more precise term for spreading work over a computers CPUs is **Multiprocessing**. This type of parallelism is very good in the case where you have a **CPU bound** task, or a task where the time to complete it is mainly derived from the speed at which CPU(s) can process it

Many machine learning algorithms and other mathematically intensive computations fall in to this category

### Concurrency

Concurrency is very similar to parallelism, but with one important distinction. It suggests that tasks _can_ run at the same time (but don't necessarily have to)

Parallelism is concurrency, but not vice versa.

Programming languages like Go and C# embrace concurrency wholeheartedly, and can take advantage of multiple CPU cores (multiprocessing)

Below is a visualization that always helps me differentiate the two

<p align="center">
  <img width="500" height="340" src="assets/concurrency-vs-parallelism.jpg">
</p>

<!-- - **Concurrency** - Stuff

- **Threading** - Stuff

- **CPU Bound** - Stuff

- **I/O Bound** - Stuff

Introduction to a couples of key concepts here (CPUs, CPU bound, I/O bound, etc). Non-blocking

- Parallelism

- Concurrency

- Threading -->

## Asyncronous Programming in Python

NOTE: We won't cover legacy asyncronous programming in Python, in the interest of time

- Async/await syntax (native coroutines)

- Coroutine function vs coroutine object

- Will skip generator based coroutines

- Coroutine is a generator, but a generator is not a coroutine
