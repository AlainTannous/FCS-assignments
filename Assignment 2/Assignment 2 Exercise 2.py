# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 21:06:59 2024

@author: alain
"""

# Ex.2: Write a program that repeatedly asks the user for a letter, and then 
#       prints all the names in this list that contain that letter.
#       names = [“Maria”, ”Hala”, ”Ghady”, ”Ehsan”, ”Joe”, ”Zoe”]
#       Ex: letter=a, the program would output
#       Maria
#       Hala
#       Ghady
#       Ehsan

names = ['Maria', 'Hala', 'Ghady', 'Ehsan', 'Joe', 'Zoe']

while True: #this will let the code keep looping
    letter = input('Enter a letter, or enter stop to exit the program: ').lower()
    
    if letter == 'stop':
        print('We are done here')
        break #to stop loop
    
    found = False    
    for element in names:
        if letter.lower() in element.lower():
            print (element)
            found = True #set found to True if a name contains the letter
    
    if not found: #if the letter was not found after looping through all elements of the list, found will remain false
        print('Letter was not found')