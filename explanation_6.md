# Union and Intersection of linked lists

## Costs

- Time: O(n) (need to traverse both linked lists)
- Space: O(n) (additional sets are used to get union and intersection)

## Implementation explanation:

We have two options:

1. use additional space (sets);
2. do not use additional space, but use nested loops, which will lead to O(n^2) time.

For this implementation, option 1 is used. Actual decision would be made according to the actual data.

Also, when trying to solve this problem, I don't understand why the linked lists given have duplicate elements.
If they are representing sets, they should not have duplicate elements.
