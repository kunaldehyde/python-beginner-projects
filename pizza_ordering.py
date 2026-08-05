# Add pepperoni for small pizza (Y or N): +$2
# Add pepperoni for medium or large pizza (Y or N): +$3
# Add extra cheese for any size pizza (Y or N): +$2

print("Welcome to python pizza deliveries.")

size = input("Small, Medium or Large: ").lower()
bill = 0

if size == "small":
    bill += 15
elif size == "medium":
    bill += 20
elif size == "large":
    bill += 25
else:
    raise SystemExit("Invalid input.")

pepperoni = input("Pepperoni? Yes or No: ").lower()

if pepperoni == "yes" and size == "small":
    bill += 2
elif pepperoni == "yes":
    bill += 3
elif pepperoni != "no":
    raise SystemExit("Invalid input")

cheese = input("Cheese? Yes or No: ").lower()

if cheese == "yes":
    bill += 2
elif cheese != "no":
    raise SystemExit("Invalid input")

print(f"Your final bill is ${bill}.")
