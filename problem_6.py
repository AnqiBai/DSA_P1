class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    # Your Solution Here
    result = LinkedList()
    # corner case
    if llist_1.size() == 0 or llist_2.size == 0:
        return result
    # calculate the union
    tempset = set()
    # traverse linkedlist 1
    tNode = llist_1.head
    while tNode:
        if tNode.value not in tempset:
            tempset.add(tNode.value)
        tNode = tNode.next
    # travserse linkedlist 2
    tNode = llist_2.head
    while tNode:
        if tNode.value not in tempset:
            tempset.add(tNode.value)
        tNode = tNode.next

    for item in tempset:
        result.append(item)
    return result


def intersection(llist_1, llist_2):
    # Your Solution Here
    result = LinkedList()
    # corner case
    if llist_1.size() == 0 or llist_2.size == 0:
        return result
    # calculate the intersection
    tempset = set()
    resultset = set()
    # traverse linkedlist 1
    tNode = llist_1.head
    while tNode:
        if tNode.value not in tempset:
            tempset.add(tNode.value)
        tNode = tNode.next
    # travserse linkedlist 2 to find common elements
    tNode = llist_2.head
    while tNode:
        if tNode.value in tempset:
            # result.append(tNode.value)
            resultset.add(tNode.value)
        tNode = tNode.next
    for item in resultset:
        result.append(item)
    return result


# Test case 1
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1, linked_list_2))
print(intersection(linked_list_1, linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))
print(intersection(linked_list_3, linked_list_4))

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [1, 2]
element_2 = []

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

assert str(union(linked_list_5, linked_list_6)) in ['1 -> 2 -> ', '2 -> 1 -> ']
assert str(intersection(linked_list_5, linked_list_6)) == ''

# Test Case 2 TODO: add run time distribution analysis
linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = [2] * 10000
element_2 = [1] * 10001

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

assert str(union(linked_list_7, linked_list_8)) in ['1 -> 2 -> ', '2 -> 1 -> ']
assert str(intersection(linked_list_7, linked_list_8)) == ''
# Test Case 3
linked_list_9 = LinkedList()
linked_list_10 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_9.append(i)

for i in element_2:
    linked_list_10.append(i)

assert str(union(linked_list_9, linked_list_10)) == ''
assert str(intersection(linked_list_9, linked_list_10)) == ''
