# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 22:12:58 2024

@author: alain
"""

# ex1:  Write a program that takes two integers from the user and outputs the range of values from this list
#       list1 = [54,76,2,4,98,100]
#       Ex: int1=20, int2=80. The program would print:
#       54
#       76

list1 = [54,76,2,4,98,100]
int1=int(input('Enter the lower limit included: '))
int2=int(input('Enter the upper limit included: '))

for element in list1:
    if int1 <= element <= int2:
        print(element)