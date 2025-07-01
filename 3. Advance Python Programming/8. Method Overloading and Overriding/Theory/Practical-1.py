"""
Write Python programs to demonstrate method overloading and method overriding.
"""

class MethOperations:
    def add(self, a, b = 0, c = 0): # Default value 
        return a + b + c
    
# Creating object

obj = MethOperations()

print(obj.add(5)) # Calls method with one argument

print(obj.add(5, 10)) # Calls method with two argument

print(obj.add(5, 10, 15)) # Calls method with three argument