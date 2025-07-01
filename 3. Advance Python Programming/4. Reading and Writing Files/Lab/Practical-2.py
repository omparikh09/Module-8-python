"""
Write a Python program to write multiple strings into a file.
"""

# Open file in write mode

with open("Exmaple1.txt", "w") as file:
    # Writing multiple strings using write()
    
    file.write("Hello, Om! Learning file handling in Python.\n")
    file.write("Writing multiple strings into a file.\n\n")
    
    lines = ["-> Hello, all!\n", "How are you guys.\n", "I am fine\n"]
    file.writelines(lines)
    
    print("File written successfully!")