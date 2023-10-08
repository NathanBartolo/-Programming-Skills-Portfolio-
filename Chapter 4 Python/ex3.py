# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 22:01:24 2023

@author: natha
"""

"""
Chapter 4 - Exercise 3: Alien Colors #3

Turn your if-else chain from Exercise 5-4 into an if-elifelse chain.

• If the alien is green, print a message that the player earned 5 points.

• If the alien is yellow, print a message that the player earned 10 points.

• If the alien is red, print a message that the player earned 15 points.

• Write three versions of this program, making sure each message is printed for the appropriate color alien.
"""
#green version
#Insert variable
alien_color = "green"

#write a if condition where the variable is true 
if alien_color == "green":
    print("niceu you just earned 5 points for shooting the aliens")

elif alien_color == "yellow":
    print("Congrats you just earned 10 points")

else :
    print("WOW this player just earned 15 points")

#yellow version
#Insert variable
alien_color = "yellow"

#write a if condition where the variable is true 
if alien_color == "green":
    print("niceu you just earned 5 points for shooting the aliens")

elif alien_color == "yellow":
    print("Congrats you just earned 10 points")

else :
    print("WOW this player just earned 15 points")
    
#red version
#Insert variable
alien_color = "red"

#write a if condition where the variable is true 
if alien_color == "green":
    print("niceu you just earned 5 points for shooting the green aliens")

elif alien_color == "yellow":
    print("Congrats you just earned 10 points for shooting the yellow alien")

else :
    print("WOW this player just earned 15 points for shootin the red alien")

