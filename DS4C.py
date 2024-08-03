#Write a program to implement the concept of Deque.
class Deque:
    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        return self.items.pop(0)

    def remove_rear(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

# Example Usage
deque = Deque()
deque.add_front(1)
deque.add_rear(2)
deque.add_front(3)
print(deque.remove_front())  # Output: 3
print(deque.remove_rear())   # Output: 2
print(deque.size())          # Output: 1
