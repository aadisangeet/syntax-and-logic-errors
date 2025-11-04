# main.py

from utils.math_operations import add, subtract, multiply, divide
from utils.string_operations import concatenate_and_reverse

def main()
    # Syntax error: Missing colon (:) after the function definition above.

    print("Welcome to the buggy Python project!")
    num1 = int(input("Enter first integer: "))
    num2 = int(input("Enter second integer: "))
    text1 = input("Enter first string: ")
    text2 = input("Enter second string: ")

    # Performing math operations
    print(f"The sum is: {add(num1, num2)}")
    print(f"The difference is: {subtract(num1, num2)}")
    print(f"The product is: {multiply(num1, num2)}")
    print(f"The quotient is: {divide(num1, num2)}")

    # String operations
    print(f"Concatenated and reversed string: {concatenate_and_reverse(text1, text2)}")

if __name__ == "__main__":
    main()
