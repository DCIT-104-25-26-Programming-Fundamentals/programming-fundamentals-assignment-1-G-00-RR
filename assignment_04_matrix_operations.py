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
# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================

def read_matrix(rows, cols):
    m = []
    for i in range(rows):
        row_input = input(f"Enter row {i + 1}: ")
        row = [int(x) for x in row_input.split()]
        m.append(row)
    return m


def print_matrix(m):
    for row in m:
        print(*row)


def transpose(m):
    rows = len(m)
    cols = len(m[0])

    result = [[0] * rows for _ in range(cols)]   # empty matrix, dimensions swapped

    for i in range(rows):
        for j in range(cols):
            result[j][i] = m[i][j]

    return result


def add_matrices(a, b):
    rows = len(a)
    cols = len(a[0])

    result = [[0] * cols for _ in range(rows)]   # empty matrix, same size as a and b

    for i in range(rows):
        for j in range(cols):
            result[i][j] = a[i][j] + b[i][j]

    return result


def multiply_matrices(a, b):
    rows_a = len(a)
    cols_a = len(a[0])
    cols_b = len(b[0])

    result = [[0] * cols_b for _ in range(rows_a)]   # result is rows_a x cols_b

    for i in range(rows_a):
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):     # walk along row i of a, and column j of b
                total = total + a[i][k] * b[k][j]
            result[i][j] = total

    return result



print("=== PART A: Transpose ===")
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter the matrix:")
matrix = read_matrix(rows, cols)

print("Original Matrix:")
print_matrix(matrix)

print("Transposed Matrix:")
print_matrix(transpose(matrix))



print("\n=== PART B: Matrix Addition ===")
rows_b = int(input("Enter number of rows: "))
cols_b = int(input("Enter number of columns: "))

print("Enter Matrix A:")
matrix_a = read_matrix(rows_b, cols_b)

print("Enter Matrix B (same size):")
matrix_b = read_matrix(rows_b, cols_b)

print("Sum of Matrices:")
print_matrix(add_matrices(matrix_a, matrix_b))



print("\n=== PART C: Matrix Multiplication ===")
rows_m = int(input("Enter number of rows for Matrix A: "))
cols_m = int(input("Enter number of columns for Matrix A (= rows for Matrix B): "))
cols_p = int(input("Enter number of columns for Matrix B: "))

print("Enter Matrix A:")
matrix_m1 = read_matrix(rows_m, cols_m)

print("Enter Matrix B:")
matrix_m2 = read_matrix(cols_m, cols_p)   # rows of B must equal cols of A

print("Product of Matrices (A x B):")
print_matrix(multiply_matrices(matrix_m1, matrix_m2))           
# =============================================================================

