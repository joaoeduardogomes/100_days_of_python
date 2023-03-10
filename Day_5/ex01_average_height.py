"""
O exercício consiste em imprimir na tela a média das alturas inseridas.
"""

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights (cm) separating the entries by using only spaces: ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
total_heights = 0
counter = 0

for height in student_heights:
    total_heights += height
    counter += 1

print(f"The average height is: {round(total_heights / counter)}cm")