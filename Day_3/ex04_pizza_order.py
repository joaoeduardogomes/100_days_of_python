"""
O exercรญcio consiste em simular um pedido de pizza.
"""

# ๐จ Don't change the code below ๐
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# ๐จ Don't change the code above ๐

#Write your code below this line ๐
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
if (extra_cheese.upper() == "Y"):
    price += 1

print(f"Your final bill is: ${price}.")