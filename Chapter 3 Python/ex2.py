# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 22:06:25 2023

@author: natha

Chapter 3 - Exercise 2: Greetings


Start with the list you used in Exercise 1, but instead of just

printing each person’s name, print a message to them. The text of each message should be the same, but each message should be

personalized with the person’s name.

"""
#insert a variable to store a list of strings
names =  ["ankol","kenlee","nayumi"]

# Print a greeting for each name
print("Hello, my good friend {}".format(names[0]))
print("Hello, my good friend {}".format(names[1]))
print("Hello, my good friend {}".format(names[2]))