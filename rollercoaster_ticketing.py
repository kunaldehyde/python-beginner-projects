#Parameters to check: Height, Age, want_photo and provide pricing accordingly.
#People aged 45-55 to be given a free ride due to midlife crises.
#Classify age into multiple groups

print("Welcome to the roller coaster ticketing center.")
height = int(input("Height in cms: "))
bill=0

if height < 120:
    print("Sorry! You cannot ride.")
else:
    age = int(input("Age: "))
    if age <= 10:
        print("Sorry! You cannot ride.")
    else:
        if age <= 18:
            bill += 5
        elif age < 45:
            bill += 10
        elif age <= 55:
            print("You get a free ride.") #Free ride due to midlife crises
        else:
            bill += 7 #discounted rate for sr citizens

        photo = input("Photo? Y or N: ").lower()
        if photo == "y":
            bill += 2
        elif photo != "n":
            raise SystemExit("Invalid input")

        print(f"Your ticket price is ${bill}. Thank you.")




