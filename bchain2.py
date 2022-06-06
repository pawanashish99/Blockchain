# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 20:30:50 2022

@author: halde + Students Sachin Ashish
"""


import hashlib

class Block:
    def __init__(self, data,index, prev_index, prev_hash): #hash we create after class is constructed
        self.data = data
        self.index = index
        self.prev_index = prev_index        
        self.prev_hash = prev_hash
        
    def hash(self):
        key = hashlib.sha256()
        key.update(str(self.index).encode('utf-8'))
        key.update(str(self.data).encode('utf-8'))
        key.update(str(self.prev_hash).encode('utf-8'))
        return key.hexdigest() # let it generate hash every time



# Gen = Block("Bank has 2 Cr",100,"NA","NA") # Genesis Block

# # =============================================================================
# # Transaction Ladger
# # Bank > A 1000
# # A > B 100
# # Bank > C 2000
# # B > C 50
# # C > A 200
# # =============================================================================

# t1 = Block("Bank > A 1000",1,100,Gen.hash())
# t2 = Block("A > B 100",2,1,t1.hash())
# t3 = Block("Bank > C 2000",3,100,Gen.hash())
# t4 = Block("B > C 50",4,2,t2.hash())
# t5 = Block("C > A 200",5,3,t3.hash())


# print( t4.prev_hash)

# print(t2.hash())
# print(t2.prev_hash)

# print(t1.hash())
# print(t1.prev_hash)

# print(Gen.hash())

