print("Welcome to the tip calculator program.")
bill = float(input("Total bill: "))
tip = int(input("Tip percentage: "))
people = int(input("Number of people to split the bill: "))
tip_calc = tip / 100 * bill
per_person = round((tip_calc + bill) / people,2)
print(f"Each person has to pay: ${per_person}")