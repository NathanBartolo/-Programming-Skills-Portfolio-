# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 16:12:40 2023

@author: natha
"""
"""
Chapter 5 - Exercise 4: River

Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.

Use a loop to print a sentence about each river, such as The Nile runs through Egypt.

Use a loop to print the name of each river included in the dictionary.

Use a loop to print the name of each country included in the dictionary.
"""
#make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.
Major_Rivers = {"Amazon River" : "Brazil",
                "Mississippi River" : "United States",
                "Yangzte River" : "China"
                }
#print a sentence about each river, such as The Nile runs through Egypt.
for river, country in Major_Rivers.items():
    print(f"the {river} runs through the {country}")

#print the name of each river included in the dictionary.
print("\nMajor_Rivers:")
for river in Major_Rivers.keys():
    print(river)
    
#print the name of each country included in the dictionary.
print("\nMajor_Rivers:")
for river in Major_Rivers.values():
    print(river)
