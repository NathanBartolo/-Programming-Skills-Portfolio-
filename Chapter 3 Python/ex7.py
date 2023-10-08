# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 14:21:21 2023

@author: natha

Chapter 3 - Exercise 7: Seeing the World

Think of at least five places in the world you’d like to visit. • Store the locations in a list. Make sure the list is not in alphabetical order.

• Print your list in its original order. Don’t worry about printing the list neatly,just print it as a raw Python list.

• Use sorted() to print your list in alphabetical order without modifying the actual list.

• Show that your list is still in its original order by printing it.

• Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.

• Show that your list is still in its original order by printing it again.

• Use reverse() to change the order of your list. Print the list to show that its order has changed.

• Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.

• Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.

• Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.

   
"""

Places_to_visit_when_its_time = ["Rome","London","Japan","Singapore","Mexico"]

 #Print your list in its original order
print("Original order")
print(Places_to_visit_when_its_time)

#Print the list in alphabetical
print("\nAlphabetical order")
print(sorted(Places_to_visit_when_its_time))

print("\nOriginal order(again):")
print(Places_to_visit_when_its_time)

# Change the order of the list using reverse()
Places_to_visit_when_its_time.reverse()

print("\nreverserd order")
print(Places_to_visit_when_its_time)

#Use sort() to change your list so it’s stored in alphabetical order
Places_to_visit_when_its_time.sort()

print("\nAlphabetical order (sorted):")
print(Places_to_visit_when_its_time)

Places_to_visit_when_its_time.sort(reverse=True)

print("\nReverse alphabetical order (sorted):")
print(Places_to_visit_when_its_time)
