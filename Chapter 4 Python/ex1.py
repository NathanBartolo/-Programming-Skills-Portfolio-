# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 21:39:59 2023

@author: natha
"""
"""
Chapter 4 - Exercise 1: Alien Colors #1
Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.

•Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.

•Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)
"""
#Version that the if statement is true
alien_color = "yellow"

#If statement that is align with the variable
if alien_color == "yellow":
    print("Congratulations you just earned 5 points")
    
#Verion that fails the if statement
alien_color = "Red"

#If statement that has different variable
if alien_color == "green":
    print("Congrats you just earned 5 points")