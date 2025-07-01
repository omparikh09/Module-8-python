"""
Write a Python program to match a word in a string using re.match().
"""

import re

text = "Python is easy to learn."
word = "Python"

match = re.match(rf'/b{word}\b',text)

if match:
    print(f"'{word}' is beginning of the string.")
else:
    print(f"'{word} is not beginning of the string.")