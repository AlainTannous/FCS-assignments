# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 22:49:47 2024

@author: alain
"""

# Ex.3: Given this list: numbers = [-12, 4, 12, 25, 67]
#       write a program that repeatedly asks the user to input a number
#       and then insert that number in its correct position in the list. 
#       And then print the list. 
#       Keep asking the user to input a number until they input the value -99.
#       For example: if the user inputs 2, the list will become numbers = [-12, 2, 4, 12, 25, 67]
#       If the user then inputs 88, the list will become numbers = [-12, 2, 4, 12, 25, 67, 88]

numbers = [-12, 4, 12, 25, 67]

while True:
    num = int(input('Enter a number: '))
    
    if num == -99:
        print('Stopped')
        break
    
    numbers.append(num) #to add the number to the end of the list
    numbers.sort() #to sort

    print(numbers)
    
    