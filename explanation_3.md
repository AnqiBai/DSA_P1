# Huffman Coding

## Requirements

- Implement Huffman encoding and decoding for strings.

## Implementation explanation:

Priority Queue is used for providing lowest frequency characters. We used Python's heapq for Priority Queue. Insertion takes O(log(n)) time, and extraction of the smallest element takes O(log(n)) time. (Since Huffman tree is a binary tree, we can use log(n) for the height of the tree.)

## Costs

Time:

- Get frequency for each character: O(n) (n is the length of the input string)
- build Huffman tree: O(klog(k)) (k is the number of distinct characters, i.e. length of the frequency array)
- encoding: O(n) (n is the length of the input string, getting the code for each char is O(1))
- decoding: O(n\*h) (n is the length of the decoded/original string, and h is the height of the Huffman tree)

Space:

- build Huffman tree: Priority Queue needs O(k), and the result tree needs O(k), so overall space is of O(k), where k is the number of distinct characters.

Characters are all leaves of the Huffman tree, and Huffman tree is a binary tree, so for a Huffman tree with 2^n leaf nodes, it has at most (2^n - 1) non-leaf nodes. Leaf nodes and non-leaf nodes are both of O(k) numbers, so the tree takes O(k) space.

## Reference:

https://www.geeksforgeeks.org/huffman-coding-greedy-algo-3/
