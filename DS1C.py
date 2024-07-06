#### Already defined matrices
def matrix_addition(matrix1, matrix2):
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

def matrix_multiplication(matrix1, matrix2):
    return [[sum(a * b for a, b in zip(row, col)) for col in zip(*matrix2)] for row in matrix1]

def matrix_transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def print_matrix(matrix):
    for row in matrix:
        print(row)

def main():
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

    while True:
        print("\nMatrix Operations Menu:")
        print("1. Add Matrices")
        print("2. Multiply Matrices")
        print("3. Transpose Matrix")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            result = matrix_addition(matrix1, matrix2)
            print("\nMatrix Addition Result:")
            print_matrix(result)
        elif choice == 2:
            result = matrix_multiplication(matrix1, matrix2)
            print("\nMatrix Multiplication Result:")
            print_matrix(result)
        elif choice == 3:
            print("\nMatrix 1:")
            print_matrix(matrix1)
            print("\nMatrix 1 Transpose:")
            print_matrix(matrix_transpose(matrix1))
            print("\nMatrix 2:")
            print_matrix(matrix2)
            print("\nMatrix 2 Transpose:")
            print_matrix(matrix_transpose(matrix2))
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

###Taking from User 
'''
def add_matrices(matrix1, matrix2):
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

def multiply_matrices(matrix1, matrix2):
    return [[sum(a * b for a, b in zip(row, col)) for col in zip(*matrix2)] for row in matrix1]

def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def input_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = list(map(int, input().split()))
        if len(row) != cols:
            raise ValueError("Invalid input. Number of elements in a row must be equal to the number of columns.")
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(*row)

print("Enter the number of rows and columns for Matrix 1:")
rows1, cols1 = map(int, input().split())
print("Enter the elements of Matrix 1 row-wise:")
matrix1 = input_matrix(rows1, cols1)

print("Enter the number of rows and columns for Matrix 2:")
rows2, cols2 = map(int, input().split())
print("Enter the elements of Matrix 2 row-wise:")
matrix2 = input_matrix(rows2, cols2)

while True:
    print("\nMatrix Operations Menu:")
    print("1. Add Matrices")
    print("2. Multiply Matrices")
    print("3. Transpose Matrix 1")
    print("4. Transpose Matrix 2")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        if rows1 != rows2 or cols1 != cols2:
            print("Matrix dimensions do not match for addition.")
        else:
            result = add_matrices(matrix1, matrix2)
            print("Result of Matrix Addition:")
            print_matrix(result)

    elif choice == 2:
        if cols1 != rows2:
            print("Matrix dimensions are not compatible for multiplication.")
        else:
            result = multiply_matrices(matrix1, matrix2)
            print("Result of Matrix Multiplication:")
            print_matrix(result)

    elif choice == 3:
        print("Transpose of Matrix 1:")
        result = transpose_matrix(matrix1)
        print_matrix(result)

    elif choice == 4:
        print("Transpose of Matrix 2:")
        result = transpose_matrix(matrix2)
        print_matrix(result)

    elif choice == 5:
        print("Exiting the program. Thank you!")
        break

    else:
        print("Invalid choice. Please select a valid option.")
'''
