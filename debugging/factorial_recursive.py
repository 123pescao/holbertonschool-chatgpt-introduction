#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer n using recursion.

    Parameters:
    n (int): A non-negative integer whose factorial is to be calculated.

    Returns:
    int: The factorial of the integer n. If n is 0, returns 1.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Ensure that the script is being run directly and the user has provided an argument
if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            num = int(sys.argv[1])  # Convert the first command-line argument to an integer
            print(factorial(num))   # Calculate and print the factorial of the provided integer
        except ValueError:
            print("Please provide a valid integer.")
    else:
        print("Usage: ./factorial_recursive.py <number>")
