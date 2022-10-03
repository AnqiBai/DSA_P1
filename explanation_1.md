# Least Recently Used Cache

## notes

cache hit / cache miss

Lookup operations get / put / set are supposed to be fast.

When designing a cache, we also put an upper bound on the size of the cache.

## Requirements

1. Use a proper data structure to implement the cache;
2. In case of a **cache miss**, get() should return -1;
3. While putting an element in the cache, put()/set() operation must insert the element. If cache is full, the least recently used entry should be removed, and then the new element should be inserted.
4. All operations must take O(1) time.

## Costs

- space: O(n)
- get least recently used item: O(1)
- set item: O(1)

## Implementation:

The requirement is to make all operations to take O(1) time.
In order to make get() by key of O(1) time complexity, we will need some map structure.
In order to make the set() of O(1) time, and considering the set() function will add/delete element at random location from the cache sequence, we will need to use doubly linked list for the cache sequence.
So we combine doubly linked list and map for the implementation. We use a node element for each cache item, build the linked list with nodes, and use map (key-value pairs, cache item as the value) to achieve access of the cache.
