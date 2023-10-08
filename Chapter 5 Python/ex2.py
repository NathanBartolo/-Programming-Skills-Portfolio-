# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 15:33:35 2023

@author: natha
"""
"""
Chapter 5 - Exercise 2: Glossary

A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.

Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store
their meanings as values.

Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print
the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between

each word-meaning pair in your output.    
"""
# Create a glossary that has the programming terms and meanings
Glossary = {"Strings":"a data type that can input text", 
            "Variable": "Stores and assign value",
            "Float": "Number with decimal point",
            "Int": "data that is a whole number",
            "Print": "to send the output"
            }
#print each word with blank spcae bt using \n
for word, definition in Glossary.items():
    print(word + ":\n" + definition + "\n")