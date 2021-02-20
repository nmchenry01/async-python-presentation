# Overview

---

<p align="center">
  <img width="460" height="300" src="assets/python-pseudo.jpg">
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

- Whether you're a developer, data scientist, business analyst, etc, accessing data is a crucial part of creating impactful programs. If you use Python (and need to access data), you'll likely end up using SQLAlchemy given it's the most popular ORM (object-relational model) in the ecosystem

# Introduction to Asyncronous Programming

---

> Asynchrony, in computer programming, refers to the occurrence of events independent of the main program flow and ways to deal with such events
> These may be "outside" events such as the arrival of signals, or actions instigated by a program that take place concurrently with program execution, without the program blocking to > wait for results. -Wikipedia

## Key Concepts

Introduction to a couples of key concepts here (CPUs, CPU bound, I/O bound, etc). Non-blocking

- Parallelism

- Concurrency

- Threading

## Asyncronous Programming in Python

NOTE: We won't cover legacy asyncronous programming in Python, in the interest of time

- Async/await syntax (native coroutines)

- Coroutine function vs coroutine object

- Will skip generator based coroutines

- Coroutine is a generator, but a generator is not a coroutine
