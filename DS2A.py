#Write a program to create a single linked list and display the node elements in reverse order.
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

    def print_reverse(self, node):
        if node is None:
            return
        self.print_reverse(node.next)
        print(node.data)

# Create a linked list
llist = LinkedList()

# Take values from the user to create the linked list
values = input("Enter values separated by spaces: ").split()
for value in values:
    llist.append(value)

# Display the node elements in reverse order
print("Node elements in reverse order:")
llist.print_reverse(llist.head)
