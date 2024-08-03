#Write a program to search the element using sequential search.
def sequential_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example Usage
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
target = 5
result = sequential_search(arr, target)
if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the list.")
