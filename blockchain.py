import datetime 
import hashlib 
from datetime import datetime

class Block: 
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index 
        self.timestamp = timestamp 
        self.data = data 
        self.previous_hash = previous_hash 
        self.hash = self.hash_block() 
    def hash_block(self): 
        sha = hashlib.sha256() 
        data = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash) 
        sha.update(data.encode('utf-8'))
        return sha.hexdigest()

def create_genesis_block(): 
    return Block(0, datetime.now(), "Genesis Block", "0")

def next_block(last_block):
    this_index = last_block.index + 1 
    this_timestamp = datetime.now() 
    this_data = "Block Data : " + str(this_index) 
    this_hash = last_block.hash 
    return Block(this_index, this_timestamp, this_data, this_hash)

if __name__ == '__main__': 
    blockchain = [create_genesis_block()] 
    previous_block = blockchain[0]

    num_of_blocks_to_add = 20

    for i in range(0, num_of_blocks_to_add): 
        block_to_add = next_block(previous_block) 
        blockchain.append(block_to_add) 
        previous_block = block_to_add 
        print("Block #{} added blockchain".format(block_to_add.index)) 
        print("Block Data: {}n".format(block_to_add.data)) 
        print("Block Hash: {}n".format(block_to_add.hash))
    
    runcheck = 'y'
    
    while(runcheck == 'y'):
        num_of_blocks_to_add += 1
        block_to_add = next_block(previous_block) 
        blockchain.append(block_to_add) 
        previous_block = block_to_add
        print("Block #{} added blockchain".format(block_to_add.index)) 
        print("Block Data: {}n".format(block_to_add.data)) 
        print("Block Hash: {}n".format(block_to_add.hash))
        runcheck = input("블럭을 추가 하시겠습니까? ")
        



