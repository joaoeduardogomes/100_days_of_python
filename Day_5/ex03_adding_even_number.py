"""
O exercício consiste em somar todos os valores pares de 1 a 100.
"""

#Write your code below this row 👇
total = 0
for num in range (1, 101):
    if num % 2 == 0:
        total += num

print(total)