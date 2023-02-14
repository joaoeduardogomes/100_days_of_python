"""
O exercício consiste em calcular os dias, semanas e meses restantes do usuário até atingir os 90 anos. O ponto de partida a ser calculado é a idade inserida.
"""
# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age = int(age)
days_left = (90 - age) * 365
weeks_left = (90 - age) * 52
months_left = (90 - age) * 12

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left until you have 90 years old.")
