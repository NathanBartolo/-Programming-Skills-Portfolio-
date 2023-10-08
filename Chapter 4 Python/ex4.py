# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 22:08:00 2023

@author: natha
"""
"""
Chapter 4 - Exercise 4: Stages of Life
Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then:

•If the person is less than 2 years old, print a message that the person is a baby.

•If the person is at least 2 years old but less than 4, print a message that the person is a toddler.

•If the person is at least 4 years old but less than 13, print a message that the person is a kid.

•If the person is at least 13 years old but less than 20, print a message that the person is a teenager.

•If the person is at least 20 years old but less than 65, print a message that the person is an adult.

•If the person is age 65 or older, print a message that the person is an elder.
"""

age = 17

if age < 2:
    print("you are a baby")

elif age < 4:
    print("You are a toddler")
elif age < 13:
    print("You are a kid")
elif age < 20:
    print("you are a teenager")
else:
    print("you are an elder")