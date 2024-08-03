#Write a program to create the tree and display the elements.
class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

def display_tree(node, level=0):
    print("  " * level + str(node.data))
    for child in node.children:
        display_tree(child, level + 1)

# Create the tree structure
root = Node("Root")
child1 = Node("Child 1")
child2 = Node("Child 2")
child3 = Node("Child 3")

root.add_child(child1)
root.add_child(child2)
child2.add_child(child3)

# Display the tree elements
display_tree(root)
