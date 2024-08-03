#Write a program to insert the element into maximum heap.
import heapq

class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, num):
        heapq.heappush(self.heap, -num)

    def get_max(self):
        return -self.heap[0]

# Example Usage
max_heap = MaxHeap()
max_heap.insert(10)
max_heap.insert(20)
max_heap.insert(5)

print(max_heap.get_max())  # Output: 20
