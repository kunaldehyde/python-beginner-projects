#Parameters to check: Height, Age, want_photo and provide pricing accordingly.
#People aged 45-55 to be given a free ride due to midlife crises.
#Classify age into multiple groups

print("Welcome to the roller coaster ride booking.")
height = int(input("Please enter your height: "))
bill = 0

if height < 120:
    print("Sorry! You cannot ride the roller coaster.")
else:
    age = int(input("Please enter your age: "))
    if age <= 10:
        print("Sorry! You are not old enough to ride the roller coaster.")
    else:
        if age <= 18:
            bill = 5
        elif age < 45:
            bill = 10
        elif age <= 55:
            print("You get a free ride. Everything will be fine.")
        else:
            bill = 7

        photo = input("Would you like a photograph as well? Type Yes or No: ").lower()
        if photo == "yes":
            bill += 2
        elif photo == "no":
            pass
        else:
            print("Invalid response. Please try again using Yes or No.")
            exit()

        if bill == 0:
            print("You don't have to pay anything.")
        else:
            print(f"Your total bill is ${bill}.")




