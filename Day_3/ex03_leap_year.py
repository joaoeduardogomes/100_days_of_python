"""
O exercício consiste em verificar se o ano inserido pelo usuário é bissexto(leap year).
"""

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
leap = "Leap year."
not_leap = "Not leap year."

if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            print (leap)
        else:
            print(not_leap)
    else:
        print(leap)
else:
    print(not_leap)