"""
O exercício consiste em criar um código do jogo FizzBuzz.
As regras são:
1) Se o número for divisível por 3, o terminal deve imprimir 'Fizz'
2) Se o número for divisível por 5, o terminal deve imprimir 'Buzz'
3) Se o número for divisível por 3 e por 5, o terminal deve imprimir 'FizzBuzz'
"""

for num in range (1, 101):
    if ((num % 3 == 0) and (num % 5 == 0)):
        print("FizzBuzz")
    elif (num % 3 == 0):
        print("Fizz")
    elif (num % 5 == 0):
        print("Buzz")
    else:
        print(num)