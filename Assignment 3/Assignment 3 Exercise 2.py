# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 20:24:39 2024

@author: alain
"""

# Given a list of characters and an integer n, generate, using recursion,
# all possible combinations of length n that contain the characters in the list.
# Example:
# Charcters=[“a”,”b”,”c”], n=2

# Output:
 
# aa
# ab
# ac
# ba
# bb
# bc
# ca
# cb
# cc

def generate_combination(list1,n,str1):
    if n == 0:
        print(str1)
        return
    for element in list1:
        generate_combination(list1,n-1,str1+element)
        
list1=['a','b','c']
n=2
str1=''

generate_combination(list1, n, str1)