print("Welcome to the tip calculator.")
bill_amount = float(input("What was the total bill? $"))
no_of_people = int(input("How many people to split the bill? "))
tip_percentage = float(input("What percentage tip would you like to give? "))
each_person_bill = (bill_amount*(1 + (tip_percentage/100)))/no_of_people
print(f"Each person should pay: ${round(each_person_bill,2)}")
