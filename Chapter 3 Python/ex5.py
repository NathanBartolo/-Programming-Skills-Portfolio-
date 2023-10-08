# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 22:25:29 2023

@author: natha

Chapter 3 - Exercise 5: Change Guest List

You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.

•Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.

•Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.

•Print a second set of invitation messages, one for each person who is still in your list.

   

"""

# Create a list of guest names
guest = ["ankol", "kenlee", "nayumi"]

# Invite the first guest to dinner and capitalize their name
name = guest[0].title()
print(f"{name}, I am inviting you to dinner")

# Invite the second guest to dinner and capitalize their name
name = guest[1].title()
print(f"{name}, can you come tonight for dinner?")

# Invite the third guest to dinner and capitalize their name
name = guest[2].title()
print(f"{name}, dinner tonight?")

# Apologize to the second guest who can't make it to dinner
name = guest[1].title()
print(f"\nSorry, {name} can't make it to dinner.")

# Replace the second guest with a new guest, 'leiko'
del guest[1]
guest.insert(1, 'leiko')

# Print the invitations again for the updated guest list
name = guest[0].title()
print(f"\n{name}, please come to dinner.")

name = guest[1].title()
print(f"{name}, please come to dinner.")

name = guest[2].title()
print(f"{name}, please come to dinner.")
