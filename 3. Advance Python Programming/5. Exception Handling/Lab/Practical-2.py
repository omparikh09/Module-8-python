"""
Write a Python program to demonstrate handling multiple exceptions.
"""

def multiple_exceptions():
    try:
        num1 = int(input("Enter a number 1 :- "))
        num2 = int(input("Enter a number 2 :- "))
        
        result = num1 / num2
        print("Result :- ",result)
        
        my_list = [10, 20, 30]
        
        index = int(input("Enter index you went to access :- "))
        print("Element at index",index,":",my_list[index])
        
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    
    except ValueError:
        print("Invalid input. Please enter a numbers.")
    
    except IndexError:
        print("Index out of range.")
    
    finally:
        print("This block is executes.")
    
multiple_exceptions()