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
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use a loop (not recursion) to generate the sequence in both parts.
# - N must be a positive integer. If it is not, print an error message.
# - Each part must be implemented in its own function (see scaffold below).
#

#
# =============================================================================
def print_fibonacci(n):
    first = 0
    second = 1

    print("Fibonacci sequence:", end=" ")

    for i in range(n):
        print(first, end=" ")
        next = first + second
        first = second
        second = next

    print()


def check_fibonacci(number):
    first = 0
    second = 1

    while first < number:
        next = first + second
        first = second
        second = next

    if first == number:
        print(number, "is a Fibonacci number.")
    else:
        print(number, "is NOT a Fibonacci number.")


n = int(input("How many terms? "))

if n <= 0:
    print("Error: Number of terms must be greater than 0.")
else:
    print_fibonacci(n)

num = int(input("Enter a number to check: "))
check_fibonacci(num)
# =============================================================================

