import hashlib


def hashGenerator(data):
    result = hashlib.sha256(data.encode())
    return result.hexdigest()


class Block:
    def __init__(self, data, hash, prev_hash):
        self.data = data
        self.hash = hash
        self.prev_hash = prev_hash


class Blockchain:
    def __init__(self):
        hashLast = hashGenerator('gen_last')
        hashStart = hashGenerator('gen_hash')

        genesis = Block('Bank has Rs.2000000', hashStart, hashLast)
        self.chain = [genesis]

    def add_block(self, data):
        prev_hash = self.chain[-1].hash
        hash = hashGenerator(data + prev_hash)
        block = Block(data, hash, prev_hash)
        self.chain.append(block)


# transaction for A
A = Blockchain()
A.add_block('A withdraw 500 from Bank')
A.add_block('B gives 500 to A')
A.add_block('C gives 500 to A')

for block in A.chain:
    print(block.__dict__)

# transaction for B
B = Blockchain()
B.add_block('B gives 500 to A')

for block in B.chain:
    print(block.__dict__)
# transaction for C
C = Blockchain()
C.add_block('C gives 500 to A')

for block in C.chain:
    print(block.__dict__)
