#Write a program to implement the collision technique.
class HashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = [[] for _ in range(size)]

    def _hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self._hash_function(key)
        self.hash_table[index].append((key, value))

    def search(self, key):
        index = self._hash_function(key)
        for k, v in self.hash_table[index]:
            if k == key:
                return v
        return None

# Example Usage
ht = HashTable(10)
ht.insert(5, 'apple')
ht.insert(15, 'banana')
ht.insert(25, 'cherry')

print(ht.search(5))  # Output: 'apple'
print(ht.search(15))  # Output: 'banana'
print(ht.search(25))  # Output: 'cherry'
print(ht.search(35))  # Output: None
