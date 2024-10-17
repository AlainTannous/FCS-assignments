# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 20:40:51 2024

@author: alain
"""

# Ex4 : Adding a number to a sorted list
# Given a sorted list of integers, and an integer value, add value to the correct position of the list.
# Example:
# Input : list1=[1,34,56,78,89], val= 77 output : list1=[1,34,56,77,78,89]
# Input : list1=[ 1,3,56,234,789], val= -99 output : list1=[-99, 1,3,56,234,789]
# Input : list1=[ 1,3,56,234,789], val= 789 output : list1=[-99, 1,3,56,234,789,789]
# Think about the best way to do this with a minimal runtime (big O value)

# Solution

# I need to append then to sort using insertion knowing that the list I have is already sorted
# so no need to do a for loop from 0 to len(list1)-1

def add_to_sorted_list(list1,number):

    list1.append(number)
    unsorted_index=len(list1)-1
    while unsorted_index > 0 and list1[unsorted_index]<list1[unsorted_index-1]: #O(n) where n is len(list1)
        
        temp=list1[unsorted_index]
        list1[unsorted_index]=list1[unsorted_index-1]
        list1[unsorted_index-1]=temp
        
        unsorted_index = unsorted_index - 1
    print(list1)
    
list1=[1,34,56,78,89]
print(list1)
add_to_sorted_list(list1,77)
add_to_sorted_list(list1,-99)
add_to_sorted_list(list1,789)
