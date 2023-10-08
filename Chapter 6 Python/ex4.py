# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 17:57:52 2023

@author: natha
"""
"""
Chapter 6 - Exercise 4: Deli

Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches.

Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is made,

move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.
"""
#make a list of sandwiches and also an empty list
sandwich_orders = ["egg sandwich", "chicken sandwich","bacon sandwich"]
finished_sandwiches = []

#make a loop that will say that  i'm making you sandwich'
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"i'm working on your {current_sandwich}.")
    finished_sandwiches.append(current_sandwich)
#also made a loop that says the sandwich is finish
print("\n")
for sandwich in finished_sandwiches:
    print(f"i made a {sandwich}.")