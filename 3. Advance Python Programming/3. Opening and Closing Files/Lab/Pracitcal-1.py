"""
Write a Python program to open a file in write mode, write some text, and then close it.
"""

# Open file in write mode

file = open("Example.txt", "w")

# write some text to the file

file.write("Hello, My name is Om!\n")
file.write("I am 22 years old\n")
file.write("Currently pursuing my skills at TOPS Technologies.")

# close the file 

file.close()

print("File written Successfully!")