# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 16:27:15 2023

@author: natha
"""
"""
Chapter 5 - Exercise 5: Pets

Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the

owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and asyou do, print everything you know about

each pet
"""
#Make a several dictionaries that inludes the kind of animal and the owner's name
pet1 = {"Kind":"Snake","Owner":"Fred"}
pet2 = {"Kind":"Bear","Owner":"Ankol"}
pet3 = {"Kind":"Cat","Owner":"Leiko"}

#make a list that store the three varaibles
pets = [pet1,pet2,pet3]

#make a loop that describe and explains what kind of pet and who's the owner
for pet in pets:
    kind = pet["Kind"]
    owner = pet["Owner"]
    print(f"this pet is a {kind} and its own by {owner}")