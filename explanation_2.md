# File Recursion

## Requirements

- find all files under a directory that have certain file extension.

## Implementation explanation:

The directory is of a tree structure, and each file is a leaf. Since we're going to find all file with certain extension, we need to check all files/directories under the given directory. So we can use DFS or BFS to solve the problem. BFS will need more space for the queue of objects to visit, while DFS will need to use recursion.

## Costs

BFS:

- space: O(n) (worst case, n is the number of nodes)
- Time: O(n) (all files need to be checked)

DFS:

- space: O(h) (h is the height of the directory tree, and this space requirement is from the function call stack.)
- Time: O(n) (all files need to be checked)
