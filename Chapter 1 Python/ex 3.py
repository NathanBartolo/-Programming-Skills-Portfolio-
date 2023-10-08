# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 23:31:59 2023

@author: natha
"""
"""
Chapter 1 - Exercise 3 : Print date and Time

Write a Python program to display the current date and time.
"""
import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))