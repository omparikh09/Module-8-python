"""
Write Python programs to Multiple inheritance.
"""

class Parent1:
    def feature1(self):
        print("Feature from Parent 1")
        
class Parent2:
    def feature2(self):
        print("Feature from Parent 2")
        
class Child(Parent1, Parent2): # Inheriting from both
    def feature3(self):
        print("Feature unique to child")
        
# Creating an object of Child

child = Child()

child.feature1() # Inherited from Parent1

child.feature2() # Inherited from Parent1

child.feature3() # Own method