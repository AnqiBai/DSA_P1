class DllNode(object):
    def __init__(self, key, value):
        self.prev = None
        self.next = None
        self.key = key
        self.value = value


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        if not isinstance(capacity, int):
            print("Invalid input. Please use an integer for LRU_Cache capacity!")
            return None
        elif capacity <= 0:
            print(
                "Invalid input. Please use a positive integer number for LRU_Cache capacity.")
        self.capacity = capacity
        self.count = 0
        self.cachemap = dict()
        # double linked list head and tail are dummy nodes
        self.DllHead = DllNode(None, None)
        self.DllTail = DllNode(None, None)
        self.DllHead.next = self.DllTail
        self.DllTail.prev = self.DllHead

    def deleteNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def addToHead(self, node):
        oldHead = self.DllHead.next
        node.next = oldHead
        oldHead.prev = node
        self.DllHead.next = node
        node.prev = self.DllHead

    def getCacheElementCount(self):
        return len(self.cachemap)

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.cachemap:
            node = self.cachemap[key]
            result = node.value
            # update the Cache since this element is used
            self.deleteNode(node)
            self.addToHead(node)
            return result
        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache.
        # If the cache is at capacity remove the oldest item.
        if key in self.cachemap:
            # update the value for the corresponding cache node
            node = self.cachemap[key]
            node.value = value
            self.deleteNode(node)
            self.addToHead(node)
        else:
            # key is not present in the cache
            node = DllNode(key, value)
            self.cachemap[key] = node
            self.addToHead(node)
            if self.count < self.capacity:
                self.count += 1
            else:
                # get the LRU node from the tail of the DLL
                tailNode = self.DllTail.prev
                # delete the LRU cache from the cache map
                del self.cachemap[tailNode.key]
                # delete the LRU node
                self.deleteNode(tailNode)


our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

# returns -1 because the cache reached it's capacity and 3 was the least recently used entry
our_cache.get(3)
our_cache.get(1)
# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
cache2 = LRU_Cache(4)
cache2.set('str1', 'html1')
cache2.set('str2', 'html2')
cache2.set('str3', 'html3')
cache2.set('str4', 'html4')
cache2.set('str1', 'html111111111111111')
assert cache2.get('str3') == 'html3'  # returns 'html3'
cache2.set('str3', 'html333333333333333')
cache2.set('str5', 'html5')
cache2.set('str6', 'html6')
# returns 'html111111111111111'
assert cache2.get('str1') == 'html111111111111111'
assert cache2.get('str2') == -1
assert cache2.get('str4') == -1
# Test Case 2
cache3 = LRU_Cache(4)
for i in range(100):
    cache3.set(i, 'value' + str(i))

assert cache3.get(None) == -1
assert cache3.count == 4
assert cache3.capacity == 4
assert cache3.get(95) == -1
assert cache3.get(96) == 'value96'
assert cache3.get(97) == 'value97'
assert cache3.get(98) == 'value98'
assert cache3.get(99) == 'value99'
# Test Case 3 - This tests against a large number, can this be treated as an edge case?
cache4 = LRU_Cache(20000)
for i in range(1500):
    cache4.set(i, 'value' + str(i))
assert cache4.capacity == 20000
assert cache4.count == 1500
assert cache4.DllTail.prev.value == 'value0'
assert cache4.DllHead.next.value == 'value1499'
assert cache4.get('1499') == -1
assert cache4.get(1499) == 'value1499'

# Test Case 4: edge case
cache5 = LRU_Cache(0)
cache6 = LRU_Cache(None)
cache7 = LRU_Cache(-1)

# Test Case 5: edge case
cache8 = LRU_Cache(1)
for i in range(1500):
    cache8.set(i, 'value' + str(i))
assert cache8.count == 1
assert cache8.capacity == 1
assert cache8.DllHead.next.value == 'value1499'
assert cache8.DllTail.prev.value == 'value1499'
