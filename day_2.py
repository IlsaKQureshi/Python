print("Welcome to the tip calculator! \n")
bill = input("What was the total bill? \n")
tip = input("How much tip in percentage would you like to give? \n")
people = input("How many people to split the bill? \n")

bill_as_float = float(bill)
tip_as_float = float(tip)
tip_as_percent = tip_as_float/100
tip_amount = bill_as_float * tip_as_percent
total_bill = bill_as_float + tip_amount
bill_per_person = total_bill/int(people)
round_amount = round(bill_per_person,2)

print("Each person should pay £" + str(round_amount))