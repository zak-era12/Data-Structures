
def get_user_input():
    arr1 = list(map(int, input("Enter elements of the first array separated by space: ").split()))
    arr2 = list(map(int, input("Enter elements of the second array separated by space: ").split()))
    return arr1, arr2

def merge_sort_arrays(arr1, arr2):
    merged_array = arr1 + arr2
    sorted_array = sorted(merged_array)
    return sorted_array


def display_sorted_array(sorted_array):
    print("Sorted Array:", sorted_array)

while True:
    print("\nMenu:")
    print("1.Insert Arrays")
    print("2. Merge and Sort Arrays")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        arr1, arr2 = get_user_input()
    elif choice=='2':
        sorted_array = merge_sort_arrays(arr1, arr2)
        display_sorted_array(sorted_array)
    elif choice == '3':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
