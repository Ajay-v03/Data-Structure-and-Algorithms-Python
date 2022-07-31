'''This class and function shows How Dictionary Works In Python'''
# hash function implementation
class HashTable:
    def __init__(self):
        self.Max = 100
        self.arr = [None]*self.Max
        
    def get_hash(self, key): #taking string and return a number that map in memory
        sum = 0
        for letter in key:
            sum += ord(letter)

        return sum % self.Max
        
    def __setitem__(self, key, val):
        hash_ = self.get_hash(key)
        self.arr[hash_] = val
        
    def __getitem__(self,key):
        hash_ = self.get_hash(key)
        return self.arr[hash_]
    
    def __delitem__(self,key):
        hash_ = self.get_hash(key)
        self.arr[hash_] = None
        
if __name__ == '__main__':
    hash_ = HashTable()
    hash_['march 6'] = 23232
    hash_.arr
    print(hash_['march 6'])
