# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 22:09:47 2024

@author: alain
"""
# Write the recursive version of binary search

def binary_search_recursive(list1,key,start,end):
    # Base case: key is not found
    if start>end:
        return False

    # Calculate the middle index
    mid=(start+end)//2

    # Check if key is at mid
    if list1[mid]==key:
        return True
    # If key is greater, search the right half
    elif list1[mid]<key:
        return binary_search_recursive(list1,key,mid+1,end)
    # If key is smaller, search the left half
    else:
        return binary_search_recursive(list1,key,start,mid-1)
    
list1=[-2,4,24,32,67,99]
print(binary_search_recursive(list1,-2,0,len(list1)-1))
print(binary_search_recursive(list1,3,0,len(list1)-1))
print(binary_search_recursive(list1,24,0,len(list1)-1))
print(binary_search_recursive(list1,65,0,len(list1)-1))
print(binary_search_recursive(list1,99,0,len(list1)-1))