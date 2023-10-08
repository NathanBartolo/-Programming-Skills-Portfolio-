# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 17:12:39 2023

@author: natha
"""
"""
Chapter 6 - Exercise 2: Movie Tickets

A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if

they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their

age, and then tell them the cost of their movie ticket
"""
#make a variable asking the user to input their age
ur_age = ("Hi! Welcome to the theater, as per theater rules, may I know your age? \n Type quit if you are finished. ")

#make a condition that determine how much will they pay depending on their age
while True:
    age = input(ur_age)
    if age == "quit":
        break
    age = int(age)
    
    if age < 3:
        print("Your are free")
    elif age > 13:
        print("you need to pay 10$")
    else:
        print("You need to pay 15$")

