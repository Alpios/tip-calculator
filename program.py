print("Welcome to the tip calculator")
total_bill=float(input("What was the total bill $"))
tip=float(input("What percentage tip would you like to give?\n"))
people=int(input("How many people to split the bill?\n"))
tip1=(tip/100)+1
bill=(total_bill/people)*tip1
bill=round(bill,2)
print(f"Each person has to pay {bill}")
