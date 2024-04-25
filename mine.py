import hashlib 

LIMIT = 90000000000000

zeros = 4

def mine(block_number,transactions,prev_hash):
    for number in limit(LIMIT):
        base_text = str(block_number) + transactions + prev_hash + str(number)
        
   