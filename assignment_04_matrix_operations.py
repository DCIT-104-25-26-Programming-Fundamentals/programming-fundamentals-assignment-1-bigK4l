# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
def read_matrix(rows, cols):
    matrix = []

    for i in range(rows):
        row = list(map(int, input("Enter row " + str(i + 1) + ": ").split()))
        matrix.append(row)

    return matrix


def transpose(matrix):
    result = []

    for j in range(len(matrix[0])):
        row = []
        for i in range(len(matrix)):
            row.append(matrix[i][j])
        result.append(row)

    return result


def add_matrices(a, b):
    result = []

    for i in range(len(a)):
        row = []
        for j in range(len(a[0])):
            row.append(a[i][j] + b[i][j])
        result.append(row)

    return result


def multiply_matrices(a, b):
    result = []

    for i in range(len(a)):
        row = []
        for j in range(len(b[0])):
            total = 0
            for k in range(len(b)):
                total += a[i][k] * b[k][j]
            row.append(total)
        result.append(row)

    return result


def print_matrix(matrix):
    for row in matrix:
        for value in row:
            print(value, end=" ")
        print()


# ---------------- PART A ----------------
print("PART A - Transpose Matrix")
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = read_matrix(rows, cols)

print("Transposed Matrix:")
print_matrix(transpose(matrix))

# ---------------- PART B ----------------
print("\nPART B - Add Two Matrices")

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter Matrix A")
matrix1 = read_matrix(rows, cols)

print("Enter Matrix B")
matrix2 = read_matrix(rows, cols)

print("Sum Matrix:")
print_matrix(add_matrices(matrix1, matrix2))

# ---------------- PART C ----------------
print("\nPART C - Multiply Two Matrices")

m = int(input("Rows in Matrix A: "))
n = int(input("Columns in Matrix A: "))
p = int(input("Columns in Matrix B: "))

print("Enter Matrix A")
matrixA = read_matrix(m, n)

print("Enter Matrix B")
matrixB = read_matrix(n, p)

print("Product Matrix:")
print_matrix(multiply_matrices(matrixA, matrixB))
# =============================================================================

