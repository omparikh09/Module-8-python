"""
Multilevel Inheritance
"""

class GrandParent:
    def house(self):
        print("Grandparent owns a house")
        
class Parent(GrandParent): # Inherits from Grandparent
    def car(self):
        print("Parent owns a car")
        
class Child(Parent): # Inherits from Parent
    def bike(self):
        print("Child owns a bike")
        
child = Child()

child.house() # Inherited from Grandprent 

child.car() # Inherited form Parent

child.bike() # Own method