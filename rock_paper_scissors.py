rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
game=[rock, paper, scissors]
comp_choice=random.choice(game)

my_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if my_choice == 0:
    print(rock)
elif my_choice == 1:
    print(paper)
elif my_choice == 2:
    print(scissors)
else:
    print("You typed an invalid number, you lose!")

print("Computer chose:\n"+comp_choice)

if my_choice == 0:
    if comp_choice == rock:
        print("It's a tie!")
    elif comp_choice == paper:
        print("You lose!")
    elif comp_choice == scissors:
        print("You win!")


if my_choice == 1:
    if comp_choice == paper:
        print("It's a tie!")
    elif comp_choice == rock:
        print("You win!")
    elif comp_choice == scissors:
        print("You lose!")

if my_choice == 2:
    if comp_choice == scissors:
        print("It's a tie!")
    elif comp_choice == rock:
        print("You lose!")
    elif comp_choice == paper:
        print("You win!")