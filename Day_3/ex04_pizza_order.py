"""
O exercício consiste em simular um pedido de pizza.
"""

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# Size:
if (size.upper() == 'S'):
    price = 15
elif (size.upper() == 'M'):
    price = 20
elif (size.upper() == 'L'):
    price = 25

# Pepperoni
if (size.upper() == 'S' and add_pepperoni.upper() == 'Y'):
    price += 2
elif (size.upper() != 'S' and add_pepperoni.upper() == 'Y'):
    price += 3

# Extra cheese:
if (size.upper() == 'S' and extra_cheese.upper() == "Y"):
    price += 1

print(f"Your final bill is: ${price}.")