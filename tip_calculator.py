print("Welcome to the bill calculator program.")
bill = float(input("Please enter your total bill: "))
tip = int(input("How much would you like to tip? 10%, 12% or 15%: "))
people = int(input("How many people to split the bill?: "))
tip_calc = tip / 100 * bill
final_bill = round((tip_calc + bill) / people,2)
print(f"Each person has to pay:${final_bill}")