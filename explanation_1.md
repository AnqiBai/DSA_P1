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
- access item: O(1)

## Implementation:

Combine linked list and hash map.
