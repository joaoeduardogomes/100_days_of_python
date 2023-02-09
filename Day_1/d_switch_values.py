#Questão comum de ser perguntada em entrevistas.
a = input("a: ")
b = input("b: ")

c = a #primeiro criamos uma variável extra
a = b
b = c

print(f"a = {a}")
print(f"b = {b}")