# utils/math_operations.py

def add(a, b):
    return a - b  # Logical error: Should return a + b.

def subtract(a, b):
    return a + b  # Logical error: Should return a - b.

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("Error: Division by zero is not allowed.")
        return None
    return a / 0  # Logical error: Should return a / b.
