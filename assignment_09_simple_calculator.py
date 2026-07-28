# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# -----------------------------------------------------------------------------
# OPERATIONS YOUR CALCULATOR MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Addition          ( + )    e.g.  10 + 3  =  13
#   2. Subtraction       ( - )    e.g.  10 - 3  =  7
#   3. Multiplication    ( * )    e.g.  10 * 3  =  30
#   4. Division          ( / )    e.g.  10 / 3  =  3.33
#   5. Modulus           ( % )    e.g.  10 % 3  =  1  (remainder)
#   6. Exponentiation    ( ** )   e.g.  2 ** 8  =  256
#   7. Quit
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        SIMPLE CALCULATOR
#   ============================
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Modulus
#   6. Exponentiation
#   7. Quit
#   Select an operation (1-7):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Select an operation (1-7): 4
#   Enter first number : 10
#   Enter second number: 3
#   Result: 10 / 3 = 3.33
#
#   Select an operation (1-7): 4
#   Enter first number : 5
#   Enter second number: 0
#   Error: Cannot divide by zero.
#
#   Select an operation (1-7): 7
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Each arithmetic operation MUST be written as its own function.
# - Use a loop so the calculator keeps running until the user selects Quit.
# - Division by zero must be caught and handled with a clear error message
#   (do NOT let the program crash).
# - Division results should be rounded to 2 decimal places.
# - Handle invalid menu choices gracefully.
#

#
# =============================================================================
def add(a, b):
    """Returns the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Returns the difference of two numbers."""
    return a - b


def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b


def divide(a, b):
    """Returns the quotient of two numbers or an error if dividing by zero."""
    if b == 0:
        return "Error: Cannot divide by zero."
    return round(a / b, 2)


def modulus(a, b):
    """Returns the remainder of division or an error if modulus by zero."""
    if b == 0:
        return "Error: Cannot divide by zero."
    return a % b


def power(a, b):
    """Returns the result of raising base a to exponent b."""
    return a**b


def show_menu():
    """Displays the main menu options."""
    print("============================")
    print("     SIMPLE CALCULATOR")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")


def get_number(prompt):
    """Helper function to prompt and validate numeric input."""
    while True:
        try:
            val = input(prompt).strip()
            if "." in val:
                return float(val)
            return int(val)
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")


def main():
    """Main program loop."""
    while True:
        show_menu()
        choice = input("Select an operation (1-7): ").strip()

        if choice == "7":
            print("Goodbye!")
            break

        if choice not in ["1", "2", "3", "4", "5", "6"]:
            print("Error: Invalid choice. Please select a number between 1 and 7.\n")
            continue

        num1 = get_number("Enter first number : ")
        num2 = get_number("Enter second number: ")

        if choice == "1":
            res = add(num1, num2)
            print(f"Result: {num1} + {num2} = {res}\n")
        elif choice == "2":
            res = subtract(num1, num2)
            print(f"Result: {num1} - {num2} = {res}\n")
        elif choice == "3":
            res = multiply(num1, num2)
            print(f"Result: {num1} * {num2} = {res}\n")
        elif choice == "4":
            res = divide(num1, num2)
            if isinstance(res, str):
                print(f"{res}\n")
            else:
                print(f"Result: {num1} / {num2} = {res:.2f}\n")
        elif choice == "5":
            res = modulus(num1, num2)
            if isinstance(res, str):
                print(f"{res}\n")
            else:
                print(f"Result: {num1} % {num2} = {res}\n")
        elif choice == "6":
            res = power(num1, num2)
            print(f"Result: {num1} ^ {num2} = {res}\n")


if __name__ == "__main__":
    main()
# =============================================================================

