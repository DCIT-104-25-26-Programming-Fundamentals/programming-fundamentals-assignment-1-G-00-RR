# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# The Fibonacci sequence is a series of numbers where each number is the sum
# of the two numbers before it:
#
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Write a Python program with TWO parts, each implemented as a function.
#
# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
# - Ask the user how many terms (N) to display.
# - Print the first N numbers of the Fibonacci sequence on one line.
#
# Example:
#   How many terms? 7
#   Fibonacci sequence: 0 1 1 2 3 5 8
#
# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Determine whether that number is a Fibonacci number.
# - Print an appropriate message.
#
# Example:
#   Enter a number to check: 13
#   13 is a Fibonacci number.
#
#   Enter a number to check: 20
#   20 is NOT a Fibonacci number.
#
# -----------------------------------------------------------------------------
# Requirement
# -----------------------------------------------------------------------------
# - Use a loop (not recursion) to generate the sequence in both parts.
# - N must be a positive integer. If it is not, print an error message.
# - Each part must be implemented in its own function (see scaffold below).
#

#
# =============================================================================
Size = int(input("Enter the number of terms: "))

if Size <= 0:
    print("Invalid Number")
else:
    X = [0] * Size
    X[0] = 0

    if Size > 1:
        X[1] = 1

    for i in range(2, Size):
        X[i] = X[i - 1] + X[i - 2]

    results = X

    print("Fibonacci sequence:", *results)
    
def is_fibonacci(number):
    if number < 0:
        return False

    a = 0
    b = 1

    if number == a or number == b:
        return True

    while b < number:
        a, b = b, a + b
        if b == number:
            return True

    return False


target = int(input("Enter a number to check: "))

if is_fibonacci(target):
    print(f"{target} is a Fibonacci number.")
else:
    print(f"{target} is NOT a Fibonacci number.")    
    

# =============================================================================

