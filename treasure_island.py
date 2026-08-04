print('''Welcome to the treasure island!
Your mission is to find the treasure.''')
choice1=input("You're at a crossroad, where do you wish to go? \n    "
              "Type \"Left\" or \"Right\": ").lower()
if choice1=="right":
    print("You fell into a hole. Game Over.")
elif choice1=="left":
    choice2=input("You've come to a lake. There is an island in the middle of the lake. \n    "
                  "Type \"Wait\" to wait for a boat. Type \"Swim\" to swim across. ").lower()
    if choice2=="swim":
        print("You get attacked by an angry trout. Game Over.")
    elif choice2=="wait":
        choice3=input("You arrive at the island unharmed. There is a house with 3 doors. \n    "
                      "One red, one yellow and one blue. Which colour do you choose? ").lower()
        if choice3=="red":
            print("It's a room full of fire. Game Over.")
        elif choice3=="blue":
            print("You enter a room of beasts. Game Over.")
        elif choice3=="yellow":
            print("You found the treasure! You Win!")
        else:
            print("Invalid input. Please try again with \"Red\", \"Blue\" or \"Yellow\": ")
    else:
        print("Invalid input. Please try again with \"Wait\" or \"Swim\": ")
else:
    print("Invalid input. Please try again with \"Left\" or \"Right\": ")

