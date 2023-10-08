# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 21:43:56 2023

@author: natha
"""
"""
Chapter 4 - Exercise 2: Alien Colors #2

Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.

•If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.

•If the alien’s color isn’t green, print a statement that the player just earned 10 points.

•Write one version of this program that runs the if block and another that runs the else block.
"""
#Insert variable
alien_color = "red"

#write a if condition where the variable is true 
if alien_color == "red":
    print("niceu you just earned 5 points for shooting the aliens")
else :
    print("WOW this player just earned 10 points")


alien_color = "red"

#write a else statement that the variable is not the same in the if condition
if alien_color == "yellow":
    print("niceu you just earned 5 points for shooting the aliens")
else :
    print("WOW this player just earned 10 points")
