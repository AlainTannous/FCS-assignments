# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 20:37:45 2024

@author: alain
"""

# Ex.4: Given this string: words
#       Ask the user for two integer values and print the slice of words that fall between these numbers. 
#       Make sure these numbers are valid and will not cause errors or weird outputs.
#       Example: int1=3 int2=6 The output would be: this 

words = '''Is this the real life? Is this just fantasy? Caught in a landslide, no escape from reality Open your eyes, look up to the skies and see I'm just a poor boy, I need no sympathy Because I'm easy come, easy go, little high, little low Any way the wind blows doesn't really matter to me, to me Mama, just killed a man Put a gun against his head, pulled my trigger, now he's dead Mama, life had just begun But now I've gone and thrown it all away Mama, ooh, didn't mean to make you cry If I'm not back again this time tomorrow Carry on, carry on as if nothing really matters Too late, my time has come Sends shivers down my spine, body's aching all the time Goodbye, everybody, I've got to go Gotta leave you all behind and face the truth Mama, ooh (any way the wind blows) I don't wanna die I sometimes wish I'd never been born at all I see a little silhouetto of a man Scaramouche, Scaramouche, will you do the Fandango? Thunderbolt and lightning, very, very frightening me (Galileo) Galileo, (Galileo) Galileo, Galileo Figaro, magnifico But I'm just a poor boy, nobody loves me He's just a poor boy from a poor family Spare him his life from this monstrosity.'''

while True:

    int1 = int(input("Enter the starting integer: ")) #this will be the first index in the sliced string
    int2 = int(input("Enter the ending integer: ")) #this will be the last index inclusive in the sliced string
        
    # Check if indices are in the valid range
    if 0 <= int1 <= int2 < len(words): #len(words) would be the total number of characters in the string
        if ((int1==0) or ((int1>0) and ((words[int1-1] == ' ') or (words[int1] == ' ')))) and ((int2 == len(words)-1) or ((words[int2+1] == ' ') or (words[int2] == ' '))):
        # criteria to make sure the indices dont cut through words
            # Print the slice of characters between int1 and int2
            print(words[int1:int2+1])
            break #break the while loop
        else:
            print("The indices would cut through a word. Please choose different indices.")
            continue 

    else:
        print(f"Please enter indices between 0 and {len(words)-1} (inclusive), with the first index <= the second.")