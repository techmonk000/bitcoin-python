import hashlib 

LIMIT = 90000000000000000000000

zeros = 6

def mine_coins(block_number,transactions,prev_hash):
    for number in range(LIMIT):
        base_text = str(block_number) + transactions + prev_hash + str(number)
        hash_trial = hashlib.sha256(base_text.encode()).hexdigest()
        if hash_trial.startswith('0' * zeros):
            print(f"Hash found successfully with number: {number} ")
            return hash_trial 
    return -1 

block_number = 24 
transactions = "7638ucheufm97"
previous_hash = "3728afjhfdj88"
   
mine_coins(block_number,transactions,previous_hash)
