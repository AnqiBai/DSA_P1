import sys
import heapq


class TreeNode:
    def __init__(self, value, freq, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.huffCode = ''
        self.freq = freq

    def __lt__(self, other):
        return self.freq < other.freq


def huffman_build_tree(data: str):
    minheap = []
    adict = dict()
    # get distinct chars and frequency
    for char in data:
        if char not in adict:
            adict[char] = 1
        else:
            adict[char] += 1

    # handle corner case:
    if len(adict.keys()) == 1:
        lNode = TreeNode(char, adict[char])
        lNode.huffCode = '0'
        dummyRoot = TreeNode('-'+char, adict[char], lNode)
        return dummyRoot

    for char in adict:
        heapq.heappush(minheap, TreeNode(char, adict[char]))

    while len(minheap) > 1:
        left = heapq.heappop(minheap)
        right = heapq.heappop(minheap)

        left.huffCode = '0'
        right.huffCode = '1'

        newNode = TreeNode(left.value + right.value,
                           left.freq+right.freq, left, right)

        heapq.heappush(minheap, newNode)

    # return the root node of the huffman tree
    return minheap[0]


def huffman_get_codes(root, codes, path):
    newPath = path + root.huffCode
    if root.left:
        huffman_get_codes(root.left, codes, newPath)
    if root.right:
        huffman_get_codes(root.right, codes, newPath)

    # if current node is a leaf node:
    if not root.left and not root.right:
        codes[root.value] = newPath

    return


def huffman_encoding(data):
    treeRootNode = huffman_build_tree(data)
    codes = {}
    path = ''
    huffman_get_codes(treeRootNode, codes, path)
    result = ''
    for char in data:
        result += codes[char]
    return (result, treeRootNode)


def getChar(startloc, data, tree):
    node = tree
    loc = startloc
    while node.left or node.right:
        currentVal = data[loc]
        loc += 1
        if currentVal == '0':
            node = node.left
        else:
            node = node.right
    return (loc, node.value)


def huffman_decoding(data, tree):
    result = ''
    newFlag = True
    loc = 0
    steps = len(data)
    while loc < steps:
        newLoc, newChar = getChar(loc, data, tree)
        result += newChar
        loc = newLoc

    return result


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(
        sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(
        sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    # Add your own test cases: include at least three test cases
    # and two of them must include edge cases, such as null, empty or very large values

    # Test Case 1 # test for encode
    data1 = 'A'*7 + 'B'*3 + 'C'*7 + 'D'*2 + 'E'*6
    encoded, treeRoot1 = huffman_encoding(data1)
    codes1 = {}
    huffman_get_codes(treeRoot1, codes1, '')
    assert codes1['E'] == '01'
    assert codes1['D'] == '000'
    assert codes1['C'] == '11'
    assert codes1['B'] == '001'
    # Test Case 2 # test for decode
    assert getChar(0, encoded, treeRoot1)[1] == 'A'
    # Test Case 3 # encode and decode
    encoded2, treeRoot2 = huffman_encoding('Hello Huffman Coding')
    assert huffman_decoding(encoded2, treeRoot2) == 'Hello Huffman Coding'
    # Test Case 4: edge case: sentence has a single character
    encoded3, treeRoot3 = huffman_encoding('*'*10)
    assert huffman_decoding(encoded3, treeRoot3) == '*' * 10
    # Test Case 5: edge case: test with a long string
    encoded4, treeRoot4 = huffman_encoding('*'*10 + 'A'*1000000)
    assert huffman_decoding(encoded4, treeRoot4) == '*' * 10 + 'A'*1000000
