#Write a program to implement the concept of linear probing.
class LinearProbeHashTable:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * self.size
        self.values = [None] * self.size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        while self.keys[index] is not None:
            index = (index + 1) % self.size
        self.keys[index] = key
        self.values[index] = value

    def search(self, key):
        index = self.hash_function(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = (index + 1) % self.size
        return None

# Example Usage
hash_table = LinearProbeHashTable(10)
hash_table.insert(5, 'apple')
hash_table.insert(15, 'banana')
hash_table.insert(25, 'cherry')

print(hash_table.search(5))  # Output: apple
print(hash_table.search(15))  # Output: banana
print(hash_table.search(25))  # Output: cherry
print(hash_table.search(10))  # Output: None
