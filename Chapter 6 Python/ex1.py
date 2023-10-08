# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 16:40:35 2023

@author: natha
"""
"""
Chapter 6 - Exercise 1: Pizza Toppings

Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping,

print a message saying you’ll add that topping to their pizza.
"""
#make a varaible tha is prompting for user to enter there toppings
pizza = "\nhi! what toppings do you like on your pizza?\nenter quit when you are done"

# Create a loop that prompts the user to enter pizza toppings until they enter 'quit'
while True:
    toppings = input(pizza)
    # Check if the user wants to quit
    if toppings != "quit":
        print(f"okay i'll add " +toppings+ "to your pizza")
    else:
        print("Pizza now making")
        break