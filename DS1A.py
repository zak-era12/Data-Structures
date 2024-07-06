def search_element(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

def sort_array(arr):
    return sorted(arr)

def reverse_array(arr):
    return arr[::-1]

arr = []

while True:
    print("\n1. Insert Element")
    print("2. Search Element")
    print("3. Sort Array")
    print("4. Reverse Array")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        element = int(input("Enter element to insert: "))
        arr.append(element)
        print("Element inserted successfully!")
    elif choice == 2:
        x = int(input("Enter element to search: "))
        index = search_element(arr, x)
        if index != -1:
            print(f"Element found at index {index}")
        else:
            print("Element not found in the array")
    elif choice == 3:
        arr = sort_array(arr)
        print("Array sorted successfully!")
        print(arr)
    elif choice == 4:
        arr = reverse_array(arr)
        print("Array reversed successfully!")
        print(arr)
    elif choice == 5:
        break
    else:
        print("Invalid choice. Please try again.")
