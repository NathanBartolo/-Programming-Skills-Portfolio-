# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 19:00:25 2023

@author: natha
"""
"""
Chapter 7 - Exercise 3: T-shirt
Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it.

Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.
"""
#define a function
def make_shirt(size, message):
    """ summarizing the size of the shirt and the message printed on it."""
    print(f"\nI'am going to make a {size}shirt.")
    print(f"it will say {message}.")
    
## Call the 'make_shirt' function with different arguments to create two shirts.    
make_shirt("large", "metaverse")
make_shirt(message = "I love python", size = "large")
    
    