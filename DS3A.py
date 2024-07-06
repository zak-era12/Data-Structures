#3A-Write a program to implement the concept of Stack with Push, Pop, Display and Exit operations.
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            return "Underflow"
        return self.stack.pop()

    def display(self):
        print(self.stack)

    def exit(self):
        return "Exiting..."

def main():
    stack = Stack()
    while True:
        print("Choose an operation:")
        print("1. Push")
        print("2. Pop")
        print("3. Display")
        print("4. Exit")
        choice = int(input())
        if choice == 1:
            item = int(input("Enter the item to push: "))
            stack.push(item)
        elif choice == 2:
            print("Popped item:", stack.pop())
        elif choice == 3:
            stack.display()
        elif choice == 4:
            print(stack.exit())
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
