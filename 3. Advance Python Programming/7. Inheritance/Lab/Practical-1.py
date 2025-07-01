"""
Write Python programs to Single inheritance.
"""

class Animal:
    def speak(self):
        print("Animal speaks")
    
class Dog(Animal):
    def bark(self):
        print("Dog barks")
        
# Creating an object

dog = Dog()
dog.speak() # Inherited method

dog.bark() # Own method