"""
Write a Python program to read a name and age from the user and print a formatted output.
"""

# Take input from user 

name = input("Enter your name :- ")
age = int(input("Enter your age :- "))

# print a formatted output

print("My name is {}, I am {} years old.".format(name, age))