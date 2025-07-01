"""
Write a Python program to read the contents of a file and print them on the console.
"""

# Open file in read mode

with open("Example.txt","+r") as file:
    content = file.readline() # Read in the file content 
    
    # print file content
    print(content)