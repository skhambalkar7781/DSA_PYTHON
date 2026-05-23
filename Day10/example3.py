class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index].append(key)
        
    def display(self):
        print(self.table)
        
h = HashTable(10)
h.insert(15)
h.insert(25)
h.insert(35)
h.display()
        
        