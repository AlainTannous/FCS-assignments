# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 21:30:15 2024

@author: alain
"""

# Exercise 3: POS for a shop
# In this system, you keep track of the items available. The items have a barcode, a name, and a price.
# When the system starts, it asks the shop owner if he wants to start a new receipt.
# If he chooses yes, he will be prompted for an item barcode and the quantity the client purchased. 
# If he answers no, the system exits.
# After choosing “yes” and then inputting the barcode and the quantity
# the shop owner is asked if he would like to add another item to the list.
# If he answers yes, he is prompted again for the barcode and quantity of the item. 
# He will keep getting this prompt until he answers no to the question. 
# Once he answered no, you the system will display the receipt where each item will appear on a line along 
# with the quantity purchased and the total cost of that item (quantity*unit price) 
# and at the last line of the receipt, the system prints the total along with the total amount. 
# Once this receipt is printed, the system goes back to the first step and asks the shop owner if he would.
# like to start a new receipt.
# Use functions.

# solution

# creating a dictionary with the items in the shop. Key is the barcode, Value is a tuple with the name and price.

stock={'000':('Pencil',0.2),'001':('Pen',0.4),'002':('Copybook',2)}

def new_receipt():
    
    answer=input('Would you like to start a new receipt? y/n').lower()
    if answer=='y':
        receipt=fill_receipt()
        print_receipt(receipt)
    else:
        print('Exiting the system')
    
def fill_receipt():
    
    receipt = []
    while True:        
        barcode=input('Enter the corresponding barcode:')
        quantity=int(input('Enter the quantity purchased:'))
        item = stock.get(barcode)
        
        if item: #checks that item is available (is not none)
            name,price = item #this assigns name to the first element and price to the second element of the tuple
            total = price*quantity
            receipt.append((name,quantity,total))
        else:
            print('Item is unavailable')
            
        additional_item=input('Would you like to add another item? y/n').lower()
        if additional_item != 'y':
            break
    return receipt

def print_receipt(receipt):
    total_cost=0
    for name,quantity,total in receipt:
        print(f'{name} x {quantity} = {total}$')
        total_cost = total_cost + total
    print(f"\nTotal Cost: {total_cost}$") 
    
new_receipt()

            
            
            
            
    