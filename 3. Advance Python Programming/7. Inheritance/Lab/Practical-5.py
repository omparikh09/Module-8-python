"""
Hybrid inheritance
"""

# Parent class
class A:
    def feature_a(self):
        print("Feature A from Class A")

# Single inheritance
class B(A):
    def feature_b(self):
        print("Feature B from Class B")

# Another base class
class C:
    def feature_c(self):
        print("Feature C from Class C")

# Multiple inheritance
class D(B, C):
    def feature_d(self):
        print("Feature D from Class D")

# Creating an object of Class D

obj = D()

obj.feature_a()  # Inherited from A via B

obj.feature_b()  # Inherited from B

obj.feature_c()  # Inherited from C

obj.feature_d()  # Own method in D