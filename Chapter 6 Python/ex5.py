# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 18:16:33 2023

@author: natha
"""
"""
Chapter 6 - Exercise 5: No pastrami

Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code

near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all

occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.
"""

#make a list of sandwiches and also an empty list
sandwich_orders = ["egg sandwich", "chicken sandwich","bacon sandwich",
                   "pastrami","pastrami","pastrami"]
finished_sandwiches = []

print("sorry, we ran out of pastrami")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove('pastrami')
    
#make a loop that will say that  i'm making you sandwich'
print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"i'm working on your {current_sandwich}.")
    finished_sandwiches.append(current_sandwich)
#also made a loop that says the sandwich is finish
print("\n")
for sandwich in finished_sandwiches:
    print(f"I made a {sandwich}.")