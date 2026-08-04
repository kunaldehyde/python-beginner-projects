# Add pepperoni for small pizza (Y or N): +$2
# Add pepperoni for medium or large pizza (Y or N): +$3
# Add extra cheese for any size pizza (Y or N): +$1

print("Welcome to python pizza deliveries.")
size = input("Which size pizza would you like? S, M or L: ").lower()

if size == "s":
    bill = 15
elif size == "m":
    bill = 20
elif size == "l":
    bill = 25
else:
    print("Invalid input. Please try again with S, M or L")
    exit()

pepperoni = input("Would you like pepperoni on your pizza? Y or N: ").lower()
if pepperoni == "y":
    if size == "s":
        bill += 2
    elif size ==  "m" or size == "l": #using this because size=="M" or "L" is understood as elif (size == "m") or ("l"): and Python treats a non-empty piece of text i.e. "L" as True, So the whole condition becomes true even if the size is "x" or anything else.
        bill += 3
elif pepperoni == "n":
    bill += 0
else:
    print("Invalid input. Please try again with Y or N")
    exit()

cheese = input("Would you like cheese on your pizza? Y or N: ").lower()
if cheese == "y":
    bill += 2
elif cheese == "n":
    bill += 0
else:
    print("Invalid input. Please try again with Y or N")
    exit()

print(f"Your final bill is: ${bill}")
