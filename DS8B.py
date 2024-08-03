#Write a program to insert the element into minimum heap.
import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, num):
        heapq.heappush(self.heap, num)

# Example Usage
min_heap = MinHeap()
min_heap.insert(5)
min_heap.insert(2)
min_heap.insert(10)

print(min_heap.heap)
