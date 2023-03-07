"""
O projeto consiste em criar um jogo funcional de pedra, papel ou tesoura.
"""

from random import randint

def select_choice(num):
    if num == 1:
        selection = rock
    elif num == 2:
        selection = paper
    elif num == 3:
        selection = scissors

    return selection

def compare_choices(user, machine):
    if (user == machine):
        print("It's a draw!")
    elif ((user == rock and machine == scissors) or (user == paper and machine == rock) or (user == scissors and machine == paper)):
        print("You won!")
    else:
        print("You lose...")


rock = '''
    _______
---'   ____)
      (_____)   Rock
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)   Paper
          _______) 
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)   Scissors
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

print("Welcome to the Rock, Paper, Scissors game!")
print("Select the number of your choice:")
input_choice = int(input("""
    1 - Rock
    2 - Paper
    3 - Scissors
Your choice: """))

player_choice = select_choice(input_choice)
machine_choice = select_choice(randint(1, 3))

print("-="*20)

print(f"You chose: {player_choice}")
print(f"The machine chose: {machine_choice}")

compare_choices(player_choice, machine_choice)