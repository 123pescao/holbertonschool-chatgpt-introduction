#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Decrease n to avoid an infinite loop
    return result

if __name__ == "__main__":
    if len(sys.argv) > 1:  # Check if an argument is provided
        try:
            num = int(sys.argv[1])
            print(factorial(num))
        except ValueError:
            print("Please provide a valid integer.")
    else:
        print("Usage: ./factorial.py <number>")
