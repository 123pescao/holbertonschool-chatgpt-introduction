#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if len(sys.argv) > 1:
    try:
        f = factorial(int(sys.argv[1]))
        print(f)
    except ValueError:
        print("Please provide a valid integer as input.")
else:
    print("Usage: ./factorial.py <number>")
