# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 21:05:39 2023

@author: natha

Chapter 2 - Exercise 3: Stripping Names


Tidy up the code to make it easier to understand

Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, “\t” and “\n”, at least once.

Print the name once, so the whitespace around the name is displayed.

Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().


"""

# put a variable and add string with leading and trailing whitespaces
name = "\tNathan Bartolo\n"

# Print the original string
print("Raw:")
print(name)

# Using lstrip() to remove leading whitespaces
print("\nUsing lstrip():")
print(name.lstrip())

# Using rstrip() to remove trailing whitespaces
print("\nUsing rstrip():")
print(name.rstrip())

# Using strip() to remove leading and trailing whitespaces
print("\nUsing strip():")
print(name.strip())