"""
O exercício consiste em escolher aleatoriamente quem vai pagar a conta entre uma lista de nomes inseridos.
"""
# Import the random module here

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ").title().strip()
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
from random import randint

rand = randint(0, len(names) - 1)

print(f"{names[rand]} is going to buy the meal today!")