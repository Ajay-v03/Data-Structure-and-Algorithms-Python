'''Chaining Collision detection techniques'''
# chaining(tuple(key,val)) store in same memory location of two items
# Linear probing(tuple(key,val)) store in empty bucket in memory while 1st element is already present in memory where 2nd element is target. 

class HashTable:
    def __init__(self):
        self.Max = 10
        self.arr = [[] for i in range(self.Max)]
        
    def get_hash(self, key): #taking string and return a number that map in memory
        sum = 0
        for letter in key:
            sum += ord(letter)

        return sum % self.Max
        
    def __getitem__(self,key):
        hash_ = self.get_hash(key)
        for kv in self.arr[hash_]:
            if kv[0] == key:
                return kv[1]
    
    def __setitem__(self, key, val):
        hash_ = self.get_hash(key)
        
        found = False
        for idx, element in enumerate(self.arr[hash_]):
            if len(element) == 2 and element[0] == key:
                self.arr[hash_][idx] = (key,val)
                found = True
            
        if not found:
            self.arr[hash_].append((key,val))
            
    def __delitem__(self,key):
        hash_ = self.get_hash(key)
        for idx, element in enumerate(self.arr[hash_]):
            if element[0] == key:
                del self.arr[hash_][idx]        
        


if __name__ == '__main__':
    hash_ = HashTable()
    hash_.get_hash('march 6')

    hash_['march 6'] = 34
    hash_['march '] = 88
    hash_['march 7'] = 23
    hash_['march 8'] = 78
    hash_['march 9'] = 99
    hash_['march 17'] = 33

    print(hash_['march 17'])

    print(hash_.arr)
    del hash_['march 17']
    print(hash_.arr)



