class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def sort_list(self):
        current = self.head
        while current:
            temp = current.next
            while temp:
                if current.data > temp.data:
                    current.data, temp.data = temp.data, current.data
                temp = temp.next
            current = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next

# Main program
dll = DoublyLinkedList()

n = int(input("Enter the number of elements: "))
print("Enter the elements:")
for _ in range(n):
    data = int(input())
    dll.append(data)

print("\nLinked List before sorting:")
dll.display()

dll.sort_list()

print("\nLinked List after sorting:")
dll.display()
