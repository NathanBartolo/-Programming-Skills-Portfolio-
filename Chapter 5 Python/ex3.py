# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 15:49:38 2023

@author: natha
"""
"""
Chapter 5 - Exercise 3: Glossary 2

Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print()

calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms

to your glossary.When you run your program again, these new words and meanings should automatically be included in the output.
"""

# Create a glossary that has the programming terms and meanings
Glossary = {"Strings":"a data type that can input text", 
            "Variable": "Stores and assign value",
            "Float": "Number with decimal point",
            "Int": "data that is a whole number",
            "Print": "to send the output",
            #loop is working so i added 5 more definitions
            "Function": "A reusable block of code that performs a specific task.",
            "List": "A collection if items that has been stored and it can contained different data types",
            "Loop": "A control structure that repeats a block of code as long as a certain condition is met.",
            "Conditional Statement": "A statement that controls the flow of a program based on a condition.",
            }

for word,meaning in Glossary.items():
    print(word + ":\n" + meaning + "\n")