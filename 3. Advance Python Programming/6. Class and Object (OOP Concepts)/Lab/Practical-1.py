"""
Write a Python program to create a class and access its properties using an object.
"""

# Defining the class

class Person:
    def __init__(self, name, age):
        self.name = name # Attribute
        
        self.age = age 
        
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
            
# Creating an object

person1 = Person("Om", 22)

# Accessing attributes

print(f"Person's Name :- {person1.name}")
print(f"Person's Age :- {person1.age}")

person1.display_info()