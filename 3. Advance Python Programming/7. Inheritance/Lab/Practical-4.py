"""
Hierarchical Inheritance
"""

class Vehicle:
    def wheels(self):
        print("Vehicle has wheels")

class Car(Vehicle):  # Car inherits from Vehicle
    def doors(self):
        print("Car has doors")

class Bike(Vehicle):  # Bike also inherits from Vehicle
    def handlebars(self):
        print("Bike has handlebars")

# Creating objects
car = Car()

bike = Bike()

car.wheels()   # Inherited from Vehicle

car.doors()    # Own method

bike.wheels()  # Inherited from Vehicle

bike.handlebars()  # Own method