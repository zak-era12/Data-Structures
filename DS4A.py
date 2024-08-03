#Write a program to implement the concept of Queue with Insert, Delete, Display and Exit operations.
class Queue:
    def __init__(self):
        self.queue = []

    def insert(self, item):
        self.queue.append(item)

    def delete(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print("Deleted item:", self.queue.pop(0))

    def display(self):
        print("Queue:", self.queue)

    def exit(self):
        print("Exiting...")

def main():
    queue = Queue()
    while True:
        print("\nQueue Operations:")
        print("1. Insert")
        print("2. Delete")
        print("3. Display")
        print("4. Exit")
        choice = int(input("Enter your choice (1-4): "))

        if choice == 1:
            item = input("Enter item to insert: ")
            queue.insert(item)
        elif choice == 2:
            queue.delete()
        elif choice == 3:
            queue.display()
        elif choice == 4:
            queue.exit()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
