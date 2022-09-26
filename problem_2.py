import os
from collections import deque


def find_files_under_dir(suffix: str, path: str):

    deq = deque([path])
    result = []
    while deq:
        currentNode = deq.popleft()
        if os.path.isfile(currentNode):
            if currentNode.endswith(suffix):
                result.append(currentNode)
        elif os.path.isdir(currentNode):
            expanded = os.listdir(currentNode)
            for item in expanded:
                deq.append(os.path.join(currentNode, item))

    return result


def find_files(suffix: str, path: str):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if type(suffix).__name__ != 'str' or type(path).__name__ != 'str':
        print('Invalid suffix or path type: not a string.')
        return []

    if os.path.isfile(path):
        if path.endswith(suffix):
            return [path]
        else:
            return []
    elif os.path.isdir(path):
        return find_files_under_dir(suffix, path)

    return []

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values


# Test Case 1: basic use case
path1 = './testdir'
suffix1 = 'c'
assert sorted(find_files(suffix1, path1)) == sorted([
    './testdir/subdir1/a.c', './testdir/subdir3/subsubdir1/b.c', './testdir/subdir5/a.c', './testdir/t1.c'])
# Test Case 2: incorrect input type
path2 = './testdir'
suffix2 = 1
assert find_files(suffix2, path2) == []
# Test Case 3: entered file path
path3 = './testdir/t1.c'
suffix3 = 'c'
assert find_files(suffix3, path3) == ['./testdir/t1.c']
# Test Case 4: entered file path
path4 = './testdir/t1.c'
suffix4 = 'cpp'
assert find_files(suffix4, path4) == []
# Test Case 5: test for a longer suffix
path5 = './testdir'
suffix5 = 'gitkeep'
assert sorted(find_files(suffix5, path5)) == sorted([
    './testdir/subdir2/.gitkeep', './testdir/subdir4/.gitkeep'])
