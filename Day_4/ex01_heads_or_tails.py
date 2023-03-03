"""
O exercício consiste em randomizar um cara ou coroa.
"""

#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
    
#Write the rest of your code below this line 👇
from random import randint

rand = randint(0, 1)

if (rand == 0):
    print("Tails")
elif (rand == 1):
    print("Heads")