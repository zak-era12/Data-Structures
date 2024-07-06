class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next

# Create a linked list
llist = LinkedList()
n = int(input("Enter the number of elements: "))
print("Enter the elements:")
for _ in range(n):
    data = int(input())
    llist.append(data)

# Display the linked list
print("Linked List:")
llist.display()

# Search for an element
key = int(input("\nEnter the element to search: "))
if llist.search(key):
    print(f"{key} is present in the linked list.")
else:
    print(f"{key} is not present in the linked list.")
