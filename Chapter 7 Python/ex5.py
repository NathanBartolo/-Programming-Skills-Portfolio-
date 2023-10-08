# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 19:17:40 2023

@author: natha
"""
"""
Chapter 7 - Exercise 5: Cities

Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence,

such as Reykjavik is in Iceland. Give the parameter for the country a default value.

Call your function for three different cities, at least one of which is not in the default country.
"""
#define a function
def describe_city(city,country = "Philippines"):
    """ put a message that describe a city and its country"""
    print(f"{city} is in {country}")
# Call the 'describe_city' function with different arguments to describe cities and their countries.   
describe_city("Manila")
describe_city("Dubai","UAE")
describe_city("Cebu")

