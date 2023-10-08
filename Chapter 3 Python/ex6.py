# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 13:51:58 2023

@author: natha

Chapter 3 - Exercise 6: Shrinking Guest List 

You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.

•Start with your program from Exercise 3-5. Add a new line that prints a message saying that you can invite only two people for dinner.

•Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.

•Print a message to each of the two people still on your list, letting them know they’re still invited.

•Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.    
"""

guests = ["ankol", "kenlee", "nayumi"]

name = guests[0].title()
print(f"{name}, I am inviting you to dinner")

name = guests[1].title()
print(f"{name}, Can you come tonight for dinner?")

name = guests[2].title()
print(f"{name}, Dinner tonight?")

name = guests[1].title()
print(f"\nSorry, {name} can't make it to dinner.")

# Replace the removed guest with a new one
guests[1] = 'leiko'

name = guests[0].title()
print(f"\n{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")

print("\nI forgot that I can only invite two people because the house is not too big")

# Pop guests from the list until only two remain
while len(guests) > 2:
    popped_guest = guests.pop()
    print(f"\nSorry, {popped_guest.title()}, I can't invite you to dinner.")

# Invite the remaining two guests
for guest in guests:
    print(f"{guest.title()}, you're still invited to dinner.")

# Empty the guest list
del guests[:]
print("My guest list is now empty:", guests)