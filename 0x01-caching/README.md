# Caching Systems in Python

This repository contains Python implementations of different caching systems:

1. [Basic Cache](#basic-cache)
2. [FIFO Cache](#fifo-cache)
3. [LIFO Cache](#lifo-cache)
4. [LRU Cache](#lru-cache)
5. [MRU Cache](#mru-cache)

## General Concepts

### What is a caching system?

A caching system is a component that stores data so that future requests for that data can be served faster. It keeps a subset of the data in a faster storage medium, reducing the time and resources required to fetch the data from the original source.

### Caching Algorithms

- **FIFO**: First In, First Out - The oldest item in the cache is removed first.
- **LIFO**: Last In, First Out - The newest item in the cache is removed first.
- **LRU**: Least Recently Used - The least recently accessed item in the cache is removed first.
- **MRU**: Most Recently Used - The most recently accessed item in the cache is removed first.

### Purpose of a caching system

The primary purpose of a caching system is to improve the performance and efficiency of data retrieval by storing frequently accessed data in a faster-accessible form.

### Limits of a caching system

Caching systems have limits such as:
- Maximum number of items that can be stored
- Eviction policies for removing items when the cache is full

## Basic Cache

### Implementation

- Inherits from `BaseCaching`
- No limit on the number of items
- Methods:
  - `put(key, item)`: Adds an item to the cache.
  - `get(key)`: Retrieves an item from the cache.

## FIFO Cache

### Implementation

- Inherits from `BaseCaching`
- Uses FIFO eviction policy
- Methods:
  - `put(key, item)`: Adds an item to the cache and evicts the oldest item if the cache is full.
  - `get(key)`: Retrieves an item from the cache.

## LIFO Cache

### Implementation

- Inherits from `BaseCaching`
- Uses LIFO eviction policy
- Methods:
  - `put(key, item)`: Adds an item to the cache and evicts the newest item if the cache is full.
  - `get(key)`: Retrieves an item from the cache.

## LRU Cache

### Implementation

- Inherits from `BaseCaching`
- Uses LRU eviction policy
- Methods:
  - `put(key, item)`: Adds an item to the cache and evicts the least recently used item if the cache is full.
  - `get(key)`: Retrieves an item from the cache.

## MRU Cache

### Implementation

- Inherits from `BaseCaching`
- Uses MRU eviction policy
- Methods:
  - `put(key, item)`: Adds an item to the cache and evicts the most recently used item if the cache is full.
  - `get(key)`: Retrieves an item from the cache.

## Requirements

- Python 3.7
- pycodestyle 2.5 for code style
- Ubuntu 18.04 LTS for testing

## How to Run

Each caching system has its own Python script. To run any script, use the following command:

```bash
./filename.py
