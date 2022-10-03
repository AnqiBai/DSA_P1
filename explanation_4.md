# Active Directory

## Requirements

- look up of whether the user is in a group.

## Costs

- space: O(h) (h is the height of the active directory tree, i.e max depth of the active directory)
- time: O(n) (worst case, we need to check all objects that are under the given directory to get to know whether the user is in the group)

## Implementation explanation:

This is a typical DFS problem.
