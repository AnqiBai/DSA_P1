# Blockchain

## Implementation explanation:

The Blockchain class is implemented as a linked list logically.
Each block stores the hash value for previous block, and by this design, the linked list requirement is fulfilled.
We have two choices:

1. add a pointer to previous block for the block class
2. use a map in the block chain class, to map the block hash and the block object

Option 2 is used for this implementation. By using the map, we maintain access / address of all blocks.

## Costs

- space: O(n) (n is the number of blocks, this extra space complexity is from the map we use)
- time of building the block chain: O(n) (n is the number of blocks)
- time of accessing a block with it hash: O(1) (since we have a map in the blockchain)

## Reference:

https://youtu.be/pYasYyjByKI
