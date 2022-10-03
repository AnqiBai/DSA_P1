import hashlib
import time


class Block:

    def __init__(self, index, previous_block_hash, data):
        assert index
        assert previous_block_hash
        assert data
        assert index >= 1
        assert len(previous_block_hash) == 64 if index > 1 else True
        assert isinstance(data, str) and isinstance(previous_block_hash, str)
        self.index = index
        self.previoud_block_hash = previous_block_hash

        self.block_data = str(self.index) + " ** " + previous_block_hash + \
            " ** " + data
        self.hash = hashlib.sha256(self.block_data.encode('utf-8')).hexdigest()
        self.timestamp = time.strftime(
            "%a, %d %b %Y %H:%M:%S", time.gmtime())

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values


# Test Case 1 : general function test
transaction_1 = "Anna sends 2 to Mike"
transaction_2 = "Bob sends 1.23 to Anna"
transaction_3 = "Charlie sends 3 to Lisa"

block_1 = Block(1, "Initial block", transaction_1)
print(block_1.block_data)
assert block_1.index == 1
assert block_1.block_data == "1 ** Initial block ** " + "Anna sends 2 to Mike"
print(block_1.hash)
print(block_1.timestamp)
time.sleep(3)
block_2 = Block(2, block_1.hash, "--".join([transaction_2, transaction_3]))
assert block_2.previoud_block_hash == block_1.hash
assert block_2.block_data == ("2 ** " + block_1.hash +
                              " ** " + transaction_2 + "--" + transaction_3)
print(block_2.block_data)
print(block_2.hash)
print(block_2.timestamp)

# Test Case 2 : demonstrate the hash value changes a lot given a small change in the block data
transaction2_1 = "Anna sends 2 to Mike"
transaction2_2 = "Bob sends 1.33 to Anna"
transaction2_3 = "Charlie sends 3 to Lisa"

b2_1 = Block(1, "Initial block", transaction2_1)
b2_2 = Block(2, b2_1.hash, "--".join([transaction2_2, transaction2_3]))

transaction2_2 = "Bob sends 1.34 to Anna"  # changes a single digit
b3_1 = Block(1, "Initial block", transaction2_1)
b3_2 = Block(2, b3_1.hash, "--".join([transaction2_2, transaction2_3]))
assert b2_1.block_data == b3_1.block_data
assert b2_1.hash == b3_1.hash
assert b2_2.block_data != b3_2.block_data
assert b2_2.hash != b3_2.hash
datadiff = [b2_2.block_data[i] == b3_2.block_data[i]
            for i in range(len(b2_2.block_data))]
datadiff_percentage = 1 - len(
    list(filter(lambda a: a, datadiff))) / len(b2_2.block_data)  # should be small since only one digit has been changed
print("datadiff percentage: ", datadiff_percentage)
hashdiff = [b2_2.hash[i] == b3_2.hash[i]
            for i in range(len(b2_2.hash))]
hashdiff_percentage = 1 - len(
    list(filter(lambda a: a, hashdiff))) / len(b2_2.hash)
# should be large (i.e. close to 1) since the hash is expected to change a lot per any data change
print("hashdiff percentage: ", hashdiff_percentage)

# Test Case 3 : test for invalid input

b4_1 = Block(-1, "", "test")  # should raise AssertionError
