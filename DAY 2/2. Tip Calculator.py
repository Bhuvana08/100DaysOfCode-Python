print("Welcome to Tip Calculator!")
total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15 ? "))
people = int(input("how many people to split the bill? "))
tip_percentage = total_bill * (tip/100)
total_bill = total_bill+tip_percentage
amt_per_person = round(total_bill/people,2)
print(f"Each person should pay : ${amt_per_person}")
