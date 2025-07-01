"""
Write a Python program to handle exceptions in a simple calculator (division by zero, invalid input).
"""

def calculator():
    try:
        operation = input("Enter operation you went to perform(+, -, *, /) :- ")
        num1 = int(input("Enter a number 1 :-"))
        num2 = int(input("Enter a number 2 :-"))
        
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            result = num1 / num2
        else:
            raise ValueError("Invalid operation. Use +, -, *, or /.")

    except ZeroDivisionError:
        print("Division by zero is not allowed.")
    else:
        print("Result :- ",result)
    
calculator()