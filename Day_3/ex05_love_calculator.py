"""
O exercício consiste em simular um indicador de afinidade do casal.
"""

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
msg = ""

name1 = name1.lower()
name2 = name2.lower()

t = name1.count("t") + name2.count("t") #3
r = name1.count("r") + name2.count("r") #2
u = name1.count("u") + name2.count("u") #2
e = name1.count("e") + name2.count("e") #3

l = name1.count("l") + name2.count("l") #1
o = name1.count("o") + name2.count("o") #3
v = name1.count("v") + name2.count("v") #0
# e = 3
true = t + r + u + e
love = l + o + v + e

true_love = str(true)+str(love)
score = int(true_love)

if score < 10 or score > 90:
    msg = f"Your score is {score}, you go together like coke and mentos."
elif 40 <= score <= 50:
    msg = f"Your score is {score}, you are alright together."
else:
    msg = f"Your score is {score}."

print(msg)

""" teste:
print(str(true)+ " " + str(love))
print(t, r, u, e)
print(l, o, v, e)
"""