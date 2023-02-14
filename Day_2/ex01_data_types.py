"""
O exercício consiste em receber um valor de dois dígitos e retornar uma soma do primeiro com o segundo dígito.
"""

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

print(f"{first_digit} + {second_digit} = {first_digit + second_digit}")