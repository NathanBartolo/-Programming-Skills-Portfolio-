# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 19:07:46 2023

@author: natha
"""
"""
Chapter 7 - Exercise 4: Large shirts

Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a

medium shirt with the default message, and a shirt of any size with a different message.

   
"""
#define a function
def make_shirt(size = "medium", message = "I love python"):
    """ summarizing the size of the shirt and the message printed on it."""
    print(f"\nI'am going to make a {size}shirt.")
    print(f"it will say {message}.")
    
## Call the 'make_shirt' function with different arguments to create different sizes and messages.      
make_shirt()
make_shirt("large", "metaverse")
make_shirt(message = "I love python", size = "small")
    
    