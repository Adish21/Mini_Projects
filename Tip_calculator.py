print("Welcome to the Tip Calculator")

Bill = float(input("What wa the total bill?:-  $"))
Tip = int(input("What is the percentage of tip would you like to give? 10 , 12. or 15?  "))
Split = int(input("How many people will split the bill?  "))

percent = Tip / 100
Tip_to_be_paid = Bill * percent
Total_bill = Tip_to_be_paid + Bill
Bill_per_person = Total_bill / Split
Grand_total = round(Bill_per_person,2)

print(f"Each person should pay {Grand_total}")
