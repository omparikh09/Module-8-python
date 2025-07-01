"""
Write a Python program to search for a word in a string using re.search().
"""

import re

text = "Pyhton is a powerful programming language."
print(text)
word = input("Enter a word you went to found in string position :- ")

match = re.search(rf'\b{word}\b',text)

if match:
    print(f"'{word}' found in the string at position {match.start()}")
else:
    print(f"'{word}' is not found in a string")