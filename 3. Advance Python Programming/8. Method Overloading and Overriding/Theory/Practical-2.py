"""
Write Python programs to demonstrate method overriding.
"""

class Parent:
    def show_message(self):
        print("Message from Parent")

class Child(Parent):
    def show_message(self): # Overriding the method
        print("Message from Child")

obj = Child()
obj.show_message()